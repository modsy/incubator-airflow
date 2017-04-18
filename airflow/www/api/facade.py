import logging
from datetime import datetime
import airflow.api.auth.basic
from airflow.api.imp.dags import run_dag
from airflow.exceptions import AirflowException
from airflow.www.app import csrf

from flask import (
    g, Markup, Blueprint, redirect, jsonify, abort, request, current_app, send_file
)

_log = logging.getLogger(__name__)

api = Blueprint('api', __name__)

requires_auth = airflow.api.auth.basic.requires_auth


@api.route('/test', methods=['GET'])
def test():
    response = jsonify({'message': 'test succeeded.'})
    return response


@csrf.exempt
@api.route('/dagruns/<string:dag_id>', methods=['POST'])
@requires_auth
def trigger_dag(dag_id):
    """
    Trigger a new dag run for a Dag with an execution date of now unless
    specified in the data.
    """
    data = request.get_json(force=True)

    conf = data.get('conf', None)
    params = data.get('params', None)

    execution_date = None
    if 'execution_date' in data and data['execution_date'] is not None:
        execution_date = data['execution_date']

        # Convert string datetime into actual datetime (now)
        try:
            d = datetime.strptime(execution_date, '%Y-%m-%dT%H:%M:%S')
            execution_date = datetime(year=d.year, month=d.month, day=d.day, hour=d.hour, minute=d.minute,
                                      second=d.second, microsecond=datetime.now().microsecond)
        except ValueError:
            error_message = (
                'Given execution date, {}, could not be identified '
                'as a date. Example date format: 2015-11-16T14:34:15'
                .format(execution_date))
            _log.info(error_message)
            response = jsonify({'error': error_message})
            response.status_code = 400

            return response
    try:
        dr = run_dag(dag_id, params=params, run_id=None, conf=conf, execution_date=execution_date)
    except AirflowException as err:
        _log.error(err)
        response = jsonify(error="{}".format(err))
        response.status_code = 404
        return response

    if getattr(g, 'user', None):
        _log.info("User {} created {}".format(g.user, dr))

    response = jsonify(message="Created {}".format(dr), run_id=dr.run_id)
    return response

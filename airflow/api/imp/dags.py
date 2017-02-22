import datetime
import json
import logging
import uuid
from airflow.exceptions import AirflowException
from airflow.models import DagRun, DagBag
from airflow.utils.state import State
import airflow.settings


def run_dag(dag_id, params=None, run_id=None, conf=None, execution_date=None):
    dagbag = DagBag()

    if dag_id not in dagbag.dags:
        raise AirflowException("Dag id {} not found".format(dag_id))

    dag = dagbag.get_dag(dag_id)

    if not execution_date:
        execution_date = datetime.datetime.now()

    assert isinstance(execution_date, datetime.datetime)
    execution_date = execution_date.replace(microsecond=0)

    if not run_id:
        run_id = "api_{0}".format(uuid.uuid4().hex)

    dr = DagRun.find(dag_id=dag_id, run_id=run_id)
    if dr:
        raise AirflowException("Run id {} already exists for dag id {}".format(
            run_id,
            dag_id
        ))

    session = airflow.settings.Session()
    trigger = DagRun(
            dag_id=dag_id,
            run_id=run_id,
            execution_date=execution_date,
            state=State.RUNNING,
            conf=conf,
            params=params,
            external_trigger=True)
    session.add(trigger)
    logging.info("Created {}".format(trigger))
    session.commit()

    return trigger

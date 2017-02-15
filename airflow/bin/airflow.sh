#!/bin/bash

export AIRFLOW_HOME=/Users/jeffreybian/workspace/incubator-airflow
export DAGS_FOLDER=${AIRFLOW_HOME}/dags
export BASE_LOG_FOLDER=${AIRFLOW_HOME}/logs
export AIRFLOW_CONFIG=${AIRFLOW_HOME}/airflow.cfg
export AWS_ACCESS_KEY_ID=AKIAJNTC4BWNEPEHTIVA
export AWS_SECRET_ACCESS_KEY=IwzaYbsPkUVhfO%2BakZbnNVey9qBsYzx9KVeOARy%2B
#export BOTO_ENDPOINTS=${AIRFLOW_HOME}/endpoints.json
airflow "$@"

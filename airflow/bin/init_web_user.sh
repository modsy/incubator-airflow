#!/bin/bash

export AIRFLOW_HOME=/Users/jeffreybian/workspace/incubator-airflow
export DAGS_FOLDER=${AIRFLOW_HOME}/dags
export BASE_LOG_FOLDER=${AIRFLOW_HOME}/logs
export AIRFLOW_CONFIG=${AIRFLOW_HOME}/airflow.cfg
python ./init_credentials.py "$@"

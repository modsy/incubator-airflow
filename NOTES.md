
##Prerequisites
MySQL 5.7


Airflow Notes:

scheduler command:
The SchedulerJob will be running and run() method will be called to 
invoke _execute() which eventually will invoke _execute_task_instances()
which will fetch task instances for associated DAG and upate their states
accordingly, then it invokes executor like this,

	self.executor.queue_command(
						task_instance,
						command,
						priority=priority,
						queue=queue)
						

Note:
New in MySQL 5.7:
- MySQL 5.7 has fractional seconds support for TIME, DATETIME, and TIMESTAMP values, with up to microseconds (6 digits) precision:
which Airflow 1.8+ is based upon, need MySQL 5.7 to make migrations work.

** Installation dependencies:
yum install git libxml2-devel mysql55-devel
yum groupinstall "Development Tools"


** Install    
sudo pip install virtualenv
virtualenv venv
. venv/bin/activate
pip install --upgrade pip
pip install lxml numpy MySQL-Python celery bcrypt flask-bcrypt flower   
pip install git+https://github.com/modsy/incubator-airflow.git@dev


** Config
1)
In Airflow.cfg, modify:
executor = CeleryExecutor
sql_alchemy_conn = mysql+mysqldb://root:@localhost:3306/airflow
authenticate = True
auth_backend = airflow.contrib.auth.backends.password_auth


2) Create database
create database airflow;


3) init database
airflow initdb

4) Create password for web user
python venv/lib/python2.7/site-packages/airflow/bin/init_credentials.py jeffrey jeffrey@modsy.com


- Database: (MySQL 5.7)
dev-staging - 
User: airflow
Pass: aIr_Fl0w



Configuraion:
1. "worker_log_server_port" need to be changed per worker on same box. ( if using docker image nothing worry about)
2. AWS Keys Id should be URL quoted.
 
Under SQS semantic:
PARALLELISM is the total number of worker instances.
Specify `queue` parameter for Operators to specify which queue to use.
# Install Airflow

1. Install WSL

2. Update packages <br>
`sudo apt update && sudo apt upgrade`

3. Install dependencies <br>
`sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev` <br>
`sudo apt install build-essential zlib1g-dev libffi-dev` 

### Install Python from Source
4. Download Python 3.10 source code <br>
`wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz` 
  
5. Extract the downloaded archive <br>
`tar -xf Python-3.10.0.tgz` <br>
   
6. Navigate to the Python source directory <br>
`cd Python-3.10.0` <br>
   
7. Configure the build <br>
`./configure enable-optimizations` <br>
   
8. Build and install Python <br>
`make -j$(nproc)` <br>
`sudo make altinstall` <br>
   
9. Verify the installation <br>
`python3.10 --version` <br>
   
10. Cleanup (optional) <br>
`cd .. ` <br>
`rm -rf Python-3.10.0` <br>
`rm Python-3.10.0.tgz` <br>
 
### Install Airflow
11. Export the environment variable AIRFLOW_HOME used by Airflow to store the dags folder, logs folder and configuration file <br>
`export AIRFLOW_HOME=/usr/local/airflow` <br>

12. To check that the environment variable has been well exported <br>
`env | grep airflow` <br>
 
13. Install all tools and dependencies that can be required by Airflow <br>
`cd ..` <br>
`sudo apt-get update -y &&
sudo apt-get install -y wget libczmq-dev curl libssl-dev git inetutils-telnet bind9utils freetds-dev libkrb5-dev libsasl2-dev libffi-dev libpq-dev freetds-bin build-essential default-libmysqlclient-dev apt-utils rsync zip unzip gcc && sudo apt-get clean`

14. Create the user airflow, set its home directory to the value of AIRFLOW_HOME and log into it <br>
`useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow` <br>
 
15. Show the file /etc/passwd to check that the airflow user has been created <br>
`cat /etc/passwd | grep airflow` <br>
 
16. Upgrade pip (already installed since we use the Docker image python 3.5) <br>
`pip install --upgrade pip` <br>
 
17. Log into airflow <br>
`su airflow` <br>

18. Create the virtual env named sandbox  <br>
`python -m venv .sandbox` <br>
 
19. Activate the virtual environment sandbox <br>
`source .sandbox/bin/activate` <br>

20. Quick Start <br>
https://airflow.apache.org/docs/apache-airflow/stable/start.html <br>

21. Download the requirement file to install the right version of Airflow’s dependencies <br>
`export AIRFLOW_VERSION=2.8.1` <br>
`export PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"` <br>
`export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"` <br>
  
22. Install the version 2.0.2 of apache-airflow with all subpackages defined between square brackets. (Notice that you can still add subpackages after all, you will use the same command with different subpackages even if Airflow is already installed) <br>
https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html <br>
`pip install "apache-airflow[crypto,celery,postgres,cncf.kubernetes,docker]==${AIRFLOW_VERSION}" --constraint 
  
23. Initialise the metadatabase <br>
`airflow db init` <br>

24. Create admin user <br>
`airflow users create -u admin -f admin -l admin -r Admin -e admin@airflow.com -p admin` <br>

25. Start Airflow’s scheduler in background <br>
`airflow scheduler &` <br>

26. Start Airflow’s webserver in background <br>
`airflow webserver &` <br>


### Build a docker image from the Dockerfile in the current directory (airflow-materials/airflow-basic)  and name it airflow-basic <br>
`docker build -t airflow-basic .`
`docker run --rm -d -p 8080:8080 airflow-basic`


# Quick Tour of Airflow CLI

docker ps
#####  Show running docker containers


docker exec -it container_id /bin/bash
#####  Execute the command /bin/bash in the container_id to get a shell session


pwd
#####  Print the current path where you are


airflow db init
#####  Initialise the metadatabase


airflow db reset
#####  Reinitialize the metadatabase (Drop everything)


airflow db upgrade
#####  Upgrade the metadatabase (Latest schemas, values, ...)


airflow webserver
#####  Start Airflow’s webserver


airflow scheduler
#####  Start Airflow’s scheduler


airflow celery worker
#####  Start a Celery worker (Useful in distributed mode to spread tasks among nodes machines)


airflow dags list
#####  Give the list of known dags (either those in the examples folder or in dags folder)


ls
#####  Display the files/folders of the current directory 


airflow dags trigger example_python_operator
#####  Trigger the dag example_python_operator with the current date as execution date


airflow dags trigger example_python_operator -e 2021-01-01
#####  Trigger the dag example_python_operator with a date in the past as execution date (This won’t trigger the tasks of that dag unless you set the option catchup=True in the DAG definition)


airflow dags trigger example_python_operator -e '2021-01-01 19:04:00+00:00'
#####  Trigger the dag example_python_operator with a date in the future (change the date here with one having +2 minutes later than the current date displayed in the Airflow UI). The dag will be scheduled at that date.


airflow dags list-runs -d example_python_operator
#####  Display the history of example_python_operator’s dag runs


airflow tasks list example_python_operator
#####  List the tasks contained into the example_python_operator dag


airflow tasks test example_python_operator print_the_context 2021-01-01
#####  Allow to test a task (print_the_context) from a given dag (example_python_operator here) without taking care of dependencies and past runs. Useful for debugging.

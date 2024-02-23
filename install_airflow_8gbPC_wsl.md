# Install Airflow

1. Install WSL

2. Update packages <br>
`sudo apt update && sudo apt upgrade`

3. Install dependencies <br>
`sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev &&
sudo apt install build-essential zlib1g-dev libffi-dev &&
sudo apt-get update -y &&
sudo apt-get install -y wget libczmq-dev curl libssl-dev git inetutils-telnet bind9utils freetds-dev libkrb5-dev libsasl2-dev libffi-dev libpq-dev freetds-bin build-essential default-libmysqlclient-dev apt-utils rsync zip unzip gcc
&& sudo apt-get clean`

### Install Python from Source
4. Download Python 3.10 source code <br>
`wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz` 
  
5. Extract the downloaded archive <br>
`tar -xf Python-3.10.0.tgz` <br>
   
6. Navigate to the Python source directory <br>
`cd Python-3.10.0` <br>
   
7. Configure the build <br>
`./configure` <br>
   
8. Build and install Python <br>
`make -j$(nproc)` <br>
`sudo make altinstall` <br>
   
9. Verify the installation <br>
`python3.10 --version` <br>
   
10. Cleanup (optional) <br>
`cd .. ` <br>
`sudo rm -rf Python-3.10.0` <br>
`sudo rm Python-3.10.0.tgz` <br>
 
### Configure the Linux ambient
11. Export the environment variable AIRFLOW_HOME used by Airflow to store the dags folder, logs folder and configuration file <br>
`export AIRFLOW_HOME=/usr/local/airflow` <br>

12. To check that the environment variable has been well exported <br>
`env | grep airflow` <br>
 
13. Install all tools and dependencies that can be required by Airflow <br>
`sudo apt-get update -y &&
sudo apt-get install -y wget libczmq-dev curl libssl-dev git inetutils-telnet bind9utils freetds-dev libkrb5-dev libsasl2-dev libffi-dev libpq-dev freetds-bin build-essential default-libmysqlclient-dev apt-utils rsync zip unzip gcc && sudo apt-get clean`

14. Create the user airflow, set its home directory to the value of AIRFLOW_HOME and log into it <br>
`useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow` <br>
 
15. Show the file /etc/passwd to check that the airflow user has been created <br>
`cat /etc/passwd | grep airflow` <br>
 
16. Create a password for the airflow user <br>
`sudo passwd airflow` <br>

17. Add airflow to sudo privikeges
`sudo visudo`<br>

> `%sudo   ALL=(ALL:ALL) ALL`<br>
  Below that line, add the following line to grant sudo privileges to the 'airflow' user:
> `airflow   ALL=(ALL:ALL) ALL`<br>
 
18. Log into airflow <br>
`su airflow` <br>

19. Create airflow directory
`sudo mkdir /home/airflow &&
sudo chown airflow:airflow /home/airflow &&
cd /home/airflow` <br>

20. Create the virtual env named sandbox  <br>
`sudo apt update && sudo apt upgrade` <br>
`python3.10 -m venv .sandbox` <br>
 
21. Activate the virtual environment sandbox <br>
`source .sandbox/bin/activate` <br>

## Install Airflow 
22. Quick Start <br>
https://airflow.apache.org/docs/apache-airflow/stable/start.html <br>

23. Download the requirement file to install the right version of Airflow’s dependencies <br>
`export AIRFLOW_VERSION=2.8.1 && 
export PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)" &&
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"` <br>
  
24. Install the version 2.0.2 of apache-airflow with all subpackages defined between square brackets. (Notice that you can still add subpackages after all, you will use the same command with different subpackages even if Airflow is already installed) <br>
https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html <br>
```pip install "apache-airflow[crypto,celery,postgres,cncf.kubernetes,docker]==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"```
  
25. Initialise the metadatabase <br>
`airflow db init` <br>

26. Create admin user <br>
`airflow users create -u admin -f admin -l admin -r Admin -e admin@airflow.com -p admin` <br>

27. Start Airflow’s scheduler in background <br>
`airflow scheduler &` <br>

28. Start Airflow’s webserver in background <br>
`airflow webserver &` <br>


### Build a docker image from the Dockerfile in the current directory (airflow-materials/airflow-basic)  and name it airflow-basic <br>
`docker build -t airflow-basic .`
`docker run --rm -d -p 8080:8080 airflow-basic`


# Quick Tour of Airflow CLI

#####  Show running docker containers
`docker ps`

#####  Execute the command /bin/bash in the container_id to get a shell session
`docker exec -it container_id /bin/bash`

#####  Print the current path where you are
`pwd`

#####  Initialise the metadatabase
`airflow db init`

#####  Reinitialize the metadatabase (Drop everything)
`airflow db reset`

#####  Upgrade the metadatabase (Latest schemas, values, ...)
`airflow db upgrade`

#####  Start Airflow’s webserver
`airflow webserver`

#####  Start Airflow’s scheduler
`airflow scheduler`

#####  Start a Celery worker (Useful in distributed mode to spread tasks among nodes machines)
`airflow celery worker`

#####  Give the list of known dags (either those in the examples folder or in dags folder)
`airflow dags list`

#####  Display the files/folders of the current directory 
`ls`

#####  Trigger the dag example_python_operator with the current date as execution date
`airflow dags trigger example_python_operator`

#####  Trigger the dag example_python_operator with a date in the past as execution date (This won’t trigger the tasks of that dag unless you set the option catchup=True in the DAG definition)
`airflow dags trigger example_python_operator -e 2021-01-01`

#####  Trigger the dag example_python_operator with a date in the future (change the date here with one having +2 minutes later than the current date displayed in the Airflow UI). The dag will be scheduled at that date.
`airflow dags trigger example_python_operator -e '2021-01-01 19:04:00+00:00'`

#####  Display the history of example_python_operator’s dag runs
`airflow dags list-runs -d example_python_operator`

#####  List the tasks contained into the example_python_operator dag
`airflow tasks list example_python_operator`

#####  Allow to test a task (print_the_context) from a given dag (example_python_operator here) without taking care of dependencies and past runs. Useful for debugging.
`airflow tasks test example_python_operator print_the_context 2021-01-01`

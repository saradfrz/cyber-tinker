# Install Airflow

1. Install WSL <br>
`wsl --unregister Ubuntu-22.04` <br>
`wsl --install Ubuntu-22.04` <br>

2. Update packages <br>
`sudo apt update && sudo apt upgrade`

3. Install dependencies <br>
`sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev &&
sudo apt install build-essential zlib1g-dev libffi-dev &&
sudo apt-get update -y &&
sudo apt-get install -y wget libczmq-dev curl libssl-dev git inetutils-telnet bind9utils freetds-dev libkrb5-dev libsasl2-dev libffi-dev libpq-dev freetds-bin build-essential default-libmysqlclient-dev apt-utils rsync zip unzip gcc
&& sudo apt-get clean`

## Install Python from Source
4. Download Python 3.10 source code <br>
`wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz` 
  
5. Extract the downloaded archive <br>
`tar -xf Python-3.10.0.tgz` <br>
   
6. Navigate to the Python source directory <br>
`cd Python-3.10.0` <br>
   
7. Configure the build <br>
` ./configure --enable-optimizations` <br>
   
8. Build and install Python <br>
`make -j$(nproc)` <br>
`sudo make altinstall` <br>
   
9. Verify the installation <br>
`python3.10 --version` <br>
   
10. Cleanup (optional) <br>
`cd .. && sudo rm -rf Python-3.10.0 && sudo rm Python-3.10.0.tgz` <br>
 

## Configure the Linux ambient

11. Create the ssh keys <br>
`ssh-keygen -t ed25519 -C "your_email@example.com"`
`git config --global user.email "you@example.com"`
`git config --global user.name "Your Name"`


12. Create airflow directory <br>
`sudo mkdir /home/airflow` <br>
`sudo chmod -R 777 /home/airflow` <br>
`cd /home/airflow` <br>

13. Clone the Airflow project <br>
`git clone git@github.com:saradfrz/courses-airflow.git . `


14. Export the environment variable AIRFLOW_HOME used by Airflow to store the dags folder, logs folder and configuration file <br>
`export AIRFLOW_HOME=/home/airflow` <br>
`export AIRFLOW_VERSION=2.8.1` <br>
`export PYTHON_VERSION=3.10` <br>
`export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"` <br>

15. To check that the environment variable has been well exported <br>
`env | grep airflow` <br>
 
16. Install all tools and dependencies that can be required by Airflow <br>
`sudo apt-get update -y &&
sudo apt-get install -y wget libczmq-dev curl libssl-dev git inetutils-telnet bind9utils freetds-dev libkrb5-dev libsasl2-dev libffi-dev libpq-dev freetds-bin build-essential default-libmysqlclient-dev apt-utils rsync zip unzip gcc && sudo apt-get clean`

17. Create the user airflow, set its home directory to the value of AIRFLOW_HOME and log into it <br>
`sudo useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow` <br>
 
18. Show the file /etc/passwd to check that the airflow user has been created <br>
`cat /etc/passwd | grep airflow` <br>
 
19. Create a password for the airflow user <br>
`sudo passwd airflow` <br>

20. Add airflow to sudo privikeges <br>
`sudo visudo`<br>

> `%sudo   ALL=(ALL:ALL) ALL`<br>

  Below that line, add the following line to grant sudo privileges to the 'airflow' user:
  
> `%airflow   ALL=(ALL:ALL) ALL`<br>
 
21. Log into airflow <br>
`su airflow` <br>

22. Create the virtual env named sandbox  <br>
`sudo apt update && sudo apt upgrade` <br>
`python3.10 -m venv .sandbox` <br>
 
23. Activate the virtual environment sandbox <br>
`source .sandbox/bin/activate` <br>

## Install Airflow 
Quick Start: https://airflow.apache.org/docs/apache-airflow/stable/start.html <br>
 
24. Install the version 2.0.2 of apache-airflow with all subpackages defined between square brackets. (Notice that you can still add subpackages after all, you will use the same command with different subpackages even if Airflow is already installed) <br>

https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html <br>

```pip install "apache-airflow[crypto,celery,postgres,cncf.kubernetes,docker]==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"```
  
25. Initialise the metadatabase <br>
`airflow db migrate` <br>
`airflow connections create-default-connections` <br>

27. Create admin user <br>
`airflow users create -u admin -f admin -l admin -r Admin -e admin@airflow.com -p admin` <br>

28. Start Airflow’s scheduler in background <br>
`airflow scheduler &` <br>

29. Start Airflow’s webserver in background <br>
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

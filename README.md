# World Wide News

World Wide News is a news feeder project focused on collecting and aggregating news articles from various sources on the internet, with a primary emphasis on economy and geopolitics. The project aims to provide users with a comprehensive overview of global events and trends in these key areas.

## Features

- **News Aggregation**: Collects news articles from diverse sources across the internet.
- **Categorized Feeds**: Organizes news articles into categories such as economy and geopolitics for easy access.
- **Customizable Filters**: Allows users to customize their news feed based on their interests and preferences.
- **Search Functionality**: Enables users to search for specific news topics or keywords.
- **Real-time Updates**: Provides timely updates with the latest news developments.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

#### 1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/world-wide-news.git
    ```

#### 2. Activate WSL2 inside VSCode
- Ensure you have WSL2 installed and configured on your machine.
- Open Visual Studio Code.
- Press `Ctrl+Shift+P` to open the command palette.
- Type and select "Remote-WSL: New Window" to open a new VSCode window connected to WSL2.

#### 3. Create a virtual environment (.venv)

##### Install Python 3 and pip
sudo apt install python3 python3-pip
##### Verify Python installation
python3 --version
##### Install virtualenv using pip
sudo pip3 install virtualenv
##### Create a virtual environment named .venv
virtualenv .venv
##### Activate the virtual environment
source .venv/bin/activate
##### Verify virtual environment activation by checking Python version
python --version
##### Now you're inside the virtual environment (.venv)##### You can install packages and run Python scripts without affecting system-wide Python installation
- To deactivate the virtual environment, simply run:
deactivate

#### 4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

#### 5. Install Airflow
- With the virtual environment activated, run the following command:
  ```bash
  pip install apache-airflow
  ```

#### 6. Install PostgreSQL inside WSL2
- Update package lists:
  ```bash
  sudo apt update
  ```
- Install PostgreSQL:
  ```bash
  sudo apt install postgresql
  ```

#### 7. Configure PostgreSQL to run as the Airflow database
- Switch to the PostgreSQL user:
  ```bash
  sudo -i -u postgres
  ```
- Access the PostgreSQL shell:
  ```bash
  psql
  ```
- Create a user and database for Airflow:
  ```sql
  CREATE USER airflow_user WITH PASSWORD 'your_password';
  CREATE DATABASE airflow_db;
  GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow_user;
  ```
- Exit the PostgreSQL shell:
  ```sql
  \q
  ```
- Exit the PostgreSQL user:
  ```bash
  exit
  ```

#### 8. Create a demo DAG
- Navigate to the Airflow home directory (e.g., `~/airflow`).
- Inside the directory, create a Python script for your demo DAG (e.g., `demo_dag.py`).
- Define your DAG in the script.

#### 9. Run the DAG
- Start the Airflow scheduler and webserver:
  ```bash
  airflow scheduler &
  airflow webserver &
  ```
- Access the Airflow web interface in your browser (http://localhost:8080 by default).
- Trigger your demo DAG from the Airflow web interface.

```
## Usage

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository and create your branch from `main`.
2. Make your contributions and ensure the code follows the project's coding standards.
3. Test your changes thoroughly.
4. Create a pull request with a clear description of your changes.

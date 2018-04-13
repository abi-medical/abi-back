# ABI Back

This is abi back source code repository, build with Django1.11, PostgreSQL with a Multitenant architecture based on django-tenants-schemas.

To configure this project, please follow the next instructions:

## Instructions

### Assumptions

- You already have [python 3.6](https://www.python.org/downloads/) installed in your local machine
- You already have [git](https://git-scm.com/downloads) installed on your local machine
- You already have installed [postgresql 9.6](https://www.postgresql.org/download/) installed on your local machine

#### You can use PostgreSQL via Docker

```bash
docker run \
    --name postgres \
    -e POSTGRES_PASSWORD=<your_secret_password> \
    -v ${PWD}/pgdata:/var/lib/postgresql/data \
    -p 5432:5432 \
    -d postgres:9.6.8-alpine
```

### Create your virtualenv

#### Using virtualenvwrapper
```shell
mkvirtualenv -p python3.6 abi 
```

#### Using plain virtualenv
```shell
python -m venv abiveenv
```

### Clone the repo
```shell
git clone https://github.com/abi-medical/abi-back
```

### Install requirements
```
cd abi-back
pip install -r requirements.txt
```

#### Troubleshooting
If you're having problems with psycopg on windows, check [this page](http://www.stickpeople.com/projects/python/win-psycopg/), 
download the right .exe file and try run
  
```bash
easy_install psycopg2-2.6.2.win-<windows_architecture>-py<python_version>-pg9.5.3-release.exe
```

If you're having problems installing psycopg on ubuntu
```bash
apt install libpq-dev
```

### Configure your postgres database

Use your favorite postgreSQL client and execute the following commands 

```sql
# NoQA
CREATE role <your_role_name> noinherit login password '<your_password>';
CREATE USER <your_user_name> WITH PASSWORD '<your_password>';
GRANT <your_role_name> to <your_user_name>;
CREATE DATABASE <database_name> owner <your_user_name>;
```

### Start your django server

Before run the project for the first time you must execute the following commands

```bash
python manage.py makemigrations
python manage.py migrate_schemas --shared
```

Now as we does not want to leave database access information on our control version system
We're going to store credentials in a file `local_variables.sh`. You can get an idea of the content
looking at `local_variables.sh.copy`. Remeber that you must create your file and insert proper data

Then execute your server in this order

```bash
source local_variables.sh
ABI_DATABASE_DATABASE=${ABI_DATABASE_DATABASE} ABI_DATABASE_USERNAME=${ABI_DATABASE_USERNAME} ABI_DATABASE_PASSWORD=${ABI_DATABASE_PASSWORD} ./manage.py runserver 8000
```

## Style guides

### Before you push, make sure you git are configured to ignore all pyc files, you can configure a global gitignore 
following [this gist](https://gist.github.com/subfuzion/db7f57fff2fb6998a16c) and in your current global gitignore file put this

```
*.pyc
```

# ABI Back

This is abi back source code repository, build with Django1.11, PostgreSQL with a Multitenant architecture based on django-tenants-schemas.

To configure this project, please follow the next instructions:

## Instructions

### Assumptions

- You already have [python 3.6](https://www.python.org/downloads/) installed in your local machine
- You already have installed [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) in your main python3 environment
- You already have [git](https://git-scm.com/downloads) installed on your local machine
- You already have installed [postgresql 9.6](https://www.postgresql.org/download/) installed on your local machine

### Create your virtualenv

```shell
mkvirtualenv -p python3.6 abi 
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

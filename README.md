# Python Micro Framework Data FastAPI Example

This document is an example project repository using [pymfdata](https://github.com/NEONKID/python-mf-data) in FastAPI.

* [한국어](https://github.com/NEONKID/python-mf-data-example/blob/main/README.ko.md)



<br />



## Install Poetry

This project uses Poetry to manage dependencies. So you need to install Poetry first.

```shell
$ pip install poetry
```

```shell
$ brew install poetry
```

Install poetry using pip or the Homebrew command.



<br />



## Install Dependencies

Use the following command to install dependencies to be used in the project.

```shell
$ git clone https://github.com/NEONKID/python-mf-data-example
```

```shell
$ poetry install
```

You can install the dependencies needed for this project via ```poetry install``` command.



<br />



## How to run

Install PostgreSQL to run this project right away. (Docker or direct installation is fine)

If you want to change the environment settings, you can use the ```common/resources/.env``` file.

```shell
$ python fastapi_advanced/run.py
```

```
Traceback (most recent call last):
  File "fastapi_advanced/run.py", line 3, in <module>
    from fastapi_advanced.src.app import create_app
ModuleNotFoundError: No module named 'fastapi_advanced'
```

If you get the above error, try replacing PYTHONPATH with your current path.

```shell
$ export PYTHONPATH=.
```



<br />



## Issue

If you have any problems at any time, please post them in the [issues](https://github.com/NEONKID/python-mf-data-example/issues) section of this repository.
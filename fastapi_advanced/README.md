# Python Micro Framework Data FastAPI Advanced

This document is a high-level example of using [pymfdata](https://github.com/NEONKID/python-mf-data) in FastAPI, and includes additional configuration such as dependency injection and layered architecture.

* [한국어](https://github.com/NEONKID/python-mf-data-example/blob/main/fastapi_advanced/README.ko.md)



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
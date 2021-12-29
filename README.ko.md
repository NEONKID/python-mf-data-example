# Python Micro Framework Data FastAPI Example

이 문서는 [pymfdata](https://github.com/NEONKID/python-mf-data)를 FastAPI에서 사용한 예제 프로젝트 레포지터리 입니다.



<br />



## Install Poetry

이 프로젝트는 Poetry를 이용하여 디펜던시를 관리합니다. 따라서 사전에 Poetry를 설치해야 합니다.

```shell
$ pip install poetry
```

```shell
$ brew install poetry
```

pip, 혹은 HomeBrew 커맨드를 이용하여 poetry를 설치합니다.



<br />



## Install Dependencies

프로젝트에 사용할 디펜던시를 설치할 때는 아래의 명령어를 이용하십시오.

```shell
$ git clone https://github.com/NEONKID/python-mf-data-example
```

```shell
$ poetry install
```

poetry install 명령어를 통해 이 프로젝트에 필요한 디펜던시를 설치할 수 있습니다.



<br />



## How to run

이 프로젝트를 바로 실행하려면 PostgreSQL을 설치하십시오. (Docker 혹은 직접 설치도 괜찮습니다)

환경 설정을 바꾸고자 하는 경우 ```common/resources/.env``` 파일을 이용하시면 됩니다.

```shell
$ python fastapi_advanced/run.py
```

```
Traceback (most recent call last):
  File "fastapi_advanced/run.py", line 3, in <module>
    from fastapi_advanced.src.app import create_app
ModuleNotFoundError: No module named 'fastapi_advanced'
```

만약 위의 오류가 나타난다면 PYTHONPATH를 현재 경로로 바꿔보십시오.

```shell
$ export PYTHONPATH=.
```



<br />



## Issue

문제 신고는 이 레포지터리의 [issues](https://github.com/NEONKID/python-mf-data-example/issues)에 올려주십시오.
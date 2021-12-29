# Python Micro Framework Data FastAPI Advanced

이 문서는 [pymfdata](https://github.com/NEONKID/python-mf-data)를 FastAPI에서 사용한 고급 예시이며 의존성 주입, 계층형 아키텍처 등의 구성을 추가 포함하고 있습니다.

* [English](https://github.com/NEONKID/python-mf-data-example/blob/main/fastapi_advanced/README.md)



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


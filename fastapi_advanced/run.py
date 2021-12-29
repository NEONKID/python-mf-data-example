import uvicorn

from fastapi_advanced.src.app import create_app

if __name__ == "__main__":
    uvicorn.run(create_app(True), host="127.0.0.1", port=5000, log_level="debug")

from src.application import app
from src.config.configuration import configs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=configs['port'])
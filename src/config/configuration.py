from starlette.config import Config

class AppConfig:
    def __init__(self, env_file: str):
        self.config = Config(env_file)
    
    def get_config(self):
        return {
          "port": int(self.config('PORT', default=8000)),
        }

app_configuration = AppConfig('.env')

configs = app_configuration.get_config()

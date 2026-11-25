import os 

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DEBUG = False 



class DevelopmentConfig(Config):
    DEBUG = True 


class TestingConfig(Config): 
    DEBUG = True    
 

config_by_name = {
    "development": DevelopmentConfig, 
    "testing": TestingConfig, 
    "production": Config
}


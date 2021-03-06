import os

class Config:
    
    NEWS_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    SOURCE_API_URL= 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    API_KEY = os.environ.get('SOURCE_API_KEY')

class ProdConfig(Config):
    """
     Class that configures production
    """

    pass


class DevConfig(Config):

    DEBUG =True  

config_options = {
'development':DevConfig,
'production':ProdConfig
}    
import os

class Config:
  '''
  General class configuration
  
  '''

  SECRET_KEY=os.environ.get("SECRET_KEY")


class ProdConfig(Config):
  '''
  Production child class

  Args:
      Config main class

  '''
  pass

class DevConfig(Config):
  '''
  Development configuration class
  '''
  DEBUG=True


class TestConfig(Config):

  '''
  Test configuration
  '''
  pass

config_options={

  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}
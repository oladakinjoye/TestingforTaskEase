import os

class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('mysql+pymysql://root:Tunde@1234@localhost/taskeasedb')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    
   SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://username:password@localhost/taskease'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
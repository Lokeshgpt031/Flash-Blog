import os
import os
SECRET_KEY = os.urandom(32)

class Config:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'lokeshgptmbnr@outlook.com'
    MAIL_PASSWORD = 'lok9052120182'

class Config:
    SECRET_KEY = "secret123"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/employee_portal"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
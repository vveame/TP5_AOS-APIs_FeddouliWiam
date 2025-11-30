import os

class Config:
    # Database
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", "3306"))
    DB_NAME = os.getenv("DB_NAME", "ex3_filiere")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Eureka
    EUREKA_SERVER = os.getenv("EUREKA_SERVER", "http://localhost:8761/eureka")
    APP_NAME = os.getenv("APP_NAME", "FILIERE-SERVICE-PY")
    APP_PORT = int(os.getenv("APP_PORT", "8081"))

    # JWT public key path
    RSA_PUBLIC_KEY_PATH = os.getenv("RSA_PUBLIC_KEY_PATH", "keys/publicKey.pem")

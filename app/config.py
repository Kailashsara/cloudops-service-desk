import os

class Config:
    APP_NAME = "CloudOps Service Desk"
    APP_VERSION = "1.0.0"
    APP_ENV = os.getenv("APP_ENV", "development")

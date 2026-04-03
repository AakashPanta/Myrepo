import os


def get_app_env():
    return os.getenv("APP_ENV", "development")


def get_app_debug():
    return os.getenv("APP_DEBUG", "false").lower() == "true"


def load_config():
    return {
        "APP_ENV": get_app_env(),
        "APP_DEBUG": get_app_debug(),
    }

import os
from pathlib import Path


def load_env_file(path=".env"):
    env_path = Path(path)
    if not env_path.exists():
        return

    for line in env_path.read_text().splitlines():
        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        if key and key not in os.environ:
            os.environ[key] = value


def get_app_env():
    return os.getenv("APP_ENV", "development")


def get_app_debug():
    return os.getenv("APP_DEBUG", "false").lower() == "true"


def load_config():
    load_env_file()

    return {
        "APP_ENV": get_app_env(),
        "APP_DEBUG": get_app_debug(),
    }

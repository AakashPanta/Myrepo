from src.version import __version__
from src.config import load_config


def main():
    config = load_config()
    env = config["APP_ENV"]
    debug = config["APP_DEBUG"]

    print(f"Mr-Robot project initialized. Version: {__version__}")
    print(f"Environment: {env}")
    print(f"Debug: {debug}")


if __name__ == "__main__":
    main()

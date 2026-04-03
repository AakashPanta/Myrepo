import json
import os
import sys
from pathlib import Path
from src.main import main
from src.version import __version__
from src.config import load_config


def show_help():
    print("Mr-Robot CLI")
    print("")
    print("Usage:")
    print("  python3 -m src.cli run")
    print("  python3 -m src.cli version")
    print("  python3 -m src.cli info")
    print("  python3 -m src.cli status")
    print("  python3 -m src.cli status-json")
    print("  python3 -m src.cli config")
    print("  python3 -m src.cli init")
    print("  python3 -m src.cli doctor")
    print("  python3 -m src.cli help")


def run():
    main()


def version():
    print(__version__)


def info():
    print("Project: Mr-Robot")
    print(f"Version: {__version__}")
    print("Platform: iPhone + iSH + GitHub")
    print("Type: Structured Python project repository")


def get_status_checks():
    return {
        "Source": os.path.exists("src/main.py"),
        "CLI": os.path.exists("src/cli.py"),
        "Tests": os.path.exists("tests/test_main.py"),
        "Docs": os.path.exists("docs/usage.md"),
        "Roadmap": os.path.exists("docs/roadmap.md"),
        "Architecture": os.path.exists("docs/architecture.md"),
        "Requirements": os.path.exists("requirements.txt"),
        "Makefile": os.path.exists("Makefile"),
    }


def status():
    checks = get_status_checks()

    print("Mr-Robot status")
    print("")

    for name, ok in checks.items():
        state = "OK" if ok else "MISSING"
        print(f"{name}: {state}")


def status_json():
    checks = get_status_checks()
    print(json.dumps(checks, indent=2))


def config():
    values = load_config()
    print("Mr-Robot configuration")
    print("")
    for key, value in values.items():
        print(f"{key}: {value}")


def init():
    Path("data").mkdir(exist_ok=True)
    Path("logs").mkdir(exist_ok=True)
    Path("data/.gitkeep").touch(exist_ok=True)
    Path("logs/.gitkeep").touch(exist_ok=True)
    print("Mr-Robot initialization complete.")
    print("Created: data/, logs/")


def doctor():
    checks = {
        "src/main.py": os.path.exists("src/main.py"),
        "src/cli.py": os.path.exists("src/cli.py"),
        "src/config.py": os.path.exists("src/config.py"),
        "src/version.py": os.path.exists("src/version.py"),
        "tests/test_main.py": os.path.exists("tests/test_main.py"),
        "tests/test_version.py": os.path.exists("tests/test_version.py"),
        "docs/usage.md": os.path.exists("docs/usage.md"),
        "docs/installation.md": os.path.exists("docs/installation.md"),
        "requirements.txt": os.path.exists("requirements.txt"),
        "Makefile": os.path.exists("Makefile"),
        ".env.example": os.path.exists(".env.example"),
    }

    print("Mr-Robot doctor")
    print("")

    failed = []

    for name, ok in checks.items():
        state = "OK" if ok else "MISSING"
        print(f"{name}: {state}")
        if not ok:
            failed.append(name)

    print("")
    if failed:
        print("Doctor result: issues found")
    else:
        print("Doctor result: all checks passed")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    else:
        command = sys.argv[1].lower()

        if command == "run":
            run()
        elif command == "version":
            version()
        elif command == "info":
            info()
        elif command == "status":
            status()
        elif command == "status-json":
            status_json()
        elif command == "config":
            config()
        elif command == "init":
            init()
        elif command == "doctor":
            doctor()
        elif command == "help":
            show_help()
        else:
            print(f"Unknown command: {command}")
            show_help()

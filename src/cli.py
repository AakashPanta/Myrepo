import os
import sys
from src.main import main
from src.version import __version__


def show_help():
    print("Mr-Robot CLI")
    print("")
    print("Usage:")
    print("  python3 -m src.cli run")
    print("  python3 -m src.cli version")
    print("  python3 -m src.cli info")
    print("  python3 -m src.cli status")
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


def status():
    checks = {
        "Source": os.path.exists("src/main.py"),
        "CLI": os.path.exists("src/cli.py"),
        "Tests": os.path.exists("tests/test_main.py"),
        "Docs": os.path.exists("docs/usage.md"),
        "Roadmap": os.path.exists("docs/roadmap.md"),
        "Architecture": os.path.exists("docs/architecture.md"),
        "Requirements": os.path.exists("requirements.txt"),
        "Makefile": os.path.exists("Makefile"),
    }

    print("Mr-Robot status")
    print("")

    for name, ok in checks.items():
        state = "OK" if ok else "MISSING"
        print(f"{name}: {state}")


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
        elif command == "help":
            show_help()
        else:
            print(f"Unknown command: {command}")
            show_help()

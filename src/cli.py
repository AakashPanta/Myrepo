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
    print("Mr-Robot status: active")
    print("Tests: available")
    print("CLI: enabled")
    print("Documentation: available")


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

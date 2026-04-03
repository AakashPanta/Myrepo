import sys
from src.main import main
from src.version import __version__


def show_help():
    print("Mr-Robot CLI")
    print("")
    print("Usage:")
    print("  python3 -m src.cli run")
    print("  python3 -m src.cli version")
    print("  python3 -m src.cli help")


def run():
    main()


def version():
    print(__version__)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    else:
        command = sys.argv[1].lower()

        if command == "run":
            run()
        elif command == "version":
            version()
        elif command == "help":
            show_help()
        else:
            print(f"Unknown command: {command}")
            show_help()

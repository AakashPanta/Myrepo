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
    print("  python3 -m src.cli bootstrap <project-name>")
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


def bootstrap(project_name):
    base = Path(project_name)

    if base.exists():
        print(f"Project already exists: {project_name}")
        return

    (base / "src").mkdir(parents=True)
    (base / "tests").mkdir()
    (base / "docs").mkdir()
    (base / "examples").mkdir()
    (base / "assets").mkdir()

    (base / "README.md").write_text(f"# {project_name}\n")
    (base / "requirements.txt").write_text("pytest\n")
    (base / ".env.example").write_text("APP_ENV=development\nAPP_DEBUG=false\n")
    (base / "Makefile").write_text(
        "run:\n\tpython3 -m src.main\n\n"
        "test:\n\tpytest\n"
    )
    (base / "src" / "__init__.py").write_text("")
    (base / "src" / "main.py").write_text(
        "def main():\n"
        f"    print({project_name!r} + ' initialized.')\n\n"
        "if __name__ == '__main__':\n"
        "    main()\n"
    )
    (base / "tests" / "__init__.py").write_text("")
    (base / "docs" / "usage.md").write_text(f"# Usage\n\nProject: {project_name}\n")
    print(f"Bootstrap complete: {project_name}")
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
        elif command == "bootstrap":
            if len(sys.argv) < 3:
                print("Usage: python3 -m src.cli bootstrap <project-name>")
            else:
                bootstrap(sys.argv[2])
        elif command == "help":
            show_help()
        else:
            print(f"Unknown command: {command}")
            show_help()

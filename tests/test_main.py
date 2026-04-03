import os
from src.main import main


def test_main_default(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == (
        "Mr-Robot project initialized. Version: 8.0.0\n"
        "Environment: development\n"
        "Debug: False"
    )


def test_main_with_env_override(capsys, monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    monkeypatch.setenv("APP_DEBUG", "true")

    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == (
        "Mr-Robot project initialized. Version: 8.0.0\n"
        "Environment: production\n"
        "Debug: True"
    )

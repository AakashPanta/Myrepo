from src.main import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Mr-Robot project initialized. Version: 8.0.0"

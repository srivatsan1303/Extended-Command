import pytest
from app import App

def test_app_welcome_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'welcome' command and outputs 'Welcome! Have a nice day'."""
    inputs = iter(['welcome', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    # Check that the exit was graceful with the correct exit code
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output from the 'hello' command
    out, err = capfd.readouterr()
    
    # Assert that 'Hi, How do you do' was printed to stdout
    assert "Welcome! Have a nice day" in out, "The 'welcome' command did not produce the expected output."

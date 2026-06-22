import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from app import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    status, _ = check_guess(50, 50)
    assert status == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    status, _ = check_guess(60, 50)
    assert status == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    status, _ = check_guess(40, 50)
    assert status == "Too Low"

def test_too_high_message():
    # If guess is too high, message should tell you to go LOWER
    status, message = check_guess(60, 50)
    assert status == "Too High"
    assert "LOWER" in message

def test_too_low_message():
    # If guess is too low, message should tell you to go HIGHER
    status, message = check_guess(40, 50)
    assert status == "Too Low"
    assert "HIGHER" in message

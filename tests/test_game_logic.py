from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_win_on_first_attempt_scores_90():
    # Old bug: 100 - 10 * (attempt_number + 1) gave 80 on attempt 1.
    # Fixed formula: 100 - 10 * attempt_number should give 90.
    score = update_score(0, "Win", 1)
    assert score == 90

def test_new_game_resets_state():
    from streamlit.testing.v1 import AppTest
    at = AppTest.from_file("app.py").run()
    # Submit a guess to build up state
    at.text_input[0].set_value("42")
    at.button[0].click().run()
    assert at.session_state.attempts == 1
    assert len(at.session_state.history) == 1
    # Click New Game and verify everything resets
    at.button[1].click().run()
    assert at.session_state.attempts == 0
    assert at.session_state.status == "playing"
    assert at.session_state.history == []

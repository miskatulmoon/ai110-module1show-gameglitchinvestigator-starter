# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

Game purpose: A number-guessing game where the player picks a difficulty, then narrows down a secret number using Higher/Lower hints. The goal is to guess correctly in as few attempts as possible to maximize score.

Bugs found:

1. Swapped hint messages (`check_guess`) — When a guess was too high, the message said "Go HIGHER!" and when too low it said "Go LOWER!"

2. Secret cast to string on even attempts (`app.py`) — Every even-numbered attempt converted the secret integer to a string before passing it to `check_guess`.

3. New Game button doesn't reset `status` — Clicking New Game reset `attempts` and generated a new secret, but left `st.session_state.status` as `"won"` or `"lost"`.

4. New Game uses hardcoded range — `random.randint(1, 100)` was hardcoded regardless of difficulty, so a new Easy game (range 1–20) would still pick a secret up to 100.

Fixes applied:

- In `check_guess`: swapped the hint messages so `"Too High"` pairs with "Go LOWER!" and `"Too Low"` pairs with "Go HIGHER!". Removed the string-comparison fallback entirely by keeping the secret as an `int` at all times.
- In `app.py`: removed the even/odd attempt type-switching block so `secret` is always passed as an integer to `check_guess`.
- In the New Game handler: added `st.session_state.status = "playing"` and `st.session_state.history = []`, and replaced the hardcoded `random.randint(1, 100)` with `random.randint(low, high)` using the difficulty-aware range.
- Moved `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` into `logic_utils.py` and imported them in `app.py`.

## 📸 Demo Walkthrough

Sample game on **Normal** difficulty (range 1–100, 8 attempts, secret = 63, starting score = 0):

1. The app loads. The sidebar shows "Range: 1 to 100" and "Attempts allowed: 8". Score is 0.
2. User types 50 and clicks Submit → hint reads "📈 Go Higher!" (correct: 50 < 63). Score: −5 (attempt 1, Too Low).
3. User types 75 → hint reads "📉 Go Lower!" (correct: 75 > 63). Score: 0 (attempt 2, Too High on an even attempt = +5).
4. User types 60 → hint reads "📈 Go Higher!" (correct: 60 < 63). Score: −5 (attempt 3, Too Low).
5. User types 65 → hint reads "📉 Go Lower!" (correct: 65 > 63). Score: 0 (attempt 4, Too High on even attempt = +5).
6. User types 63 → "🎉 Correct!" Balloons fire. Score: +40 (win on attempt 5: 100 − 10×6 = 40). Final score: 40.
7. The input and Submit button are locked. Clicking "New Game" resets attempts, score, history, and status.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ pytest tests/ -v
============================= test session starts ==============================
platform darwin -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
collected 5 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 20%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 40%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 60%]
tests/test_game_logic.py::test_win_on_first_attempt_scores_90 PASSED     [ 80%]
tests/test_game_logic.py::test_new_game_resets_state PASSED              [100%]

============================== 5 passed in 0.26s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

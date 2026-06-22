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
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
      The game's purpose is to guess the correct number based on hints that are given after the intial guess. It is also to help us learn how to use AI to debug and write tests.
- [ ] Detail which bugs you found.
      Bugs I have found included having too many game over messages, with one playing when the user still had one more attempt left and then at 0 attempts a new game over screen would come up. Another issue was one where when you first entered a guess, the hint would show, but the attempts would not. This would lead to an incorrect amount of guesses you were able to do. Another issue was the hints being backwards. If your number was too high, it would tell you to go higher. If it was too low, it would tell you to go lower.
      There was also an issue with the reset button, where it would not properly reset the game and leave it in a partially un reset state.
- [ ] Explain what fixes you applied.
      The fixes I applied were that for the game over messages, I combined them into one message for when there was 0 guesses left, which corrected the issue of there being game over at 1 attempt remaining. For when the amount of attempts was off, the order of which the number was updating and printing was off. The number would print, and then update. I changed it so that it would update with the button press, and then print the updated state. The hints being backwards was an issue in logic, where the logic was reversed. I simply swapped the text that displayed, which was giving wrong info before. With the reset button, only a few variables were being reset back to their default states, not all. I made sure to also make sure things like the history array was empty, that the session state was "playing" instead of ended. Reset the score to 0 and set the difficulty range for the new game.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User reads instructions
2. User enters a guess between 1 and 100
3. User looks at hint: "Too Low, Go Higher!" if the score is too low, "Too High, Go Lower!" if the score is too big.
4. The score updates after each guess.
5. Repeat step 3 until there are no more guesses left.
6. Game ends when there is no more guesses left or when the user guesses correctly.

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

============================================================================================================ test session starts ============================================================================================================
platform win32 -- Python 3.11.3, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\nickh\Documents\CodePath\AI110\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 5 items

tests\test_game_logic.py ..... [100%]

============================================================================================================= 5 passed in 0.76s =============================================================================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

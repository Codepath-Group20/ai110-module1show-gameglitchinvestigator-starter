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

- [x] Describe the game's purpose.
The application is a classic number guessing game built using the Streamlit framework. Players select a difficulty setting and attempt to find a randomly generated secret number within a specified number of attempts while receiving dynamically calculated lower/higher clues.

- [x] Detail which bugs you found.
Discovered that the application lacked session state management, causing the target number to randomize on every single user submission. Additionally, the guess input validation fields allowed extreme out-of-bounds inputs, the guess attempt counters arbitrarily restricted standard boundaries, and the UI layout text provided completely inverted high/low hints.

- [x] Explain what fixes you applied.
Centralized the logic math away from the Streamlit execution tree by refactoring core rules into standalone functions within `logic_utils.py`. Fixed the inverted string responses, bound the guess calculations securely, and established proper test fixtures to verify integrity.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. **Start Game:** The user loads the application in the browser; the system generates a stable secret number behind the scenes and displays the standard guessing parameters based on the chosen difficulty.

2. **Initial Guess:** The user inputs a numerical guess (e.g., `40`) and clicks "Submit Guess" or triggers the validation flow.
 
3. **Dynamic Feedback Loop:** The game references `logic_utils.py` and returns a precise clue—evaluating the input against the persistent target to accurately display "📉 Go LOWER!" or "📈 Go HIGHER!".

4. **Attempt & Score Update:** The application state reduces the remaining attempts counter by exactly one, stores the entry in the visible Guess History log, and adjusts the session score metrics predictably.

5. **Win State Trigger:** Upon matching the hidden number exactly, the dashboard locks down inputs, surfaces a celebratory "🎉 You got it!" alert banner, and halts attempt consumption. 

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

```text
(venv) [leo@precision ai110-module1show-gameglitchinvestigator-starter]$ python -m pytest tests/test_game_logic.py
=================================== test session starts ====================================
platform linux -- Python 3.11.13, pytest-9.1.0, pluggy-1.6.0
rootdir: /home/leo/Classes/summer_2026/CodePath_A110/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 3 items                                                                           

tests/test_game_logic.py ...                                                          [100%]

==================================== 3 passed in 0.06s =====================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

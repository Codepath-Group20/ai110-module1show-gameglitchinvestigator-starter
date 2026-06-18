# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Show hint doesn't toggle and New Game doesn't reset the game.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1."Enter" key doesn't work and one has to use the Submit Guess button.
2. The hints were backwards when suggesting choosing larger or smaller number.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                                     | Expected Behavior                                | Actual Behavior                                  | Console Output / Error |
|-------------------------------------------|--------------------------------------------------|--------------------------------------------------|------------------------|
|Guess 40                                   |Should say "Go Lower"                             |Displayed "📈 Go HIGHER!"                         |None                    |
|Guesses outside 1-100 (e.g., `300`, `-10`) |Should show a warning and not count as an attempt |Allowed the guess and deducted an attempt         |None                    |
|Total of 7 guesses tracked in history      |Should show "Attempts left: 1" (8 - 7)            |Showed "Attempts left: 0" and triggered Game Over |None                    |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copilot in order to save tokens for later use.
I utilized the integrated AI coding assistant panel within VS Code (Raptor Mini/Copilot) alongside a text chat collaborator to talk through the architecture. Using the panel allowed me to leverage workspace context to analyze the files directly. This hybrid approach helped me double-check logic without manually wasting API tokens.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI correctly identified the root cause of the inverted hint bug inside `app.py`. It pointed out that while the conditional execution statement `if guess > secret:` was syntactically perfect, the internal return string mistakenly outputted "Go HIGHER!". I verified this by accepting the refactored code and watching the Streamlit application instantly flip to the correct hint behavior.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI initially suggested running a raw `pytest tests/test_game_logic.py` script from the root terminal path. This was misleading because it didn't account for how Python maps relative directories in a virtual environment, leading to a frustrating `ModuleNotFoundError: No module named 'logic_utils'`. I verified this error in my shell and resolved it by forcing Python to inject the execution path using the `python -m pytest` module pattern.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was genuinely fixed when it could pass both an automated programmatic verification cycle and a manual execution test. The code couldn't just look visually correct in the browser layout; it also had to consistently pass the unit assertions. Ensuring the fixes satisfied separate validation barriers stopped regression errors.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I executed an automated test suite using `python -m pytest tests/test_game_logic.py`. The execution ran three separate validation checks against the refactored `check_guess` module functions in 0.06 seconds. The resulting green passing logs proved that the boundary outputs safely matched our expected logic assertions.

- Did AI help you design or understand any tests? How?
Yes, the AI generated the explicit assertion blocks for `tests/test_game_logic.py` based on the exact tuple return values of our newly refactored helper file. It helped me understand how to cleanly isolate state math away from the UI framework so it could be evaluated independently. This made it clear why separating backend calculations from presentation layers is vital for testability.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit acts like a script that completely re-reads and re-executes your entire Python file from the very first line to the last line every single time a user clicks a button or interacts with the screen. Because everything wipes clean on a rerun, "Session State" acts like a separate sticky note on the side where Python safely writes down and remembers your variables—like the secret number or your score—so they don't get erased when the app refreshes.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to keep utilizing atomic, micro-focused commits using the command line rather than staging an entire project's worth of chaotic changes at the very end. Breaking changes into granular git steps makes it incredibly easy to track down bugs or safely view the original template using history commands like `git show HEAD~1`.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I will make a conscious habit to read through the generated diff files much more closely *before* clicking the editor's "Keep" or "Accept" overlay prompts. It is easy to get caught up in the speed of automated streaming code generation and lose track of what the starting template file structure originally looked like.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project proved that AI-generated code can often look completely flawless on the surface while being fundamentally broken underneath. It taught me that syntax and logic are two entirely different animals, and a developer must always critically audit an AI's output.

import pytest
from streamlit.testing.v1 import AppTest

def test_game_over_ui_sync():
    """Ensure that when out of attempts, the game over message appears

    and the 'Attempts left: 1' text disappears.
    """
    # 1. Initialize the Streamlit App simulation
    at = AppTest.from_file("app.py").run()
    
    # 2. Simulate selecting a difficulty or initializing state if needed
    # (Assuming defaults: max_attempts = 8)
    
    # 3. Simulate entering 8 incorrect guesses to run out of attempts
    # We find the input widget, change its value, and click submit
    for _ in range(8):
        # Substitute 'number_input' or 'button' with the actual keys/labels used in your app.py
        if at.number_input:
            at.number_input[0].set_value(999).run() # Force a wrong guess
        if at.button:
            at.button[0].click().run()

    # 4. Assertions: Verify the UI elements match the exact game-over state
    # Ensure the error banner appears
    assert len(at.error) > 0 
    
    # Ensure the stale "Attempts left: 1" text is NOT present in the main body
    for text_element in at.text:
        assert "Attempts left: 1" not in text_element.value

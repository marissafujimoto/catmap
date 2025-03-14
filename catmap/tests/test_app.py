"""Module for app testing."""
from streamlit.testing.v1 import AppTest


def test_page_one_button_click():
    """A user clicks to go to page 1."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    assert at.session_state.current_page == "home" # start on home page
    at.button[0].click().run()
    assert at.session_state.current_page == "page_1" # After click, move to page 1

def test_page_two_button_click():
    """A user clicks to go to page 2."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    assert at.session_state.current_page == "home" # start on home page
    at.button[1].click().run()
    assert at.session_state.current_page == "page_2" # After click, move to page 2

def test_return_to_home_from_page_one():
    """A user clicks to go back to home from page 1."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    assert at.session_state.current_page == "home" # start on home page
    at.button[0].click().run()
    assert at.session_state.current_page == "page_1" # After click, move to page 2
    at.button[1].click().run()
    assert at.session_state.current_page == "home" # After click one page 2, return to home

def test_return_to_home_from_page_two():
    """A user clicks to go back to home from page 1."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    assert at.session_state.current_page == "home" # start on home page
    at.button[1].click().run()
    assert at.session_state.current_page == "page_2" # After click, move to page 2
    at.button[1].click().run()
    assert at.session_state.current_page == "home" # After click one page 2, return to home

def test_open_close_info_button_page_one():
    """A user clicks on the info button on page 1 to open and close it."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[0].click().run() # move to page 1
    assert at.session_state.current_page == "page_1" # After click, move to page 1
    assert not at.info # info is not displayed 
    at.button[0].click().run() # click info button
    assert at.info[0].value == "Different categories correspond to different clustering." # info line is displayed
    at.button[0].click().run() # click info button again 
    assert not at.info # info is not displayed 

def test_open_close_info_button_page_two():
    """A user clicks on the info button on page 1 to open and close it."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[1].click().run() # move to page 2
    assert at.session_state.current_page == "page_2" # After click, move to page 1
    assert not at.info # info is not displayed 
    at.button[0].click().run() # click info button
    assert at.info[0].value == "Different categories correspond to different clustering." # info line is displayed
    at.button[0].click().run() # click info button again 
    assert not at.info # info is not displayed 

def test_expander_label_page_one():
    """A user clicks on the info button on page 1 to open and close it."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[0].click().run() # move to page 1
    assert at.session_state.current_page == "page_1" # After click, move to page 1
    assert at.expander[0].label == "About this dashboard"

def test_expander_label_page_two():
    """A user clicks on the info button on page 1 to open and close it."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[1].click().run() # move to page 2
    assert at.session_state.current_page == "page_2" # After click, move to page 2
    assert at.expander[0].label == "About this dashboard"

def test_selectbox_dropdown_page_one():
    """A user clicks on the info button on page 1 to open and close it."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[0].click().run() # move to page 1
    assert at.session_state.current_page == "page_1" # After click, move to page 1
    assert at.selectbox[0].label == "Column"
    assert at.selectbox[0].options == at.session_state.column_options
    assert at.selectbox[0].index == 0

def test_selectbox_dropdown_page_two():
    """A user clicks on the info button on page 1 to open and close it."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[1].click().run() # move to page 2
    assert at.session_state.current_page == "page_2" # After click, move to page 2
    assert at.selectbox[0].label == "Column"
    assert at.selectbox[0].options == at.session_state.column_options
    assert at.selectbox[0].index == 0
    
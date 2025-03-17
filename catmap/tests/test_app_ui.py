import pytest # type: ignore
from streamlit.testing.v1 import AppTest

@pytest.fixture
def app_ui_test():
    """Fixture to initialize the app test instance."""
    app = AppTest.from_file("../src/catmap/app.py").run()
    
    # Explicitly set session state if missing
    if "current_page" not in app.session_state:
        app.session_state["current_page"] = "home"
    
    return app

def test_page_one_button_click(app_ui_test):
    """A user clicks to go to page 1."""
    assert app_ui_test.session_state.current_page == "home" # start on home page
    app_ui_test.button[0].click().run()
    assert app_ui_test.session_state.current_page == "page_1" # After click, move to pag

def test_page_two_button_click(app_ui_test):
    """A user clicks to go to page 2."""
    assert app_ui_test.session_state.current_page == "home" # start on home page
    app_ui_test.button[1].click().run()
    assert app_ui_test.session_state.current_page == "page_2" # After click, move to page 2

def test_return_to_home_from_page_one(app_ui_test):
    """A user clicks to go back to home from page 1."""
    assert app_ui_test.session_state.current_page == "home" # start on home page
    app_ui_test.button[0].click().run()
    assert app_ui_test.session_state.current_page == "page_1" # After click, move to page 2
    app_ui_test.button[1].click().run()
    assert app_ui_test.session_state.current_page == "home" # After click one page 2, return to home

def test_return_to_home_from_page_two(app_ui_test):
    """A user clicks to go back to home from page 1."""
    assert app_ui_test.session_state.current_page == "home" # start on home page
    app_ui_test.button[1].click().run()
    assert app_ui_test.session_state.current_page == "page_2" # After click, move to page 2
    app_ui_test.button[1].click().run()
    assert app_ui_test.session_state.current_page == "home" # After click one page 2, return to home

def test_open_close_info_button_page_one(app_ui_test):
    """A user clicks on the info button on page 1 to open and close it."""
    app_ui_test.button[0].click().run() # move to page 1
    assert app_ui_test.session_state.current_page == "page_1" # After click, move to page 1
    assert not app_ui_test.info # info is not displayed
    app_ui_test.button[0].click().run() # click info button
    assert app_ui_test.info[0].value == "Different categories correspond to different clustering."
    # info line is displayed
    app_ui_test.button[0].click().run() # click info button again
    assert not app_ui_test.info # info is not displayed

def test_open_close_info_button_page_two(app_ui_test):
    """A user clicks on the info button on page 1 to open and close it."""
    app_ui_test.button[1].click().run() # move to page 2
    assert app_ui_test.session_state.current_page == "page_2" # After click, move to page 1
    assert not app_ui_test.info # info is not displayed
    app_ui_test.button[0].click().run() # click info button
    assert app_ui_test.info[0].value == "Different categories correspond to different clustering."
    # info line is displayed
    app_ui_test.button[0].click().run() # click info button again
    assert not app_ui_test.info # info is not displayed

def test_expander_label_page_one(app_ui_test):
    """A user clicks on the info button on page 1 to open and close it."""
    app_ui_test.button[0].click().run() # move to page 1
    assert app_ui_test.session_state.current_page == "page_1" # After click, move to page 1
    assert app_ui_test.expander[0].label == "About this dashboard"

def test_expander_label_page_two(app_ui_test):
    """A user clicks on the info button on page 1 to open and close it."""
    app_ui_test.button[1].click().run() # move to page 2
    assert app_ui_test.session_state.current_page == "page_2" # After click, move to page 2
    assert app_ui_test.expander[0].label == "About this dashboard"

def test_selectbox_dropdown_page_one(app_ui_test):
    """A user clicks on the info button on page 1 to open and close it."""
    app_ui_test.button[0].click().run() # move to page 1
    assert app_ui_test.session_state.current_page == "page_1" # After click, move to page 1
    assert app_ui_test.selectbox[0].label == "Column"
    assert app_ui_test.selectbox[0].options == app_ui_test.session_state.column_options
    assert app_ui_test.selectbox[0].index == 0

def test_selectbox_dropdown_page_two(app_ui_test):
    """A user clicks on the info button on page 1 to open and close it."""
    app_ui_test.button[1].click().run() # move to page 2
    assert app_ui_test.session_state.current_page == "page_2" # After click, move to page 2
    assert app_ui_test.selectbox[0].label == "Column"
    assert app_ui_test.selectbox[0].options == app_ui_test.session_state.column_options
    assert app_ui_test.selectbox[0].index == 0
"""Module for app testing."""
from streamlit.testing.v1 import AppTest


def test_page_one_button_click():
    """A user clicks to go to page 1."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    assert at.session_state.current_page == "home"  # start on home page
    at.button[0].click().run()
    assert at.session_state.current_page == "page_1"  # After click, move to page 1


def test_page_two_button_click():
    """A user clicks to go to page 2."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    assert at.session_state.current_page == "home"  # start on home page
    at.button[1].click().run()
    assert at.session_state.current_page == "page_2"  # After click, move to page 2


def test_return_to_home_from_page_one():
    """A user clicks to go back to home from page 1."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    assert at.session_state.current_page == "home"  # start on home page
    at.button[0].click().run()
    assert at.session_state.current_page == "page_1"  # After click, move to page 2
    at.button[1].click().run()
    # After click one page 2, return to home
    assert at.session_state.current_page == "home"


def test_return_to_home_from_page_two():
    """A user clicks to go back to home from page 2."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    assert at.session_state.current_page == "home"  # start on home page
    at.button[1].click().run()
    assert at.session_state.current_page == "page_2"  # After click, move to page 2
    at.button[1].click().run()
    # After click one page 2, return to home
    assert at.session_state.current_page == "home"


def test_open_close_info_button_page_one():
    """A user clicks on the info button on page 1 to open and close it."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[0].click().run()  # move to page 1
    assert at.session_state.current_page == "page_1"  # After click, move to page 1
    assert not at.info  # info is not displayed
    at.button[0].click().run()  # click info button
    # info line is displayed
    assert at.info[0].value == "Different categories correspond to different clustering."
    at.button[0].click().run()  # click info button again
    assert not at.info  # info is not displayed


def test_open_close_info_button_page_two():
    """A user clicks on the info button on page 2 to open and close it."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[1].click().run()  # move to page 2
    assert at.session_state.current_page == "page_2"  # After click, move to page 1
    assert not at.info  # info is not displayed
    at.button[0].click().run()  # click info button
    # info line is displayed
    assert at.info[0].value == "Different categories correspond to different clustering."
    at.button[0].click().run()  # click info button again
    assert not at.info  # info is not displayed


def test_expander_label_page_one():
    """A user clicks on the info button on page 1 to open and close it."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[0].click().run()  # move to page 1
    assert at.session_state.current_page == "page_1"  # After click, move to page 1
    assert at.expander[0].label == "About this dashboard"


def test_expander_label_page_two():
    """A user clicks on the info button on page 2 to open and close it."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[1].click().run()  # move to page 2
    assert at.session_state.current_page == "page_2"  # After click, move to page 2
    assert at.expander[0].label == "About this dashboard"


def test_selectbox_dropdown_page_one():
    """A user clicks on the info button on page 1 to open and close it."""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[0].click().run()  # move to page 1
    assert at.session_state.current_page == "page_1"  # After click, move to page 1
    assert at.selectbox[0].label == "Column"
    assert at.selectbox[0].options == ["Study", "Patient",
                                       "Cell_Cluster_level1", "Cell_Cluster_level2", "Stage"]


def test_selectbox_dropdown_page_two():
    # TODO: when unit test framework is finished, test if color of the px.scatter changes based on column
    """Tests the column dropdown functionality on page 2"""
    at = AppTest.from_file("../src/catmap/app.py").run()
    at.button[1].click().run()  # move to page 2
    at.selectbox[0].set_value("Stage").run()  # column dropdown set to Stage
    assert at.session_state.selected_column_colon == "Stage"
    assert at.session_state.current_page == "page_2"  # After click, move to page 2
    assert at.selectbox[0].label == "Column"
    assert at.selectbox[0].options == ["Patient", "Cluster Level 1", "Cluster Level 2",
                                       "Cancer/Normal", "Stage", "Lymph Node Status", "MMR Status", "MMR MLH1"]

"""Module for UI app testing."""

import unittest
from streamlit.testing.v1 import AppTest

class TestAppUI(unittest.TestCase):
    """Unit tests for Streamlit app UI."""

    def setUp(self):
        """Initialize a fresh app instance for the testing"""
        self.at = AppTest.from_file("../src/catmap/app.py").run()

    def test_page_one_button_click(self):
        """A user clicks to go to page 1."""
        self.assertEqual(self.at.session_state.current_page, "home") # start on home page
        self.at.button[0].click().run()
        self.assertEqual(self.at.session_state.current_page, "page_1") # After click, move to page 1

    def test_page_two_button_click(self):
        """A user clicks to go to page 2."""
        self.assertEqual(self.at.session_state.current_page, "home") # start on home page
        self.at.button[1].click().run()
        self.assertEqual(self.at.session_state.current_page, "page_2") # After click, move to page 2

    def test_return_to_home_from_page_one(self):
        """A user clicks to go back to home from page 1."""
        self.assertEqual(self.at.session_state.current_page, "home") # start on home page
        self.at.button[0].click().run()
        self.assertEqual(self.at.session_state.current_page, "page_1") # After click, move to page 2
        self.at.button[1].click().run()
        self.assertEqual(self.at.session_state.current_page, "home")
        # After click one page, return to home

    def test_return_to_home_from_page_two(self):
        """A user clicks to go back to home from page 1."""
        self.assertEqual(self.at.session_state.current_page, "home") # start on home page
        self.at.button[1].click().run()
        self.assertEqual(self.at.session_state.current_page, "page_2") # After click, move to page 2
        self.at.button[1].click().run()
        self.assertEqual(self.at.session_state.current_page, "home")
        # After click one page, return to home

    def test_open_close_info_button_page_one(self):
        """A user clicks on the info button on page 1 to open and close it."""
        self.at.button[0].click().run()
        self.assertEqual(self.at.session_state.current_page, "page_1")
        self.assertFalse(self.at.info)  # Info is not displayed
        self.at.button[0].click().run()
        # pylint: disable=line-too-long
        self.assertEqual(self.at.info[0].value, "Different categories correspond to different clustering.")
        # pylint: enable=line-too-long
        self.at.button[0].click().run()
        self.assertFalse(self.at.info)  # Info is not displayed

    def test_open_close_info_button_page_two(self):
        """A user clicks on the info button on page 1 to open and close it."""
        self.at.button[1].click().run()
        self.assertEqual(self.at.session_state.current_page, "page_2")
        self.assertFalse(self.at.info)
        self.at.button[0].click().run()
        # pylint: disable=line-too-long
        self.assertEqual(self.at.info[0].value, "Different categories correspond to different clustering.")
        # pylint: enable=line-too-long
        self.at.button[0].click().run()
        self.assertFalse(self.at.info)

    def test_expander_label_page_one(self):
        """A user clicks on the info button on page 1 to open and close it."""
        self.at.button[0].click().run()
        self.assertEqual(self.at.session_state.current_page, "page_1")
        self.assertEqual(self.at.expander[0].label, "About this dashboard")

    def test_expander_label_page_two(self):
        """A user clicks on the info button on page 1 to open and close it."""
        self.at.button[1].click().run()
        self.assertEqual(self.at.session_state.current_page, "page_2")
        self.assertEqual(self.at.expander[0].label, "About this dashboard")


    def test_selectbox_dropdown_page_one(self):
        """A user clicks on the info button on page 1 to open and close it."""
        self.at.button[0].click().run()
        self.assertEqual(self.at.session_state.current_page, "page_1")
        self.assertEqual(self.at.selectbox[0].label, "Column")
        self.assertEqual(self.at.selectbox[0].options, self.at.session_state.column_options)
        self.assertEqual(self.at.selectbox[0].index, 0)

    def test_selectbox_dropdown_page_two(self):
        """A user clicks on the info button on page 1 to open and close it."""
        self.at.button[1].click().run()
        self.assertEqual(self.at.session_state.current_page, "page_2")
        self.assertEqual(self.at.selectbox[0].label, "Column")
        self.assertEqual(self.at.selectbox[0].options, self.at.session_state.column_options)
        self.assertEqual(self.at.selectbox[0].index, 0)



if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
import time


class TestLinks(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cwd = os.getcwd() + "/web/home.html"
        cls.driver.get(f"file://{cwd}")
        cls.wait = WebDriverWait(cls.driver, 10)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_click_next_page_link(self):
        self.driver.save_screenshot('images/links/test_1_1.png')

        # Click the "Next Page" link
        if "nextpage.html" in self.driver.current_url:
            return

        next_page_link = self.driver.find_element(By.LINK_TEXT, "Next Page")
        next_page_link.click()
        self.driver.save_screenshot('images/links/test_1_2.png')


        time.sleep(5)

        # Verify that the URL has changed
        self.wait.until(EC.url_contains("nextpage.html"))
        current_url = self.driver.current_url
        self.assertIn("nextpage.html", current_url, "URL did not change to the next page.")

    def test_02_check_title_next_page(self):
        # Click the "Next Page" link and verify URL change

        self.test_01_click_next_page_link()

        # Verify that the title contains "Next Page"
        title = self.driver.title
        self.assertIn("Next Page", title, "Page title does not contain 'Next Page'.")
        self.driver.save_screenshot('images/links/test_2_1.png')

        time.sleep(5)

    def test_03_change_title(self):
        # Click the "Next Page" link
        self.test_01_click_next_page_link()

        # Click the button to change the title
        change_title_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Change Title')]")
        change_title_button.click()
        self.driver.save_screenshot('images/links/test_3_1.png')

        time.sleep(5)

        # Verify that the title has changed to "Finish"
        self.wait.until(EC.title_is("Finish"))
        title = self.driver.title
        self.assertEqual(title, "Finish", "Page title was not changed to 'Finish'.")
        time.sleep(5)

    def test_04_navigate_back_to_home(self):

        self.test_01_click_next_page_link()
        # Click the "Next Page" link

        # Click the button to navigate back to the home page
        back_to_home_link = self.driver.find_element(By.LINK_TEXT, "Back to Home Page")
        back_to_home_link.click()
        self.driver.save_screenshot('images/links/test_4_1.png')

        time.sleep(5)

        # Verify that we are back on the home page
        self.wait.until(EC.title_contains("Automation Project"))
        self.assertIn("Automation Project", self.driver.title, "Did not navigate back to the home page.")
        time.sleep(5)


if __name__ == "__main__":
    unittest.main()

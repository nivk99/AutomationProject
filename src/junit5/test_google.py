import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


class TestJunitWorkflow(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # הפעלת דפדפן Chrome
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cwd = os.getcwd() + "/../home_page/web/home.html"
        cls.driver.get(cwd)
        cls.wait = WebDriverWait(cls.driver, 50)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_navigate_to_google(self):
        # Click the link to Google
        google_link = self.driver.find_element(By.LINK_TEXT, "Google")  # Adjust link text or locator as needed
        google_link.click()
        self.driver.save_screenshot('images/test_1.png')
        time.sleep(3)


        # Verify that we have navigated to Google
        self.wait.until(EC.url_contains("google.com"))
        self.assertIn("google.com", self.driver.current_url, "Did not navigate to Google.")

    def test_02_search_junit_on_google(self):
        # Perform search for "Junit" on Google
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Junit" + Keys.RETURN)
        self.driver.save_screenshot('images/test_2.png')

        time.sleep(3)


        # Wait for search results to load
        self.wait.until(EC.presence_of_element_located((By.ID, "search")))

    def test_03_click_junit5_link(self):
        # Click on the JUnit 5 link
        junit5_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "JUnit 5")
        junit5_link.click()
        self.driver.save_screenshot('images/test_3.png')

        time.sleep(3)


        # Verify that we are on the JUnit 5 page
        self.wait.until(EC.url_to_be("https://junit.org/junit5/"))
        self.assertEqual(self.driver.current_url, "https://junit.org/junit5/", "Did not navigate to JUnit 5 page.")

    def test_04_navigate_to_user_guide(self):
        # Click on the User Guide link
        user_guide_link = self.driver.find_element(By.LINK_TEXT, "User Guide")  # Adjust link text or locator as needed
        user_guide_link.click()
        self.driver.save_screenshot('images/test_4.png')

        time.sleep(3)


        # Verify that we are on the User Guide page
        self.wait.until(EC.url_to_be("https://junit.org/junit5/docs/current/user-guide/"))
        self.assertEqual(self.driver.current_url, "https://junit.org/junit5/docs/current/user-guide/",
                         "Did not navigate to User Guide.")

    def test_05_select_getting_started(self):
        # Click on the Getting Started section
        getting_started_link = self.driver.find_element(By.CSS_SELECTOR,
                                                        "a.toc-link.node-name--H3[href='#overview-getting-started']")
        getting_started_link.click()
        self.driver.save_screenshot('images/test_5.png')

        time.sleep(3)
        # Verify that we are on the Getting Started section
        self.wait.until(EC.url_contains("getting-started"))
        self.assertIn("getting-started", self.driver.current_url, "Did not navigate to Getting Started section.")

    def test_06_check_user_guide_header(self):
        # Verify that there is an h3 header with text "1.4. Getting Started"
        header = self.driver.find_element(By.XPATH, "//*[@id='overview-getting-started']")
        self.assertIsNotNone(header, "Header '1.4. Getting Started' not found.")


if __name__ == "__main__":
    unittest.main()

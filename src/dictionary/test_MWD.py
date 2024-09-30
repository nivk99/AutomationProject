import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


class TestMerriamWebster(unittest.TestCase):

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

    def test_01_navigate_to_merriam_webster(self):
        # Click the link to Merriam-Webster Dictionary
        merriam_webster_link = self.driver.find_element(By.LINK_TEXT,
                                                        "Merriam-Webster Dictionary")  # Adjust link text or locator as needed
        self.driver.save_screenshot('images/test_1.png')

        merriam_webster_link.click()
        time.sleep(3)


        # Verify that we have navigated to Merriam-Webster
        self.wait.until(EC.url_to_be("https://www.merriam-webster.com/"))
        self.assertEqual(self.driver.current_url, "https://www.merriam-webster.com/",
                         "Did not navigate to Merriam-Webster.")

    def test_02_search_qa_in_merriam_webster(self):
        # Search for the term "QA" in Merriam-Webster
        search_box = self.driver.find_element(By.ID, "home-search-term")  # Adjust locator if necessary
        self.driver.save_screenshot('images/test_2_1.png')

        search_box.send_keys("QA" + Keys.RETURN)
        time.sleep(3)

        # Verify that the definition contains "quality assurance"
        definition_element = self.driver.find_element(By.CLASS_NAME,
                                                      "dtText")  # Adjust selector if necessary
        self.driver.save_screenshot('images/test_2_2.png')

        definition_text = definition_element.text
        self.assertIn("quality assurance", definition_text, "Definition for 'QA' is incorrect or not found.")
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time


class TestDownloadButton(unittest.TestCase):
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

    def test_01_click_download_button(self):
        # Click the download button
        download_button = self.driver.find_element(By.XPATH, "//button[text()='Start Downloading']")
        self.driver.save_screenshot('images/download_button/test_1_1.png')
        download_button.click()

        # Wait for the download complete message to appear
        confirmation_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[@id='download-finished-msg']//button[text()='OK']"))
        )
        self.assertTrue(confirmation_button.is_displayed(), "Download message is not displayed.")
        self.driver.save_screenshot('images/download_button/test_1_2.png')
        confirmation_button.click()
        time.sleep(5)

        # Verify that the message appears
        self.wait.until(EC.invisibility_of_element_located((By.ID, "download-finished-msg")))
        time.sleep(5)

    def test_02_confirm_download_message(self):
        # Click the download button
        download_button = self.driver.find_element(By.XPATH, "//button[text()='Start Downloading']")
        self.driver.save_screenshot('images/download_button/test_2_1.png')
        download_button.click()

        # Wait for the download complete message to appear
        confirmation_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[@id='download-finished-msg']//button[text()='OK']"))
        )
        # Click the confirm button in the message
        confirmation_button.click()
        time.sleep(5)

        # Wait for the message to disappear
        self.wait.until(EC.invisibility_of_element_located((By.ID, "download-finished-msg")))
        time.sleep(5)
        self.driver.save_screenshot('images/download_button/test_2_2.png')

        # Verify that the message is no longer displayed
        message = self.driver.find_element(By.ID, "download-finished-msg")
        self.assertFalse(message.is_displayed(), "Download message is still displayed after clicking confirm.")


if __name__ == "__main__":
    unittest.main()

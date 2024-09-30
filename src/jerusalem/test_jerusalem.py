import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.common.action_chains import ActionChains


class TestJerusalemMunicipality(unittest.TestCase):

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

    def test_01_navigate_to_jerusalem_municipality(self):
        # Click the link to Jerusalem Municipality
        jerusalem_link = self.driver.find_element(By.LINK_TEXT,
                                                  "Jerusalem Municipality")  # Adjust link text or locator as needed
        self.driver.save_screenshot('images/test_1.png')

        jerusalem_link.click()

        time.sleep(5)


        # Wait for the page to load and verify that the URL is correct
        self.wait.until(EC.url_contains("https://www.jerusalem.muni.il/"))
        self.assertIn("https://www.jerusalem.muni.il/", self.driver.current_url,
                      "Did not navigate to Jerusalem Municipality website.")

    def test_02_access_property_tax_payment(self):

        self.driver.find_element(By.XPATH, "//*[@id='emergencyModal']/div/div/div[1]/button/span").click()
        self.driver.save_screenshot('images/test_2_1.png')

        time.sleep(5)

        # מצא את האלמנט של "תושבים"
        self.driver.find_element(By.CLASS_NAME, "has-submenu").click()
        self.driver.save_screenshot('images/test_2_2.png')

        time.sleep(5)


        # עכשיו מצא את הקישור של "תשלום ארנונה" ולחץ עליו
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(By.CSS_SELECTOR, "a[href='/he/residents/arnona/property-tax-payment/']"))).click()
        self.driver.save_screenshot('images/test_2_3.png')

        time.sleep(5)


        # Click the button to initiate property tax payment
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='divContent']/section/div/div[1]/button/h3"))).click()  # Adjust locator if necessary
        self.driver.save_screenshot('images/test_2_4.png')

        time.sleep(5)


        # Wait for the payment page to load and get the text
        page_text = self.driver.find_element(By.XPATH, "//*[@id='openItem0']/div/div[1]").text
        self.driver.save_screenshot('images/test_2_5.png')

        self.assertIn("ניתן לשלם את הארנונה באמצעות טופס",page_text)
        # Print the text to the console
        print(page_text)
        time.sleep(5)



if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# options let you add arguments on how to start the browser
from selenium.webdriver.chrome.options import Options



class TestGoogleTranslate(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # initial operation - open browser...
        # for maximized browser - create an Option object and add argument for maximized
        options = Options()
        options.add_argument('--start-maximized')
        cls.driver = webdriver.Chrome(options=options)
        # set the base url for all files if you want to write less code in the test methods
        cls.driver.get("https://www.google.com/")
        cls.wait = WebDriverWait(cls.driver, 50)

        # time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_search_translate_on_google(self):
        # Find the Google search box
        search_box = self.driver.find_element(By.NAME, "q")
        # Search Google for Google Translate

        search_box.send_keys("Google Translate")
        self.assertEqual(self.driver.find_element(By.NAME, "q").get_attribute("value"),
                         "Google Translate")
        search_box.send_keys(Keys.ENTER)
        self.driver.save_screenshot('images/test_01.png')

        time.sleep(2)

        # Wait for search results to load
        self.wait.until(EC.presence_of_element_located((By.ID, "search")))

    def test_02_click_translate_link(self):
        # Click on the first link (Google Translate)
        self.driver.find_element(By.PARTIAL_LINK_TEXT,
                                 "Google Translate").click()
        self.driver.save_screenshot('images/test_02.png')

        time.sleep(2)

        self.wait.until(EC.url_to_be("https://translate.google.com/?hl=iw&sl=en&tl=iw&op=translate"))
        self.assertEqual(self.driver.current_url, "https://translate.google.com/?hl=iw&sl=en&tl=iw&op=translate",
                         "Did not navigate to Google Translate page.")

    def test_03_translate_qa(self):

        # Wait for the Google Translate page to load
        time.sleep(5)


        # Find the text input box for translation and enter the word 'QA'
        input_box = self.driver.find_element(By.XPATH,
                                             '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/div/c-wiz/span/span/div/textarea')
        input_box.send_keys("Quality Assurance")
        self.driver.save_screenshot('images/test_03_1.png')

        # Wait for the translation to load
        time.sleep(5)

        # Find the translation element and read its text
        translated_text = self.driver.find_element(By.XPATH, '//span[@class="ryNqvb" and @jsname="W297wb"]').text
        print(f"The translation of 'QA' is: {translated_text}")
        time.sleep(10)
        self.driver.save_screenshot('images/test_03_2.png')

        # Check the result (for example, whether the translation contains the expected word)
        self.assertIn("הבטחת איכות", translated_text)  # Check if "איכות" is in the translation
        time.sleep(10)



if __name__ == "__main__":
    unittest.main()

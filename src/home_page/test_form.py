import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from time import sleep


class TestForm(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cwd = os.getcwd() + "/web/home.html"
        cls.driver.get(f"file://{cwd}")
        cls.wait = WebDriverWait(cls.driver, 10)
        sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_fill_and_submit_form(self):

        # מילוי הטופס ושליחה
        first_name_input = self.driver.find_element(By.NAME, "first-name")
        last_name_input = self.driver.find_element(By.NAME, "last-name")
        city_select = self.driver.find_element(By.NAME, "city")
        email_input = self.driver.find_element(By.NAME, "email")
        area_code_select = self.driver.find_element(By.NAME, "area-code")
        mobile_input = self.driver.find_element(By.NAME, "mobile")

        # מילוי השדות
        first_name_input.send_keys("Niv")
        sleep(2)
        last_name_input.send_keys("Kotek")
        sleep(2)
        city_select.send_keys("Jerusalem")
        sleep(2)
        email_input.send_keys("nivk99@gmail.com")
        sleep(2)
        area_code_select.send_keys("053")
        sleep(2)
        mobile_input.send_keys("8203773")
        sleep(2)
        self.driver.save_screenshot('images/form/test_1_1.png')

        # Select gender
        gender_male_radio = self.driver.find_element(By.ID, "male")
        gender_male_radio.click()
        sleep(2)

        # Select preferred professions
        profession_math = self.driver.find_element(By.ID, "math")
        profession_math.click()
        sleep(2)
        profession_physics = self.driver.find_element(By.ID, "physics")
        profession_physics.click()
        sleep(2)
        self.driver.save_screenshot('images/form/test_1_2.png')

        # Submit the form
        submit_button = self.driver.find_element(By.ID, "submit-form")
        submit_button.click()
        sleep(2)




        # Verify the query string
        current_url = self.driver.current_url

        self.assertIn("first-name=Niv", current_url, "Query string for first name is incorrect.")
        self.assertIn("last-name=Kotek", current_url, "Query string for last name is incorrect.")
        self.assertIn("email=nivk99%40gmail.com", current_url, "Query string for email is incorrect.")
        self.assertIn("mobile=8203773", current_url, "Query string for mobile is incorrect.")
        self.assertIn("city=Jerusalem", current_url, "Query string for city is incorrect.")
        self.assertIn("area-code=053", current_url)
        self.assertIn("gender=male", current_url, "Query string for gender is incorrect.")
        self.assertIn("proffesions=math", current_url, "Query string for professions (math) is incorrect.")
        self.assertIn("proffesions=physics", current_url, "Query string for professions (physics) is incorrect.")

    def test_02_clear_form(self):
        self.driver.save_screenshot('images/form/test_2_1.png')

        # Fill out the form
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
        self.driver.find_element(By.ID, "mobile").send_keys("123-45-678")

        # Select a city
        select_city = self.driver.find_element(By.ID, "city")
        select_city.send_keys("Jerusalem")

        # Select gender
        self.driver.find_element(By.ID, "male").click()

        # Select preferred professions
        self.driver.find_element(By.ID, "math").click()

        # Clear the form
        self.driver.find_element(By.ID, "reset-form").click()
        sleep(2)

        # Verify that all fields are cleared
        self.assertEqual(self.driver.find_element(By.ID, "first-name").get_attribute("value"), "",
                         "First name field is not cleared.")
        self.assertEqual(self.driver.find_element(By.ID, "last-name").get_attribute("value"), "",
                         "Last name field is not cleared.")
        self.assertEqual(self.driver.find_element(By.ID, "email").get_attribute("value"), "",
                         "Email field is not cleared.")
        self.assertEqual(self.driver.find_element(By.ID, "mobile").get_attribute("value"), "",
                         "Mobile field is not cleared.")
        self.assertEqual(self.driver.find_element(By.ID, "city").get_attribute("value"), "---choose city---", "City selection is not cleared.")

        self.assertFalse(self.driver.find_element(By.ID, "male").is_selected(), "Male radio button is not cleared.")
        self.assertFalse(self.driver.find_element(By.ID, "female").is_selected(), "Female radio button is not cleared.")
        self.assertFalse(self.driver.find_element(By.ID, "other").is_selected(), "Other radio button is not cleared.")
        self.assertFalse(self.driver.find_element(By.ID, "math").is_selected(), "Math checkbox is not cleared.")
        self.assertFalse(self.driver.find_element(By.ID, "physics").is_selected(), "Physics checkbox is not cleared.")
        self.assertFalse(self.driver.find_element(By.ID, "biology").is_selected(), "Biology checkbox is not cleared.")
        self.assertFalse(self.driver.find_element(By.ID, "chemistry").is_selected(),
                         "Chemistry checkbox is not cleared.")
        self.assertFalse(self.driver.find_element(By.ID, "english").is_selected(), "English checkbox is not cleared.")


if __name__ == "__main__":
    unittest.main()

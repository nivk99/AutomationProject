import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
# options let you add arguments on how to start the browser
from selenium.webdriver.chrome.options import Options
import multiprocessing

def open_link(link_url, results,i):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)

    try:
        # Initialize WebDriver (e.g., with ChromeDriver)

        # Open the link
        driver.get(link_url)
        driver.save_screenshot(f'images/open_link{i}.png')



        print(f"Opened link: {link_url}")
        title = driver.title
        print(f"title - {title}")

        time.sleep(2)
        driver.find_element(By.XPATH, "//span[contains(text(),'שלחו לי פרטים') or contains(text(),'לקבלת פרטים')]")
        time.sleep(2)

        element = driver.find_element(By.XPATH, "//span[contains(text(), 'קורס')]")
        # מציאת האלמנט באמצעות CSS Selector
        element = driver.find_element(By.CSS_SELECTOR, "span.wixui-rich-text__text[style*='color:#004128;']")

        print(element.text)

        time.sleep(2)
        driver.find_element(By.XPATH, "//input[contains(@aria-label, 'שם מלא')]").send_keys("Yossi Kugel")
        first_name_value = driver.find_element(By.XPATH, "//input[contains(@aria-label, 'שם מלא')]").get_attribute(
            "value")
        results.append(first_name_value == "Yossi Kugel")  # Append result to the results list

        time.sleep(2)
        driver.find_element(By.NAME, "phone").send_keys("052111")
        phone_value = driver.find_element(By.NAME, "phone").get_attribute("value")
        results.append(phone_value == "052111")

        time.sleep(2)
        driver.find_element(By.NAME, "email").send_keys("Yossi@gmail.com")
        email_value = driver.find_element(By.NAME, "email").get_attribute("value")
        results.append(email_value == "Yossi@gmail.com")

        time.sleep(2)
        driver.find_element(By.XPATH, "//textarea[@placeholder='עוד משהו חשוב שנדע?']").send_keys("אני אוהב ללמוד")
        textarea_value = driver.find_element(By.XPATH, "//textarea[@placeholder='עוד משהו חשוב שנדע?']").get_attribute(
            "value")
        results.append(textarea_value == "אני אוהב ללמוד")

        # Wait for 2 seconds to simulate some interaction
        time.sleep(2)

    except Exception as e:
        time.sleep(10)
        print(f"Error occurred: {e}")
        results.append(False)  # Append False to indicate failure
    finally:
        # Close the browser
        driver.quit()
        print(f"נסגר הקישור: {link_url}")


class MyTestCase(unittest.TestCase):
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

    def test_01_search_hitech_school_on_google(self):
        # Perform search for "Junit" on Google
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("בית ספר להייטק וסייבר של אוניברסיטת בר אילן")
        self.assertEqual(self.driver.find_element(By.NAME, "q").get_attribute("value"),
                         "בית ספר להייטק וסייבר של אוניברסיטת בר אילן")
        self.driver.save_screenshot('images/test_1.png')

        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        # Wait for search results to load
        self.wait.until(EC.presence_of_element_located((By.ID, "search")))

    def test_02_click_hitech_school_link(self):
        # Click on the hitech_school link
        click = self.driver.find_element(By.PARTIAL_LINK_TEXT,
                                         "קורסי הייטק | בית ספר להייטק וסייבר של אוניברסיטת בר-אילן")
        self.driver.save_screenshot('images/test_2.png')

        click.click()

        time.sleep(2)

        self.wait.until(EC.url_to_be("https://www.hitech-school.biu.ac.il/"))
        self.assertEqual(self.driver.current_url, "https://www.hitech-school.biu.ac.il/",
                         "Did not navigate to hitech_school page.")

    def test_03_check_title(self):
        # Verify that the title contains "Next Page"
        title = self.driver.title
        self.assertIn(title, "קורסי הייטק | בית ספר להייטק וסייבר של אוניברסיטת בר-אילן",
                      "Page title does not contain 'קורסי הייטק | בית ספר להייטק וסייבר של אוניברסיטת בר-אילן")
        self.driver.save_screenshot('images/test_3.png')

    def test_04_QA_course_search(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element(By.XPATH, "//*[@id='comp-jvm80mrb3label']")
        self.driver.save_screenshot('images/test_4_1.png')
        element.click()
        time.sleep(2)

        find_qa = self.driver.find_element(By.XPATH, '//*[@id="input_search-box-input-comp-lki4txv1"]')
        find_qa.send_keys("QA")
        time.sleep(2)
        self.assertEqual(
            self.driver.find_element(By.XPATH, '//*[@id="input_search-box-input-comp-lki4txv1"]').get_attribute(
                "value"), "QA")
        time.sleep(2)
        self.driver.save_screenshot('images/test_4_2.png')
        find_qa.send_keys(Keys.ENTER)

        current_url = self.driver.current_url
        self.assertIn("q=QA", current_url)
        time.sleep(2)

    def test_05_writing_details(self):
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'sil_d4M').click()
        time.sleep(2)
        self.driver.save_screenshot('images/test_5_1.png')

        self.driver.find_element(By.ID, "input_comp-ls7aigyw").send_keys("Yossi Kugel")
        self.assertEqual(self.driver.find_element(By.ID, "input_comp-ls7aigyw").get_attribute("value"), "Yossi Kugel",
                         "First name field is not cleared.")
        time.sleep(2)
        self.driver.find_element(By.ID, "input_comp-ls7aigza1").send_keys("052111")
        self.assertEqual(self.driver.find_element(By.ID, "input_comp-ls7aigza1").get_attribute("value"), "052111")

        time.sleep(2)
        self.driver.find_element(By.ID, "input_comp-ls7aigzi3").send_keys("Yossi@gmail.com")
        self.assertEqual(self.driver.find_element(By.ID, "input_comp-ls7aigzi3").get_attribute("value"),
                         "Yossi@gmail.com")

        time.sleep(2)
        self.driver.find_element(By.ID, "textarea_comp-ls7aigzr1").send_keys("אני אוהב ללמוד קורס QA")
        self.assertEqual(self.driver.find_element(By.ID, "textarea_comp-ls7aigzr1").get_attribute("value"),
                         "אני אוהב ללמוד קורס QA")
        self.driver.save_screenshot('images/test_5_2.png')

        time.sleep(2)

    def test_06_main_page(self):
        self.driver.find_element(By.ID, 'comp-jvm80mrb0label').click()
        self.driver.save_screenshot('images/test_6.png')

        time.sleep(2)
        self.assertEqual(self.driver.current_url, "https://www.hitech-school.biu.ac.il/",
                         "Did not navigate to hitech_school page.")

    def test_07_courses(self):
        self.driver.find_element(By.XPATH, '//*[@id="comp-l59b9dy4"]/a/span').click()
        self.driver.save_screenshot('images/test_7_1.png')

        time.sleep(5)
        list_element = self.driver.find_element(By.CSS_SELECTOR, "div[role='list']")
        elements = list_element.find_elements(By.CSS_SELECTOR, "div[role='listitem'].Zc7IjY")
        self.assertEqual(len(elements), 18)

        for index, element in enumerate(elements):
            link = element.find_element(By.CSS_SELECTOR, "a[data-testid='linkElement']")

            # הוצאת הקישור מ-'href'
            link_url = link.get_attribute("href")
            print(f"נמצא קישור: {link_url}")

            results = multiprocessing.Manager().list()  # Using a manager to share data between processes

            # Create a process to open the link
            process = multiprocessing.Process(target=open_link, args=(link_url, results,index))

            # Start the process
            process.start()

            # Wait for the process to finish
            process.join()

            for result in results:
                self.assertTrue(result, link_url)
                print("Check - ", link_url)

            time.sleep(2)


if __name__ == '__main__':
    unittest.main()

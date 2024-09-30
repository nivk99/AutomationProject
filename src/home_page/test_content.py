import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


#  Content testing (1)

class TestContent(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cwd = os.getcwd() + "/web/home.html"
        cls.driver.get(f"file://{cwd}")
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.driver.save_screenshot('images/content/01_open page.png')
        sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_page_title(self):
        # Check the page title
        self.assertEqual(self.driver.title, "Automation Project")

    def test_main_heading(self):
        # Check if the main heading (h1) contains the text "Automation Project - Main Page"
        main_heading = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(main_heading, "Automation Project - Main Page", "Main heading text does not match.")

    def test_single_h1_element(self):
        # Check if there is exactly one h1 element on the page
        h1_elements = self.driver.find_elements(By.TAG_NAME, "h1")
        self.assertEqual(len(h1_elements), 1, "There should be exactly one h1 element.")

    def test_two_tables(self):
        # Check if there are exactly two tables on the page
        tables = self.driver.find_elements(By.TAG_NAME, "table")
        self.assertEqual(len(tables), 2, "There should be exactly two tables.")

    def test_first_table_title(self):
        # Check if the title of the first table is "Cities of the World"
        first_table_heading = self.driver.find_element(By.XPATH, "/html/body/section/main/h2[1]").text
        self.assertEqual(first_table_heading, "Cities of the World", "First table title does not match.")

    def test_second_table_title(self):
        # Check if the title of the second table is "Student Details"
        second_table_heading = self.driver.find_element(By.XPATH, "/html/body/section/main/h2[2]").text
        self.assertEqual(second_table_heading, "Student Details", "Second table title does not match.")

    def test_student_table_row_count(self):
        # Locate the "Student Details" table and check if it has 5 rows
        table = self.driver.find_element(By.XPATH, "/html/body/section/main/div[2]")
        rows = table.find_elements(By.XPATH, "/html/body/section/main/div[2]/table/tbody/tr")
        self.assertEqual(len(rows), 5, "The student table does not have 5 rows.")

    def test_student_names(self):
        # Verify the list of first names in the student table
        expected_names = ["John", "Jane", "Alice", "Michael", "Emily"]
        table = self.driver.find_element(By.XPATH, "/html/body/section/main/div[2]")
        name_cells = table.find_elements(By.XPATH,
                                         "/html/body/section/main/div[2]/table/tbody/tr/td[2]")  # 2nd column is for First Name

        # Verify the number of names matches
        self.assertEqual(len(name_cells), len(expected_names), "The number of names does not match.")

        # Verify each name
        actual_names = [cell.text for cell in name_cells]
        print(actual_names)
        self.assertEqual(set(actual_names), set(expected_names), "The list of names does not match.")


if __name__ == "__main__":
    unittest.main()

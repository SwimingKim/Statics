import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/Users/suyoung/Documents/Dev/chromedriver')
URL = "http://www.python.org"

class PythonOrgSearce(unittest.TestCase) :
    def setUp(self) :
        self.driver = driver;

    def test_searce_in_python_org(self) :
        driver = self.driver;
        driver.get(URL)
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self) :
        self.driver.close()

if __name__ == "__main__" :
    unittest.main()

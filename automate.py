from selenium import webdriver 

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    # Login test start
    def test_success_login(self):
      browser=self.browser
      browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
      time.sleep (3)

      browser.find_element(By.NAME,"username").send_keys("Admin")
      time.sleep(1)

      browser.find_element(By.NAME,"password").send_keys("admin123")
      time.sleep(1)

      browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
      time.sleep(2)

      response_data = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[1]/a/div[2]/img").text
      response_message = browser.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[1]/a/div[2]/img").text

      self.assertIn('client brand banner', response_data)
      self.assertEqual(response_message, 'client brand banner')

      # Login Test Finish

    #admin Test start 

def Admin_Test(self):
    browser=self.browser
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    browser.find_element(By.NAME,"username").send_keys("Admin")
    time.sleep(1)

    browser.find_element(By.NAME,"passdword").send_keys("admin123")
    time.sleep(1)

    browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    time.sleep(2)

    browser.find_element(BY.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
    time.sleep(2)

    
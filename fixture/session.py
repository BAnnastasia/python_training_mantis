
from selenium.webdriver.common.by import By
class SessionHelper:
    def __init__(self, app):
        self.app = app
    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
        #Login
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, '//input[@value="Login"]').click()


    def logout(self):
        driver = self.app.driver
        #Logout
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements(By.LINK_TEXT, "Logout")) > 0


    def is_logged_in_as(self, username):
        driver = self.app.driver
        return self.get_logged_user() == username
    def get_logged_user(self):
        driver =self.app.driver
        return driver.find_element(By.CSS_SELECTOR, "td.login-info-left span").text

    def ensure_login(self, username, password):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username,password)
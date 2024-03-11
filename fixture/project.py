
from selenium.webdriver.common.by import By
from model.project import Project

from selenium.webdriver.common.by import By

class ProjectHelper:
    def __init__(self, app):
        self.app = app


    def create(self, project):
        driver = self.app.driver
        self.open_manage_proj_page()
        driver.find_element(By.XPATH, "//input[@value=\'Create New Project\']").click()
        self.fild_group_form(project)
        driver.find_element(By.XPATH, "//input[@value=\'Add Project\']").click()

    def fild_group_form(self, project, clear=False):
        driver = self.app.driver
        self.app.apply_value_str_by_name(driver, "name", project.name, clear)
    def open_manage_proj_page(self):
        driver = self.app.driver
        #http://localhost/mantisbt-1.2.20/manage_proj_page.php
        if not (driver.current_url.endswith("/manage_proj_page.php")):
            driver.find_element(By.LINK_TEXT, "Manage").click()
            driver.find_element(By.LINK_TEXT, "Manage Projects").click()

    def delete_project_by_id(self, id):
        driver = self.app.driver
        self.open_manage_proj_page()
        self.select_project_by_id(id)
        driver.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        driver.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()

    def select_project_by_id(self, id):
        driver = self.app.driver
        driver.find_element(By.XPATH, "//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % id).click()
        #driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()




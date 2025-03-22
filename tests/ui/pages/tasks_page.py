from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.ui.pages.base_page import BasePage


class TasksPage(BasePage):
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
    LOG_OUT_BTN = (By.CSS_SELECTOR, "a[data-testid='nav-logout']")
    INFO_MSG = (By.CSS_SELECTOR,"div.alert.alert-info.alert-dismissible.fade.show[data-testid='flash-message-info']")
    CREATE_TASK_BTN =(By.CLASS_NAME, "btn.btn-primary")
    INPUT_NEW_TASK_TITLE = (By.ID, "title")
    INPUT_TASK_DESCRIPTION = (By.ID, "description")
    SUBMIT_BTN = (By.CSS_SELECTOR, 'button[data-testid="submit-button"]')
    TASK_TITLE = (By.CSS_SELECTOR, "h5.card-title.mb-0")
    TASK_DESC = (By.CSS_SELECTOR, "p[data-testid^='task-description-']")
    TASK_INFO_BTN = (By.CLASS_NAME, "btn.btn-sm.btn-info")
    CHANGE_TASK_STATUS_BTN = (By.CSS_SELECTOR, "button[data-testid='toggle-status-button']")
    EDIT_BTN = (By.CSS_SELECTOR, "a[data-testid='edit-button']")
    DONE_CHECKBOX =(By.ID, "completed")
    DONE_STATUS = (By.CLASS_NAME, "btn.btn-sm.btn-success")
    DELETE_BTN = (By.CSS_SELECTOR, "button[data-testid^='delete-task-button-']")
    MODAL_WINDOW = (By.CSS_SELECTOR, "div.modal-content")
    MODAL_WINDOW_DELETE = (By.CSS_SELECTOR, "button[data-testid^='delete-confirm-button-']")


    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text

    def find_username_in_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOG_OUT_BTN)
        )
        return self.find_element(self.LOG_OUT_BTN).text

    def log_out(self):
        return self.click_element(self.LOG_OUT_BTN)

    def find_info_message(self):
        return self.find_element(self.INFO_MSG).text

    def click_new_task_btn(self):
        return self.click_element(self.CREATE_TASK_BTN)

    def enter_new_task_title(self, title):
        self.enter_text(self.INPUT_NEW_TASK_TITLE, title)

    def enter_new_task_description(self, description):
        self.enter_text(self.INPUT_TASK_DESCRIPTION, description)

    def submit_task(self):
        return self.click_element(self.SUBMIT_BTN)

    def check_task_title(self):
        return self.find_element(self.TASK_TITLE).text

    def check_done_task(self):
        return self.find_element(self.DONE_STATUS)

    def check_task_description(self):
        return self.find_element(self.TASK_DESC).text

    def get_task_details(self):
        return self.click_element(self.TASK_INFO_BTN)

    def check_task_status_btn(self):
        return self.find_element(self.CHANGE_TASK_STATUS_BTN)

    def click_edit_btn(self):
        return self.click_element(self.EDIT_BTN)

    def count_tasks_with_title_duplicate(self, title):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TASK_TITLE)
        )
        tasks = self.driver.find_elements(*self.TASK_TITLE)
        return len([task for task in tasks if task.text == title])

    def mark_task_done(self):
        return self.click_element(self.DONE_CHECKBOX)

    def delete_task(self):
        self.click_element(self.DELETE_BTN)

        confirm_delete = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MODAL_WINDOW_DELETE)
        )

        self.driver.execute_script("arguments[0].scrollIntoView();", confirm_delete)
        confirm_delete.click()

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.MODAL_WINDOW)
        )


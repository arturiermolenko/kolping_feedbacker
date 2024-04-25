from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class KolpingFeedbacker():
    FEEDBACKER_LINK = "https://die-kolping-akademie-augsburg.limesurvey.net/354338?lang=de"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def leave_feedback(self) -> None:
        self.driver.get(self.FEEDBACKER_LINK)
        
        self.choose_and_weiter("datasecurity_accepted")
        self.choose_and_weiter("javatbd354338X542X5621F")
        self.choose_and_weiter("answer354338X542X5618AO05")
        self.choose_and_weiter("answer354338X542X5614AO05")
        self.choose_and_weiter("answer354338X542X5609AO05")
        self.choose_and_weiter("answer354338X542X5620AO05")
        self.choose_and_weiter("answer354338X542X5613AO05")
        self.choose_and_weiter("answer354338X542X5610AO05")
        self.choose_and_weiter("answer354338X542X5611AO05")
        self.choose_and_weiter("answer354338X542X5612AO02")
        self.choose_and_weiter("answer354338X542X5619AO05")
        self.choose_and_weiter("javatbd354338X542X5615N")
        self.choose_and_weiter("answer354338X542X5622AO05")
        self.weiter_button_click()
        sleep(5)
        # self.weiter_button_click()
        
        self.driver_quit()
    
    def choose_and_weiter(self, id: str) -> None:
        button = self.driver.find_element(By.ID, id)
        self.driver.execute_script("arguments[0].click();", button)
        sleep(1)
        self.weiter_button_click()


    def weiter_button_click(self) -> None:
        weiter_button = self.driver.find_element(By.ID, "ls-button-submit")
        self.driver.execute_script("arguments[0].click();", weiter_button)

    def driver_quit(self):
        self.driver.quit()



if __name__ == "__main__":
    feedback = KolpingFeedbacker()
    feedback.leave_feedback()


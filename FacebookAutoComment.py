from selenium import webdriver
from selenium.common.exceptions import (WebDriverException)
from webdrivermanager import ChromeDriverManager
from time import sleep
import os


class Browser:
    @staticmethod
    def openChrome():
        try:
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--headless")
            browser = webdriver.Chrome(chrome_options=chrome_options)
            return browser
        except WebDriverException:
            ChromeDriverManager().download_and_install()
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--headless")
            browser = webdriver.Chrome(chrome_options=chrome_options)
            return browser


class FacebookCommenting:
    def __init__(self, browser, email, password):
        self.browser = browser
        self.email = email
        self.password = password

    def openFacebook(self):
        self.browser.get("https://facebook.com")
        sleep(1)

    def login(self):
        emailElement = self.browser.find_element_by_id("email")
        emailElement.send_keys(self.email)
        passwordElem = self.browser.find_element_by_id("pass")
        passwordElem.send_keys(self.password)
        passwordElem.submit()
        sleep(2)
        if self.browser.current_url == "https://www.facebook.com/checkpoint/?next":
            loginCode = input("Enter login code (2-factor authentication): ")
            loginCodeElem = self.browser.find_element_by_id("approvals_code")
            loginCodeElem.send_keys(loginCode)
            buttonElem = self.browser.find_element_by_xpath(
                '//*[@id="checkpointSubmitButton"]')
            buttonElem.click()
            radioElem = self.browser.find_element_by_xpath('//*[@id="u_0_3"]')
            radioElem.click()
            sleep(0.5)
            buttonElem = self.browser.find_element_by_xpath(
                '//*[@id="checkpointSubmitButton"]')
            buttonElem.click()

    def switchPage(self, url):
        try:
            if url != "/n":
                self.browser.get(url)
        except Exception:
            url = input(
                "Enter url of the desired page correctly or press enter to continue with homepage"
            )
            self.switchPage(url)

    def selectComment(self):
        commentElem = self.browser.find_elements_by_link_text("Comment")
        return commentElem

    def comment(self, commentTabs, comment):
        for button in commentTabs:
            try:
                button.click()
                sleep(1)
            except Exception:
                continue
            commentBox = self.browser.switch_to_active_element()
            commentBox.send_keys(comment)
            commentBox.send_keys(Keys.RETURN)
            print("Done !")
            sleep(1)

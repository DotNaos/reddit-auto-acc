import time
import csv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import names
import os
from dotenv import load_dotenv

load_dotenv()
class Driver():
    def __init__(self):
        print('Starting instance...')
        load_dotenv()
        self.r_place = 'https://www.reddit.com/r/place'
        self.register = 'https://www.reddit.com/register'
        # self.base_email = 'cds.rplace@gmail.com'
        self.base_email = os.getenv('BASE-MAIL')

        # HTML Elements
        # Register
        self.email_register_field = 'regEmail'
        self.register_confirm_button = 'AnimatedForm__submitButton'

        # Choose a username
        self.username_suggestion_button = 'Onboarding__usernameSuggestion'
        self.password_field = 'regPassword'
        self.password = os.getenv('PASSWD')

        if not self.base_email:
            raise Exception('BASE-MAIL not found in .env file')
        if not self.password:
            raise Exception('PASSWD not found in .env file')


        self.driver = webdriver.Chrome()
        self.driver.get(self.register)

        # Generate mail
        self.email = self.gen_mail(self.base_email)

        # Register
        self.fill_field(self.email_register_field, By.ID, self.email)

        # Confirm
        self.click_button(self.register_confirm_button, By.CLASS_NAME)

        time.sleep(1)

        # Choose a username
        self.click_button(self.username_suggestion_button, By.CLASS_NAME)

        # Choose a password
        self.fill_field(self.password_field, By.ID, self.password)

        # save username
        self.username = self.driver.find_element(by=By.ID, value='regUsername').get_property('value')
        self.username = str(self.username)


    def end(self):
        # if register is solved then save the generated mail and its username in a csv file
        with open('mails.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([self.email, self.username])


        time.sleep(1)
        self.driver.quit()

    def gen_mail(self, mail):
        mail = mail.split('@')
        mail[0] = mail[0] + '+' + names.get_first_name() + str(random.randint(0, 1000))
        return '@'.join(mail)

    def fill_field(self, field, by, value):
        while True:
            try:
                self.driver.find_element(by=by, value=field).send_keys(value)
                break
            except:
                time.sleep(1)
                continue
            break

    def click_button(self, button, by):
        while True:
            try:
                self.driver.find_element(by=by, value=button).click()
                break
            except:
                time.sleep(1)
                continue
            break
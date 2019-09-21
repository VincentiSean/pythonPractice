#! python3
# commandEmail.py - This program takes an email (to receive the message) and a message 
#    as arguments on the command line then sends the message to the email through 
#    preset email/password login information

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Setup variables
userEmail = 'fakeEmailforPrac@gmail.com'
userPass = 'notReelThough'

# Receive command line arguments (arg 1 == receiving email && arg 2 == message to send)
print('Please enter the email of the receiver...')
receiver = input()
print('Please enter a subject line...')
subject = input()
print('Please enter the message you would like to send...')
message = input()
print('Sending email now.')

# login to gmail through preset login information
browser = webdriver.Firefox()       # set the browser as Firefox
browser.get('https://gmail.com')    # go to gmail.com

# Input email to login
emailElement = browser.find_element_by_id('identifierId')
emailElement.send_keys(userEmail)

# Click next button
nextElement = browser.find_element_by_id('identifierNext')
nextElement.click()

# Input password with a delay to trick gmail
wait = WebDriverWait(browser, 10)
passwordElem = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
passwordElem.send_keys(userPass)
passwordElem.submit()

# Click next button
nextElement = browser.find_element_by_id('passwordNext')
nextElement.click()

print('Logged in...')

# send email
compose = browser.find_element_by_xpath('//div[@gh="cm"]')  # use xpath to find "compose" because no easy identifier
compose.click()

print('Creating message...')

#sendArea = browser.find_element_by_id(':8m')
sendArea = wait.until(EC.element_to_be_clickable((By.ID, ':8m')))
sendArea.send_keys(receiver)

subjectArea = browser.find_element_by_id(':84')
subjectArea.send_keys(subject)

messageArea = browser.find_element_by_id(':99')
messageArea.send_keys(message)
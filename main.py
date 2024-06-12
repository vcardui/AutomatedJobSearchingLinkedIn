# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2024, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: June 10th, 2024
# | Last update..: June 12th, 2024
# | WhatIs.......: Automating Job Searching on LinkedIn - Main
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Locating Selenium Elements: https://selenium-python.readthedocs.io/locating-elements.html
# HTML in emails: https://docs.python.org/2/library/email-examples.html#id5

# ------------------------- Libraries -------------------------
import time  # time.sleep(1)
import datetime  # datetime.datetime.now()
import pyperclip  # pyperclip.paste()

# Send emails imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------------------- Variables -------------------------
mySkills = ['python', 'c++', 'html', 'css', 'c#', 'php']
jobsDic = {}

# Time
now = datetime.datetime.now()
todayDate = now.strftime("%d/%m/%Y")
todayTime = now.strftime("%H:%M")

emailSubject = f"Automating Job Searching on LinkedIn {todayDate} at {todayTime}"

# Emojis
computerEmoji = '&#128421;'
officeEmoji = '&#127970;'

# Email data
carduibotEmail = "carduibot@gmail.com"
carduibotPassword = ""

myEmail = "vanessa@reteguin.com"
myLinkedInPassword = ""

# --------------------------- Code ----------------------------
# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Open LinkedIn
driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3934266225&f_AL=true&keywords=Python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# Sign in (email and password)
signInForm = driver.find_element(By.LINK_TEXT, value="Sign in")
signInForm.click()

email = driver.find_element(By.ID, value="username")
email.send_keys(myEmail, )

password = driver.find_element(By.ID, value="password")
password.send_keys(myLinkedInPassword, )

signInButton = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
signInButton.click()

# Human intervention for going through captcha

# Wait until LinkedIn jobs page loads (messagingButton loads)
verifiedCaptcha = False
while not verifiedCaptcha:
    try:
        loggedIn = driver.find_element(By.XPATH,
                                       value='/html/body/div[5]/div[4]/aside[1]/div[1]/header/div[3]/button[2]')
        verifiedCaptcha = True
    except NoSuchElementException:
        time.sleep(2)

messagingButton = driver.find_element(By.XPATH,
                                      value='/html/body/div[5]/div[4]/aside[1]/div[1]/header/div[3]/button[2]')
messagingButton.click()

# Get items in list container
jobsContainer = driver.find_element(By.CLASS_NAME, value="scaffold-layout__list-container")
jobsList = jobsContainer.find_elements(By.TAG_NAME, value="li")

# Get data for each item
for item in jobsList:
    # Reset variables
    languages = []
    workModality = ""
    level = ""

    try:
        item.click()

        # Get job title
        title = driver.find_elements(By.TAG_NAME, value="h1")[1].text
        print(title)

        # Get job description and see if my skills match the requirements
        description = driver.find_element(By.ID, value="job-details")
        for skill in mySkills:
            if skill in description.text.lower():
                languages.append(skill)

        # If available, get work modality (remote, onsite, etc.) and position level (junior, senior, etc.)
        try:
            aboutTheJob = \
                driver.find_elements(By.CSS_SELECTOR, value=".job-details-jobs-unified-top-card__job-insight span")[
                    0].text.split('\n')
            workModality = aboutTheJob[0]
            level = aboutTheJob[2]
        except StaleElementReferenceException:
            print("aboutTheJob: stale element reference: stale element not found in the current frame")

        # Get work position and post's published date
        positionDetails = driver.find_elements(By.CSS_SELECTOR,
                                               value=".job-details-jobs-unified-top-card__primary-description-container div")[
            0].text.split(' · ')
        location = positionDetails[0]
        publishedDate = positionDetails[1]

        # Copying the Post's URL
        shareArrow = driver.find_element(By.XPATH,
                                         value='/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/button')
        shareArrow.click()

        copyLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                               "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div/ul/li[3]/ul/li[1]")))
        copyLink.click()

        clipboard_text = pyperclip.paste()

        # Evaluating if job offer should be saved
        if ('aguascalientes' in location.lower()) or (('python' in languages) and (workModality.lower() == 'remote')):
            print("This is a good one :)")
            saveButton = driver.find_element(By.XPATH,
                                             value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[5]/div/button')
            saveButton.click()

        jobsDic[title] = {
            "Languages": languages,
            "Location": location,
            "Work Modality": workModality,
            "Level": level,
            "Published Date": publishedDate,
            "Description": description.text,
            "Link": clipboard_text
        }
    except StaleElementReferenceException:
        print("item.click(): stale element reference: stale element not found in the current frame")
    except ElementClickInterceptedException:
        print(
            'element click intercepted: Element <li id="ember221" class="ember-view   jobs-search-results__list-item occludable-update p0 relative scaffold-layout__list-item" data-occludable-job-id="3937287243">...</li> is not clickable at point (261, 725). Other element would receive the click: <footer class="artdeco-toast-item__meta">...</footer>')

print(jobsDic)

time.sleep(30)

# Email me with jobs data

# Creating email HTML body
emailBody = """
    <html>
      <head></head>
      <body>
        <p>
            Hi miss Stark!<br>
            This is your automated job searching on LinkedIn results for today. Enjoy!<br><br>

            Best regards,<br>
            CarduiBot<br>
        </p>
    """

for i in jobsDic:
    languagesHTML = ""
    for j in jobsDic[i]['Languages']:
        if languagesHTML != "":
            languagesHTML += ", "

        if j.lower() == 'python':
            languagesHTML += f'<span style="color: #00B9BC;">{j}</span>'
        else:
            languagesHTML += j

    workModalityHTML = jobsDic[i]['Work Modality']

    if workModalityHTML == 'Remote':
        workModalityHTML += f' {computerEmoji}'
    elif workModalityHTML == 'Hybrid':
        workModalityHTML += f' {computerEmoji} + {officeEmoji}'
    elif workModalityHTML == 'On - site':
        workModalityHTML += f' {officeEmoji}'

    emailBody += f"""
           <strong>{i}</strong>
           <ul>
              <li>Languages: {languagesHTML}</li>
              <li>Location: {jobsDic[i]['Location']}</li>
              <li>Work Modality: {workModalityHTML}</li>
              <li>Level: {jobsDic[i]['Level']}</li>
              <li>Link : <a href="{jobsDic[i]['Link']}">{jobsDic[i]['Link']}</a></li>
            </ul>
        """
emailBody += """
      </body>
    </html>
    """
print(emailBody)

# Create email message container
email = MIMEMultipart('alternative')
email['Subject'] = emailSubject
email['From'] = carduibotEmail
email['To'] = myEmail

# Record the MIME type email's HTML part
HTMLPart = MIMEText(emailBody, 'html')

email.attach(HTMLPart)

print(email.as_string())

# Send message with smtplib

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=carduibotEmail, password=carduibotPassword)
connection.sendmail(from_addr=carduibotEmail,
                    to_addrs=myEmail,
                    msg=email.as_string())
connection.close()

# Close the window
driver.close()  # Close active tab
driver.quit()  # Quit the entire program

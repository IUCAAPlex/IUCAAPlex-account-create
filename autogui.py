import pyautogui
import time

from auto_script import fetch_emails

print(pyautogui.size())
print(pyautogui.position())
# pyautogui.moveTo(700, 500, duration=5)
pyautogui.click(450, 170)
# url = "https://www.iucaa.in/en/people/people-research-scholars"
# url = "https://www.iucaa.in/en/people/people-project-students"
url = "https://www.iucaa.in/en/people/people-post-doctoral-fellows"
pswd = '1234'

emails = fetch_emails(url)

for email in emails:
    pyautogui.click(120, 400)  # clicking Users button
    time.sleep(1)
    pyautogui.click(359, 242)  # clicking the + button
    pyautogui.click(368, 321)  # clicking the Name field
    pyautogui.typewrite(email)
    pyautogui.click(368, 410)  # clicking the Password field
    pyautogui.typewrite(pswd)
    pyautogui.click(270, 520)  # clicking the checkbox
    pyautogui.click(500, 590)  # clicking the save button
    time.sleep(1)


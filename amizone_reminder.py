from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import json 
from dotenv import load_dotenv
from send_email import frame_email_and_send

load_dotenv()

script_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_path)

print(script_path)

handled_companies = set()
counter = 0
config = {}

# load JSON File handled.json
with open('handled.json', 'r') as file:
    handled_file_data = json.load(file)
    if handled_file_data:
        handled_companies = set(handled_file_data['handled_companies'])
        counter = handled_file_data['counter']

with open ('config.json', 'r') as file:
    config = json.load(file)

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--window-size=1366,768")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver = webdriver.Chrome(options=options)

driver.get(config['amizone_url'])

# Adding explicit wait for username_box
username_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "_UserName")))
password_box = driver.find_element(by=By.NAME, value="_Password")

# login logic
username_box.send_keys(os.environ['AMIZONE_USERNAME'])
password_box.send_keys(os.environ['AMIZONE_PASSWORD'])
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button").click()

# check if button exists 
try:
    my_courses_button = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.ID, 'menu-toggler'))).click()
except:
    print("No Menu Toggler Found")

# Finding ATPC Placement button
my_courses_button = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'ATPC Placement'))).click()

# Finding Placement Section
placement_button = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.ID, config['Placement_Sub_Button_ID']))).click()

table_element = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="table-information"]')))
 
placement_data = table_element.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table

for company_details_row in placement_data:
    company_details = company_details_row.find_elements(By.TAG_NAME, "td")  # note: index start from 0, 1 is col 2f
    
    if len(company_details) == 6:
        sno, company_name, registration_start, registration_end, data_file, status =  company_details[0].text, company_details[1].text, company_details[2].text, company_details[3].text, company_details[4], company_details[5].text
        # Check if JSON File contains the company name
        if status == config['trigger_text'] and company_name not in handled_companies:
            file_url = data_file.find_element(By.TAG_NAME, "a").get_attribute('href')

            data = {
                'company_name': company_name,
                'registration_start': registration_start,
                'registration_end': registration_end,
                'data_file': file_url,
                'counter': counter + 1
            }
            
            frame_email_and_send(data)
            handled_companies.add(company_name)

driver.quit()

# Save handled_companies to handled.json
counter += 1
with open('handled.json', 'w') as file:
    json.dump({
        'handled_companies': list(handled_companies),
        'counter': counter
        }, file)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import csv

def append_to_csv(a, b, filename="phones.csv"):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([a, b])

def Find_Element_By_XPATH(d, x):
    WebDriverWait(d, 30).until(EC.presence_of_element_located((By.XPATH, x)))
    return d.find_element(By.XPATH, x)

def Find_Elements_By_XPATH(d, x):
    WebDriverWait(d, 30).until(EC.presence_of_all_elements_located((By.XPATH, x)))
    return d.find_elements(By.XPATH, x)

def human_typing(element, text):
    for char in text:
        element.send_keys(char)
def random_sleep(min_seconds, max_seconds):
    time.sleep(random.uniform(min_seconds, max_seconds))

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome1")  # Saved Profile
driver = webdriver.Chrome(options=chrome_options)

print("Start... 🚀")
driver.get("https://divar.ir")  # Don't change link

# Wait to load search input
divar_search = Find_Element_By_XPATH(driver, '//*[@id="app"]/header/nav/div/div[2]/div/div/div[1]/form/input')
time.sleep(1)

# Human Typing
human_typing(divar_search, "اچ سی کراس")
time.sleep(1)
divar_search.send_keys(Keys.RETURN)  # Enter on search input

time.sleep(3)  # Wait to load

def extract_phone_number(driver):
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//a[starts-with(@href, "tel:")]'))
        )
        phone_element = driver.find_element(By.XPATH, '//a[starts-with(@href, "tel:")]')
        phone_number = phone_element.get_attribute('href').replace('tel:', '').strip()
        return phone_number
    except:
        return None

def get_ads():
    try:
        return Find_Elements_By_XPATH(driver, '//article')
    except:
        return []

visited_ads = set()

while True:
    ads = get_ads()

    for ad in ads:
        try:
            ad_link = Find_Element_By_XPATH(ad, './a')
            href = ad_link.get_attribute('href')

            if not href:
                continue

            ad_id = href.split('/')[-1]
            if ad_id in visited_ads:
                continue

            visited_ads.add(ad_id)

            # Click on AD
            driver.execute_script("arguments[0].scrollIntoView(true);", ad)
            random_sleep(0.5, 1.5)  # 🌀 Delay before click on AD
            ad_link.click()

            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
            title = driver.find_element(By.TAG_NAME, 'h1').text.strip()

            random_sleep(1, 2)  # 🌀 Delay before click on Contact details button

            # Button for display number
            try:
                phone_button = Find_Element_By_XPATH(driver, '//button[contains(@class,"post-actions__get-contact")]')
                phone_button.click()
                random_sleep(1, 2)  # 🌀 Delay after Click on Button
            except Exception as e:
                print(f"❌ Couldn't find Contact Button for {title}")

            phone = extract_phone_number(driver)

            if phone:
                print(f"✅ {phone} -> {title}")
                append_to_csv(title, phone)
            else:
                print(f"❌ No phone found for {title}")

            random_sleep(1, 2.5)  # 🌀 Delay Before back to ADS list
            driver.back()
            random_sleep(1, 2.5)  # 🌀 Delay after Back

            break  # Get new list after Back

        except Exception as e:
            print(f"Error: {e}")
            try:
                driver.back()
            except:
                pass
            random_sleep(1, 2)
            continue
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting.")

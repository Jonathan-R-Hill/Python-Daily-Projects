import pandas as pd
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from msedge.selenium_tools import EdgeOptions, Edge


# make Edge headless

edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument('headless')


exe_path = "C:/Users/jonny/Desktop/Stuff/Coding related/edgedriver_win64/msedgedriver.exe"

FROM = "Newcastle"
FROM_CODE = "NCL"   # Newcastle
DATE = datetime.today().strftime('%d/%m/%Y')

# ----------------------------------- Read locations data from excel ------------------------------------- #
'''
{'Tokyo': {'IATA Code': 'TYO', 'Lowest Price': 800}, 
'Sydney': {'IATA Code': 'SYD', 'Lowest Price': 900}, 
'Seoul': {'IATA Code': 'ICN', 'Lowest Price': 550}}
'''
data = pd.read_excel("Locations.xlsx")
data_dict = data.set_index("City").to_dict('index')


for key in data_dict.items():
    browser = webdriver.Edge(executable_path=exe_path)  # capabilities=edge_options.to_capabilities()
    browser.set_window_size(1, 1)
    browser.set_window_position(1, 1)
    TO_CODE = key[1]['IATA Code']
    TO = key[0]
    url = f"https://www.expedia.co.uk/lp/flights/{FROM_CODE}/{TO_CODE}/{FROM}-to-{TO}"
    print(f'From Newcastle: {FROM_CODE} to {key[0]}: {TO_CODE}')

    browser.get(url=url)
    try:
        element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="wizard-flight-pwa-1"]/h1'))
        )
        with open("Prices.txt", 'a') as f:
            f.write(f"{DATE}\nFrom Newcastle: {FROM_CODE} TO {key[0]}: {TO_CODE}.  Cheapest price: {element.text[0:5]}\n"
                    f"{url}\n\n")
        print("Cheapest price:", element.text[0:5])
    finally:
        browser.quit()


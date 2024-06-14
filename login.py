import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

accounts = int(len(sys.argv[1:]) / 2)
print(f'Config {accounts} accounts')
for i in range(accounts):
    email = sys.argv[1 + i]
    passwd = sys.argv[1 + i + accounts]
    print('----------------------------')

    # 1. open browser
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1000, 720)
    driver.get("https://game.maj-soul.net/1/")
    print(f'Account {i + 1} loading game...')
    
    # Adding WebDriverWait to wait for elements to load
    wait = WebDriverWait(driver, 30)
    
    # Ensure the screen is loaded
    screen = wait.until(EC.presence_of_element_located((By.ID, 'layaCanvas')))
    
    # 2. Input email
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 1279.9, 278.031)\
        .click()\
        .perform()
    
    email_input = wait.until(EC.presence_of_element_located((By.NAME, 'input')))
    email_input.send_keys(email)
    print('Input email successfully')

    # 3. Input password
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 1279.9, 328.031)\
        .click()\
        .perform()
    
    password_input = wait.until(EC.presence_of_element_located((By.NAME, 'input')))
    password_input.send_keys(passwd)
    print('Input password successfully')

    # 4. Login
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 1279.9, 378.031)\
        .click()\
        .perform()
    
    print('Entering game...')
    sleep(20)  # waiting for the game to load...
    print('Login success')
    driver.quit()

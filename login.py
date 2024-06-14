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
    email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="input"]')))
    email_input.click()
    email_input.send_keys(email)
    print('Input email successfully')

    # 3. Input password
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="input_password"]')))
    password_input.click()
    password_input.send_keys(passwd)
    print('Input password successfully')

    # 4. login
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '目标按钮的CSS选择器'))) # 请替换为实际按钮的选择器
    login_button.click()
    
    print('Entering game...')
    sleep(20)  # waiting for the game to load...
    print('Login success')
    driver.quit()

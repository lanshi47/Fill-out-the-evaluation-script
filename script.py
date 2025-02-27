import time
import pandas as pd
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
import os


def scrape_current_page():
    # Define the number of pages to scrape
    n = int(os.getenv("NUM"), 20)
    for i in range(0, n):
        # 启动谷歌浏览器
        driver = webdriver.Chrome(executable_path=os.getenv("CHROME_DRIVER_PATH"))

        # 定义url
        url = os.getenv("URL")
        # 访问url
        driver.get(url)
        # 浏览器最大化
        driver.maximize_window()
        # 隐式等待
        driver.implicitly_wait(5)

        try:
            # 等待页面加载并找到账号和密码输入框
            username_field = driver.find_element('xpath', '//*[@id="username"]')  # 替换为实际的ID或其他定位符
            password_field = driver.find_element('xpath', '//*[@id="password"]')  # 替换为实际的ID或其他定位符

            # 输入账号和密码

            username_field.send_keys(os.getenv('USERNAME'))  # 替换为实际的账号
            password_field.send_keys(os.getenv('PASSWORD'))  # 替换为实际的密码

            # 点击登录按钮
            login_button = driver.find_element('xpath', '//*[@id="fm1Input"]/div[5]/div/input')  # 替换为实际的ID或其他定位符
            login_button.click()

            element_xpath = '//*[@id="memo-list"]/div[2]/div[3]/div[2]/div[3]/div[2]/div/div[2]'
            element = driver.find_element('xpath', element_xpath)


            element.click()
            excellent_options = driver.find_elements('xpath', '//*[@id="demo"]/div[2]/label[1]/span[1]')
            print(excellent_options)
            for option in excellent_options:
                driver.execute_script("arguments[0].scrollIntoView();", option)
                option.click()

            submit_button = driver.find_element('xpath', '//*[@id="survery"]/button')
            submit_button.click()
            # 等待弹窗出现并检查评分
            time.sleep(1)
            popup_xpath = '/html/body/div[5]/div/div/div/div[2]/div'
            score_text = driver.find_element('xpath', popup_xpath).text
            # 如果评分为100分，则点击确定按钮
            if "100.0" in score_text:
                confirm_button_xpath = '/html/body/div[5]/div/div/div/div[3]/a[2]'
                confirm_button = driver.find_element('xpath', confirm_button_xpath)
                confirm_button.click()


        finally:
            driver.quit()

# -*- coding: utf-8 -*-

import configparser
from selenium import webdriver


def get_config_info(file_name, group, item):
    '''get config file's information'''
    config = configparser.ConfigParser()
    config.read(file_name, encoding='utf-8')
    return config[group][item]


def auto_iine():
    '''Click Like! buttons that haven't been clicked'''
    ini_file = 'config.ini'
    url = get_config_info(ini_file, 'URL', 'url')
    mail = get_config_info(ini_file, 'LOGIN', 'mail')
    driver = webdriver.Chrome()
    driver.get(url)
    print('Please Login')
    username_element = driver.find_element_by_name('username')
    username_element.send_keys(mail)
    password_element = driver.find_element_by_name('password')
    password_element.send_keys('')
    while driver.current_url != url: pass
    print('Login Success')

    # srcが特定画像の要素取得方法 http://logic.moo.jp/data/archives/723.html
    # chromeでxpathの動作確認 http://dangerous-animal141.hatenablog.com/entry/2015/02/07/101251
    iine_elements = driver.find_elements_by_xpath("//img[contains(@src, '/images/icon_good.png')]")
    for iine_element in iine_elements:
        # Element is not clickable at point対処方法 https://javaworld.helpfulness.jp/post-254/
        # 画面スクロール方法  https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
        driver.execute_script("window.scrollTo(0, {});".format(iine_element.location['y']))
        iine_element.click()


if __name__ == '__main__':
    auto_iine()

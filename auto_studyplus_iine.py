# -*- coding: utf-8 -*-
# todo:exe形式にしてGUIをつけさせる
# todo:メールアドレスとパスワードは初回起動時空白とし
#      入力後、正常終了した場合,config.iniを作成して終了
#      次回起動時は生成したconfig.iniを使う
# todo:studyplusのトップページからログインさせ、studylogに移動し自動入力させる


import configparser
from selenium import webdriver
import time


def get_config_info(file_name, group, item):
    """get config file's information"""
    config = configparser.ConfigParser()
    config.read(file_name, encoding='utf-8')
    return config[group][item]


def auto_iine():
    """Click Like! buttons that haven't been clicked"""
    ini_file = 'config.ini'
    # url = get_config_info(ini_file, 'URL', 'url')
    mail = get_config_info(ini_file, 'LOGIN', 'mail')
    driver = webdriver.Chrome()
    driver.get('https://www.studyplus.jp/')
    login_form = driver.find_element_by_class_name('link-dummy')
    login_form.click()
    driver.implicitly_wait(5)
    print('Please Login')

    username_element = driver.find_element_by_xpath(
        '/html/body/bs-modal[1]/div/div/bs-modal-body/div/form/div[1]/div[1]/div/div[2]/input')
    username_element.send_keys(mail)
    password_element = driver.find_element_by_xpath(
        '/html/body/bs-modal[1]/div/div/bs-modal-body/div/form/div[1]/div[2]/div/div[2]/input')
    password_element.send_keys('')
    header_sub_menu_element = driver.find_element_by_id('headSubMenu-list')
    while 'マイページ' not in header_sub_menu_element.text:
        header_sub_menu_element = driver.find_element_by_id('headSubMenu-list')
        time.sleep(3)
    print('Login Success')

    # srcが特定画像の要素取得方法 http://logic.moo.jp/data/archives/723.html
    # chromeでxpathの動作確認 http://dangerous-animal141.hatenablog.com/entry/2015/02/07/101251
    iine_elements = driver.find_elements_by_xpath("//img[contains(@src, '/images/icon_good.png')]")
    for iine_element in iine_elements:
        # Element is not clickable at point対処方法 https://javaworld.helpfulness.jp/post-254/
        # 画面スクロール方法  https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
        driver.execute_script("window.scrollTo(0, {});".format(iine_element.location['y']))
        iine_element.click()
    print('Auto click was done.')


if __name__ == '__main__':
    auto_iine()

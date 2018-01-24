# -*- coding: utf-8 -*-
# todo:終了結果を何らかの形で表示させる

import configparser
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import tkinter as tk
import os
import sys


class Application(tk.Frame):
    def __init__(self, master, user_or_mail):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets(user_or_mail)

    def create_widgets(self, user_or_mail):
        self.user_or_mail_label = tk.Label(self, text='ユーザー名 or メールアドレス')
        self.user_or_mail_entry = tk.Entry(self, width=30)
        self.user_or_mail_entry.insert(tk.END, user_or_mail)
        self.password_label = tk.Label(self, text='パスワード')
        self.password_entry = tk.Entry(self, width=30)
        # 引数付きの関数の指定方法
        # https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
        self.start_button = tk.Button(self, text='開始', command=lambda: auto_iine(self))

        self.user_or_mail_label.grid(row=0, column=0)
        self.user_or_mail_entry.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)
        self.start_button.grid(row=2, column=1)


def get_config_info(file_name, group, item):
    """
    config.ini内に記載されている情報を取得する
    """
    config = configparser.ConfigParser()
    config.read(file_name, encoding='utf-8')
    return config[group][item]


def auto_iine(tk_gui):
    """
    まだクリックされていない「いいね」ボタンを押す
    """
    driver = webdriver.Chrome()
    driver.get('https://www.studyplus.jp/sign_in')

    username_element = driver.find_element_by_name('username')
    username_element.send_keys(tk_gui.user_or_mail_entry.get())
    while driver.current_url != "https://www.studyplus.jp/":
        time.sleep(3)
    studylog_button = driver.find_element_by_class_name('commonBtn')
    studylog_button.click()
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//img[contains(@src, '/images/icon_good.png')]")))

        # srcが特定画像の要素取得方法 http://logic.moo.jp/data/archives/723.html
        # chromeでxpathの動作確認 http://dangerous-animal141.hatenablog.com/entry/2015/02/07/101251
        iine_elements = driver.find_elements_by_xpath("//img[contains(@src, '/images/icon_good.png')]")
        for iine_element in iine_elements:
            # Element is not clickable at point対処方法 https://javaworld.helpfulness.jp/post-254/
            # 画面スクロール方法  https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
            driver.execute_script("window.scrollTo(0, {});".format(iine_element.location['y']))
            iine_element.click()
    except TimeoutException as e:
        pass
    sys.exit(0)


if __name__ == '__main__':
    ini_file = 'config.ini'
    user_or_mail = ''
    if os.path.exists(os.path.join(os.getcwd(), ini_file)):
        user_or_mail = get_config_info(ini_file, 'LOGIN', 'mail')
    root = tk.Tk()
    app = Application(root, user_or_mail)
    app.mainloop()

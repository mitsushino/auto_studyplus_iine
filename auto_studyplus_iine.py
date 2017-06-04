# -*- coding: utf-8 -*-

import configparser
from selenium import webdriver


def get_url():
    '''接続したいURLを設定ファイルから読み取る'''
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    return config['URL']['url']


def auto_iine():
    '''まだ、「いいね！」していないボタンを自動的にクリックする'''
    url = get_url()
    browser = webdriver.Chrome()
    browser.get(url)
    print('ログインしてください')
    while browser.current_url != url: pass
    print('ログインしました')

    # srcが特定画像の要素取得方法 http://logic.moo.jp/data/archives/723.html
    # chromeでxpathの動作確認 http://dangerous-animal141.hatenablog.com/entry/2015/02/07/101251
    iine_elements = browser.find_elements_by_xpath("//img[contains(@src, '/images/icon_good.png')]")
    for iine_element in iine_elements:
        iine_element.click()


if __name__ == '__main__':
    auto_iine()
    input('処理が完了しました')

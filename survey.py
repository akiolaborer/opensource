from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import chromedriver_binary
import time
import datetime
import math
import urllib.parse


"""
ChatGPT
環境問題に関する検索キーワードとしては、以下のようなものがあります。

CO2排出量
温室効果ガス
グローバルウォーミング
持続可能性
SDGs
3R (Reduce, Reuse, Recycle)
エコロジー
環境保護
自然環境
気候変動
再生可能エネルギー
循環型社会
経済成長と環境問題
水資源管理
持続可能な開発
環境影響評価
環境基準
環境マネジメント
環境技術
環境規制
これらのキーワードを使用することで、環境問題に関する情報をより効率的に収集することができます。
また、環境問題は多岐にわたるため、検索キーワードを組み合わせたり、具体的な問題や地域名を追加することで、より具体的な情報を得ることができます。



keywords = ["CO2排出量", "温室効果ガス", "グローバルウォーミング", "持続可能性",
           "SDGs", "3R (Reduce, Reuse, Recycle)", "エコロジー", "環境保護",
           "自然環境", "自然環境", "気候変動", "再生可能エネルギー", "循環型社会",
           "経済成長と環境問題", "水資源管理", "持続可能な開発", "環境影響評価",
           "環境基準", "環境マネジメント", "環境技術", "環境規制"]

"""

"""
ChatGPT
営業電話に関するキーワードとしては、以下のようなものがあります。

営業電話マナー
法律遵守
電話営業
顧客アプローチ
販売促進
コールセンター
CRM
アウトバウンドコール
インバウンドコール
テレマーケティング
"""

keywords = ["営業電話マナー", "法律遵守", "電話営業","顧客アプローチ", "販売促進",
            "コールセンター", "CRM", "アウトバウンドコール", "インバウンドコール", "テレマーケティング"
            ]
count = 100
min = 2
max = 15

timestamp =  datetime.datetime.now().strftime("%Y%m%d")

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

def get_tweet(keyword):
    index = 7
    #1:index[0] - index[19]
    #2:index[0] - index[13]
    domain = 'https://twitter.com/'
    query = 'search?q='
    keyword = urllib.parse.quote(keywords[index])
    filter = '&f=live'
    """
    &f=
    &f=live
    &f=user
    &f=image
    &f=video
    """
    url = domain + query + keyword + filter

    options = Options()
    #options.add_argument('--headless')

    driver = webdriver.Chrome(options = options)
    driver.get(url)
   
    WebDriverWait(driver, max).until(EC.visibility_of_element_located((By.TAG_NAME, 'article' )))
    keyword = keywords[index]
    for i in range(count):
        get_article(keyword, driver)
        scroll_to_elem(driver)
        time.sleep(min)
   
    print("tweet=", keywords[index])
    driver.quit()


def scroll_to_elem(driver):
    elems = driver.find_elements(by=By.TAG_NAME, value='article')
    last = elems[-1]

    actions = ActionChains(driver)
    actions.move_to_element(last)
    actions.perform()


def get_article(keyword, driver):
    articles = driver.find_elements(by=By.TAG_NAME, value='article')
    print("articles =", articles)
    dump = "./"+ keyword + timestamp + ".txt"
    with open(dump, "a", encoding="utf-8") as f:
        for article in articles:
            tag = article.get_attribute('innerText') 
            print("tag=", tag)
            f.writelines(tag)
            f.write('\n')


if __name__ == '__main__':
    start = time.process_time()
    get_tweet(keywords)
    end = time.process_time()
   
    se = 2 * math.sqrt((0.5 * (1 - 0.5)) / count)
    #信用区間95％、回答比率は0.5で固定の値を用いる

    print("count=", count)
    print("standard error= ", se)
    print("start, end=", '{0}, {1}'.format(start, end)) 
    









    



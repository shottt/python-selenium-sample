from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.support.ui import Select
import time

# ドライバー指定でChromeブラウザを開く
CHROMEDRIVER = './chromedriver'
chrome_service = fs.Service(executable_path=CHROMEDRIVER)
browser = webdriver.Chrome(service=chrome_service)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# ヘッドレスブラウザで立ち上げる場合の設定（GUI立ち上がらない）
# options.add_argument('--headless')
# browser = webdriver.Chrome(service=chrome_service, options=options)

# 待機時間（10秒）を設定
browser.implicitly_wait(10)
browser.get('https://www.library.chiyoda.tokyo.jp/')

#千代田図書館の開館状況を取得
# schedule_el = browser.find_elements(By.XPATH, '//li[@id="chiyoda-today-status"]/div/div/span')
# print([s.text for s in schedule_el])

# Pythonプログラミングで検索
text_box = browser.find_element(By.NAME, 'txt_word')
text_box.send_keys('Pythonプログラミング')
btn = browser.find_element(By.NAME, 'submit_btn_searchEasy')
btn.click()

# 昇順設定
order = browser.find_element(By.ID, 'opt_oder')
order_select = Select(order)
order_select.select_by_value('0')

# 再表示
btn_sort = browser.find_element(By.NAME, 'submit_btn_sort')
btn_sort.click()

# 5秒間結果のウィンドウを開いたままにする
time.sleep(5)
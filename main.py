from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

def get_source_html(url):
    driver = webdriver.Firefox()
    driver.maximize_window()
    try:
        print('[ + ] Driver getting url!')
        driver.get(url = url)
        print('[ + ] Driver url found succefully!')
        sleep(1)
        sell_extracted_info = driver.find_element(By.ID, 'market_commodity_forsale')
        request_extracted_info = driver.find_element(By.ID, 'market_commodity_buyrequests')
        print('[ + ] Class text extracted succefully!')
        sleep(1)
        print('[INFO]')
        print(sell_extracted_info.text)
        print(request_extracted_info.text)
    except Exception:
        print('[ - ] Error! Please, check your url or class name!')
    finally:
        driver.close()
        driver.quit()
def get_url(string=input('Insert your steam market item name here : '), game=input('Insert your game name here : ')):
    games = {
    'Dota 2' : '570',
    'Rust' : '252490',
    'CSGO' : '730'
}
    words = string.split()
    result_string = ''
    result_string += words[0]
    for i in range(1, len(words)):
        result_string += f'%20{words[i]}'
    return f'https://steamcommunity.com/market/listings/{games[game]}/{result_string}'
def main():
    get_source_html(get_url())
if __name__ == '__main__':
    main()

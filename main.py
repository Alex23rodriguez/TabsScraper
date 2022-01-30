# %%
import imp
from bs4 import BeautifulSoup
import json
from time import sleep
from selenium import webdriver
import json
# %%


def wait_for_element(func, tag, tries=50, timeout=0.5, cooldown=1):
    sleep(cooldown)
    for _ in range(tries):
        try:
            elem = func(tag)
            sleep(cooldown)
            return elem
        except:
            sleep(timeout)
    assert False, f'{tag} element not found after {timeout * tries} seconds'


# %%
# Settings
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.dir",
                  "/Users/alex/Documents/Code/Python/WebScrapping/")
fp.set_preference("browser.download.folderList", 2)


def main():
    d = webdriver.Firefox(fp)
    url = 'https://www.ultimate-guitar.com/top/tabs'
    d.get(url)
    sleep(1)


def get_explore_page(page_num):
    return f'https://www.ultimate-guitar.com/explore?order=hitstotal_desc&page={page_num}'


def get_songs_in_page(d, page_num):
    d.get(get_explore_page(page_num))
    songs = d.find_elements_by_tag_name(
        'section')[2].find_elements_by_tag_name('header')[1:]

    return [header.find_element_by_tag_name('a').get_attribute('href') for header in songs]


# %%
d = webdriver.Firefox(fp)
# %%
song_urls = []
for i in range(1, 21):
    song_urls += get_songs_in_page(d, i)
# %%
len(song_urls)

# %%
json.dump(song_urls, open('song_urls.json', 'w'))
# %%

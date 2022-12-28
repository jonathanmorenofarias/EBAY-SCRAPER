import pandas as pd
from bs4 import BeautifulSoup
import request

url_main = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='
product = 'rx6700xt'
url_rest = '&_sacat=0&LH_BIN=1&rt=nc&LH_ItemCondition=1000%7C3000%7C1500&_pgn='
page_num = '1'

url = url_main + product + url_rest + page_num


import requests
from bs4 import BeautifulSoup
import lxml
import csv
import pandas as pd
import xlwt
import xlrd
import re
from openpyxl.workbook import Workbook


def get_2019_wine(url_real):
    r = requests.get(url_real, timeout=20)
    soup = BeautifulSoup(r.text, 'lxml')
    # div_all = soup.find_all('div', {'id': 'content'})
    div_all = soup.find_all('tr', {'class': True})
    # print(div_all)
    workbook = xlwt.Workbook(encoding='utf-8')
    writebook = xlwt.Workbook(r'farr.xlsx')
    cell_overwrite_ok=True
    sheet = writebook.add_sheet('test1',cell_overwrite_ok)
    row = 1

    for wine in div_all:
        wine_info = wine.find('a', href=True)
        # print('11111111111111111')
        wine_info_link = wine_info['href']
        wine_info_link_full = 'https://www.farrvintners.com'+wine_info_link
        print(wine_info_link_full)
        wine_info_name = wine_info.text
        print(wine_info_name)
        r1 = requests.get(wine_info_link_full, timeout=20)
        soup1 = BeautifulSoup(r1.text, 'lxml')
        div_sub = soup1.find_all('tr',{'class', True})
        sheet.write(row, 1, wine_info_name)
        sheet.write(row, 2, wine_info_link_full)
        for i in div_sub:
            div_farr = i.find('span', {'class','notranslate'})
            div_name_farr = i.find('i')
            try:
                div_name_farr_con = div_name_farr.text
                div_farr_point = div_farr.text
                div_name_sum= div_name_farr_con[0:7]
                if div_name_sum == 'Farr Vi':
                    print(div_name_farr_con)
                    print(div_farr_point)
                    sheet.write(row, 3, div_farr_point)
                elif div_name_sum == 'Neal Ma':
                    print(div_name_farr_con)
                    print(div_farr_point)
                    sheet.write(row, 4, div_farr_point)
                elif div_name_sum == 'James L':
                    print(div_name_farr_con)
                    print(div_farr_point)
                    sheet.write(row, 5, div_farr_point)
                elif div_name_sum == 'James S':
                    print(div_name_farr_con)
                    print(div_farr_point)
                    sheet.write(row, 6, div_farr_point)
                elif div_name_sum == 'Antonio':
                    print(div_name_farr_con)
                    print(div_farr_point)
                    sheet.write(row, 7, div_farr_point)
                elif div_name_sum == 'Jane An':
                    print(div_name_farr_con)
                    print(div_farr_point)
                    sheet.write(row, 8, div_farr_point)
                elif div_name_sum == 'Lisa Pe':
                    print(div_name_farr_con)
                    print(div_farr_point)
                    sheet.write(row, 9, div_farr_point)

            except AttributeError:
                continue
        row = row + 1

    writebook.save('farr.xlsx')





def main():

    root_2019_url = 'https://www.farrvintners.com/en_primeur/winelist.php?rows_per_page=-1'
    get_2019_wine(root_2019_url)



if __name__ == '__main__':
        main()
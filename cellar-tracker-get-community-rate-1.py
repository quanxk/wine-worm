import requests
from bs4 import BeautifulSoup
import lxml
import csv
# import pandas as pd
import xlwt
import xlrd
import re
# from openpyxl.workbook import Workbook


def get_comm_wine(url_real):
    wine_link_list = []
    c = '#selected%3DW3281014_21_Kcad808d20554f65117a43a2d39f9fa4f'
    for i in range(1,3):
        b=str(i)
        url_full = url_real+b+c
        print(url_full)
        r = requests.get(url_full, timeout=20)
        soup = BeautifulSoup(r.text, 'lxml')
        # div_all = soup.find_all('div', {'class': 'produit_description'})
        print(soup)
        div_all = soup.find_all('td',{'class','score'})
        print (div_all)
    #     for wine in div_all:
    #         wine_info = wine.find('a', href=True)
    #         wine_info_link = wine_info['href']
    #         # print(wine_info_link)
    #         wine_link_full = 'https://www.chateauprimeur.com'+wine_info_link
    #         print(wine_link_full)
    #         wine_link_list.append(wine_link_full)
    # print(wine_link_list)
    return (wine_link_list)

# def get_2019_point(wine_url_list):
#     row = 1
#     workbook = xlwt.Workbook(encoding='utf-8')
#     writebook = xlwt.Workbook(r'chateau-primeur.xlsx')
#     cell_overwrite_ok = True
#     sheet = writebook.add_sheet('test1', cell_overwrite_ok)
#     for i in wine_url_list:
#         r = requests.get(i, timeout=20)
#         soup = BeautifulSoup(r.text, 'lxml')
#         div_all = soup.find_all('ul', {'class': 'produit_notations'})
#         div_1 = soup.find('span', {'class': 'produit_nom'})
#         div_2 = soup.find('span', {'class': 'produit_classement'})
#         div_3 = soup.find('span', {'class': 'produit_appellation'})
#         div_name = div_1.text
#         div_class = div_2.text
#         div_terr = div_3.text
#         print(div_name,div_class,div_terr)
#
#         sheet.write(row, 1, div_name)
#         sheet.write(row, 2, div_class)
#         sheet.write(row, 3, div_terr)
#         sheet.write(0, 1, 'Wine name')
#         sheet.write(0, 2, 'Wine Classe')
#         sheet.write(0, 3, 'Terror')
#         sheet.write(0, 4, 'Bettane & Desseauve')
#         sheet.write(0, 5, 'Terre de Vins')
#         sheet.write(0, 6, 'Decanter')
#         sheet.write(0, 7, 'Anthocyanes/Y.Castaing')
#         sheet.write(0, 8, 'J.Suckling')
#         sheet.write(0, 9, 'JMQuarin')
#         sheet.write(0, 10, 'Vinous–N.Martin')
#         sheet.write(0, 11, 'WineCellarInsider/JeffLeve')
#         sheet.write(0, 12, 'Vinous-A.Galloni')
#         sheet.write(0, 13, 'WineAdvocate/L.Perrotti')
#         sheet.write(0, 14, 'Jeb Dunnuck')
#         sheet.write(0, 15, 'link')
#         sheet.write(row, 15, i)
#
#         # print(div_all)
#         for j in div_all:
#             wine_line = j.find_all('li')
#             for k in wine_line:
#                 wine_name_1 = k.text
#                 # print(wine_name_1)
#                 wine_rate_name = wine_name_1
#                 # print(wine_rate_name)
#                 wine_split = wine_rate_name.split(':')
#                 wine_name_r = wine_split[0]
#                 wine_point = wine_split[1]
#                 wine_name_abc=wine_name_r.replace(' ','')
#                 wine_name_abb = wine_name_abc.replace('\n','')
#                 print(wine_name_abb)
#                 # print('11111111')
#
#                 if wine_name_abb == 'Bettane&Desseauve':
#                     sheet.write(row, 4, wine_point)
#                     print(wine_point)
#                 elif wine_name_abb == 'TerredeVins':
#                     sheet.write(row, 5, wine_point)
#                     print(wine_point)
#                 elif wine_name_abb == 'Decanter':
#                     sheet.write(row, 6, wine_point)
#                     print(wine_point)
#                 elif wine_name_abb == 'Anthocyanes/Y.Castaing':
#                     sheet.write(row, 7, wine_point)
#                     print(wine_point)
#                 elif wine_name_abb == 'J.Suckling':
#                     sheet.write(row, 8, wine_point)
#                     print(wine_point)
#                 elif wine_name_abb == 'JMQuarin':
#                     sheet.write(row, 9, wine_point)
#                     print(wine_point)
#                 elif wine_name_abb == 'Vinous–N.Martin':
#                     sheet.write(row, 10, wine_point)
#                     print(wine_point)
#                 elif wine_name_abb == 'WineCellarInsider/JeffLeve':
#                     sheet.write(row, 11, wine_point)
#                     print(wine_point)
#                 elif wine_name_abb == 'Vinous-A.Galloni':
#                     sheet.write(row, 12, wine_point)
#                     print(wine_point)
#                 elif wine_name_abb == 'WineAdvocate/L.Perrotti':
#                     sheet.write(row, 13, wine_point)
#                     print(wine_point)
#                 elif wine_name_abb == 'JebDunnuck':
#                     sheet.write(row, 14, wine_point)
#                     print(wine_point)
#
#         row = row+1
#
#     writebook.save('chateau-primeur.xlsx')


def main():

    root_cell_url = 'https://www.cellartracker.com/list.asp?VB=2000&iUserOverride=0&Table=List&Country=France&O=CScoreSort+DESC&Region=Bordeaux&Type=Red&VT=2020&Page='
    get_comm_wine(root_cell_url)



if __name__ == '__main__':
        main()
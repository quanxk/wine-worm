import requests
from bs4 import BeautifulSoup
import lxml
import csv
import pandas as pd
import xlwt
import xlrd
from openpyxl.workbook import Workbook

def get_100_wine(i):
    url2 = '?showOutOfStock=true&ratingmin=100'
    url_real = 'https://www.wine.com/list/wine/7155/' + i + url2
    r = requests.get(url_real,timeout = 20)
    soup = BeautifulSoup(r.text,'lxml')
    div_all = soup.find_all('div',{'class':'prodItem_wrap'})

    wine_unit_list = []
    wine_list = []
    wine_ini = []
    wine_unit_ini = []
    wine_point = []
    wine_unit_point = []

    for wine1 in div_all:
        div_name = wine1.find('span', {'itemprop': 'name'}, {'class': 'prodItemInfo_name'})

        wine_unit_list.append(div_name.text)
        div_ini = wine1.find_all('span', {'class': 'wineRatings_initials'})
        for ini in div_ini:
            div_ivi_1 = ini.text
            wine_unit_ini.append(div_ivi_1)


        div_point = wine1.find_all('span', {'class': 'wineRatings_rating'})
        for point in div_point:
            div_point_1 = point.text
            wine_unit_point.append(div_point_1)


        wine_list.append(wine_unit_list)
        wine_ini.append(wine_unit_ini)
        wine_point.append(wine_unit_point)

        wine_unit_list = []
        wine_unit_point = []
        wine_unit_ini = []

    return wine_list,wine_ini,wine_point





def main():
    url = 'https://www.wine.com/list/wine/napa-valley/7155-106882/'
    url2 = '?showOutOfStock=true'
    wine_list=[]
    wine_ini=[]
    wine_point=[]
    wine_list_i = []
    wine_ini_i = []
    wine_point_i = []



    wine_list_1, wine_ini_1, wine_point_1 = get_100_wine('')
    pd_list_result = pd.DataFrame(wine_list_1)
    pd_ini_result = pd.DataFrame(wine_ini_1)
    pd_point_result = pd.DataFrame(wine_point_1)

    for i in range(2,41):
        wine_list_i, wine_ini_i, wine_point_i = get_100_wine(str(i))
        pd_ini_i = pd.DataFrame(wine_ini_i)
        pd_list_i = pd.DataFrame(wine_list_i)
        pd_point_i = pd.DataFrame(wine_point_i)
        pd_ini_result = pd_ini_result.append(pd_ini_i)
        pd_list_result = pd_list_result.append(pd_list_i)
        pd_point_result = pd_point_result.append(pd_point_i)


        if i % 3 == 0:
            print('完成{}页'.format(i))

    col_name = pd_ini_result.columns.tolist()  # 将数据框的列名全部提取出来存放在列表里
    col_name.insert(0, 'name')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['name'] = pd_list_result

    col_name.insert(2, 'p1')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p1'] = pd_point_result[0]

    col_name.insert(4, 'p2')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p2'] = pd_point_result[1]


    col_name.insert(6, 'p3')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p3'] = pd_point_result[2]

    col_name.insert(8, 'p4')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p4'] = pd_point_result[3]

    col_name.insert(10, 'p5')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p5'] = pd_point_result[4]


    col_name.insert(12, 'p6')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p6'] = pd_point_result[5]


    col_name.insert(14, 'p7')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p7'] = pd_point_result[6]


    col_name.insert(16, 'p8')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p8'] = pd_point_result[7]



    writer = pd.ExcelWriter('/Users/xiaoke/wine-100-point.xlsx')
#    pd_list_result.to_excel(writer,sheet_name='list')
    pd_ini_result.to_excel(writer,sheet_name='wine')
#    pd_point_result.to_excel(writer, sheet_name='point')
    writer.save()


if __name__ == '__main__':
    main()
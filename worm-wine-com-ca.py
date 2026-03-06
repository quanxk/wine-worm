import requests
from bs4 import BeautifulSoup
import lxml
import csv
import pandas as pd
import xlwt
import xlrd
from openpyxl.workbook import Workbook

def get_100_wine(i):
    url2 = '?showOutOfStock=true'
    url_real = 'https://www.wine.com/list/wine/napa-valley/7155-106882/' + i + url2
    r = requests.get(url_real,timeout = 20)
    soup = BeautifulSoup(r.text,'lxml')
    div_all = soup.find_all('div',{'class':'prodItem_wrap'})
    # div_name = soup.find_all('span',{'itemprop':'name'},{'class':'prodItemInfo_name'})
    # div_ini = soup.find_all('span',{'class':'wineRatings_initials'})
    # div_point = soup.find_all('span',{'class':'wineRatings_rating'})
    wine_list=[]
    wine_unit_list = []
    wine_ini = []
    wine_unit_ini = []
    wine_point = []
    wine_unit_point = []

    for wine1 in div_all:
        div_name = wine1.find('span', {'itemprop': 'name'}, {'class': 'prodItemInfo_name'})
#       div_name_1 = div_name.find_all(title)
#       div_name_1 = div_name.find_all('span', {'class': 'prodItemInfo_name'}, {'itemprop': 'name'}, {'title'})
        #print(div_name)
        wine_unit_list.append(div_name.text)
        div_ini = wine1.find_all('span', {'class': 'wineRatings_initials'})
        for ini in div_ini:
            div_ivi_1 = ini.text
            wine_unit_ini.append(div_ivi_1)

            #wine_unit_ini = []
            #print('hi')
            #print(div_ivi_1)
        div_point = wine1.find_all('span', {'class': 'wineRatings_rating'})
        for point in div_point:
            div_point_1 = point.text
            wine_unit_point.append(div_point_1)

            #wine_unit_point = []
            #print(div_point_1)
        wine_list.append(wine_unit_list)
        wine_ini.append(wine_unit_ini)
        wine_point.append(wine_unit_point)
        # print(wine_unit_list)
        # print(wine_ini)
        # print(wine_point)
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
    # pd_list_result = []
    # pd_ini_result = []
    # pd_point_result = []
    # wine_list_4 = []
    # wine_ini_4 = []
    # wine_point_4 = []

    wine_list, wine_ini, wine_point = get_100_wine('')
    pd_ini = pd.DataFrame(wine_ini)
    pd_list = pd.DataFrame(wine_list)
    pd_point = pd.DataFrame(wine_point)
    for i in range(2,1231):
        wine_list_i, wine_ini_i, wine_point_i = get_100_wine('/{}'.format(i))
        pd_ini_i = pd.DataFrame(wine_ini_i)
        pd_list_i = pd.DataFrame(wine_list_i)
        pd_point_i = pd.DataFrame(wine_point_i)
        pd_list_result = pd_list.append(pd_list_i)
        pd_ini_result = pd_ini.append(pd_ini_i)
        pd_point_result = pd_point.append(pd_point_i)


    # print(pd_ini_result)
    print(pd_list_result)
    print(pd_ini_result)
    print(pd_point_result)
    col_name = pd_ini_result.columns.tolist()  # 将数据框的列名全部提取出来存放在列表里
    #col_point = pd_point_result.columns.tolist()
    #print('point: ',col_point)
    print(col_name)
    col_name.insert(0,'name')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['name'] = pd_list_result

    col_name.insert(2, 'p1')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p1'] = pd_point_result[0]
    print(col_name)
    print(pd_point_result[1])
    col_name.insert(4, 'p2')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p2'] = pd_point_result[1]
    print(col_name)
    print(pd_point_result[2])

    col_name.insert(6, 'p3')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p3'] = pd_point_result[2]
    print(col_name)

    col_name.insert(8, 'p4')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p4'] = pd_point_result[3]
    print(col_name)

    col_name.insert(10, 'p5')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p5'] = pd_point_result[4]
    print(col_name)

    col_name.insert(12, 'p6')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p6'] = pd_point_result[5]
    print(col_name)

    col_name.insert(14, 'p7')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p7'] = pd_point_result[6]
    print(col_name)

    col_name.insert(16, 'p8')
    pd_ini_result = pd_ini_result.reindex(columns=col_name)
    pd_ini_result['p8'] = pd_point_result[7]
    print(col_name)

    writer = pd.ExcelWriter('/Users/xiaoke/wine-list-ca.xlsx')
    #pd_list_result.to_excel(writer,sheet_name='list')
    pd_ini_result.to_excel(writer,sheet_name='wine')
    #pd_point_result.to_excel(writer, sheet_name='point')
    writer.save()


if __name__ == '__main__':
    main()
import requests
from bs4 import BeautifulSoup
import xlwt


def get_100_wine(i):
    url1 = 'https://www.wine.com/list/wine/bordeaux/red-wine/vintage-2018/7155-107078-124-383'
    url2 = '?showOutOfStock=true&sortBy=topRated'
    url3 = '/'

    workbook = xlwt.Workbook(encoding='utf-8')
    wine_row0 = 1
    wine_row1 = 0
    wine_col0 = 0
    wine_col1 = 0
    count = 0
    worksheet = workbook.add_sheet('Bordeaux2018索引')
    worksheet.write(0, 0, 'Name')
    worksheet.write(0, 1, 'Link')
    worksheet.write(0, 2, 'WS')
    worksheet.write(0, 3, 'Status')
    worksheet.write(0, 4, 'JS')
    worksheet.write(0, 5, 'Status')
    worksheet.write(0, 6, 'D')
    worksheet.write(0, 7, 'Status')
    worksheet.write(0, 8, 'JD')
    worksheet.write(0, 9, 'Status')
    worksheet.write(0, 10, 'WA')
    worksheet.write(0, 11, 'Status')
    worksheet.write(0, 12, 'AG')
    worksheet.write(0, 13, 'Status')

    for i in range(1,7):
        url_real1 = url1 + url3 + str(i) + url2
        r = requests.get(url_real1, timeout=20)
        soup = BeautifulSoup(r.text, 'lxml')
        div_all1 = soup.find_all('div', {'class': 'prodItemInfo'})

        for wine1 in div_all1:
            div_name1 = wine1.find('span', {'itemprop': 'name'}, {'class': 'prodItemInfo_name'})
            div_link = wine1.find('a', {'class': 'prodItemInfo_link'})
            print(div_name1.text)
            div_link1 = div_link.get('href')
            div_link_final = 'https://wine.com/' + div_link1
            print(div_link_final)
            count += 1
            worksheet.write(wine_col0 + count, 0, div_name1.text)
            worksheet.write(wine_col0 + count, 1, div_link_final)
            r1 = requests.get(div_link_final, timeout=20)
            soup = BeautifulSoup(r1.text, 'lxml')
            div_all2 = soup.find_all('div', {'class': 'pipProfessionalReviews_list'})

            for wine2 in div_all2:
                div_rate2 = wine2.find('span', {'class': 'wineRatings_initials'})
                div_rate3 = wine2.find('span', {'class': 'wineRatings_rating'})
                div_rate1 = wine2.find('div', {'class': 'pipSecContent_copy'})
                div_rate11 = div_rate1.text
                div_rate4 = div_rate11.find('Barrel Sample')
                if div_rate2.text == 'WS':
                    worksheet.write(wine_col0 + count, 2, div_rate3.text)
                    if div_rate4 == -1:
                        worksheet.write(wine_col0 + count, 3, 'In Bottle')
                    else:
                        worksheet.write(wine_col0 + count, 3, 'Barrel Sample')
                elif div_rate2.text == 'JS':
                    worksheet.write(wine_col0 + count, 4, div_rate3.text)
                    if div_rate4 == -1:
                        worksheet.write(wine_col0 + count, 5, 'In Bottle')
                    else:
                        worksheet.write(wine_col0 + count, 5, 'Barrel Sample')
                elif div_rate2.text == 'D':
                    worksheet.write(wine_col0 + count, 6, div_rate3.text)
                    if div_rate4 == -1:
                        worksheet.write(wine_col0 + count, 7, 'In Bottle')
                    else:
                        worksheet.write(wine_col0 + count, 7, 'Barrel Sample')
                elif div_rate2.text == 'JD':
                    worksheet.write(wine_col0 + count, 8, div_rate3.text)
                    if div_rate4 == -1:
                        worksheet.write(wine_col0 + count, 9, 'In Bottle')
                    else:
                        worksheet.write(wine_col0 + count, 9, 'Barrel Sample')
                elif div_rate2.text == 'RP':
                    worksheet.write(wine_col0 + count, 10, div_rate3.text)
                    if div_rate4 == -1:
                        worksheet.write(wine_col0 + count, 11, 'In Bottle')
                    else:
                        worksheet.write(wine_col0 + count, 11, 'Barrel Sample')
                elif div_rate2.text == 'V':
                    worksheet.write(wine_col0 + count, 12, div_rate3.text)
                    if div_rate4 == -1:
                        worksheet.write(wine_col0 + count, 13, 'In Bottle')
                    else:
                        worksheet.write(wine_col0 + count, 13, 'Barrel Sample')
                print(div_rate2.text)
                print(div_rate3.text)
                print(div_rate1.text)
                if div_rate4 == -1:
                    print('In Bottle')
                else:
                    print('Barrel Sample')

            print('-----------------------------------分割线---------------------------------------------')

    workbook.save('wine-bordeaux-2018.xls')
    print('您的文件： wine-bordeaux-2018.xls 已经成功生成')

def main():

    get_100_wine('')

if __name__ == '__main__':
    main()
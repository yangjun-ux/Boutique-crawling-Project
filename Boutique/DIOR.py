from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
import urllib.request
import pandas as pd

# 디올 남성 의류

def dior_clothes():    
    url_base = 'https://www.dior.com/ko_kr'
    url_sub = '/%EB%82%A8%EC%84%B1-%ED%8C%A8%EC%85%98/%EB%A0%88%EB%94%94-%ED%88%AC-%EC%9B%A8%EC%96%B4/%EC%A0%84%EC%B2%B4-%EB%A0%88%EB%94%94-%ED%88%AC-%EC%9B%A8%EC%96%B4'
    url = url_base + url_sub
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    brand = []
    name = []
    price = []
    img = []
    sex = []
    url = []
    for item in soup.find_all('div', 'product product-legend-bottom product--cdcbase'):
        brand.append('Dior')
        name.append(item.find(class_='multiline-text').get_text())
        price.append(item.find(class_='price-line').get_text().replace('₩', ''))
        img.append(item.find('img')['src'])
        sex.append('Men')
        url.append(urljoin(url_base, item.find('a')['href']))
# dataframe        
    data = {'title': name, 'price': price, 'image': img, 'sex': sex, 'brand': brand}
    df_mens_clothes = pd.DataFrame(data)

# download images
    print('남성의류 사진 저장을 시작합니다')
    for idx, link in enumerate(img):
        urllib.request.urlretrieve(link, 'dior mens clothes/' + 'dior' + str(idx) + '.jpg')

# 디올 여성 의류 
    url_base = 'https://www.dior.com/ko_kr'
    url_sub = '/%EC%97%AC%EC%84%B1-%ED%8C%A8%EC%85%98/%EC%97%AC%EC%84%B1-%EC%9D%98%EB%A5%98/%EC%A0%84%EC%B2%B4-%EB%A0%88%EB%94%94-%ED%88%AC-%EC%9B%A8%EC%96%B4'
    url = url_base + url_sub
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    brand = []
    name = []
    price = []
    img = []
    sex = []
    url = []
    for item in soup.find_all('div', 'product product-legend-bottom product--cdcbase'):
        brand.append('Dior')
        name.append(item.find(class_='multiline-text').get_text())
        price.append(item.find(class_='price-line').get_text().replace('₩', ''))
        img.append(item.find('img')['src'])
        sex.append('Women')
        url.append(urljoin(url_base, item.find('a')['href']))

# dataframe
    data = {'title': name, 'price': price, 'image': img, 'sex': sex, 'brand': brand}
    df_womens_clothes = pd.DataFrame(data)   

# concat data
    dior_clothes_df = pd.concat([df_mens_clothes, df_womens_clothes]).reset_index(drop=True)
    dior_clothes_df.to_csv('dior_clothes.csv', index=False, encoding='utf-8')
# download images
    print('여성의류 사진 저장을 시작합니다')
    for idx, link in enumerate(img):
        urllib.request.urlretrieve(link, 'dior womens clothes/' + 'dior' + str(idx) + '.jpg')
    
    return dior_clothes_df


# 디올 남성 가방

def dior_bags():   
    
    url_base = 'https://www.dior.com/ko_kr'
    url_sub = '/%EB%82%A8%EC%84%B1-%ED%8C%A8%EC%85%98/%EA%B0%80%EC%A3%BD-%EC%A0%9C%ED%92%88/%EC%A0%84%EC%B2%B4-%EA%B0%80%EC%A3%BD-%EC%A0%9C%ED%92%88'
    url = url_base + url_sub
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    brand = []
    name = []
    price = []
    img = []
    sex = []
    url = []

    for item in soup.find_all('div', 'product product-legend-bottom product--cdcbase'):
        brand.append('Dior')
        name.append(item.find(class_='multiline-text').get_text())
        price.append(item.find(class_='price-line').get_text().replace('₩', ''))
        img.append(item.find('img')['src'])
        sex.append('Men')
        url.append(urljoin(url_base, item.find('a')['href']))
    
# dataframe : dior mens bags
    data = {'title': name, 'price': price, 'image': img, 'sex': sex, 'brand': brand}
    df_mens_bags = pd.DataFrame(data)
    
# download images
    print('남성가방 사진 저장을 시작합니다')
    for idx, link in enumerate(img):
        urllib.request.urlretrieve(link, 'dior mens bags/' + 'dior' + str(idx) + '.jpg')

# 디올 여자 가방
    url_base = 'https://www.dior.com/ko_kr'
    url_sub = '/%EC%97%AC%EC%84%B1-%ED%8C%A8%EC%85%98/%EC%97%AC%EC%84%B1-%EA%B0%80%EB%B0%A9/%EB%AA%A8%EB%93%A0-%EA%B0%80%EC%A3%BD%EC%A0%9C%ED%92%88'
    url = url_base + url_sub
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    brand = []
    name = []
    price = []
    img = []
    sex = []
    url = []

    for item in soup.find_all('div', 'product product-legend-bottom product--cdcbase'):
        brand.append('Dior')
        name.append(item.find(class_='multiline-text').get_text())
        price.append(item.find(class_='price-line').get_text().replace('₩', ''))
        img.append(item.find('img')['src'])
        sex.append('women')
        url.append(urljoin(url_base, item.find('a')['href']))
    
# dataframe : dior women bags
    data = {'title': name, 'price': price, 'image': img, 'sex': sex, 'brand': brand}
    df_womens_bags = pd.DataFrame(data)
    
# concat data
    dior_bags_df = pd.concat([df_mens_bags, df_womens_bags]).reset_index(drop=True)
    dior_bags_df.to_csv('dior_bags.csv', index=False, encoding='utf-8')

# download images
    print('여성가방 사진 저장을 시작합니다')
    for idx, link in enumerate(img):
        urllib.request.urlretrieve(link, 'dior womens bags/' + 'dior' + str(idx) + '.jpg')
    
    return dior_bags_df

# 디올 남성 신발

def dior_shoes():   
    
    url_base = 'https://www.dior.com/ko_kr'
    url_sub = '/%EB%82%A8%EC%84%B1-%ED%8C%A8%EC%85%98/%EC%8A%88%EC%A6%88/%EB%AA%A8%EB%93%A0-%EC%8A%88%EC%A6%88'
    url = url_base + url_sub
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    brand = []
    name = []
    price = []
    img = []
    sex = []
    url = []

    for item in soup.find_all('div', 'product product-legend-bottom product--cdcbase'):
        brand.append('Dior')
        name.append(item.find(class_='multiline-text').get_text())
        price.append(item.find(class_='price-line').get_text().replace('₩', ''))
        img.append(item.find('img')['src'])
        sex.append('Men')
        url.append(urljoin(url_base, item.find('a')['href']))
    
# dataframe : dior mens shoes
    data = {'title': name, 'price': price, 'image': img, 'sex': sex, 'brand': brand}
    df_mens_shoes = pd.DataFrame(data)
    
# download images
    print('남성신발 사진 저장을 시작합니다')
    for idx, link in enumerate(img):
        urllib.request.urlretrieve(link, 'dior mens shoes/' + 'dior' + str(idx) + '.jpg')

# 디올 여자 신발
    url_base = 'https://www.dior.com/ko_kr'
    url_sub = '/%EC%97%AC%EC%84%B1-%ED%8C%A8%EC%85%98/%EC%97%AC%EC%84%B1-%EC%8A%88%EC%A6%88/%EB%AA%A8%EB%93%A0-%EC%8A%88%EC%A6%88'
    url = url_base + url_sub
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    brand = []
    name = []
    price = []
    img = []
    sex = []
    url = []

    for item in soup.find_all('div', 'product product-legend-bottom product--cdcbase'):
        brand.append('Dior')
        name.append(item.find(class_='multiline-text').get_text())
        price.append(item.find(class_='price-line').get_text().replace('₩', ''))
        img.append(item.find('img')['src'])
        sex.append('women')
        url.append(urljoin(url_base, item.find('a')['href']))
    
# dataframe : dior women bags
    data = {'title': name, 'price': price, 'image': img, 'sex': sex, 'brand': brand}
    df_women_shoes = pd.DataFrame(data)
    
# concat data
    dior_shoes_df = pd.concat([df_mens_shoes, df_women_shoes]).reset_index(drop=True)
    dior_shoes_df.to_csv('dior_shoes.csv', index=False, encoding='utf-8')

# download images
    print('여성신발 사진 저장을 시작합니다')
    for idx, link in enumerate(img):
        urllib.request.urlretrieve(link, 'dior women shoes/' + 'dior' + str(idx) + '.jpg')
    
    return dior_shoes_df
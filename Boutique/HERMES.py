import urllib.request
import requests
import pandas as pd
import re


# 에르메스 옷 크롤링
def h_clothes(pages=3):
    """
    HERMES 한국 사이트에 접속하여 남자, 여자 옷 항목의 모든 페이지에서 데이터를 가져옵니다.
    가져온 데이터를 데이터 프레임의 형태로 바꿔출력해주고,
    사진 링크를 이용하여 사진 파일을 다운로드 합니다.
    
    pages 는 기본적으로 3이며, 원하는 페이지 수를 입력하면 그만큼의 데이터만 가져옵니다.
    
    저장 경로를 변경하고 싶을 때에는
    urllib.request.urlretrieve(url, 'clothes/' + 'g' + str(idx) + '.jpg')에서
    clothes/ 를 다른 폴더 명으로 변경하시면 됩니다(미리 만들어져 있어야 함)
    """
    title = []
    price = []
    img = []
    sex = []
    dfs = []
    ls = []
    url = 'https://bck.hermes.com/product?locale=us_en&category=COLLECTIONPE&sort=relevance'
    response = requests.get(url)
    data = response.json()
    data = data['products']
    print("남성 옷 1페이지 크롤링 중 입니다...")
    for idx in range(len(data)):
        title_ = data[idx]['title']
        price_ = data[idx]['price'] * 1300
        img_ = 'https://' + str(data[idx]['assets'][0])[11:-2]
        sex_ = 'Men'
        title.append(title_)
        price.append(price_)
        img.append(img_)
        sex.append(sex_)
    for page in range(1, pages + 1):
        print("남성 옷 {}페이지 크롤링 중 입니다...".format(page))
        page = page * 36
        url = 'https://bck.hermes.com/product?urlParams=fh_view_size=36%26country=us%26fh_location=--%252Fcategories%253C%257Bcollectionpe%257D&locale=us_en&category=COLLECTIONPE&sort=relevance&offset={}'.format(
            page)
        response = requests.get(url)
        data = response.json()
        data = data['products']
        for idx in range(len(data)):
            title_ = data[idx]['title']
            price_ = data[idx]['price'] * 1300
            img_ = 'https://' + str(data[idx]['assets'][0])[11:-2]
            sex_ = 'Men'
            title.append(title_)
            price.append(price_)
            img.append(str(img_))
            sex.append(sex_)

    url = 'https://bck.hermes.com/product?locale=us_en&category=PRECOLLECTIONPE&sort=relevance'
    response = requests.get(url)
    print(response)
    data = response.json()
    data = data['products']
    print("여성 옷 1페이지 크롤링 중 입니다...")
    for idx in range(len(data)):
        title_ = data[idx]['title']
        price_ = data[idx]['price'] * 1300
        img_ = 'https://' + str(data[idx]['assets'][0])[11:-2]
        sex_ = 'Women'
        title.append(title_)
        price.append(price_)
        img.append(img_)
        sex.append(sex_)
    title_df = pd.DataFrame(title)
    price_df = pd.DataFrame(price)
    img_df = pd.DataFrame(img)
    sex_df = pd.DataFrame(sex)
    dfs.append(title_df)
    dfs.append(price_df)
    dfs.append(img_df)
    dfs.append(sex_df)
    hermes_clothes_df = pd.concat(dfs, axis=1)
    hermes_clothes_df['brand'] = 'HERMES'
    hermes_clothes_df.columns = [['title', 'price', 'image', 'sex', 'brand']]
    hermes_clothes_df = hermes_clothes_df[[
        'brand', 'title', 'price', 'sex', 'image']]
    hermes_clothes_df.to_csv('hermes_clothes.csv',
                             encoding='utf-8', index=False)
    for idx, link in enumerate(img):
        url = link
        urllib.request.urlretrieve(url, 'clothes/' + 'h' + str(idx) + '.jpg')
    return hermes_clothes_df

# 에르메스 가방 크롤링
def h_bags(pages=3):
    """
    HERMES 한국 사이트에 접속하여 남자, 여자 가방 항목의 모든 페이지에서 데이터를 가져옵니다.
    가져온 데이터를 데이터 프레임의 형태로 바꿔출력해주고,
    사진 링크를 이용하여 사진 파일을 다운로드 합니다.
    
    pages 는 기본적으로 3이며, 원하는 페이지 수를 입력하면 그만큼의 데이터만 가져옵니다.
    
    저장 경로를 변경하고 싶을 때에는
    urllib.request.urlretrieve(url, 'bags/' + 'g' + str(idx) + '.jpg')에서
    bags/ 를 다른 폴더 명으로 변경하시면 됩니다(미리 만들어져 있어야 함)
    """
    title = []
    price = []
    img = []
    sex = []
    dfs = []
    ls = []
    url = 'https://bck.hermes.com/product?locale=us_en&category=WOMENBAGSBAGSCLUTCHES&sort=relevance'
    response = requests.get(url)
    data = response.json()
    data = data['products']
    print("여성 가방 1페이지 크롤링 중 입니다...")
    for idx in range(len(data)):
        title_ = data[idx]['title']
        price_ = data[idx]['price'] * 1300
        img_ = 'https://' + str(data[idx]['assets'][0])[11:-2]
        sex_ = 'Women'
        title.append(title_)
        price.append(price_)
        img.append(img_)
        sex.append(sex_)
    for page in range(1, pages + 1):
        print("여성 가방 {}페이지 크롤링 중 입니다...".format(page+1))
        page = page * 36
        url = 'https://bck.hermes.com/product?urlParams=fh_view_size=36%26country=us%26fh_location=--%252Fcategories%253C%257Bwomenbagsbagsclutches%257D&locale=us_en&category=WOMENBAGSBAGSCLUTCHES&sort=relevance&offset={}'.format(
            page)
        response = requests.get(url)
        data = response.json()
        data = data['products']
        for idx in range(len(data)):
            title_ = data[idx]['title']
            price_ = data[idx]['price'] * 1300
            img_ = 'https://' + str(data[idx]['assets'][0])[11:-2]
            sex_ = 'Women'
            title.append(title_)
            price.append(price_)
            img.append(str(img_))
            sex.append(sex_)

    url = 'https://bck.hermes.com/product?locale=us_en&category=MENBAGSBAGS&sort=relevance'
    response = requests.get(url)
    print(response)
    data = response.json()
    data = data['products']
    print("남성 가방 1페이지 크롤링 중 입니다...")
    for idx in range(len(data)):
        title_ = data[idx]['title']
        price_ = data[idx]['price'] * 1300
        img_ = 'https://' + str(data[idx]['assets'][0])[11:-2]
        sex_ = 'Men'
        title.append(title_)
        price.append(price_)
        img.append(img_)
        sex.append(sex_)
    title_df = pd.DataFrame(title)
    price_df = pd.DataFrame(price)
    img_df = pd.DataFrame(img)
    sex_df = pd.DataFrame(sex)
    dfs.append(title_df)
    dfs.append(price_df)
    dfs.append(img_df)
    dfs.append(sex_df)
    hermes_bags_df = pd.concat(dfs, axis=1)
    hermes_bags_df['brand'] = 'HERMES'
    hermes_bags_df.columns = [['title', 'price', 'image', 'sex', 'brand']]
    hermes_bags_df = hermes_bags_df[[
        'brand', 'title', 'price', 'sex', 'image']]
    hermes_bags_df.to_csv('hermes_bags.csv',
                             encoding='utf-8', index=False)
    for idx, link in enumerate(img):
        url = link
        urllib.request.urlretrieve(url, 'bags/' + 'h' + str(idx) + '.jpg')
    return hermes_bags_df
# 에르메스 신발 크롤링
def h_shoes(pages = 3):
    """
    HERMES 한국 사이트에 접속하여 남자, 여자 신발 항목의 모든 페이지에서 데이터를 가져옵니다.
    가져온 데이터를 데이터 프레임의 형태로 바꿔출력해주고,
    사진 링크를 이용하여 사진 파일을 다운로드 합니다.
    
    pages 는 기본적으로 3이며, 원하는 페이지 수를 입력하면 그만큼의 데이터만 가져옵니다.
    
    저장 경로를 변경하고 싶을 때에는
    urllib.request.urlretrieve(url, 'shoes/' + 'g' + str(idx) + '.jpg')에서
    shoes/ 를 다른 폴더 명으로 변경하시면 됩니다(미리 만들어져 있어야 함)
    """
    title = []
    price = []
    img = []
    sex = []
    dfs = []
    ls = []
    url = 'https://bck.hermes.com/product?locale=us_en&category=MENSHOES&sort=relevance'
    response = requests.get(url)
    data = response.json()
    data = data['products']
    print("남성 신발 1페이지 크롤링 중 입니다...")
    for idx in range(len(data)):
        title_ = data[idx]['title']
        price_ = data[idx]['price'] * 1300
        img_ = 'https://' + str(data[idx]['assets'][0])[11:-2]
        sex_ = 'Men'
        title.append(title_)
        price.append(price_)
        img.append(img_)
        sex.append(sex_)
    for page in range(1, pages + 1):
        print("남성 신발 {}페이지 크롤링 중 입니다...".format(page+1))
        page = page * 36
        url = 'https://bck.hermes.com/product?urlParams=fh_view_size=36%26country=us%26fh_location=--%252Fcategories%253C%257Bmenshoes%257D&locale=us_en&category=MENSHOES&sort=relevance&offset={}'.format(
            page)
        response = requests.get(url)
        data = response.json()
        data = data['products']
        for idx in range(len(data)):
            title_ = data[idx]['title']
            price_ = data[idx]['price'] * 1300
            img_ = 'https://' + str(data[idx]['assets'][0])[11:-2]
            sex_ = 'Men'
            title.append(title_)
            price.append(price_)
            img.append(str(img_))
            sex.append(sex_)

    url = 'https://bck.hermes.com/product?locale=us_en&category=WOMENSHOES&sort=relevance'
    response = requests.get(url)
    data = response.json()
    data = data['products']
    print("여성 신발 1페이지 크롤링 중 입니다...")
    for idx in range(len(data)):
        title_ = data[idx]['title']
        price_ = data[idx]['price'] * 1300
        img_ = 'https://' + str(data[idx]['assets'][0])[11:-2]
        sex_ = 'Women'
        title.append(title_)
        price.append(price_)
        img.append(img_)
        sex.append(sex_)
        pages = 7
    for page in range(1, pages + 1):
        print("여성 신발 {}페이지 크롤링 중 입니다...".format(page))
        page = page * 36
        url = 'https://bck.hermes.com/product?urlParams=fh_view_size=36%26country=us%26fh_location=--%252Fcategories%253C%257Bwomenshoes%257D&locale=us_en&category=WOMENSHOES&sort=relevance&offset={}'.format(
            page)
        response = requests.get(url)
        data = response.json()
        data = data['products']
        for idx in range(len(data)):
            title_ = data[idx]['title']
            price_ = data[idx]['price'] * 1300
            img_ = 'https://' + str(data[idx]['assets'][0])[11:-2]
            sex_ = 'Women'
            title.append(title_)
            price.append(price_)
            img.append(str(img_))
            sex.append(sex_)
    title_df = pd.DataFrame(title)
    price_df = pd.DataFrame(price)
    img_df = pd.DataFrame(img)
    sex_df = pd.DataFrame(sex)
    dfs.append(title_df)
    dfs.append(price_df)
    dfs.append(img_df)
    dfs.append(sex_df)
    hermes_shoes_df = pd.concat(dfs, axis=1)
    hermes_shoes_df['brand'] = 'HERMES'
    hermes_shoes_df.columns = [['title', 'price', 'image', 'sex', 'brand']]
    hermes_shoes_df = hermes_shoes_df[[
        'brand', 'title', 'price', 'sex', 'image']]
    hermes_shoes_df.to_csv('hermes_shoes.csv',
                             encoding='utf-8', index=False)
    for idx, link in enumerate(img):
        url = link
        urllib.request.urlretrieve(url, 'shoes/' + 'h' + str(idx) + '.jpg')
    return hermes_shoes_df
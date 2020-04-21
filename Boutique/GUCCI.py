import urllib.request
import requests
import pandas as pd
import re

# 구찌 가방 크롤링
def g_bags(pages = 10):
    """
    GUCCI 한국 사이트에 접속하여 남자, 여자 가방 항목의 모든 페이지에서 데이터를 가져옵니다.
    가져온 데이터를 데이터 프레임의 형태로 바꿔출력해주고,
    사진 링크를 이용하여 사진 파일을 다운로드 합니다.
    
    pages 는 기본적으로 10이며, 원하는 페이지 수를 입력하면 그만큼의 데이터만 가져옵니다.
    
    저장 경로를 변경하고 싶을 때에는
    urllib.request.urlretrieve(url, 'bags/' + 'g' + str(idx) + '.jpg')에서
    bags/ 를 다른 폴더 명으로 변경하시면 됩니다(미리 만들어져 있어야 함)
    """
    
    title = []
    price = []
    sex = []
    img = []
    dfs = []
    for page in range(1, pages+1):
        url = "https://www.gucci.com/kr/ko/c/productgrid?categoryCode=men-bags&show=Page&page={}".format(page)
        response = requests.get(url)
        print("여자 가방 {}페이지 크롤링 중 입니다...".format(page))
        a = response.json()['products']
        b = a['items']
        for idx in range(len(b)):
            title.append(b[idx]['title'])
            price.append(b[idx]['price'])
            img.append(b[idx]['primaryImage']['src'][2:])
            sex.append('Men')
    for page in range(1, pages+1):
        url = "https://www.gucci.com/kr/ko/c/productgrid?categoryCode=women-handbags&show=Page&page={}".format(page)
        response = requests.get(url)
        print("남자 가방 {}페이지 크롤링 중 입니다...".format(page))
        a = response.json()['products']
        b = a['items']
        for idx in range(len(b)):
            title.append(b[idx]['title'])
            price.append(b[idx]['price'])
            img.append(b[idx]['primaryImage']['src'][2:])
            sex.append('Women')
    title_df = pd.DataFrame(title)
    price_df = pd.DataFrame(price)
    img_df = pd.DataFrame(img)
    sex_df = pd.DataFrame(sex)
    dfs.append(title_df)
    dfs.append(price_df)
    dfs.append(img_df)
    dfs.append(sex_df)
    gucci_bags_df = pd.concat(dfs, axis=1)
    gucci_bags_df.reset_index(drop=True, inplace=True)
    gucci_bags_df['brand'] = 'GUCCI'
    gucci_bags_df.columns = ['title', 'price', 'image', 'sex', 'brand']
    gucci_bags_df = gucci_bags_df[['brand', 'title', 'price', 'sex', 'image']]
    a = list(gucci_bags_df['price'])
    ls = []
    for x in a:
        num = re.findall("\d+", x)
        num = "".join(num)
        num = int(num)
        ls.append(num)
    gucci_bags_df['price'] = ls
    gucci_bags_df.to_csv("gucci_bags.csv", index=False, encoding="utf-8")
    print("사진 저장을 시작합니다")
    for idx, link in enumerate(img):
        url = "http://" + link
        urllib.request.urlretrieve(url, 'bags/' + 'g' + str(idx) + '.jpg')
    return gucci_bags_df



# 구찌 옷 크롤링
def g_clothes(pages = 10):
    """
    GUCCI 한국 사이트에 접속하여 남자, 여자 옷 항목의 모든 페이지에서 데이터를 가져옵니다.
    가져온 데이터를 데이터 프레임의 형태로 바꿔출력해주고,
    사진 링크를 이용하여 사진 파일을 다운로드 합니다.
    
    pages 는 기본적으로 10이며, 원하는 페이지 수를 입력하면 그만큼의 데이터만 가져옵니다.
    
    저장 경로를 변경하고 싶을 때에는
    urllib.request.urlretrieve(url, 'clothes/' + 'g' + str(idx) + '.jpg')에서
    clothes/ 를 다른 폴더 명으로 변경하시면 됩니다(미리 만들어져 있어야 함)
    """
    
    title = []
    price = []
    sex = []
    img = []
    dfs = []
    for page in range(1, pages+1):
        url = "https://www.gucci.com/kr/ko/c/productgrid?categoryCode=men-readytowear&show=Page&page={}".format(page)
        response = requests.get(url)
        print("남자 옷 {}페이지 크롤링 중 입니다...".format(page))
        a = response.json()['products']
        b = a['items']
        for idx in range(len(b)):
            title.append(b[idx]['title'])
            price.append(b[idx]['price'])
            img.append(b[idx]['primaryImage']['src'][2:])
            sex.append('Men')
    for page in range(1, pages+1):
        url = "https://www.gucci.com/kr/ko/c/productgrid?categoryCode=women-readytowear&show=Page&page={}".format(page)
        response = requests.get(url)
        print("여자 옷 {}페이지 크롤링 중 입니다...".format(page))
        a = response.json()['products']
        b = a['items']
        for idx in range(len(b)):
            title.append(b[idx]['title'])
            price.append(b[idx]['price'])
            img.append(b[idx]['primaryImage']['src'][2:])
            sex.append('Women')
    title_df = pd.DataFrame(title)
    price_df = pd.DataFrame(price)
    img_df = pd.DataFrame(img)
    sex_df = pd.DataFrame(sex)
    dfs.append(title_df)
    dfs.append(price_df)
    dfs.append(img_df)
    dfs.append(sex_df)
    gucci_clothes_df = pd.concat(dfs, axis=1)
    gucci_clothes_df.reset_index(drop=True, inplace=True)
    gucci_clothes_df['brand'] = 'GUCCI'
    gucci_clothes_df.columns = ['title', 'price', 'image', 'sex', 'brand']
    gucci_clothes_df = gucci_clothes_df[['brand', 'title', 'price', 'sex', 'image']]
    a = list(gucci_clothes_df['price'])
    ls = []
    for x in a:
        num = re.findall("\d+", x)
        num = "".join(num)
        num = int(num)
        ls.append(num)
    gucci_clothes_df['price'] = ls
    gucci_clothes_df.to_csv("gucci_clothes.csv", index=False, encoding="utf-8")
    print("사진 저장을 시작합니다")
    for idx, link in enumerate(img):
        url = "http://" + link
        urllib.request.urlretrieve(url, 'clothes/' + 'g' + str(idx) + '.jpg')
    return gucci_clothes_df



# 구찌 신발 크롤링
def g_shoes(pages = 10):
    """
    GUCCI 한국 사이트에 접속하여 남자, 여자 신발 항목의 모든 페이지에서 데이터를 가져옵니다.
    가져온 데이터를 데이터 프레임의 형태로 바꿔출력해주고,
    사진 링크를 이용하여 사진 파일을 다운로드 합니다.
    
    pages 는 기본적으로 10이며, 원하는 페이지 수를 입력하면 그만큼의 데이터만 가져옵니다.
    
    저장 경로를 변경하고 싶을 때에는
    urllib.request.urlretrieve(url, 'shoes/' + 'g' + str(idx) + '.jpg')에서
    shoes/ 를 다른 폴더 명으로 변경하시면 됩니다(미리 만들어져 있어야 함)
    """
    
    title = []
    price = []
    sex = []
    img = []
    dfs = []
    for page in range(1, pages+1):
        url = "https://www.gucci.com/kr/ko/c/productgrid?categoryCode=men-shoes&show=Page&page={}".format(page)
        response = requests.get(url)
        print("남자 신발 {}페이지 크롤링 중 입니다...".format(page))
        a = response.json()['products']
        b = a['items']
        for idx in range(len(b)):
            title.append(b[idx]['title'])
            price.append(b[idx]['price'])
            img.append(b[idx]['primaryImage']['src'][2:])
            sex.append('Men')
    for page in range(1, pages+1):
        url = "https://www.gucci.com/kr/ko/c/productgrid?categoryCode=women-shoes&show=Page&page={}".format(page)
        response = requests.get(url)
        print("여자 신발 {}페이지 크롤링 중 입니다...".format(page))
        a = response.json()['products']
        b = a['items']
        for idx in range(len(b)):
            title.append(b[idx]['title'])
            price.append(b[idx]['price'])
            img.append(b[idx]['primaryImage']['src'][2:])
            sex.append('Women')
    title_df = pd.DataFrame(title)
    price_df = pd.DataFrame(price)
    img_df = pd.DataFrame(img)
    sex_df = pd.DataFrame(sex)
    dfs.append(title_df)
    dfs.append(price_df)
    dfs.append(img_df)
    dfs.append(sex_df)
    gucci_shoes_df = pd.concat(dfs, axis=1)
    gucci_shoes_df.reset_index(drop=True, inplace=True)
    gucci_shoes_df['brand'] = 'GUCCI'
    gucci_shoes_df.columns = ['title', 'price', 'image', 'sex', 'brand']
    gucci_shoes_df = gucci_shoes_df[['brand', 'title', 'price', 'sex', 'image']]
    a = list(gucci_shoes_df['price'])
    ls = []
    for x in a:
        num = re.findall("\d+", x)
        num = "".join(num)
        num = int(num)
        ls.append(num)
    gucci_shoes_df['price'] = ls
    gucci_shoes_df.to_csv("gucci_shoes.csv", index=False, encoding="utf-8")
    print("사진 저장을 시작합니다")
    for idx, link in enumerate(img):
        url = "http://" + link
        urllib.request.urlretrieve(url, 'shoes/' + 'g' + str(idx) + '.jpg')
    return gucci_shoes_df
import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import re

#가방
def j_bags():
    """
    JIMMY CHOO 한국 사이트에 접속하여 남자, 여자 가방 항목의 모든 페이지에서 데이터를 가져옵니다.
    가져온 데이터를 데이터 프레임의 형태로 바꿔출력해주고,
    사진 링크를 이용하여 사진 파일을 다운로드 합니다.
 
    저장 경로를 변경하고 싶을 때에는
    urllib.request.urlretrieve(url, 'bags/' + 'g' + str(idx) + '.jpg')에서
    bags/ 를 다른 폴더 명으로 변경하시면 됩니다(미리 만들어져 있어야 함)
    """
    
    #여자
    total = []
    for i in range(1, 9):
        start = (i-1) * 40
        url = "https://row.jimmychoo.com/en_KR/women/handbags/?psortd1=1&psortb1=bestMatch&sz=40&start={}&format=page-element".format(start)
        response = requests.get(url)
        dom = BeautifulSoup(response.content, "html.parser")
        elements = dom.select(".js-grid-tile")
        datas = []
        for element in elements:
            datas.append({
                "brand" : "JIMMYCHOO",
                "sex" : "Women",
                "title" : element.select_one(".name-link").get("data-productname") + "(" + element.select_one(".name-link > .visuallyhidden").text + ")",
                "price" : element.select_one(".standart-price > .product-standard-price").text.strip(),
                "image" : 'https://row.jimmychoo.com' + element.select_one("img").get("data-main-src").split("?")[0]
        })

        w_bags = pd.DataFrame(datas)[["brand", "title", "price", "sex", "image"]].reset_index(drop = True)

        l = []
        for i in w_bags["price"]:
            n = re.findall("\d+", i)
            n = "".join(n)
            n = int(n)
            l.append(n)
        w_bags["price"] = l
        
        total.append(w_bags)
        
    w_bags = pd.concat(total).reset_index(drop = True)

    #남자
    
    #실행
    w_bags.to_csv('jimmychoo_bags.csv', index=False, encoding='utf-8')
    
    for idx, link in enumerate(w_bags["image"]):
        url = link
        urllib.request.urlretrieve(url, 'bags/' + "j" + str(idx) + '.jpg')
    
    return w_bags

#신발
def j_shoes():
    """
    JIMMY CHOO 한국 사이트에 접속하여 남자, 여자 신발 항목의 모든 페이지에서 데이터를 가져옵니다.
    가져온 데이터를 데이터 프레임의 형태로 바꿔출력해주고,
    사진 링크를 이용하여 사진 파일을 다운로드 합니다.
 
    저장 경로를 변경하고 싶을 때에는
    urllib.request.urlretrieve(url, 'shoes/' + 'g' + str(idx) + '.jpg')에서
    shoes/ 를 다른 폴더 명으로 변경하시면 됩니다(미리 만들어져 있어야 함)
    """
    #여자
    url = "https://row.jimmychoo.com/en_KR/women/shoes/?psortd1=1&psortb1=bestMatch&sz=40&start=0&format=page-element"
    response = requests.get(url)
    dom = BeautifulSoup(response.content, "html.parser")
    elements = dom.select(".js-grid-tile")
    datas = []
    for element in elements:
        datas.append({
            "brand": "JIMMYCHOO",
            "title": element.select_one("a").get("aria-label") + "(" + element.select_one("a > .visuallyhidden").text + ")",
            "price": element.select_one(".product-standard-price").text.strip(),
            "image": "https://row.jimmychoo.com" + element.select_one("img").get("src").split("?")[0],
            "sex": "Women"
        })

    w_shoes = pd.DataFrame(datas)[["brand", "title", "price", "sex", "image"]]

    l = []
    for i in w_shoes["price"]:
        n = re.findall("\d+", i)
        n = "".join(n)
        n = int(n)
        l.append(n)
    w_shoes["price"] = l
    
    #남자
    url = "https://row.jimmychoo.com/en_KR/men/shoes/?psortd1=1&psortb1=bestMatch&sz=40&start=0&format=page-element"
    response = requests.get(url)
    dom = BeautifulSoup(response.content, "html.parser")
    elements = dom.select(".js-grid-tile")
    datas = []
    for element in elements:
        datas.append({
            "brand" : "JIMMYCHOO",
            "title" : element.select_one(".name-link").text.strip().split("\n")[0] + ", " + element.select_one(".name-link").text.strip().split("\n")[1],
            "price" : element.select_one(".product-standard-price").text.strip(),
            "image" : "https://row.jimmychoo.com" + element.select_one("img").get("src").split("?")[0],
            "sex" : "Men"
        })
        
    m_shoes = pd.DataFrame(datas)[["brand", "title", "price", "sex", "image"]]
    
    p = []
    for i in m_shoes["price"]:
        pr = re.findall("\d+", i)
        pr = "".join(pr)
        pr = int(pr)
        p.append(pr)

    m_shoes["price"] = p
    
    #합치기
    jimmychoo_shoes_df = pd.concat([w_shoes, m_shoes]).reset_index(drop=True)
    jimmychoo_shoes_df.to_csv("jimmychoo_shoes.csv", index=False, encoding='utf-8')
    for idx, link in enumerate(jimmychoo_shoes_df["image"]):
        url = link
        urllib.request.urlretrieve(url, 'shoes/' + 'j' + str(idx) + '.jpg')
    
    return jimmychoo_shoes_df
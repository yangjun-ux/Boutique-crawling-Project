from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.request

#가방
def b_bags():
    
    #여자
    total = []
    for page in range(1, 10):
        url = "https://kr.burberry.com/womens-bags/?start={}&pageSize=40&productsOffset=&cellsOffset=8&cellsLimit=&__lang=ko".format(page)
        response = requests.get(url)
        dom = BeautifulSoup(response.content, "html.parser")
        elements = dom.select(".product-card")

        datas = []
        for element in elements:
            datas.append({
                "brand": "BURBERRY",
                "title": element.select_one("a").get("aria-label"),
                "price": element.select_one(".product-card-price").text.strip(),
                "sex" : "Women",
                "image": element.select_one(".cell-asset-image").get("data-src").split("?")[0]
            })

        w_bag = pd.DataFrame(datas)[["brand", "title", "price", "sex", "image"]].reset_index(drop=True)

        ls = []
        for x in w_bag["price"]:
            num = re.findall("\d+", x)
            num = "".join(num)
            num = int(num)
            ls.append(num)
        w_bag["price"] = ls
        total.append(w_bag)
    w_bag = pd.concat(total)
    
    #남자
    url2 = "https://kr.burberry.com/web-api/pages?offset=17&limit=17&order_by=&pagePath=%2Fmens-bags%2Fbum-bags%2Fproducts&country=KR&language=ko"
    response = requests.get(url2)
    data2 = response.json()["data"]
    p = []
    for i in range(len(data2)):
        d = data2[i]['price']['current']['value']
        p.append(d)
        
    e = []
    for i in range(len(data2)):
        g = data2[i]["rollover_media"]["image"]
        g_1 = "https:" + g
        e.append(g_1)
    
    m_bag = pd.DataFrame(data2)[["extended_image_alt"]]
    m_bag["price"] = p
    m_bag["image"] = e
    m_bag["brand"] = "BURBERRY"
    m_bag["sex"] = "Men"
    
    m_bag = m_bag.rename(columns = {"extended_image_alt":"title"})
    m_bag = m_bag[["brand", "title", "price", "sex", "image"]]
    
    #합치기
    burberry_bag_df = pd.concat([w_bag, m_bag]).reset_index(drop=True)
    burberry_bag_df.to_csv('burberry_bags.csv', index=False, encoding='utf-8')
    for idx, link in enumerate(burberry_bag_df["image"]):
        url = link
        urllib.request.urlretrieve(url, 'clothes/' + 'b' + str(idx) + '.jpg')
        
    return burberry_bag_df
   
 #신발
def b_shoes():
    
    #여자
    url = "https://kr.burberry.com/web-api/pages?offset=0&limit=50&order_by=&pagePath=/womens-sneakers/products&country=KR&language=ko"
    response = requests.get(url)
    data = response.json()["data"]
    
    w_shoes = pd.DataFrame(data)[["extended_image_alt"]]
    
    p = []
    for i in range(len(data)):
        a = data[i]["price"]["current"]["value"]
        p.append(a)
        
    e = []
    for i in range(len(data)):
        b = data[i]["rollover_media"]["image"]
        b_1 = "http:" + b
        e.append(b_1)
        
    w_shoes["price"] = p
    w_shoes["image"] = e
    w_shoes["brand"] = "BURBERRY"
    w_shoes["sex"] = "Women"
    w_shoes = w_shoes.rename(columns = {"extended_image_alt":"title"})
    
    w_shoes = w_shoes[["brand", "title", "price", "sex", "image"]]
    
    #남자
    url2 = "https://kr.burberry.com/web-api/pages?offset=0&limit=50&order_by=&pagePath=%2Fmens-shoes%2Fsneakers%2Fproducts&country=KR&language=ko"
    response = requests.get(url2)
    data = response.json()["data"]
    
    m_shoes = pd.DataFrame(data)[["extended_image_alt"]]
    
    p = []
    for i in range(len(data)):
        h = data[i]["price"]["current"]["value"]
        p.append(h)
        
    e = []
    for i in range(len(data)):
        j = data[i]["media"]["image"]
        j_1 = "https:" + j
        e.append(j_1)
        
    m_shoes["price"] = p
    m_shoes["image"] = e
    m_shoes["sex"] = "Men"
    m_shoes["brand"] = "BURBERRY"
    m_shoes = m_shoes.rename(columns = {"extended_image_alt" : "title"})
    
    m_shoes = m_shoes[["brand", "title", "price", "sex", "image"]]
    
    #합치기
    burberry_shoes_df = pd.concat([w_shoes, m_shoes]).reset_index(drop=True)
    burberry_shoes_df.to_csv("burberry_shoes.csv", index=False, encoding='utf-8')
    for idx, link in enumerate(burberry_shoes_df["image"]):
        url = link
        urllib.request.urlretrieve(url, 'clothes/' + 'b' + str(idx) + '.jpg')
    
    return burberry_shoes_df
# Boutique crawling Project
## - 명품 사이트 웹 크롤링 프로젝트

### - 총 6개의 명품 브랜드

- GUCCI, LOUIS VUITTON, BURBERRY, JIMMY CHOO, DIOR, HERMES

- 3개의 품목(가방(bags), 옷(clothes), 신발(shoes))

### 설치 방법
`pip install Boutique_crawling`

### - 각 모듈별로 bags(), clothes(), shoes() 함수가 있으며 이를 통해 물품의 이름, 가격, 성별, 이미지 링크 데이터를 수집할 수 있음

### - 사진자료도 함께 다운로드 됩니다.

#### - 예시

```python
from Boutique.GUCCI import g_bags
g_bags()
```

사용 시 해당 디렉토리에 bags, clothes, shoes 디렉토리를 미리 만들어주세요

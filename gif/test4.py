import random


fruit = ['사과', '포도', '복숭아', '오렌지', '자두', '망고', '키위', '자두', '배', '딸기', '바나나', '자몽', '석류', '수박', '멜론', '파인애플', '체리', '참외', '유자', '귤', '블루베리', '살구', '레몬', '감', '청포도', '코코넛', '리치', '라임', '산딸기', '거봉']
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
animal = ['개', '고양이', '너구리', '여우', '라쿤', '수달', '햄스터', '다람쥐', '양', '알파카', '사슴', '토끼', '고슴도치', '말', '원숭이', '박쥐', '참새', '까치', '병아리', '오리', '부엉이', '앵무새', '거북이', '캥거루', '뱀', '악어', '개구리', '도롱뇽', '라마', '청설모']
subway = ['강남역', '군자역', '공덕역', '공릉역', '관악역', '구로역', '금호역', '길음역', '용산역', '녹천역', '노원역', '논현역', '당곡역', '도봉역', '뚝섬역', '사당역', '마들역', '마포역', '망원역', '먹골역', '미아역', '반포역', '부평역', '삼성역', '상봉역', '서울역', '석촌역', '시청역', '쌍문역', '안국역', '월계역', '용산역', '인천역', '잠실역', '종각역', '중계역', '진접역', '창동역', '하계역', '합정역', '혜화역', '회현역']
icecream = ['거북알', '구구콘', '아맛나', '빠삐코', '보석바', '돼지바', '옥동자', '고드름', '죠스바', '수박바', '티코', '메로나', '비비빅', '요맘때', '뽕따', '캔디바', '쌍쌍바', '폴라포', '바밤바', '누가바', '호두마루', '체리마루', '엑설런트', '빵또아', '더위사냥', '스크류바', '메가톤바', '찰옥수수', '초코퍼지', '와', '투게더']
country = ['그리스', '네덜란드', '네팔', '노르웨이', '뉴질랜드', '덴마크', '독일', '라오스', '러시아', '멕시코', '몰디브', '미국', '베트남', '벨기에', '브라질', '스웨덴', '스위스', '스페인', '싱가포르', '영국', '이란', '이집트', '인도', '체코', '캐나다', '태국', '터키', '폴란드', '프랑스', '핀란드', '필리핀', '헝가리']
noodle = ['신라면', '짜파게티', '안성탕면', '너구리', '비빔면', '무파마', '새우탕', '삼양라면', '왕뚜껑', '틈새라면', '참깨라면', '진라면', '스낵면', '열라면', '진짬뽕', '컵누들', '육개장', '사리곰탕', '튀김우동', '감자탕면', '짜짜로니', '꼬꼬면', '카레라면', '불닭', '김치라면', '진짜장', '짜왕', '쇠고기면', '해물라면', '공화춘', '짜장범벅']
drink = ['비락식혜', '코카콜라', '펩시', '트레비', '봉봉', '갈배', '환타', '웰치스', '코코팜', '립톤', '이프로', '밀키스', '토레타', '사이다', '데미소다', '게토레이', '피크닉', '카프리썬', '쿨피스', '맥콜', '닥터페퍼', '비타오백', '모구모구', '암바사', '아침햇살', '초록매실', '초코에몽', '데자와', '알로에', '마운틴듀', '실론티']
major = ['국문', '영문', '일문', '불문', '독문', '사학', '경제', '행정', '언영', '교심', '체육', '수학', '원생조', '경영', '패산', '디미', '정보', '소융', '산디', '데사', '현미', '공예', '시디', '자전', '사복', '기독', '중문', '첨미디','화학', '생공', '아동']
area = ['수원', '용인', '성남', '고양', '부천', '안산', '안양', '양주', '파주', '김포', '화성', '원주', '강릉', '인제', '평창', '속초', '포항', '김천', '김해', '진주', '통영', '전주', '군산', '일산', '목포', '여수', '순천', '나주', '서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종']

global gametheme
gametheme = []
gametheme = fruit.copy()
print(str(gametheme))
linear_array = []
linear_array = gametheme.copy()
global random_array
random_array = []

for i in range(9):
    temp = random.choice(linear_array)
    random_array.append(temp)
    linear_array.remove(temp)

print(str(random_array))

from tkinter import*
from tkinter import messagebox
import random
import tkinter.font
from tkinter.simpledialog import *

win = Tk()
win.title("빙고 게임")
win.geometry("1920x1080")


global value
font = tkinter.font.Font(family = "UhBee Se_hyun", size = 22)

# 주제 리스트

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




# 함수
def mainFunc() :
    for wg in win.pack_slaves():
        wg.destroy()
    for get in win.place_slaves():
        get.destroy()

        
    global game
    game = PhotoImage(file = "gif/choicemain.gif")
    gameLabel = Label(win, image = game, anchor = CENTER)
    gameLabel.place(x = 550, y = 50)
    global choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice10
    global cho1, cho2, cho3, cho4, cho5, cho6, cho7, cho8, cho9, cho10
    choice1 = PhotoImage(file = "gif/choice1.gif")
    choice2 = PhotoImage(file = "gif/choice2.gif")
    choice3 = PhotoImage(file = "gif/choice3.gif")
    choice4 = PhotoImage(file = "gif/choice4.gif")
    choice5 = PhotoImage(file = "gif/choice5.gif")
    choice6 = PhotoImage(file = "gif/choice6.gif")
    choice7 = PhotoImage(file = "gif/choice7.gif")
    choice8 = PhotoImage(file = "gif/choice8.gif")
    choice9 = PhotoImage(file = "gif/choice9.gif")
    choice10 = PhotoImage(file = "gif/choice10.gif")
    cho1 = Button(win, image = choice1, anchor = CENTER, command = fruitclick)
    cho2 = Button(win, image = choice2, anchor = CENTER, command = numberclick)
    cho3 = Button(win, image = choice3, anchor = CENTER, command = animalclick)
    cho4 = Button(win, image = choice4, anchor = CENTER, command = subwayclick)
    cho5 = Button(win, image = choice5, anchor = CENTER, command = icecreamclick)
    cho6 = Button(win, image = choice6, anchor = CENTER, command = countryclick)
    cho7 = Button(win, image = choice7, anchor = CENTER, command = noodleclick)
    cho8 = Button(win, image = choice8, anchor = CENTER, command = drinkclick)
    cho9 = Button(win, image = choice9, anchor = CENTER, command = majorclick)
    cho10 = Button(win, image = choice10, anchor = CENTER, command = areaclick)
    
    cho1.place(x = 95, y = 300)
    cho2.place(x = 375, y = 300)
    cho3.place(x = 655, y = 300)
    cho4.place(x = 935, y = 300)
    cho5.place(x = 1195, y = 300)
    cho6.place(x = 50, y = 550)
    cho7.place(x = 330, y = 550)
    cho8.place(x = 610, y = 550)
    cho9.place(x = 890, y = 550)
    cho10.place(x = 1150, y = 550)


global content
content = []
def alldestroy():
    for wg in win.pack_slaves():
        wg.destroy()
    for get in win.place_slaves():
        get.destroy()

def userbingoplace():
    global bingo1, bingo2, bingo3, bingo4, bingo5, bingo6, bingo7, bingo8, bingo9
    bingo1 = Button(win, text = " ", anchor = CENTER, width=6, height =2, font = font, command = bingoenter1)
    bingo1.place(x = 150, y = 230)
    bingo2 = Button(win, text = " ", anchor = CENTER, width=6, height =2, font  = font, command = bingoenter2)
    bingo2.place(x = 300, y = 230)
    bingo3 = Button(win, text = " ", anchor = CENTER, width=6, height =2, font = font, command = bingoenter3)
    bingo3.place(x = 450, y = 230)
    bingo4 = Button(win, text = " ", anchor = CENTER, width=6, height =2, font = font, command = bingoenter4)
    bingo4.place(x = 150, y = 370)
    bingo5 = Button(win, text = " ", anchor = CENTER, width=6, height =2, font = font, command = bingoenter5)
    bingo5.place(x = 300, y = 370)
    bingo6 = Button(win, text = " ", anchor = CENTER, width=6, height =2, font = font, command = bingoenter6)
    bingo6.place(x = 450, y = 370)
    bingo7 = Button(win, text = " ", anchor = CENTER, width=6, height =2, font = font, command = bingoenter7)
    bingo7.place(x = 150, y = 510)
    bingo8 = Button(win, text = " ", anchor = CENTER, width=6, height =2, font = font, command = bingoenter8)
    bingo8.place(x = 300, y = 510)
    bingo9 = Button(win, text = " ", anchor = CENTER, width=6, height =2, font = font, command = bingoenter9)
    bingo9.place(x = 450, y = 510)

global gametheme #주제 선택에 따른 리스트 전역변수 생성
gametheme = []
global random_array
global linear_array
random_array = []

def themechoice():
    random_array = []
    linear_array = gametheme.copy()
    
    for i in range(9):
        temp = random.choice(gametheme)
        gametheme.remove(temp)
        random_array.append(temp)
    


def fruitclick():
    alldestroy()    
    userbingoplace()
    gamestart.place(x = 100, y= 670)
    caution.place(x = 180, y = 160)
    fullofbingo.place(x = 200, y = 0)
    menuago.place(x = 1100, y = 0)
    fruitLabel.place(x=600, y = -50)
    gametheme = fruit.copy()
    themechoice()
    
    


    
def animalclick():
    alldestroy()    
    userbingoplace()
    caution.place(x = 180, y = 160)
    fullofbingo.place(x = 200, y = 0)
    menuago.place(x = 1100, y = 10)
    animalLabel.place(x=600, y = -50)
    gametheme = animal.copy()
    themechoice()
    

def areaclick():
    alldestroy()    
    userbingoplace()
    caution.place(x = 180, y = 160)
    fullofbingo.place(x = 200, y = 0)
    menuago.place(x = 1200, y = 10)
    areaLabel.place(x=600, y = -50)
    gametheme = area.copy()
    themechoice()
    

def countryclick():
    alldestroy()    
    userbingoplace()
    caution.place(x = 180, y = 160)
    fullofbingo.place(x = 200, y = 0)
    menuago.place(x = 1100, y = 10)
    countryLabel.place(x=600, y = -50)
    gametheme = country.copy()
    themechoice()

def drinkclick():
    alldestroy()    
    userbingoplace()
    caution.place(x = 180, y = 160)
    fullofbingo.place(x = 200, y = 0)
    menuago.place(x = 1100, y = 10)
    drinkLabel.place(x=600, y = -50)
    gametheme = drink
    themechoice()

def majorclick():
    alldestroy()    
    userbingoplace()
    caution.place(x = 180, y = 160)
    fullofbingo.place(x = 200, y = 0)
    menuago.place(x = 1100, y = 10)
    majorLabel.place(x=600, y = -50)
    gametheme = major
    themechoice()

def numberclick():
    alldestroy()    
    userbingoplace()
    caution.place(x = 180, y = 160)
    fullofbingo.place(x = 200, y = 0)
    menuago.place(x = 1100, y = 10)
    numberLabel.place(x=600, y = -50)
    gametheme = number
    themechoice()

def subwayclick():
    alldestroy()    
    userbingoplace()
    gamestart.place(x = 100, y= 800)
    caution.place(x = 180, y = 160)
    fullofbingo.place(x = 200, y = 0)
    menuago.place(x = 1100, y = 10)
    subwayLabel.place(x=600, y = -50)
    gametheme = subway
    themechoice()

def icecreamclick():
    alldestroy()    
    userbingoplace()
    caution.place(x = 180, y = 160)
    fullofbingo.place(x = 200, y = 0)
    menuago.place(x = 1100, y = 10)
    icecreamLabel.place(x=600, y = -50)
    gametheme = icecream
    themechoice()

def noodleclick():
    alldestroy()    
    userbingoplace()
    caution.place(x = 180, y = 160)
    fullofbingo.place(x = 200, y = 0)
    menuago.place(x = 1100, y = 10)
    noodleLabel.place(x=600, y = -50)
    gametheme = noodle
    themechoice()

# 게임 시작

def Letstart():
    alldestroy()
    Bingoplace2()
    Bingoplace3()

def Bingoplace2():
    global ubingo1, ubingo2, ubingo3, ubingo4, ubingo5, ubingo6, ubingo7, ubingo8, ubingo9
    ubingo1 = Button(win, text = content[0] , anchor = CENTER, width=6, height =2, font = font, command = bingoenter1)
    ubingo1.place(x = 150, y = 270)
    ubingo2 = Button(win, text = content[1], anchor = CENTER, width=6, height =2, font  = font, command = bingoenter2)
    ubingo2.place(x = 300, y = 270)
    ubingo3 = Button(win, text =content[2], anchor = CENTER, width=6, height =2, font = font, command = bingoenter3)
    ubingo3.place(x = 450, y = 270)
    ubingo4 = Button(win, text = content[3], anchor = CENTER, width=6, height =2, font = font, command = bingoenter4)
    ubingo4.place(x = 150, y = 410)
    ubingo5 = Button(win, text =content[4], anchor = CENTER, width=6, height =2, font = font, command = bingoenter5)
    ubingo5.place(x = 300, y = 410)
    ubingo6 = Button(win, text = content[5], anchor = CENTER, width=6, height =2, font = font, command = bingoenter6)
    ubingo6.place(x = 450, y = 410)
    ubingo7 = Button(win, text = content[6], anchor = CENTER, width=6, height =2, font = font, command = bingoenter7)
    ubingo7.place(x = 150, y = 550)
    ubingo8 = Button(win, text =content[7], anchor = CENTER, width=6, height =2, font = font, command = bingoenter8)
    ubingo8.place(x = 300, y = 550)
    ubingo9 = Button(win, text =content[8], anchor = CENTER, width=6, height =2, font = font, command = bingoenter9)
    ubingo9.place(x = 450, y = 550)

def Bingoplace3():
    global cbingo1, cbingo2, cbingo3, cbingo4, cbingo5, cbingo6, cbingo7, cbingo8, cbingo9
    cbingo1 = Button(win, text = random_array[0], anchor = CENTER, width = 6, height = 2, font = font)
    cbingo2 = Button(win, text = random_array[1], anchor = CENTER, width = 6, height = 2, font = font)
    cbingo3 = Button(win, text = random_array[2], anchor = CENTER, width = 6, height = 2, font = font)
    cbingo4 = Button(win, text = random_array[3], anchor = CENTER, width = 6, height = 2, font = font)
    cbingo5 = Button(win, text = random_array[4], anchor = CENTER, width = 6, height = 2, font = font)
    cbingo6 = Button(win, text = random_array[5], anchor = CENTER, width = 6, height = 2, font = font)
    cbingo7 = Button(win, text = random_array[6], anchor = CENTER, width = 6, height = 2, font = font)
    cbingo8 = Button(win, text = random_array[7], anchor = CENTER, width = 6, height = 2, font = font)
    cbingo9 = Button(win, text = random_array[8], anchor = CENTER, width = 6, height = 2, font = font)

    cbingo1.place(x = 600, y = 270)
    cbingo2.place(x = 750, y = 270)
    cbingo3.place(x = 900, y = 270)
    cbingo4.place(x = 600, y = 410)
    cbingo5.place(x = 750, y = 410)
    cbingo6.place(x = 900, y = 410)
    cbingo7.place(x = 600, y = 550)
    cbingo8.place(x = 750, y = 550)
    cbingo9.place(x = 900, y = 550)
    
    


    


#빙고 입력
    
def bingoenter1():
    value = askstring("빙고 입력", "채울 빙고의 내용을 입력하세요")
    bingo1.configure(text = str(value))
    content.insert(0,value)

def bingoenter2():
    value = askstring("빙고 입력", "채울 빙고의 내용을 입력하세요")
    bingo2.configure(text = str(value))
    content.insert(1,value)

def bingoenter3():
    value = askstring("빙고 입력", "채울 빙고의 내용을 입력하세요")
    bingo3.configure(text = str(value))
    content.insert(2,value)

def bingoenter4():
    value = askstring("빙고 입력", "채울 빙고의 내용을 입력하세요")
    bingo4.configure(text = str(value))
    content.insert(3,value)

def bingoenter5():
    value = askstring("빙고 입력", "채울 빙고의 내용을 입력하세요")
    bingo5.configure(text = str(value))
    content.insert(4,value)

def bingoenter6():
    value = askstring("빙고 입력", "채울 빙고의 내용을 입력하세요")
    bingo6.configure(text = str(value))
    content.insert(5,value)

def bingoenter7():
    value = askstring("빙고 입력", "채울 빙고의 내용을 입력하세요")
    bingo7.configure(text = str(value))
    content.insert(6,value)

def bingoenter8():
    value = askstring("빙고 입력", "채울 빙고의 내용을 입력하세요")
    bingo8.configure(text = str(value))
    content.insert(7,value)

def bingoenter9():
    value = askstring("빙고 입력", "채울 빙고의 내용을 입력하세요")
    bingo9.configure(text = str(value))
    content.insert(8,value)

caution = Label(win, text = "단어를 정확히 입력해주세요", font = font)

startsticker = PhotoImage(file = "gif/gamestart.gif")
gamestart = Button(win, image = startsticker, anchor = CENTER, command = Letstart)






# 메뉴판

fruit = PhotoImage(file = "gif/fruit.gif")
animal = PhotoImage(file = "gif/animal.gif")
area = PhotoImage(file = "gif/area.gif")
country = PhotoImage(file = "gif/country.gif")
drink = PhotoImage(file = "gif/drink.gif")
major = PhotoImage(file = "gif/major.gif")
number = PhotoImage(file = "gif/number.gif")
subway = PhotoImage(file = "gif/subway.gif")
icecream = PhotoImage(file = "gif/icecream.gif")
noodle = PhotoImage(file = "gif/noodle.gif")
fruitLabel = Label(win, image = fruit)
animalLabel = Label(win, image = animal)
areaLabel = Label(win, image = area)
countryLabel = Label(win, image = country)
drinkLabel = Label(win, image = drink)
majorLabel = Label(win, image = major)
numberLabel = Label(win, image = number)
subwayLabel = Label(win, image = subway)
icecreamLabel = Label(win, image = icecream)
noodleLabel = Label(win, image = noodle)
ago9 = PhotoImage(file = "gif/ago9.gif")
menuago = Label(win, image = ago9)
fulling = PhotoImage(file = "gif/fullofbingo.gif")
fullofbingo = Label(win, image = fulling)




    




# 메인 함수

made = PhotoImage(file = "gif/madeby.gif")
madelabel = Label(win, image = made)
bigAgo = PhotoImage(file = "gif/mainicon5.gif")
main_ago = Label(win, image = bigAgo, anchor = SE, width=1000, height =1000)
buttonimage = PhotoImage(file = "gif/mainicon4.gif")
startbutton = Button(win, image = buttonimage, command = mainFunc, anchor = 'center')
title = PhotoImage(file = "gif/mainicon3.gif")
titlelabel = Label(win, image = title, anchor = CENTER)
shine1 = PhotoImage(file = "gif/mainicon1.gif")
shine2 = PhotoImage(file = "gif/mainicon2.gif")
shineLabel1 = Label(win, image = shine1, anchor = CENTER)
shineLabel2 = Label(win, image = shine2, anchor = CENTER)





#startbutton.bind("<Button>", start)

# Canvas.create_image(100,100,image = main_ago)
#background.pack(fill = X)

titlelabel.place( x = 520, y=300)
main_ago.pack(side = RIGHT)
startbutton.place(x = 630, y = 600)
shineLabel1.place(x = 420, y = 400)
shineLabel2.place(x = 1000, y = 250)
madelabel.place(x = 0, y = 700)

shineLabel1.place(x = 420, y = 400)





win.mainloop()

from tkinter import *
from PIL import ImageTk,Image
import random

#  예제 1) tkinter 파이썬 GUI 레이블(label)
# tkinter를 사용하여 텍스트와 이미지를 나타내보자

menulist = ['짜장면', '짬뽕', '탕수육', '라면', '국밥']

# 루트화면 (root window) 생성
tk = Tk()

# window 창 크기 설정
tk.geometry('800x600')

# gui 타이틀
tk.title("오늘 머 먹지?")

# 텍스트 표시
label = Label(tk, text='AI가 추천 해주는 메뉴는?', font=("돋음", 10))

# 레이블 배치 실행
label.pack(side = TOP, padx = 20, pady = 20)

# 함수 정의 (버튼을 누르면 텍스트 내용이 바뀜)
def event():
    menu = random.choice(menulist)
    msg = '{} 추천!'.format(menu)
    label.configure(text=msg)
    img = PhotoImage(file = '{}.png'.format(menu)) # 이미지 읽고
    label_image = Label(image = img) # 이미지 넣고
    label_image.image = img # 레퍼런스 추가
    # label_image.grid(column = 0, row = 2)
    label_image.pack(side = TOP, padx = 10, pady = 10)

button = Button(tk, text='추천 메뉴', command=event)
# button2 = Button(tk, text='버튼2 입니다.')
button.pack(side = BOTTOM, padx = 10, pady = 10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
# button2.pack(side=LEFT, padx=10, pady= 10)

# 4. 메인루프 실행
tk.mainloop()


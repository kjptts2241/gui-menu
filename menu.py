import time
import random

menulist = ['짜장면', '짬뽕', '탕수육', '라면', '국밥']

print('골라줘 메뉴!!!')
print('AI가 추천 해주는 메뉴는?')
for i in range(5, 0, -1):
    print(f'{i}..')
    time.sleep(1)
# print('4..')
# time.sleep(1)
# print('3..')
# time.sleep(1)
# print('2..')
# time.sleep(1)
# print('1..')
# time.sleep(1)
print('엄청난 분석을 통해 오늘의 추천 메뉴를 추천 드립니다.')
menu = random.choice(menulist) # 리스트안에서 랜덤으로 하나를 추출
print(f'{menu} 입니다.')
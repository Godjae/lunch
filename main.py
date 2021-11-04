import random #alt로 위아래 조절가능
print("오늘 점심 뭐 먹지?")
# 메뉴 리스트를 만들어보자
menu = ["짜장면", "짬뽕", "라면", "김밥", "돈까스"]
print(menu)

print("이 중에서 당신의 머릿속을 분석하여 추천하는 메뉴는? ")
print("두구 두구 두구 두구~~~~")
a = random.randint(0, 4)
print("{}입니다.".format(menu[a])) #menu 리스트 내에서 몇번째인지
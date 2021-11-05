from tkinter import * #tkinter라는 외부라이브러리의 함수를 모두 사용
import random
menu = ["짜장면", "짬뽕", "라면", "김밥", "돈가스"]

def pressed(): #버튼 클릭 이벤트
    foodname= random.choice(menu)
    msg = "오늘의메뉴는 {}".format(foodname)
    label.configure(text=msg)
    img = PhotoImage(file='{}.png'.format(foodname)) #이미지 읽고
    lbl = Label(image=img)#이미지 넣어
    lbl.image = img #래퍼런스 추가
    lbl.grid(column=0, row=2)
    # lbl.pack()


root=Tk()
root.title("오늘 뭐먹지") #제목
root.geometry("540x380")

btn1= Button(root,text="추천메뉴", command=pressed)
btn1.grid(column=0, row=0)
# btn1.pack()

label = Label(root,text="두구두구", font=("돋움",10))
label.grid(column=0,row=1)
root.mainloop()

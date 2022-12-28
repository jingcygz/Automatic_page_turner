import pynput.mouse as mouse
from time import *
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from random import *
import webbrowser as web

fangxiang = 'up'


def automatic_page_turner():
    m = mouse.Controller()
    automatic_page_turner_window = Tk()
    automatic_page_turner_window.title('自动翻页器')
    automatic_page_turner_window.geometry('600x400')

    def fanye():
        global fangxiang
        try:
            entry_get = entry.get()
            if entry_get == '':
                entry_get = 10
            else:
                entry_get = float(entry_get)
            if entry_get == 0:
                entry_get = 10
            if fangxiang == 'up' and entry_get < 0:
                entry_get = abs(entry_get)
            if fangxiang == 'down' and entry_get > 0:
                entry_get = abs(entry_get)

            def ok():
                question = askretrycancel('确定？', '%s' % '最后一遍，是否翻页（可能造成卡顿）')
                if question:
                    j = 5
                    showinfo('准备', '%s' % '开始计时5秒钟')
                    for a in range(5):  # 倒计时
                        print('倒计时:' + str(j))
                        j = j - 1
                        sleep(1)
                    m.scroll(0, entry_get)

            if entry_get <= 1000:
                if entry_get >= 50:
                    question = askquestion('确定？', '%s' % '确定要翻页大于50次吗？')
                    if question == 'yes':
                        ok()
                else:
                    ok()
            else:
                showerror('错误', '%s' % '请勿翻大于1000遍')
                entry.delete(0, END)
        except Exception as x:
            showerror('错误', '%s' % x)
            entry.delete(0, END)

    def suijifanye():
        global fangxiang
        try:
            def ok():
                question = askretrycancel('确定？', '%s' % '最后一遍，是否翻页（可能造成卡顿）')
                if question:
                    j = 5
                    showinfo('准备', '%s' % '开始计时5秒钟')
                    for a in range(5):  # 倒计时
                        print('倒计时:' + str(j))
                        j = j - 1
                        sleep(1)
                    m.scroll(0, randint(-1000, 1000))
            ok()
        except Exception as x:
            showerror('错误', '%s' % x)
            entry.delete(0, END)

    def up():
        global fangxiang
        fangxiang = 'up'
        showinfo('成功', '%s' % '设置成功，键为{}'.format(fangxiang))

    def down():
        global fangxiang
        fangxiang = 'down'
        showinfo('成功', '%s' % '设置成功，键为{}'.format(fangxiang))

    def github():
        web.open('https://github.com/jingcygz/Automatic_page_turner')

    label = Label(automatic_page_turner_window, text="制作：小井井")
    label.pack()

    label_1 = Label(automatic_page_turner_window, text="翻页")
    label_1.place(relx=0.3, rely=0.3)

    entry = Entry(automatic_page_turner_window)
    entry.place(relx=0.5, rely=0.3)

    button = Button(automatic_page_turner_window, text="开始", command=fanye)
    button.place(relx=0.5, rely=0.6)

    button_1 = Button(automatic_page_turner_window, text="随机地翻", command=suijifanye)
    button_1.place(relx=0.5, rely=0.7)

    button_2 = Button(automatic_page_turner_window, text="小破站", command=github)
    button_2.place(relx=0.5, rely=0.8)

    button_3 = Button(automatic_page_turner_window, text="上", command=up)
    button_3.place(relx=0.4, rely=0.5)

    button_4 = Button(automatic_page_turner_window, text="下", command=down)
    button_4.place(relx=0.6, rely=0.5)

    automatic_page_turner_window.mainloop()


if __name__ == '__main__':
    automatic_page_turner()

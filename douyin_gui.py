from tkinter import  *
from tkinter import messagebox
def closeWindow():
    messagebox.showinfo(title="警告",message="请不要关闭")
    return
def Love():
    # 顶级窗口
    love = Toplevel(window)
    love.geometry("300x100+200+300")
    love.title("好巧")
    label = Label(love,text="好巧", font=('微软雅黑', 30,),fg='green')
    label.pack()
    btn = Button(love,text='OK',width=10,height=3,command=closeAllWindow)
    btn.pack()

def noLove():
    # 顶级窗口
    nolove = Toplevel(window)
    nolove.geometry("300x100+200+300")
    nolove.title("不巧")
    label = Label(nolove, text="在考虑考虑吧", font=('微软雅黑', 30,),fg='green')
    label.pack()
    btn = Button(nolove,text='OK',width=10,height=3,command=nolove.destroy)
    btn.pack()
    nolove.protocol("WM_DELETE_WINDOW",closenoLove)

def closenoLove():
    return

def closeAllWindow():
    window.destroy()

# 创建窗口
window = Tk()

# 窗口标题
window.title("你好")

# 窗口尺寸
window.geometry("500x600")
# 窗口位置
window.geometry("+200+300")

# window.geometry("500x600+500+600")
# protocol 用户关闭窗口触发事件
window.protocol("WM_DELETE_WINDOW",closeWindow)
# 标签控件
label = Label(window, text='hi,你好', font=('微软雅黑', 30,),fg='red')
label.grid(row=0, column=0)

label2 = Label(window,text='你在吗', font=('微软雅黑', 30,),fg='red')
# 对齐方式sticky , N S W E
label2.grid(row=1,column=1,sticky=E)

# 图片
photo = PhotoImage(file="F:/pythonwork/4.png")
imageLable = Label(window,image=photo)
imageLable.grid(row=2,columnspan=3)

# 按钮1
btn = Button(window,text="呼叫",width=15,height=3,command=Love)
btn.grid(row=3,column=0)
# 弹窗1

# 按钮2
btn2 = Button(window,text="删除",width=15,height=3,command=noLove)
btn2.grid(row=3,column=1)
# 弹窗2
# 显示窗口 消息循环
window.mainloop()


# 生成程序
# pyinstall F -w -ico (文件名)
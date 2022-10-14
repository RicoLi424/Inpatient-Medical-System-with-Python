import datetime
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import os
import time
import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
window0 = tk.Tk()
window0.title("住院管理信息系统");
window0.geometry("1000x700+250+250")
window0.resizable(1, 1)
img = Image.open('picture/hospital.png')  # 打开图片
photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
imglabel = tk.Label(window0, image=photo).place(x = 240,y=0)
conn = pymysql.connect(host='localhost', user='root', password='Ltm123456789', port=3306)
cur = conn.cursor()
cur.execute("use hospitaldb;")
img1 = Image.open('picture/ren.png')  # 打开图片
photo1 = ImageTk.PhotoImage(img1)  # 用PIL模块的PhotoImage打开
imglabel = tk.Label(window0, image=photo1).place(x = 345,y=220)
img2 = Image.open('picture/zhuce.png')  # 打开图片
photo2 = ImageTk.PhotoImage(img2)  # 用PIL模块的PhotoImage打开
imglabel = tk.Label(window0, image=photo2).place(x = 600,y=222)
img3 = Image.open('picture/yiyuan.png')  # 打开图片
photo3 = ImageTk.PhotoImage(img3)  # 用PIL模块的PhotoImage打开
imglabel = tk.Label(window0, image=photo3).place(x = 350,y=420)
img4 = Image.open('picture/yijian.png')  # 打开图片
photo4 = ImageTk.PhotoImage(img4)  # 用PIL模块的PhotoImage打开
imglabel = tk.Label(window0, image=photo4).place(x = 600,y=420)
P3 = tk.Button(window0,width=1000,height=20,highlightbackground='lightGreen')
P3.place(x=0,y=680)



def denglu():
    window = tk.Toplevel()
    window.title("住院管理信息系统");
    window.geometry("1000x700+250+250")
    window.resizable(0, 0)
    img = Image.open('picture/hospital.png')  # 打开图片
    photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
    imglabel = tk.Label(window, image=photo).place(x=240, y=0)

    var1 = tk.StringVar()
    var2 = tk.StringVar()
    tk.Label(window,text='用户名:', font=('Lohit Kannada',24,'bold')).place(x=340,y=300)
    e1 = tk.Entry(window,show = None,textvariable =var1,font=('microsoft',24,'bold') ,width = 15)
    e1.place(x = 450,y=300)

    tk.Label(window,text='密码:',font=('microsoft',24,'bold')).place(x=365,y=340)
    e2 = tk.Entry(window,show = '*',textvariable =var2,font=('microsoft',24,'bold'),width = 15)
    e2.place(x= 450,y=350)


    def login():
        user = var1.get()
        psw = var2.get()
        print(user,psw)
        sql='select * from users where username=%s and password=%s'
        cur.execute(sql,(user,psw))
        data = cur.fetchone()
        if data==None:
            tk.messagebox.askquestion(title='警告', message='错误的用户名或密码\n                                    or\n您没有权限登陆该系统')
        else:
            name = data[1]
            job = data[3]
            pid = data[0]
            pid1=data[0]

            if job == '护士':
                window.destroy()
                mainwindow = tk.Toplevel()
                mainwindow.title('导诊主界面')
                #mainwindow.state('zoomed')
                mainwindow.geometry("1100x700+250+120")
                mainwindow.resizable(0, 0)
                '''tk.Label(text='早上好! ' + job +': '+name, font=('Lohit Kannada',30,'bold')).place(x=450, y=250)  # 问候语'''
                img = Image.open('picture/hospital.png')  # 打开图片
                photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
                tk.Label(mainwindow, image=photo).place(x=260, y=0)



                def apply():
                    lp1 = tk.Label(mainwindow,text='患者ID:',font=25)
                    lp1.place(x=350, y=250)
                    text1 = tk.Text(mainwindow, width=40,height=10, font=('宋体',20),highlightbackground='darkgreen')
                    varPhone = tk.StringVar()
                    le1 = tk.Entry(mainwindow,show=None, textvariable=varPhone, font=21, width=15)
                    le1.place(x=480, y=250)
                    P3 = tk.Button(mainwindow, width=1000, height=20, highlightbackground='lightGreen')
                    P3.place(x=0, y=680)

                    def search():
                        try:
                            text1.delete('1.0','end')
                            sql1=f'select * from patients where id={varPhone.get()}&& n_id={pid} '
                            cur.execute(sql1)
                            a = cur.fetchall()
                            sql1 = f'select * from patients where id={varPhone.get()} '
                            cur.execute(sql1)
                            b = cur.fetchall()
                            if b!=():
                                if a==():
                                    tk.messagebox.showwarning('警告', "无权限")
                                else:

                                    text1.place(x=310,y=310)
                                    text1.insert(tk.END, f'病人ID:  {a[0][0]}\n姓名：{a[0][1]}\n性别：{a[0][3]}\n出生日期：{a[0][4]}\n身份证号码：{a[0][2]}\n账户余额：{a[0][5]}\n主管护士：{a[0][6]}')
                                    sql2=f'select pr_id from r_prescription where p_id={varPhone.get()}'
                                    cur.execute(sql2)
                                    a=cur.fetchall()
                                    for i in a:
                                        sql3=f'select contentp, contentm from prescription where id={i[0]} '
                                        cur.execute(sql3)
                                        a1 = cur.fetchall()
                                        text1.insert(tk.END,f'\n处方：{a1[0][0]}\n药品：{a1[0][1]}')
                                    sql4=f'select cl_id from r_checklist where p_id={varPhone.get()}'
                                    cur.execute(sql4)
                                    a = cur.fetchall()
                                    for i in a:
                                        sql5=f'select content from checklist where id={i[0]} '
                                        cur.execute(sql5)
                                        a2 = cur.fetchall()
                                        text1.insert(tk.END, f'\n检查单：{a2[0][0]}')
                                    B5.place(x=520,y=600)
                            else:
                                tk.messagebox.showwarning('', "此病人不存在")

                        except:
                            tk.messagebox.showwarning('', "非法输入")
                    b6 = tk.Button( mainwindow,text="查询", command=search,font=25,width=4,height=1,highlightbackground='lightgreen')
                    b6.place(x=690, y=250)
                    def leave():
                        sql0=f'select r_id from bed where patient = {varPhone.get()}'
                        cur.execute(sql0)
                        a= cur.fetchone()
                        if a!=None:
                            sql1=f'update room set vacancy= vacancy+1 where id=(select r_id from bed where patient={varPhone.get()}) '
                            cur.execute(sql1)
                            conn.commit()
                            sql6 = f'update bed set time=null where patient={varPhone.get()}'
                            cur.execute(sql6)
                            sql3 = f'update bed set patient=-1 where patient={varPhone.get()}'
                            cur.execute(sql3)
                            sql4 = f'delete from doctor_patient where p_id={varPhone.get()}'
                            cur.execute(sql4)
                            sql5 = f'update patients set n_id=null where id= {varPhone.get()}'
                            cur.execute(sql5)
                            conn.commit()
                            tk.messagebox.showinfo('',"出院成功")
                        else:
                            tk.messagebox.showerror('', "出院失败")

                    B5 = tk.Button(mainwindow,text="出院", command=leave, width=4, height=1, highlightbackground='lightgreen', font=('KacstBook', 20, 'italic'))
                    def cancel():
                        lp1.destroy()
                        le1.destroy()
                        b2.destroy()
                        b6.destroy()
                        text1.destroy()
                        B5.destroy()


                    b2 = tk.Button(mainwindow,text='返回', font=25, command=cancel,width=4,height=1,highlightbackground='red')
                    b2.place(x=790, y=250)

                P = tk.Button(mainwindow, text="患者", command=apply,width=5,height=1,fg='green',font =('KacstBook',20,'italic'),highlightbackground='lightGreen')
                P.place(x=530,y=180)
                mainwindow.mainloop()
            if job == '病人':
                window.destroy()
                mainwindow = tk.Toplevel()
                mainwindow.title('我的界面')
                # mainwindow.state('zoomed')
                mainwindow.geometry("1100x700+250+120")
                mainwindow.resizable(0,0)
                img = Image.open('picture/hospital.png')  # 打开图片
                photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
                tk.Label(mainwindow, image=photo).place(x=260, y=1)

                img1 = Image.open('picture/1.png')  # 打开图片
                photo1 = ImageTk.PhotoImage(img1)  # 用PIL模块的PhotoImage打开
                tk.Label(mainwindow, image=photo1).place(x=246, y=230)
                img2 = Image.open('picture/2.png')  # 打开图片
                photo2 = ImageTk.PhotoImage(img2)  # 用PIL模块的PhotoImage打开
                tk.Label(mainwindow, image=photo2).place(x=500, y=230)
                img3 = Image.open('picture/3.png')  # 打开图片
                photo3 = ImageTk.PhotoImage(img3)  # 用PIL模块的PhotoImage打开
                tk.Label(mainwindow, image=photo3).place(x=764, y=230)
                img4 = Image.open('picture/4.png')  # 打开图片
                photo4 = ImageTk.PhotoImage(img4)  # 用PIL模块的PhotoImage打开
                tk.Label(mainwindow, image=photo4).place(x=246, y=480)
                img5 = Image.open('picture/5.png')  # 打开图片
                photo5 = ImageTk.PhotoImage(img5)  # 用PIL模块的PhotoImage打开
                tk.Label(mainwindow, image=photo5).place(x=500, y=480)
                img6 = Image.open('picture/6.png')  # 打开图片
                photo6 = ImageTk.PhotoImage(img6)  # 用PIL模块的PhotoImage打开
                tk.Label(mainwindow, image=photo6).place(x=764, y=480)




                def xinxi():
                    window0 = tk.Toplevel()
                    window0.title('我的信息')
                    window0.geometry("600x400+450+120")
                    window0.resizable(0, 0)
                    img = Image.open('picture/2.png')  # 打开图片
                    photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
                    tk.Label(window0, image=photo).place(x=250, y=10)
                    t = tk.Label(window0,text='基本信息：',font=('Typewriter', 20))
                    t.place(x=100,y=110)
                    text2 = tk.Text(window0, highlightbackground='black',width=30, height=8, font=('Typewriter', 20))
                    sql1 = f'select id,name,nationalid,sex,dob,balance from patients where id={pid}'
                    cur.execute(sql1)
                    a = cur.fetchall()
                    sql = f'select d_id from doctor_patient where {pid}=p_id'
                    cur.execute(sql)
                    c = cur.fetchall()
                    text2.insert(tk.END,f'病人ID: {a[0][0]}\n姓名：{a[0][1]}\n性别：{a[0][3]}\n出生日期：{a[0][4]}\n身份证号码：{a[0][2]}\n账户余额：{a[0][5]}\n')
                    text2.place(x=100, y=150)
                    for i in c:
                        sql33=f'select do.name, de.name from doctors do, department de where do.d_id=de.id and do.id={i[0]}'
                        cur.execute(sql33)
                        c1 = cur.fetchall()
                        text2.insert(tk.END, f'我的挂号: {c1[0][0]}  {c1[0][1]}\n')
                    def zhuxiao():
                        sql=f'delete from users where id={pid}'
                        cur.execute(sql)

                    def c():
                        window0.destroy()

                    P10 = tk.Button(window0, text="返回", command=c, width=7, height=1, fg='green',
                                    highlightbackground='YellowGreen', font=('KacstBook', 20, 'italic'))
                    P10.place(x=250, y=350)


                    window0.mainloop()
                def chufang():
                    window1=tk.Toplevel()
                    window1.title('我的报告')
                    window1.geometry("600x400+450+120")
                    window1.resizable(0, 0)
                    img = Image.open('picture/1.png')
                    photo = ImageTk.PhotoImage(img)
                    tk.Label(window1, image=photo).place(x=250, y=10)
                    text3 = tk.Text(window1, highlightbackground='black',width=30, height=8, font=('Typewriter', 20))
                    sql2 = f'select pr_id from r_prescription where p_id={pid}'
                    cur.execute(sql2)
                    a = cur.fetchall()
                    t = tk.Label(window1, text='处方信息：', font=('Typewriter', 20))
                    t.place(x=100, y=110)
                    for i in a:
                        sql3 = f'select contentp, contentm from prescription where id={i[0]} '
                        cur.execute(sql3)
                        a1 = cur.fetchall()
                        text3.insert(tk.END, f'\n处方：{a1[0][0]}\n药品：{a1[0][1]}')
                    text3.place(x=100,y=150)
                    def c():
                        window1.destroy()

                    P10 = tk.Button(window1, text="返回", command=c, width=7, height=1, fg='green',
                                    highlightbackground='YellowGreen', font=('KacstBook', 20, 'italic'))
                    P10.place(x=250, y=350)
                    window1.mainloop()

                def jiancha():
                    window2 = tk.Toplevel()
                    window2.title('我的检查单')
                    window2.geometry("600x400+450+120")
                    window2.resizable(0, 0)
                    img = Image.open('picture/3.png')  # 打开图片
                    photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
                    tk.Label(window2, image=photo).place(x=250, y=1)
                    text3 = tk.Text(window2, highlightbackground='black', width=30, height=8, font=('Typewriter', 20))
                    text3.place(x=100,y=150)
                    sql4 = f'select cl_id,ci_id from r_checklist where p_id={pid}'
                    cur.execute(sql4)
                    a = cur.fetchall()
                    t = tk.Label(window2, text='检查单信息：', font=('Typewriter', 20))
                    t.place(x=100, y=110)
                    for i in a:
                        sql=f'select name from checkitem where id={i[1]}'
                        sql5 = f'select content from checklist where id={i[0]} '
                        cur.execute(sql)
                        a8=cur.fetchall()
                        cur.execute(sql5)
                        a2 = cur.fetchall()
                        text3.insert(tk.END, f'检查项目：{a8[0][0]}\n检查医嘱：{a2[0][0]}')

                    def c():
                        window2.destroy()

                    P10 = tk.Button(window2, text="返回", command=c, width=7, height=1, fg='green',
                                    highlightbackground='YellowGreen', font=('KacstBook', 20, 'italic'))
                    P10.place(x=250, y=350)
                    window2.mainloop()
                def jiaoyi():
                    window3 = tk.Toplevel()
                    window3.title('我的账单')
                    window3.geometry("600x400+450+120")
                    window3.resizable(0, 0)
                    img = Image.open('picture/4.png')  # 打开图片
                    photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
                    tk.Label(window3, image=photo).place(x=256, y=10)
                    text4 = tk.Text(window3, width=45, height=12, font=20,highlightbackground='black')
                    text4.place(x=95, y=145)
                    sql1 = f'select * from account where p_id={pid}'
                    cur.execute(sql1)
                    a = cur.fetchall()
                    for i in a:
                        text4.insert(tk.END, f'\n{i}')
                    window3.mainloop()
                def chongzhi():
                    window4 = tk.Toplevel()
                    window4.title('充值')
                    window4.geometry("600x400+450+120")
                    window4.resizable(0, 0)
                    img = Image.open('picture/5.png')  # 打开图片
                    photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
                    tk.Label(window4, image=photo).place(x=250, y=10)
                    lp1 = tk.Label(window4,text='充值金额:', font=20)
                    lp1.place(x=160, y=150)
                    varPhone = tk.StringVar()
                    le1 = tk.Entry(window4,show=None, textvariable=varPhone, font=21, width=15)
                    le1.place(x=260, y=150)
                    def chong100 ():
                        sql = f'update patients set balance = balance+100 where id={pid} '
                        cur.execute(sql)
                        sql1 = f'insert into account values(null,\'充值\',100,\'充值\',now(),{pid})'
                        cur.execute(sql1)
                        conn.commit()
                        tk.messagebox.showinfo('提示', '成功充值100元')

                    def chong500 ():
                        sql = f'update patients set balance = balance+500 where id={pid} '
                        cur.execute(sql)
                        sql1 = f'insert into account values(null,\'充值\',500,\'充值\',now(),{pid})'
                        cur.execute(sql1)
                        conn.commit()
                        tk.messagebox.showinfo('提示', '成功充值500元')
                    def chong1000 ():
                        sql = f'update patients set balance = balance+1000 where id={pid} '
                        cur.execute(sql)
                        sql1 = f'insert into account values(null,\'充值\',1000,\'充值\',now(),{pid})'
                        cur.execute(sql1)
                        conn.commit()
                        tk.messagebox.showinfo('提示', '成功充值1000元')

                    def tijiao():
                        try:
                            b1=varPhone.get()
                            b2=int(b1)
                            if b2<0:
                                tk.messagebox.showwarning('提示', "金额错误")
                            else:
                                sql = f'update patients set balance = balance+{b2} where id={pid} '
                                print(sql)
                                cur.execute(sql)
                                sql1 = f'insert into account values(null,\'充值\',{b2},\'充值\',now(),{pid})'
                                print(sql1)
                                cur.execute(sql1)
                                conn.commit()
                                tk.messagebox.showinfo('提示', f'成功充值{b2}元')

                        except:
                            tk.messagebox.showwarning('提示', '非法输入')

                    b13 = tk.Button(window4, text='提交', command=tijiao, width=4, height=1, fg='green',font=20,highlightbackground='lightgreen')
                    b13.place(x=440, y=150)
                    b14 = tk.Button(window4, text='100', command=chong100, width=4, height=1, fg='green', font=('KacstBook', 20, 'italic'),highlightbackground='lightgreen')
                    b14.place(x=200, y=250)
                    b15 = tk.Button(window4, text='500', command=chong500, width=4, height=1, fg='green', font=('KacstBook', 20, 'italic'),highlightbackground='lightgreen')
                    b15.place(x=300, y=250)
                    b16 = tk.Button(window4, text='1000', command=chong1000, width=4, height=1, fg='green', font=('KacstBook', 20, 'italic'),highlightbackground='lightgreen')
                    b16.place(x=400, y=250)
                    window4.mainloop()

                def guahao():
                    window5 = tk.Toplevel()
                    window5.title('预约挂号')
                    window5.geometry("600x400+450+120")
                    window5.resizable(0, 0)
                    img = Image.open('picture/6.png')  # 打开图片
                    photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
                    tk.Label(window5, image=photo).place(x=266, y=10)
                    sql = f'select name from department'
                    cur.execute(sql)
                    department=cur.fetchall()
                    delist = ttk.Combobox(window5,font=20, width=18)
                    delist.place(x=240,y=150)
                    delist['value'] = department
                    lp1 = tk.Label(window5,text='选择科室:', font=20)
                    lp1.place(x=170, y=150)
                    def doctor():
                        dname = delist.get()
                        sql=f'select name from doctors where d_id=(select id from department where name=\'{dname}\')'
                        cur.execute(sql)
                        doctorname=cur.fetchall()
                        delist1 = ttk.Combobox(window5,font=20, width=18)
                        delist1.place(x=240, y=250)
                        delist1['value'] = doctorname
                        lp2 = tk.Label(window5,text='选择医生:', font=20)
                        lp2.place(x=170, y=250)
                        def signup():
                            sql0=f'select d_id from doctor_patient where p_id={pid}'
                            cur.execute(sql0)
                            a=cur.fetchall()
                            docname=delist1.get()
                            sql=f'select id from doctors where name=\'{docname}\''
                            cur.execute(sql)
                            did=cur.fetchone()
                            print(did)
                            temp=False
                            for i in a:
                                if i==did :
                                    temp=True
                            if temp:
                                tk.messagebox.showwarning('提示', '挂号失败')
                            else:
                                sql1 = f'insert into doctor_patient values({did[0]},{pid})'
                                cur.execute(sql1)
                                # 医生挂号费用
                                conn.commit()
                                tk.messagebox.showinfo('提示', '挂号成功')
                        b2 = tk.Button(window5, text="挂号", command=signup, width=4, height=1,highlightbackground='lightgreen' ,font=('KacstBook', 20, 'italic'))
                        b2.place(x=280,y=310)
                    b1 = tk.Button(window5,text='提交', font=20, command=doctor)
                    b1.place(x=460, y=150)
                    window5.mainloop()

                b8 = tk.Button(mainwindow, text="我的报告", command=chufang, width=7, height=1, fg='green',
                              font=('KacstBook', 20, 'italic'),highlightbackground='lightgreen')
                b8.place(x=240, y=315)
                b9 = tk.Button(mainwindow, text="我的检查单", command=jiancha, width=8, height=1, fg='green',
                               font=('KacstBook', 20, 'italic'),highlightbackground='lightgreen')
                b9.place(x=760, y=315)
                b10 = tk.Button(mainwindow, text="我的信息", command=xinxi, width=7, height=1, fg='green',
                               font=('KacstBook', 20, 'italic'),highlightbackground='lightgreen')
                b10.place(x=500, y=315)
                b11 = tk.Button(mainwindow, text="我的账单", command=jiaoyi, width=7, height=1, fg='green',
                                font=('KacstBook', 20, 'italic'),highlightbackground='lightgreen')
                b11.place(x=236, y=570)
                b12 = tk.Button(mainwindow, text="充值", command=chongzhi, width=7, height=1, fg='green',
                                font=('KacstBook', 20, 'italic'),highlightbackground='lightgreen')
                b12.place(x=500, y=570)
                b13 = tk.Button(mainwindow, text="预约挂号",command=guahao, width=7, height=1, fg='green',
                                font=('KacstBook', 20, 'italic'),highlightbackground='lightgreen')
                b13.place(x=760, y=570)


                mainwindow.mainloop()

            if job == '医生':

                window.destroy()
                mainwindow = tk.Toplevel()
                mainwindow.title('医生主界面')
                mainwindow.geometry("1100x700+250+120")
                mainwindow.resizable(0, 0)
                first = tk.Label(mainwindow,text='你好! ' + job + ':' + name, font=('times',30))
                first.place(x=450, y=350)
                img = Image.open('picture/hospital.png')
                photo = ImageTk.PhotoImage(img)
                tk.Label(mainwindow, image=photo).place(x=270, y=5)


                def diagnose():
                    first.destroy()
                    varNo = tk.StringVar()
                    l1 = tk.Label(mainwindow,text = '患者ID :', font = 20)
                    l1.place(x=240, y=270)
                    No = tk.Entry(mainwindow,show = None,textvariable = varNo,font = 21,width = 15)
                    No.place(x=340,y=270)
                    l2 = tk.Label(mainwindow,text='病人信息:', font = 20)
                    l2.place(x=240, y=310)
                    Dia = tk.Text(mainwindow,height = 20,font = 21,width=50)
                    Dia.place(x=340, y=310)
                    def input():
                        try:
                            Dia.delete('1.0','end')
                            sql1=f'select * from patients where id={varNo.get()} '
                            cur.execute(sql1)
                            a = cur.fetchall()
                            Dia.insert(tk.END, f'病人ID: {a[0][0]}      姓名：{a[0][1]}        性别：{a[0][3]}\n出生日期：{a[0][4]}\n身份证号码：{a[0][2]}\n账户余额：{a[0][5]}\n主管护士：{a[0][6]}')
                            sql2=f'select pr_id from r_prescription where p_id={varNo.get()}'
                            cur.execute(sql2)
                            a=cur.fetchall()
                            for i in a:
                                sql3=f'select contentp, contentm from prescription where id={i[0]} '
                                cur.execute(sql3)
                                a1 = cur.fetchall()
                                Dia.insert(tk.END,f'\n处方：{a1[0][0]}药品：{a1[0][1]}')
                            sql4=f'select ci_id from r_checklist where p_id={varNo.get()}'
                            cur.execute(sql4)
                            a = cur.fetchall()
                            for i in a:
                                sql5=f'select name from checkitem where id={i[0]} '
                                cur.execute(sql5)
                                a2 = cur.fetchall()
                                Dia.insert(tk.END, f'\n检查单：{a2[0][0]}')
                        except:
                            tk.messagebox.showinfo('', "此病人不存在")
                        else:
                            tk.messagebox.showinfo(title='', message='查询成功!')


                    def cancel():
                        l1.destroy()
                        No.destroy()
                        l2.destroy()
                        Dia.destroy()
                        b2.destroy()
                        b3.destroy()

                    b3 = tk.Button(mainwindow,text='查询患者信息', font=10, command=input)
                    b3.place(x=540, y=270)
                    b2=tk.Button(mainwindow,text='返回', font=10, command=cancel)
                    b2.place(x=650, y=270)

                def items():
                    first.destroy()
                    sql = 'select name from checkitem'
                    cur.execute(sql)
                    items = cur.fetchall()
                    print(items)
                    varNo = tk.StringVar()
                    l1 = tk.Label(mainwindow,text='患者ID:', font=20)
                    l1.place(x=240, y=270)
                    No = tk.Entry(mainwindow,show=None, textvariable=varNo, font=21, width=15)
                    No.place(x=340, y=270)
                    l3 = tk.Label(mainwindow,text='检查单信息:', font=20)
                    l3.place(x=240, y=310)
                    t = tk.Text(mainwindow,highlightbackground="black",height=8,width=50,font=20)
                    t.place(x=340,y=310)
                    l2 = tk.Label(mainwindow,text='检查项目:', font=20)
                    l2.place(x=240, y=500)
                    itemList = ttk.Combobox(mainwindow,font=20,width=30)
                    itemList.place(x=340,y=500)
                    itemList['value'] = items



                    def take():
                        pnum = varNo.get()
                        iname = itemList.get()
                        content = t.get('1.0','end')
                        now_time = datetime.datetime.now()
                        sql = f'select * from patients where id={pnum}'
                        cur.execute(sql)
                        a = cur.fetchone()
                        d_id= data[0]
                        sql = f'select * from checkitem where name =\'{iname}\''
                        print(sql)
                        cur.execute(sql)
                        a1 = cur.fetchone()
                        item_id = a1[0]
                        item_price = a1[2]


                        if a == None:
                            tk.messagebox.showinfo(title='', message='检查单开立失败,病人不存在!')
                            print("Successfully Handeling!")
                        else:
                            sql = f'select * from patients where id ={pnum}'
                            cur.execute(sql)
                            d = cur.fetchone()
                            if(d[5]<item_price):
                                tk.messagebox.showinfo(title='', message='检查单开立失败,余额不足!')
                            else:
                                sql = f'insert into checklist values(null,now(),\'{content}\')'
                                print(sql)
                                cur.execute(sql)
                                conn.commit()
                                sql = f'select id from checklist order by id desc limit 1'
                                cur.execute(sql)
                                a= cur.fetchone()
                                sql = f'insert into r_checklist values({d_id},{pnum},{a[0]},{item_id})'
                                print(sql)
                                cur.execute(sql)
                                conn.commit()
                                sql = f'update patients set balance = balance-{item_price} where id = {pnum}'
                                cur.execute(sql)
                                conn.commit()
                                sql = f'insert into account values(null,\'消费\',{item_price},\'检查单\',now(),{pnum})'
                                cur.execute(sql)
                                conn.commit()
                                tk.messagebox.showinfo(title='', message=f'检查单开立成功,扣除金额{item_price}元')

                    def cancel():
                        l1.destroy()
                        l2.destroy()
                        b2.destroy()
                        b3.destroy()
                        l3.destroy()
                        itemList.destroy()
                        t.destroy()
                        No.destroy()


                    b2 = tk.Button(mainwindow,text='返回', font=10, command=cancel)
                    b2.place(x=650, y=270)
                    b3 = tk.Button(mainwindow,text='开立检查项目', font=10, command=take)
                    b3.place(x=550, y=270)  # 录入系统键
                    # Dia = tk.Text(height=5, font=21)
                    # Dia.place(x=240, y=100)

                def prescription():
                    first.destroy()
                    sql = 'select name from medicine'
                    cur.execute(sql)
                    medicines = cur.fetchall()
                    print(medicines)
                    varNo = tk.StringVar()
                    l1 = tk.Label(mainwindow,text='患者ID :', font=20)
                    l1.place(x=240, y=270)
                    No = tk.Entry(mainwindow,show=None, textvariable=varNo, font=21, width=15)
                    No.place(x=340, y=270)
                    l4 = tk.Label(mainwindow,text='处方信息:', font=20)
                    l4.place(x=240, y=310)
                    t = tk.Text(mainwindow,highlightbackground="black",height=8, width=50,font=20)
                    t.place(x=340, y=310)
                    l2 = tk.Label(mainwindow,text='药品清单:', font=20)
                    l2.place(x=240, y=500)
                    medList = ttk.Combobox(mainwindow,font=20, width=30)
                    medList.place(x=340, y=500)
                    medList['value'] = medicines
                    varQuantity = tk.IntVar()
                    l3 = tk.Label(mainwindow,text='数量:', font=20)
                    l3.place(x=240, y=540)
                    q = tk.Entry(mainwindow,show=None, textvariable=varQuantity, font=21, width=15)
                    q.place(x=340, y=540)


                    def take():
                        pnum = varNo.get()
                        mname = medList.get()
                        quantity = varQuantity.get()
                        now_time = datetime.datetime.now()
                        sql = f'select * from patients where id={pnum}'
                        cur.execute(sql)
                        a = cur.fetchone()
                        d_id = data[0]
                        sql = f'select * from medicine where name =\'{mname}\''
                        cur.execute(sql)
                        a1 = cur.fetchone()
                        medicine_id = a1[0]
                        medicine_price = a1[2]*quantity
                        content = t.get('1.0','end')

                        if a == None:
                            tk.messagebox.showinfo(title='', message='处方开立失败,病人不存在!')
                            print("Successfully Handeling!")
                        else:
                            sql = f'select * from patients where id ={pnum}'
                            cur.execute(sql)
                            d = cur.fetchone()
                            if (d[5] < medicine_price):
                                tk.messagebox.showinfo(title='', message='处方开立失败,余额不足!')
                            else:
                                sql = f'insert into prescription values(null,now(),\'{content}\',\'{mname}\')'
                                cur.execute(sql)
                                conn.commit()
                                sql = f'select id from prescription order by id desc limit 1'
                                cur.execute(sql)
                                a = cur.fetchone()
                                sql = f'insert into r_prescription values({d_id},{pnum},{a[0]},{medicine_id})'
                                cur.execute(sql)
                                conn.commit()
                                sql = f'update patients set balance = balance-{medicine_price} where id = {pnum}'
                                cur.execute(sql)
                                conn.commit()
                                sql = f'insert into account values(null,\'消费\',{medicine_price},\'处方\',now(),{pnum})'
                                cur.execute(sql)
                                conn.commit()
                                tk.messagebox.showinfo(title='', message=f'处方开立成功,扣除金额{medicine_price}元')


                    def cancel():
                        l1.destroy()
                        l2.destroy()
                        l3.destroy()
                        b2.destroy()
                        b3.destroy()
                        l4.destroy()
                        t.destroy()
                        medList.destroy()
                        No.destroy()
                        q.destroy()

                    b2 = tk.Button(mainwindow,text='返回', font=10, command=cancel)
                    b2.place(x=700, y=270)
                    b3 = tk.Button(mainwindow,text='开立处方', font=10, command=take)
                    b3.place(x=600, y=270)  # 录入系统键

                def hos():

                    first.destroy()
                    varNo = tk.StringVar()
                    l2 = tk.Label(mainwindow,text='患者ID :', font=20)
                    l2.place(x=240, y=270)
                    No2 = tk.Entry(mainwindow,show=None, textvariable=varNo, font=21, width=15)
                    No2.place(x=340, y=270)
                    days = tk.IntVar()
                    l1 = tk.Label(mainwindow,text='住院天数 :', font=20)
                    l1.place(x=240, y=370)
                    l3 = tk.Label(mainwindow,text='剩余总床位 :', font=20)
                    l3.place(x=240, y=500)
                    sql = f'select count(*) from bed where patient=-1'
                    cur.execute(sql)
                    count = cur.fetchone()[0]
                    l4 = tk.Text(mainwindow,height=3,width=5,font=20)
                    l4.place(x=320,y=500)
                    l4.insert('1.0',f'{count}')
                    No = tk.Entry(mainwindow,show=None, textvariable=days, font=21, width=15)
                    No.place(x=340, y=370)

                    def cancel():
                        l1.destroy()
                        No.destroy()
                        b2.destroy()
                        b3.destroy()
                        l2.destroy()
                        l3.destroy()
                        l4.destroy()
                        No2.destroy()

                    def input():
                        pid = varNo.get()
                        day = days.get()
                        sql = f'select count(*) from bed where patient=-1'
                        cur.execute(sql)
                        count = cur.fetchone()[0]
                        sql = f'select * from patients where id={varNo.get()}'
                        cur.execute(sql)
                        ddd = cur.fetchone()

                        if count<=0:
                            tk.messagebox.showinfo(title='', message=f'床位不足')
                        elif ddd==None:
                            tk.messagebox.showinfo(title='', message=f'病人不存在')
                        else:

                            sql = f'select * from bed where patient=-1 && r_id=(select id from room where vacancy>=1&&d_id=(select d_id from doctors where id={pid1})limit 1) order by Rand()  limit 1'
                            cur.execute(sql)
                            a = cur.fetchone()
                            if a==None:
                                tk.messagebox.showinfo(title='', message=f'该科室床位不足，请耐心等待')
                            else:
                                sql = f'select price from room where id = {a[3]}'
                                cur.execute(sql)
                                price = cur.fetchone()[0]
                                total_price = price * day
                                sql = f'select balance from patients where id = {pid}'
                                cur.execute(sql)
                                ba = cur.fetchone()[0]
                                if ba<total_price:
                                    tk.messagebox.showinfo(title='', message=f'余额不足')
                                elif ddd[6]!=None:
                                    tk.messagebox.showinfo(title='', message=f'病人未出院')
                                else:
                                    sql = f'update room set vacancy=vacancy-1 where id = {a[3]}'
                                    cur.execute(sql)
                                    conn.commit()

                                    sql = f'update bed set patient={pid}, time = now() where id = {a[0]}'
                                    cur.execute(sql)
                                    conn.commit()

                                    sql = f'update patients set n_id=(select id from nurses where d_id=(select d_id from doctors where id={pid1}) order by Rand() limit 1) where id = {pid}'
                                    cur.execute(sql)
                                    conn.commit()

                                    sql = f'update patients set balance= balance - {total_price} where id = {pid}'
                                    cur.execute(sql)
                                    conn.commit()

                                    sql = f'insert into account values(null,\'消费\',{total_price},\'住院\',now(),{pid})'
                                    cur.execute(sql)
                                    conn.commit()

                                    tk.messagebox.showinfo(title='', message=f'住院成功,扣除金额{total_price}元')

                                    sql = f'select count(*) from bed where patient=-1'
                                    cur.execute(sql)
                                    count = cur.fetchone()[0]
                                    l4.delete('1.0', 'end')
                                    l4.insert('1.0', f'{count}')

                    b2 = tk.Button(mainwindow,text='返回', font=10, command=cancel)
                    b2.place(x=700, y=270)
                    b3 = tk.Button(mainwindow,text='住院', font=10, command=input)
                    b3.place(x=600, y=270)



                font1 = tkFont.Font(family='times', size=24, weight='bold')
                button1 = tk.Button(mainwindow, text="查询患者信息", command=diagnose, activebackground="blue",
                                    activeforeground="red",
                                    fg="green", bg="green", font=font1)
                button2 = tk.Button(mainwindow, text="检查项目开立", command=items, activebackground="blue",
                                    activeforeground="red", fg="green", bg="green", font=font1)
                button3 = tk.Button(mainwindow, text="处方项目开立", command=prescription, activebackground="blue",
                                    activeforeground="red", fg="green", bg="green", font=font1)

                button4 = tk.Button(mainwindow, text="住院", command=hos, activebackground="blue",
                                    activeforeground="red", fg="green", bg="green", font=font1)


                button1.place(x=200, y=200)


                button2.place(x=400, y=200)


                button3.place(x=600, y=200)

                button4.place(x=800, y=200)


                mainwindow.mainloop()
    def cancel():
        window.destroy()

    tk.Button(window,text='登录',fg='green',font =('KacstBook',20,'italic'), highlightbackground='yellowgreen',bd=2,width=5,height=1,command = login).place(x=370,y=500)
    tk.Button(window,text='取消',fg='red',font =('KacstBook',20,'italic'),highlightbackground='yellowgreen',width=5,height=1,command = cancel).place(x=640,y=500)
    window.mainloop()

def register():
    window1 = tk.Toplevel()
    window1.title('患者注册')
    window1.geometry("1100x700+250+120")
    window1.resizable(0, 0)
    img = Image.open('picture/hospital.png')  # 打开图片
    photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
    tk.Label(window1, image=photo).place(x=270, y=5)
    name = tk.StringVar()
    l1 = tk.Label(window1,text='患者姓名 :', font=20)
    l1.place(x=380, y=200)
    l2 = tk.Entry(window1,show=None, textvariable=name, font=21, width=15)
    l2.place(x=520, y=200)
    nid = tk.StringVar()
    l3 = tk.Label(window1, text='身份证号 :', font=20)
    l3.place(x=380, y=250)
    l4 = tk.Entry(window1, show=None, textvariable=nid, font=21, width=15)
    l4.place(x=520, y=250)
    sex = tk.StringVar()
    l5 = tk.Label(window1, text='性别 :', font=20)
    l5.place(x=380, y=300)
    l6 = tk.Entry(window1, show=None, textvariable=sex, font=21, width=15)
    l6.place(x=520, y=300)
    dob = tk.StringVar()
    l7 = tk.Label(window1, text='出生日期 :', font=20)
    l7.place(x=380, y=350)
    l8 = tk.Entry(window1, show=None, textvariable=dob, font=21, width=15)
    l8.place(x=520, y=350)
    user = tk.StringVar()
    l9 = tk.Label(window1, text='用户名 :', font=20)
    l9.place(x=380, y=400)
    l10 = tk.Entry(window1, show=None, textvariable=user, font=21, width=15)
    l10.place(x=520, y=400)
    password = tk.StringVar()
    l11= tk.Label(window1, text='密码 :', font=20)
    l11.place(x=380, y=450)
    l12 = tk.Entry(window1, show=None, textvariable=password, font=21, width=15)
    l12.place(x=520, y=450)

    def r():
        name1 = name.get()
        nid1 = nid.get()
        sex1 = sex.get()
        dob1 = dob.get()
        username1 = user.get()
        password1 = password.get()
        sql = f'select nationalid from patients where nationalid=\'{nid1}\''
        cur.execute(sql)
        x1 = cur.fetchone()
        sql1 = f'select username from users where username=\'{username1}\''
        cur.execute(sql1)
        x2 = cur.fetchone()
        if x1 != None:
            tk.messagebox.showwarning(title='警告', message='该用户已存在')
        elif x2 != None:
            tk.messagebox.showwarning(title='警告', message='用户名重复')
        else:
            try:
                sql = f'insert into users values(null,\'{username1}\',\'{password1}\',\'病人\')'
                cur.execute(sql)
                conn.commit()
                sql = f'select id from users order by id desc limit 1'
                cur.execute(sql)
                a = cur.fetchone()
                sql = f'delete from users where username=\'\' or password=\'\''
                cur.execute(sql)
                conn.commit()
                sql = f'insert into patients values({a[0]},\'{name1}\',\'{nid1}\',\'{sex1}\',{dob1},0,null)'
                cur.execute(sql)
                conn.commit()
                tk.messagebox.showinfo(title='', message='注册成功')
            except:
                tk.messagebox.showinfo(title='警告', message='输入信息有误，请重新输入')
    def c():
        window1.destroy()
    l13 = tk.Button(window1, text='注册',width=5,height=1,highlightbackground='YellowGreen', font =('KacstBook',20,'italic'), command=r)
    l13.place(x=370, y=550)
    l14 = tk.Button(window1, text='取消',width=5,height=1, font =('KacstBook',20,'italic'), command=c,highlightbackground='red',)
    l14.place(x=620, y=550)
    window1.mainloop()

def jianjie():

    window1 = tk.Toplevel()
    window1.title('医院简介')
    window1.geometry("1100x700+250+120")
    window1.resizable(0, 0)
    img = Image.open('picture/xie1.png')
    photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
    imglabel = tk.Label(window1, image=photo).place(x=-3, y=-3)


    def can():
        window1.destroy()
    P10 = tk.Button(window1, text="返回", command=can, width=7, height=1, fg='green',
                   highlightbackground='YellowGreen', font=('KacstBook', 20, 'italic'))
    P10.place(x=500, y=600)

    window1.mainloop()

def chaxun():
    window2 = tk.Toplevel()
    window2.title('查询统计')
    window2.geometry("1000x700+250+250")
    window2.resizable(0, 0)
    img = Image.open('picture/hospital.png')  # 打开图片
    photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
    imglabel = tk.Label(window2, image=photo).place(x=240, y=0)
    img1 = Image.open('picture/yisheng.png')  # 打开图片
    photo1 = ImageTk.PhotoImage(img1)  # 用PIL模块的PhotoImage打开
    imglabel = tk.Label(window2, image=photo1).place(x=305, y=220)
    img2 = Image.open('picture/yaopin.png')  # 打开图片
    photo2 = ImageTk.PhotoImage(img2)  # 用PIL模块的PhotoImage打开
    imglabel2 = tk.Label(window2, image=photo2).place(x=605, y=220)
    img3 = Image.open('picture/keshi.png')  # 打开图片
    photo3 = ImageTk.PhotoImage(img3)  # 用PIL模块的PhotoImage打开
    imglabel3 = tk.Label(window2, image=photo3).place(x=310, y=470)
    img4 = Image.open('picture/jiancha.png')  # 打开图片
    photo4 = ImageTk.PhotoImage(img4)  # 用PIL模块的PhotoImage打开
    imglabel4 = tk.Label(window2, image=photo4).place(x=605, y=470)
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    def sort(a):
        return dict(sorted(a.items(), key=lambda x: x[1], reverse=True)[:10])
    def doc():
        window3 = tk.Toplevel()
        window3.title('人气医生')
        window3.geometry("1000x700+250+250")
        window3.resizable(0, 0)
        sql = f'select * from doctor_patient'
        cur.execute(sql)
        dp = cur.fetchall()
        sql = f'select * from doctors'
        cur.execute(sql)
        d = cur.fetchall()
        id_doctor = {}
        for i in d:
            id_doctor[i[0]] = i[1]
        doctor_count = {}
        for i in id_doctor:
            doctor_count[id_doctor[i]] = 0
        for i in dp:
            name = id_doctor[i[0]]
            doctor_count[name] += 1
        doctor_count = sort(doctor_count)
        x1 = list(doctor_count.keys())
        x2 = list(doctor_count.values())
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        df = pd.DataFrame({'医生姓名': x1, '挂号数量': x2})
        fig1 = plt.figure(figsize=(10, 5))
        ax1 = fig1.add_subplot(1, 1, 1)
        df.plot.bar(title="医生挂号数量统计", x='医生姓名', y='挂号数量', rot=0, ax=ax1)
        canvas = FigureCanvasTkAgg(fig1, window3)
        canvas.get_tk_widget().place(x=0, y=100)
        def can():
            window3.destroy()
        P10 = tk.Button(window3, text="返回", command=can, width=7, height=1, fg='green',
                        highlightbackground='YellowGreen', font=('KacstBook', 20, 'italic'))
        P10.place(x=470, y=620)
        window3.mainloop()
    def med():
        window4 = tk.Toplevel()
        window4.title('热销药品')
        window4.geometry("1000x700+250+250")
        window4.resizable(0, 0)
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        sql = f'select * from medicine'
        cur.execute(sql)
        m = cur.fetchall()
        sql = f'select * from r_prescription'
        cur.execute(sql)
        rm = cur.fetchall()
        medicine_count = {}
        id_medicine = {}
        for i in m:
            medicine_count[i[1]] = 0
            id_medicine[i[0]] = i[1]
        for i in rm:
            medicine_count[id_medicine[i[3]]] += 1
        medicine_count = sort(medicine_count)
        x1 = list(medicine_count.keys())
        x2 = list(medicine_count.values())
        df = pd.DataFrame({'药品名称': x1, '开立数量': x2})
        fig1 = plt.figure(figsize=(10, 5))
        ax1 = fig1.add_subplot(1, 1, 1)
        df.plot.pie(title="药品处方开立数量统计", labels=x1, y='开立数量', figsize=(10, 5),ax=ax1)
        canvas = FigureCanvasTkAgg(fig1, window4)
        canvas.get_tk_widget().place(x=0, y=100)
        def can():
            window4.destroy()
        P10 = tk.Button(window4, text="返回", command=can, width=7, height=1, fg='green',
                        highlightbackground='YellowGreen', font=('KacstBook', 20, 'italic'))
        P10.place(x=470, y=620)

        window4.mainloop()
    def dep():
        window5 = tk.Toplevel()
        window5.title('热门科室')
        window5.geometry("1000x700+250+250")
        window5.resizable(0, 0)
        sql = f'select * from doctor_patient'
        cur.execute(sql)
        dp = cur.fetchall()
        sql = f'select * from doctors'
        cur.execute(sql)
        d = cur.fetchall()
        sql = f'select * from department'
        cur.execute(sql)
        de = cur.fetchall()
        id_department = {}
        for i in de:
            id_department[i[0]] = i[1]
        doctor_count_d = {}
        for i in de:
            doctor_count_d[i[1]] = 0
        doctor_department = {}
        for i in d:
            doctor_department[i[0]] = i[3]
        for i in dp:
            doctor_count_d[id_department[doctor_department[i[0]]]] += 1
        doctor_count_d = sort(doctor_count_d)
        x1 = list(doctor_count_d.keys())
        x2 = list(doctor_count_d.values())
        df = pd.DataFrame({'科室名称': x1, '挂号数量': x2})
        fig1 = plt.figure(figsize=(10, 5))
        ax1 = fig1.add_subplot(1, 1, 1)
        df.plot.line(title="科室挂号数量统计", x='科室名称', y='挂号数量', rot=0, figsize=(10, 5),ax=ax1)
        canvas = FigureCanvasTkAgg(fig1, window5)
        canvas.get_tk_widget().place(x=0, y=100)

        def can():
            window5.destroy()

        P10 = tk.Button(window5, text="返回", command=can, width=7, height=1, fg='green',
                        highlightbackground='YellowGreen', font=('KacstBook', 20, 'italic'))
        P10.place(x=470, y=620)
        window5.mainloop()

    def chec():
        window6 = tk.Toplevel()
        window6.title('火热检查')
        window6.geometry("1000x700+250+250")
        window6.resizable(0, 0)
        sql = f'select * from checkitem'
        cur.execute(sql)
        ci = cur.fetchall()
        sql = f'select * from r_checklist'
        cur.execute(sql)
        rci = cur.fetchall()
        checkitem_count = {}
        id_checkitem = {}
        for i in ci:
            checkitem_count[i[1]] = 0
            id_checkitem[i[0]] = i[1]
        for i in rci:
            checkitem_count[id_checkitem[i[3]]] += 1
        checkitem_count = sort(checkitem_count)
        x1 = list(checkitem_count.keys())
        x2 = list(checkitem_count.values())
        df = pd.DataFrame({'检查项目名称': x1, '开立数量': x2})
        fig1 = plt.figure(figsize=(10, 5))
        ax1 = fig1.add_subplot(1, 1, 1)
        df.plot.barh(title="检查项目开立数量统计", x='检查项目名称', y='开立数量', rot=0, figsize=(10, 5),ax=ax1)
        canvas = FigureCanvasTkAgg(fig1, window6)
        canvas.get_tk_widget().place(x=0, y=100)
        def can():
            window6.destroy()

        P10 = tk.Button(window6, text="返回", command=can, width=7, height=1, fg='green',
                        highlightbackground='YellowGreen', font=('KacstBook', 20, 'italic'))
        P10.place(x=470, y=620)
        window6.mainloop()



    p11 = tk.Button(window2,text="人气医生",  width=7, height=1,command=doc, fg='green', highlightbackground='YellowGreen', font=('KacstBook', 20, 'italic'))
    p11.place(x=310,y=340)
    p12 = tk.Button(window2, text="热销药品", width=7, height=1,command=med, fg='green', highlightbackground='YellowGreen',
                    font=('KacstBook', 20, 'italic'))
    p12.place(x=610, y=340)
    p13 = tk.Button(window2, text="热门科室", width=7, height=1,command=dep, fg='green', highlightbackground='YellowGreen',
                    font=('KacstBook', 20, 'italic'))
    p13.place(x=310, y=590)
    p14 = tk.Button(window2, text="热门检查", width=7, height=1,command=chec, fg='green', highlightbackground='YellowGreen',
                    font=('KacstBook', 20, 'italic'))
    p14.place(x=610, y=590)

    window2.mainloop()


P = tk.Button(window0, text="登陆", command=denglu,width=5,height=1,fg='green',highlightbackground='YellowGreen',font =('KacstBook',20,'italic'))
P.place(x=355,y=310)
P1 = tk.Button(window0, text="注册", command=register,width=5,height=1,fg='green',highlightbackground='YellowGreen',font =('KacstBook',20,'italic'))
P1.place(x=605,y=310)
P2 = tk.Button(window0, text="医院简介",width=7,height=1,command= jianjie,fg='green',highlightbackground='YellowGreen',font =('KacstBook',20,'italic'))
P2.place(x=348,y=510)
P3 = tk.Button(window0, text="查询统计",width=7,height=1,command=chaxun,fg='green',highlightbackground='YellowGreen',font =('KacstBook',20,'italic'))
P3.place(x=598,y=510)

window0.mainloop()









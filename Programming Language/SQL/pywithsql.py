from networkx import cubical_graph
import pymysql
from tkinter import *
from tkinter import messagebox

from sympy import root

passwd = ''

#연결
# conn = pymysql.connect(host='127.0.0.1', port=3306,user='root', password= passwd,db='soloDB', charset='utf8')
# cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS userTable")
# cur.execute("CREATE TABLE userTable (id CHAR(4), userName CHAR(15), email CHAR(15), birthYear INT)")
# cur.execute("INSERT INTO userTable VALUES('hong', '홍지윤', 'hong@naver.com', 1996)")
# cur.execute("INSERT INTO userTable VALUES('kim', '김태연', 'kim@daum.net', 2011)")
# cur.execute("INSERT INTO userTable VALUES('star', '별사랑', 'star@paran.com', 1990)")
# cur.execute("INSERT INTO userTable VALUES('yang', '양지은', 'yang@gmail.com', 1993)")

# conn.commit()
# conn.close()


# #input으로 쿼리 입력

# conn, cur = None, None
# data1, data2, data3, data4 = "", "", "", ""
# sql = ""

# conn = pymysql.connect(host='127.0.0.1', port=3306,user='root', password= passwd,db='soloDB', charset='utf8')
# cur = conn.cursor()

# while True:
#     data1 = input("사용자 ID ==> ")
#     if data1 == "" : break;
#     data2 = input("사용자 이름 ==> ")
#     data3 = input("이메일 ==> ")
#     data4 = input("출생년도 ==> ")
#     sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
#     cur.execute(sql)

# conn.commit()
# conn.close()

# strtest = "heck"
# print("'+ heck + '")
    

# #쿼리 조회
# con, cur = None, None   
# data1, data2, data3, data4 = "", "", "", ""
# row = None

# conn = pymysql.connect(host='127.0.0.1', port=3306,user='root', password= passwd,db='soloDB', charset='utf8')
# cur = conn.cursor()

# cur.execute("SELECT * FROM userTable")
# print("사용자ID   사용자이름   이메일   출생년도")
# print("--------------------------------------------------")

# while (True) :
#     row = cur.fetchone()
#     if row == None :
#         break;
#     data1 = row[0]; data2 = row[1]
#     data3 = row[2]; data4 = row[3]
#     print("%5s %15s %15s %d" % (data1, data2, data3, data4))

# conn.close()


# #tkinter
def insertData():
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""

    conn = pymysql.connect(host='127.0.0.1', port=3306,user='root', password= passwd,db='soloDB', charset='utf8')
    cur = conn.cursor()

    data1 = edt1.get(); data2 = edt2.get()
    data3 = edt3.get(); data4 = edt4.get()
    sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(sql)

    conn.commit()
    conn.close()

    messagebox.showinfo("성공", "데이터 입력 성공")

def selectData():
    strData1, strData2, strData3, strData4 = [], [], [], []

    conn = pymysql.connect(host='127.0.0.1', port=3306,user='root', password= passwd,db='soloDB', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userTable")

    strData1.append("사용자ID"); strData2.append("사용자이름")
    strData3.append("이메일"); strData4.append("출생년도")
    strData1.append("----------"); strData2.append("----------")
    strData3.append("----------"); strData4.append("----------")

    while (True) :
        row = cur.fetchone()
        if row == None :
            break;
        strData1.append(row[0]); strData2.append(row[1])
        strData3.append(row[2]); strData4.append(row[3])
    
    listData1.delete(0, listData1.size() - 1); listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1); listData4.delete(0, listData4.size() - 1)

    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, item1); listData2.insert(END, item2)
        listData3.insert(END, item3); listData4.insert(END, item4)
    
    conn.close()

root = Tk()
root.geometry("600x400")
root.title("GUI with SQL")

edtFrame = Frame(root); edtFrame.pack()
listFrame = Frame(root); listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

edt1 = Entry(edtFrame, width=10); edt1.pack(side=LEFT, padx=10, pady=10)
edt2 = Entry(edtFrame, width=10); edt2.pack(side=LEFT, padx=10, pady=10)
edt3 = Entry(edtFrame, width=10); edt3.pack(side=LEFT, padx=10, pady=10)
edt4 = Entry(edtFrame, width=10); edt4.pack(side=LEFT, padx=10, pady=10)

btnInsert = Button(edtFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)
btnSelect = Button(edtFrame, text="조회", command=selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)

listData1 = Listbox(listFrame, bg='yellow'); listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame, bg='yellow'); listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame, bg='yellow'); listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame, bg='yellow'); listData4.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()



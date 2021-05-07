#import

from tkinter import *
import socket,threading
from tkinter import messagebox

#membuat window GUI untuk bermain
win = Tk()

playerAktif = True
ans = ''

LOCALHOST = "127.0.0.1"
PORT = 8080

clientsock, clientAddress = None, None

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")

def clientThread(ins):
    thread = threading.Thread(target = ins)
    thread.daemon = True
    thread.start()

def run():
    global playerAktif
    global ans
    while True:
        temp, clientAddress = clientsock.recvfrom(2048)
        msg = temp.decode()
        splitter = msg.split('-')
        ans = splitter[0]
        update()
        if splitter[1] == 'YourTurn':
            playerAktif = True
            print("giliran pemain 1")

def update():
    if ans == 'a':
        satuSatu()
    elif ans == 'b':
        satuDua()
    elif ans == 'c':
        satuTiga()
    elif ans == 'd':
        duaSatu()
    elif ans == 'e':
        duaDua()
    elif ans == 'f':
        duaTiga()
    elif ans == 'g':
        tigaSatu()
    elif ans == 'h':
        tigaDua()
    elif ans == 'i':
        tigaTiga()

def connection():
    global clientsock, clientAddress
    clientsock, clientAddress = server.accept()
    run()
clientThread(connection)

win.title("pemain 1 - tic tac toe")
win.geometry("400x400")
pemain1 = Label(win, text="pemain 1: X")
pemain1.grid(row=1, column=0)
pemain2 = Label(win, text="pemain2 2: O")
pemain2.grid(row=2, column=0)

def satuSatu():
    global ans
    global playerAktif
    if leftTopBtn["text"] == " " and playerAktif == True:
        leftTopBtn["text"] = "X"
        kirim = '{}-{}'.format('a','YourTurn').encode()
        clientsock.send(kirim)
        playerAktif = False
        check()
    elif ans == 'a' and playerAktif == False:
        leftTopBtn["text"] = "O"
        playerAktif = True
        check()

def satuDua():
    global ans
    global playerAktif
    if centerTopBtn["text"] == " " and playerAktif == True:
        centerTopBtn["text"] = "X"
        kirim = '{}-{}'.format('b','YourTurn').encode()
        clientsock.send(kirim)
        playerAktif = False
        check()
    elif ans == 'b' and playerAktif == False:
        centerTopBtn["text"] = "O"
        playerAktif = True
        check()

def satuTiga():
    global ans
    global playerAktif
    if rightTopBtn["text"] == " " and playerAktif == True:
        rightTopBtn["text"] = "X"
        kirim = '{}-{}'.format('c','YourTurn').encode()
        clientsock.send(kirim)
        playerAktif = False
        check()
    elif ans == 'c' and playerAktif == False:
        rightTopBtn["text"] = "O"
        playerAktif = True
        check()

def duaSatu():
    global ans
    global playerAktif
    if leftCenterBtn["text"] == " " and playerAktif == True:
        leftCenterBtn["text"] = "X"
        kirim = '{}-{}'.format('d','YourTurn').encode()
        clientsock.send(kirim)
        playerAktif = False
        check()
    elif ans == 'd' and playerAktif == False:
        leftCenterBtn["text"] = "O"
        playerAktif = True
        check()

def duaDua():
    global ans
    global playerAktif
    if centerCenterBtn["text"] == " " and playerAktif == True:
        centerCenterBtn["text"] = "X"
        kirim = '{}-{}'.format('e','YourTurn').encode()
        clientsock.send(kirim)
        playerAktif = False
        check()
    elif ans == 'e' and playerAktif == False:
        centerCenterBtn["text"] = "O"
        playerAktif = True
        check()

def duaTiga():
    global ans
    global playerAktif
    if rightCenterBtn["text"] == " " and playerAktif == True:
        rightCenterBtn["text"] = "X"
        kirim = '{}-{}'.format('f','YourTurn').encode()
        clientsock.send(kirim)
        playerAktif = False
        check()
    elif ans == 'f' and playerAktif == False:
        rightCenterBtn["text"] = "O"
        playerAktif = True
        check()
    
def tigaSatu():
    global ans
    global playerAktif
    if leftBottomBtn["text"] == " " and playerAktif == True:
        leftBottomBtn["text"] = "X"
        kirim = '{}-{}'.format('g','YourTurn').encode()
        clientsock.send(kirim)
        playerAktif = False
        check()
    elif ans == 'g' and playerAktif == False:
        leftBottomBtn["text"] = "O"
        playerAktif = True
        check()

def tigaDua():
    global ans
    global playerAktif
    if centerBottomBtn["text"] == " " and playerAktif == True:
        centerBottomBtn["text"] = "X"
        kirim = '{}-{}'.format('h','YourTurn').encode()
        clientsock.send(kirim)
        playerAktif = False
        check()
    elif ans == 'h' and playerAktif == False:
        centerBottomBtn["text"] = "O"
        playerAktif = True
        check()

def tigaTiga():
    global ans
    global playerAktif
    if rightBottomBtn["text"] == " " and playerAktif == True:
        rightBottomBtn["text"] = "X"
        kirim = '{}-{}'.format('i','YourTurn').encode()
        clientsock.send(kirim)
        playerAktif = False
        check()
    elif ans == 'i' and playerAktif == False:
        rightBottomBtn["text"] = "O"
        playerAktif = True
        check()

temp = 0
def check():
    global temp
    button1 = leftTopBtn["text"]
    button2 = centerTopBtn["text"]
    button3 = rightTopBtn["text"]
    button4 = leftCenterBtn["text"]
    button5 = centerCenterBtn["text"]
    button6 = rightCenterBtn["text"]
    button7 = leftBottomBtn["text"]
    button8 = centerBottomBtn["text"]
    button9 = rightBottomBtn["text"]
    temp += 1

    # Horizontal
    if (button1 == button2 and button1 == button3 and button1 == "O") or (button1 == button2 and button1 == button3 and button1 == "X"):
        checkMenang(leftTopBtn["text"])
    if (button4 == button5 and button4 == button6 and button4 == "O") or (button4 == button5 and button4 == button6 and button4 == "X"):
        checkMenang(leftCenterBtn["text"])
    if (button7 == button8 and button7 == button9 and button7 == "O") or (button7 == button8 and button7 == button9 and button7 == "X"):
        checkMenang(leftBottomBtn["text"])

    # Vertical
    if (button1 == button4 and button1 == button7 and button1 == "O") or (button1 == button4 and button1 == button7 and button1 == "X"):
        checkMenang(leftTopBtn["text"])
    if (button2 == button5 and button2 == button8 and button2 == "O") or (button2 == button5 and button2 == button8 and button2 == "X"):
        checkMenang(centerTopBtn["text"])
    if (button3 == button6 and button3 == button9 and button3 == "O") or (button3 == button6 and button3 == button9 and button7 == "X"):
        checkMenang(rightTopBtn["text"])

    # Diagonal
    if (button1 == button5 and button1 == button9 and button1 == "O") or (button1 == button5 and button1 == button9 and button1 == "X"):
        checkMenang(leftTopBtn["text"])
    if (button7 == button5 and button7 == button3 and button7 == "O") or (button7 == button5 and button7 == button3 and button7 == "X"):
        checkMenang(leftBottomBtn["text"])

    if temp == 9:
        messagebox.showinfo("permainan seri")
        win.destroy()
        # res = messagebox.askquestion("ingin bermain lagi?")
        # if res == 'yes':
        #     return 1 #clientThread(1)
        # else:
        #     sys.exit()

def checkMenang(ins):
    ans = ins + " menang!"
    messagebox.showinfo("ingin bermain lagi?", ans)
    win.destroy()
    # if res == 'yes':
    #     return 1 #clientThread(1)
    # else:
    #     sys.exit()

#button grid#

#baris 1

leftTopBtn = Button(win, text = " ", bg = "white", width = 6, height = 3, command = satuSatu)
leftTopBtn.grid(column = 1, row = 1)
centerTopBtn = Button(win, text = " ", bg = "white", width = 6, height = 3, command = satuDua)
centerTopBtn.grid(column = 2, row = 1)
rightTopBtn = Button(win, text = " ", bg = "white", width = 6, height = 3, command = satuTiga)
rightTopBtn.grid(column = 3, row = 1)

#baris 2
leftCenterBtn = Button(win, text = " ", bg = "white", width = 6, height = 3, command = duaSatu)
leftCenterBtn.grid(column = 1, row = 2)
centerCenterBtn = Button(win, text = " ", bg = "white", width = 6, height = 3, command = duaDua)
centerCenterBtn.grid(column = 2, row = 2)
rightCenterBtn = Button(win, text = " ", bg = "white", width = 6, height = 3,  command = duaTiga)
rightCenterBtn.grid(column = 3, row = 2)

#baris 3
leftBottomBtn = Button(win, text = " ", bg = "white", width = 6, height = 3, command = tigaSatu)
leftBottomBtn.grid(column = 1, row = 3)
centerBottomBtn = Button(win, text = " ", bg = "white", width = 6, height = 3, command = tigaDua)
centerBottomBtn.grid(column = 2, row = 3)
rightBottomBtn = Button(win, text = " ", bg = "white", width = 6, height = 3,  command = tigaTiga)
rightBottomBtn.grid(column = 3, row = 3)

win.mainloop()

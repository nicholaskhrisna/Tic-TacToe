# Import
import socket,threading
from tkinter import *
from tkinter import messagebox

# Penggunaan Tkinter
win = Tk()

giliran = True
box = ''

LOCALHOST = "127.0.0.1"
PORT = 8080

clientsock, clientAddress = None, None

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")

def createThread(ins):
    thread = threading.Thread(target = ins)
    thread.daemon = True
    thread.start()

def run():
    global giliran
    global box
    while True:
        temp, clientAddress = clientsock.recvfrom(2048)
        msg = temp.decode()
        splitter = msg.split('-')
        box = splitter[0]
        update()
        if splitter[1] == 'YourTurn':
            giliran = True
            print("giliran pemain 1")

def update():
    if box == 'a':
        satuSatu()
    elif box == 'b':
        satuDua()
    elif box == 'c':
        satuTiga()
    elif box == 'd':
        duaSatu()
    elif box == 'e':
        duaDua()
    elif box == 'f':
        duaTiga()
    elif box == 'g':
        tigaSatu()
    elif box == 'h':
        tigaDua()
    elif box == 'i':
        tigaTiga()

def connection():
    global clientsock, clientAddress
    clientsock, clientAddress = server.accept()
    run()

createThread(connection)



# GUI---------------------------------------------
win.title("Tic-Tac-Toe (Pemain 1 : X)")
win.geometry("400x300")
pemain1 = Label(win, text="Pemain 1 (Server) : X")
pemain1.grid(row=1, column=0)
pemain2 = Label(win, text="Pemain 2 (Client) : O")
pemain2.grid(row=2, column=0)
# GUI---------------------------------------------



# Fungsi tiap box---------------------------------
def satuSatu():
    global box
    global giliran
    if leftTopBtn["text"] == " " and giliran == True:
        leftTopBtn["text"] = "X"
        kirim = '{}-{}'.format('a','YourTurn').encode()
        clientsock.send(kirim)
        giliran = False
        check()
    elif box == 'a' and giliran == False:
        leftTopBtn["text"] = "O"
        giliran = True
        check()

def satuDua():
    global box
    global giliran
    if centerTopBtn["text"] == " " and giliran == True:
        centerTopBtn["text"] = "X"
        kirim = '{}-{}'.format('b','YourTurn').encode()
        clientsock.send(kirim)
        giliran = False
        check()
    elif box == 'b' and giliran == False:
        centerTopBtn["text"] = "O"
        giliran = True
        check()

def satuTiga():
    global box
    global giliran
    if rightTopBtn["text"] == " " and giliran == True:
        rightTopBtn["text"] = "X"
        kirim = '{}-{}'.format('c','YourTurn').encode()
        clientsock.send(kirim)
        giliran = False
        check()
    elif box == 'c' and giliran == False:
        rightTopBtn["text"] = "O"
        giliran = True
        check()

def duaSatu():
    global box
    global giliran
    if leftCenterBtn["text"] == " " and giliran == True:
        leftCenterBtn["text"] = "X"
        kirim = '{}-{}'.format('d','YourTurn').encode()
        clientsock.send(kirim)
        giliran = False
        check()
    elif box == 'd' and giliran == False:
        leftCenterBtn["text"] = "O"
        giliran = True
        check()

def duaDua():
    global box
    global giliran
    if centerCenterBtn["text"] == " " and giliran == True:
        centerCenterBtn["text"] = "X"
        kirim = '{}-{}'.format('e','YourTurn').encode()
        clientsock.send(kirim)
        giliran = False
        check()
    elif box == 'e' and giliran == False:
        centerCenterBtn["text"] = "O"
        giliran = True
        check()

def duaTiga():
    global box
    global giliran
    if rightCenterBtn["text"] == " " and giliran == True:
        rightCenterBtn["text"] = "X"
        kirim = '{}-{}'.format('f','YourTurn').encode()
        clientsock.send(kirim)
        giliran = False
        check()
    elif box == 'f' and giliran == False:
        rightCenterBtn["text"] = "O"
        giliran = True
        check()
    
def tigaSatu():
    global box
    global giliran
    if leftBottomBtn["text"] == " " and giliran == True:
        leftBottomBtn["text"] = "X"
        kirim = '{}-{}'.format('g','YourTurn').encode()
        clientsock.send(kirim)
        giliran = False
        check()
    elif box == 'g' and giliran == False:
        leftBottomBtn["text"] = "O"
        giliran = True
        check()

def tigaDua():
    global box
    global giliran
    if centerBottomBtn["text"] == " " and giliran == True:
        centerBottomBtn["text"] = "X"
        kirim = '{}-{}'.format('h','YourTurn').encode()
        clientsock.send(kirim)
        giliran = False
        check()
    elif box == 'h' and giliran == False:
        centerBottomBtn["text"] = "O"
        giliran = True
        check()

def tigaTiga():
    global box
    global giliran
    if rightBottomBtn["text"] == " " and giliran == True:
        rightBottomBtn["text"] = "X"
        kirim = '{}-{}'.format('i','YourTurn').encode()
        clientsock.send(kirim)
        giliran = False
        check()
    elif box == 'i' and giliran == False:
        rightBottomBtn["text"] = "O"
        giliran = True
        check()
# Fungsi tiap box---------------------------------



# Check kondisi menang----------------------------
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
        messagebox.showinfo("Permainan Seri")
        win.destroy()
        # res = messagebox.askquestion("ingin bermain lagi?")
        # if res == 'yes':
        #     return 1 #createThread(1)
        # else:
        #     sys.exit()

def checkMenang(ins):
    ans = "Pemain " + ins + " menang!"
    messagebox.showinfo("Permainan Selesai!", ans)
    win.destroy()
    # if res == 'yes':
    #     return 1 #createThread(1)
    # else:
    #     sys.exit()

# Check kondisi menang----------------------------



# Tampilan box permainan--------------------------

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

# Tampilan box permainan--------------------------
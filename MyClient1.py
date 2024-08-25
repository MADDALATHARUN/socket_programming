
#client

import socket
from tkinter import *
from tkinter import ttk
import threading

HEADER = 64
PORT = 5353
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.144.81"
sender_id = "ram"
recevier_id = "Tharun"
text = NONE
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Officially connecting to the server.
client.connect(ADDR)
client.send(sender_id.encode())

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
window=Tk()
window.title ('Chat')
window.geometry("300x400")
frame2 = Frame(window, bg = "white")
frame2.pack(side = BOTTOM)

def send_msg():
    display_text()
    client.send(recevier_id.encode())
    send(text)

def recevie_msg():
    global text
    while TRUE:
        text = client.recv(2048).decode(FORMAT)
        display_text("server")

def display_text(task = "client"):
    global text
    if task =="client":
        direction = "ne"
        text = text_box.get()
    else:
        direction = "nw"
    frame1 = Frame(window, height = 40, width = 300)
    frame1.pack(side = TOP, anchor = direction)
        
    if text:
        label = Label(frame1, text = text, fg = "white", bg = "black")
        label.pack(side = TOP, padx = 5, pady = 5, fill = 'x')  
        text_box.delete(0, END)

text_box = Entry(frame2, bg = "black", fg = "white", width = 40, relief = RAISED)
text_box.pack(side = LEFT, padx = 3 , pady = 0)

send_button = Button(frame2, text = "send", command = display_text, fg = "black", bg = "gray")
send_button.pack(side = RIGHT, padx = 2, pady = 10)

thread = threading.Thread(target = recevie_msg)
thread.start()
window.mainloop()

import tkinter as tk
import winsound 
from PIL import Image, ImageTk

# _____________________________Constant___________________________________
WIN_WIDTH = 1370
WIN_HEIGHT = 780
coin= 5
diamond=20

# _____________________________Variables__________________________________
levelGrid = []
isreset=[False,False,False]
iswin=[True,False,False]
swtict = True
isAllowtomove = True
countwin = 0
numcoin = 0
numdiamond=0
colorTime = 'black'

# _____________________________Function____________________________________
#  start game___________
def start(event):

    canvas.delete('all')
    canvas.create_image(0,0 , image=page1 , anchor='nw')
    canvas.create_text(500,50 , text="Jack's", font=("Lucky Coin", 100, "bold") ,fill='#223BC9', anchor='nw' )
    canvas.create_text(455,145 , text="Adventure", font=('Lucky Coin', 75) ,fill='#067FD0', anchor='nw' )

    # enter button
    canvas.create_image(510,200 , image=button , anchor='nw' , tags='enter')
    canvas.create_text(650,365 , text='START', font=('Zorque', 20) ,fill='white', anchor='nw' , tags='enter')
    # enter button
    canvas.create_image(510,300 , image=button , anchor='nw' , tags='info')
    canvas.create_text(650,465 , text='STORY', font=('Zorque', 20) ,fill='white', anchor='nw' , tags='info')
    # exit button
    canvas.create_image(510,400 , image=button, anchor='nw' , tags='exit')
    canvas.create_text(665,565 , text='EXIT', font=('Zorque', 20) ,fill='white', anchor='nw' , tags='exit')
#  exit game___________
def exitfromgame(event):
    canvas.quit()
#  info___________
def info(event):
    canvas.create_image(0,0 , image=button , anchor='nw')
    # go back
    canvas.create_image(20,20 , image=button , anchor='nw' , tags='back')
    canvas.create_text(65,45 , text='back', font=('Zorque', 30) , anchor='nw' , tags='back')
#  choose level___________
def chooslevel(event):
    global isreset
    canvas.delete('all')
    isreset=[False,False,False]
    # interface page level
    canvas.create_image(0,0 , image=page2 , anchor='nw')
    # go back
    canvas.create_image(20,20 , image=button , anchor='nw' , tags='back')
    canvas.create_text(65,45 , text='back', font=('Zorque',30) , anchor='nw' , tags='back')
    # level 1 
    canvas.create_image(300,240 , image = button , anchor = 'nw' , tags = 'level1')
    canvas.create_text(365,315 , text='Low', font = ('Zorque', 25) , anchor='nw' , tags='level1')
    # level 2
    canvas.create_image(600,240 , image = button, anchor='nw' , tags='level2')
    canvas.create_text(632,315 , text='Medium', font=('Zorque', 25) , anchor='nw' , tags='level2')
    # level 3
    canvas.create_image(900,240 , image=button , anchor='nw' , tags='level3')
    canvas.create_text(955,315 , text='Hard', font=('Zorque', 25) , anchor='nw' , tags='level3')
#  grid level low___________

# ____________________Main_________________________
root = tk.Tk()
root.geometry(str(WIN_WIDTH)+ 'x' + str(WIN_HEIGHT))
frame = tk.Frame(root)
canvas = tk.Canvas(frame)
root.title("Jack's Adventure")

icon = tk.PhotoImage(file='images/icon.png')
root.iconphoto(True,icon)
root.resizable(0,0)



# _____________________________Image_________________________________________

page1= ImageTk.PhotoImage(file="images/page1.jpg")
page2= ImageTk.PhotoImage(file="images/page2.jpg")
wall=ImageTk.PhotoImage(file="images/wall.png")
button=ImageTk.PhotoImage(file="images/button.png")

# _____________________________Call function__________________________________

start(event=start) 

# _____________________________button Bind___________________________________________

canvas.tag_bind('button', '<Button-1>',chooslevel)
canvas.tag_bind('button', '<Button-1>',start)
canvas.tag_bind('button', '<Button-1>',info)
# canvas.tag_bind('level1', '<Button-1>',gridLevelLow)
# canvas.tag_bind('Restart', '<Button-1>',reset)
# canvas.tag_bind('level2', '<Button-1>',gridLevelMedium)
# canvas.tag_bind('Menu', '<Button-1>',chooslevel)
# canvas.tag_bind('level3', '<Button-1>',gridLevelHard)
# canvas.tag_bind('exit', '<Button-1>',exitfromgame)
# canvas.tag_bind('next', '<Button-1>',nextlevel)
# canvas.tag_bind('bonus', '<Button-1>',gridLevelImpossible)
# canvas.tag_bind('next1', '<Button-1>',Congra)

frame.pack(expand=True, fill='both')
canvas.pack(expand=True, fill='both')
root.mainloop()
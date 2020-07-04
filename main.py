from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
from multiprocessing import Process
#from AnimatedGif import *
from tkinter import PhotoImage
from tkinter import Label
import pyglet

from ner import Parser
from object_detection_tutorial import parser_object
import random
import os
from difflib import get_close_matches

global propound,name
def HashtagPropounder():

    #keyword=["airplane","bear","bird","friend"]
    #keyword1=["new york","texas"]
    #p1 = Process(target = loading)
    #p1.start()
    global inputstr, propound,name
    p = Parser()

    p.load_models("models/")
    p1 = parser_object(name)
    keyword = p1.run_model()

    keyword1 = p.predict(inputstr)
    print(keyword1)

    files=os.listdir('C:/Hashtag Propounder/Hashtag Corpus/')
    hashtags=[]
    count = 0
    for i in keyword:
        j=i + ".txt"
        if j in files:
            file=open('C:/Hashtag Propounder/Hashtag Corpus/' + j)
            lines1=file.read().splitlines()
            hashtags.append(random.sample(lines1,k=3))
            count+=3
        else:
            c_file=open('C:/Hashtag Propounder/Hashtag Corpus/common.txt')
            lines2=c_file.read().splitlines()
            hashtags.append(get_close_matches(i,lines2))

    for i in keyword1:
        word=[]
        word.append("#"+i)
        hashtags.append(word)
        count+=1

    while(count<=30):
        count+=1
        c1_file=open("C:/Hashtag Propounder/Hashtag Corpus/common.txt")
        lines3=c1_file.read().splitlines()
        hashtags.append(random.sample(lines3,k=1))
        
    propound = []        
    for i in hashtags:
        for j in i:
            propound.append(j)
    print(propound)
    hashtagScreen()

class AnimatedGIF(Label, object):
    def __init__(self, master, path, forever=True):
        self._master = master
        self._loc = 0
        self._forever = forever

        self._is_running = False

        im = Image.open(path)
        self._frames = []
        i = 0
        try:
            while True:
                photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))
                self._frames.append(photoframe)

                i += 1
                im.seek(i)
        except EOFError: pass

        self._last_index = len(self._frames) - 1

        try:
            self._delay = im.info['duration']
        except:
            self._delay = 100

        self._callback_id = None

        super(AnimatedGIF, self).__init__(master, image=self._frames[0])

    def start_animation(self, frame=None):
        if self._is_running: return

        if frame is not None:
            self._loc = 0
            self.configure(image=self._frames[frame])

        self._master.after(self._delay, self._animate_GIF)
        self._is_running = True

    def stop_animation(self):
        if not self._is_running: return

        if self._callback_id is not None:
            self.after_cancel(self._callback_id)
            self._callback_id = None

        self._is_running = False

    def _animate_GIF(self):
        self._loc += 1
        self.configure(image=self._frames[self._loc])

        if self._loc == self._last_index:
            if self._forever:
                self._loc = 0
                self._callback_id = self._master.after(self._delay, self._animate_GIF)
            else:
                self._callback_id = None
                self._is_running = False
        else:
            self._callback_id = self._master.after(self._delay, self._animate_GIF)

    def pack(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).pack(**kwargs)

    def grid(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).grid(**kwargs)

    def place(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).place(**kwargs)

    def pack_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).pack_forget(**kwargs)

    def grid_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).grid_forget(**kwargs)

    def place_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).place_forget(**kwargs)

def loading():
    from tkinter import Tk, Label
    global root3
    print ("In loading")
    root3 = Tk()
    root3["bg"] = "white"
    root3.wm_attributes("-topmost", True)

    l = AnimatedGIF(root3, "loading.gif")
    l.place(x=500,y=500)
    l.pack()   
    root3.mainloop()

def imgcap(): #Interface 2
    global root
    root=Tk()
    root.title("Hashtags")
    #img = PhotoImage(file="bicon.png")

    BackImg2 = PhotoImage(file = 'browsebg.png')
    Frame2 = Frame(root)
    ImgLabel2 = Label(Frame2, image= BackImg2)
    root.wm_attributes("-topmost", True)
    b1=Button(Frame2,text='Browse',font=('times',24,'italic'),bd=0,width=15,bg='#84CFCC',command=eopen_file)
    b1.place(x=960,y=237)
    #b1.config(image=img)

    Frame2.pack(fill='both', expand=True,)
    ImgLabel2.pack(fill='both', expand=True,)
    #b1.pack()
    root.mainloop()

def hashtagScreen():
  global root4,name,inputstr,propound,listbox
  #msg=txt.get('1.0',END)
  def inserttext(item):
      global listbox
      txt.insert('end',' '+item)
      sel = listbox.curselection()
      for index in sel[::-1]:
          listbox.delete(index)   
  root4=Tk()
  root4.wm_attributes("-topmost", True)
  BackImg5 = PhotoImage(file = 'captionbg.png')
  Frame5 = Frame(root4)
  ImgLabel5 = Label(Frame5, image= BackImg5)
  UserImageBeforeRezise = Image.open(name)
  UserImage = UserImageBeforeRezise.resize((352, 352), Image.ANTIALIAS)
  UserImage = ImageTk.PhotoImage(UserImage)
  UserImageLabel = Label(root4, image=UserImage, bg = "#2c829e")
  UserImageLabel.config(height = 352,width = 352,font="Rockwell  10")
  UserImageLabel.place(x=75, y=59)
  b4=Button(root4,text="Home",bd=0,font=('times',24,'italic'),width=7,bg="#808285",command=destroy5)
  b4.place(x=82,y=635)
  
  listbox = Listbox(root4)
  for i in range(len(propound)):
      listbox.insert(i,propound[i])
  b5=Button(root4,text="Insert",bd=0,font=('times',24,'italic'),width=9,bg="#84CFCC",command=lambda:inserttext(listbox.get(ACTIVE)))
  b5.place(x=1120,y=622)
  
  txt=Text(root4,height=7,width=40,bd=0,font=('times',24,'italic'))
  txt.place(x=507,y=101)
  txt.insert('1.0',inputstr)
  listbox.place(x=490,y=404)
  Frame5.pack(fill='both', expand=True,)
  ImgLabel5.pack(fill='both', expand=True,)
  root4.mainloop()


def destroy():
    global window
    window.destroy()
    imgcap()
def destroy2():
    global root1
    root1.destroy()
    main()

def destroy3():
    global root2
    root2.destroy()
    main()

def destroy4():
    global root2,inputstr
    inputstr = textBox.get('1.0','end-1c')
    root2.destroy()
    
    HashtagPropounder()
    
def destroy5():
    global root4
    root4.destroy()
    main()

def ImageLoader(): #Interface 3
    global root1,root,name
    root.destroy()
    root1=Tk()
    root1.wm_attributes("-topmost", True)
    BackImg3 = PhotoImage(file = 'browse2bg.png')
    Frame3 = Frame(root1)
    ImgLabel3 = Label(Frame3, image= BackImg3)
    b2=Button(root1,text="Home",bd=0,font=('times',24,'italic'),width=7,bg="#84CFCC",command=destroy2)
    b2.place(x=990,y=237)
    b3=Button(root1,text="Caption",bd=0,font=('times',24,'italic'),width=9,bg="#a7a9ac",command=caption)
    b3.place(x=990,y=467)

    UserImageBeforeRezise = Image.open(name)
    UserImage = UserImageBeforeRezise.resize((550, 550), Image.ANTIALIAS)
    UserImage = ImageTk.PhotoImage(UserImage)
    UserImageLabel = Label(root1, image=UserImage, bg = "#2c829e")
    UserImageLabel.config(height = 550,width = 550,font="Rockwell  10")
    UserImageLabel.place(x=130, y=92)

    Frame3.pack(fill='both', expand=True,)
    ImgLabel3.pack(fill='both', expand=True,)
    root1.mainloop()


def caption(): #Interface 4
    global root2,name,textBox
    
    root1.destroy()
    root2=Tk()
    root2.wm_attributes("-topmost", True)
    BackImg4 = PhotoImage(file = 'captionbg.png')
    Frame4 = Frame(root2)
    ImgLabel4 = Label(Frame4, image= BackImg4)

    UserImageBeforeRezise = Image.open(name)
    UserImage = UserImageBeforeRezise.resize((352, 352), Image.ANTIALIAS)
    UserImage = ImageTk.PhotoImage(UserImage)
    UserImageLabel = Label(root2, image=UserImage, bg = "#2c829e")
    UserImageLabel.config(height = 352,width = 352,font="Rockwell  10")
    UserImageLabel.place(x=75, y=59)
    textBox=Text(root2,height=7,width=40,bd=0,font=('times',24,'italic'))
    textBox.place(x=507,y=101)
    
    b4=Button(root2,text="Home",bd=0,font=('times',24,'italic'),width=7,bg="#808285",command=destroy3)
    b4.place(x=82,y=635)
    b5=Button(root2,text="Analyze",bd=0,font=('times',24,'italic'),width=9,bg="#84CFCC",command=destroy4)
    b5.place(x=1120,y=622)

    Frame4.pack(fill='both', expand=True,)
    ImgLabel4.pack(fill='both', expand=True,)
    root2.mainloop()

# def loadscreen():
    # global root3,root2
    # root2.destroy
    # root3=Tk()
    # root3.wm_attributes("-fullscreen", True)
    # # canvas = Canvas(width = 300, height = 200, bg = 'yellow')
    # # canvas.pack(expand = YES, fill = BOTH)
    # # gif1 = PhotoImage(file = 'load.gif')
    # # canvas.create_image(50, 10, image = gif1, anchor = NW)

    # lbl_with_my_gif = AnimatedGif(root3, 'load.gif', 0.04)  # (tkinter.parent, filename, delay between frames)
    # lbl_with_my_gif.pack()  # Packing the label with the animated gif (grid works just as well)
    # lbl_with_my_gif.start()  # Shows gif at first frame and we are ready to go
    # lbl_with_my_gif.stop()
    # root3.mainloop()

def eopen_file():
    global name
    name = askopenfilename(initialdir="Pictures",filetypes =(("PNG File", "*.png"),("JPG File", "*.jpg"),("All Files","*.*")),title = "Choose a file.")

    if (name!=""):
        ImageLoader()


def main():    # INTERFACE 1
    global window
    window=Tk()
    window.wm_attributes("-topmost", 1)
#    BackImg1 = PhotoImage(file='homebg.png')
    path = 'homebg.png'
    img = ImageTk.PhotoImage(Image.open(path))
    Frame1 = Frame(window)
    ImgLabel1 = Label(Frame1, image= img)
    b1=Button(window,text="Next",width=10,bd=0,bg="#6ABE70",font=('times',15,'italic'),command=destroy).place(x=1220,y=666)
    b6=Button(window,text="Quit",width=10,bd=0,bg="#6ABE70",font=('times',15,'italic'),command=lambda:window.destroy()).place(x=200,y=666)          
    Frame1.pack(fill='both', expand=True,)
    ImgLabel1.pack(fill='both', expand=True,)


    #b2=Button(window,text="Quit",width=30,font=('times',15,'italic'),command=window.destroy).place(x=100,y=300)
    window.mainloop()

main()

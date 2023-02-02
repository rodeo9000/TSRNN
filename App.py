import os
import numpy
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from keras.models import load_model

#Loading the model
model = load_model('/home/rodean/Coding/traffic/model/CNN.h5')

#Type Names
Types = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)',      
            3:'Speed limit (50km/h)',       
            4:'Speed limit (60km/h)',      
            5:'Speed limit (70km/h)',    
            6:'Speed limit (80km/h)',      
            7:'End of speed limit (80km/h)',     
            8:'Speed limit (100km/h)',    
            9:'Speed limit (120km/h)',     
           10:'No passing',   
           11:'No passing veh over 3.5 tons',     
           12:'Right-of-way at intersection',     
           13:'Priority road',    
           14:'Yield',     
           15:'Stop',       
           16:'No vehicles',       
           17:'Veh > 3.5 tons prohibited',       
           18:'No entry',       
           19:'General caution',     
           20:'Dangerous curve left',      
           21:'Dangerous curve right',   
           22:'Double curve',      
           23:'Bumpy road',     
           24:'Slippery road',       
           25:'Road narrows on the right',  
           26:'Road work',    
           27:'Traffic signals',      
           28:'Pedestrians',     
           29:'Children crossing',     
           30:'Bicycles crossing',       
           31:'Beware of ice/snow',
           32:'Wild animals crossing',      
           33:'End speed + passing limits',      
           34:'Turn right ahead',     
           35:'Turn left ahead',       
           36:'Ahead only',      
           37:'Go straight or right',      
           38:'Go straight or left',      
           39:'Keep right',     
           40:'Keep left',      
           41:'Roundabout mandatory',     
           42:'End of no passing',      
           43:'End no passing veh > 3.5 tons' }
                          

def Upload():
    try:
        path = filedialog.askopenfilename()
        chosen = Image.open(path)
        chosen = chosen.resize((160, 160))
        image = ImageTk.PhotoImage(chosen)
        display_image.configure(image = image)
        display_image.image = image
        name.configure(text = '')

        Visible(path)
        new_button()

    except:
        print ("Failed to Upload Image")
        pass

def Source():
    source = Button(main, text = 'Source Code', padx = 10, pady = 5)
    source.configure(background = 'red', foreground = 'white', font = ('arial', 16, 'bold'))
    source.place(relx = 0.70, rely = 0.54)
    lintext = 'https://github.com/rodeo9000/Traffic-Sign-AI'
    link.configure(background = '#507af8', foreground = 'dark blue', text = linktext, font = ('comic sans', 18, 'bold'))

def Visible(path):
    classify = Button(main, text = "Classify Image", command = lambda: Classify(path), padx = 10, pady = 5)
    classify.configure(background = 'blue', foreground = 'white', font = ('arial', 16, 'bold'))
    classify.place(relx = 0.12, rely = 0.54)

def Classify(path):
    global label_packed
    image = Image.open(path)
    image = image.resize((40,40))
    image = numpy.expand_dims(image, axis = 0)
    image = numpy.array(image)
    prediction = model.predict([image])[0]
    prediction = numpy.argmax(prediction, axis = 0)
    type = Types[prediction + 1]
    name.configure(background = '#507af8', foreground = 'maroon', text = type, font = ('comic sans', 25, 'bold')) 
    
   
#Tkinter application
main = tk.Tk()
main.geometry('800x600')
main.title('Traffic Sign Recognition AI')
main.configure(background = '#507af8')

name = Label(main, background = 'black', font = ('comic sans', 25,'bold'))
display_image = Label(main)

upload = Button(main, text = "Upload Image", command = Upload , padx = 10, pady = 5)
upload.configure(background = 'black', foreground = 'white', font = ('comic sans', 16,'bold'))

upload.pack(side = BOTTOM, pady = 50)
display_image.pack(side = BOTTOM, expand = True)
name.pack(side = BOTTOM, expand = True)
title = Label(main, text = '''AI Traffic Sign Classifier
------------------------------------------------------------------------------''', pady = 20, font = ('comic sans', 24,'bold'))

title.configure(background = '#507af8', foreground = 'black')
title.pack()
main.mainloop()

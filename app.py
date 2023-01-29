import numpy
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from keras.models import load_model

#Loading the model
model = load_model('/home/rodean/Coding/traffic/model/CNN.h5')

# All Traffic Signs classes Names
classes = { 1:'Speed limit (20km/h)',
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
                          

def Upload_Image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded = uploaded.resize((160, 160))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        print ("Failed to Upload Image")
        pass

def show_classify_button(file_path):
    classify_b = Button(top,text="Recognise Image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='black', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.70,rely=0.45)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((40,40))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict([image])[0]
    pred = numpy.argmax(pred, axis=0)
    sign = classes[pred+1]
    label.configure(background = '#507af8', foreground='black', text = sign) 
    
   


#Tkinter application
top = tk.Tk()
top.geometry('800x600')
top.title('Traffic Sign Recognition AI')
top.configure(background='#507af8')

label = Label(top, background='black', font=('comic sans', 25,'bold'))
sign_image = Label(top)

upload = Button(top, text = "Upload Image", command = Upload_Image , padx = 10, pady = 5)
upload.configure(background = 'black', foreground = 'white', font = ('comic sans', 18,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="AI Traffic Sign Classifier", pady=20, font=('comic sans', 24,'bold'))
heading.configure(background='#507af8',foreground='black')
heading.pack()
top.mainloop()

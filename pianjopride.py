#!/usr/bin/env python
# coding: utf-8

# In[57]:


import turtle
import time


# In[58]:


#näyttö
screen = turtle.getscreen()
#näytön taustaväri
screen.bgcolor("white")
#Näytön nimi
screen.title("Seuratkaa Najsparia!")


# In[59]:


oogway = turtle.Turtle()


# In[60]:


#Määritellään kilpparin vauhti
oogway.speed('slowest')
oogway.penup()
#kilpparin muoto
oogway.shape("turtle")


# In[61]:


#Lipun korkeus ja leveys
flag_height = 650
flag_width = 475


# In[62]:


#Kilpparin aloituskohta
start_x = -237
start_y = 125


# In[63]:


#Raitojen korkeudet ja pituudet
stripe_height = flag_height/13
stripe_width = flag_width


# In[64]:


#Mihin lippu tulee ja miten neliö täytetään

def piirrä_lippu(x,y,height,width,color):
    oogway.goto(x,y)
    oogway.pendown()
    oogway.color(color)
    oogway.begin_fill()
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.end_fill()
    oogway.penup()


# In[65]:


#Tehdäänpäs sitten ne raidat

def piirrä_raidat():
    x = start_x
    y = start_y
    
    for stripe in range(0,1):
        for color in ["red", "orange", "yellow", "green", "blue"]:
            piirrä_lippu(x,y,stripe_height, stripe_width, color)
            y = y - stripe_height
            
    #Vika raita
        piirrä_lippu(x,y,stripe_height, stripe_width, "purple")
        y = y - stripe_height


# In[ ]:


#Aloitus aika
time.sleep(5)
#Piirrä raidat
piirrä_raidat()
#piilota kilppari
oogway.hideturtle()
#ikkuna auki
screen.mainloop()


# In[ ]:





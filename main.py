from turtle import heading, width
from unittest import result
import numpy as np
from PIL import Image


def decToHex(num):
    num = hex(num)
    num = num.split('x')
    num = num[1]
    return num

def colorSelection(color):
    #idea: set di colore --> prendo il colore del pixel --> calcolo la differenza tra lui e il colore(assoluta) --> se minore di quella precedete metto in memoria quella
    
    #p.s.: per farlo bisognerebbe creare una palette con del senso

    #colors: red,other red,green,other green,blue,other blue,dark blue,white,black,orange,brown,pink,light blue,celeste,grey,yellow,otheryellow,purple,
    colors = {(255,0,0),(255,51,51),(0,255,0),(51,255,51),(0,0,255),(51,51,255),(0,0,153),(255,255,255),(0,0,0),(255,138,0),(153,76,0),(255,204,204),(51,154,255),(0,255,255),(0,204,204),(160,160,160),(255,255,0),(153,51,255)}#palette stile gameboy

    minDiff = 255*3
    finalColor = color

    for c in colors:
        diff = abs(color[0] - c[0])
        diff += abs(color[1] - c[1])
        diff += abs(color[2] - c[2])
        if(diff < minDiff):
            minDiff = diff
            finalColor = c

    return finalColor

def drawSquare(pos_x,pos_y,width,height,pixelboard):
    for i in range(width):
        for j in range(height):
            pixelBoard[i+pos_x,j+pos_y] = (0,0,0)

def flatcolor(width,height,rangeDimension,pixelboard): 
    for i in range(width):
        for j in range(height):# link per lavorare sulle tuple https://note.nkmk.me/en/python-tuple-operation/
            oldValue = pixelBoard[i,j]
            oldValue = list(oldValue)
            '''
            #metodo 1
            oldValue[0] = int(oldValue[0]/rangeDimension)*rangeDimension
            oldValue[1] = int(oldValue[1]/rangeDimension)*rangeDimension
            oldValue[2] = int(oldValue[2]/rangeDimension)*rangeDimension
            '''
            '''
            #metodo 2
            #creo il valore in hex
            rValue = decToHex(oldValue[0])
            gValue = decToHex(oldValue[1])
            bValue = decToHex(oldValue[2])
            colorValue = rValue + gValue + bValue
            #print("hex value == " + colorValue)
            #calcolo il colore
            colorValue = int(colorValue,base=16)
            #print("dec value = " + str(colorValue))
            colorValue = int(colorValue/rangeDimension)*rangeDimension

            #riporto tutto a rgb
            colorValue = decToHex(colorValue)
            while(len(colorValue) < 6):
                colorValue = "0" + colorValue
            #print("after op = " + colorValue)
            oldValue[0] = int(colorValue[5] + colorValue[4],base=16)
            oldValue[1] = int(colorValue[3] + colorValue[2],base=16)
            oldValue[2] = int(colorValue[1] + colorValue[0],base=16)
            '''
            #metodo 3
            oldValue = colorSelection(oldValue)

            oldValue = tuple(oldValue)            
            pixelBoard[i,j] = oldValue
            
    

#take image
image = Image.open("/home/user/Documents/python/image_manipulation_thing/roncoloFishing.png")
#image.show() broken

#modify image
width,height = image.size
print("image size = " + str(width) + "x" + str(height))
pixelBoard = image.load() #carica l'immagine come una pixelboard
#drawSquare(0,0,100,100,pixelBoard)
flatcolor(width,height,1000,pixelBoard)

#
image.save('rf.png')
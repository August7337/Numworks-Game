from math import *
from turtle import *
from kandinsky import *
from ion import *
#320 * 240
#variable
i=0
px=125
py=175

sx=20
sy=40

Pvelocity = 10

def sq(xp,yp):
  fill_rect(xp,yp,
  sx,sy,
  color(220,120,220))  

while i==0:
    
  if keydown(KEY_RIGHT):
    fill_rect(px,py,Pvelocity,sy,color(255,255,255))
    px=px+Pvelocity
    
  if keydown(KEY_LEFT):
    fill_rect(px+sx-Pvelocity,py,Pvelocity,sy,color(255,255,255))
    px=px-Pvelocity
    
  if keydown(KEY_UP):
    fill_rect(px,py+sy-Pvelocity,sx,Pvelocity,color(255,255,255))
    py=py-Pvelocity
    
  if keydown(KEY_DOWN) and py<240-(sy*1.5-2):
    fill_rect(px,py,sx,Pvelocity,color(255,255,255))
    py=py+Pvelocity
  
  sq(px,py)

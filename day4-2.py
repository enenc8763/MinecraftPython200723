# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:44:04 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
x,y,z = mc.player.getTilePos()
for i in range(100):
    r = random.randrange(1,5)
    if r == 1:
        mc.setBlock(x,y,z,x+4,y,z,46)
    elif r ==2:
        mc.setBlocks(x,y,z,x-4,y,z,137)
    elif r ==3:
        mc.setBlocks(x,y,z,x,y,z+4,1)
    elif r == 4:
        mc.setBlocks(x,y,z,x,y,z-4,56)
        z = z-4
        
        

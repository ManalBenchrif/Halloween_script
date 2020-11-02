import pygame
import time
from pygame import mixer
from time import sleep

# to use pygame's functionality. 
pygame.init()

# create the display surface object 
window=pygame.display.set_mode((400,400))

# set the pygame window name 
pygame.display.set_caption('Halloween prank ') 

# Starting the mixer  (initialize)
mixer.init() 

# Loading the song 
mixer.music.load("witches_house.ogg")

# Start playing the song 
mixer.music.play()


sleep(2.0) #function suspends execution of the current thread for a given number of seconds.

# create a surface object, image is drawn on it. 
image=pygame.image.load("halo.jpg")

# copying the image surface object 
window.blit(image,(0,0))

# Draws the surface object to the screen.
pygame.display.update()

sleep(5.0)

mixer.init()
mixer.music.load("wlaugh.ogg")
mixer.music.play()

sleep(15.0)
mixer.music.stop()




# pygame
import pygame
from time import sleep

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.music.load("Projects/Assets/calm.mp3")   
pygame.mixer.music.play()
sleep(10)

image = pygame.image.load("Projects/Assets/ghost.jpg")
window.blit(image, (0, 0))
pygame.display.update()

pygame.mixer.music.load("Projects/Assets/scare.mp3")
pygame.mixer.music.play()
sleep(5)


# sleep(5)




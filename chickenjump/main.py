import pygame
from data.konstanta import *
from data.aset import load_aset
from ui.menu import menu_play
from core.logic import *

pygame.init()
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Chiken Jump")
jam = pygame.time.Clock()

font_kecil = pygame.font.Font("freesansbold.ttf", 16)
font_besar = pygame.font.Font("freesansbold.ttf", 22)

aset = load_aset()
state = init_game()

jalan = True
while jalan:
    jam.tick(FPS)

    if state["menu"]:
        tombol = menu_play(layar, font_besar, font_kecil)
        jalan = handle_menu_event(tombol, state)
        continue

    jalan = handle_event(state)
    update_game(state)
    draw(layar, state, aset, font_kecil, font_besar)

    pygame.display.flip()

pygame.quit()

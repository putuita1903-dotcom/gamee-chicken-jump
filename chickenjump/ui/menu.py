import pygame
from data.konstanta import *

def menu_play(layar, font_besar, font_kecil):
    layar.fill(PUTIH)

    judul = font_besar.render("CHIKEN JUMP", True, HITAM)
    play = font_besar.render("PLAY", True, PUTIH)

    tombol = pygame.Rect(130, 260, 140, 45)
    pygame.draw.rect(layar, HITAM, tombol, border_radius=10)

    layar.blit(judul, (LEBAR//2 - judul.get_width()//2, 180))
    layar.blit(
        play,
        (tombol.centerx - play.get_width()//2,
         tombol.centery - play.get_height()//2)
    )

    info = font_kecil.render("Klik PLAY / SPACE", True, HITAM)
    layar.blit(info, (LEBAR//2 - info.get_width()//2, 320))

    pygame.display.flip()
    return tombol

import pygame

def cek_tabrakan(state):
    rect_pemain = pygame.Rect(
        state["x"] + 20,
        state["y"] + 40,
        25,
        5
    )

    for p in state["platforms"][:]:
        rect_platform = pygame.Rect(p[0], p[1], p[2], p[3])

        if rect_platform.colliderect(rect_pemain) and state["dy"] > 0:
            if state["skor"] >= 350 and not p[5]:
                state["platforms"].remove(p)
            return True
    return False

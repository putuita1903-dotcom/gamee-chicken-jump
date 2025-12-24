import pygame
from data.konstanta import *
from core.pemain import cek_tabrakan
from core.platfrom import init_platform, platform_acak, gerak_platform

def init_game():
    return {
        "menu": True,

        "x": 170,
        "y": 400,
        "dx": 0,
        "dy": 0,

        "air": 2,
        "nyawa": 3,
        "skor": 0,
        "high": 0,

        "game_over": False,

        "double": False,
        "double_mulai": 0,
        "double_trigger": -1,

        "air_trigger": -1,

        "platforms": init_platform(),
        "flip": False
    }

def handle_menu_event(tombol, state):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            return False
        if e.type == pygame.MOUSEBUTTONDOWN and tombol.collidepoint(e.pos):
            state["menu"] = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            state["menu"] = False
    return True

def handle_event(state):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            return False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if state["game_over"]:
                    state.update(init_game())
                elif state["air"] > 0:
                    state["air"] -= 1
                    state["dy"] = -15

            if e.key == pygame.K_a:
                state["dx"] = -3
                state["flip"] = True
            if e.key == pygame.K_d:
                state["dx"] = 3
                state["flip"] = False

        if e.type == pygame.KEYUP:
            if e.key in (pygame.K_a, pygame.K_d):
                state["dx"] = 0

    return True

def update_game(state):
    if state["game_over"]:
        return

    state["x"] += state["dx"]
    state["y"] += state["dy"]
    state["dy"] += 0.4

    state["x"] = max(0, min(state["x"], LEBAR - 50))

    if cek_tabrakan(state):
        state["dy"] = -10

    if state["y"] < 250 and state["dy"] < 0:
        for p in state["platforms"]:
            p[1] -= state["dy"]

        tertinggi = min(p[1] for p in state["platforms"])
        if tertinggi > -JARAK_PLATFORM:
            state["platforms"].append(
                platform_acak(tertinggi - JARAK_PLATFORM)
            )
            state["skor"] += 2 if state["double"] else 1

    gerak_platform(state["platforms"], state["skor"])
    bonus(state)

    if state["y"] > 440:
        state["nyawa"] -= 1
        if state["nyawa"] > 0:
            state["x"], state["y"], state["dy"] = 170, 400, 0
            state["platforms"] = init_platform()
        else:
            state["game_over"] = True

    state["high"] = max(state["high"], state["skor"])

def bonus(state):
    if state["skor"] > 0 and state["skor"] % INTERVAL_DOUBLE == 0:
        if state["skor"] != state["double_trigger"]:
            state["double"] = True
            state["double_mulai"] = pygame.time.get_ticks()
            state["double_trigger"] = state["skor"]

    if state["double"] and pygame.time.get_ticks() - state["double_mulai"] > DURASI_DOUBLE:
        state["double"] = False

    if state["skor"] > 0 and state["skor"] % 50 == 0:
        if state["skor"] != state["air_trigger"]:
            state["air"] += 1
            state["air_trigger"] = state["skor"]

def draw(layar, state, aset, font_kecil, font_besar):
    if state["skor"] < 150:
        layar.blit(aset["bg_desa"], (0,0))
    elif state["skor"] < 350:
        layar.blit(aset["bg_langit"], (0,0))
    else:
        layar.blit(aset["bg_angkasa"], (0,0))

    img = aset["player"]
    if state["flip"]:
        img = pygame.transform.flip(img, True, False)
    layar.blit(img, (state["x"], state["y"]))

    for p in state["platforms"]:
        if state["skor"] < 150:
            layar.blit(aset["platform_tanah"], (p[0], p[1]))
        elif state["skor"] < 350:
            layar.blit(aset["platform_awan"], (p[0], p[1]))
        else:
            layar.blit(aset["platform_kapal"], (p[0], p[1]))

    layar.blit(font_kecil.render(f"Skor: {state['skor']}", True, HITAM), (280,30))
    layar.blit(font_kecil.render(f"High: {state['high']}", True, HITAM), (280,10))
    layar.blit(font_kecil.render(f"Air Jump: {state['air']}", True, HITAM), (10,30))
    layar.blit(font_kecil.render(f"Nyawa: {state['nyawa']}", True, HITAM), (10,10))

    if state["double"]:
        layar.blit(font_besar.render("DOUBLE SCORE!", True, HITAM), (90,80))

    if state["game_over"]:
        layar.blit(font_besar.render("GAME OVER - SPACE", True, HITAM), (60,120))

import pygame

def load_aset():
    aset = {}

    aset["player"] = pygame.transform.scale(
        pygame.image.load("asset/chicken.png"), (50, 50)
    )

    aset["bg_desa"] = pygame.image.load("asset/vilage.png")
    aset["bg_langit"] = pygame.image.load("asset/sky.png")
    aset["bg_angkasa"] = pygame.image.load("asset/univer.png")

    aset["platform_tanah"] = pygame.transform.scale(
        pygame.image.load("asset/dirt.png"), (70, 10)
    )
    aset["platform_awan"] = pygame.transform.scale(
        pygame.image.load("asset/cloud.png"), (70, 10)
    )
    aset["platform_kapal"] = pygame.transform.scale(
        pygame.image.load("asset/kapal.png"), (70, 10)
    )

    return aset

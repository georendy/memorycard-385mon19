
### bagian hubugnkan modul
import pygame
pygame.init() #menyalakan semua fitur pygame

### bagian variabel global
lebar_scene = 400
tinggi_scene = 400
judul_scene = "LABIRIN LABIRON LABIREN"
gambar_background = "background.jpg"
gambar_pemain = "hero.png"
gambar_musuh = "cyborg.png"
gambar_harta = "treasure.png"
musik_background = "jungles.ogg"
musik_ketabrak = "kick.ogg"
musik_harta = "money.ogg"
GAME_RUN = True #untuk boolean game nyala

### bagian pembuatan scene dan fps
scene = pygame.display.set_mode((lebar_scene, tinggi_scene))
scene.fill((0,0,0))
pygame.display.set_caption(judul_scene)
fps = pygame.time.Clock()
## gambar latarnya
latar_belakang = pygame.transform.scale(
    pygame.image.load(gambar_background),
    (lebar_scene, tinggi_scene))

### bagian pembuatan musik
pygame.mixer.init() #nyalakan fitur mixer
pygame.mixer.music.load(musik_background)
pygame.mixer.music.set_volume(0.5) #dalam persen
pygame.mixer.music.play()

### bagian pembuatan tulisan

### bagian pembuatan kelas
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, gambar, x, y, lebar, tinggi, kecepatan):
        super().__init__()
        self.lebar = lebar
        self.tinggi = tinggi
        self.gambar = pygame.transform.scale(
            pygame.image.load(gambar),
            (self.lebar, self.tinggi))
        self.rect = self.gambar.get_rect()
        self.rect.x = x #posisi X
        self.rect.y = y #posisi Y
        self.kecepatan = kecepatan
    def reset(self):
        scene.blit(self.gambar, (self.rect.x, self.rect.y))

### bagian pembuatan sprite
pemain = GameSprite(gambar=gambar_pemain, x=20, y=20,
                    lebar=50, tinggi=50, kecepatan=10)
musuh = GameSprite(gambar=gambar_musuh, x=120, y=20,
                    lebar=50, tinggi=50, kecepatan=10)
harta = GameSprite(gambar=gambar_harta, x=120, y=200,
                    lebar=50, tinggi=50, kecepatan=0)

### bagian pembuatan game loop
while GAME_RUN:
    ### bagian event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUN = False #game akan berhenti

    ## bagian tampilannya
    scene.blit(latar_belakang, (0,0))
    pemain.reset()
    musuh.reset()
    harta.reset()

    ### bagian sangat penting (dan selalu di paling bawah)
    fps.tick(60)
    pygame.display.update()
























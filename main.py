import pygame
from tkinter import simpledialog
pygame.init()
#Cores
branco = (255,255,255)
preto = (0,0,0)
#Variáveis
running = True
#Tela e som
tamanhoTela = (1800,1000)
espaco = pygame.image.load("espaco1.jpg")
tela = pygame.display.set_mode( tamanhoTela)
icone = pygame.image.load("iconeNave.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Space Marker")
pygame.mixer.music.load("somEspaco.wav")
pygame.mixer.music.play(-1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            posicao = pygame.mouse.get_pos()
            #Caixa de pergunta sobre o nome da estrela !
            caixadepergunta = simpledialog.askstring("Space", "Digite o nome da estrela")
            print(caixadepergunta)

    tela.blit( espaco, (0, 0) )
    pygame.display.update()
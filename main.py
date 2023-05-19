import pygame
from tkinter import simpledialog
pygame.init()
#Cores
branco = (255,255,255)
preto = (0,0,0)
#Variáveis
running = True
estrelas = {}

#Tela e som
tamanhoTela = (1800,1000)
espaco = pygame.image.load("espaco1.jpg")
tela = pygame.display.set_mode( tamanhoTela)
icone = pygame.image.load("iconeNave.png")
#Texto das opções
textoX = 20
textoYF10 = 20
textoYF11 = 50
textoYF12 = 80
texto = pygame.font.Font(None, 38)
renderdotextoF10 = texto.render("Pressione F10 para salvar os pontos!", True, branco)
renderdotextoF11 = texto.render("Pressione F11 para Carregar os pontos!", True, branco)
renderdotextoF12 = texto.render("Pressione F12 para Deletar os pontos!", True, branco)
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

            posicao = str(pygame.mouse.get_pos())
            nomeEstrela = simpledialog.askstring("Space", "Digite o nome da estrela")
            if nomeEstrela == "":
                nomeEstrela = "Desconhecido"

            with open("posicaoEstrelas.txt", "a") as arquivo:
                arquivo.write(nomeEstrela + ": " + posicao + "\n")
            
            if nomeEstrela == None:
                nomeEstrela = "Desconhecido"
            
            

    tela.blit( espaco, (0, 0) )
    tela.blit(renderdotextoF10, (textoX, textoYF10))
    tela.blit(renderdotextoF11, (textoX, textoYF11))
    tela.blit(renderdotextoF12, (textoX, textoYF12))

    pygame.display.update()
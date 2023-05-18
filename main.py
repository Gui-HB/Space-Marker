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
#Texto das opções
textoX = 200
textoYF10 = 100
textoYF11 = 135
textoYF12 = 170
texto = pygame.font.Font(None, 38)
renderdotextoF10 = texto.render("Pressione F10 para salvar os pontos", True, branco)
renderdotextoF11 = texto.render("Pressione F11 para Carregar os pontos", True, branco)
renderdotextoF12 = texto.render("Pressione F12 para Deletar os pontos", True, branco)
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
            #if caixadepergunta == None:
                #caixadepergunta = "Desconhecido"+str(posicao)
            #estrelas[caixadepergunta] = posicao

    tela.blit( espaco, (0, 0) )
    tela.blit(renderdotextoF10, (textoX, textoYF10))
    tela.blit(renderdotextoF11, (textoX, textoYF11))
    tela.blit(renderdotextoF12, (textoX, textoYF12))

    pygame.display.update()
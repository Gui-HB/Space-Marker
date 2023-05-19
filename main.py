import pygame
import ast
from tkinter import simpledialog,messagebox

pygame.init()
# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
# Variáveis
running = True
estrelas = []
x = 0
y = 0
# Tela e som
try:
    tamanhoTela = (1800, 1000)
    espaco = pygame.image.load("espaco1.jpg")
    tela = pygame.display.set_mode(tamanhoTela)
    icone = pygame.image.load("iconeNave.png")
    pygame.display.set_icon(icone)
    pygame.display.set_caption("Space Marker")
    pygame.mixer.music.load("somEspaco.wav")
    pygame.mixer.music.play(-1)
except:
    messagebox.showerror("Erro!","Arquivos de inicialização do jogo não foram carregados corretamente!")
    pygame.quit()
    

# Texto das opções
textoX = 20
textoYF10 = 20
textoYF11 = 50
textoYF12 = 80
texto = pygame.font.Font(None, 38)
renderdotextoF10 = texto.render("Pressione F10 para salvar os pontos!", True, branco)
renderdotextoF11 = texto.render("Pressione F11 para Carregar os pontos!", True, branco)
renderdotextoF12 = texto.render("Pressione F12 para Deletar os pontos!", True, branco)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT or event.type == 1:

            posicao = (pygame.mouse.get_pos())
            x, y = posicao
            nomeEstrela = simpledialog.askstring("Space", "Digite o nome da estrela")
            if nomeEstrela == "" or nomeEstrela== None:
                nomeEstrela = "Desconhecido"

            with open("nomePosicao.txt", "a") as nomePosicao:
                nomePosicao.write(str(nomeEstrela) + " : " + str(posicao)+"\n")
            with open("posicoes.txt", "a") as posicoes:
                posicoes.write(str(posicao)+"\n")
            pygame.draw.circle(espaco,branco,(x,y),5)


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            with open("posicoes.txt", "r") as posicoes:
                for posicao in posicoes:
                    x, y = ast.literal_eval(posicao)
                    pygame.draw.circle(espaco,branco,(x,y),5)
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            with open("posicoes.txt", "w") as posicoes:
                posicoes.write = ""
            with open("nomePosicao.txt", "w") as nomePosicao:
                nomePosicao.write = ""
            tela.fill((0,0,0))
                


    

    tela.blit( espaco, (0, 0) )
    tela.blit(renderdotextoF10, (textoX, textoYF10))
    tela.blit(renderdotextoF11, (textoX, textoYF11))
    tela.blit(renderdotextoF12, (textoX, textoYF12))


    pygame.display.update()
pygame.quit()
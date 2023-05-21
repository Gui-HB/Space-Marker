import pygame, ast, time
from tkinter import simpledialog,messagebox

pygame.init()
# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
# Variáveis
running = True
estrelas = {}
primeiroClique = True


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
fonte_nome_estrela = pygame.font.Font(None, 24)
renderdotextoF10 = texto.render("Pressione F10 para salvar os pontos!", True, branco)
renderdotextoF11 = texto.render("Pressione F11 para Carregar os pontos!", True, branco)
renderdotextoF12 = texto.render("Pressione F12 para Deletar os pontos!", True, branco)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT or event.type == 1:
            posicao = (pygame.mouse.get_pos())
            if primeiroClique == True:
                x, y = posicao
                pygame.draw.circle(espaco,branco,(x,y),5)
                primeiroClique = False
                nomeEstrela = simpledialog.askstring("Space", "Digite o nome da estrela")
                if nomeEstrela == "" or nomeEstrela == None:
                    nomeEstrela = "Desconhecido"
                estrelas[nomeEstrela] = posicao
                with open("nomePosicao.txt", "a") as nomePosicao:
                    nomePosicao.write(str(nomeEstrela) + " : " + str(posicao)+"\n")
                with open("posicoes.txt", "a") as posicoes:
                    posicoes.write(str(posicao)+"\n")
                    pygame.draw.circle(espaco,branco,(x,y),5) 
            else:
                a, b = posicao
                pygame.draw.line(espaco,branco,(x,y),(a,b),1)
                x, y = posicao
                nomeEstrela = simpledialog.askstring("Space", "Digite o nome da estrela")
                if nomeEstrela == "" or nomeEstrela == None:
                    nomeEstrela = "Desconhecido"
                estrelas[nomeEstrela] = posicao
                with open("nomePosicao.txt", "a") as nomePosicao:
                    nomePosicao.write(str(nomeEstrela) + " : " + str(posicao)+"\n")
                with open("posicoes.txt", "a") as posicoes:
                    posicoes.write(str(posicao)+"\n")
                    pygame.draw.circle(espaco,branco,(x,y),5)                


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            with open("posicoes.txt", "r") as posicoes:
                iter_posicoes = iter(posicoes)
                primeiro_ponto = True
                ponto_anterior = None
                
                for posicao in iter_posicoes:
                    x, y = ast.literal_eval(posicao)
                    pygame.draw.circle(espaco, branco, (x, y), 5)
                    
                    if primeiro_ponto:
                        primeiro_ponto = False
                    else:
                        pygame.draw.line(espaco, branco, ponto_anterior, (x, y))
                    
                    ponto_anterior = (x, y)
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            with open("posicoes.txt", "w") as posicoes:
                posicoes.write = ""
            with open("nomePosicao.txt", "w") as nomePosicao:
                nomePosicao.write = ""
    

    tela.blit( espaco, (0, 0) )
    tela.blit(renderdotextoF10, (textoX, textoYF10))
    tela.blit(renderdotextoF11, (textoX, textoYF11))
    tela.blit(renderdotextoF12, (textoX, textoYF12))

    for nome, posicao in estrelas.items():
        nome_surface = fonte_nome_estrela.render(nome, True, branco)
        tela.blit(nome_surface, posicao)

    pygame.display.update()
pygame.quit()
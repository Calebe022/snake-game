import pygame
import random

pygame.init()

LARGURA, ALTURA = 600, 400
TAMANHO = 20
VELOCIDADE = 10

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake Game")

PRETO = (30, 30, 30)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
BRANCO = (255, 255, 255)

fonte = pygame.font.Font(None, 36)

def desenhar_botao(texto, x, y, largura, altura, cor, cor_texto):
    pygame.draw.rect(tela, cor, (x, y, largura, altura), border_radius=10)
    texto_render = fonte.render(texto, True, cor_texto)
    tela.blit(texto_render, (x + 15, y + 10))
    return pygame.Rect(x, y, largura, altura)

def tela_inicial():
    rodando = True
    while rodando:
        tela.fill(PRETO)
        titulo = fonte.render("SNAKE GAME", True, BRANCO)
        tela.blit(titulo, (LARGURA // 3, ALTURA // 4))

        botao_jogar = desenhar_botao("JOGAR", LARGURA // 3, ALTURA // 2, 150, 50, VERDE, BRANCO)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.collidepoint(evento.pos):
                    rodando = False
                    
def tela_game_over(pontuacao):
    rodando = True
    while rodando:
        tela.fill(PRETO)
        texto = fonte.render(f"Game Over! Pontuação: {pontuacao}", True, BRANCO)
        tela.blit(texto, (LARGURA // 4, ALTURA // 3))

        botao_reiniciar = desenhar_botao("REINICIAR", LARGURA // 3, ALTURA // 2, 150, 50, VERMELHO, BRANCO)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_reiniciar.collidepoint(evento.pos):
                    return 

def jogo():
    
    x, y = LARGURA // 2, ALTURA // 2
    velocidade_x, velocidade_y = 0, 0
    corpo = [(x, y)]

    comida_x = random.randint(0, (LARGURA - TAMANHO) // TAMANHO) * TAMANHO
    comida_y = random.randint(0, (ALTURA - TAMANHO) // TAMANHO) * TAMANHO

    rodando = True
    clock = pygame.time.Clock()
    pontuacao = 0

    while rodando:
        tela.fill(PRETO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and velocidade_x == 0:
                    velocidade_x = -TAMANHO
                    velocidade_y = 0
                elif evento.key == pygame.K_RIGHT and velocidade_x == 0:
                    velocidade_x = TAMANHO
                    velocidade_y = 0
                elif evento.key == pygame.K_UP and velocidade_y == 0:
                    velocidade_y = -TAMANHO
                    velocidade_x = 0
                elif evento.key == pygame.K_DOWN and velocidade_y == 0:
                    velocidade_y = TAMANHO
                    velocidade_x = 0
                    
        x += velocidade_x
        y += velocidade_y
        corpo.insert(0, (x, y))

        if x == comida_x and y == comida_y:
            comida_x = random.randint(0, (LARGURA - TAMANHO) // TAMANHO) * TAMANHO
            comida_y = random.randint(0, (ALTURA - TAMANHO) // TAMANHO) * TAMANHO
            pontuacao += 10 
        else:
            corpo.pop()

        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA or (x, y) in corpo[1:]:
            tela_game_over(pontuacao)
            return

        pygame.draw.rect(tela, VERMELHO, (comida_x, comida_y, TAMANHO, TAMANHO))

        for parte in corpo:
            pygame.draw.rect(tela, VERDE, (*parte, TAMANHO, TAMANHO), border_radius=5)

        texto_pontos = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))

        pygame.display.update()
        clock.tick(VELOCIDADE)

while True:
    tela_inicial()
    jogo()

import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 600, 400
TAMANHO = 20
VELOCIDADE = 10

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake Game")

# Definição de cores
PRETO = (30, 30, 30)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
BRANCO = (255, 255, 255)

# Fonte para textos
fonte = pygame.font.Font(None, 36)

# Função para desenhar botões
def desenhar_botao(texto, x, y, largura, altura, cor, cor_texto):
    pygame.draw.rect(tela, cor, (x, y, largura, altura), border_radius=10)
    texto_render = fonte.render(texto, True, cor_texto)
    tela.blit(texto_render, (x + 15, y + 10))
    return pygame.Rect(x, y, largura, altura)

# Função para a tela inicial
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

# Função para a tela de game over
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
                    return  # Reinicia o jogo

# Função principal do jogo
def jogo():
    # Posição inicial da cobra
    x, y = LARGURA // 2, ALTURA // 2
    velocidade_x, velocidade_y = 0, 0
    corpo = [(x, y)]

    # Geração inicial da comida
    comida_x = random.randint(0, (LARGURA - TAMANHO) // TAMANHO) * TAMANHO
    comida_y = random.randint(0, (ALTURA - TAMANHO) // TAMANHO) * TAMANHO

    rodando = True
    clock = pygame.time.Clock()
    pontuacao = 0

    while rodando:
        tela.fill(PRETO)

        # Captura eventos
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

        # Movimentação da cobra
        x += velocidade_x
        y += velocidade_y
        corpo.insert(0, (x, y))

        # Verifica se comeu a comida
        if x == comida_x and y == comida_y:
            comida_x = random.randint(0, (LARGURA - TAMANHO) // TAMANHO) * TAMANHO
            comida_y = random.randint(0, (ALTURA - TAMANHO) // TAMANHO) * TAMANHO
            pontuacao += 10  # Aumenta a pontuação
        else:
            corpo.pop()

        # Verifica colisões (parede ou corpo)
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA or (x, y) in corpo[1:]:
            tela_game_over(pontuacao)
            return  # Sai do jogo para recomeçar

        # Desenha comida
        pygame.draw.rect(tela, VERMELHO, (comida_x, comida_y, TAMANHO, TAMANHO))

        # Desenha a cobra
        for parte in corpo:
            pygame.draw.rect(tela, VERDE, (*parte, TAMANHO, TAMANHO), border_radius=5)

        # Exibe pontuação
        texto_pontos = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))

        pygame.display.update()
        clock.tick(VELOCIDADE)

# Executa o jogo com tela inicial
while True:
    tela_inicial()
    jogo()
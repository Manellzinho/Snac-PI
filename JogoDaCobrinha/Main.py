import pygame,sys,random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load('Imagens/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Imagens/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Imagens/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Imagens/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Imagens/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Imagens/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Imagens/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Imagens/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Imagens/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Imagens/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Imagens/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Imagens/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Imagens/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Imagens/body_bl.png').convert_alpha()

        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    def draw_snake(self):
        '''for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen,(183, 111, 122), block_rect)'''

        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0] #Descobrindo a posição que a cabeça deve olhar, subtração de vetores
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1] #Msm coisa da cabeça, mas usando o último e o penultimo vetor
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]  # copia o corpo da cobra -1 bloco final
            body_copy.insert(0, body_copy[0] + self.direction)  # insere a cabeça da cobra na posição 0 do array, e na posição do antigo body[0] + direction
            self.body = body_copy[:]  # retorna a alteração pra self.body
            self.new_block = False
        else:
            body_copy = self.body[:-1]  # copia o corpo da cobra -1 bloco final
            body_copy.insert(0, body_copy[
                0] + self.direction)  # insere a cabeça da cobra na posição 0 do array, e na posição do antigo body[0] + direction
            self.body = body_copy[:]  # retorna a alteração pra self.body

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect(screen, (126,166,114),fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self): #Não é necessariamente uma colisão, mas uma sobreposição de coordenadas
        if self.fruit.pos == self.snake.body[0]: #Checa se a cabeça da cobra está sobreponto a posição da fruta
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number: # Nossa grid tem _cell_number_ células, esse if checa se acabeça da cobra está entre 0 e número máximo de celulas do grid
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                print('Game over by self collision')
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        '''Vamos desenhar uma célula mais escura nas linhas pares, nas colunas pares
        E nas linhas ímpares, nas colunas impares'''
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3) # o score vai ser dado a partir do tamanho da cobra
        score_surface = game_font.render(score_text, True, (56,74,12)) #Parametros do renderer(O que vai ser renderizdo, antialiasing,color)
        score_x = int(cell_number*cell_size - 60) #posicionamento do score
        score_y = int(cell_number*cell_size - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y)) # criação do rectangle onde o score vai ser posicionado
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)

        pygame.draw.rect(screen,(167,209,61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen, (56,74,12), bg_rect, 2)  # ultimo parametro é o width do outline

pygame.mixer.pre_init(44100, -16,2,512) #parâmetro mais técnico sobre som, faz com que não tenha delay no som

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size)) # criando um "falso" grid
clock = pygame.time.Clock() #Variável para padronizar o desempenho do jogo em diferentes computadores
apple = pygame.image.load('Imagens/apple_logo2.2.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT # criamos um evento personalizado
pygame.time.set_timer(SCREEN_UPDATE, 150) #Esse evento vai ser chamada a cada 150 milissegundos

main_game = MAIN()

while True: # local onde construiremos todos os elementos do jogo
    for event in pygame.event.get(): # laço que procura em todos os eventos possíveis, se o evento pygame.QUIT foi chamado(fechar a janela no x)
        if event.type == pygame.QUIT:
            pygame.quit() # oposto de pygame.init()
            sys.exit() #encerra qualquer código que esteja rodando
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN: # evento que identifica se alguma tecla foi pressionada, e troca a direção do vetor direction de acordo
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1: #A cobra não pode se mover na direção oposta a direção anterior
                    main_game.snake.direction = Vector2(0, -1) # lembrando que o eixo y é invertido aqui
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)


    screen.fill((175,215,70)) # código RGB 0 - 255
    main_game.draw_elements()
    #screen.blit(test_surface,test_rect) # A função blit "desenha" a superficie teste_surface em cima de screen, na posição(x,y)
    pygame.display.update()
    clock.tick(60) #Define o framerate do while, ou seja, caso o clock.tick(60), o while vai rodar apenas 60 vezes por segundo
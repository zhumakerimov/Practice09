import pygame
import sys
from ball import Ball

def main():
    pygame.init()
    
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    ball_radius = 25
    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    
    ball = Ball(ball_x, ball_y, ball_radius, RED)
    
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move(0, -20, SCREEN_WIDTH, SCREEN_HEIGHT)
                elif event.key == pygame.K_DOWN:
                    ball.move(0, 20, SCREEN_WIDTH, SCREEN_HEIGHT)
                elif event.key == pygame.K_LEFT:
                    ball.move(-20, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
                elif event.key == pygame.K_RIGHT:
                    ball.move(20, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        
        screen.fill(WHITE)
        ball.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
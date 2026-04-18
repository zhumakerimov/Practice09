import pygame
import sys
import os
from clock import MickeyClock

def main():
    pygame.init()
    
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mickey's Clock")
    
    WHITE = (255, 255, 255)
    
    hand_path = "images/mickey_hand.png"
    
    if not os.path.exists(hand_path):
        os.makedirs("images", exist_ok=True)
        temp = pygame.Surface((20, 200), pygame.SRCALPHA)
        pygame.draw.rect(temp, (0, 0, 0), (8, 0, 4, 200))
        pygame.draw.circle(temp, (0, 0, 0), (10, 20), 8)
        pygame.image.save(temp, hand_path)
        print("Created hand image")
    
    mickey_clock = MickeyClock(screen, hand_path)
    
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2
    
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        mickey_clock.draw(center_x, center_y)
        pygame.display.flip()
        clock.tick(1)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
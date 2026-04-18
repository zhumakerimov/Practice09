import pygame
import sys
import os
from player import MusicPlayer

def main():
    pygame.init()
    pygame.mixer.init()
    
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Music Player")
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (100, 100, 255)
    
    font_title = pygame.font.Font(None, 36)
    font_info = pygame.font.Font(None, 28)
    
    music_dir = os.path.join(os.path.dirname(__file__), "music")
    player = MusicPlayer(music_dir)
    player.load_tracks()
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.previous_track()
                elif event.key == pygame.K_q:
                    running = False

        title = font_title.render("MUSIC PLAYER", True, BLUE)
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 20))
        
        track = font_info.render(f"Now Playing: {player.get_current_track_name()}", True, BLACK)
        screen.blit(track, (50, 100))
        
        status = font_info.render(f"Status: {player.get_status()}", True, GREEN if player.get_status() == "Playing" else BLACK)
        screen.blit(status, (50, 150))
        
        controls = font_info.render("P=Play S=Stop N=Next B=Previous Q=Quit", True, BLACK)
        screen.blit(controls, (50, SCREEN_HEIGHT - 50))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
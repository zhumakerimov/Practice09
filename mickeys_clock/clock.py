import pygame
import math
from datetime import datetime

class MickeyClock:
    def __init__(self, screen, hand_image_path):
        self.screen = screen
        original = pygame.image.load(hand_image_path)
        self.minute_hand = pygame.transform.scale(original, (15, 150))
        self.second_hand = pygame.transform.scale(original, (10, 180))
        self.font = pygame.font.Font(None, 48)
        
    def get_angles(self):
        now = datetime.now()
        minutes = now.minute
        seconds = now.second
        
        minute_angle = minutes * 6
        second_angle = seconds * 6
        
        return minute_angle, second_angle
    
    def rotate_hand(self, image, angle, center):
        rotated_image = pygame.transform.rotate(image, -angle)
        new_rect = rotated_image.get_rect(center=center)
        return rotated_image, new_rect
    
    def draw_clock_face(self, center_x, center_y):
        pygame.draw.circle(self.screen, (0, 0, 0), (center_x, center_y), 250, 3)
        
        for hour in range(1, 13):
            angle = math.radians(90 - hour * 30)
            x = center_x + 210 * math.cos(angle)
            y = center_y - 210 * math.sin(angle)
            
            text = self.font.render(str(hour), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x, y))
            self.screen.blit(text, text_rect)
    
    def draw(self, center_x, center_y):
        self.draw_clock_face(center_x, center_y)
        
        minute_angle, second_angle = self.get_angles()
        
        minute_hand, minute_rect = self.rotate_hand(
            self.minute_hand, minute_angle, (center_x, center_y)
        )
        
        second_hand, second_rect = self.rotate_hand(
            self.second_hand, second_angle, (center_x, center_y)
        )
        
        self.screen.blit(minute_hand, minute_rect)
        self.screen.blit(second_hand, second_rect)
import pygame
import os

pygame.init()

os.makedirs("mickeys_clock/images", exist_ok=True)

surface = pygame.Surface((30, 200), pygame.SRCALPHA)

pygame.draw.ellipse(surface, (0, 0, 0), (5, 0, 20, 200))

pygame.draw.circle(surface, (0, 0, 0), (15, 25), 12)
pygame.draw.circle(surface, (255, 255, 255), (10, 20), 4)
pygame.draw.circle(surface, (255, 255, 255), (20, 20), 4)

pygame.image.save(surface, "mickeys_clock/images/mickey_hand.png")
print("Created mickey_hand.png")
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the window
window_size = (640, 480)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame Window with Text')

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load fonts
font1 = pygame.font.SysFont('Arial', 48)  # You can replace with another system font
font2 = pygame.font.SysFont('Courier New', 36)  # Another example font

# Text to display
text1 = font1.render('Welcome to Pygame!', True, BLACK)  # (Text, Anti-aliasing, Color)
text2 = font2.render('Using multiple fonts!', True, BLACK)

# Positioning the text
text1_rect = text1.get_rect(center=(window_size[0]//2, window_size[1]//2 - 50))
text2_rect = text2.get_rect(center=(window_size[0]//2, window_size[1]//2 + 50))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the background with white
    window.fill(WHITE)
    
    # Draw text
    window.blit(text1, text1_rect)
    window.blit(text2, text2_rect)
    
    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()


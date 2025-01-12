import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet

def main():
    print("Starting asteroids!")
    pygame.init()
    pygame.font.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Asteroids')
    clock = pygame.time.Clock()
    
    score = 0
    font = pygame.font.Font(None, 64)
    
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Bullet.containers = (bullets, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        for object in updatable:
            object.update(dt) 
        
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over!")
                pygame.quit()
                quit()
            for bullet in bullets:
                if bullet.is_colliding(asteroid):
                    asteroid.split()
                    bullet.kill()
                    score += 1
            
        screen.fill("black")
        text = font.render(f"Current Score: {score}", True, "white")
        text_pos = text.get_rect(centerx=SCREEN_WIDTH // 2, centery=50)
        screen.blit(text, text_pos)
            
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
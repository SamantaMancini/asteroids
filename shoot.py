from circleshape import CircleShape
import pygame

SHOT_RADIUS = 5

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), SHOT_RADIUS, 2)

    def update(self, time_delta):
        # Update position based on velocity
        self.position.x += self.velocity.x * time_delta
        self.position.y += self.velocity.y * time_delta
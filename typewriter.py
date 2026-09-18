import pygame

class Typewriter: 
    def __init__(self, text):
        self.text = text
        self.font = pygame.font.SysFont("Courier New", 18)
        self.speed = 30
        self.displayed_characters = 0
        self.last_update = pygame.time.get_ticks()

    def update(self): 
        now = pygame.time.get_ticks()
        if self.displayed_characters < len(self.text) and now - self.last_update > self.speed: 
            self.displayed_characters += 1
            self.last_update = now

    def draw(self, window, position): 
        surface = self.font.render(self.text[:self.displayed_characters], True, (255,255,255))
        window.blit(surface,position)

    def complete(self): 
        return self.displayed_characters >= len(self.text)

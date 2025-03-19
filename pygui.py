import pygame
import time

class Button:
    def __init__(self, pos, width, height, text, background_color="#6c6", color="#fff", hover_background_color="#5b5", hover_color="#ccc", font='Arial', font_size=16, function=lambda _: ..., args=None, sleep=0.1):
        pygame.init()
        pygame.font.init()
        
        self.x, self.y = pos
        self.width = width
        self.height = height
        self.text = text
        self.background_color = background_color
        self.color = color
        self.hover_background_color = hover_background_color
        self.hover_color = hover_color
        self.font_size = font_size
        self.font = font
        self.font = pygame.font.SysFont(self.font, self.font_size)
        self.text_size = self.font.size(self.text)
        self.text = self.font.render(self.text, False, self.hex_to_rgb(color))
        self.function = function
        self.args = args
        self.sleep = sleep

    def check_events(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        hover = False
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            hover = True
        return {
            'hover': hover,
            'clicked': clicked[0]
            }

    def process(self):
        self.function(self.args)
        time.sleep(self.sleep)

    def draw(self, surface):
        events = self.check_events()

        hover = events.get('hover')
        if events.get('clicked'):
            self.process()

        color = self.hex_to_rgb(self.background_color) if not hover else self.hex_to_rgb(self.hover_background_color)

        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))
        surface.blit(self.text, (self.x + self.width // 2 -  self.text_size[0] // 2, self.y + self.height // 2 - self.text_size[1] // 2))

    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        if len(value) == 3:
            value = ''.join([i * 2 for i in value])
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
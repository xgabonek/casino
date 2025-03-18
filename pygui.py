import pygame

class Button:
    def __init__(self, x, y, width, height, text, background_color="#6c6", color="#fff", hover_background_color="#ccc", hover_color="#5b5", font='Arial', font_size=16):
        pygame.init()
        pygame.font.init()
        
        self.x = x
        self.y = y
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
        self.text = self.font.render(self.text, False, self.hex_to_rgb(color))

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

    def draw(self, surface):
        pygame.draw.rect(surface, self.hex_to_rgb(self.background_color), (self.x, self.y, self.width, self.height))
        surface.blit(self.text, (self.x, self.y))

    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
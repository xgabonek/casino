import pygame
import time

def hex_to_rgb(value): # This function makes a RGB value from HEX; example: "#fff" will return (255, 255, 255) tuple
    value = value.lstrip('#')
    if len(value) == 3:
        value = ''.join([i * 2 for i in value])
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

"""
pygui.Button
Arguments:
Pos[x, y],
width,
height,
text,
optional background_color,
optional color,
optional hover_background_color,
optional hover_color,
optional font_size,
optional font_family

First you create a button:
button = pygui.Button(100, 100, 200, 50, "Click me")
than you should draw it every frame in your main loop:
button.draw(SURFACE) where surface is pygame.surface.Surface

margin stands for outer distance between sticked objects. margin[0] is for x, [1] is for y
stick_or_insert stands for parent- positioning: 0 for stick, 1 for insert
"""

class Button:
    def __init__(self, pos_or_parent, width: int, height: int, text: str, background_color: str="#6c6", color: str="#fff", hover_background_color: str="#5b5", hover_color: str="#ccc", font_family: str='segoeuiemoji', font_size: int=16, func=lambda _: ..., args: list=None, sleep: float=0.1, margin=[10, 10], stick_or_insert=None):
        pygame.init()
        pygame.font.init()
        
        if isinstance(pos_or_parent, (list, tuple)):
            pos = pos_or_parent
            self.x, self.y = pos
        else:
            parent = pos_or_parent
            if stick_or_insert is None:
                raise ValueError
            if stick_or_insert == 0:
                self.x, self.y = parent.x + parent.width + margin[0], parent.y
            else:
                self.x, self.y = parent.x + margin[0], parent.y + margin[1]

        self.width = width
        self.height = height
        self.text = text
        self.background_color = background_color
        self.color = color
        self.hover_background_color = hover_background_color
        self.hover_color = hover_color
        self.font_size = font_size
        self.font_family = font_family
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.text_size = self.font.size(self.text)
        self.text = self.font.render(self.text, True, hex_to_rgb(color))
        self.function = func
        self.args = args
        self.sleep = sleep

    def check_events(self) -> dict[bool, bool]:
        mouse = pygame.mouse.get_pos()
        clicked = False
        hover = False
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            clicked = pygame.mouse.get_pressed()[0]
            hover = True
        return {
            'hover': hover,
            'clicked': clicked
            }


    def process(self) -> None:
        self.function(self.args)
        time.sleep(self.sleep)

    def change_text(self, text) -> None:
        self.text = self.font.render(text, True, hex_to_rgb(self.color))

    def draw(self, surface: pygame.SurfaceType) -> None:
        events = self.check_events()
        hover = events.get('hover')
        if events.get('clicked'):
            self.process()

        if self.text_size[0] + 5 >= self.width:
            self.width = self.text_size[0] + 20

        color = hex_to_rgb(self.background_color) if not hover else hex_to_rgb(self.hover_background_color)

        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))
        surface.blit(self.text, (self.x + self.width // 2 -  self.text_size[0] // 2, self.y + self.height // 2 - self.text_size[1] // 2))
    
"""
The same as button but not clickable
If you want for insert image dont put text because it will not be showed and add image link or path
"""
class Label:
    def __init__(self, pos_or_parent, width: int, height: int, text: str, background_color: str="#6c6", color: str="#fff", font: str='segoeuiemoji', font_size: int=16, image: str=None, margin=[10, 10], stick_or_insert: int=None):
        pygame.init()
        pygame.font.init()
    
        if isinstance(pos_or_parent, (list, tuple)):
            pos = pos_or_parent
            self.x, self.y = pos
        else:
            parent = pos_or_parent
            if stick_or_insert is None:
                raise ValueError
            if stick_or_insert == 0:
                self.x, self.y = parent.x + parent.width + margin[0], parent.y
            else:
                self.x, self.y = parent.x + margin[0], parent.y + margin[1]

        self.width = width
        self.height = height
        self.background_color = hex_to_rgb(background_color)
        self.color = hex_to_rgb(color)
        self.font_size = font_size
        self.font = font
        self.font = pygame.font.SysFont(self.font, self.font_size)
        self.text_size = self.font.size(text)
        self.text = self.font.render(text, True, self.color)

    def change_text(self, text) -> None:
        self.text = self.font.render(text, True, self.color)

    def draw(self,surface) -> None:
        if self.text_size[0] + 5 >= self.width:
            self.width = self.text_size[0] + 20

        pygame.draw.rect(surface, self.background_color, (self.x, self.y, self.width, self.height))
        surface.blit(self.text, (self.x + self.width // 2 -  self.text_size[0] // 2, self.y + self.height // 2 - self.text_size[1] // 2))
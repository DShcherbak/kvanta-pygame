import pygame
import sys
import math
from random import randint

_screen = None           # private singleton surface
_bg     = "white"        # store so we can re-fill every frame
_clock = None
_brush = None
_pen   = None 
_pen_width = None 

def start_drawing(size=(1000, 1000), bg="white", title="Kvanta"):
    global _screen, _bg, _clock, _brush, _pen, _pen_width
    pygame.init()
    _screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    _bg = bg
    _screen.fill(pygame.Color(bg))
    _clock = pygame.time.Clock()
    _brush = (255, 255, 255)
    _pen = (0, 0, 0)
    _pen_width = 1

# ---- drawing helpers -----------------------------------------------------
def _require_screen():
    if _screen is None:
        raise RuntimeError("Call start_drawing() first")

def circle(x, y, radius):
    _require_screen()
    pygame.draw.circle(_screen, pygame.Color(_brush), (x, y), radius, 0)
    draw_circle(x, y, radius)

def draw_circle(x, y, radius):
    if _pen_width > 0:
        pygame.draw.circle(_screen, pygame.Color(_pen), (x, y), radius, _pen_width)


def rectangle(x1 : int, y1 : int, x2 : int, y2 : int):
    _require_screen()
    x = min(x1, x2)
    y = min(y1, y2)
    width = abs(x2-x1)
    height = abs(y2-y1)
    pygame.draw.rect(_screen, pygame.Color(_brush), (x, y, width, height), 0)
    draw_rectangle(x1, y1, x2, y2)

def draw_rectangle(x1 : int, y1 : int, x2 : int, y2 : int):
    if _pen_width > 0:
        x = min(x1, x2)
        y = min(y1, y2)
        width = abs(x2-x1)
        height = abs(y2-y1)
        pygame.draw.rect(_screen, pygame.Color(_pen), (x, y, width, height), _pen_width)

def arc(x, y, radius, angle_1, angle_2):
    _require_screen()
    rad_1 = math.radians(angle_1)
    rad_2 = math.radians(angle_2)
    pygame.draw.arc(_screen, pygame.Color(_pen), (x-radius, y-radius, 2*radius, 2*radius), rad_1, rad_2, _pen_width)

def clear():
    _require_screen()
    _screen.fill((255, 255, 255))

def draw_frame():
    _require_screen()
    pygame.display.flip()
    _clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def set_brush_color(color : str):
    global _brush
    _brush = color 

def set_brush_rgb(r : int, g : int, b : int):
    global _brush 
    _brush = (r, g, b)

def set_pen_color(color : str):
    global _pen
    _pen = color

def set_pen_rgb(r : int, g : int, b : int):
    global _pen 
    _pen = (r, g, b)

def set_pen_width(width : int):
    global _pen_width
    _pen_width = width

def set_pixel(x : int, y: int, color):
    _require_screen()
    _screen.set_at((x, y), pygame.Color(color))

def line(x1: int, y1: int, x2: int, y2: int):
    _require_screen()
    pygame.draw.line(_screen, pygame.Color(_pen), (x1, y1), (x2, y2), _pen_width)

def random(from_: int, to_: int) -> int:
    return randint(from_, to_)

def polygon(points):
    _require_screen()
    pygame.draw.polygon(_screen, pygame.Color(_brush), points)
    draw_polygon(points)
    
def draw_polygon(points):
    _require_screen()
    if _pen_width > 0:
        pygame.draw.polygon(_screen, pygame.Color(_pen), points, _pen_width)
    



# add more helpers as needed...

# ---- main loop -----------------------------------------------------------
def end_drawing():
    """Show the window until the user closes it."""
    _require_screen()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
import pygame
import os
import win32api
import win32con
import win32gui
from sys import exit

pygame.init()

screenWidth = pygame.display.get_desktop_sizes()[0][0]

# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (((screenWidth / 2) - 100), 20)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20, 880)

screen = None
size = []


def show():
    global size
    global screen

    string = "A-D-Y"
    imagen = pygame.image.load(".\\image\\LOGO-ADY.png")

    fuchsia = (128, 0, 255)
    dark_red = (25, 25, 25)
    textcolor = 255, 255, 255
    fontsize = 25
    size = [190, 170]

    pygame.display.set_caption('A-D-Y')
    screen = pygame.display.set_mode(size, pygame.NOFRAME)
    basicfont = pygame.font.SysFont("Consolas", fontsize)

    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 200, win32con.LWA_ALPHA)

    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) |
                           win32con.WS_EX_TOOLWINDOW)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    text = basicfont.render(string, True, textcolor, dark_red)
    textrect = text.get_rect()
    textrect.bottom = screen.get_rect().bottom
    textrect.centerx = screen.get_rect().centerx
    screen.fill(fuchsia)
    pygame.draw.rect(screen, fuchsia, textrect)
    pygame.draw.rect(screen, dark_red, pygame.Rect(0, 0, 190, 170))
    screen.blit(text, textrect)
    imagen = pygame.transform.scale(imagen, (140, 141))
    screen.blit(imagen, (25, 0))
    pygame.display.flip()


def hide():
    global screen
    screen = pygame.display.set_mode((1, 1), pygame.NOFRAME)
    pygame.display.flip()


def caps_lock(mayus):
    global size
    global screen

    string = ""
    imagen = None

    if mayus:
        string = "Caps OFF"
        imagen = pygame.image.load(".\\image\\LOGO-eNdV20.png")
    elif not mayus:
        string = "Caps ON"
        imagen = pygame.image.load(".\\image\\LOGO-ADY.png")

    fuchsia = (128, 0, 255)
    dark_red = (25, 25, 25)
    textcolor = 255, 255, 255
    fontsize = 25
    size = [190, 170]

    pygame.display.set_caption('A-D-Y Caps/Num/Scroll Lock Indicator')
    screen = pygame.display.set_mode(size, pygame.NOFRAME)
    basicfont = pygame.font.SysFont("Consolas", fontsize)

    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 200, win32con.LWA_ALPHA)

    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) |
                           win32con.WS_EX_TOOLWINDOW)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    text = basicfont.render(string, True, textcolor, dark_red)
    textrect = text.get_rect()
    textrect.bottom = screen.get_rect().bottom
    textrect.centerx = screen.get_rect().centerx
    screen.fill(fuchsia)
    pygame.draw.rect(screen, fuchsia, textrect)
    pygame.draw.rect(screen, dark_red, pygame.Rect(0, 0, 190, 170))
    screen.blit(text, textrect)
    imagen = pygame.transform.scale(imagen, (140, 141))
    screen.blit(imagen, (25, 0))
    pygame.display.flip()

    pygame.time.delay(1000)
    screen = pygame.display.set_mode((1, 1), pygame.NOFRAME)
    pygame.display.flip()


def scroll_lock(scroll):
    global size
    global screen

    string = ""
    imagen = None

    if scroll:
        string = "Scroll OFF"
        imagen = pygame.image.load(".\\image\\LOGO-eNdV20.png")
    elif not scroll:
        string = "Scroll ON"
        imagen = pygame.image.load(".\\image\\LOGO-ADY.png")

    fuchsia = (128, 0, 255)
    dark_red = (25, 25, 25)
    textcolor = 255, 255, 255
    fontsize = 25
    size = [190, 170]

    pygame.display.set_caption('A-D-Y Caps/Num/Scroll Lock Indicator')
    screen = pygame.display.set_mode(size, pygame.NOFRAME)
    basicfont = pygame.font.SysFont("Consolas", fontsize)

    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 200, win32con.LWA_ALPHA)

    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) |
                           win32con.WS_EX_TOOLWINDOW)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    text = basicfont.render(string, True, textcolor, dark_red)
    textrect = text.get_rect()
    textrect.bottom = screen.get_rect().bottom
    textrect.centerx = screen.get_rect().centerx
    screen.fill(fuchsia)
    pygame.draw.rect(screen, fuchsia, textrect)
    pygame.draw.rect(screen, dark_red, pygame.Rect(0, 0, 190, 170))
    screen.blit(text, textrect)
    imagen = pygame.transform.scale(imagen, (140, 141))
    screen.blit(imagen, (25, 0))
    pygame.display.update()

    pygame.time.delay(1000)
    screen = pygame.display.set_mode((1, 1), pygame.NOFRAME)
    pygame.display.update()


def num_lock(num):
    global size
    global screen

    string = ""
    imagen = None

    if num:
        string = "Num OFF"
        imagen = pygame.image.load(".\\image\\LOGO-eNdV20.png")
    elif not num:
        string = "Num ON"
        imagen = pygame.image.load(".\\image\\LOGO-ADY.png")

    fuchsia = (128, 0, 255)
    dark_red = (25, 25, 25)
    textcolor = 255, 255, 255
    fontsize = 25
    size = [190, 170]

    pygame.display.set_caption('A-D-Y Caps/Num/Scroll Lock Indicator')
    screen = pygame.display.set_mode(size, pygame.NOFRAME)
    basicfont = pygame.font.SysFont("Consolas", fontsize)

    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 200, win32con.LWA_ALPHA)

    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) |
                           win32con.WS_EX_TOOLWINDOW)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    text = basicfont.render(string, True, textcolor, dark_red)
    textrect = text.get_rect()
    textrect.bottom = screen.get_rect().bottom
    textrect.centerx = screen.get_rect().centerx
    screen.fill(fuchsia)
    pygame.draw.rect(screen, fuchsia, textrect)
    pygame.draw.rect(screen, dark_red, pygame.Rect(0, 0, 190, 170))
    screen.blit(text, textrect)
    imagen = pygame.transform.scale(imagen, (140, 141))
    screen.blit(imagen, (25, 0))
    pygame.display.update()

    pygame.time.delay(1000)
    screen = pygame.display.set_mode((1, 1), pygame.NOFRAME)
    pygame.display.update()


def end():
    pygame.display.quit()
    pygame.quit()
    exit()

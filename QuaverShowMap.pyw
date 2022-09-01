import pygame

# WINDOW Stuff
WIDTH = 400
HEIGHT = 100

pygame.init()

pygame.font.init()

background_colour = (100, 100, 100)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
  
pygame.display.set_caption('Quaver Guide')
  
screen.fill(background_colour)

# OTHER PYGAME Stuff
font = pygame.font.Font('C:\\Program Files (x86)\\Steam\\steamapps\\common\\Quaver\\Fonts\\lato-black.ttf',22)
titleFont = pygame.font.Font('C:\\Program Files (x86)\\Steam\\steamapps\\common\\Quaver\\Fonts\\lato-black.ttf',22)

# OTHER Stuff
running = True

Diff = "[No Diff Selected]"
Title = "No Map Found"
ID = "No ID Found"
Mods = "(No Mods In Use)"

Mod = ""

T = ""
D = ""
M = ""
I = ""

def Check():
  with open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Quaver\\Data\\Temp\\Now Playing\\mapid.txt", "r") as txt_file:
    return txt_file.readlines()

def SetInfo():
  global Diff, Title, ID, Mods, Mod, T, D, M, I
  with open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Quaver\\Data\\Temp\\Now Playing\\difficulty.txt", "r") as txt_file:
    Diff = txt_file.readlines()
  with open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Quaver\\Data\\Temp\\Now Playing\\map.txt", "r") as txt_file:
    Title = txt_file.readlines()
  with open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Quaver\\Data\\Temp\\Now Playing\\mapid.txt", "r") as txt_file:
    ID = txt_file.readlines()
  with open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Quaver\\Data\\Temp\\Now Playing\\mods.txt", "r") as txt_file:
    Mods = txt_file.readlines()

  Mod = ""

  for x in Mods:
    Mod += x

  Mods = Mod

  # Decides whether 
  if len(Mods.split(',')) > 1:
    ModsPrefix = "Mods: "
  else:
    ModsPrefix = "Mod: "

  T = Title[0]
  D = "Difficulty: " + str(Diff[0])
  M = ModsPrefix + "(" + str(Mods) + ")"
  I = "Map ID: " + ID[0]

SetInfo()

# Main
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
        if event.type == pygame.VIDEORESIZE:
            w, h = pygame.display.get_surface().get_size()
            WIDTH = w
            HEIGHT = h

    if Check != ID:
      SetInfo()

    screen.fill(background_colour)
    pygame.draw.rect(screen, (66,66,66), pygame.Rect(3, 3, WIDTH-10, HEIGHT-10), 0, 0, 0, 0, 0, 10)
    pygame.draw.rect(screen, (33,33,33), pygame.Rect(3, 3, WIDTH-10, HEIGHT-10), 3, 0, 0, 0, 0, 10)

    if font.size(T)[0]+16 > WIDTH:
      titleFontSize = 22 / ((font.size(T)[0]+16)/WIDTH)
    else:
      titleFontSize = 22
    
    titleFont = pygame.font.Font('C:\\Program Files (x86)\\Steam\\steamapps\\common\\Quaver\\Fonts\\lato-black.ttf', round(titleFontSize-1))
    pygame.draw.line(screen, (50,50,50), (WIDTH/2 - titleFont.size(T)[0]/2,35), (WIDTH/2 + titleFont.size(T)[0]/2,35), 3)



    TA = titleFont.render(T,False,(255,255,255))
    DA = font.render(D,False,(255,255,255))
    MA = font.render(M,False,(255,255,255))
    IA = font.render(I,False,(255,255,255))


    screen.blit(TA,(round(WIDTH/2 - titleFont.size(T)[0]/2,35),10))
    screen.blit(DA, (round(WIDTH/2 - font.size(D)[0]-10,35),40))
    screen.blit(MA, (round(WIDTH/2 + 10),40))
    screen.blit(IA, (round(WIDTH/2 - titleFont.size(I)[0]/2),60))

    pygame.display.update()
    pygame.display.flip()
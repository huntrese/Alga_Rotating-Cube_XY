# Imports
import sys
import pygame
import math
import time
# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []
VERTEX_ARRAY=[]
EDGES = []
ARRAY2D=[]

li=[]
li2=[]
with open("D:\mesh\mesh.csv") as file:
    data=file.readlines()
    for i in data:
            a=i.split(";")
            print(a)
            VERTEX_ARRAY.append((float(a[0]),float(a[1]),float(a[2][:-2])))
        
    print(VERTEX_ARRAY)
li=[]
with open('D:\\mesh\\file.txt') as file:
    data=file.readline()[1:-1]
    a=data.split(',')
    for i in a:
        b=i.replace("[","").replace("]","").replace(" ","")
        li.append(int(b))

for i in range(len(li)-1):
    if li[i]!=li[i+1]:
        EDGES.append((li[i],li[i+1]))
print(EDGES)


focal_length = 720

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

def myFunctionX():
    for j in range(180):
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    return("")       
            screen.fill((255, 255, 255))
            customButton = Button(400, 10, 120, 40, 'STOP',stop)
            customButton.process()
            Matrix=get_Matrix('X',j)
            newCoords=[]
            coords2D=[]
            newCoords=rotateX(VERTEX_ARRAY,Matrix)
            print(newCoords)
            for i in newCoords:
                coords2D.append(to_2D(i))
            print(coords2D)
            for i in EDGES:

                pygame.draw.line(screen, "blue",coords2D[i[0]] ,coords2D[i[1]])
            pygame.display.flip()
                
        except:
            pass
def myFunctionY():
    for j in range(180):
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    return("")  
       
            screen.fill((255, 255, 255))
            customButton = Button(400, 10, 120, 40, 'STOP',stop)
            customButton.process()
            Matrix=get_Matrix('Y',j)
            newCoords=[]
            coords2D=[]
            newCoords=rotateX(VERTEX_ARRAY,Matrix)
            print(newCoords)
            for i in newCoords:
                coords2D.append(to_2D(i))
            print(coords2D)
            for i in EDGES:

                pygame.draw.line(screen, "blue",coords2D[i[0]] ,coords2D[i[1]])
            pygame.display.flip()
                
        except:
            pass

def stop():
    pygame.event.post(pygame.event.Event(pygame.KEYUP, key=pygame.K_RIGHT))
    pygame.display.flip()


def get_Matrix(c,alfa):
    if c.lower()=="y":
        MATRIX=[
            [math.cos(alfa),0,-math.sin(alfa)],
            [0,1,0],
            [math.sin(alfa),0,math.cos(alfa)]
            ]
    if c.lower()=="x":
        MATRIX=[
            [1,0,0],
            [0,math.cos(alfa),math.sin(alfa)],
            [0,-math.sin(alfa),math.cos(alfa)]
            ]
    return(MATRIX)

def to_pygame(coords, height):
    
    return (height + coords)

def to_2D(vertex):
    x = vertex[0] * (focal_length/(focal_length+vertex[2]))
    y = vertex[1] * (focal_length/(focal_length+vertex[2]))
    return((to_pygame(x,350),to_pygame(y,250)))

def rotateX(coords,matrix):
    result=[[0,0,0]for x,y,z in VERTEX_ARRAY]
    for i in range(len(coords)):
   # iterate through columns of Y
        for j in range(len(matrix[0])):
       # iterate through rows of Y
            for k in range(len(matrix)):
                result[i][j] += coords[i][k] * matrix[k][j]
    return(result)


customButton = Button(30, 30, 40, 20, 'X', myFunctionX)
customButton = Button(30, 70, 40, 20, 'Y', myFunctionY)


# Game loop.
while True:
    screen.fill((255, 255, 255))
    
    coords2D=[]
    for i in VERTEX_ARRAY:
        coords2D.append(to_2D(i))
    for i in EDGES:
        pygame.draw.line(screen, "blue",coords2D[i[0]] ,coords2D[i[1]])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for object in objects:
        object.process()
   
    
    pygame.display.flip()
    fpsClock.tick(fps)
import pygame
import time
from threading import *


class MainMenuButton(Thread):
    def __init__(self,screen,CordinateX,CordinateY,*args):
        Thread.__init__(self)
        self.X=CordinateX
        self.Y=CordinateY
        self.screen = screen
        self.CordinateX=CordinateX
        self.CordinateY=CordinateY

    def run(self):
        try:
            while(True):
                self.pos=pygame.mouse.get_pos()

                self.OnMainMenuButton=False
                if self.pos[0] > self.X and self.pos[0] < self.X + 240 and self.pos[1] > self.Y and self.pos[1] < self.Y + 35:
                    self.OnMainMenuButton=True

                pygame.font.init()

                if self.OnMainMenuButton == False:
                    pygame.draw.rect(self.screen,(255,255,255),(self.X,self.Y,240,35))
                    myfont = pygame.font.SysFont('helvetica', 20)
                    textsurface = myfont.render("Go Back to Main Menu", False, (0, 0, 0))
                    self.screen.blit(textsurface, (self.X+17, self.Y))
                else:
                    pygame.draw.rect(self.screen,(0,0,0),(self.X,self.Y,240,35))
                    pygame.draw.rect(self.screen,(255,255,255),(self.X,self.Y,240,35),3)
                    myfont = pygame.font.SysFont('helvetica', 20)
                    textsurface = myfont.render("Go Back to Main Menu", False, (255, 255, 255))
                    self.screen.blit(textsurface, (self.X+17, self.Y))
                pygame.event.get()
                pygame.display.update()
        except:
            pass



class ExitText(Thread):
    def __init__(self,screen,CordinateX,CordinateY,*args):
        Thread.__init__(self)
        self.X=CordinateX
        self.Y=CordinateY
        self.screen = screen
        self.CordinateX=CordinateX
        self.CordinateY=CordinateY

    def run(self):
        try:
            while(True):
                pygame.font.init()
                myfont = pygame.font.SysFont('helvetica', 20)
                textsurface = myfont.render("Press Esc to Exit.", False, (255, 255, 255))
                self.screen.blit(textsurface, (self.X+17, self.Y))
        except:
            pass



class OperationsDoneRat:
    def __init__(self,NoOfOperations,screen,X,Y,String):
        try:
            self.NoOfOperations=NoOfOperations
            self.screen=screen
            self.X=X
            self.Y=Y
            pygame.font.init()

            myfont = pygame.font.SysFont('helvetica', 20)
            textsurface = myfont.render(String, False, (255, 255, 255))
            self.screen.blit(textsurface, (self.X + 50, self.Y))
            myfont = pygame.font.SysFont('helvetica', 20)
            textsurface = myfont.render("Operations Performed: "+str(self.NoOfOperations), False, (255, 255, 255))
            self.screen.blit(textsurface, (self.X, self.Y+40))
        except:
            pass


class OperationsDoneKnight:
    def __init__(self,NoOfOperations,screen,X,Y,String):
        try:
            self.NoOfOperations=NoOfOperations
            self.screen=screen
            self.X=X
            self.Y=Y

            pygame.font.init()

            myfont = pygame.font.SysFont('helvetica', 20)
            textsurface = myfont.render(String, False, (255, 255, 255))
            self.screen.blit(textsurface, (self.X+10, self.Y))
            myfont = pygame.font.SysFont('helvetica', 20)
            textsurface = myfont.render("Operations Performed: "+str(self.NoOfOperations), False, (255, 255, 255))
            self.screen.blit(textsurface, (self.X, self.Y+40))
        except:
            pass
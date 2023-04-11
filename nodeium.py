import pygame

class node:
    def __init__(self,col,rect,hdh=5) -> None:
        self.col = col
        self.drg = False
        self.HDH =hdh
        self.rect = pygame.rect.Rect(rect)
        self.hd = pygame.rect.Rect(rect)
        self.nds = self.hd.y + (hdh + 3)
        self.co = self.hd.x+(self.hd.w-6)
        self.ci = self.hd.x+1
        self.outcon = [conn("white",0,0)]
        self.incon = [conn("white",0,0)]
        I = self.nds
        for i in self.outcon:
            i.rect.x,i.rect.y = self.co,I
            I += 6
        I = self.nds
        for i in self.incon:
            i.rect.x,i.rect.y = self.ci,I
            I += 6
        self.hd.h = hdh
    def draw(self,scr:pygame.Surface):
        scr.fill((50,50,50),self.rect)
        scr.fill(self.col,self.hd)
        for i in self.outcon:
            i.draw(scr)
        for i in self.incon:
            i.draw(scr)
    def click(self,mp):
        if self.drg:
            drgd = self.rect.collidepoint(mp)
        else:
            drgd = self.hd.collidepoint(mp)
        if drgd:
            self.drg = True
            self.hd.centerx = mp[0]
            self.rect.centerx = mp[0]
            self.hd.top = mp[1]-3
            self.rect.top = mp[1]-3

            self.nds = self.hd.y + (self.HDH + 3)
            self.co = self.hd.x+(self.hd.w-6)
            self.ci = self.hd.x+1

            I = self.nds
            for i in self.outcon:
                i.rect.x,i.rect.y = self.co,I
                I += 6
            I = self.nds
            for i in self.incon:
                i.rect.x,i.rect.y = self.ci,I
                I += 6
        
        else:
            self.drg = False

class conn:
    def __init__(self,col,x,y,con=None) -> None:
        self.col = col
        self.connd = con
        self.x,self.y = x,y
        self.rect = pygame.Rect(x,y,5,5)
    def draw(self,scr:pygame.Surface):
        pygame.draw.rect(scr,self.col,self.rect,2)
        if self.connd:
            pygame.draw.line(scr,self.col,(self.rect.x+2,self.rect.y+2),(self.connd.rect.x+2,self.connd.rect.y+2),3)
            
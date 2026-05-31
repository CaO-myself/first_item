import pygame

class Image_Surface:#图像对象
    def __init__(self,item,rect,look=True,name=None):
        self.item=item
        self.rect=item.get_rect()
        self.rect.center=rect
        self.name=name
        self.look=look

    def display(self,screen):
        if self.look:
            screen.blit(self.item,self.rect)

class Font_Surface:#文字对象
    def __init__(self,text,rect,font,color=(255,255,255),look=True,name=None):
        self.item=font.render(text, True, color)
        self.rect=self.item.get_rect()
        self.rect.center=rect
        self.name=name
        self.look=look

    def display(self,screen):
        if self.look:
            screen.blit(self.item,self.rect)

class Black_Ground:#背景对象
    def __init__(self,x,y,image,name=None,look=None):
        self.item=image
        self.rect = self.item.get_rect()#建立矩形区域
        self.rect.center=(x/2,y/2)
        self.name=name
        self.look=look

    def display(self,screen):
        if self.look:
            screen.blit(self.item,self.rect)

class Line_Surface:#线条对象
    def __init__(self,item,rect,color=(255,255,255),look=True,mode=None):
        self.item=pygame.Surface((item))
        self.item.fill(color)
        self.rect=self.item.get_rect()
        self.look=True
        if mode==None:self.rect.center=rect#模式改变时，可以自主赋值

    def display(self,screen):
        if self.look:
            screen.blit(self.item,self.rect)

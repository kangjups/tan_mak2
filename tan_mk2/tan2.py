# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 22:28:20 2022

@author: angel
"""

import pygame
import random

class character:
    def __init__(self,img,x,y,hp):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.hp = hp

        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255,255,255)
        
        self.font = pygame.font.SysFont(None,30)
        self.hp_img = self.font.render(str(self.hp),True,self.WHITE)
        
    def screen(self,screen):
        screen.blit(self.img,(self.x,self.y))
        screen.blit(self.hp_img,(self.x+60,self.y+80))
        
    
    def pv(self):
        self.rect = self.img.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
        
    def hp(self):
        pass
    
    

class weapon:
    def __init__(self,img,speed,damage):
        self.img = pygame.image.load(img)
        self.speed = speed
        self.damage = damage
        self.weapons = []
        
        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        
        
    def add_weapon(self,x,y):
        self.weapons.append([x, y])
    
    def min_weapon(self):
        self.weapons = [ [w[0] + self.speed, w[1]] for w in self.weapons]
        self.weapons = [ [w[0], w[1]] for w in self.weapons if w[0] < 1100 ]
        
    def pv(self):
        for idx, self.img_val in enumerate(self.img):
            self.x = self.img_val[0]
            self.y = self.img_val[1]

            # 무기 정보
            self.rect = self.img.get_rect()
            self.rect.left = self.x
            self.rect.top = self.y
    
    def screen(self,screen):
        for self.x, self.y in self.weapons:
            screen.blit(self.img, (self.x+50,self.y+40))
        
def manu():    
    pygame.init()
    pygame.mixer.init()
    
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # 화면
    manu = pygame.image.load("manu.png")
    
    
    running = True
    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False 
          
            if event.type == pygame.KEYDOWN:
                pass           
            
            if event.type == pygame.MOUSEMOTION:
                pass
            
            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스의 어떤 버튼을 눌렀을때
                if event.button == 1:  # 마우스 왼쪽 클릭시
                    x, y = pygame.mouse.get_pos()    
                    if x > 400 and x < 800 and y > 400 and y < 490:
                        running = False
                    if x > 400 and x < 800 and y > 520 and y < 610:
                        print("setting")
                    if x > 400 and x < 800 and y > 650 and y < 740:
                        running = False
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            
        # 화면 그리기
        screen.blit(manu, (0, 0)) # 배경 화면 
        pygame.display.update() # 화면 업데이트 
    
    pygame.quit() 
    if x > 400 and x < 800 and y > 400 and y < 490:
        return True  
    if x > 400 and x < 800 and y > 650 and y < 740:
        return False 
    
def tan():    
    pygame.init()
    pygame.mixer.init()
    
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    pygame.display.set_caption("tan")
    
    clock = pygame.time.Clock()
    
    # 화면
    background = pygame.image.load("back_ground.png")
    blue_box = pygame.image.load("blue_box.png")
    red_box = pygame.image.load("red_box.png")
    
    player = character("player.png",250,345,100) # 플레이어
    monster = character("monster.png",815,345,100) # 몬스터
    arrow = weapon("arrow.png",20,20) # 화살
    
    running = True
    while running:
        dt = clock.tick(30)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False 
          
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_a: 
                    player.x -= 175
                
                if event.key == pygame.K_d: 
                    player.x += 175
                
                if event.key == pygame.K_w: 
                    player.y -= 120 
                    
                if event.key == pygame.K_s: 
                    player.y += 120
                    
                if event.key == pygame.K_SPACE: 
                    arrow.add_weapon(player.x,player.y)
                
            if event.type == pygame.MOUSEMOTION:
                pass
            
            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스의 어떤 버튼을 눌렀을때
                if event.button == 1:  # 마우스 왼쪽 클릭시
                    x, y = pygame.mouse.get_pos()    
                    if y > 0 and y < 600:
                        arrow.add_weapon(player.x,player.y)
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pass
                
        # 플레이어 캐릭터 이동 제한
        if player.x <= 75 : # 플레이어 x 최소 제한
            player.x = 75
        if player.x >= 425: # 플레이어 x 최대 제한
            player.x = 425
            
        if player.y <= 225 : # 플레이어 y 최소 제한
            player.y = 225
        if player.y >= 465: # 플레이어 y 최대 제한 
            player.y = 465
        
        # 탄환 이동
        arrow.min_weapon()
        
        # 충돌감지
        player.pv()
        monster.pv()
        arrow.pv()
        if monster.rect.colliderect(arrow.rect):
            print("dd")
        
        # 화면 그리기
        screen.blit(background, (0, 0)) # 배경 화면 
       
        for i in range(3): # 박스
            for a in range(3):
               screen.blit(blue_box,(75+(a*175),225 + (i*120)))
               screen.blit(red_box,(640+(a*175),225 + (i*120)))
        
        player.screen(screen) # 플레이어 
        monster.screen(screen) # 몬스터
        arrow.screen(screen) # 탄환
        
        pygame.display.update() # 화면 업데이트 
    
    pygame.quit() 
    return False
    
if __name__ == "__main__":
    runing = manu()
    while runing :    
        runing = tan()




# _*_coding:utf -8 _*_
import pygame
import time
from pygame.locals import *
from sys import exit
import os
import os.path
import random
pygame.init()

#loading
screen = pygame.display.set_mode((1600, 900), 0, 32)
pygame.display.set_caption("Card game")
my_font = pygame.font.SysFont("other/font.ttf", 42)
text_surface_ask = my_font.render("Do you want to get another card?", True, (255,255,255))
text_surface_ask_final = my_font.render("Do you want to get another card?", True, (255,255,255))
text_surface_win = my_font.render("You WIN! Press 'r' to restart the game", True, (255,255,255))
text_surface_lose = my_font.render("Sorry you lost! Press 'r' to restart the game", True, (255,255,255))
text_surface_tied = my_font.render("Wow, tied! Press 'r' to restart the game", True, (255,255,255))
bg = pygame.image.load('background.jpg').convert_alpha()

cards_img=[]
for i in range(1,14):
    card_img_loc = "cards/"+str(i)+".jpg"
    cards_img.append(pygame.image.load(card_img_loc).convert())

icon = pygame.image.load("cards/13.jpg").convert_alpha()
pygame.display.set_icon(icon)
while(True):
    #游戏开始
    #电脑抽卡
    host_card3 = -10
    host_card1 = random.randint(1,13)
    host_card2 = random.randint(1,13)
    sum_host_temp = host_card1 + host_card2
    while(True):
        if sum_host_temp < 12:
            host_card3 = random.randint(1,10)
            sum_host = host_card1 + host_card2 + host_card3
            sum_host_temp = sum_host
            print("<12")
            print(sum_host)
        elif sum_host_temp > 21:
            host_card1 = random.randint(1,13)
            host_card2 = random.randint(1,13)
            sum_host = host_card1 + host_card2
            sum_host_temp = sum_host
            print(">21")
            print(sum_host)
        else:
            sum_host = host_card1 + host_card2
            print("good")
            break
    #玩家抽卡
    player_cards_list = []
    player_card1 = random.randint(1,13)
    player_card2 = random.randint(1,13)
    while player_card1 + player_card2 >21:
        player_card1 = random.randint(1,13)
        player_card2 = random.randint(1,13)
    player_cards_list.append(player_card1)
    player_cards_list.append(player_card2)
    sum_player = player_card1 + player_card2

    show_computer_card = False
    # 游戏主循环
    while(True):
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        card_x = 100
        for i in range(len(player_cards_list)):
            screen.blit(cards_img[player_cards_list[i]-1], (card_x, 500))
            card_x+=50


        if sum_player<=21:
            screen.blit(text_surface_ask, (card_x+300, 500))
            if event.type == KEYDOWN and event.key == K_y:
                card_next = random.randint(1,13)
                player_cards_list.append(card_next)
                sum_player += card_next
                event.type == KEYUP
                time.sleep(0.15)
            elif event.type == KEYDOWN and event.key == K_n:
                if sum_player<sum_host:
                    text_surface_ask = text_surface_lose
                    show_computer_card = True
                elif sum_player == sum_host:
                    text_surface_ask = text_surface_tied
                    show_computer_card = True
                else:
                    text_surface_ask = text_surface_win
                    show_computer_card = True
                event.type == KEYUP
        else:
            screen.blit(text_surface_lose, (card_x+300, 500))
            screen.blit(cards_img[host_card1-1], (100, 100))
            screen.blit(cards_img[host_card2-1], (150, 100))
            if host_card3 != -10:
                screen.blit(cards_img[host_card3-1], (200, 100))
            if event.type == KEYDOWN and event.key == K_r:
                text_surface_ask = text_surface_ask_final
                break

        if show_computer_card == True:
            screen.blit(cards_img[host_card1-1], (100, 100))
            screen.blit(cards_img[host_card2-1], (150, 100))
            if host_card3 != -10:
                screen.blit(cards_img[host_card3-1], (200, 100))
            if event.type == KEYDOWN and event.key == K_r:
                text_surface_ask = text_surface_ask_final
                break

        # 刷新画面
        pygame.display.update()

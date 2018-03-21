import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #开始游戏循环
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建play按钮
    play_button = Button(ai_settings,screen,"PLAY")

    #创建一个用于存储游戏统计信息的实例，并创建计分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.creat_fleet(ai_settings,screen,ship,aliens) 
    
    while 1:
        gf.check_event(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)#检查键盘事件

        if stats.game_active:
            ship.update()#更新飞船位置
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)#把所有更新的
        #内容显示到屏幕上
run_game()
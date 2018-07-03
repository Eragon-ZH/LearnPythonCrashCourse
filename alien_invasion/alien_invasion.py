import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from sound import Music

def run_game():
    # 初始化，创建屏幕对象
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建开始按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于统计游戏统计信息的实例, 创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船, 子弹编组， 外星人编组
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.creat_fleet(ai_settings, screen, ship, aliens)
    # 创建背景音乐
    music = Music()
    music.bg_music.play(-1)
    # 开始循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                                                        aliens,bullets, music)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                                                                        bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                                                                        bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                                                                    play_button)

run_game()

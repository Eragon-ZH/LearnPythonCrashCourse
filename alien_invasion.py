import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats

def run_game():
    # 初始化，创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于统计游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船, 子弹编组， 外星人编组
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.creat_fleet(ai_settings, screen, ship, aliens)

    # 开始循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()

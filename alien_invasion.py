# --*-- coding:utf-8 --*--
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	
	pygame.display.set_caption("外星人入侵--咸阳师范学院--秦时小")
	#创建一艘飞船
	ship = Ship(screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个用于存储外星人的编组
	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen,aliens)
	#创建开始按钮
	button = Button("play",screen)
	#创建一个记分板
	scoreboard = Scoreboard(str(ai_settings.score),screen)
	#开始游戏的主循环
	while True:
		gf.update_screen(ai_settings,screen,ship,aliens,bullets,button,scoreboard)
		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets,button)
		if ai_settings.game_flag == False:
			continue
		#更新飞船位置
		ship.update()
		#更新子弹
		bullets.update()
		#更新外星人
		aliens.update()
		#检测子弹是否射中外星人
		for bullet in bullets.copy():
			for alien in aliens.copy():
				if bullet.rect.top == alien.rect.bottom and alien.rect.left <= bullet.rect.x <= alien.rect.right:
					aliens.remove(alien)
					bullets.remove(bullet)
					ai_settings.score +=10#每杀死一个外星人分数加10
					scoreboard.set_score(str(ai_settings.score))
					break
		#检测外星人当前数量来控制外星人个数不少于多少
		if len(aliens) <= ai_settings.alien_count:
			gf.create_fleet(ai_settings,screen,aliens)
		#检测是否碰到底部或飞船
		for alien in aliens.copy():
			if alien.rect.bottom == ship.rect.top and (ship.rect.x - alien.rect.width)<= alien.rect.x <= (ship.rect.x+ship.rect.width) :
				aliens.empty() #清空外星人
				bullets.empty()#清空子弹
				ai_settings.game_flag = False
				ai_settings.score = 0
			elif alien.rect.bottom == screen.get_rect().bottom:
				aliens.empty()
				bullets.empty()
				ai_settings.game_flag = False
				ai_settings.score = 0
		#删除已经消失的子弹
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		#更新屏幕
		gf.update_screen(ai_settings,screen,ship,aliens,bullets,button,scoreboard)
run_game()

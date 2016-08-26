# --*-- coding:utf-8 --*--
import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	"""处理键盘按下事件"""
	if event.key == pygame.K_RIGHT:
		ship.move_right = True
	elif event.key == pygame.K_LEFT:
		ship.move_left = True
	elif event.key == pygame.K_SPACE:
		"""创建一个子弹并将其加入到编组中"""
		#限制屏幕上最多出现的子弹数量
		if len(bullets)<ai_settings.bullet_max_count:
			new_bullet = Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event,ship):
	"""处理键盘抬起事件"""
	if event.key == pygame.K_RIGHT:
		ship.move_right = False
	elif event.key == pygame.K_LEFT:
		ship.move_left = False

def check_mouse_pos(button,ai_settings,mouse_x,mouse_y):
	"""检查鼠标是否点击到了按钮上"""
	if button.rect.left <= mouse_x <=button.rect.right and button.rect.top <= mouse_y <=button.rect.bottom:
		ai_settings.game_flag = True
	
def check_events(ai_settings,screen,ship,bullets,button):
	"""响应按钮和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		#按下键盘
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_mouse_pos(button,ai_settings,mouse_x,mouse_y)
			
def update_screen(ai_settings,screen,ship,aliens,bullets,button,scoreboard):
	"""更新屏幕图像，并重新绘制"""
	#设置屏幕背景颜色
	screen.fill(ai_settings.bg_color)
	#绘制所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	#绘制记分板
	scoreboard.draw()
	#绘制飞船
	ship.blitShip()
	#绘制每个外星人
	aliens.draw(screen)
	#绘制按钮
	if ai_settings.game_flag == False:
		button.draw()
	#让最近绘制的屏幕可见
	pygame.display.flip()

def get_alien_count(ai_settings,spacing_width):
	"""计算每行能容纳多少外星人"""
	available_width = ai_settings.screen_width - 2*spacing_width #屏幕可用宽度
	alien_count = int(available_width/(2*spacing_width)) #每行可以放下多少个外星人
	return alien_count
	
def create_alien(ai_settings,screen,aliens,number):
	"""创建一个外星人并将其放在当前行"""
	alien = Alien(ai_settings,screen)
	spacing_width = alien.rect.width #两个外星人之间的间距
	alien.x = spacing_width + 2*alien.rect.width*number
	alien.rect.x = alien.x
	aliens.add(alien)
	
def create_fleet(ai_settings,screen,aliens):
	"""创建外星人群体"""
	alien = Alien(ai_settings,screen)
	spacing_width = alien.rect.width #两个外星人之间的间距
	alien_count = get_alien_count(ai_settings,spacing_width)
	#创建第一行外星人
	for number in range(alien_count):
		create_alien(ai_settings,screen,aliens,number)
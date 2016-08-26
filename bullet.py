# --*-- coding:utf-8 --*--
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""管理飞船发射的子弹"""
	def __init__(self,ai_settings,screen,ship):
		"""在飞船所处的位置创建一个子弹对象"""
		super(Bullet,self).__init__()
		self.screen = screen
		
		#在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_hight)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""向上移动子弹"""
		self.rect.y -= self.speed_factor
	
	def draw_bullet(self):
		"""在屏幕上绘制子弹,下面两句都可以"""
		pygame.draw.rect(self.screen,self.color,self.rect)
		#self.screen.fill(self.color,self.rect)
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""外星人类"""
	def __init__(self,ai_settings,screen):
		"""初始化外星人并设置其初始位置"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#加载外星人图片
		self.image = pygame.image.load("images/alien.bmp")
		self.rect = self.image.get_rect()
		
		#初始化外星人的初始位置,以外星人的宽和高作为初始坐标
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#存储外星人的准确位置，以浮点型存储
		#这样能够减慢外星人的移动速度
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		#外星人的速度计数
		self.speed = 0.0
	
	def update(self):
		"""控制外星人的移动速度并更新外星人位置"""
		if int(self.speed) == 1:
			self.rect.y += 1
			self.speed = 0.0
		else:
			self.speed +=0.1
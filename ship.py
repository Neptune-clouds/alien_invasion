# --*-- coding:utf-8 --*--
import pygame

class Ship():
	def __init__(self,screen):
		"""接收屏幕,根据屏幕来放置飞船位置"""
		self.screen = screen
		#加载飞船图片
		self.image = pygame.image.load("images/ship.bmp")
		#获取飞船的矩形
		self.rect = self.image.get_rect()
		#获取屏幕的矩形
		self.screen_rect = self.screen.get_rect()
		
		#根据屏幕来设置飞船的位置到屏幕底部居中
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#移动标志
		self.move_right = False
		self.move_left = False
	
	def update(self):
		"""更新飞船的位置"""
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 2
		if self.move_left and self.rect.left >self.screen_rect.left:
			self.rect.centerx -= 2
				
	def blitShip(self):
		"""绘制飞船到指定位置"""
		self.screen.blit(self.image,self.rect)

import pygame.font
import pygame.image

class Scoreboard():
	def __init__(self,score,screen):
		self.score = score
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.font = pygame.font.SysFont(None,50)
		self.text_color = 255,0,0
		self.bg_color = 0,255,0
		
	
	def draw(self):	
		"""绘制分数到屏幕显示"""
		self.score_image = self.font.render(self.score,True,self.text_color,self.bg_color)
		self.rect = self.score_image.get_rect()
		self.rect.top = self.screen_rect.top
		self.rect.centerx = self.screen_rect.centerx
		self.screen.blit(self.score_image,self.rect)
	
	def set_score(self,score):
		"""设置分数"""
		self.score = score
		
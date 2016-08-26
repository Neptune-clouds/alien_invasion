import pygame.font
import pygame.image

class Button():
	def __init__(self,msg,screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.font = pygame.font.SysFont(None,100)
		self.text_color = 255,0,0
		self.bg_color = 0,255,0
		self.msg_image = self.font.render(msg,True,self.text_color,self.bg_color)
		self.rect = self.msg_image.get_rect()
		self.rect.center = self.screen_rect.center
		pygame.image.save(self.msg_image,"./images/a.bmp")
	def draw(self):	
		self.screen.blit(self.msg_image,self.rect)
		
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""表示单个外星人"""
	def __init__(self,ai_settings,screen):
		"""初始化外星人并设置其其实位置"""
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#加载外星人图像，设置其rect属性
		self.image = pygame.image.load(r'C:\Users\dell\大战外星人\images\alien.bmp')
		self.rect = self.image.get_rect()

		#外星人出现在屏幕左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#存储外星人的准确位置
		self.x = float(self.rect.x)

	def check_edges(self):
		"""如果外星人处于屏幕边缘，返回true"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):
		"""向右移动外星人"""
		self.x += (self.ai_settings.alien_speed_factor*
			            self.ai_settings.fleet_direction)
		#改变所移动距离的正负从而实现相反方向移动
		self.rect.x = self.x

	def blitme(self):
		self.screen.blit(self.image,self.rect)

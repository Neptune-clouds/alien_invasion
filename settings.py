# --*-- coding:utf-8 --*--
class Settings():
	"""存储卫星人所有设置的类"""
	def __init__(self):
		"""初始化游戏的设置"""
		# 屏幕设置
		self.screen_width = 1200 #宽
		self.screen_height = 700 #高
		self.bg_color = (230,230,230) #屏幕背景颜色

		# 子弹设置
		self.bullet_speed_factor = 1 #速度
		self.bullet_width = 3 #宽度
		self.bullet_hight = 10 #高度
		self.bullet_color = 255,0,0 #红色子弹
		
		self.bullet_max_count = 5  #同时出现的子弹的最大数量

		#外星人设置
		self.alien_count = 5 #屏幕上最少外星人数量
		
		#游戏状态标志 true表示开始，false表示结束
		self.game_flag = False
		self.score = 0 #分数
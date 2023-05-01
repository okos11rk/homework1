class Kassa:
	def __init__(self):
		self.money = 0
	def top_up(self, x):
		self.money += x
	def count_1000(self):
		print(self.money//1000, 'т.р.')
	def take_away(self, x):
		if self.money > x:
			self.money -= x
		else:
			print("Недостаточно денег")
k1 = Kassa()
print(k1.money)
k1.money+= 122
print(k1.money)
k1.count_1000()
k1.take_away(222)
print(k1.money)
k1.top_up(45)
print(k1.money)

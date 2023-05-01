import math
class Turtle:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.s = 1 
	def go_up(self):
		self.y += self.s
	def go_down(self):
		self.y -= self.s
	def go_left(self):
		self.x -= self.s
	def go_right(self):
		self.x += self.s
	def evolve(self):
		self.s += 1
	def degrade(self):
		if self.s <=1:
			print("Ошибка")
		else:
			self.s -= 1
	def count_moves(self, x2, y2):
		s = math.ceil((abs(self.x - x2) + abs(self.y - y2))/self.s)
		return s
t1 = Turtle()

print(t1.x, t1.y, t1.s)
t1.evolve()
print(t1.x, t1.y, t1.s)
t1.go_up()
print(t1.x, t1.y, t1.s)
t1.go_down()
print(t1.x, t1.y, t1.s)
t1.go_left()
print(t1.x, t1.y, t1.s)
t1.go_right()
print(t1.x, t1.y, t1.s)
t1.evolve()
print(t1.x, t1.y, t1.s)
t1.degrade()
print(t1.x, t1.y, t1.s)
print(t1.count_moves(10,20))

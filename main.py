import os
import random

class Entity:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, direct):
		# W, A, S, D
		if direct.upper() == "W" and self.y != 0:
			self.y -= 1
		if direct.upper() == "A" and self.x != 0:
			self.x -= 1
		if direct.upper() == "S" and self.y != 9:
			self.y += 1
		if direct.upper() == "D" and self.x != 9:
			self.x += 1

class Player(Entity):
	def __init__(self, x, y, maxHp):
		Entity.__init__(self, x, y)
		self.curHp = maxHp
		self.maxHp = maxHp

	def move(self, direct):
		if (e.x == p.x + 1 and e.y == p.y and direct.upper() == "D") or (e.x == p.x - 1 and e.y == p.y and direct.upper() == "A") or (e.y == p.y + 1 and e.x == p.x and direct.upper() == "S") or (e.y == p.y - 1 and e.x == p.x and direct.upper() == "W"):	
			pass
		else:
			Entity.move(self, direct)

class Enemy(Entity):
	def __init__(self, x, y, damage):
		Entity.__init__(self, x, y)
		self.damage = damage

	def attack(self, player):
		player.curHp -= self.damage
		
	def move(self, b):
		if b != "":
			a = random.randint(1, 4)
			if a == 1:
				if g.y == e.y - 1 and g.x == e.x:
					pass
				else:
					Entity.move(self, "w")
			elif a == 2:
				if g.x == e.x - 1 and g.y == e.y:
					pass
				else:
					Entity.move(self, "a")
			elif a == 3:
				if g.y == e.y + 1 and g.x == e.x:
					pass
				else:
					Entity.move(self, "s")
			elif a == 4:
				if g.x == e.x + 1 and g.y == e.y:
					pass
				else:
					Entity.move(self, "d")

class Field:
	def create_field(x, y):
		field = []
		for w in range(x):
			field.append([])
			for h in range(y):
				if w == p.y and h == p.x:
					field[w].append("[P]")
				elif w == g.y and h == g.x:
					field[w].append("[G]")
				elif w == e.y and h == e.x:
					field[w].append("[M]")
				else:
					field[w].append("[ ]")
		return field 

p = Player(0, 0, 10)
e = Enemy(6, 6, 5)
g = Entity(7, 7)

while True:
	
	field = Field.create_field(10, 10)
	
	for i in field:
		for q in i:
			print(q, end = "")
		print()
	
	a = input()
	os.system("clear")
	e.move(a)
	p.move(a)
	
	if (e.x == p.x + 1 and e.y == p.y) or (e.x == p.x - 1 and e.y == p.y) or (e.y == p.y + 1 and e.x == p.x) or (e.y == p.y - 1 and e.x == p.x):
		e.attack(p)
		print("SEI STATO COLPITO")

	print("la tua vita è {} su {} per una percentuale di {}".format(p.curHp, p.maxHp, (str((p.curHp/p.maxHp)*100) + "%" )))
	
	if p.curHp <= 0:
		print('''
 .d8888b.           d8b                                     888                 8888888b.      
d88P  Y88b          Y8P                                     888                 888  "Y88b     
Y88b.                                                       888                 888    888     
 "Y888b.    .d88b.  888      88888b.d88b.   .d88b.  888d888 888888 .d88b.       888    888 d8b 
    "Y88b. d8P  Y8b 888      888 "888 "88b d88""88b 888P"   888   d88""88b      888    888 Y8P 
      "888 88888888 888      888  888  888 888  888 888     888   888  888      888    888     
Y88b  d88P Y8b.     888      888  888  888 Y88..88P 888     Y88b. Y88..88P      888  .d88P d8b 
 "Y8888P"   "Y8888  888      888  888  888  "Y88P"  888      "Y888 "Y88P"       8888888P"  Y8P 
		''')
		print()
		input()
		break

	if p.x == g.x and p.y == g.y:
		print('''
 /$$   /$$           /$$       /$$    /$$ /$$             /$$               /$$
| $$  | $$          |__/      | $$   | $$|__/            | $$              | $$
| $$  | $$  /$$$$$$  /$$      | $$   | $$ /$$ /$$$$$$$  /$$$$$$    /$$$$$$ | $$
| $$$$$$$$ |____  $$| $$      |  $$ / $$/| $$| $$__  $$|_  $$_/   /$$__  $$| $$
| $$__  $$  /$$$$$$$| $$       \  $$ $$/ | $$| $$  \ $$  | $$    | $$  \ $$|__/
| $$  | $$ /$$__  $$| $$        \  $$$/  | $$| $$  | $$  | $$ /$$| $$  | $$    
| $$  | $$|  $$$$$$$| $$         \  $/   | $$| $$  | $$  |  $$$$/|  $$$$$$/ /$$
|__/  |__/ \_______/|__/          \_/    |__/|__/  |__/   \___/   \______/ |__/
		''')
		print()
		input()
		break






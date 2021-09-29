from font5x7 import Font5x7

class Message(object):

	def __init__(self, argument):
		self.text = open(argument[2]).read().splitlines()
		self.style = argument[1][0]

	def draw(self, message):
		output = [[0 for x in range(7)] for y in range(500)]
		for i in range(len(message)):
			increment = 0
			holder = ord(message[i])
			if holder == 10: holder = 32
			for h in range((i * 5), (i * 5 + 5)):
				column = Font5x7[((holder-32) * 5) + increment]
				for k in range(0, 7):
					output[h][k] = column % 2
					column = column // 2
				increment += 1

		for k in range(7):
			for h in range(len(message) * 5):
				if ((h != 0) and ((h % 5) == 0)): print("   ", end = '')
				if (output[h][k] == 1): print(self.style, end = '')
				else: print(' ', end='')
			print('')
		print('')

from font5x7 import Font5x7

class Message(object):

	def __init__(self, message, lineType, style):
		self.text = message
		self.type = lineType
		self.style = style

	def print(self):
		if self.type == 'C':
			for row in self.text:
				for character in range(len(row)):
					self.__drawLine(row[character])

		elif self.type == 'W':
			for row in self.text:
				if len(row) != 0: self.__drawLine(row)

		elif self.type == 'L':
			for row in self.text:
				self.__drawLine(row)

	def __drawLine(self, line):
		output = [[0 for _ in range(7)] for _ in range(len(line * 5))]
		for i in range(len(line)):
			increment = 0
			holder = ord(line[i])
			if holder == 10: holder = 32
			for h in range((i * 5), (i * 5 + 5)):
				column = Font5x7[((holder-32) * 5) + increment]
				for k in range(0, 7):
					output[h][k] = column % 2
					column = column // 2
				increment += 1

		for k in range(7):
			for h in range(len(line) * 5):
				if ((h != 0) and ((h % 5) == 0)): print("   ", end = '')
				if (output[h][k] == 1): print(self.style, end = '')
				else: print(' ', end='')
			print('')
		print('')

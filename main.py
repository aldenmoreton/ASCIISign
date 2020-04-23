import sys
from message import Message

def main():
	if len(sys.argv) != 3:
		return -1

	m = Message(sys.argv)

	if sys.argv[1][0] == 'C':
		for i in m.text:
			for j in range(len(i)):
				m.draw(i[j])

	elif sys.argv[1][0] == 'W':
		for i in m.text:
			if len(i) != 0: m.draw(i)

	elif sys.argv[1][0] == 'L':
		for i in m.text:
			m.draw(i)

	else:
		print("Invalid Format")

if __name__ == '__main__':
	main()
	
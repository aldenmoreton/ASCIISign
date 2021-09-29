import sys
from message import Message

def main():

	args = {}

	if len(sys.argv) != 3:
		args['message'] = [input('Enter your message:')]
		args['lineType'] = input('Enter your line type:')
		args['style'] = input('Enter your character style:')
	else:
		args = {}
		args['message'] = open(sys.argv[2]).read().splitlines()
		args['lineType'] = sys.argv[1][0]
		args['style'] = sys.argv[1][1]

	m = Message(**args)
	m.print()

if __name__ == '__main__':
	main()

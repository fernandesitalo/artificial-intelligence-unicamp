from read_and_process_input import *
from geometric_functions import *
from IdaStar import IdaStar

def main():
	archive = "input.txt"
	obj_input = read_and_process_input(archive)
	print(obj_input.graph)

	test = IdaStar(obj_input.graph)


if __name__ == '__main__':
    main()
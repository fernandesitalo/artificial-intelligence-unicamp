from read_and_process_input import *
from geometric_functions import *
from IdaStar import IdaStar
from IterativeDeepening import ID

def main():
	archive = "input.txt"
	obj_input = read_and_process_input(archive)
	print(obj_input.graph)

	test = ID(obj_input.graph, 5)
	visitations, path = test.run()
	print("IterativeDeepening")
	print("visitations:", visitations)
	print("path:", path)


if __name__ == '__main__':
    main()
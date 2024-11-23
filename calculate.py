import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):

	"""
	Принимает тип фигуры fig,
	название функции func и размер для данной фигуры size.
	Возвращает результат переданной операции
	для данной фигуры данного размера result.
	"""

	try:
		if len(size) > 1:
			raise Exception("Too many figure sides to calc")
		elif len(size) < 1:
			raise Exception("No figure sides inputed")
		elif fig not in figs:
			raise Exception("Not correct figure name")
		elif func not in funcs:
			raise Exception("Not correct function name")
	except Exception as e:
		return e
	else:
		result = eval(f'{fig}.{func}({size[0]})')
		return result


if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
	
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)

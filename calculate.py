import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):

	"""
    Принимает тип фигуры fig, название функции func и размер для данной фигуры size.

    Возвращает результат переданной операции для данной фигуры данного размера result.
    """
	
	if fig not in figs:
		return "Not correct figure name"
	if func not in funcs:
		return "Not correct function name"
	if len(size) > 1 and (fig == "circle" or fig == "square"):
		return "Too many figure sides to calc"
	if len(size) == 0 and (fig == "circle" or fig == "square"):
		return "No figure sides inputed"

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

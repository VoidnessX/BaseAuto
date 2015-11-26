def func(num):
	def func1(num):
		print num 

	def func2(num):
		print num+3
	func_dict = {1:func1, 2:func2}
	
	func_dict[1](num)

	
func(1)

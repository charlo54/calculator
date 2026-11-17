from calculator import add, subtract, divide, multiply, CircleArea

def test_add():
	#arrange
	a,b=2,3
	#act
	result= add(2,3)
	#assert
	assert result == 5

def test_divide():
	assert divide(6, 2) == 3

def test_subtract():
	assert subtract(57, 3) == 54

def test_multiply():
	assert multiply(5, 8) == 40

def test_divide_uneven():
	#arrange
	a,b=5,2
	#act
	result= divide(a,b)
	#assert
	assert result ==2.5

def test_circleArea():
	assert CircleArea(-4) =="Error"

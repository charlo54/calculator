# SCCM4910 lab project - a four operation calculator

def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def multiply(a,b):
	return a*b

def divide(a,b):
	return a/b 

def CircleArea(r):
	if r>=0:
		return 3.14*r*r
	else:
		return "Error"

def main():
	while True:
		a = float(input("enter first number"))
		op= input("enter operator (+,-,*,/)")
		b = float(input("enter second number"))
		if op=="+":
			print("your answer is...",add(a,b))
		elif op=="-":
			print("your answer is...",subtract(a,b))
		elif op=="*":
			print("your answer is...",multiply(a,b))
		elif op=="/":
			print("your answer is...",divide(a,b))
		else:
			print("try that again buckeroo. i cant believe you messed up something so blatantly simple. dont even play with me.")

if __name__ == "__main__":
	main()

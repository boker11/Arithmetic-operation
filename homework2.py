# -*- coding: gb2312 -*-

import sys
import random

from fractions import Fraction

class Equation():
	def __init__(self):
		self.op = ["+","-","*","��","/"]
		self.priority = {'+':1,'-':1,'*':2,'��':2}
		self.equ = self.getEquation()
		self.answer = self.getAnswer()

	#���������ʽ
	def getEquation(self):
		number = random.randint(2,9)
		tmpstring = ""
		tmpop = ''
		tmpint = 0
		for i in range(number):
			if tmpop == '/':            #�������
				tmpint = random.randint(tmpint+1,9)
				tmpop = random.choice(self.op[:-1])
			elif tmpop == '��':          #�������
				tmpint = random.randint(1,8)
				tmpop = random.choice(self.op)
			else:
				tmpint = random.randint(0,8)
				tmpop = random.choice(self.op)
			#��ӵ���ʽ��
			tmpstring += str(tmpint)
			tmpstring += tmpop
		tmpstring = list(tmpstring)
		#�޸����һ������Ϊ=
		tmpstring[-1] = '='
		tmpstring = ''.join(tmpstring)
		return tmpstring

	#����ʽ��
	def getAnswer(self):
		#�����зֺŵı��ʽ���ɴ�������list
		equlist = []
		i = 0
		while(i < len(self.equ)-1):
			if self.equ[i+1] != '/':
				equlist.append(self.equ[i])
				i += 1
			else:
				equlist.append(Fraction(int(self.equ[i]),int(self.equ[i+2])))
				i += 3

		#����׺���ʽת��Ϊ��׺
		new_equlist = self.change_list(equlist)
		#�����׺���ʽ�Ľ��
		return(self.calculate(new_equlist))

	#ת��Ϊ��׺���ʽ
	def change_list(self,equation):
		tmplist = []
		stack = []
		for op in equation:
			if type(op) == str and op >= '0' and op <= '9':
				tmplist.append(int(op))
			elif type(op) != str:
				tmplist.append(op)
			elif len(stack) == 0 or op == '(' or stack[-1] == '(':
				stack.append(op)
			elif op == ')':
				tmpTopStack = ''
				while tmpTopStack != '(':
					tmpTopStack = stack.pop()
					if tmpTopStack != '(':
						tmplist.append(tmpTopStack)
			else:
				while(len(stack) > 0 and self.priority[stack[-1]] >= self.priority[op]): #ջ�����ȼ����ڵ��ڸ÷��ţ�������ջ
					tmplist.append(stack.pop())
				stack.append(op)
		while(len(stack) != 0):
			tmplist.append(stack.pop())
		return tmplist 	


	#�����׺���ʽ�Ľ��
	def calculate(self,_list):
		tmpStack = []
		for tmpValue in _list:
			if type(tmpValue) != str:
				tmpStack.append(tmpValue)
			else:
				number_y = tmpStack.pop()
				number_x = tmpStack.pop()
				if tmpValue == "+":
					tmpStack.append(self.plus(number_x,number_y))
				elif tmpValue == "-":
					tmpStack.append(self.minus(number_x,number_y))
				elif tmpValue == "*":
					tmpStack.append(self.multiply(number_x,number_y))
				else:
					tmpStack.append(self.divide(number_x,number_y))
		return tmpStack[0]

	#��������
	def plus(self,num1,num2):
		return num1+num2

	def minus(self,num1,num2):
		return num1-num2

	def multiply(self,num1,num2):
		return num1*num2

	def divide(self,num1,num2):
		return Fraction(num1,num2)


def main():
	if sys.argv[1] != "-n":
		raise IOError("Please enter the right command!")
	num = int(sys.argv[2])
	score = 0
	print("���β��Թ�{}�⣬����100��".format(num))
	for i in range(1,num+1):
		equation = Equation()
		print("-----------------------------")
		print("��{}��: {}".format(i,equation.equ),end = '')
		ans = input().strip()
		if ans == str(equation.answer):
			score += 1
			print("�ش���ȷ������")
		else:
			print("�ش���󡣣��� ��ȷ�𰸣�{}".format(equation.answer))
	print("-----------------------------")
	print("���Խ��������β��Ե÷֣�{}��".format(round(float(score)/float(num)*100)))

if __name__ == '__main__':
	main()

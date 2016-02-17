# -*- coding: utf-8 -*-
class Schoolmember:
	"""docstring for Schoolmember"""
	def __init__(self, name, sex, nation):
		self.name = name
		self.sex = sex
		self.nation = nation
		
	def tell(self):
		print 'Hi, my name is %s, I am come from %s' % (self.name, self.nation)

class Student(Schoolmember): #继承主类
	def __init__(self, Name, Sex, Nation, Class, Score):
		Schoolmember.__init__(self, Name, Sex, Nation) #继承
		self.Class = Class
		self.Score = Score

	def paytuition(self, money):
		if money < 5000:
			print 'Get out!'
		else:
			print 'Welcome'

class Teacher(Schoolmember):
	def __init__(self, Name, Sex, Nation, Course, Salary):
		Schoolmember.__init__(self, Name, Sex, Nation)
		self.Course = Course
		self.Salary = Salary

	def teaching(self):
		print 'I am teaching %s, I am making %s per month!' % (self.Course, self.Salary)


S1 = Student('Jason', 'M', 'China', 'Python', 88)
S1.tell() #继承了主类的方法
S1.paytuition(5001)
S1.age = 30
print S1.age

T1 = Teacher('Alex', 'M', 'China', 'Python', 5000)
T1.tell()
T1.teaching()
print"I am 6'2\"tall."
print'I am 6\'2"tall.'

tabby_cat="\tI'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm\\a\\cat."

fat_cat='''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t*Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print '''she said:"he's a boy"'''

print"How old are you?",
age=raw_input()
print"How tall are you?",
height=raw_input()
print"How much do you weigh?",
weight=raw_input()

print"So,you're %s old,%s tall and %s heavy."%(age,height,weight)

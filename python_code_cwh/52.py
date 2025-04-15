# from emp import Employee
# # from emp import StudentEvaluator

# e = Employee("Harry")
# print(str(e))
# print(repr(e))
# # print(e.name)
# # print(len(e))
# # e()-

from emp import Employee, StudentEvaluator

e = Employee("Harry")
print(str(e))   
print(repr(e))  
print(e.name)     
print(len(e))   
e()             

print()


evaluator = StudentEvaluator()
evaluator("Raju", 75)   
evaluator("Vikas", 32)  

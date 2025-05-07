# LAMBDA FUNCTION

# def double(x):
#     return x * 2

def appl(fx, value):
    return 6 + fx(value)

double = lambda x : x*2
cube = lambda x : x*x*x
avg = lambda x,y,z : (x+y+z)/3

print(double(5))
print(cube(5))
print(avg(8,5,3))
print(appl(cube,2))
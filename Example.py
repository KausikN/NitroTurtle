'''
Example Turtle Programs
'''

# Imports
import turtle

# Main Funtions
# 1
def Ex1(mx):
    f = 1
    n = len(mx)
    tur = turtle.Turtle()
    tur.setpos(0, 0)
    j = 0
    while(j < n):
        if (f == 1):
            i = 0
            while(i <= n-1):
                tur.goto(i, j)
                i += 10
        if (f == 0):
            i = n-1
            while(i > -1):
                tur.goto(i, j)
                i -= 10
        f += 1
        if (f == 2):
            f = 0
        j += 10
    turtle.done()

# 2
def Ex2(mx):
    tur = turtle.Turtle()
    tur.setpos(0, 0)
    n = len(mx)
    second = int(n/2)
    tur.goto(second-1, second-1)
    tur.goto(second-1, second)
    tur.goto(second, second-1)
    tur.goto(second, second)
    turtle.done()

# Driver Code
Ex1(list(range(100)))
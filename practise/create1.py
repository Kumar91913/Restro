def my_function(**a):
    print("hi")
    print(a['a'],a['b'],a['c'],a['d'])
my_function(a="20",b="30",c="40",d="444444444444444")

def my_function(a="sandeep"):
    print("hi")
    print("hi:",a)
my_function()

def my_function(a,b):
    print("hi")
    print("hi:",a)
    print("hi:",b)
my_function(['15'],['20'])


def  my_function(a):
    for i in a:
        print('@'+i+'@', end=", ")
my_function(["sandeep","naveen","usha","madhu","suma","vs","karun"])

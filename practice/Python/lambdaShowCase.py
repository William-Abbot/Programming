def foo(x,y,z):
    result = x+y+z
    return result

def main():
    print(foo(1,2,3), "  regular function\n")
    print((lambda x,y,z : x+y+z)(1,2,3), "  lambda (input variable(s)) : function ---> lambda x,y,z : x+y+z\n")

if __name__ == "__main__":
    main()

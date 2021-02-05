# name: Ian Espinosa
# email: IanEspinosaBiz@gmail.com
# problem: Triangle

# define the recursive function triangle after this comment
def triangle(n):
    if n == 1:
        return '\n' + '*'
    else:
        return str(triangle(n - 1)) + '\n' + '*' * n

def main_test():
    tests = [0, '\n*', '\n*\n**', '\n*\n**\n***', '\n*\n**\n***\n****', '\n*\n**\n***\n****\n*****',
             '\n*\n**\n***\n****\n*****\n******', '\n*\n**\n***\n****\n*****\n******\n*******',
             '\n*\n**\n***\n****\n*****\n******\n*******\n********',
             '\n*\n**\n***\n****\n*****\n******\n*******\n********\n*********',
             '\n*\n**\n***\n****\n*****\n******\n*******\n********\n*********\n**********']
    errors = 0
    for n in range(1, len(tests)):
        student = triangle(n)
        correct = tests[n]
        if student != correct:
            print("test n = ", n)
            print("-" * 20)
            print(f"FAILED triangle({n})")
            print("Your triangle is:", repr(student))
            print(student)
            print()
            print("Test was expecting:", repr(correct))
            print(correct)
            errors += 1
    if errors == 0:
        print("All Passed")
    else:
        print("-" * 20)
        print(f"\n\nFAILED {errors} TESTS")

if __name__ == '__main__':
    main_test()
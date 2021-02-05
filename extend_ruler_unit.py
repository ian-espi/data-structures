# Project: Ruler
# Name: Ian Espinosa
# email: IanEspinosaBiz@gmail.com

# RulerUnit should have be usable with  +, -, /, *, ==, >, >=, <, and <=
# implement the appropriate 'operator method' see https://docs.python.org/3/library/operator.html
# use the __ methods so we use __add__ and not add
# note / is __truediv__, not __div__

#  1 inch on 1/64 ruler
def draw():
    for i in range(6): print(" " +(" "*(2**i-1)).join('|'*(2**(6-i)+1)))
    print("0.0"+" "*29 + "0.5"+ " "*29+"1.0\n")

class RulerUnit():

    # Constructor takes Inches and fraction numerator and denominator
    # Ruler( 3, 3, 16 ) will be 3 inches and 3/16 of an inch


    def __init__(self, inches, numerator, denominator):  # for 4 3/8 would call RulerUnit( 4, 3, 8)
        ''' RulerUnit( inches, numerator, denominator)'''
        if numerator == 0:
            denominator = 1
        elif denominator == 0:
            raise ValueError("Denominator is zero for a non zero numerator")
        sixtyfourths = int((inches + (numerator / denominator)) * 64.0 + 0.5)  # trim to nearest # of 64th
        self.u = int(sixtyfourths)

    def _reduce(self,f):
        ''' _reduce(fraction) will return (numerator, denominator in lowest common terms
            reduces 4/8 or .5 to 1/2 and return (1,2)
            '''
        if f == 0:
            return (0, 1)
        n = f
        d = 64 # start
        while n % 2 == 0:
            n /= 2
            d /= 2
        return (n, d)


    def __str__(self):
        ''' special cases if inches is zero or numerator is zero '''
        inches = self.u // 64
        left = self.u % 64
        if left == 0 or self.u == 0: # case of no fraction part or zero units
            return "%d" % ( inches )
        n, d = self._reduce(left)
        if inches > 0:
            return "%d %d/%d" % ( inches, n, d )
        else:
            return "%d/%d" % ( n, d )

    def __float__(self):
        return float(self.u/64.0)

    def __add__(self, other):
        return RulerUnit( 0, self.u + other.u, 64)

    def __eq__(self, other):
        return self.u == other.u

    def parts(self):
        return (self.u//64, (self.u % 64) / 64)

    # - * / > < >= <=
    # ADD YOUR NEW CODE AFTER THIS COMMENT
    def __sub__(self, other):
        return RulerUnit( 0, self.u - other.u, 64)

    def __mul__(self, other):
        return RulerUnit( 0, (self.u * other.u)/64, 64)

    def __truediv__(self, other):
        return RulerUnit( 0, (self.u / other.u),1)

    def __gt__(self, other):
        return self.u > other.u

    def __lt__(self, other):
        return self.u < other.u

    def __ge__(self, other):
        return self.u >= other.u

    def __le__(self, other):
        return self.u <= other.u



if __name__ == '__main__':

    x1 = RulerUnit(1,1,4)
    x2 = RulerUnit(2,1,4)
    x3 = x1 * x2
    print(x3, x3.u)
    n1 = RulerUnit(1,1,2)
    # print('n1:', n1)
    assert(n1.u == 96)  # test if constructor works

    assert(str(n1) == '1 1/2') # test if str works

    n2 = RulerUnit(0,1,3)
    # print('1/3 -> n2:', n2)
    assert(str(RulerUnit(0, 1, 3)) == "21/64") # test if constructor value between 64ths

    n3 = RulerUnit(0,1,4)
    # print('n3:', n3)

    n4 = n1 + n3
    # print('n4:', n4)

    assert( str(n4) == "1 3/4") # test add: 1 1/2 + 1/4 ->  1 3/4"

    assert( n4 == RulerUnit(1, 3, 4)) # test if add and equality work

    # print( 'n4.parts():', n4.parts())
    assert( n4.parts() == ( 1, 0.75)) # test parts work

    assert( str(RulerUnit( 2, 1, 4) - RulerUnit( 0, 1, 2)) == "1 3/4") # test subtract

    assert( str(RulerUnit( 2, 1, 4) / RulerUnit( 1, 1, 8)) == "2") # test divide
    assert( str(RulerUnit( 2, 3, 4) / RulerUnit( 0, 1, 2)) == "5 1/2") # test divide

    assert(str(RulerUnit(2, 1, 4) * RulerUnit(1, 1, 8)) == "2 17/32")  # test multiply
    assert(str(RulerUnit(2, 3, 4) * RulerUnit(0, 1, 2)) == "1 3/8")  # test multiply

    assert(     RulerUnit( 2, 1, 4) >= RulerUnit( 2, 1, 4)) == "true"
    assert( not RulerUnit( 2, 1, 4) >= RulerUnit( 2, 33, 64)) == "true"

    assert(     RulerUnit( 2, 1, 4) <= RulerUnit( 2, 1, 4)) == "true"
    assert( not RulerUnit( 2, 33, 64) <= RulerUnit( 2, 1, 4)) == "true"
    assert(     RulerUnit(2, 1, 4) <= RulerUnit(2, 33, 64)) == "true"

    assert(     RulerUnit( 2, 33, 64) > RulerUnit( 2, 1, 4)) == "true"
    assert( not RulerUnit(2, 1, 4) > RulerUnit(2, 1, 4)) == "true"
    assert( not RulerUnit( 2, 1, 4)  > RulerUnit( 2, 1, 4)) == "true"

    assert( not RulerUnit( 2, 33, 64) < RulerUnit( 2, 1, 4)) == "true"
    assert(     RulerUnit(2, 1, 4) < RulerUnit(2, 33, 64)) == "true"
    assert( not RulerUnit( 2, 1, 4)  < RulerUnit( 2, 1, 4)) == "true"




    print("*** PASSED ASSERTIONS\n *** make sure to run check_rulerunits.py for grading")

    draw()
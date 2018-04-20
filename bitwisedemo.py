def masktest(lhs, rhs):
    
    print("")
    print("====================================================================")
    print("LOOKING AT {} and {} ".format(lhs, rhs))
    print("")
    s = "The LHS is {} - the binary equivalent of which is : ".format(lhs) 
    print("{:>90} {:08b}".format(s, lhs ))
    s = "The RHS is {} - the binary equivalent of which is : ".format(rhs) 
    print("{:>90} {:08b}".format(s, rhs ))
    print("")

    s = "When you 'bitwise and' the two values you get : {} - the binary equivalent of which : ".format(lhs & rhs)
    print("{:>90} {:08b}".format(s, lhs & rhs))

    s = "When you 'bitwise or ' the two values you get : {} - the binary equivalent of which : ".format(lhs | rhs)
    print("{:>90} {:08b}".format(s, lhs | rhs))


    s = "When you 'bitwise xor' the two values you get : {} - the binary equivalent of which : ".format(lhs ^ rhs)
    print("{:>90} {:08b}".format(s, lhs ^ rhs))

    print("")
    print("====================================================================")
    print("")

if __name__ == "__main__":
    masktest(1, 3)
    masktest(10, 12)
    masktest(8, 4)


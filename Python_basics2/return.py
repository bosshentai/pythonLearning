def sum(num1,num2):
    return num1 + num2


def sum1(num1,num2):
    def anotherFunc(n1,n2):
        return n1 + n2 
    return anotherFunc(num1,num2)


total = sum(10,5)
print(sum(10,total))

total1 = sum1(10,20)
print(total1)
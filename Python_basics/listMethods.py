basket = [1,2,3,4,5]
#len()
print(len(basket))


#adding
# basket.append(100)
# newList =  basket

# basket.insert(5,100)
# newList = basket

#basket.extend([100,101])
newList = basket.extend([100])
#print(basket)
#print(newList)

#removing
#basket.pop()
#print(basket)

#basket.remove(4)
#print(basket)

# # newList = basket.clear()
# print(basket)
basket2 = ['a','f','b','c','d','e']
#print(basket2.index('d'))
#print( 'd' in basket2 )
print(basket2.count('d'))


# order 
basket2.sort()
basket2.reverse()
print(basket2)
#print(len(basket2))
print(basket2[::-1])
#print(sorted(basket2))

print(list(range(100)))


# list unpacking 
a,b,c, *other = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)
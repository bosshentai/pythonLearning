# map, filter, zip, and reduce 

# def multiply_by2(li):
#     #new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list



myList = [1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2,myList)))
print(myList)
#print(multiply_by2([1,2,3]))
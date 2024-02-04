
# Функции высщего порядка!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def doub (list_1):
#     res=list()
#     for i in list_1:
#         if i % 2==0:
#             res.append((i, i*i))
#     return res

# ..............................................................

list_1 = [1, 2, 3, 5 ,8 ,15, 23, 38]
# print (list_1)
# print (doub(list_1))              


# def select (f, col):              # = MAP 
#     return[f(x) for x in col]

# def where (f, col):                # fILTER
#     return[x for x in col if f(x) ]



res =map (int, list_1)
res = filter(lambda x: x%2 ==0, res)
res = list (map (lambda x: (x, x*x), res))
print (res)

# MAP MAP  MAP MAP  MAP MAP  MAP MAP  MAP MAP  MAP MAP  MAP MAP  MAP MAP  MAP MAP 

# list_1 = [x for x in range (1,20)]
# print (list_1)

# list_1=list(map(lambda x: x+10, list_1))
# print (list_1)


# #............................................
# data = '12 13 44 54 44'
# # print (data)
# # data = data.split()
# # print (data)

# data = list(map(int, data.split()))
# print(data)


# FILTER FILTER FILTER FILTER FILTER FILTER FILTER FILTER FILTER FILTER FILTER 
# FILTER (логическое выражение (true/false), переменная)
# data = [5, 15, 14, 44, 3, 34, 54, 55, 56]
# res = list(filter(lambda x: x%10 ==5, data))
# print (res)
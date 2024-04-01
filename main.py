# 1.
# my_list = ['MOSCOW','BISHKEK','ALMATY','BERLIN','ANKARA']
# def make_to_lower(my_list):
#     return my_list.lower()
# new_list = list(map(lambda lst: lst.lower(),my_list))
# print(new_list)

# 2.
my_list = [4,3,6,8,9,7,1,2,34,5,56,76]
new_list = list(filter(lambda lst: (lst%2==0),my_list))
new_list2 = list(map(lambda pow: pow**3,new_list))
print(new_list)
print(new_list2)
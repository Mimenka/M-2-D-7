my_list = ['MOSCOW','BISHKEK','ALMATY','BERLIN','ANKARA']
def make_to_lower(my_list):
    return my_list.lower()
new_list = list(map(lambda lst: lst.lower(),my_list))
print(new_list)
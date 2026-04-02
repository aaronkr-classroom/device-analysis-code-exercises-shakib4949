#LIST
my_list1= [1,2, 'a', "Hello"]
my_list2= [1,'a', 3,67]
my_list1[1]=67
my_list2.append(89)

# Tuple
my_t1 = ('SHAKIB', 1990)
my_t23 = (2005, 1990)
print(my_t23[0])
my_t23= (100,1000)
my_list1.append("Hi")

#Dictonary
my_dic = {
    "name": "SHAKIB",
    "year": 1990,
    "country": "Bangladesh",
    "my_list": my_list1   
}

print(my_dic)

my_dic['tup']=(1,4,5)
my_dic['name']= "Ryan"


#Set
set1 = {1, 2, 'a', "Hello"}
set2 = {2, 3, 'b', "Hello"}

union_set = set1 | set2
intersection_set = set1 & set2
diff_set = set1 - set2
sym_diff_set = set1- set2

print('u', union_set)
print('i', intersection_set)
print('d', diff_set)
print('sd', sym_diff_set)




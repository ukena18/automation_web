# def find_min(arr):
#     try:
#         arr_min = arr[0]
#     except:
#         return None
#     for num in range(len(arr)):
#         if arr[num]<arr_min:
#             arr_min = num
#     return arr_min, arr[arr_min]
#
#
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(min_index+1,len(arr)):
#             if arr[min_index]< arr[j]:
#
#
#
# my_arr = [13,23,32,53,3,2]
# print(find_min(my_arr))


#
#
# def selection_sort(arr):
#
#     size = len(arr)
#
#     for i in range(size-1 ):
#         min_index = i
#         for j in range(min_index+1,size):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index]  = arr[min_index], arr[i]
#     return arr
#
# my_arr = [13,23,32,53,3,2]
# print(selection_sort(my_arr))


#
# def section_sort(arr):
#     for i in range(len(arr)-1):
#         check_index = i
#
#         for j in range(check_index+1,len(arr)):
#             if arr[j]<arr[i]:
#                 check_index = j
#         arr[i] , arr[check_index ] = arr[check_index], arr[i]
#
#     return arr
#
#
# arr = [1,6,34,4,5]
# print(section_sort(arr))

def sort_dict(arr):

    for i in range(len(arr)-1):
        check_index = i
        for j in range(check_index+1,len(arr)):
            if arr[j]["First Name"]<arr[check_index]["First Name"]:
                check_index = j
            if arr[j]["First Name"] == arr[check_index]["First Name"]:
                    if arr[j]["Last Name"] < arr[check_index]["Last Name"]:
                            check_index = j


        arr[i], arr[check_index] = arr[check_index], arr[i]
    return arr

given_list = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

print(sort_dict(given_list))

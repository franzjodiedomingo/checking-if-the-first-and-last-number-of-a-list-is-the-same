# True if the first and last statements are the same.
# False, otherwise.

def check_first_and_last_equal(test_list):
    
    if len(test_list) <= 1:
        return False
    return test_list[0] == test_list[-1]

test_list1 = [1,2,3,1]
test_list2 = [1,2,3,4]

print(f"Given List: {test_list1}")
print("result is", check_first_and_last_equal(test_list1))
print(f"numbers_y: {test_list2}, {check_first_and_last_equal(test_list2)}")
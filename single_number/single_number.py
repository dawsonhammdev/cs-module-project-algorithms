'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # we need to return the number that doesn't show up twice.
    # we could use a for loop to iterate through the array but need 
    # for x in arr:
    #     if x != x:
    #         print(x)
    # a way to make sure there isn't a duplicate.

    # a set in python can have no duplicates.
    # so if we compare the len of a set and the original list we should 
    # be able to find the duplicate.
    # if arr.Count(arr[0]) == len(set(arr)):
    #     return True
    # else:
    #     return False

    ans = arr[0]
    for i in range(1,len(arr)):
        ans ^= arr[i]
    return ans


    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
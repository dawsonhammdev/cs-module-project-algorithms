'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # we can use insertion sort to move the zeros to the right side
    # we need to compare the numbers and if not zero the move left
    for i in range(1, len(arr)): 
        key = arr[i]
        


    return arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
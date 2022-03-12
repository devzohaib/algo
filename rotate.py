
# Rotate the list
def rotate(arr):

    # copy
    arr_copy = arr[:]
    
    # save the last element
    x = arr[-1]

    for i in range(len(arr) - 1 , 0, -1):

        # shift the elements from [current index -1] to  [current index]
        # move [i-1] to [i]
        arr[i] = arr[i - 1]
    
    # set the first element to the saved last element
    arr[0] = x

    print("Before: ", arr_copy)
    print("After : ", arr)

    return None

if __name__ == '__main__':

    # input List 
    arr = [1,2,3,4,5,6,7]

    # objective is to Rotate list
    # output List  = [7,2,3,4,5,6,1]

    rotate(arr)

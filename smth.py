array = [2, 1, 5, 1, 3, 2]

def sub_array(array, k):
    window_sum = 0
    max_window_sum = 0

    for i in range(k):
        window_sum += array[i]

    max_window_sum = window_sum
    
    for i in range(k, len(array)):
        window_sum += array[i] - array[i - k]
        max_window_sum = max(window_sum, max_window_sum)

    
    return max_window_sum


    
        

    

print(sub_array(array, 3))
        
import queue

print(20*'=')
print(' DIVIDE AND CONQUER')
print(20*'=')

max_number = int(input('How many numbers do we have = '))
num_queue = queue.Queue(maxsize = max_number)
num_arr = []

for n in range(0,max_number):
    num_input = int(input('Input numbers [' + str(n+1) + '] = '))
    num_arr.append(num_input)

print('')
print(35*'-')
print(' ARRAY [BEFORE DIVIDE AND CONQUER]')
print(35*'-')
print(num_arr)

num_queue.put(num_arr)
arr_mid = []

while(num_queue.qsize() > 0):
    arr_check = num_queue.get() #get from queue and delete from it
    if len(arr_check) > 0:
        mid_idx = len(arr_check)//2 #// floor division
        mid = arr_check[mid_idx]
        arr_left = arr_check[0:mid_idx]
        arr_right = arr_check[mid_idx+1:]
        arr_mid.append(mid)
        num_queue.put(arr_left)
        num_queue.put(arr_right)
    
print('')
print(34*'-')
print(' ARRAY [AFTER DIVIDE AND CONQUER]')
print(34*'-')  
print(arr_mid)

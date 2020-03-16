import queue

print(20*'=')
print(' DIVIDE AND CONQUER')
print(20*'=')

x = int(input('maximum = '))
num_queue = queue.Queue(maxsize = x)
num_arr = []

for a in range(0,x):
    num_arr.append(int(input('Input numbers = ')))

print('')
print(num_arr)

num_queue.put(num_arr)
arr_mid = []

while(num_queue.qsize() > 0):
    arr_check = num_queue.get() #get from queue and delete from it
    if len(arr_check) >= 0:
        mid_idx = len(arr_check)//2 #// floor
        mid = arr_check[mid_idx]
        arr_left = arr_check[0:mid_idx]
        arr_right = arr_check[mid_idx+1:]
        arr_mid.append(mid)
        num_queue.put(arr_left)
        num_queue.put(arr_right)
    
        
print('')  
print(arr_mid)


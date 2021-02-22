import time
time_lapsed_ini = time.perf_counter()
arr = ['cavalo']
arr2 = ['uva', 'pessego', 'melancia', 'banana']

for i in range(len(arr)):
    if arr[i] == 'cavalo':
        print('Cavalo has founded')

for i in range(len(arr2)):
    if arr2[i] == 'melancia':
        print('melancia has founded')

s = 0
for i in range(1, 1000000):
    s += 1
print(s)

# return seconds
time_lapsed_final = time.perf_counter()

# return nanoseconds
# time_lapsed = time.thread_time_ns()

print(time_lapsed_final - time_lapsed_ini)

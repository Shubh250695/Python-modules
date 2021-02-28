import time

fruits = ['banana', 'grapes']
print('Initial queue')
print(fruits)

tic = time.perf_counter()

# enqueue 1
fruits.append('mango')
print('\nAfter enqueue 1 - mango')
print(fruits)
toc = time.perf_counter()
print(f"{toc - tic:0.4f} seconds")

#enqueue 2
fruits.append('orange')
print('\nAfter enqueue 2 - orange')
print(fruits)
toc = time.perf_counter()
print(f"{toc - tic:0.4f} seconds")

# dequeue 1
first_item = fruits.pop(0)
print('\nAfter dequeue 1 - first item of previous queue')
print(fruits)
toc = time.perf_counter()
print(f"{toc - tic:0.4f} seconds")

# dequeue 2
first_item = fruits.pop(0)
print('\nAfter dequeue 2 - first item of previous queue')
print(fruits)
toc = time.perf_counter()
print(f"{toc - tic:0.4f} seconds")
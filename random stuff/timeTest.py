import time 

def snippet_1():
    i = 0 
    steps = 0 
    while i <=1000000:
        if i % 2== 0:
            pass
        i += 1
        steps += 1
    return steps 


def snippet_2():
    i = 0
    steps = 0 

    while i <= 1000000:
        i += 2 
        steps += 1
    return steps
        

start = time.time()
steps_1 = snippet_1()
end = time.time()
time1 = end - start

start = time.time()
steps_2 = snippet_2()
end = time.time()
time2 = end - start

print(f"Snippet 1 time taken is {time1} seconds, steps taken are {steps_1}")
print(f"Snippet 2 time taken is {time2} seconds, steps taken are {steps_2}")
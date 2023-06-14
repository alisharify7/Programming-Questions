import time


global steps
steps = 0

print("[G] Generating List ")
test_arr =  [x for x in range(1,1_00_000_000+1)]
print("[EG] List generated successfully")


def bin_search(arr, tar, end, start=0):
    """ 
        arr = array for search
        tar = target number for search
        start = location for start
        end = end location of search <len(arr)>
    """
    global steps
    # print(f"start: {start}, end:{end}")
    for each in range(start, end):
        middle = (start+end)//2
        if arr[middle] > tar:
            steps += 1
            return bin_search(arr=arr, tar=tar, start=start, end=middle)
        elif arr[middle] < tar:
            steps += 1
            return bin_search(arr=arr, tar=tar, start=middle, end=end)
        else:
            return [f"Found :{arr[middle]} Using Binary algorithm, in {steps} steps", time.time() * 1000]


def linear_search(arr, tar):
    start = time.time() * 1000
    for index,value in enumerate(arr):
        if value == tar:
            end=(time.time() * 1000)
            return f"Found {value} Using linear algorithm, in {index+1} steps, {end - start} ms"




print(f"[S] Search Started!")
start = time.time() * 1000
result = bin_search(arr=test_arr, tar=9_9999_999, start=0, end=len(test_arr))
print(result[0], f"in {result[-1] - start} ms")


result = linear_search(arr=test_arr,  tar=9_9999_999)
print(result)
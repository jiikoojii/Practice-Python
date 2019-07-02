import time
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Give me a number: ")
start_time = time.time()
while n != 1:
    n = collatz(int(n))
elapsed_time = time.time() - start_time
print("It took", elapsed_time, " seconds to reach number 1")
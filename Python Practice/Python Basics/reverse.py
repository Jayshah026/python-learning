n = int(input())

nums = list(map(int, input().split()))

print(f"Here is the original numbers you have given {nums}")

nums.reverse()

print(*nums, " Here is the reverse of the numbers")
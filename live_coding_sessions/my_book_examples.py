# count = 0
# while not False:
#     print(count)
#     count += (2)
#     if count >= (10):
#         break
# print("ended")

# for num in range(1, ):
#     if num == 5:
#         continue
#     print(num)
#     if num == 8:
#         break
# print("see you")

# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print("looe stoped")


# secret_number = 7

# guess_count = 0
# guess = 0

# while guess != secret_number:
#   guess_count += 1
#   guess = float(input("Guess a number between 1 and 10: "))

# print(f"You guessed it in {guess_count} tries!")

# outer_count = 5

# while outer_count > 0:
#   # Outer loop controls the number of times the inner loop runs
#   inner_count = 1
#   while inner_count <= outer_count:
#     # Inner loop repeats for each outer loop iteration
#     print(inner_count, end=" ")
#     inner_count += 1
#   print()  # Move to a new line after each outer loop iteration
#   outer_count -= 1

# rows = 10

# for i in range(1, rows + 1):
#   # Outer loop controls the number of rows
#   for j in range(1, i + 2):
#     # Inner loop prints asterisks for each row
#     print("*", end="")
#   print()  # Move to a new line after each row of asterisks

# row = 5
# for i in range(1, row +1):
#   for j in range(1, i + 1):
#     print( "*", end= " ")
#   print()
#   row += 4

size = int(input("Enter the size of the pattern:."))
if size <= 0:
    print("please enter a positive inter.")
    

row = 0
while row < size:

    for _ in range(size):
        print("*", end="")
    print()
    row += 1
# def add_move(moves):
#     moves.append('s')
# moves = []
# print(moves)
# add_move(moves)
# print(moves)


def elementInArray(arr, x):
    for i in arr:
        for j in i:
            if j == x:
                print('Element found')
                break
            else:
                print(j)

        # If the inner loop completes without encountering
        # the break statement then the following else
        # block will be executed and outer loop will
        # continue to the next value of i:
        else:
            continue

        # If the inner loop terminates due to the
        # break statement, the else block will not
        # be executed and the following break
        # statement will terminate the outer loop also:
        print('e')
        continue



# Driver Code:
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 4
elementInArray(arr, x)
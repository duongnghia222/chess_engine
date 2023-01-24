# def add_move(moves):
#     moves.append('s')
# moves = []
# print(moves)
# add_move(moves)
# print(moves)

#
# def elementInArray(arr, x):
#     for i in arr:
#         for j in i:
#             if j == x:
#                 print('Element found')
#                 break
#             else:
#                 print(j)
#
#         # If the inner loop completes without encountering
#         # the break statement then the following else
#         # block will be executed and outer loop will
#         # continue to the next value of i:
#         else:
#             continue
#
#         # If the inner loop terminates due to the
#         # break statement, the else block will not
#         # be executed and the following break
#         # statement will terminate the outer loop also:
#         print('e')
#         continue


#
# # Driver Code:
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# x = 4
# elementInArray(arr, x)




# import pygame
#
# pygame.init()
#
# # Set the window size and caption
# size = (800, 600)
# caption = "Pop-up Example"
# pygame.display.set_caption(caption)
# screen = pygame.display.set_mode(size)
# # Create the message surface
# message = "Hello, World!"
# font = pygame.font.Font(None, 36)
# text_surface = font.render(message, True, (255, 255, 255))
#
# # Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     # Clear the screen
#     screen.fill((0, 0, 0))
#     # Draw the message surface
#     screen.blit(text_surface, (400, 300))
#     # Update the display
#     pygame.display.update()
#
# pygame.quit()


####################################
# go backward when removing element #
####################################
my_list = [1, 2, 3, 3, 4, 5]
element_to_remove = (3, 4)

for i in my_list:
    if i in element_to_remove:
        my_list.remove(i)

print(my_list)  # [1, 2, 4, 5]
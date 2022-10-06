# # PROGRAM STARTS HERE!
import sys
import time
import os
from source import main_menu
from source import access_func as af

# while True:
#     try:
#         main_menu.menu1()
#     except ValueError:
#         os.system('clear')
#         print("Input error, please enter only integers")
#         print()
#         print()
#         print("Main menu will be loaded shortly...")
#         time.sleep(1)
        
        
#     except Exception as e:
#         os.system('clear')
#         print('An error occurred: ' + str(e))
#         print()
#         print()
#         print("Main menu will be loaded shortly...")
#         time.sleep(1)

#once its all good, you can uncomment the top and comment the bottom one
if __name__ == "__main__":   
    main_menu.menu1()
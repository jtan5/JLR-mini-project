# def printdynamic(a, question, art, add_option=0):
#     # clear() - using replit
#     os.system('clear')
#     print(art)
#     print(question)
#     for index, val in enumerate(a):
#         print(f"[{index}] - {val}")
#     if add_option == 1:
#         print("99 - Return to main menu")

#     choice2 = int(input("Please enter a valid option as listed above\n"))
#     if (choice2) < len(a):
#         selecteditem = a[choice2]
#         return choice2, len(a), selecteditem
#     else:
#         return choice2, len(a), "Invalid selection"
from unittest.mock import patch
import os
import sys
current_path = os.getcwd()
sys.path.append(current_path)
print(sys.path)
    
    
from source.main_menu import printdynamic
@patch("builtins.input")
def test_print_dynamic_common_case(mock_input):
    #assemble
    dummy_list =["Water","Fire","Earth","Wind"]
    mock_input.return_value = 2
    expected = (2,len(dummy_list),dummy_list[mock_input()])
    #act
    result = printdynamic(dummy_list,"dummy_question","art")
    #assert
    assert result ==expected

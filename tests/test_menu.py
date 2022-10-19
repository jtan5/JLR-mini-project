from unittest.mock import patch
from unittest.mock import Mock
from unittest import TestCase
import os
import sys
current_path = os.getcwd()
sys.path.append(current_path)
print(sys.path)
    
    
from source import menu, functions
from source import access_func as af

    
    
###################################################################################################
##     MAIN MENU
###################################################################################################
@patch("builtins.input", side_effect = [7,2])
@patch("source.menu.courier_menu")
def test_main_menu(mock_function,mock_input):
    #assemble
    expected = 1
    #act
    menu.main_menu()
    #result = mock_function()
    print()
    print()

    print(f"mock_function: {mock_function.call_count}")
    print()
    print()
    assert mock_function.call_count == expected
    
###################################################################################################
##     PRODUCT MENU
###################################################################################################
@patch("builtins.input", side_effect = [7,0])
@patch("source.menu.main_menu")
def test_product_menu(mock_function,mock_input):
    #assemble
    expected = 1
    #act
    menu.product_menu()
    #result = mock_function()
    print()
    print()

    print(f"mock_function: {mock_function.call_count}")
    print()
    print()
    assert mock_function.call_count == expected
    
###################################################################################################
##     PRODUCT MENU
###################################################################################################
@patch("builtins.input", side_effect = [7,0])
@patch("source.menu.main_menu")
def test_courier_menu(mock_function,mock_input):
    #assemble
    expected = 1
    #act
    menu.courier_menu()
    #result = mock_function()
    print()
    print()

    print(f"mock_function: {mock_function.call_count}")
    print()
    print()
    assert mock_function.call_count == expected
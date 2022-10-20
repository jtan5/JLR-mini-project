from unittest.mock import patch
from unittest.mock import Mock
from unittest import TestCase
import os
import sys
current_path = os.getcwd()
sys.path.append(current_path)
print(sys.path)
from source import order_menu

###################################################################################################
##     TEST GET CUSTOMER ID
###################################################################################################
@patch("builtins.input", side_effect = [7,4,1])
@patch("source.order_menu.new_customer_entry")
def test_courier_menu(mock_function,mock_input):
    #assemble
    mock_function.return_value = "9880"
    expected = "9880"
    #act
    actual = order_menu.get_customer_id()
    #result = mock_function()
    print()
    print()
    print("1 for Yes to new customer")
    print()
    print()
    assert actual ==expected
    
###################################################################################################
##     NEW CUSTOMER ENTRY
###################################################################################################
@patch("builtins.input", side_effect = ["Dummyname","20 Dummy Road", "2020", "1"])
@patch("source.order_menu.af.get_new_customer_id")
@patch("source.order_menu.af.insert_customer")
def test_new_customer_entry(mock_function_1,mock_function_2,mock_input):
    #assemble
    mock_function_1.return_value = ("Dummyname","20 Dummy Road", "2020", "West Midlands")
    mock_function_2.return_value = 8888
    expected = 8888
    #act
    actual = order_menu.new_customer_entry()
    #result = mock_function()
    print()
    print()
    print()
    print()
    assert actual ==expected
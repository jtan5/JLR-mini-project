
from unittest.mock import patch
from unittest import TestCase
import os
import sys
current_path = os.getcwd()
sys.path.append(current_path)
print(sys.path)
    
    
from source import menu

@patch("builtins.input")
def test_print_dynamic_common_case(mock_input):
    #assemble
    dummy_list =["Water","Fire","Earth","Wind"]
    mock_input.return_value = 2 #Earth
    expected = (2,len(dummy_list),dummy_list[mock_input()])
    #act
    result = menu.print_dynamic(dummy_list,"dummy_question","art")
    #assert
    assert result ==expected


@patch("builtins.input")
def test_print_dynamic_edge_case(mock_input):
    #assemble
    dummy_list =["Water","Fire","Earth","Wind"]
    mock_input.return_value = 3 #Earth
    expected = (3,len(dummy_list),dummy_list[mock_input()])
    #act
    result = menu.print_dynamic(dummy_list,"dummy_question","art")
    #assert
    assert result ==expected
    

# @patch("builtins.input")
# @patch("builtins.print")
# def test_print_dynamic_corner_case(mock_print,mock_input):
#     #assemble
#     dummy_list =["Water","Fire","Earth","Wind"]
#     mock_input.return_value = "a" #Earth
#     expected = "Menu will load shortly..."
#     #act
#     result = print_dynamic(dummy_list,"dummy_question","art")
#     #assert
#     mock_print.assert_called_with(expected)


class RecursionTest(TestCase):
    def setUp(self):
        self.counter = 0  # counts the number of calls

    def checked_fct(self, fct):  # wrapper function that increases a counter on each call
        def wrapped(*args, **kwargs):
            self.counter += 1
            return fct(*args, **kwargs)

        return wrapped

    def test_recursion(self):
        # replace your function with the checked version
        with mock.patch('my_module.test01',
                        self.checked_fct(my_module.test01)):  # assuming test01 lives in my_module.py
            result = my_module.test01('444')  # call the function
            self.assertEqual(result, 3)  # check for the correct result
            self.assertGreater(self.counter, 1)  # ensure the function has been called more than once
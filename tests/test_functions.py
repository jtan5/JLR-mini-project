
from unittest.mock import patch
from unittest import TestCase
import os
import sys
current_path = os.getcwd()
sys.path.append(current_path)
print(sys.path)
    
    
from source import menu, functions, access_func

####################################################################################################
###     SELECTION CATCHER
####################################################################################################
@patch("builtins.input")
def test_selection_catcher_common_case(mock_input):
    #assemble
    dummy_list =["Water","Fire","Earth","Wind"]
    mock_input.return_value = 2 #Earth
    expected = 2
    #act
    result = functions.selection_catcher(dummy_list,"dummy_question","art")
    #assert
    assert result ==expected


@patch("builtins.input")
def test_selection_catcher_edge_case(mock_input):
    #assemble
    dummy_list =["Water","Fire","Earth","Wind"]
    mock_input.return_value = 3 #Earth
    expected = 3
    #act
    result = functions.selection_catcher(dummy_list,"dummy_question","art")
    #assert
    assert result ==expected
    
@patch("builtins.input", side_effect = [4,5,6,7,3])
def test_selection_catcher_corner_case(mock_input):
    #assemble
    dummy_list =["Water","Fire","Earth","Wind"]
    mock_input.return_value = 3 #Earth
    expected = 3
    #act
    result = functions.selection_catcher(dummy_list,"dummy_question","art")
    #assert
    assert result ==expected

####################################################################################################
###     SELECTION CATCHER DICT
####################################################################################################
@patch("builtins.input")
def test_selection_catcher_dict_common_case(mock_input):
    #assemble
    dummy_list =[{"element1":"Water"},{"element2":"Fire"},{"element3":"Earth"},{"element4":"Wind"}]
    mock_input.return_value = 2 #Earth
    expected = 2
    #act
    result = functions.selection_catcher_dict(dummy_list,"dummy_question","art")
    #assert
    assert result ==expected


@patch("builtins.input")
def test_selection_catcher_dict_edge_case(mock_input):
    #assemble
    dummy_list =[{"element1":"Water"},{"element2":"Fire"},{"element3":"Earth"},{"element4":"Wind"}]
    mock_input.return_value = 3 #Earth
    expected = 3
    #act
    result = functions.selection_catcher_dict(dummy_list,"dummy_question","art")
    #assert
    assert result ==expected
    
@patch("builtins.input", side_effect = [4,5,6,7,3])
def test_selection_catcher_dict_corner_case(mock_input):
    #assemble
    dummy_list =[{"element1":"Water"},{"element2":"Fire"},{"element3":"Earth"},{"element4":"Wind"}]
    expected = 3
    #act
    result = functions.selection_catcher_dict(dummy_list,"dummy_question","art")
    #assert
    assert result ==expected

####################################################################################################
###     PRICE CATCHER
####################################################################################################
@patch("builtins.input", side_effect = ["",0,2.334])
def test_price_catcher_common_case(mock_input):
    #assemble
    expected = 2.33
    #act
    result = functions.price_catcher("dummy question")
    #assert
    assert result ==expected

####################################################################################################
###     BLANK CATCHER
####################################################################################################
@patch("builtins.input", side_effect = ["",0,"watermelon"])
def test_blank_catcher_common_case(mock_input):
    #assemble
    expected = "watermelon"
    #act
    result = functions.blank_catcher("dummy question")
    #assert
    assert result ==expected
    

####################################################################################################
###     INT CATCHER
####################################################################################################
@patch("builtins.input", side_effect = ["",0,"watermelon",9])
def test_int_catcher_common_case(mock_input):
    #assemble
    expected = 9
    #act
    result = functions.int_catcher("dummy question")
    #assert
    assert result ==expected
    
####################################################################################################
###     PHONE CATCHER
####################################################################################################
@patch("builtins.input", side_effect = ["24 2332 2232", "07 999 444 666", "+61433366333","+447 999 444 666"])
def test_phone_catcher_common_case(mock_input):
    #assemble
    expected = "+61433366333" #added aussie number "+447999444666"
    #act
    result = functions.phone_catcher()
    #assert
    assert result == expected

####################################################################################################
###     SERVICING AREA CATCHER
####################################################################################################
@patch("builtins.input", side_effect = [8,5,"Not now",2])
def test_servicing_area_catcher_common_case(mock_input):
    #assemble
    #dummy_list =["Water","Fire","Earth","Wind"]
    #mock_input.return_value = 2 #Earth
    expected = "District-9"
    #act
    result = functions.servicing_area_catcher()
    #assert
    assert result ==expected
####################################################################################################
###     PRINT_DYNAMIC_LIST
####################################################################################################
@patch("builtins.print")
def test_print_dynamic_list(mock_print):
    #assemble
    dummy_list =["Water","Fire","Earth","Wind"]
    expected_print = "[3] - Wind"
    #act
    functions.print_dynamic_list(dummy_list)
    #assert
    mock_print.assert_called_with(expected_print)
###################################################################################################
##     PRINT_DICT
###################################################################################################

@patch("builtins.print")
def test_print_dict(mock_print):
    #assemble
    #dummy_list =[{"element1":"Water0","element2":"Fire0","element3":"Earth0"},{"element1":"Water1","element2":"Fire1","element3":"Earth1"},{"element1":"Water2","element2":"Fire2","element3":"Earth2"},{"element1":"Water3","element2":"Fire3","element3":"Earth3"}]
    dummy_list ={"element1":"Water0","element2":"Fire0","element3":"Earth0"}
    expected_print = '       element1:Water0              \n\n       element2:Fire0               \n\n       element3:Earth0              \n'
    #act
    functions.print_dict(dummy_list)
    #assert
    mock_print.assert_called_with(expected_print)
    

####################################################################################################
###     PRINT_LIST_OF_DICT
####################################################################################################
# @patch("builtins.print")
# def test_print_list_of_dict(mock_print):
#     #assemble
#     dummy_list =[{"element1":"Water0","element2":"Fire0","element3":"Earth0"},{"element1":"Water1","element2":"Fire1","element3":"Earth1"},{"element1":"Water2","element2":"Fire2","element3":"Earth2"},{"element1":"Water3","element2":"Fire3","element3":"Earth3"}]
#     #dummy_list ={"element1":"Water0","element2":"Fire0","element3":"Earth0"}
#     expected_print = "element1    element2    element3\n----------  ----------  ----------\nWater0      Fire0       Earth0\nWater1      Fire1       Earth1\nWater2      Fire2       Earth2\nWater3      Fire3       Earth3"
#     #act
#     functions.print_list_of_dict(dummy_list)
#     #assert
#     mock_print.assert_called_with(expected_print)
####################################################################################################
###     PRINT_LIST_OF_DICT
####################################################################################################
@patch("builtins.print")
def test_print_list_of_dict(mock_print):
    #assemble
    dummy_list =[{"element1":"Water0","element2":"Fire0","element3":"Earth0"},{"element1":"Water1","element2":"Fire1","element3":"Earth1"},{"element1":"Water2","element2":"Fire2","element3":"Earth2"},{"element1":"Water3","element2":"Fire3","element3":"Earth3"}]
    #dummy_list ={"element1":"Water0","element2":"Fire0","element3":"Earth0"}
    expected_print = "element1    element2    element3\n----------  ----------  ----------\nWater0      Fire0       Earth0\nWater1      Fire1       Earth1\nWater2      Fire2       Earth2\nWater3      Fire3       Earth3"
    #act
    functions.print_list_of_dict(dummy_list)
    #assert
    mock_print.assert_called_with(expected_print)
####################################################################################################
###     PRINT_LIST_OF_DICT_SELECTION
####################################################################################################
@patch("builtins.print")
def test_print_list_of_dict_selection(mock_print):
    #assemble
    dummy_list =[{"element1":"Water0","element2":"Fire0","element3":"Earth0"},{"element1":"Water1","element2":"Fire1","element3":"Earth1"},{"element1":"Water2","element2":"Fire2","element3":"Earth2"},{"element1":"Water3","element2":"Fire3","element3":"Earth3"}]
    #dummy_list ={"element1":"Water0","element2":"Fire0","element3":"Earth0"}
    expected_print = '[ 3] ->        element1:Water3                     element2:Fire3                      element3:Earth3              '
    #act
    functions.print_list_of_dict_selection(dummy_list)
    #assert
    mock_print.assert_called_with(expected_print)
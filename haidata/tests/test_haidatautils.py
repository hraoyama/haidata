# using pytest; from the anaconda command line in the parent directory : py.test -v tests/

import sys, os

# this places the test file directory in the path such that we can run the test from command line
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath)
sys.path.insert(0, myPath + '/../')
sys.path.insert(0, myPath + '/../config')

from haidatautils import *


def test_int_list_to_element_list():

    reference_word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    input_string1 = "5"
    input_string2 = "0:5"
    input_string3 = "0,1,5:7"
    input_string4 = "0:26"
    input_string5 = "24:26,4:6,8,0"
    input_string6 = "24:26,4:6,8,0,25,10:12"

    assert int_list_to_element_list(input_string1, reference_word) == "F"
    assert int_list_to_element_list(input_string2, reference_word) == "ABCDE"
    assert int_list_to_element_list(input_string3, reference_word) == "ABFG"
    assert int_list_to_element_list(input_string4, reference_word) == reference_word
    assert int_list_to_element_list(input_string5, reference_word) == "AEFIYZ"
    assert int_list_to_element_list(input_string6, reference_word) == "AEFIKLYZ"

    reference_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                      "T", "U", "V", "W", "X", "Y", "Z"]
    input_string1 = "5"
    input_string2 = "0:5"
    input_string3 = "0,1,5:7"
    input_string4 = "0:26"
    input_string5 = "24:26,4:6,8,0"
    input_string6 = "24:26,4:6,8,0,25,10:12"

    assert int_list_to_element_list(input_string1, reference_list) == ["F"]
    assert int_list_to_element_list(input_string2, reference_list) == ["A", "B", "C", "D", "E"]
    assert int_list_to_element_list(input_string3, reference_list) == ["A", "B", "F", "G"]
    assert int_list_to_element_list(input_string4, reference_list) == reference_list
    assert int_list_to_element_list(input_string5, reference_list) == ["A", "E", "F", "I", "Y", "Z"]
    assert int_list_to_element_list(input_string6, reference_list) == ["A", "E", "F", "I", "K", "L", "Y",
                                                                                    "Z"]

    pass


def test_element_list_to_int_list():

    reference_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                      "T", "U", "V", "W", "X", "Y", "Z"]

    assert element_list_to_int_list(["F"], reference_list) == [5]
    assert element_list_to_int_list(["A", "B", "C", "D", "E"], reference_list) == list(range(5))
    assert element_list_to_int_list(["A", "B", "F", "G"], reference_list) == [0, 1, 5, 6]
    assert element_list_to_int_list(reference_list, reference_list) == list(range(26))
    assert element_list_to_int_list(["A", "E", "F", "I", "Y", "Z"], reference_list) == [0, 4, 5, 8, 24, 25]
    assert element_list_to_int_list(["A", "E", "F", "I", "K", "L", "Y", "Z"], reference_list) == [0, 4, 5,
                                                                                                               8, 10,
                                                                                                               11,
                                                                                                               24, 25]

    pass


def test_mixed_list_to_int_list():

    reference_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                      "T", "U", "V", "W", "X", "Y", "Z"]

    assert mixed_list_to_int_list("F", reference_list) == [5]
    assert mixed_list_to_int_list(r'A, B, C, D, E', reference_list) == list(range(5))
    assert mixed_list_to_int_list(r'A, B, F, G', reference_list) == [0, 1, 5, 6]
    assert mixed_list_to_int_list(r'A, E, F, I, Y, Z', reference_list) == [0, 4, 5, 8, 24, 25]
    assert mixed_list_to_int_list(r'A, E, F, I, K, L, Y, Z', reference_list) == [0, 4, 5, 8, 10, 11, 24,
                                                                                              25]
    assert mixed_list_to_int_list("5", reference_list) == [5]
    assert mixed_list_to_int_list(r'0:5', reference_list) == list(range(5))
    assert mixed_list_to_int_list(r'0:2, 5:7', reference_list) == [0, 1, 5, 6]
    assert mixed_list_to_int_list(r'0, 4, 5, 8, 24:26', reference_list) == [0, 4, 5, 8, 24, 25]
    assert mixed_list_to_int_list(r'0, 4:6, 8, 10:12, 24, 25', reference_list) == [0, 4, 5, 8, 10, 11, 24,
                                                                                              25]

    assert mixed_list_to_int_list(r'A, B, 0:5', reference_list) == list(range(5))
    assert mixed_list_to_int_list(r'A, B, 2:5', reference_list) == list(range(5))
    assert mixed_list_to_int_list(r'0:2, F, G', reference_list) == [0, 1, 5, 6]
    assert mixed_list_to_int_list(r'0:2, F, 6', reference_list) == [0, 1, 5, 6]
    assert mixed_list_to_int_list(r'A, 1, F, 6', reference_list) == [0, 1, 5, 6]
    assert mixed_list_to_int_list(r'A, 1, 5, G', reference_list) == [0, 1, 5, 6]
    assert mixed_list_to_int_list(r'0, B, F, 6', reference_list) == [0, 1, 5, 6]
    assert mixed_list_to_int_list(r'A, B, 5, 6', reference_list) == [0, 1, 5, 6]

    assert mixed_list_to_int_list(r'A, 4, 5, I, 24:26', reference_list) == [0, 4, 5, 8, 24, 25]
    assert mixed_list_to_int_list(r'0, 4:6, 8, 10:12, Y, 25', reference_list) == [0, 4, 5, 8, 10, 11, 24,
                                                                                               25]
    pass


def test_slice_string_to_list():
    input_string1 = "10:15"
    assert slice_string_to_list(input_string1) == [10, 11, 12, 13, 14]

    try:
        input_string2 = "7:5"
        slice_string_to_list(input_string2)
    except ValueError as ve:
        assert True
    else:
        assert False

    pass


def test_to_int_list():
    input_string1 = "10:15,8"
    assert to_int_list(input_string1) == [8, 10, 11, 12, 13, 14]

    input_string2 = "11,10:15,8,14"
    assert to_int_list(input_string2) == [8, 10, 11, 12, 13, 14]

    try:
        input_string3 = "0,1,7:5"
        to_int_list(input_string3)
    except ValueError as ve:
        assert True
    else:
        assert False

    input_string4 = "1100:1200"
    assert to_int_list(input_string4) == list(range(1100, 1200))

    input_string5 = "15,18,1:5"
    assert to_int_list(input_string5) == [1, 2, 3, 4, 15, 18]

    input_string6 = "15, 18, 1:5"
    assert to_int_list(input_string6) == [1, 2, 3, 4, 15, 18]

    input_string7 = "15,18, 1:5"
    assert to_int_list(input_string7) == [1, 2, 3, 4, 15, 18]

    input_string8 = "15, 18,1:5"
    assert to_int_list(input_string8) == [1, 2, 3, 4, 15, 18]

    pass


# not used at the moment
def test_listify_strings():
    t1 = listify_strings(["AA", "BB"], "CC")
    t2 = listify_strings("AA", ["BB", "CC"])
    t3 = listify_strings("AA", "BB")
    t4 = listify_strings(["AA"], ["BB"])
    t5 = listify_strings(t3, "CC")
    t6 = listify_strings(t4, ["CC"])
    t7 = listify_strings("AA", ["BB"])
    t8 = listify_strings(["AA"], "BB")

    testlist1 = [t1, t2, t5, t6]
    target1 = ["AA", "BB", "CC"]

    testlist2 = [t3, t4, t7, t8]
    target2 = ["AA", "BB"]

    assert all(map(lambda tx: all(map(lambda x: x[0] == x[1], list(zip(tx, target1)))), testlist1))
    assert all(map(lambda tx: all(map(lambda x: x[0] == x[1], list(zip(tx, target2)))), testlist2))

    pass

# if __name__ == "__main__":
#     test_mixed_list_to_int_list()
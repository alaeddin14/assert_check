import unittest
import logging
from unittest.mock import patch
from assert_check import (
    run_assert, 
    assert_none_check, 
    assert_list_check,
    assert_dict_check,
    assert_str_check,
    assert_int_check,
    assert_float_check,
    assert_bool_check,
    assert_keys_check,
    assert_non_empty_check
)

class TestAssertCheck(unittest.TestCase):
    """Test cases for assert_check functions."""
    
    def setUp(self):
        """Set up test fixtures"""
        # Disable logging during tests to reduce noise
        logging.disable(logging.CRITICAL)
    
    def tearDown(self):
        """Tear down test fixtures"""
        # Re-enable logging after tests
        logging.disable(logging.NOTSET)
    
    def test_run_assert_pass(self):
        """Test run_assert when condition is True"""
        # Should not raise any exception
        run_assert(True, "This should not fail")
    
    def test_run_assert_fail(self):
        """Test run_assert when condition is False"""
        with self.assertRaises(AssertionError) as context:
            run_assert(False, "Expected failure")
        self.assertEqual(str(context.exception), "Expected failure")
    
    def test_assert_none_check_pass(self):
        """Test assert_none_check with a non-None value"""
        # Should not raise any exception
        assert_none_check("Not None")
        assert_none_check(0)  # Edge case: zero is not None
        assert_none_check(False)  # Edge case: False is not None
        assert_none_check("")  # Edge case: Empty string is not None
    
    def test_assert_none_check_fail(self):
        """Test assert_none_check with None"""
        with self.assertRaises(AssertionError) as context:
            assert_none_check(None)
        self.assertEqual(str(context.exception), "Item must not be None")
    
    def test_assert_none_check_custom_message(self):
        """Test assert_none_check with a custom message"""
        custom_msg = "Custom None error message"
        with self.assertRaises(AssertionError) as context:
            assert_none_check(None, custom_msg)
        self.assertEqual(str(context.exception), custom_msg)
    
    def test_assert_list_check_pass(self):
        """Test assert_list_check with lists"""
        # Should not raise any exception
        assert_list_check([])
        assert_list_check([1, 2, 3])
        assert_list_check(list())
    
    def test_assert_list_check_fail(self):
        """Test assert_list_check with non-lists"""
        for non_list in ["string", 123, {"a": 1}, (1, 2), None, set()]:
            with self.subTest(non_list=non_list):
                with self.assertRaises(AssertionError):
                    assert_list_check(non_list)
    
    def test_assert_dict_check_pass(self):
        """Test assert_dict_check with dictionaries"""
        # Should not raise any exception
        assert_dict_check({})
        assert_dict_check({"key": "value"})
        assert_dict_check(dict())
    
    def test_assert_dict_check_fail(self):
        """Test assert_dict_check with non-dictionaries"""
        for non_dict in ["string", 123, [1, 2], (1, 2), None, set()]:
            with self.subTest(non_dict=non_dict):
                with self.assertRaises(AssertionError):
                    assert_dict_check(non_dict)
    
    def test_assert_str_check_pass(self):
        """Test assert_str_check with strings"""
        # Should not raise any exception
        assert_str_check("string")
        assert_str_check("")
        assert_str_check(str())
    
    def test_assert_str_check_fail(self):
        """Test assert_str_check with non-strings"""
        for non_str in [123, [1, 2], {"a": 1}, (1, 2), None, set()]:
            with self.subTest(non_str=non_str):
                with self.assertRaises(AssertionError):
                    assert_str_check(non_str)
    
    def test_assert_int_check_pass(self):
        """Test assert_int_check with integers"""
        # Should not raise any exception
        assert_int_check(0)
        assert_int_check(123)
        assert_int_check(-456)
    
    def test_assert_int_check_fail(self):
        """Test assert_int_check with non-integers"""
        for non_int in ["string", 1.23, [1, 2], {"a": 1}, (1, 2), None, set()]:
            with self.subTest(non_int=non_int):
                with self.assertRaises(AssertionError):
                    assert_int_check(non_int)
    
    def test_assert_float_check_pass(self):
        """Test assert_float_check with floats"""
        # Should not raise any exception
        assert_float_check(0.0)
        assert_float_check(1.23)
        assert_float_check(-4.56)
    
    def test_assert_float_check_fail(self):
        """Test assert_float_check with non-floats"""
        for non_float in ["string", 123, [1, 2], {"a": 1}, (1, 2), None, set()]:
            with self.subTest(non_float=non_float):
                with self.assertRaises(AssertionError):
                    assert_float_check(non_float)
    
    def test_assert_bool_check_pass(self):
        """Test assert_bool_check with booleans"""
        # Should not raise any exception
        assert_bool_check(True)
        assert_bool_check(False)
    
    def test_assert_bool_check_fail(self):
        """Test assert_bool_check with non-booleans"""
        for non_bool in ["string", 123, 0, 1, [1, 2], {"a": 1}, (1, 2), None, set()]:
            with self.subTest(non_bool=non_bool):
                with self.assertRaises(AssertionError):
                    assert_bool_check(non_bool)
    
    def test_assert_keys_check_pass(self):
        """Test assert_keys_check with dictionaries containing required keys"""
        # Should not raise any exception
        assert_keys_check({"a": 1, "b": 2}, ["a"])
        assert_keys_check({"a": 1, "b": 2}, ["a", "b"])
        assert_keys_check({"a": 1, "b": 2, "c": 3}, ["a", "b"])
        assert_keys_check({"a": 1}, set())  # Empty required keys
    
    def test_assert_keys_check_fail(self):
        """Test assert_keys_check with dictionaries missing required keys"""
        with self.assertRaises(AssertionError):
            assert_keys_check({"a": 1}, ["b"])
        
        with self.assertRaises(AssertionError):
            assert_keys_check({"a": 1}, ["a", "b"])
        
        # Not a dictionary
        with self.assertRaises(AssertionError):
            assert_keys_check("not a dict", ["key"])
    
    def test_assert_non_empty_check_pass(self):
        """Test assert_non_empty_check with non-empty collections"""
        # Should not raise any exception
        assert_non_empty_check([1])
        assert_non_empty_check({"a": 1})
        assert_non_empty_check("string")
        assert_non_empty_check((1, 2))
    
    def test_assert_non_empty_check_fail(self):
        """Test assert_non_empty_check with empty collections"""
        for empty_item in [[], {}, "", tuple()]:
            with self.subTest(empty_item=empty_item):
                with self.assertRaises(AssertionError):
                    assert_non_empty_check(empty_item)


if __name__ == "__main__":
    unittest.main()

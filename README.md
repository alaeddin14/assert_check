# Assert Check Utility

This Python module provides a set of utility functions for performing various assertion checks. These functions are designed to validate input data and raise meaningful errors when conditions are not met. Each function logs relevant information before raising an `AssertionError` to help with debugging.

## Features

- **None Check**: Ensure an item is not `None`.
- **Type Checks**: Validate if an item is of a specific type (e.g., list, dictionary, string, integer, float, boolean).
- **Key Presence Check**: Verify that a dictionary contains required keys.
- **Non-Empty Check**: Ensure an item is not empty.



## Usage

Use the assertion functions to validate your data:
   ```python
   my_list = [1, 2, 3]
   assert_list_check(my_list)

   my_dict = {"a" : 1 , "b" : 2 , "c" : 3}
   assert_keys_check(my_dict, ["a" , "e"])
   ```


## License

This project is licensed under the MIT License.
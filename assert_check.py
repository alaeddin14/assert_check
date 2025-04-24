import logging
from typing import Any, Dict, List, Set, Union, TypeVar, Type, Optional, Sequence, Mapping

# Configure logging
logging.basicConfig(level=logging.INFO)

def run_assert(condition: bool, message: str) -> None:
    """
    Check the condition and log the message if the assertion fails.
    Args:
        condition (bool): The condition to check.
        message (str): The message to log if the assertion fails.
    """
    if not condition:
        logging.error(message)  # Log an error message
        raise AssertionError(message)  # Raise an AssertionError

T = TypeVar('T')

def assert_type_check(item: Any, expected_type: Union[Type, tuple], type_name: str, msg: Optional[str] = None) -> None:
    """
    Generic function to check if an item is of the expected type.
    
    Args:
        item: The item to check.
        expected_type: The type or tuple of types to check against.
        type_name: String representation of the type for logging.
        msg: Optional custom error message.
    """
    if not isinstance(item, expected_type):
        default_msg = f"Item must be a {type_name}"
        message = msg if msg is not None else default_msg
        logging.info(f"Performing {type_name} Check...")
        logging.info(f"{item=}")
        run_assert(False, message)

def assert_none_check(item: Any, msg: str = "Item must not be None") -> None:
    """
    Check if the item is None and log the message if it is.
    
    Args:
        item: The item to check.
        msg: The message to log if the assertion fails.
    """
    if item is None:
        logging.info("Performing None Check...")
        logging.info(f"{item=}")
        run_assert(False, msg)

def assert_list_check(item: Any, msg: str = "Item must be a list") -> None:
    """
    Check if the item is a list and log the message if it is not.
    
    Args:
        item: The item to check.
        msg: The message to log if the assertion fails.
    """
    assert_type_check(item, list, "List", msg)

def assert_dict_check(item: Any, msg: str = "Item must be a dictionary") -> None:
    """
    Check if the item is a dictionary and log the message if it is not.
    
    Args:
        item: The item to check.
        msg: The message to log if the assertion fails.
    """
    assert_type_check(item, dict, "Dictionary", msg)

def assert_str_check(item: Any, msg: str = "Item must be a string") -> None:
    """
    Check if the item is a string and log the message if it is not.
    
    Args:
        item: The item to check.
        msg: The message to log if the assertion fails.
    """
    assert_type_check(item, str, "String", msg)

def assert_int_check(item: Any, msg: str = "Item must be an integer") -> None:
    """
    Check if the item is an integer and log the message if it is not.
    
    Args:
        item: The item to check.
        msg: The message to log if the assertion fails.
    """
    assert_type_check(item, int, "Integer", msg)

def assert_float_check(item: Any, msg: str = "Item must be a float") -> None:
    """
    Check if the item is a float and log the message if it is not.
    
    Args:
        item: The item to check.
        msg: The message to log if the assertion fails.
    """
    assert_type_check(item, float, "Float", msg)

def assert_bool_check(item: Any, msg: str = "Item must be a boolean") -> None:
    """
    Check if the item is a boolean and log the message if it is not.
    
    Args:
        item: The item to check.
        msg: The message to log if the assertion fails.
    """
    assert_type_check(item, bool, "Boolean", msg)

def assert_keys_check(item: Dict[Any, Any], required_keys: Union[List[Any], Set[Any]], msg: str = "Item must contain the required keys") -> None:
    """
    Check if the dictionary contains the required keys and log the message if it does not.
    
    Args:
        item: The dictionary to check.
        required_keys: A collection of keys that must be present.
        msg: The message to log if the assertion fails.
    """
    if not isinstance(item, dict) or not all(key in item for key in required_keys):
        logging.info("Performing Key Presence Check...")
        logging.info(f"{item=}, {required_keys=}")
        run_assert(False, msg)

def assert_non_empty_check(item: Union[Sequence[Any], Mapping[Any, Any]], msg: str = "Item must not be empty") -> None:
    """
    Check if the item is non-empty and log the message if it is not.
    
    Args:
        item: The item to check.
        msg: The message to log if the assertion fails.
    """
    if not item:
        logging.info("Performing Non-Empty Check...")
        logging.info(f"{item=}")
        run_assert(False, msg)


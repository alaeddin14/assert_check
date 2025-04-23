import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def run_assert(condition, message):
    """
    Check the condition and log the message if the assertion fails.
    Args:
        condition (bool): The condition to check.
        message (str): The message to log if the assertion fails.
    """
    if not condition:
        logging.error(message)  # Log an error message
        raise AssertionError(message)  # Raise an AssertionError

def assert_none_check(item:any , msg= "Item must not be None"):
    """
    Check if the item is None and log the message if it is.
    Args:
        item (any): The item to check.
        msg (str): The message to log if the assertion fails.
    """
    if item is None:
        logging.info("Performing None Check...")
        logging.info(f"{item=}")
        run_assert(False, msg)  # Trigger the assertion

def assert_list_check(item, msg="Item must be a list"):
    """
    Check if the item is a list and log the message if it is not.
    Args:
        item (any): The item to check.
        msg (str): The message to log if the assertion fails.
    """
    if not isinstance(item, list):
        logging.info("Performing List Check...")
        logging.info(f"{item=}")
        run_assert(False, msg)  # Trigger the assertion

def assert_dict_check(item, msg="Item must be a dictionary"):
    """
    Check if the item is a dictionary and log the message if it is not.
    Args:
        item (any): The item to check.
        msg (str): The message to log if the assertion fails.
    """
    if not isinstance(item, dict):
        logging.info("Performing Dictionary Check...")
        logging.info(f"{item=}")
        run_assert(False, msg)  # Trigger the assertion

def assert_str_check(item, msg="Item must be a string"):
    """
    Check if the item is a string and log the message if it is not.
    Args:
        item (any): The item to check.
        msg (str): The message to log if the assertion fails.
    """
    if not isinstance(item, str):
        logging.info("Performing String Check...")
        logging.info(f"{item=}")
        run_assert(False, msg)  # Trigger the assertion

def assert_int_check(item, msg="Item must be an integer"):
    """
    Check if the item is an integer and log the message if it is not.
    Args:
        item (any): The item to check.
        msg (str): The message to log if the assertion fails.
    """
    if not isinstance(item, int):
        logging.info("Performing Integer Check...")
        logging.info(f"{item=}")
        run_assert(False, msg)  # Trigger the assertion

def assert_float_check(item, msg="Item must be a float"):
    """
    Check if the item is a float and log the message if it is not.
    Args:
        item (any): The item to check.
        msg (str): The message to log if the assertion fails.
    """
    if not isinstance(item, float):
        logging.info("Performing Float Check...")
        logging.info(f"{item=}")
        run_assert(False, msg)  # Trigger the assertion

def assert_bool_check(item, msg="Item must be a boolean"):
    """
    Check if the item is a boolean and log the message if it is not.
    Args:
        item (any): The item to check.
        msg (str): The message to log if the assertion fails.
    """
    if not isinstance(item, bool):
        logging.info("Performing Boolean Check...")
        logging.info(f"{item=}")
        run_assert(False, msg)  # Trigger the assertion

def assert_keys_check(item, required_keys, msg="Item must contain the required keys"):
    """
    Check if the dictionary contains the required keys and log the message if it does not.
    Args:
        item (dict): The dictionary to check.
        required_keys (list | set): A collection of keys that must be present.
        msg (str): The message to log if the assertion fails.
    """
    if not isinstance(item, dict) or not all(key in item for key in required_keys):
        logging.info("Performing Key Presence Check...")
        logging.info(f"{item=}, {required_keys=}")
        run_assert(False, msg) # Trigger the assertion

def assert_non_empty_check(item, msg="Item must not be empty"):
    """
    Check if the item is non-empty and log the message if it is not.
    Args:
        item (sequence | dict): The item to check.
        msg (str): The message to log if the assertion fails.
    """
    if not item:
        logging.info("Performing Non-Empty Check...")
        logging.info(f"{item=}")
        run_assert(False, msg) # Trigger the assertion


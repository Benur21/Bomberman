def goto_inline(x: int, y: int) -> str:
    """This function returns a string value that, when printed, will move the console cursor to the desired coordinates.

    Args:
        x (int): X coordinate, starting with 0.
        y (int): Y coordinate, stating with 0.

    Returns:
        str: Value that moves the cursor to the desired location.
    """
    # Add 1 because goto's coordinates start from 1 and I want it to start with 0
    return f"\033[{y+1};{x+1}H"

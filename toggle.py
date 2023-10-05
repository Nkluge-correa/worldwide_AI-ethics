
def toggle_modal(n1, n2, is_open):
    """
    Toggles the visibility of the simple modal window.

    Args:
    ---------
        n1 (bool): A flag to check if the first modal is open or closed.
        n2 (bool): A flag to check if the second modal is open or closed.
        is_open (bool): A flag to check if the modal is currently open or not.

    Returns:
    ---------
        bool: The updated value of the `is_open` flag after toggling the modal window.
    """
    if n1 or n2:
        return not is_open
    return is_open


def toggle_offcanvas(n1, is_open):
    """
    Toggles the visibility of the offcanvas element.

    Args:
    ---------
        n1 (bool): A flag to check if the offcanvas element is open or closed.
        is_open (bool): A flag to check if the offcanvas element is currently open or not.

    Returns:
    ---------
        bool: The updated value of the `is_open` flag after toggling the offcanvas element.
    """
    if n1:
        return not is_open
    return is_open

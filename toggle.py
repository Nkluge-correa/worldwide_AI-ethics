
def toggle_modal(n1, n2, is_open):
    """
    Opens the simple modals across the pages.
    """
    if n1 or n2:
        return not is_open
    return is_open

from random import randint


def random_color() -> str:
    """Generate a random color in hex format."""
    return "#%06x" % randint(0, 0xFFFFFF)

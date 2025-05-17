#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise NameError(message)
# Example usage:
if __name__ == "__main__":
    try:
        raise_exception_msg("This is a custom error message")
    except NameError as e:
        print(e)
    finally:
        pass

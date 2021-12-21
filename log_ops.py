"""

+----------------+-------------------------------------------------------+
| Author:        | Ganesh Kuramsetti                                     |
+----------------+-------------------------------------------------------+
| Script Name:   | log_ops.py                                            |
+----------------+-------------------------------------------------------+
| Date Created:  | 26-Aug-2021                                           |
+----------------+-------------------------------------------------------+
| Description:   | A module file that holds the log or debug statements. |
+----------------+-------------------------------------------------------+
| Language:      | Python                                                |
+----------------+-------------------------------------------------------+
| Prerequisites: | Python3                                               |
+----------------+-------------------------------------------------------+
| Instructions:  | Do not execute this file, import and use instead.     |
+----------------+-------------------------------------------------------+
| Date Updated:  | 26-Aug-2021                                           |
+----------------+-------------------------------------------------------+

"""

# !/usr/bin/python
# importing libraries
import datetime


def log_with_pre_bffr(text):
    """Prints the given string with an empty line before

    Args:
        text (string): String that should be print to the output.
    """
    print("")
    print(f"###.....{datetime.datetime.now()}.....###")
    print(text)


def log_with_post_bffr(text):
    """Prints the given string with an empty line after

    Args:
        text (string): String that should be print to the output.
    """
    print(f"###.....{datetime.datetime.now()}.....###")
    print(text)
    print("")


def log_with_bffr(text):
    """Prints the given string with an empty line before and after

    Args:
        text (string): String that should be print to the output.
    """
    print("")
    print(f"###.....{datetime.datetime.now()}.....###")
    print(text)
    print("")


# Execute the below code block if this file run as a primary file.
if __name__ == '__main__':
    something = " with you."
    log_with_pre_bffr(f"Hell{something}")

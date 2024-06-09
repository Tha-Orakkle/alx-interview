#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """Validate whether a given dataset represents a valid utf-8 encoding"""

    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # determine the length of bytes in this UTF-8 character
            while byte & mask:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                # where it is a 1 byte character
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Check that the byte is of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1

    return num_bytes == 0

#!/usr/bin/python3
"""Implement validUTF8 function"""


def validUTF8(data):
    """Validate if a dataset is valid UTF-8 encoding"""
    """
    Step 1: Initialize a variable to keep track
    of the number of bytes in the current character
    """
    num_bytes = 0

    # Step 2: Iterate through each byte in the data
    for byte in data:
        """
        Step 3: Check the 8th bit to determine
        if it's a start byte or a continuation byte
        """
        if num_bytes == 0:
            if (byte >> 7) == 0:
                # Single-byte character (starts with 0)
                continue
            elif (byte >> 5) == 0b110:
                # Two-byte character (starts with 110)
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                # Three-byte character (starts with 1110)
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                # Four-byte character (starts with 11110)
                num_bytes = 3
            else:
                # Invalid start byte
                return False
        else:
            # Check if the byte is a continuation byte (starts with 10)
            if (byte >> 6) != 0b10:
                return False
            """
            Decrement the number of remaining
            bytes to process for this character
            """
            num_bytes -= 1

    # Step 4: Check if there are any remaining bytes to process
    return num_bytes == 0

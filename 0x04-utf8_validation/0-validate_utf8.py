#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    helper1 = 1 << 7
    helper2 = 1 << 6
    bits_count = 0

    for i in range(len(data)):
        if bits_count == 0:
            temp_helper = 1 << 7
            while temp_helper & data[i]:
                bits_count += 1
                temp_helper >>= 1

            if bits_count == 0:
                continue

            if bits_count > 4:
                return False
        else:
            for j in range(1, bits_count):
                if i + j >= len(data):
                    return False
                if not (data[i + j] & helper1 and not (data[i + j] & helper2)):
                    return False
        bits_count -= 1
    return bits_count == 0

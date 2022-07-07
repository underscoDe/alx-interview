#!/usr/bin/python3
""" Stats """
from sys import stdin


def print_log_stats(file_size, stats):
    """Print stats"""
    print(f'File size: {file_size}')
    for k in sorted(stats):
        print(f'{k}: {stats[k]}')


if __name__ == "__main__":
    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in stdin:
            if count == 10:
                print_log_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_log_stats(size, status_codes)

    except KeyboardInterrupt:
        print_log_stats(size, status_codes)
        raise

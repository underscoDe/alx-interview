#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_log_stats(file_size, stats):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print(f'File size: {file_size}')
    for k in sorted(stats):
        print(f'{k}: {stats[k]}')


if __name__ == '__main__':
    from sys import stdin
    count = 0
    total_size = 0
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    statuses_count = {}

    try:
        for line in stdin:
            if count == 10:
                print_log_stats(total_size, statuses_count)
                count = 0
            else:
                count += 1

            line_details = line.split(' - ')[1]
            try:
                total_size += int(line_details.split()[-1])
            except (ValueError, IndexError):
                pass

            try:
                code = int(line_details.split()[-2])
                if code in status_codes:
                    if code in statuses_count:
                        statuses_count[code] += 1
                    else:
                        statuses_count[code] = 1
            except (KeyError, IndexError):
                pass
    except KeyboardInterrupt:
        print_log_stats(total_size, statuses_count)
        raise

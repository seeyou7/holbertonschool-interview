#!/usr/bin/python3
import sys

# Dictionary to hold counts for each status code
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0
line_count = 0


def print_statistics():
    """Print accumulated file size and status code metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def process_line(line):
    """Process a log line to extract status code and file size."""
    global total_size
    try:
        # Split the line by space and validate the format
        parts = line.split()
        if len(parts) == 9 and parts[5] == '"GET' and parts[6] == '/projects/260' and parts[7] == 'HTTP/1.1"':
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update status code count and total file size if valid
            if status_code in status_codes:
                status_codes[status_code] += 1
                total_size += file_size
    except (IndexError, ValueError):
        # Ignore lines not match the expected format or have invalid values
        pass


try:
    for line in sys.stdin:
        process_line(line)
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    # Print stats upon keyboard interruption (CTRL+C)
    print_statistics()
    sys.exit(0)

# Final statistics if end of input is reached
print_statistics()

#!/usr/bin/python3


import sys
import signal

# Initialize variables
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_metrics():
    """Print the accumulated metrics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))

def signal_handler(sig, frame):
    """Handle keyboard interrupt (Ctrl + C) by printing metrics before exiting."""
    print_metrics()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) < 7:
            continue
        
        # Extract the status code and file size
        status_code = parts[-2]
        file_size = parts[-1]

        # Convert status_code and file_size to integers if possible
        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # Update total file size
        total_file_size += file_size

        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Handle keyboard interrupt gracefully
    print_metrics()
    sys.exit(0)

finally:
    # Print metrics in case of any unexpected termination
    print_metrics()

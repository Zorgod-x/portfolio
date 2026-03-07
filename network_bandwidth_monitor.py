import psutil
import time

def get_bytes_sent_received():
    """
    Get the total bytes sent and received.
    """
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_received = net_io.bytes_recv
    return bytes_sent, bytes_received

def calculate_speed(prev_sent, prev_received, interval):
    """
    Calculate upload and download speeds in bytes per second (B/s).
    """
    current_sent, current_received = get_bytes_sent_received()
    sent_speed = (current_sent - prev_sent) / interval
    received_speed = (current_received - prev_received) / interval
    return sent_speed, received_speed

def main():
    try:
        interval = 1  # Update interval in seconds
        prev_sent, prev_received = get_bytes_sent_received()

        while True:
            sent_speed, received_speed = calculate_speed(prev_sent, prev_received, interval)
            prev_sent, prev_received = get_bytes_sent_received()

            print(f"Upload speed: {sent_speed:.2f} B/s")
            print(f"Download speed: {received_speed:.2f} B/s")
            print("-" * 30)

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()

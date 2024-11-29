from typing import List

# https://leetcode.com/discuss/interview-question/5898854/L5-Google-or-Interview-Exp.-or-Rejected


def classify_messages_optimized(logs):
    last_printed_time = {}  # Dictionary to store the last printed timestamp of each message
    printed_messages = []  # List to store the printed messages

    for log in logs:
        current_message = log["message"]
        current_time = log["timeStamp"]

        if (
            current_message not in last_printed_time
            or current_time - last_printed_time[current_message] > 10
        ):
            printed_messages.append(current_message)
            last_printed_time[
                current_message
            ] = current_time  # Update the last printed time

    return printed_messages


if __name__ == "__main__":
    logs = [
        {"timeStamp": 1, "message": "Hello"},
        {"timeStamp": 2, "message": "Hello"},
        {"timeStamp": 8, "message": "Hey"},
        {"timeStamp": 12, "message": "Hello"},
    ]

    output = classify_messages_optimized(logs)
    print(output)

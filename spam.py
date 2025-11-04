import pyautogui
import time
import random
import sys

message = input("Enter the message to spam: ")
count = int(input("How many times do you want to send it? "))
min_delay = float(input("Enter minimum delay (seconds): "))
max_delay = float(input("Enter maximum delay (seconds): "))

add_counter = input("Add message counter at the end? (y/n): ").lower() == "y"

print("\nPlease select a chat window. You have 10 seconds...")
time.sleep(10)

try:
    for i in range(1, count + 1):
        text_to_send = f"{message} / ({i})" if add_counter else message

        pyautogui.typewrite(text_to_send)
        pyautogui.press("enter")
        print(f"✅ Sent {i}/{count}")

        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)

    print("\n🎉 Finished sending all messages!")

except KeyboardInterrupt:
    print("\n🛑 Stopped by user (KeyboardInterrupt).")
    sys.exit()

except Exception as e:
    print(f"\n⚠️ Error occurred: {e}")

import pyautogui , time , random
message ="hi"
count=10
min_delay = 2.0
max_delay = 3.0

print("Please select a chat within 10 seconds")
time.sleep(10)
try:
	for i in range(1 , count+1):
		pyautogui.typewrite(message)
		pyautogui.press("enter")
		print(f"Sent {i} / {count}")
		delay= random.uniform(min_delay,max_delay)
		time.sleep(delay)
except KeyboardInterrup:
	print("Stopprd by user (KeyboardInterrup).")
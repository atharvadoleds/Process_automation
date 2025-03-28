import pyautogui
import time
import winsound

print("Move your mouse to the desired location and click. I'll record the position and play a sound.")
print("Press Ctrl+C to stop the script.")

try:
    while True:
        # Wait for 10 seconds before starting
        print("Waiting 10 seconds before starting...")
        time.sleep(5)

        # Get the current mouse position
        current_position = pyautogui.position()
        print(f"Recorded position: {current_position}")

        # Play a sound to indicate that the position has been recorded
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

except KeyboardInterrupt:
    print("Script stopped.")
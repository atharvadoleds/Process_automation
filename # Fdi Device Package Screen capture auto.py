import pyautogui
import time

# Coordinates for the actions
file_menu_coords = (22, 29)
device_menu_coords = (64, 34)
device_setup_coords = (64, 296)
quick_setup_coords = (374, 296)
quick_setup_warning_coords = (1111, 697)
quick_setup_reset_converter_coords = (999, 645)
drive_overview_coords = (675, 420)
Motor_overview_coords = (675, 520)
Limits_overview_coords = (675, 610)
quick_setup_finish_coords = (1306, 1112)




# Function to take a screenshot and save it
def take_screenshot(file_name):
    time.sleep(12)
    screenshot = pyautogui.screenshot()
    save_path = rf'C:\Users\z004b2dn\{file_name}'
    screenshot.save(save_path)
    print(f"Screenshot saved as {save_path}")

# Wait for 5 seconds before starting the automation
print("Waiting 8 seconds before starting the automation...")
time.sleep(8)

# 1 Quick setup procedure capture

# Step 1: Click the "Device" menu
pyautogui.moveTo(device_menu_coords[0], device_menu_coords[1])
pyautogui.click()
time.sleep(4)

# Step 2: Click the "Device Setup" option
pyautogui.moveTo(device_setup_coords[0], device_setup_coords[1])
pyautogui.click()
time.sleep(2)

# Step 3: Click the "Quick Setup" option to open Quick setup warning
pyautogui.moveTo(quick_setup_coords[0], quick_setup_coords[1])
pyautogui.click()
time.sleep(2)

# Step 4: Take a screenshot of the "Quick Setup warning" dialog box
take_screenshot('quick_setup_dialog_warning.png')
time.sleep(10)

# Step 5: Click ok on "Quick Setup warning" option to open reset converter option
pyautogui.moveTo(quick_setup_warning_coords[0], quick_setup_warning_coords[1])
pyautogui.click()
time.sleep(10)

# Step 6: Take a screenshot of the "Reset converter option" dialog box
take_screenshot('Reset converter option.png')

# Step 7: Click ok on  "reset converter option" to open Quick setup system overview
pyautogui.moveTo(quick_setup_reset_converter_coords[0],quick_setup_reset_converter_coords[1])
pyautogui.click()
time.sleep(10)

# Step 8: Take a screenshot of the "Quick Setup system overview" dialog box
take_screenshot('quick_setup_system_overview.png')

# Step 9: Click ok on  "Drive information" to open Drive information overview
pyautogui.moveTo(drive_overview_coords[0],drive_overview_coords[1])
pyautogui.click()
time.sleep(12)

# Step 10: Take a screenshot of the "Drive Information" dialog box
take_screenshot('Drive Information.png')

# Step 11: Click ok on  "Motor" to Motor overview
pyautogui.moveTo(Motor_overview_coords[0],Motor_overview_coords[1])
pyautogui.click()
time.sleep(10)

# Step 12: Take a screenshot of the "Motor overview" dialog box
take_screenshot('Motor overview.png')

# Step 13: Click ok on  "Limits" to Limits overview
pyautogui.moveTo(Limits_overview_coords[0],Limits_overview_coords[1])
pyautogui.click()
time.sleep(10)

# Step 14: Take a screenshot of the "Limits overview" dialog box
take_screenshot('Limits Overview.png')

# Step 11: Click Finish to complete Quick setup
pyautogui.moveTo(quick_setup_finish_coords[0],quick_setup_finish_coords[1])
pyautogui.click()
time.sleep(12)

# Step 12: Take a screenshot of the "Quick Setup finished successfully" dialog box
take_screenshot('Quick setup finish.png')
print("Automation completed!")
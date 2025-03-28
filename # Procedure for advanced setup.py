# Procedure for advanced setup

import pyautogui
import time

# Coordinates for the actions
file_menu_coords = (25, 29)
device_menu_coords = (64, 34)
device_setup_coords = (64, 296)
advanced_setup_coords = (342, 319)
advanced_setup_warning_coords = (1113, 695)
advanced_setup_reset_converter_coords = (997, 641)
advanced_setup_system_overview_coords = (613, 362)
drive_info_coords = (627, 367)
motor_overview_coords = (641, 444)
line_drive_options_coords = (616, 534)
operating_mode_coords = (612, 655)
limits_coords = (641, 741)
edit_parameters_coords = (1100, 728)
speed_limit_coords = (630, 238)
skip_frequency_coords = (742, 238)
ramp_function_generator_coords = (823, 238)
current_setting_coords = (935, 238)
apply_settings_coords = (1499, 951)
optimization_coords = (609, 826)
io_config_coords = (617, 913)
digital_inputs_BICO_coords = (1546, 357)
click_on_interconnection_1_coords = (1053, 199)
interconnection_exist_reset_ok_coords = (1170, 622)
click_on_interconnection_2_coords = (1053, 224)
all_bico_connections_coords = (920, 59)
Ok_BICO_connections = (1444, 1124)
edit_ai0_coords = (1186, 889)
edit_ai0_ok_coords = (1386, 909)
edit_ao0_coords = (1180, 973)
edit_a00_ok_coords = (1386, 909)
fieldbus_telegram_coords = (610, 996)
advanced_setup_finish_coords = (1462, 1150)
advanced_setup_successfull = (1096, 641)

# Function to take a screenshot and save it
def take_screenshot(file_name):
    time.sleep(12)
    screenshot = pyautogui.screenshot()
    save_path = rf'C:\Users\z004b2dn\{file_name}'
    screenshot.save(save_path)
    print(f"Screenshot saved as {save_path}")

# Wait for 8 seconds before starting the automation
print("Waiting 8 seconds before starting the automation...")
time.sleep(8)

# 2 Advanced setup procedure capture

# Step 1: Click the "Device" menu
pyautogui.moveTo(device_menu_coords[0], device_menu_coords[1])
pyautogui.click()
time.sleep(4)

# Step 2: Navigate to "Device Setup" and click the "Device Setup" option
pyautogui.moveTo(device_setup_coords[0], device_setup_coords[1])
pyautogui.click()
time.sleep(2)

# Step 3: Navigate to "Advanced Setup" Click the "Advanced Setup" option to open Advanced setup warning
pyautogui.moveTo(advanced_setup_coords[0], advanced_setup_coords[1])
pyautogui.click()
time.sleep(2)

# Step 4: Take a screenshot of the "Advanced Setup warning" dialog box
take_screenshot('advanced_setup_warning.png')
time.sleep(10)

# Step 5: Click "ok" on "Advanced Setup warning" option to open reset converter option
pyautogui.moveTo(advanced_setup_warning_coords[0], advanced_setup_warning_coords[1])
pyautogui.click()
time.sleep(6)

# Step 6: Take a screenshot of the "Reset converter option" dialog box
take_screenshot('advanced_setup_reset_converter.png')

# Step 7: Click ok on "reset converter option" to open Advanced setup system overview
pyautogui.moveTo(advanced_setup_reset_converter_coords[0], advanced_setup_reset_converter_coords[1])
pyautogui.click()
time.sleep(6)

# Step 8: Take a screenshot of the "Advanced Setup system overview" section
take_screenshot('advanced_setup_system_overview.png')

# Step 9: Click on "Drive information" to open Drive information section
pyautogui.moveTo(drive_info_coords[0], drive_info_coords[1])
pyautogui.click()
time.sleep(8)

# Step 10: Take a screenshot of the "Drive Information" section
take_screenshot('drive_information.png')

# Step 11: Click on "Motor" to open Motor section
pyautogui.moveTo(motor_overview_coords[0], motor_overview_coords[1])
pyautogui.click()
time.sleep(8)

# Step 12: Take a screenshot of the "Motor overview" section
take_screenshot('motor_overview.png')

# Step 13: Click on "Line/drive options" to open Line/drive options section
pyautogui.moveTo(line_drive_options_coords[0], line_drive_options_coords[1])
pyautogui.click()
time.sleep(8)

# Step 14: Take a screenshot of the "Line/drive options" section
take_screenshot('line_drive_options.png')

# Step 15: Click on "Operating mode" to open Operating mode section
pyautogui.moveTo(operating_mode_coords[0], operating_mode_coords[1])
pyautogui.click()
time.sleep(10)

# Step 16: Take a screenshot of the "Operating mode" section
take_screenshot('operating_mode.png')

# Step 17: Click on "Limits" to open Limits section
pyautogui.moveTo(limits_coords[0], limits_coords[1])
pyautogui.click()
time.sleep(10)

# Step 18: Take a screenshot of the "Limits" section
take_screenshot('limits.png')

# Step 19: Under "Limits" navigate to "Edit parameters" and click on "Edit parameters"
pyautogui.moveTo(edit_parameters_coords[0], edit_parameters_coords[1])
pyautogui.click()
time.sleep(10)

# Step 20: Take a screenshot of the "Speed limit" section under limits settings
take_screenshot('speed_limit.png')

# Step 21: Click on "Skip frequency" section
pyautogui.moveTo(skip_frequency_coords[0], skip_frequency_coords[1])
pyautogui.click()
time.sleep(10)

# Step 22: Take a screenshot of the "Skip frequency" section
take_screenshot('skip_frequency.png')

# Step 23: Click on "Ramp-function generator" section
pyautogui.moveTo(ramp_function_generator_coords[0], ramp_function_generator_coords[1])
pyautogui.click()
time.sleep(10)

# Step 24: Take a screenshot of the "Ramp-function generator" section
take_screenshot('ramp_function_generator.png')

# Step 25: Click on "Current setting" section
pyautogui.moveTo(current_setting_coords[0], current_setting_coords[1])
pyautogui.click()
time.sleep(10)

# Step 26: Take a screenshot of the "Current setting" section
take_screenshot('current_setting.png')

# Step 27: Click "OK" to apply settings
pyautogui.moveTo(apply_settings_coords[0], apply_settings_coords[1])
pyautogui.click()
time.sleep(10)

# Step 28: Click on "Optimization" to open Optimization section
pyautogui.moveTo(optimization_coords[0], optimization_coords[1])
pyautogui.click()
time.sleep(10)

# Step 29: Take a screenshot of the "Optimization" section
take_screenshot('optimization.png')

# Step 30: Click on "I/O configuration" to open I/O configuration section
pyautogui.moveTo(io_config_coords[0], io_config_coords[1])
pyautogui.click()
time.sleep(20)

# Step 31: Take a screenshot of the "I/O configuration" section
take_screenshot('io_configuration.png')

# Step 32: Click on "Digital inputs for all BICO connections" button
pyautogui.moveTo(digital_inputs_BICO_coords[0], digital_inputs_BICO_coords[1])
pyautogui.click()
time.sleep(10)

# Step 33: Click "Yes" to "Reset telegram"
pyautogui.moveTo(interconnection_exist_reset_ok_coords[0], interconnection_exist_reset_ok_coords[1])
pyautogui.click()
time.sleep(10)

# Step 34: Take a screenshot of the "Reset telegram" dialog box
take_screenshot('reset_telegram.png')

# Step 35: Select first telegram "c0810 command data set selection" to trigger "Interconnection exist" screen
pyautogui.moveTo(click_on_interconnection_1_coords[0], click_on_interconnection_1_coords[1])
pyautogui.click()
time.sleep(10)

# Step 36: Take screenshot of "Interconnection exist" screen
take_screenshot('interconnection_exist.png')

# Step 37: Click "yes"
pyautogui.moveTo(interconnection_exist_reset_ok_coords[0], interconnection_exist_reset_ok_coords[1])
pyautogui.click()
time.sleep(10)

# Step 38: Select 2 telegrams from "Frequently used connections"
pyautogui.moveTo(click_on_interconnection_2_coords[0], click_on_interconnection_2_coords[1])
pyautogui.click()
time.sleep(10)

# Step 39: Take a screenshot of the "Frequently used connections"
take_screenshot('frequently_used_connections.png')

# Step 40: Click on "All BICO connections"
pyautogui.moveTo(all_bico_connections_coords[0], all_bico_connections_coords[1])
pyautogui.click()
time.sleep(10)

# Step 41: Select 2 telegrams from "All BICO connections"
pyautogui.moveTo(all_bico_connections_coords[0], all_bico_connections_coords[1])
pyautogui.click()
time.sleep(10)

# Step 42: Take a screenshot of the "Frequently used connections"
take_screenshot('all_bico_connections.png')

# Step 43: Click "OK"
pyautogui.moveTo(Ok_BICO_connections[0], Ok_BICO_connections[1])
pyautogui.click()
time.sleep(10)

# Step 44: Click on "Edit settings for AI 0" under Analog inputs
pyautogui.moveTo(edit_ai0_coords[0], edit_ai0_coords[1])
pyautogui.click()
time.sleep(10)

# Step 45: Take screenshots for "Edit settings for AI 0"
take_screenshot('edit_ai0.png')

# Step 46: Click on "Edit settings for A0 0" under Analog outputs
pyautogui.moveTo(edit_ao0_coords[0], edit_ao0_coords[1])
pyautogui.click()
time.sleep(10)

# Step 47: Take screenshots for "Edit settings for A0 0"
take_screenshot('edit_ao0.png')

# Step 48: Click ok on "Fieldbus and telegram" to Fieldbus and telegram section
pyautogui.moveTo(fieldbus_telegram_coords[0], fieldbus_telegram_coords[1])
pyautogui.click()
time.sleep(10)

# Step 49: Take a screenshot of the "Fieldbus and telegram" section
take_screenshot('fieldbus_telegram.png')

# Step 50: Click Finish to complete Advanced setup
pyautogui.moveTo(advanced_setup_finish_coords[0], advanced_setup_finish_coords[1])
pyautogui.click()
time.sleep(12)

# Step 51: Take a screenshot of the "Advanced Setup finished successfully" dialog box
take_screenshot('advanced_setup_finish.png')

print("Automation completed!")
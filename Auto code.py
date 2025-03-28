import time
from pywinauto.keyboard import send_keys 
from pywinauto import Application
import pyautogui
from pywinauto.findwindows import find_windows

#from pywinauto.findwindows import find_window_by_process

# Open the installed PC software
#app = Application(backend="uia").start('C:/Program Files (x86)/SIEMENS/SIMATIC_PDM/bin/Siemens.Automation.Pdm.FrameApplication.exe')


# Open the application
main_window = Application(backend= 'uia').start("S7tgtopx.exe")

time.sleep(5)

# Acknowledge the popup
popup = main_window.top_window()
popup.OK.click()
time.sleep(5)
#popup = app.top_window()
#popup.set_focus()
#popup.minimize()
popup.TreeView.get_item(u'\\Sinamics').expand()
popup.TreeView.get_item(u'\\Sinamics\\networks').expand()
popup.TreeView.get_item(u'\\Sinamics\\networks\\PROFINET network').expand()
popup.TreeView.get_item(u'\\Sinamics\\networks\\PROFINET network\\SINAMICS G220 BASIC').click_input()
send_keys('^%o')

time.sleep(10)

# Connect to the window directly assuming it's open
window = Application(backend='uia').connect(title='SINAMICS G220 BASIC')

# Print control types to understand the window structure
controls = window.descendants()
for control in controls:
    print(f"Control type: {control.control_type()}, Control name: {control.window_text()}")

# Optionally close the window
try:
    close_button = window.child_window(title="Close", control_type="Button")
    if close_button.exists():
        close_button.click_input()
        print("Window closed successfully.")
except Exception as e:
    print("Error interacting with the window:", e)


#print(window.control_type)

#window.MenuItem(u'&APPLICATIONMENU_device').click_input()
#window[u'APPLICATIONMENU_updateDiagnostics'].click_input()
#window.MenuItem[u'APPLICATIONMENU_device'].click()
#child_window =popup.child_window(title=u'SINAMICS G220 BASIC')
#child_window.set_focus()
#file_item = child_window.get_item('Expert List')
#file_item.right_click_input()
#child_window.send_keys("{Device}")'
#child_window.TreeView.get_item(u'\\SINAMICS G220 BASIC\\Expert List').click_input()
#child_window.maximize()

#child_window.child_window.top_window()
#print("Class Name:",child_window.ClassName)
#child_window.print_control_identifiers()
#child_window.TreeView.get_item(u'\\SINAMICS G220 BASIC').expand()
#child_window.TreeView.get_item(u'\\SINAMICS G220 BASIC\\Expert List').click_input()
#child_window.offline_root_menu.click_input()

#child_window = popup.child_window(title='SINAMICS G220 BASIC')
#child_window = child_window[1]
#child_window.set_focus()
#child_window.TreeView.get_item(u'\\SINAMICS G220 BASIC\\Expert List').click_input()



#child_window.click_input()
#popup.click_input()
#popup = app.top_window()
#popup1 = Application(backend= 'uia').connect(title="SINAMICS G220 BASIC", control_type="Window",)
#@popup=pywinauto.findwindows(title = "SINAMICS G220 BASIC", control_type= "Window", visible_only= 'True')
#popup = app.top_window()
#popup.maximize()
#popup.TreeView.get_item(u'\\Sinamics G220 BASIC').click_input()
#popup.set_focus()
#popup.TreeView.get_item(u'\\Sinamics G220 BASIC').click_input()
#popup.print_control_identifiers()
#popup.child_window(title="Sinamics", control_type="TreeItem")
#popup.print_control_identifiers()
#pywinauto.find_elements(class_name = "SINAMICS G220 BASIC")
#elements = findwindows.find_elements()
#print_control_identifiers()
#print()
#print(popup.dump_properties())
#window = app.SIMATIC
#

#window.maximize()
#send_keys('^%o')
#pyautogui.rightClick()
#main_window = app.window(title="SIMATICPDMstandalone")
#send_keystrokeys('^%(^)o')
#app.print_control_identifiers()
#pywinauto.find_elements(class_name = "SINAMICS G220 BASIC")
#main_window = app.window()
#pywinauto.mouse.click(button='right',coords=(0,0))
#pywinauto.findbestmatch.get_non_text_control_name(ctrl, controls,text_ctrls)
#location = pyautogui.locateOnScreen('folder.png')

import lab1.search_bar_functionality
import json
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

root = Tk()
root.title('Lab 1 - Ana Sarapova')
#root.iconbitmap('D:\workspace\CS\lab1\icon.ico')
root.geometry("1000x600")

# Create new file function
def new_file():
    my_text.delete("1.0", END) #delete previous text
    root.title('New File - Text Editor')  #update status bars
    status_bar.config(text="New File        ")

# Open files
def open_file():
    my_text.delete("1.0", END) #delete previous text

    # Grab Filename
    text_file = filedialog.askopenfilename(initialdir = 'lab1/policies',
		title = 'Open File', filetypes = (('All Files', '*.*'), ) )

    # Update Status bars
    name = text_file
    status_bar.config(text = f'{name}       ')
    name = name.replace('lab1', '')
    root.title(f'{name} - Text Editor')

    #Open the file
    text_file = open(text_file, 'r')
    stuff = text_file.read()

    #Add file to textbox
    my_text.insert(END, stuff)

    #Close the open file
    text_file.close()

# Save as file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*",
        initialdir="lab1/policies/", 
        title='Save file', 
        filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"),('All Files', '*.*')))
    if text_file:
        # Update status bar
        name = text_file
        status_bar.config(text=f'Saved: {name}       ')
        name = name.replace('lab1/policies/', '')
        root.title(f'{name} - Text Editor')

    # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
		
		# Close the file
        text_file.close()


def find_all(a_str, sub):
	start = 0
	while True:
		start = a_str.find(sub, start)
		if start == -1: return
		yield start
		start += len(sub) #use start += 1 to find overlapping matches

def save_to_json():
	text_file = filedialog.asksaveasfilename(
		defaultextension = '.*',
		initialdir = 'lab1',
		title = 'Save File', filetypes = (('All Files', '*.*'), ))

	if text_file:
		# Update Status Bars
		name = text_file
		status_bar.config(text = f'{name}      ')
		name = name.replace('lab1/policies', '')
		root.title(f'{name} - Text Editor')

		# Save the file
		with open(text_file, 'w') as outfile:
			

			contents = my_text.get(1.0, END)
			contents = contents.replace('            :', ':')
			contents = contents.replace('           :', ':')
			contents = contents.replace('          :', ':')
			contents = contents.replace('         :', ':')
			contents = contents.replace('        :', ':')
			contents = contents.replace('       :', ':')
			contents = contents.replace('      :', ':')
			contents = contents.replace('     :', ':')
			contents = contents.replace('    :', ':')
			contents = contents.replace('   :', ':')
			contents = contents.replace('  :', ':')
			contents = contents.replace(' :', ':')

			start = list(find_all(contents, '<custom_item>'))
			ending = list(find_all(contents, '</custom_item>'))

			custom_item = {}

			custom_item['PASSWORD_POLICY'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
											  'check_type': [], 'password_policy': []}
			custom_item['LOCKOUT_POLICY'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
											 'check_type': [], 'lockout_policy': []}
			custom_item['KERBEROS_POLICY'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
											  'check_type': [], 'kerberos_policy': []}
			custom_item['AUDIT_POLICY'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
										   'check_type': [], 'audit_policy': []}
			custom_item['AUDIT_POLICY_SUBCATEGORY'] = {'type': [], 'description': [], 'value_type': [],
													   'value_data': [], 'check_type': [], 'audit_policy_policy': []}
			custom_item['AUDIT_POWERSHELL'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
											   'powershell_args:': [], 'only_show_cmd_output:': [], 'check_type': [],
											   'severity:': [], 'powershell_option': [], 'powershell_console_file:': []}
			custom_item['AUDIT_FILEHASH_POWERSHELL'] = {'type': [], 'description': [], 'value_type': [], 'file': [],
														'value_data': []}
			custom_item['AUDIT_IIS_APPCMD'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
											   'appcmd_args': [], 'only_show_cmd_output': [], 'check_type': [],
											   'severity': [], 'appcmd_list': [], 'appcmd_filter': [],
											   'appcmd_filler_value': []}
			custom_item['AUDIT_ALLOWED_OPEN_PORTS'] = {'type': [], 'description': [], 'value_type': [],
													   'value_data': [], 'port_type': []}
			custom_item['AUDIT_DENIED_OPEN_PORTS'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
													  'port_type': []}
			custom_item['AUDIT_PROCESS_ON_PORT'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
													'port_type': [], 'port_no': [], 'port_option': [], 'check_type': []}
			custom_item['AUDIT_USER_TIMESTAMPS'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
													'timestamp': [], 'ignore_users': [], 'check_type': []}
			custom_item['BANNER_CHECK'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
										   'reg_key': [], 'reg_item': [], 'is_substring': []}
			custom_item['CHECK_ACCOUNT'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
											'account_type': [], 'check_type': []}
			custom_item['CHECK_LOCAL_GROUP'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
												'group_type': [], 'check_type': []}
			custom_item['ANONYMOUS_SID_SETTING'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
													'check_type': []}
			custom_item['SERVICE_POLICY'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
											 'check_type': [], 'service_name': []}
			custom_item['GROUP_MEMBERS_POLICY'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
												   'check_type': [], 'group_name': []}
			custom_item['USER_GROUPS_POLICY'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
												 'check_type': [], 'user_name': []}
			custom_item['USER_RIGHTS_POLICY'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
												 'check_type': [], 'right_type': [], 'use_domain': []}
			custom_item['FILE_CHECK'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
										 'check_type': [], 'file_option': []}
			custom_item['FILE_VERSION'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
										   'check_type': [], 'file': [], 'file_option': [], 'check_type': []}
			custom_item['FILE_PERMISSIONS'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
											   'check_type': [], 'file': [], 'acl_option': []}
			custom_item['FILE_AUDIT'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
										 'check_type': [], 'file': [], 'acl_option': []}
			custom_item['FILE_CONTENT_CHECK'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
												 'check_type': [], 'regex': [], 'expect': [], 'file_option': [],
												 'avoid_floppy_access': []}
			custom_item['FILE_CONTENT_CHECK_NOT'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
													 'check_type': [], 'regex': [], 'expect': [], 'file_option': []}
			custom_item['REG_CHECK'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
										'reg_key': [], 'reg_item': [], 'key_item': []}
			custom_item['REGISTRY_SETTING'] = {'type': [], 'description': [], 'info': [], 'value_type': [],
											   'value_data': [], 'reg_key': [], 'reg_item': [], 'reg_enum': [],
											   'reg_option': []}
			custom_item['REGISTRY_PERMISSIONS'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
												   'check_type': [], 'reg_key': [], 'acl_option': []}
			custom_item['REGISTRY_AUDIT'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
											 'check_type': [], 'reg_key': [], 'acl_option': []}
			custom_item['REGISTRY_TYPE'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
											'reg_key': [], 'reg_item': [], 'reg_option': []}
			custom_item['SERVICE_PERMISSIONS'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
												  'check_type': [], 'service': [], 'acl_option': []}
			custom_item['SERVICE_AUDIT'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
											'check_type': [], 'service': [], 'acl_option': []}
			custom_item['WMI_POLICY'] = {'type': [], 'description': [], 'value_type': [], 'value_data': [],
										 'check_type': [], 'wmi_namespace': [], 'wmi_request': [], 'wmi_attribute': [],
										 'wmi_key': []}
			for i in range(len(start)):
				content_type_block = contents[start[i] + 13 : ending[i]]
				type_ = content_type_block[content_type_block.find('type:') + 6: content_type_block[content_type_block.find('type:') + 5 :].find('\n') + content_type_block.find('type:') + 5 ]
				for element in list(custom_item[type_].keys()):
					length_of_element = len(element) + 1
					if content_type_block.find(element) != -1:
						custom_item[type_][element].append(content_type_block[content_type_block.find(element + ':') + length_of_element: content_type_block[content_type_block.find(element + ':') + length_of_element :].find('\n') + content_type_block.find(element + ':') + length_of_element ].strip())
					else:
						custom_item[type_][element].append('')

			json.dump(custom_item, outfile)

# Change a selected text color
def text_color():

	# Pick a color
	my_color = colorchooser.askcolor()[1]
	if my_color:
		status_bar.config(text=my_color)

		# Create a font
		color_font = font.Font(my_text, my_text.cget("font"))

		# Configure a tag
		my_text.tag_configure("colored", font=color_font, foreground=my_color)

		# Define current tags
		current_tags = my_text.tag_names("sel.first")

		#If statement to see if the tag has been set
		if "colored" in current_tags:
			my_text.tag_remove("colored", "sel.first", "sel.last")
		else:
			my_text.tag_add("colored", "sel.first", "sel.last")

def bg_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(bg=my_color)

def all_text_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(fg=my_color)

# Create a toolbar
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create Scrollbar For The Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame,width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure Scrollbar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_command(label="Export to Json", command=save_to_json)
file_menu.add_separator
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add Color Menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected text", command=text_color)
color_menu.add_command(label="All text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)

# Add status bar to bottom of app
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


lab1.search_bar_functionality.root.mainloop()

root.mainloop()
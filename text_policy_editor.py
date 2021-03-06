import json
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os
import re

root = Tk()
root.title('Lab 1 - Ana Sarapova')
root.geometry("1200x700")

# Update the listbox
def update(data):
    # Clear the listbox
    my_list.delete(0, END)

    # Add listing to listbox
    for item in data:
        my_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(event):
    # Delere whatever is in the entry box
    my_entry.delete(0, END)

    # Add clinked list item to entry box
    my_entry.insert(0, my_list.get(ANCHOR))


# Create a function to check entry vs listbox
def check(event):
    # Grab what was typed
    typed = my_entry.get()

    if typed == '':
        data = listing
    else:
        data = []
        for item in listing:
            if typed.lower() in item.lower():
                data.append(item)
    
    # Update listbox with selected items
    update(data)

# Create an entry box
my_entry = Entry(root, font=("Tahoma", 11))
my_entry.pack(ipady = 5, ipadx = 100)
# setting focus
my_entry.focus_set()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=10)

# Create a list for search bar
listing = ["reg_key","password", "type", "description", "check_type", "group_policy", "display_name", "value_type", "value_data"]

# Add the searching items to the list
update(listing)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
my_list.bind("<KeyRelease>", check)

# adding of search buttom
button = Button(my_entry, text = 'Find')
button.pack(side = RIGHT)
my_entry.pack(side = TOP)


def check_audit():
    file = open('output.json',)
    audit = json.load(file)

    failed_audits = []
    status_of_audits = []

    with open('audit_result.txt', 'w') as to_save:
        for custom_item in audit:
            try:
                cmd = 'reg query ' + custom_item['reg_key'][1:-1] + ' /v ' + custom_item['reg_item'][1:-1]
                output = os.popen(cmd).read()
                pattern = custom_item['value_data']
                is_present = re.search(pattern, output)
                to_save.write(custom_item['description'][1:-1] + '\t\t\t\t\t\t')
                if is_present:
                    status_of_audits.append(1)
                    to_save.write('Valid' + '\n\n')
                else:
                    failed_audits.append(custom_item)
                    status_of_audits.append(0)
                    to_save.write('Invalid' + '\n')
                    to_save.write('Expected: ' + custom_item['value_data'] + '\n')
                    to_save.write('Found: ' + output + '\n\n')
            except:
                failed_audits.append(custom_item)
                status_of_audits.append(0)
                to_save.write('Invalid' + '\n')

    file_invalid = open('invalid_audits.json', 'w')
    json.dump(failed_audits, file_invalid, indent = 4)

# Create new file function
def new_file():
    my_text.delete("1.0", END) #delete previous text
    root.title('New File - Text Editor')  #update status bars
    status_bar.config(text="New File        ")


def find_all(a_str, sub):
	start = 0
	while True:
		start = a_str.find(sub, start)
		if start == -1: return
		yield start
		start += len(sub) #use start += 1 to find overlapping matches


# Open files
def open_file():
	global number_of_jsons
	global to_json
	global extension
	global current_file

	# Delete previous text
	my_text.delete('1.0', END)
	
	# Grab  Filename
	text_file = filedialog.askopenfilename(
		initialdir = 'lab1/policies/',
		title = 'Open File', filetypes = (('All Files', '*.*'), ) )
	
	current_file = text_file
	
	# Update Status bars
	name = text_file
	status_bar.config(text = f'{name}       ')
	name = name.replace('lab1/policies/', '')
	root.title(f'{name} - Text Editor')

	extension = ''
	i = len(name) - 1
	while name[i] != '.':
		extension += name[i]
		i-=1
	extension = extension[::-1]

	# Open the file
	if extension == 'audit':
		text_file = open(text_file, 'r')
		contents = text_file.read()

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

		general_custom_item = {}
		general_custom_item_keys = []


		for key in custom_item:
			keys_list = list(custom_item[key])
			for key_x in keys_list:
				if key_x not in general_custom_item_keys:
					general_custom_item_keys.append(key_x)

		general_custom_item['serial_number_custom_item'] = []

		for key in general_custom_item_keys:
			general_custom_item[key] = []

		general_custom_item['info'] = []
		general_custom_item['reference'] = []
		general_custom_item['solution'] = []
		general_custom_item['see_also'] = []

		for i in range(len(start)):
			content_type_block = contents[start[i] + 13 : ending[i]]
			general_custom_item['serial_number_custom_item'].append(i)
			for element in list(general_custom_item.keys()):
				length_of_element = len(element) + 1
				if content_type_block.find(element) != -1:
					general_custom_item[element].append(content_type_block[content_type_block.find(element + ':') + length_of_element: content_type_block[content_type_block.find(element + ':') + length_of_element :].find('\n') + content_type_block.find(element + ':') + length_of_element ].strip())
				else:
					if element != 'serial_number_custom_item':
						general_custom_item[element].append('')

		number_of_jsons = len(general_custom_item['serial_number_custom_item'])

		to_json = []
		for i in range(len(general_custom_item['type'])):
			to_print = {}
			for element in list(general_custom_item.keys()):
				if general_custom_item[element][i] != '':
					to_print[element] = general_custom_item[element][i]
			to_json.append(to_print)


		my_text.insert(END, json.dumps(to_json, indent = 4))

		#Close the opened file
		text_file.close()
	
	elif extension == 'json':

		text_file = open(text_file, 'r')
		to_json = json.load(text_file)
		number_of_jsons = len(to_json)
		my_text.insert(END, json.dumps(to_json, indent = 4))
		text_file.close()


# Save as file
def save_as_file():
	global number_of_jsons
	global to_json
	global extension

	def check():
		global custom_items_to_use
		global number_of_jsons
		global to_json
		global extension
		global current_file

		custom_items_to_use = []
		for i in range(len(chkbuttons)):
			if var[i].get() == 1:
				custom_items_to_use.append(i)
		root_checkbox.destroy()
		
		text_file = filedialog.asksaveasfilename(
				defaultextension = '.*',
				initialdir = 'lab1/policies/',
				title = 'Save File', filetypes = (('All Files', '*.*'), ))

		if text_file:
		# Update Status Bars
			name = text_file
			status_bar.config(text = f'{name}       ')
			name = name.replace('lab1/policies/', '')
			root.title(f'{name} - Text Editor')

			to_print = []
			for i in custom_items_to_use:
				to_print.append(to_json[i])

		# Save the file
			text_file = open(text_file, 'w')
			json.dump(to_print, text_file, indent = 4)
		
		# Close the file
			text_file.close()

	def select_all_():

		for i in range(len(chkbuttons)):
			var[i].set(1)


	def deselect_all_():

		for i in range(len(chkbuttons)):
			var[i].set(0)
	
	root_checkbox = Tk()
	root_checkbox.title('Select custom item boxes')
	sb = Scrollbar(root_checkbox, orient = 'vertical')
	text = Text(root_checkbox, width = 40, height = 20, yscrollcommand = sb.set)
	sb.config(command = text.yview)
	sb.pack(side = 'right', fill = 'y')
	var = []
	for i in range(number_of_jsons):
		var.append(IntVar(root_checkbox))
	text.pack(side = 'top', fill = 'both', expand = True)
	chkbuttons = [Checkbutton(root_checkbox, text="Custom Item Nr.%s" % i, variable = var[i], onvalue = 1, offvalue = 0)
                          for i in range(number_of_jsons)]
	for cb in chkbuttons:
		text.window_create('end', window = cb)
		text.insert('end', '\n')

	submit = Button(root_checkbox, text = 'Submit')
	submit.pack(side = BOTTOM)
	submit.config(command = check)

	select_all = Button(root_checkbox, text = 'Select All')
	select_all.pack(side = TOP)
	select_all.config(command = select_all_)

	deselect_all = Button(root_checkbox, text = 'Deselect All')
	deselect_all.pack(side = TOP)
	deselect_all.config(command = deselect_all_)	

	root_checkbox.mainloop()   

def r_audit():

	text_file = 'output.json'
	name = 'output.json'
	root.title(f'{name} - Text Editor')
	text_file = open(text_file, 'w')
	text_file.write(my_text.get(1.0, END))
	text_file.close()

	check_audit()
	new_file()
	
	text_file = 'audit_result.txt'
	text_file = open(text_file, 'r')
	my_text.insert(END, text_file.read())


def enforce_audit():
    text_file = 'to_enforce_audits.json'
    name = 'to_enforce_audits.json'
    root.title(f'{name} - Text Editor')
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))

    text_file.close()

    cmd_backup = 'reg /e ' + 'C:\Backup.reg'
    enforce_all_audits()

    new_file()

    my_text.insert(END, 'DONE! Rerun Run Audit option to check the status!')


def enforce_all_audits():
    file = open('to_enforce_audits.json', )
    audit = json.load(file)

    for custom_item in audit:
        cmd_export = 'reg export ' + custom_item['reg_key'][1:-1] + ' policy_backup' + str(custom_item['custom_item_number']) + '.reg' + ' /y '
        output_export = os.popen(cmd_export).read()
        cmd_delete = 'reg delete ' + custom_item['reg_key'][1:-1] + ' /v ' +custom_item['reg_item'][1:-1] + ' /f'
        output_delete = os.popen(cmd_delete).read()
        v = custom_item['value_data']
        try:
            cmd_add = 'reg add ' + custom_item['reg_key'][1:-1] + ' /v ' + custom_item['reg_item'][1:-1] + ' /t ' + 'REG' + custom_item['value_type'][6:] + ' /d ' + hex(int(v))
            output_add = os.popen(cmd_add).read()
        except ValueError:
            pass


def rollback():
    global audit_status

    text_file = 'to_enforce_audits.json'
    name = 'to_enforce_audits.json'
    root.title(f'{name} - Text Editor')
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))

    text_file.close()

    rollback_audits()

    new_file()

    my_text.insert(END, 'DONE! Rerun Run Audit option to check the status!')


def rollback_audits():
    file = open('output1.json', )
    audit = json.load(file)

    for custom_item in audit:
        cmd_import = 'reg import ' + 'policy_backup' + str(custom_item['custom_item_number']) + '.reg'
        output_import= os.popen(cmd_import).read()


def export():
	global number_of_jsons
	global to_json
	global extension

	def check():
		global custom_items_to_use
		global number_of_jsons
		global to_json
		global extension
		global current_file

		custom_items_to_use = []
		for i in range(len(chkbuttons)):
			if var[i].get() == 1:
				custom_items_to_use.append(i)
		root_checkbox.destroy()
		
		text_file = filedialog.asksaveasfilename(
				defaultextension = '.*',
				initialdir = 'lab1/policies/',
				title = 'Save File', filetypes = (('All Files', '*.*'), ))

		if text_file:
		# Update Status Bars
			name = text_file
			status_bar.config(text = f'{name}       ')
			name = name.replace('lab1/policies/', '')
			root.title(f'{name} - Text Editor')

			text_file = open(text_file, 'w')

			to_print = []
			for i in custom_items_to_use:
				text_file.write('<custom_item>\n')
				for j in to_json[i]:
					text_file.write('\t' + j + ' : ' + str(to_json[i][j]) + '\n')
				text_file.write('</custom_item>\n')
		
	 		# Close the file
			text_file.close()

	def select_all_():

		for i in range(len(chkbuttons)):
			var[i].set(1)

	def deselect_all_():

		for i in range(len(chkbuttons)):
			var[i].set(0)
	
	root_checkbox = Tk()
	root_checkbox.title('Select custom item boxes')
	sb = Scrollbar(root_checkbox, orient = 'vertical')
	text = Text(root_checkbox, width = 40, height = 20, yscrollcommand = sb.set)
	sb.config(command = text.yview)
	sb.pack(side = 'right', fill = 'y')
	var = []
	for i in range(number_of_jsons):
		var.append(IntVar(root_checkbox))
	text.pack(side = 'top', fill = 'both', expand = True)
	chkbuttons = [Checkbutton(root_checkbox, text="Custom Item Nr.%s" % i, variable = var[i], onvalue = 1, offvalue = 0)
                          for i in range(number_of_jsons)]
	for cb in chkbuttons:
		text.window_create('end', window = cb)
		text.insert('end', '\n')

	submit = Button(root_checkbox, text = 'Submit')
	submit.pack(side = BOTTOM)
	submit.config(command = check)

	select_all = Button(root_checkbox, text = 'Select All')
	select_all.pack(side = TOP)
	select_all.config(command = select_all_)

	deselect_all = Button(root_checkbox, text = 'Deselect All')
	deselect_all.pack(side = TOP)
	deselect_all.config(command = deselect_all_)	

	root_checkbox.mainloop()  

def find():
    global start_occurrences
    global end_occurrences
    global index_word
    
    start_occurrences = []
    end_occurrences = [] 
    index_word = 0 
    
    my_text.tag_remove('found', '1.0', END)
     
    s = my_entry.get()

    if s:
        idx = '1.0'
        while 1:
            idx = my_text.search(s, idx, nocase=1,
                              stopindex=END)
            if not idx: break
            
            start_occurrences.append(idx)

            lastidx = '%s+%dc' % (idx, len(s))
            end_occurrences.append(lastidx)

            idx = lastidx

        next_word()


def next_word():
    global index_word
    global start_occurrences
    global end_occurrences
    
    if index_word < len(start_occurrences):
        my_text.tag_remove('found', '1.0', END)
        idx = start_occurrences[index_word]
        lastidx = end_occurrences[index_word]
        my_text.tag_add('found', idx, lastidx)
        to_see = int(idx[0:idx.find('.')])
        my_text.yview(to_see - 10)
        if index_word < (len(start_occurrences) - 1):
            index_word += 1
        my_text.tag_config('found', foreground='black', background = 'red')
 
def back_word():
    global index_word
    global start_occurrences
    global end_occurrences

    if index_word >= 0:
        my_text.tag_remove('found', '1.0', END)
        idx = start_occurrences[index_word]
        lastidx = end_occurrences[index_word]
        my_text.tag_add('found', idx, lastidx)
        to_see = int(idx[0:idx.find('.')])
        my_text.yview(to_see - 10)
        if (index_word > 0):
            index_word -= 1
        my_text.tag_config('found', foreground='black', background = 'red')

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
my_text = Text(my_frame,width=97, height=25, font=("Helvetica", 11), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
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
file_menu.add_command(label="Export to Json", command=export)
file_menu.add_command(label = 'Run Audit', command = r_audit)
file_menu.add_command(label='Enforce Audit', command=enforce_audit)
file_menu.add_command(label='Rollback', command=rollback)
file_menu.add_separator
file_menu.add_command(label="Exit", command=root.quit)

# Add Color Menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected text", command=text_color)
color_menu.add_command(label="All text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)

back_button = Button(my_entry, text = 'Back')
back_button.pack(side = RIGHT)

next_button = Button(my_entry, text = 'Next')
next_button.pack(side = RIGHT)
next_button.config(command = next_word)
back_button.config(command = back_word)
button.config(command=find)

# Add status bar to bottom of app
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()
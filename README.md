# Windows Security Policies Parser & Editor

This is a windows security policies parser program written in Python using the tkinter library.


# Task 1
• Import the manually downloaded policies from a predefined trusted location

• Parse and understand the format of data within the imported policy

• Save the same set of policies under a different name in a structured form (as JSON).

# Task 2
• Choose which options to run(by selecting or deselecting options)

• Search by name for an option (via a search bar)

• Select or deselect all options in one click

• Create and `Save As`, `Export to Json` policy that contains only the selected options under the same name or a different one

# Task 3
• Perform an audit of the workstation, using the options that were selected;

• Output the results of the audit on screen.

# Implementation

## Step 1

To run the program use:
```
    python3 path/to/file/text_policy_editor.py
```

## Step 2

Once the desktop app is running go to: 

`File -> Open_file` 

Open the desired windows policy. It will be opened as parsed JSON file.
Make sure it is the right one. Once sure, go to:

`File -> Export`

There will pop-up a window with check boxes that you will select for subsequent export of them into JSON file.
Now you can open it in the default system explorer and see the chosen policies.

`File -> Save_as_file`

It works same as Export, where the pop up a window to choose files to export. However, in this case, you are able to save files in every wanted format as: `.txt`, `.doc`, `.py`, etc.

## Step 3

Open the exported `Json` file with the selected policies with the `Open` funtion and Use `Run Audit` for policy validation.

`File -> Open`
`File -> Run Audit`

## Step 4

Press `Exit` the `Text Editor` window.

`File -> Exit`

Quit the `Text Editor`


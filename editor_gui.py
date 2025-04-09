import PySimpleGUI as sg
import os
import io

run_next_thread = False
base64_image = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAH+UExURQAAAP87If87If87If87If87If87If87If87If87If87ISUjJFAlIe5sFiUjJCMgIfU5IP87If46IPI5IKszH7lxFf93Fv90Fv9xF+pbGsMzINQ2IaovH62jC//xANnNBZGID6yKEfmAE/d4FL9JG9s2IKaRDvPOA+/FBX5UF89EHe04IF9YFf/wAPjeAe/DBL2VENA/Iek6IH9bFv7wAPvlAcKeC7Z1Eug5IKNlFO3gAv7xAPniAfDTA8N6EYstIMyUDuvdAvPNBJF7EfZcGeE3IPmQEfnsAP7oAfjWAvC3B/C1B/CzCIYrIP49IP63Cv+7Cf++Cf/BCNjMBfvoAO/CBdWkCfxBH6EvH6+lC/faAr6bC/CJELkyIP9IL/5zFsi2B/zpAPTRA+m3C7tQKHVTT/7sAPDFBGtZFftJHvw8I/k6IIpCG9WtCHwtH5k7HczABvzsAO7CBYNsE+BYGbIxILUxIOc4IP6UEcq+B/3tAPjfAvjeAtzHBaOZDZZ7EIpDG/5AH+5IJFk/KzYyHaCWDfrjAfHKA3dEGtw/H+o4IU9JGP3sAOK7BquCENc1IO44IIpYGfvnAfnhAc6RDXEvHn9CHOLVBPTUA6yTDfVzFMw0IGknIOPRBPDJBFw8GuVBHtVaGcilCcKQDMEzIPlnGMGLDYU8HMYzIP///xk1TTUAAAARdFJOUwAMWp+/Hg+PLc/vBoP2ARovY7xO3wAAAAFiS0dEqScPBgQAAAAHdElNRQfnCw0WKRQEGPwCAAABjklEQVQ4y2NggANGJmYWQSBgYWZiZMAErMyCSICZFU2ajV0QDbCzIctzcApiAE4OJHkuuLCQMJzJxYFFXlBEVExcQlJKGlkFG5L5MrJyQCCvoKikrAK0BeIOJPepqslBgLqGphbIpWD/IeS1dUCSunJ6+gaGELeAfIvwv5ExSN7E1MzcAh4ewPBDGGBpJSdnbWNrZ4/kWUYGJjjbwREo7+Ts4oocGkwIG9xMwBa4e3h6efv4IuxggbL8/AMCg4JBSkJCw8LhJrAwIJsXEQlUEBUdE4skBlYQB2HHJ8jJJSYlp6BECZIJqWlAV6RnZGZhV5CdYy1nHZWbhx6pcEfmF8hZFxYVl5SWlSPLs8C8WVEJDISq6prauvoGZAXMsIBqbGpuabWWk2tr7+hEDSh4UHd1y8n19Pb1ozqBER5ZEybqTpo8ZSqaE5kR0T1t+oyZs2aj+4EVnmDmzJ03fwG6NCTBgJPcwkWLl2BIw5IcMNEuXbYcUxqRrLl5eFfgk2fg4xcgkHEIZz3CmRd39gcA0k9l8LbQyIEAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjMtMTEtMTNUMjI6NDE6MjArMDA6MDC1A2E6AAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIzLTExLTEzVDIyOjQxOjIwKzAwOjAwxF7ZhgAAACh0RVh0ZGF0ZTp0aW1lc3RhbXAAMjAyMy0xMS0xM1QyMjo0MToyMCswMDowMJNL+FkAAAAASUVORK5CYII='
already_occured = False
replace_this_home = ""
current_home = ""
run_once = True
space_or_no = ""


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def default_house_choice():
    global current_home
    if not os.listdir("homes"):
        pass
    else:
        latest_edited_file = max([f for f in os.scandir("homes")], key=lambda x: x.stat().st_mtime).name
        current_home = "homes/" + latest_edited_file
        return latest_edited_file.replace(".txt", "")


def retrieve_household_items():
    global current_home
    try:
        with open(current_home, 'r') as textfile:
            content = textfile.read().splitlines()
        return content
    except:
        return []


def remove_item(line_user_removed):
    with open(current_home, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        try:
            idx = lines.index(f"{line_user_removed}\n")
        except:
            idx = lines.index(f"{line_user_removed}")
        lines.pop(idx)
        f.truncate()
        f.writelines(lines)


# Input is the search term - returns list that contains all matches - If there is an error, returns -1
def search_for_item(item_query):
    with open(current_home, 'r') as textfile:
        lines = textfile.readlines()
        query_matches = []
        try:
            for line in lines:
                item_info = line.split(',')
                if query.lower() in item_info[0].lower():
                    query_matches.append(line)
        except:
            return -1
    return query_matches


def add_item(new_item):
    set_home = "homes/" + values["_ITEMHOME_"] + ".txt"
    if os.path.exists(set_home):
        pass
    else:
        open(set_home, "w")
    with open(set_home, 'r+') as textfile:
        textfile.seek(0, io.SEEK_END)
        try:
            textfile.write(new_item + "\n")
        except:
            return -1


def amount_homes():
    with open("settings.txt", 'r') as textfile:
        content = textfile.read().splitlines()
    textfile.close()
    return int(content[0].replace("Homes: ", ""))


def prevent_poor_inputs(which_input):
    if values[which_input] and not values[which_input][-1].isdigit():
        window[which_input].update(values[which_input][:-1])
    try:
        if 1 > int(values[which_input]) or int(values[which_input]) > 50:
            window[which_input].update(values[which_input][:-1])
            sg.popup("You can't do 0 and the max is 50 homes/storage units")
    except:
        pass


def change_num_homes():
    global space_or_no
    if 1 <= int(values["_NUMHOMES2_"]) <= 9:
        space_or_no = " "
    else:
        space_or_no = ""
    with open("settings.txt", 'r+') as settings_file:
        settings_file.write("Homes: " + values["_NUMHOMES2_"] + space_or_no)
        settings_file.close()
    window["DROPDOWN_MENU"].update(values=generate_list())
    window["DROPDOWN_MENU2"].update(values=generate_list())
    window["_ITEMHOME_"].update(values=generate_list())


def generate_list():
    homes_list = []
    for number in range(1, amount_homes() + 1):
        homes_list.append("Home " + str(number))
    with open("updated_names.txt", 'r') as textfile:
        name_content = textfile.read().splitlines()
        for name_lines in name_content:
            try:
                changed_home = homes_list[homes_list.index(name_lines)]
                changed_name = name_content[name_content.index(changed_home) + 1]
                homes_list[homes_list.index(changed_home)] = changed_name.replace(".txt", "")
            except:
                pass
    return homes_list


def update_default_inputs():
    window["DROPDOWN_MENU"].update(values=generate_list())
    window["_NUMHOMES2_"].update(value=amount_homes())
    window["_ITEMHOME_"].update(values=generate_list())
    window["DROPDOWN_MENU2"].update(values=generate_list())


sg.theme('Black')

make_these_inputs_visible = [
    [sg.Text("Item Name:"), sg.Push(), sg.Input(size=(20, 1), enable_events=True, key='_ITEMNAME_')],
    [sg.Text("Item Home:"), sg.Push(),
     sg.Combo(values=[], size=(18, 1), readonly=True, enable_events=True, key="_ITEMHOME_")],
    [sg.Text("Item Room:"), sg.Push(), sg.Input(size=(20, 1), enable_events=True, key='_ITEMROOM_')],
    [sg.Text("Item Storage Location:"), sg.Input(size=(20, 1), enable_events=True, key='_ITEMSTORED_')],
    [sg.Button("Add Item", visible=True, button_color=('white', 'green'), key="NEWITEM")]
]

layout1 = [
    [sg.Text("Search Bar"), sg.Input(do_not_clear=True, size=(20, 1), enable_events=True, key='_INPUT_'),
     sg.Image("settingsImage.png", key="_SETTINGS_", enable_events=True)],
    [sg.Listbox(retrieve_household_items(), size=(40, 10), enable_events=True, key='_LIST_', horizontal_scroll=True)],
    [sg.pin(sg.Button("Remove Item", visible=False, button_color=('white', 'red'), key="removal"))],
    [sg.Text("Seeing Inventory for:"),
     sg.Combo(values=[], readonly=True, enable_events=True, key="DROPDOWN_MENU2",
              default_value=default_house_choice())],
    [sg.Checkbox("Add Item", key='_ADDITEM_', enable_events=True, visible=False)],
    [sg.pin(sg.Column(make_these_inputs_visible, visible=False, key="INPUTS"))]
]

layout2 = [
    [sg.Text("How many homes/storage units do you have?:"),
     sg.Input(do_not_clear=True, size=(20, 1), enable_events=True, key='_NUMHOMES_')],
    [sg.Button('Enter', visible=False, bind_return_key=True)]
]

layout3 = [
    [sg.Text("SETTINGS:")],
    [sg.Text("How many homes/storage units do you have?:"),
     sg.Input(do_not_clear=True, size=(20, 1), enable_events=True, key='_NUMHOMES2_', default_text="")],
    [sg.Text("Change home name for:"), sg.Combo(values=[], enable_events=True, key="DROPDOWN_MENU")],
    [sg.Button('Save Changes', visible=True, key="SAVE_CHANGES")]
]

col1 = sg.Column(layout1, key="-COL1-", visible=False)
col2 = sg.Column(layout2, key="-COL2-", visible=True)
col3 = sg.Column(layout3, key="-COL3-", visible=False)

layout = [[col1, col2, col3]]

# Create the window
window = sg.Window("Household Item Finder", layout, icon=base64_image, finalize=True, resizable=False)

if os.path.isfile("settings.txt"):
    window["-COL2-"].update(visible=False)
    window["-COL1-"].update(visible=True)
    update_default_inputs()

# Event loop
while True:
    event, values = window.read(timeout=200)
    if event == "_LIST_":
        window["removal"].update(visible=True)
    if event == "_NUMHOMES2_":
        prevent_poor_inputs("_NUMHOMES2_")
    if event == "_NUMHOMES_" and not os.path.isfile("settings.txt"):
        prevent_poor_inputs("_NUMHOMES_")
    if event == "DROPDOWN_MENU":
        replace_this_home = values["DROPDOWN_MENU"]
    if event == "SAVE_CHANGES":
        if values["_NUMHOMES2_"] == "":
            sg.popup_quick_message("Value of homes/storage units should not be empty!", background_color="red")
        else:
            if replace_this_home.strip() == "":
                change_num_homes()
                pass
            else:
                change_num_homes()
                concise_home_path = "homes/" + replace_this_home + ".txt"
                with open("updated_names.txt", 'r+') as updated_names_file:
                    names_file_content = updated_names_file.readlines()
                    try:
                        try:
                            check_home_index = names_file_content.index(replace_this_home + "\n")
                            add_one_or_zero = 1
                        except:
                            check_home_index = names_file_content.index(replace_this_home + ".txt" + "\n")
                            add_one_or_zero = 0
                        names_file_content[check_home_index + add_one_or_zero] = values["DROPDOWN_MENU"] + ".txt" + "\n"
                        change_filename_to = names_file_content[check_home_index + add_one_or_zero]
                        if os.path.isfile(concise_home_path):
                            os.replace(concise_home_path, "homes/" + change_filename_to)
                        updated_names_file.seek(0)
                        updated_names_file.writelines(names_file_content)
                        updated_names_file.truncate()
                    except:
                        updated_names_file.seek(0, io.SEEK_END)
                        updated_names_file.write(replace_this_home + "\n")
                        updated_names_file.write(values["DROPDOWN_MENU"] + ".txt" + "\n")
                        if os.path.isfile(concise_home_path):
                            os.replace(concise_home_path, "homes/" + values["DROPDOWN_MENU"] + ".txt")
                # change the name of the file to the new name!
                window["DROPDOWN_MENU"].update(values=generate_list())
                window["DROPDOWN_MENU2"].update(values=generate_list())
                window["_ITEMHOME_"].update(values=generate_list())
            sg.popup_quick_message("Settings Saved!", background_color="green")
            window["-COL1-"].update(visible=True)
            window["-COL3-"].update(visible=False)
    if event == "_SETTINGS_":
        window["-COL1-"].update(visible=False)
        window["-COL3-"].update(visible=True)
    if event == "Enter" and not os.path.isfile("settings.txt"):
        num_of_homes = values["_NUMHOMES_"]
        if num_of_homes == "":
            sg.popup("Input is empty!", title="Error")
        else:
            window["-COL2-"].update(visible=False)
            window["-COL3-"].update(visible=False)
            window["-COL1-"].update(visible=True)
            file = open("settings.txt", "w+")
            file.write(f"Homes: {num_of_homes}")
            file.close()
            update_default_inputs()
            # UPDATE generate_list, amount_homes
    if event == "removal":
        selected_item = values['_LIST_']
        selected_item = ''.join(selected_item)
        remove_item(selected_item)
        window["_LIST_"].update(retrieve_household_items())
        window["removal"].update(visible=False)
        sg.popup_quick_message("Item Removed!", background_color="red")
    if event == sg.WINDOW_CLOSED:
        break

    # Search bar input event
    if event == "_INPUT_" and values["_LIST_"] != []:
        query = values["_INPUT_"]

        if query:
            matched_items = search_for_item(query)
            window["_LIST_"].update(matched_items)
        else:
            window["_LIST_"].update(retrieve_household_items())

    # Adds new item to data text file upon clicking the "Add Item" button
    if event == "NEWITEM":
        try:
            if values["_ITEMNAME_"].strip() == "":
                sg.popup_quick_message("Values must not be empty!", background_color="red")
            elif values["_ITEMHOME_"].strip() == "":
                sg.popup_quick_message("Values must not be empty!", background_color="red")
            elif values["_ITEMROOM_"].strip() == "":
                sg.popup_quick_message("Values must not be empty!", background_color="red")
            elif values["_ITEMSTORED_"].strip() == "":
                sg.popup_quick_message("Values must not be empty!", background_color="red")
            else:
                new_item_query = ", ".join(
                    [values["_ITEMNAME_"], values["_ITEMHOME_"], values["_ITEMROOM_"], values["_ITEMSTORED_"]])
                add_item(new_item_query)
                sg.popup_quick_message("Item added successfully!", background_color="green")
                window["_LIST_"].update(retrieve_household_items())
        except:
            sg.popup_quick_message("An error occured!")
    if values["DROPDOWN_MENU2"] == "":
        window["_ADDITEM_"].update(visible=False)
    else:
        window["_ADDITEM_"].update(visible=True)
        current_home = "homes/" + values["DROPDOWN_MENU2"] + ".txt"
        if os.path.exists(current_home):
            pass
        else:
            open(current_home, "w")
        if run_once:
            window["_LIST_"].update(retrieve_household_items())
            run_once = False
    if event == "DROPDOWN_MENU2":
        window["_LIST_"].update(retrieve_household_items())
    # Visibility event for Add Item checkbox
    if event == "_ADDITEM_":
        if values["_ADDITEM_"]:
            window["INPUTS"].update(visible=True)
        else:
            window["INPUTS"].update(visible=False)

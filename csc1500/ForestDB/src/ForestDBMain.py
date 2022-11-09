from tkinter import *;
from tkinter import ttk;
import ForestDatabase;



#Load database from save file
ForestDatabase.load();



#Create a window
window = Tk();
window.title('ForestDB');



#Create the frames for each menu
agreement_frame = ttk.Frame(window, padding=10);
main_frame = ttk.Frame(window, padding=10);

query_frame = ttk.Frame(window, padding=10);
query_options_frame = ttk.Frame(query_frame, padding=10);
query_output_frame = ttk.Frame(query_frame, padding=10);

manage_frame = ttk.Frame(window, padding=10);
manage_options_frame = ttk.Frame(manage_frame, padding=10);
manage_options_frame.grid(columns=2, rows=1);
manage_add_frame = ttk.Frame(manage_options_frame);
manage_add_frame.grid(columns=2, rows=len(ForestDatabase.template_field_names)+1);
manage_sav_frame = ttk.Frame(manage_options_frame);
manage_sav_frame.grid(columns=3, rows=2);

manage_viewdb_frame = ttk.Frame(manage_frame, padding=10);

info_frame = ttk.Frame(window, padding=10);


###################
# AGREEMENT FRAME #
###################
#Legal user agreement
agreement = '';
agreement += 'By using this software you agree not to sell or distribute\n'
agreement += 'data without the express consent of Forestview\n\n'
agreement += 'You hereby indemnify Forestview from all legal ramnifications\n'
agreement += 'regarding data breaches, zero-day attacks, and database worms.\n\n'
agreement += 'Vendors are required to make periodic vulnerability\n'
agreement += 'assessments of this system. This agreement is subject\n'
agreement += 'to change, and will change to stay accurate with the\n'
agreement += 'current security and technology climate.'

ttk.Label(master=agreement_frame, text='Agreement').pack();
ttk.Label(master=agreement_frame, text=agreement).pack();

#Runs when accepting user agreement
def agreementButton():
    main_frame.pack();
    info_frame.pack();
    agreement_frame.pack_forget();

ttk.Button(master=agreement_frame, text='I Agree', command=agreementButton).pack()








###################
# MAIN MENU FRAME #
###################
def selectQueryMenu():
    query_frame.pack();
    manage_frame.pack_forget();
    info_frame.pack_forget();

def selectManageMenu():
    manage_frame.pack();
    query_frame.pack_forget();
    info_frame.pack_forget();

def selectIfoMenu():
    info_frame.pack();
    manage_frame.pack_forget();
    query_frame.pack_forget();

Button(main_frame, text='Query Menu', command=selectQueryMenu).pack(side=LEFT);
Button(main_frame, text='Manage Menu', command=selectManageMenu).pack(side=LEFT);
Button(main_frame, text='Info', command=selectIfoMenu).pack(side=LEFT);





##############
# INFO FRAME #
##############
info = '';
info += "	The ForestDB application currently has two main menus for\n"
info += "querying and managing the database. These menus are called the query\n"
info += "and manage menu respectively. Each employee has fields which store their\n"
info += "data. For example, one employee field is their name, which stores that one\n"
info += "particular employee’s name. If you want to query employees by name, you\n"
info += "should first select the name option from the drop down menu, and then enter\n"
info += "the name you wish to query for. Pressing the query button will execute the\n"
info += "query based on the currently selected field and the value to query by.\n"
info += "You can query employees by any field that they contain, such as ssn, email,\n"
info += "phone, skills etc. The manage menu provides multiple database tools which\n"
info += "manage the database. First off there is a save and backup button. The save\n"
info += "button will save any added employees to the database. When entering data\n"
info += "into the database, it is important to save the database before closing the\n"
info += "program, otherwise that data will be lost. The backup button automatically\n"
info += "generates a new backup of the database at the point in time in which the\n"
info += "button was pressed. Backups are unlimited, and the next backup will be\n"
info += "place in the data/backups folder with a name and a number, the higher the\n"
info += "number, the later in time the backup. The main database file is saved into\n"
info += "data/databases/forestdb, it is important to restrict privilege to this file,\n"
info += "as it contains all the employee data of the database. The add button will add\n"
info += "an employee to the database, assuming all of the fields of the employee are\n"
info += "filled out correctly below the add button. If the fields are not filled out\n"
info += "correctly, the label next to the add button will be updated with an error.\n"
info += "In order to remove an employee from the database, simply type their unique id\n"
info += "(found leftmost of the employee’s data in the database view box) and then press\n"
info += "the ‘Remove Employee’ button. They will be deleted from the database. At this\n"
info += "point in time, there is no way to edit an employee currently in the database.\n"
info += "If you wish to edit an employee’s fields that is currently in the database,\n"
info += "you should delete the employee and re-enter their data."

info_lbl = Label(info_frame, text=info);
info_lbl.pack(side=LEFT);







###############
# QUERY FRAME #
###############

#
# Query Options Frame
#

#Create drop down menu for which field to query by
query_field_var = StringVar(query_options_frame);
query_field_var.set('name');
query_field_menu = OptionMenu(query_options_frame, query_field_var, *ForestDatabase.template_field_names);

#Create text entry box for value to query by
query_value_box = Text(query_options_frame, height=1, width=30);

#Executes the query function
def doQuery():
    value = query_value_box.get(1.0, 'end-1c');
    field = query_field_var.get();

    results = ForestDatabase.DATABASE.query(field, value);
    query_output_listbox.delete(0, END);

    if(value == ''):
        results = ForestDatabase.DATABASE.entries;

    for result in results:
        query_output_listbox.insert(END, results[result]);
        
#Create query button (uses doQuery() function)
query_button = Button(master=query_options_frame, text='Query', command=doQuery);

query_button.pack(side=LEFT);
query_field_menu.pack(side=LEFT);
query_value_box.pack(side=LEFT);
query_options_frame.pack(side=TOP);


#
# Query Output Frame
#

#Create output & scrollbar
query_output_scrollbar = ttk.Scrollbar(master=query_output_frame, orient='vertical');
query_output_listbox = Listbox(master=query_output_frame, width=180);
for uid in ForestDatabase.DATABASE.entries:
    query_output_listbox.insert(END, ForestDatabase.DATABASE.entries[uid]);

#Link scrollbar & output box together
query_output_listbox.config(yscrollcommand = query_output_scrollbar.set);
query_output_scrollbar.config(command=query_output_listbox.yview);

query_output_scrollbar.pack(side=RIGHT, fill=BOTH);
query_output_listbox.pack(side=LEFT, fill=BOTH);
query_output_frame.pack(side=BOTTOM);






################
# MANAGE FRAME #
################

#
# Manage Options Frame
#
# Adding Employees
#

#Create an entry box for each field
field_entry_boxes = [];
for i in range(len(ForestDatabase.template_field_names)):
    lbl = Label(manage_add_frame, text=ForestDatabase.template_field_names[i]);
    lbl.grid(column=0, row=1+i);
    
    field_entry_boxes.append(Text(manage_add_frame, height=1, width=20));
    field_entry_boxes[i].grid(column=1, row=1+i);

#Info label
add_ifo_lbl = Label(manage_add_frame, text='Enter Employee Data');
add_ifo_lbl.grid(column=1, row=0);

invalid_chars = '!#$%^&*()-=_+~`:;{}[]\\|\'\"<>,/?';

#Adds a user from the text entry boxes if possible
def addEmployee():
    #Gets values from all the boxes
    values = [];
    for entry_box in field_entry_boxes:
        values.append(entry_box.get(1.0, 'end-1c'));

    #Attempts to cast them to the proper type
    corrected_values = [];
    success = True;
    for i in range(len(values)):
        #Ensure data was entered
        if(len(values[i]) < 1):
            success = False;
            break;
        
        #Ensure entered data doesn't have invalid chars
        for c in invalid_chars:
            if(c in values[i]):
                add_ifo_lbl.config(text='Invalid Char {0}'.format(c));
                success = False;
                break;

        #Ensure data is correct format
        try:
            corrected_values.append(ForestDatabase.template_field_types[i](values[i]));
        except:
            add_ifo_lbl.config(text='Invalid {0}'.format(ForestDatabase.template_field_names[i]));
            success = False;
            break;

    if(not success):
        return;

    #Adds the employee
    ForestDatabase.DATABASE.append(ForestDatabase.Employee(corrected_values));
    add_ifo_lbl.config(text='Added User');
    updateManageViewbox();

    #Clears the boxes
    for entry_box in field_entry_boxes:
        entry_box.delete(1.0, END);
        

#First row add button
add_button = Button(manage_add_frame, text='Add', command=addEmployee);
add_button.grid(column=0, row=0);


#
# Manage Options Frame
#
# Removing Employees & Saving / Backup
#

Label(manage_sav_frame, text='   ').grid(column=1, row=0);
Label(manage_sav_frame, text='   ').grid(column=1, row=1);

remove_box = Text(manage_sav_frame, height=1, width=20);
remove_box.grid(column=2, row=1);

def saveButton():
    ForestDatabase.save();

def backupButton():
    ForestDatabase.backup();

def removeEmployee():
    entered = remove_box.get(1.0, 'end-1c');
    uid = -1;
    try:
        uid = int(entered);
        del ForestDatabase.DATABASE.entries[uid];
        updateManageViewbox();
    except:
        raise;
        return;
    
    

    
remove_btn = Button(manage_sav_frame, text='Remove Employee', command=removeEmployee);
remove_btn.grid(column=2, row=0)

save_btn = Button(manage_sav_frame, text='Save', command=saveButton);
backup_btn = Button(manage_sav_frame, text='Backup', command=backupButton);
save_btn.grid(column=0, row=0);
backup_btn.grid(column=0, row=1);


manage_add_frame.grid(column=0);
manage_sav_frame.grid(column=1);
manage_options_frame.pack(side=LEFT);


#
# Manage View Database Frame
#

#Create output & scrollbar
manage_viewdb_scrollbar = ttk.Scrollbar(master=manage_viewdb_frame, orient='vertical');
manage_viewdb_listbox = Listbox(master=manage_viewdb_frame, width=100);

def updateManageViewbox():
    manage_viewdb_listbox.delete(0, END);
    
    for uid in ForestDatabase.DATABASE.entries:
        manage_viewdb_listbox.insert(END, '{0}: {1}'.format(uid, ForestDatabase.DATABASE.entries[uid]));

updateManageViewbox();

#Link scrollbar & output box together
manage_viewdb_listbox.config(yscrollcommand = manage_viewdb_scrollbar.set);
manage_viewdb_scrollbar.config(command=manage_viewdb_listbox.yview);

manage_viewdb_scrollbar.pack(side=RIGHT, fill=BOTH);
manage_viewdb_listbox.pack(side=LEFT, fill=BOTH);
manage_viewdb_frame.pack(side=RIGHT);

agreement_frame.pack(side=RIGHT);
window.mainloop();

import AbstractDatabase;
import FileManager;

##################
# ForestDatabase #
##################
# Developed by Ryan Alsobrooks
# Database implementation for Forestview

#Name of the active database save file
FNAME = 'forestdb';



#Define a template for how to store data in each entry
template_field_names = ['name', 'position', 'address', 'email', 'phone', 'ssn', 'skills'];
template_field_types = [str, str, str, str, int, int, str];
EMPLOYEE_TEMPLATE = AbstractDatabase.EntryTemplate(template_field_names, template_field_types);

#Employee object builder
Employee = lambda fields: AbstractDatabase.Entry(EMPLOYEE_TEMPLATE, fields);

#Define database
DATABASE = AbstractDatabase.Database(EMPLOYEE_TEMPLATE);



#Loads database into memeory from primary save file
def load():
    if(FileManager.dbExists(FNAME)):
        DATABASE.merge(FileManager.loadDb(FNAME));
        print('Loaded database from {0}'.format(FNAME));
    else:
        print('{0} not found'.format(FNAME));

#Saves the database
def save():
    FileManager.saveDb(FNAME, DATABASE);

#Saves a new backup of the current database
def backup():
    FileManager.genNewBackup(DATABASE);

#Loads the database from a backup
#Version is the number of versions behind the latest backup
def loadBackup(version):
    latest = FileManager.getCurrentBackup();
    selected = latest - version;
    if(FileManager.backupExists(selected)):
        DATABASE = FileManager.loadBackup(selected);
        print('Loaded database from backup{0}'.format(selected));
    else:
        print('backup{0} not found'.format(selected));

#Loads another database and merges it with the current version
def loadAndMerge(name):
    if(FileManager.dbExists(name)):
        loaded = FileManager.loadDb(name);
        DATABASE.merge(loaded);
        print('Merged {0} with {1}'.format(name, FNAME));


    
    
    

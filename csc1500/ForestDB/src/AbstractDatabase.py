import random;

####################
# AbstractDatabase #
####################
# Developed by Ryan Alsobrooks
# Abstract database definition



#Utility class for generating random unique ids
class UUID:
    def __init__(self):
        self.uid = random.randint(0, max_int);

    def __str__(self):
        return str(self.uid);

    

#A class used to define the template of every database entry
class EntryTemplate:
    def __init__(self, field_names, field_types):
        if(len(field_names) != len(field_types)):
            raise Exception('CRITICAL::FORESTDB::ABSTRACTDB::ENTRYTEMPLATE Field Name & Type Mismatch');
        self.field_names = field_names;
        self.field_types = field_types;

    def __str__(self):
        out = '';
        for i in range(len(self.field_names)):
            out += '{0}:{1},'.format(self.field_names[i], self.field_types[i]);
        return out[0:len(out)-1];


            
#Class for storing all data about a database entry
class Entry:
    def __init__(self, template, fields):
        self.template = template;
        self.fields = fields;

    #Returns true if the employee contains a specified value for a given field
    def query(self, field_name, value):
        #Get location of desired field, return False if it doesn't exist
        fieldloc = self.template.field_names.index(field_name);
        if(fieldloc == -1):
            return False;
        
        #Return True if a string field contains value, otherwise return exact comparison
        if(self.template.field_types[fieldloc] == str):
            return value in self.fields[fieldloc];
        else:
            return value == self.fields[fieldloc];

    def __str__(self):
        out = '';
        for i in range(len(self.template.field_types)):
            out += '{0}:{1},'.format(self.template.field_names[i], self.fields[i]);
        return out[0:len(out)-1];



#Manages a database dictionary
class Database:
    def __init__(self, template):
        self.template = template;
        self.entries = {};

    def merge(self, somedb):
        if(somedb.template != self.template):
            raise Exception('ERROR::FORESTDB::ABSTRACTDB::DATABASE::MERGE Template Mismatch');
            return;
        self.entries.update(somedb.entries);

    def append(self, entry):
        if(entry.template != self.template):
            raise Exception('ERROR::FORESTDB::ABSTRACTDB::DATABASE::APPEND Template Mismatch');
            return;
        self.entries.update({UUID(), entry});

    def remove(self, uuid):
        del self.entries[uuid];

    def query(self, field_name, value):
        results = {};
        
        for uuid in entries:
            if(self.entries[uuid].query(field_name, value)):
                results.update({uuid : self.entries[uuid]});

        return results;

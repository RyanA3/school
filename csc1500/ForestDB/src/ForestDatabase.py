import AbstractDatabase;

##################
# ForestDatabase #
##################
# Developed by Ryan Alsobrooks
# Database implementation for Forestview



#Define a template for how to store data in each entry
template_field_names = ['name', 'position', 'address', 'email', 'phone', 'ssn', 'skills'];
template_field_types = [str, str, str, str, int, int, str];
EMPLOYEE_TEMPLATE = AbstractDatabase.EntryTemplate(template_field_names, template_field_types);



#Employee object builder
Employee = lambda fields: AbstractDatabase.Entry(EMPLOYEE_TEMPLATE, fields);



#Define database and load into memory
DATABASE = AbstractDatabase.Database(EMPLOYEE_TEMPLATE);

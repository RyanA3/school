import os;
import pickle;




#Utility function for mkdir since python's implementation is awful
def mkdir(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path);
        except:
            raise;



#Get current location & location for saving files
CURRENT_FOLDER = os.getcwd();
CURRENT_FOLDER = CURRENT_FOLDER[0:len(CURRENT_FOLDER)-4];
DATA_FOLDER = '{0}/data'.format(CURRENT_FOLDER);
BACKUP_FOLDER = '{0}/backups'.format(DATA_FOLDER);
DATABASE_FOLDER = '{0}/databases'.format(DATA_FOLDER);
FOREST_DB = 'forestdb';

#Ensure directories exist
mkdir(DATA_FOLDER);
mkdir(BACKUP_FOLDER);
mkdir(DATABASE_FOLDER);




#Generates name of a backup file
backup_file = lambda num: '{0}/backup{1}'.format(BACKUP_FOLDER, num);

#Generates name of a db file
db_file = lambda name: '{0}/{1}'.format(DATABASE_FOLDER, name);

#Returns the current latest backup
def getCurrentBackup():
    num = 0;
    for f in os.listdir(BACKUP_FOLDER):
        try:
            cur = int(f[6:len(f)]);
            if(cur > num):
                num = cur;
        except:
            continue;
    return num;



#Generates a new backup given the current database
def genNewBackup(database):
    data = pickle.dumps(database);
    newbackup = open(backup_file(getCurrentBackup()+1), 'wb');
    newbackup.write(data);
    newbackup.close();

#Loads a backup
def loadBackup(num):
    latest = getCurrentBackup();
    if(num > latest):
        raise Exception('Attempted to load a backup later than the latest version');
        return;
    db = pickle.load(open(backup_file(num), 'rb'));
    return db;

#Loads a database
def loadDb(name):
    try:
        somef = open(db_file(name), 'rb');
        db = pickle.load(somef);
        return db;
    except:
        raise;

#Saves a database
def saveDb(name, database):
    try:
        somef = open(db_file(name), 'wb');
        data = pickle.dumps(database);
        somef.write(data);
        somef.close();
    except:
        raise;
    
    

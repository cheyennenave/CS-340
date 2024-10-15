from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        USER = username
        PASS = password 
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31670 # changing this to match Dr. Wilsons port #
        DB = 'AAC' # changing this to match Dr. Wilson database
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        #shelter = AnimalShelter(username, password, HOST, PORT, DB, COL)

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary  
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, searchData):
        #queries for docs from aac database with animals collection
        if searchData:
            # This if conditions will return items based on searchData criteria
            data = self.database.animals.find(searchData, {"_id": False})
        else:
            # your else statement should return all items
            data = self.database.animals.find({}, {"_id": False})
        # not that you have the results, you can return a list
        return list(data)
    
# Create method to implement the U in CRUD.
    def update(self, searchData, updateData):
        #updates animal data changes based on input
        if searchData is not None:
            result = self.database.animals.update_many(searchData, { "$set" : updateData})
        else:
            return "{}"
        return result

# Create method to implement the D in CRUD
    def delete(self, deleteData):
        #deletes animal data based on input
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        return result
        
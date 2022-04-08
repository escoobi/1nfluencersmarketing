import pymongo

class Connect:

    client = pymongo.MongoClient("mongodb+srv://1nfluencersmarketing:"
                             "dir70-ti@1nfluencersmarketing.g9iny.mongodb.net/"
                             "1nfluencersmarketing?retryWrites=true&w=majority")
    db = client.db01

from init import Initialization


class DB:
    def __init__(self):
        self.DB = None

    def setupDB(self):
        print('Creating database...')
        self.DB = {}
        init = Initialization()
        self.DB = init.loadData(DB)

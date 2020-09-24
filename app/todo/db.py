# app/todo/db.py
# Natawut Nupairoj
# Department of Computer Engineering, Chulalongkorn University
# Created for 2110415 Software Defined Systems

class Database:
    # handle singleton pattern
    __instance = None

    @staticmethod
    def getInstance():
        if Database.__instance == None:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Database.__instance = self
            self.__last_id = 0
            self.__data = {}

    def add(self, todo):
        id = self.__last_id
        self.__last_id += 1
        self.__data[id] = todo
        return id

    def get(self, id):
        if id in self.__data:
            return self.__data[id]
        return None

    def get_all(self):
        if len(self.__data) > 0:
            return list(self.__data.values())
        else:
            return []

    def search(self, q, tags):
        r = []
        tagset = set(tags)
        if len(self.__data) > 0:
            if q == '' and len(tagset) == 0:
                r = list(self.__data.values())
            else:
                for id in self.__data:
                    todo = self.__data[id]
                    in_q = (q == '') or (q in todo['title']) or (q in todo['detail'])
                    in_t = (len(tagset) == 0) or (len(set(todo['tags']) & tagset) > 0)
                    if in_q and in_t:
                        r.append(todo)
        return r



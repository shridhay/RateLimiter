from datetime import datetime

class RateLimiter:

    def __init__(self, limit, reject=False):
        assert limit > 0
        self.limit = limit
        self.countRejects = reject
        self.requests = {}  

    def allowRequest(self, uuid, timestamp):
        if uuid not in self.requests:
            self.requests[uuid] = (timestamp, 1)
            return True
        if timestamp > self.requests[uuid][0]:
            self.requests[uuid] = (timestamp, 1)
            return True
        if self.requests[uuid][1] < self.limit:
            self.requests[uuid] = (timestamp, self.requests[uuid][1] + 1)
            return True
        elif self.countRejects:
            self.requests[uuid] = (timestamp, self.requests[uuid][1] + 1)
            return False
        else:
            return False

    def getNumberOfRequestsUUID(self, uuid):
        return self.requests[uuid][1] if uuid in self.requests else -1

    def getNumberOfRequests(self):
        return {uuid : self.requests[uuid][1] for uuid in self.requests}

    def printNumberOfRequestsUUID(self, uuid):
        print(self.requests[uuid][1] if uuid in self.requests else -1)

    def printNumberOfRequests(self):
        print({uuid : self.requests[uuid][1] for uuid in self.requests})

    def printUUIDs(self):
        print(list(self.requests.keys()))

    def printRequests(self):
        print(self.requests)

    def printLimit(self):
        print(self.limit)

    def getRequests(self):
        return self.requests

    def getUUIDs(self):
        return list(self.requests.keys())

    def getRequestsUUID(self, uuid):
        return [] if uuid not in self.requests else self.requests[uuid]

    def getLimit(self):
        return self.limit

    def printCountRejects(self):
        print(self.countRejects)

    def getCountRejects(self):
        return self.countRejects

    def setCountRejects(self, reject):
        self.countRejects = reject

    def setLimit(self, limit):
        self.limit = limit

    def clearRequests(self):
        self.requests.clear()

    def clearAllRequests(self):
        for uuid in self.requests:
            self.requests[uuid] = (0, 0)

    def clearRequestsUUID(self, uuid):
        if uuid in self.requests:
            self.requests[uuid] = (0, 0)

    def clearCountRejects(self):
        self.countRejects = False

    def evictUUID(self, uuid):
        if uuid in self.requests:
            del self.requests[uuid]


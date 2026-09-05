from collections import deque
from datetime import datetime

class RateLimiter:
        
    def __init__(self, limit, window=1, reject=False):
        assert limit > 0
        self.limit = limit
        self.window = window
        self.reject = reject
        self.requests = {}
    
    def allowRequest(self, uuid, timestamp):
        if uuid not in self.requests:
            self.requests[uuid] = deque([timestamp])
            return True
        q = self.requests[uuid]
        while q and timestamp - q[0] > self.window:
            q.popleft()
        if len(q) >= self.limit:
            if self.reject:
                q.append(timestamp)
            return False
        else:
            q.append(timestamp)
            return True

    def getNumberOfRequestsUUID(self, uuid):
        return len(self.requests[uuid]) if uuid in self.requests else -1

    def getNumberOfRequests(self):
        return {uuid : len(self.requests[uuid]) for uuid in self.requests}

    def printNumberOfRequestsUUID(self, uuid):
        print(len(self.requests[uuid]) if uuid in self.requests else -1)
        
    def printNumberOfRequests(self):
        print({uuid : len(self.requests[uuid]) for uuid in self.requests})
    
    def printUUIDs(self):
        print(list(self.requests.keys()))

    def printRequests(self):
        print(self.requests)

    def printRequestsUUID(self, uuid):
        print([] if uuid not in self.requests else self.requests[uuid])

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

    def printAppendRejects(self):
        print(self.reject)

    def getAppendRejects(self):
        return self.reject

    def setAppendRejects(self, reject):
        self.reject = reject

    def setLimit(self, limit):
        self.limit = limit

    def clearAllRequests(self):
        self.requests.clear()

    def clearRequestsUUID(self, uuid):
        if uuid in self.requests:
            self.requests[uuid].clear()

    def clearAppendRejects(self):
        self.reject = False

    def evictUUID(self, uuid):
        if uuid in self.requests:
            del self.requests[uuid]

    def addUUID(self, uuid):
        if uuid not in self.requests:
            self.requests[uuid] = deque()

from collections import deque
from datetime import datetime

class RateLimiter:

    # If reject is set to true, rejected requests will still be recorded in requests, if set to false rejected requests will not be recorded.
    
    def __init__(self, limit, reject=False):
        assert limit > 0
        self.limit = limit
        self.appendRejects = reject
        self.requests = {}

    # Important to note that requests will always arrive in a non-decreasing order due to the arrow of time. Stale requests will be removed via q.popleft(). New requests will be appended via q.append(elem).

    def allowRequest(self, uuid, now):        
        if uuid not in self.requests:
            self.requests[uuid] = deque([now])
            return True
        else:
            q = self.requests[uuid]
            while q and now - q[0] > 2:    
                q.popleft()
            if len(q) >= self.limit:
                if self.appendRejects:
                    q.append(now)
                return False
            else:
                q.append(now)
                return True

    def getNumberOfRequestsUUID(uuid):
        return len(self.requests[uuid]) if uuid in self.requests else -1

    def getNumberOfRequests():
        return {uuid : len(self.requests[uuid]) for uuid in self.requests}

    def printNumberOfRequestsUUID(uuid):
        print(len(self.requests[uuid]) if uuid in self.requests else -1)
        
    def printNumberOfRequests():
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
        print(self.appendRejects)

    def getAppendRejects(self):
        return self.appendRejects

    def setAppendRejects(self, reject):
        self.appendRejects = reject

    def setLimit(self, limit):
        self.limit = limit

    def clearAllRequests(self):
        self.requests.clear()

    def clearRequestsUUID(self, uuid):
        if uuid in self.requests:
            self.requests[uuid].clear()

    def clearAppendRejects(self):
        self.appendRejects = False

    def evictUUID(self, uuid):
        if uuid in self.requests:
            del self.requests[uuid]

    def addUUID(self, uuid):
        if uuid not in self.requests:
            self.requests[uuid] = deque()

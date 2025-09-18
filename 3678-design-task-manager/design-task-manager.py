import heapq

class TaskManager(object):
    def __init__(self, tasks):
        self.task_info = {}
        self.heap = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId, taskId, priority):
        self.task_info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        if taskId in self.task_info:
            userId, _ = self.task_info[taskId]
            self.task_info[taskId] = (userId, newPriority)
            heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId):
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self):
        while self.heap:
            negPri, negTid, tid = heapq.heappop(self.heap)
            pri = -negPri
            if tid in self.task_info and self.task_info[tid][1] == pri:
                userId, _ = self.task_info.pop(tid)
                return userId
        return -1

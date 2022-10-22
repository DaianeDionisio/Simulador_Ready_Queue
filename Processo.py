class Processo(object):
    def __init__(self, process, arrivalTime, burstTime, priority):
        self.process = process
        self.arrivalTime = int(arrivalTime)
        self.bursTime = int(burstTime)
        self.priority = int(priority)
        self.lastRun = 0
        self.runBefore = 0
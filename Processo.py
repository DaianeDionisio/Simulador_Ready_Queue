class Processo(object):
    def __init__(self, process, arrivalTime, burstTime, priority):
        self.process = process
        self.arrivalTime = arrivalTime
        self.bursTime = burstTime
        self.priority = priority
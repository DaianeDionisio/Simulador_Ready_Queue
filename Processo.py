class Processo(object):
    def __init__(self, process, arrivalTime, burstTime, priority):
        self.process = process #nome
        self.arrivalTime = int(arrivalTime)
        self.bursTime = int(burstTime)
        self.priority = int(priority)
        # última execução, para cálculo do tempo de espera do processo
        self.lastRun = 0
        # o quanto foi executado antes da última execução, para cálculo do tempo de espera do processo
        self.runBefore = 0
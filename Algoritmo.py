from Processo import  Processo

class Algoritmo(object):

    def __init__(self, decisioAlgorithm, process):
        self.decisioAlgorithm = decisioAlgorithm
        self.process: list[Processo] = []
        self.process = process

        if(self.decisioAlgorithm == "1"):
            self.priorityScheduling(self.process)
        elif(decisioAlgorithm == "2"):
            self.roundRobin(self.process)

    def priorityScheduling(self, process):
        self.process: list[Processo] = []
        self.process = process

        arrivalTime = 0
        processMorePriority = Processo
        oldProcessMorePriority = Processo
        indiceProcessMorePriority = 0

        while(len(self.process)):
            priority = 100

            for i in self.process:
                if(int(i.arrivalTime) <= arrivalTime and int(i.priority) < priority):
                    processMorePriority = i
                    indiceProcessMorePriority = process.index(i)
                    priority = int(i.priority)

            if(processMorePriority != oldProcessMorePriority):
                print(arrivalTime, " - Processo em Execução: ", processMorePriority.process)
                arrivalTime = arrivalTime + int(processMorePriority.bursTime)
                oldProcessMorePriority = processMorePriority
                self.process.pop(indiceProcessMorePriority)

            else:
                arrivalTime = arrivalTime+1

        print(arrivalTime, "- Fim da execução dos processos")

    def roundRobin(self, process):
        self.process: list[Processo] = []
        self.process = process
        for i in self.process:
            print(i.process)

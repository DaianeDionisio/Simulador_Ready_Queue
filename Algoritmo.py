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
                print(arrivalTime, " - Sem processo dispovível para execução no momento")
                arrivalTime = arrivalTime+1

        print(arrivalTime, "- Fim da execução dos processos")

    def roundRobin(self, process):
        self.process: list[Processo] = []
        self.process = process

        print("Qual o valor do quantum?")
        quantum = int(input())

        arrivalTime = 0
        numProcessos = len(self.process)

        while (numProcessos):
            numProcessosArrivalTime = numProcessos
            for i in self.process:
                if(int(i.arrivalTime) <= arrivalTime):
                    if(int(i.bursTime) > 0):
                        print(arrivalTime, " - Processo em Execução: ", i.process)

                        if(numProcessos == 1):
                            arrivalTime = arrivalTime + int(i.bursTime)
                            i.bursTime = 0
                            numProcessos = numProcessos-1

                        else:
                            if(int(i.bursTime)>= quantum):
                                arrivalTime = arrivalTime + quantum
                                i.bursTime = int(i.bursTime) - quantum
                                if(i.bursTime == 0):
                                    numProcessos = numProcessos-1

                            else:
                                arrivalTime = arrivalTime + int(i.bursTime)
                                i.bursTime = 0
                                numProcessos = numProcessos-1

                else:
                    numProcessosArrivalTime = numProcessosArrivalTime-1

            if(numProcessosArrivalTime == 0):
                print(arrivalTime, " - Sem processo dispovível para execução no momento")
                arrivalTime = arrivalTime + 1

        print(arrivalTime, "- Fim da execução dos processos")
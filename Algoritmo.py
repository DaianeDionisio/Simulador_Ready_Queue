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
        numProcessos = len(self.process)

        while(numProcessos):
            priority = 100

            for i in self.process:
                if(i.arrivalTime <= arrivalTime and i.priority < priority and i.bursTime > 0):
                    processMorePriority = i
                    indiceProcessMorePriority = process.index(i)
                    priority = i.priority

            if(processMorePriority != oldProcessMorePriority):
                print(arrivalTime, " - Processo em Execução: ", processMorePriority.process)
                process[indiceProcessMorePriority].lastRun = arrivalTime
                arrivalTime = arrivalTime + processMorePriority.bursTime
                oldProcessMorePriority = processMorePriority
                process[indiceProcessMorePriority].bursTime = 0
                numProcessos = numProcessos-1

            else:
                print(arrivalTime, " - Sem processo dispovível para execução no momento")
                arrivalTime = arrivalTime+1

        print(arrivalTime, "- Fim da execução dos processos")
        self.calculateAverageTime(process)

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
                if(i.arrivalTime <= arrivalTime):
                    if(i.bursTime > 0):
                        print(arrivalTime, " - Processo em Execução: ", i.process)
                        i.lastRun = arrivalTime

                        if(numProcessos == 1):
                            arrivalTime = arrivalTime + i.bursTime
                            i.bursTime = 0
                            numProcessos = numProcessos-1

                        else:
                            if(i.bursTime >= quantum):
                                arrivalTime = arrivalTime + quantum
                                i.bursTime = i.bursTime - quantum
                                if(i.bursTime == 0):
                                    numProcessos = numProcessos-1
                                else:
                                    i.runBefore = i.runBefore + quantum

                            else:
                                arrivalTime = arrivalTime + i.bursTime
                                i.bursTime = 0
                                numProcessos = numProcessos-1

                else:
                    numProcessosArrivalTime = numProcessosArrivalTime-1

            if(numProcessosArrivalTime == 0):
                print(arrivalTime, " - Sem processo dispovível para execução no momento")
                arrivalTime = arrivalTime + 1

        print(arrivalTime, "- Fim da execução dos processos")
        self.calculateAverageTime(process)

    def calculateAverageTime(self, process):
        somaTEPX = 0

        for i in process:
            somaTEPX = somaTEPX + (i.lastRun - i.runBefore - i.arrivalTime)

        averageTime = somaTEPX/len(process)

        print("Tempo médio de espera: ", averageTime, "ms")




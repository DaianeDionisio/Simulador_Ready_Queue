from Processo import Processo

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

        time = 0
        processMorePriority = Processo
        oldProcessMorePriority = Processo
        numProcess = len(self.process)

        while(numProcess):
            priority = 1000

            for i in self.process:
                if(i.arrivalTime <= time and i.priority < priority and i.bursTime > 0):
                    processMorePriority = i
                    indexProcessMorePriority = self.process.index(i)
                    priority = i.priority

            if(processMorePriority != oldProcessMorePriority):
                print(time, " - Processo em Execução: ", processMorePriority.process)
                self.process[indexProcessMorePriority].lastRun = time
                time = time + processMorePriority.bursTime
                oldProcessMorePriority = processMorePriority
                self.process[indexProcessMorePriority].bursTime = 0
                numProcess = numProcess-1

            else:
                print(time, " - Sem processo dispovível para execução no momento")
                time = time+1

        print(time, "- Fim da execução dos processos")
        self.calculateAverageTime(process)

    def roundRobin(self, process):
        self.process: list[Processo] = []
        self.process = process

        print("Qual o valor do quantum?")
        quantum = int(input())

        time = 0
        numProcess = len(self.process)

        while (numProcess):
            numRunningProcesses = numProcess
            for i in self.process:
                if(i.arrivalTime <= time):
                    if(i.bursTime > 0):
                        print(time, " - Processo em Execução: ", i.process)
                        i.lastRun = time

                        if(numProcess == 1):
                            time = time + i.bursTime
                            i.bursTime = 0
                            numProcess = numProcess-1

                        else:
                            if(i.bursTime >= quantum):
                                time = time + quantum
                                i.bursTime = i.bursTime - quantum
                                if(i.bursTime == 0):
                                    numProcess = numProcess-1
                                else:
                                    i.runBefore = i.runBefore + quantum

                            else:
                                time = time + i.bursTime
                                i.bursTime = 0
                                numProcess = numProcess-1

                else:
                    numRunningProcesses = numRunningProcesses-1

            if(numRunningProcesses == 0):
                print(time, " - Sem processo disponível para execução no momento")
                time = time + 1

        print(time, "- Fim da execução dos processos")
        self.calculateAverageTime(process)

    def calculateAverageTime(self, process):
        somaTEPX = 0

        for i in process:
            somaTEPX = somaTEPX + (i.lastRun - i.runBefore - i.arrivalTime)

        averageTime = somaTEPX/len(process)

        print("Tempo médio de espera: ", averageTime, "ms")
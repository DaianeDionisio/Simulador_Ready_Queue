from Processo import Processo
from Algoritmo import Algoritmo

processos: list[Processo] = []

menu = True
while (menu):
    processos.clear()
    print("--------------Simulador de fila de prontos--------------")
    print("Adicione os processos:")
    processMenu = True

    while(processMenu):
        print("Índice do processo:")
        process = input()
        print("Arrival Time:")
        arrivalTime = input()
        print("Burst Time:")
        burstTime = input()
        print("Priority:")
        priority = input()
        newProcess = Processo(process,arrivalTime,burstTime,priority)
        processos.append(newProcess)

        print("Deseja adicionar mais processos?:")
        print("1 - sim")
        print("2 - não")
        decisionProcess = input()

        if(decisionProcess == "2"):
            processMenu = False

    print("Escolha o algoritmo desejado:")
    print("1 - Priority Scheduling")
    print("2 - Round Robin")
    decisioAlgorithm = input()
    newAlgorithm = Algoritmo(decisioAlgorithm, processos)




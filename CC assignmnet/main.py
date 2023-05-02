import math as math

global  Primes
Primes=[]


def CheckPrimes(n):
    if n<2:
        return False
    for x in range(2,int(math.sqrt(n)+1)):
        if(n%x)==0:
            return False
    return True
def Generate(a,b):
    for a in range(b+1):
        if CheckPrimes(a)==True:
            Primes.append(a)
    for x in Primes:
        print(x)

import psutil
import time

def monitor(k):
    cpu_percentages = []
    mem_percentages = []
    end_time = time.time() + k*60

    while time.time() < end_time:
        cpu_percentages.append(psutil.cpu_percent(1))
        mem_percentages.append(psutil.virtual_memory().percent)

    return cpu_percentages,mem_percentages
    

def main():
    print (CheckPrimes(int(input("Enter a number to check: "))))
    print(Generate(int(input("Enter First Number: ")),int(input("Enter Second Number: "))))
    cpu_usages, mem_usages = monitor(1)
    print(f"CPU Usages: {cpu_usages}")
    print(f"Memory Usages: {mem_usages}")
if __name__=="__main__" :
    main()
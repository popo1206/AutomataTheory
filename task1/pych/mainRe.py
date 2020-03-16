import generator
import time
import regular

if __name__ == '__main__':
    print("Choose your fighter:\n"
          "1.From File\n"
          "2.From Console\n")
    n=int(input())
    rr = regular.RegularExp()
    if (n==1):
        print("Input number of strings:")
        k=int(input())
        f=open('task1.txt','w')
        gen=generator.Generator(k,f)
        gen.generator_all()
        f.close()
        n1 = time.perf_counter()
        rr.checkStringFile()
        n2 = time.perf_counter()
        print('time:',n2-n1)
    if (n==2):
        n1 = time.perf_counter()
        while True:
            print("Input string:(for exit enter exit)")
            string=input()
            if string!='exit':
                rr.checkStringConcole(string)
            else:
                break
    rr.saveDict()
import smcFile
import generator
import time
if __name__ == '__main__':
    obj=smcFile.AppClass()
    print('Choose:\n'
          '1.File reading\n'
          '2.Concole reading\n')
    k=int(input())
    if k==1:
        n1=time.perf_counter()
        f=open('task1.txt','w')
        res = open('resSMC.txt', 'w')
        st = open('statictic.txt', 'w')
        gen=generator.Generator(1000,f)
        gen.generator_all()
        f.close()
        f=open('task1.txt','r')
        obj.ReadFile(f,res,st)
        n2=time.perf_counter()
        print("time:", n2-n1)
    if k==2:
        n1=time.perf_counter()
        f = open('resSMC_1.txt','w')
        while True:
            print('Enter the string (exit if you wanna stop)')
            str1 = input()
            if str1 != 'exit':
                t = obj.CheckString(str1)
                if t:
                    f.write(str1)
            else:
                f.close()
                break
        n2=time.perf_counter()
        print("time:", n2 - n1)


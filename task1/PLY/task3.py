import parcerClass
import generator
import time
if __name__ == '__main__':
    parser=parcerClass.Parser()
    print('Choose:\n'
          '1.File reading\n'
          '2.Concole reading\n')
    k=int(input())
    if k==1:
        f=open('task1.txt','w')
        res = open('ResParser.txt', 'w')
        st = open('statictic.txt', 'w')
        gen=generator.Generator(10000,f)
        gen.generator_all()
        f.close()
        f=open('task1.txt','r')
        n1 = time.perf_counter()
        for s in f:
            parser.check_string(s)
            if parser._flag==True:
                res.write(s)
        n2 = time.perf_counter()
        for i in parser._a:
            st.write(i+' = '+str(parser._a[i])+'\n')

        print("time:", n2-n1)
    if k==2:

        while True:
            print('Enter the string (exit if you wanna stop)')
            str1 = input()
            if str1 != 'exit':
                str1+='\n'
                t=parser.check_string(str1)
                if parser._flag:
                   print('ok')
                else:
                    print('Error string')
            else:
                break
        print(parser._a)


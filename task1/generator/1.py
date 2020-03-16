import random
import string
from random import choice

class Generator:
    def __init__(self, n=1000000,f=open('task1.txt' , 'w'),k=100):
        self._n = n
        self._f = f
        self._addressee=[]
        self._addresseeNum=k

    def __del__(self):
        self._f.close()

    def get_mailto(self):
        return 'mailto:'

    def generator_adressee(self):
        for k in range(self._addresseeNum):
           self._addressee.append(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1,20))))

    def generator_email(self):
        right_str = choice(self._addressee)+'@'+''.join(choice(string.ascii_letters+string.digits) for _ in range(random.randint(1,20)))+'.'+''.join(choice(string.ascii_letters)for _ in range(random.randint(1, 5)))
        return right_str

    def generator_right_str(self):

        s = self.get_mailto()+self.generator_email()
        s1=', '.join(self.generator_email() for _ in range(random.randint(0,5)))+'\n'
        if s1:
            return s+', '+s1
        return s+'\n'

    def spoil_str_1(self,str ):
        ll= str.split(':')
        return ll[0]+'\n'

    def spoil_str_2(self, str):
        ll = str.split('@')
        pp=ll[len(ll)-1].split('.')
        return ll[0]+'@.'+pp[len(pp)-1]

    def spoil_str_3(self,str):
        str.split('\n')
        return (str[0]+'jjfjfjfjfjjffjkfkf'+'\n')

    def spoil_str_4(self,str):
        ll=str.split('.')
        return ll[0]+'.dfhskjfhksjhfdkjshdfkjshdkfjsdfhksdjhfskhdskj'+ll[len(ll)-1]

    def spoil_str_5(self,str):
        ll=str.split('.')
        return ll[len(ll)-1]

    def spoil_str_6(self, str):
        ll = str.split(':')
        return ll[len(ll)-1]

    def generator_all(self):
        self.generator_adressee()
        ll=[self.spoil_str_1,
       self.spoil_str_2,
       self.spoil_str_3,
         self.spoil_str_4,
        self.spoil_str_5,
        self.spoil_str_6]


        for _ in range(self._n):
            n = random.randint(0, 5)
            self._f.write(choice((self.generator_right_str(), ll[n](self.generator_right_str()))))



if __name__ == '__main__':
    f=open('task1.txt','w')
    gen = Generator(1000,f,100)
    gen.generator_all()




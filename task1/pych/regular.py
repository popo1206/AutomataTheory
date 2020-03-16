import re



class RegularExp:
    def __init__(self,f=open('task1.txt','r')):
        self._f=f
        self._res=open('ResFile.txt','w')
        self._stat=open('Statistic.txt','w')
        self._regex=r'mailto:(?P<name_user>[a-zA-Z0-9]{1,20})@[a-zA-Z0-9]{1,20}\.[a-zA-Z]{1,5}(\, [a-zA-Z0-9]{1,20}@[a-zA-Z0-9]{1,20}\.[a-zA-Z]{1,5})*\n';
        self._dict={}
        self._helpreg=r'@[a-zA-Z0-9]{1,20}\.[a-zA-Z]{1,5}\, '

    def __del__(self):
        self._f.close()
        self._res.close()
        self._stat.close()



    def checkStringFile(self):
        for i in self._f:
            match=re.fullmatch(self._regex,i)
            if match is not None:
                mass = re.split(self._helpreg, i.rstrip())
                mass.remove(mass[0])
                if len(mass)>0:
                    hh=mass[len(mass)-1].split('@')
                    mass[len(mass)-1]=hh[0]
                self._res.write(i)
                if self._dict.get(match.group('name_user')) is None:
                    self._dict[match.group('name_user')]=1
                for k in mass:
                    if self._dict.get(k) is None:
                        self._dict[k] = 1
                    else:
                        self._dict[k]+=1

    def checkStringConcole(self,i):
        i=i+'\n'
        match = re.fullmatch(self._regex, i)
        if match is not None:
            mass = re.split(self._helpreg, i.rstrip())
            mass.remove(mass[0])
            if len(mass) > 0:
                hh = mass[len(mass) - 1].split('@')
                mass[len(mass) - 1] = hh[0]
            self._res.write(i)
            if self._dict.get(match.group('name_user')) is None:
                self._dict[match.group('name_user')] = 1
            for k in mass:
                if self._dict.get(k) is None:
                    self._dict[k] = 1
                else:
                    self._dict[k] += 1
    def saveDict(self):
        for i in self._dict:
            self._stat.write(i + '=' + str(self._dict[i]) + '\n')














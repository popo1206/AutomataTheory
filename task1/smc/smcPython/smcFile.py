import smcFile_sm

class AppClass:
    def __init__(self):
        self._fsm = smcFile_sm.AppClass_sm(self)
        self._fsm.enterStartState()
        self._is_acceptable = False
        self._length = 0
        self._flag=True
        self._name=''
        self._dict={}
        self._name_mass=[]
        self._strName=''
        self._c=''

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def isLess6(self):
        return self._length <= 6
    def isLess5(self):
        return self._length <= 5

    def isLess20(self):
        return self._length < 20



    def CheckString(self, string):
        self._fsm.Start()
        string = string.lower()
        self._flag=True
        for c in string:
            self._c=c
            if c.isalpha():
                self._fsm.Letter()
                if self._flag:
                    self._name+=c
            elif c.isdigit():
                self._fsm.Digit()
            elif c == ' ':
                self._fsm.SpaceSym()
            elif c == '@':
                self._fsm.AtSignSym()
            elif c == ':':
                self._fsm.ColonSym()
            elif c == '.':
                self._fsm.PointSym()
            elif c==',':
                self._fsm.CommaSym()
            elif c == '\n':
                self._fsm.EOS()
                break
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        return self._is_acceptable

    def LengthInc(self):
        self._length += 1

    def LengthZero(self):
        self._length = 0


    def isMailto(self):
        t = (self._name == "mailto")
        self._name = ''
        self._flag=False
        return t

    def ClearSMC(self):
        self.LengthZero()
        self._name=''
        self._is_acceptable = True

    def LengthNoZero(self):
        return self._length > 0

    def AddName(self):
        self._name_mass.append(self._strName)
        self._strName=''


    def PutInDec(self):
        for i in self._name_mass:

            if self._dict.get(i) is None:
                self._dict[i]=1
            else :
                self._dict[i]+=1
    def makeName(self):
        self._strName+=self._c



    def ClearMass(self):
           self._name_mass[:]=[]

    def ReadFile(self,f,res,st):

        for line in f.readlines():
            match = self.CheckString(line)
            if match:
                res.write(line)
        for i in self._dict:
            st.write(i + '=' + str(self._dict[i]) + '\n')
        res.close()
        f.close()
        st.close()



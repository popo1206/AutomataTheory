# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : smcFile.sm

import statemap


class AppClassState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def AtSignSym(self, fsm):
        self.Default(fsm)

    def ColonSym(self, fsm):
        self.Default(fsm)

    def CommaSym(self, fsm):
        self.Default(fsm)

    def Digit(self, fsm):
        self.Default(fsm)

    def EOS(self, fsm):
        self.Default(fsm)

    def Letter(self, fsm):
        self.Default(fsm)

    def PointSym(self, fsm):
        self.Default(fsm)

    def SpaceSym(self, fsm):
        self.Default(fsm)

    def Start(self, fsm):
        self.Default(fsm)

    def Unknown(self, fsm):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException(msg)

class MainMap_Default(AppClassState):

    def Start(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.ClearSMC()
        finally:
            fsm.setState(MainMap.Start)
            fsm.getState().Entry(fsm)


    def Unknown(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def Letter(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def Digit(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def SpaceSym(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def CommaSym(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def ColonSym(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def AtSignSym(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


    def PointSym(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(MainMap.Error)
            fsm.getState().Entry(fsm)


class MainMap_Start(MainMap_Default):

    def ColonSym(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.isMailto() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.LengthZero()
            finally:
                fsm.setState(MainMap.Colon)
                fsm.getState().Entry(fsm)
        else:
            MainMap_Default.ColonSym(self, fsm)
        
    def Letter(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.isLess6() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Unacceptable()
            finally:
                fsm.setState(MainMap.Error)
                fsm.getState().Entry(fsm)


class MainMap_Colon(MainMap_Default):

    def Digit(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.LengthInc()
            ctxt.makeName()
        finally:
            fsm.setState(MainMap.Name_User)
            fsm.getState().Entry(fsm)


    def Letter(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.LengthInc()
            ctxt.makeName()
        finally:
            fsm.setState(MainMap.Name_User)
            fsm.getState().Entry(fsm)


class MainMap_Name_User(MainMap_Default):

    def AtSignSym(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.LengthZero()
            ctxt.AddName()
        finally:
            fsm.setState(MainMap.AtSign)
            fsm.getState().Entry(fsm)


    def Digit(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.isLess20() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.LengthInc()
                ctxt.makeName()
            finally:
                fsm.setState(endState)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Unacceptable()
            finally:
                fsm.setState(MainMap.Error)
                fsm.getState().Entry(fsm)


    def Letter(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.isLess20()  :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.LengthInc()
                ctxt.makeName()
            finally:
                fsm.setState(endState)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Unacceptable()
            finally:
                fsm.setState(MainMap.Error)
                fsm.getState().Entry(fsm)


class MainMap_AtSign(MainMap_Default):

    def Digit(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.LengthInc()
        finally:
            fsm.setState(MainMap.Name_Server)
            fsm.getState().Entry(fsm)


    def Letter(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.LengthInc()
        finally:
            fsm.setState(MainMap.Name_Server)
            fsm.getState().Entry(fsm)


class MainMap_Name_Server(MainMap_Default):

    def Digit(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.isLess20() :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Unacceptable()
            finally:
                fsm.setState(MainMap.Error)
                fsm.getState().Entry(fsm)


    def Letter(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.isLess20()  :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Unacceptable()
            finally:
                fsm.setState(MainMap.Error)
                fsm.getState().Entry(fsm)


    def PointSym(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.LengthZero()
        finally:
            fsm.setState(MainMap.Point)
            fsm.getState().Entry(fsm)


class MainMap_Point(MainMap_Default):

    def Letter(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.LengthInc()
        finally:
            fsm.setState(MainMap.Name_Zone)
            fsm.getState().Entry(fsm)


class MainMap_Name_Zone(MainMap_Default):

    def CommaSym(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.LengthZero()
        finally:
            fsm.setState(MainMap.Comma)
            fsm.getState().Entry(fsm)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Acceptable()
            ctxt.LengthZero()
            ctxt.PutInDec()
            ctxt.ClearMass()
        finally:
            fsm.setState(MainMap.OK)
            fsm.getState().Entry(fsm)


    def Letter(self, fsm):
        ctxt = fsm.getOwner()
        if  ctxt.isLess5()  :
            endState = fsm.getState()
            fsm.clearState()
            try:
                ctxt.LengthInc()
            finally:
                fsm.setState(endState)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Unacceptable()
            finally:
                fsm.setState(MainMap.Error)
                fsm.getState().Entry(fsm)


class MainMap_Comma(MainMap_Default):

    def SpaceSym(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(MainMap.Space)
        fsm.getState().Entry(fsm)


class MainMap_Space(MainMap_Default):

    def Digit(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.LengthInc()
            ctxt.makeName()
        finally:
            fsm.setState(MainMap.Name_User)
            fsm.getState().Entry(fsm)


    def Letter(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.LengthInc()
            ctxt.makeName()
        finally:
            fsm.setState(MainMap.Name_User)
            fsm.getState().Entry(fsm)


class MainMap_Error(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Unacceptable()
            ctxt.ClearMass()
        finally:
            fsm.setState(endState)


class MainMap_OK(MainMap_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Acceptable()
        finally:
            fsm.setState(endState)


class MainMap(object):

    Start = MainMap_Start('MainMap.Start', 0)
    Colon = MainMap_Colon('MainMap.Colon', 1)
    Name_User = MainMap_Name_User('MainMap.Name_User', 2)
    AtSign = MainMap_AtSign('MainMap.AtSign', 3)
    Name_Server = MainMap_Name_Server('MainMap.Name_Server', 4)
    Point = MainMap_Point('MainMap.Point', 5)
    Name_Zone = MainMap_Name_Zone('MainMap.Name_Zone', 6)
    Comma = MainMap_Comma('MainMap.Comma', 7)
    Space = MainMap_Space('MainMap.Space', 8)
    Error = MainMap_Error('MainMap.Error', 9)
    OK = MainMap_OK('MainMap.OK', 10)
    Default = MainMap_Default('MainMap.Default', -1)

class AppClass_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, MainMap.Start)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None
        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:

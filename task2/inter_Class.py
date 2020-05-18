import sys
import par_Class
import copy
from par_Class import SyntaxTreeNode
import math
import random


class Var:
    def __init__(self, symtype=[] or '', value=None):
        self.type = symtype
        self.value = value

    def __repr__(self):
        return f'{self.type}, {self.value}'

    def __deepcopy__(self, memodict={}):
        return Var(self.type, self.value)

class MyInterpreter:

    # Initialize the interpreter. prog is a dictionary
    def __init__(self):
        self.parser = par_Class.Parser()
        self.prog = None
        self.symbol_table = [dict()]
        self.functions = None
        self.tree = None
        self.type=[]
        self.scope = 0
        self.flagOperation=True



    def interpreter(self,  prog=None):
        self.prog = prog
        self.tree, self.functions, _correct = self.parser.parse(self.prog)
        if _correct:
            self.interpreter_tree(self.tree)
            self.interpreter_node(self.tree)
        else:
                sys.stderr.write(f'Can\'t intemperate incorrect input file\n')

    def interpreter_tree(self, tree):
        print("Program tree:\n")
        tree.print()
        print("\n")

    def interpreter_node(self, node):
        self.type.clear()
        if node is None:
            return
        #program
        elif node.type == 'program':
            self.interpreter_node(node.children)
        #program->stategroup
        elif node.type == 'stategroup':
            for child in node.children:
                self.interpreter_node(child)

        # statement --> declaration
        elif node.type == 'declaration':
            if node.children[0].type=='type':
                self._createType(node.children[0])
            if node.children[1].type=='vars':
                children = node.children[1]
                self._declaration(children)

        #statement-->assignment
        elif node.type == 'assignment':
            self._assignment(node)
        # for array assignment
        elif node.type == 'index':
            return self._indexing(node)

        elif node.type == 'bin_op':
            exp1=node.children[0]
            if (exp1.type != 'name') and (exp1.type != 'num'):
                exp1 = self.interpreter_node(exp1)
            exp2 = node.children[1]
            if (exp2.type != 'name') and (exp2.type != 'num'):
                exp2 = self.interpreter_node(exp2)

            if node.value == '+':
                return self._plus(exp1, exp2)
            elif node.value=='-':
                return self._minus(exp1, exp2)
            elif node.value=='*':
                return self._mul(exp1,exp2)
            elif node.value=='/':
                return self._div(exp1,exp2)
            elif node.value=='%':
                return self._mod(exp1,exp2)






    #create expression of type
    def _createType(self,type : SyntaxTreeNode):
         if isinstance(type.children,SyntaxTreeNode):
            self.type.append(type.value)
            self._createType(type.children)
         elif isinstance(type.children,list):
            self.type.append(type.value)


    def _declaration(self, node: par_Class.SyntaxTreeNode):

        if node.type=='vars':
            for child in node.children:
                self._declaration(child)
        else:
            if node.type == 'assignment':
                self._create_new_var(self.type, node.children[0].value)
                if node.children[1].type=='num':
                    if self.symbol_table[self.scope][node.children[0].value].type[0]== \
                    'const value' or 'value' or 'const array of' or 'array of':
                        self.symbol_table[self.scope][node.children[0].value].value=node.children[1].value
                    else:
                        sys.stderr.write(f'Cant assign number to {self.symbol_table[self.scope][node.children[0].value].type}\n')
                elif node.children[1].type=='name':
                    if self.symbol_table[self.scope][node.children[1].value] is None:
                        sys.stderr.write(f'Error assignment: this var {node.children[1].value} doesnt exist\n')
                    elif self.symbol_table[self.scope][node.children[1].value].value is None:
                        sys.stderr.write(f'Error assignment: this var {node.children[1].value} is undefined\n')
                    elif  (self.symbol_table[self.scope][node.children[0].value].type[0]==\
                        'value' or 'const value') and (self.symbol_table[self.scope][node.children[1].value].type[0]==\
                        'value' or 'const value'):
                        self.symbol_table[self.scope][node.children[0].value].value= \
                            self.symbol_table[self.scope][node.children[1].value].value
                    elif  (self.symbol_table[self.scope][node.children[0].value].type[0]==\
                        'array of' or 'const array of') and (self.symbol_table[self.scope][node.children[1].value].type[0]==\
                        'array of' or 'const array of'):
                        self.symbol_table[self.scope][node.children[0].value].value= \
                            self.symbol_table[self.scope][node.children[1].value].value
                    elif  (self.symbol_table[self.scope][node.children[0].value].type[0]==\
                        'pointer' or 'const pointer' or 'const pointer const') and (self.symbol_table[self.scope][node.children[1].value].type[0]==\
                        'pointer' or 'const pointer' or 'const pointer const'):
                        self.symbol_table[self.scope][node.children[0].value].value= \
                            self.symbol_table[self.scope][node.children[1].value].value
                elif node.children[1].type!='num' or 'name':
                    self.symbol_table[self.scope][node.children[0].value].value=\
                    self.interpreter_node(node.children[1])



            else:
                self._create_new_var(self.type, node.value)
                #needed to check const
                 #if self.type[0]==('const value' or 'const pointer const' or 'const pointer' or 'const array of'):
                    #print('Modififcation const is needed assignment')
                #else:



    def _plus(self, exp1: SyntaxTreeNode, exp2: SyntaxTreeNode):
        type1=''
        type2=''
        val1=0
        val2=0
        if exp1.type=='name':
            if self.symbol_table[self.scope][exp1.value].value!=None:
                type1=self.symbol_table[self.scope][exp1.value].type[0]
                val1=self.symbol_table[self.scope][exp1.value].value
            else:
                sys.stderr.write(f'Illigial operation: var  {exp1.value} does not have value\n')
                self.flagOperation=False
                return Var('num',1)
        else:
            type1='num'
            val1=exp1.value
        if exp2.type=='name':
            if self.symbol_table[self.scope][exp2.value].value != None:
                type2 = self.symbol_table[self.scope][exp2.value].type[0]
                val2 = self.symbol_table[self.scope][exp2.value].value
            else:
                sys.stderr.write(f'Illigial operation: var  {exp2.value} does not have value\n')
                self.flagOperation = False
                return Var('num', 1)
        else:
            type2 = 'num'
            val2=exp2.value

        if (type1=='value' or 'const value' or 'num') and  (type2=='value' or 'const value' or 'num'):
            return Var('num',val1+val2)
        elif (type1=='pointer' and type2!='pointer') or (type1!='pointer' and type2=='pointer'):
            return Var('pointer',val1+val2)
        elif (type1=='array of' or type2=='array of'):
            sys.stderr.write(f'Cant plus with type array of\n')
            self.flagOperation = False
            return Var('num', 1)
        else:
            sys.stderr.write(f'Unknown error\n')
            self.flagOperation = False
            return Var('num', 1)

    def _minus(self, exp1: SyntaxTreeNode, exp2: SyntaxTreeNode):
        type1=''
        type2=''
        val1=0
        val2=0
        if exp1.type=='name':
            if self.symbol_table[self.scope][exp1.value].value!=None:
                type1=self.symbol_table[self.scope][exp1.value].type[0]
                val1=self.symbol_table[self.scope][exp1.value].value
            else:
                sys.stderr.write(f'Illigial operation: var  {exp1.value} does not have value\n')
                self.flagOperation = False
                return Var('num', 1)
        else:
            type1='num'
            val1=exp1.value
        if exp2.type=='name':
            if self.symbol_table[self.scope][exp2.value].value != None:
                type2 = self.symbol_table[self.scope][exp2.value].type[0]
                val2 = self.symbol_table[self.scope][exp2.value].value
            else:
                sys.stderr.write(f'Illigial operation: var  {exp2.value} does not have value\n')
                self.flagOperation = False
                return Var('num', 1)
        else:
            type2 = 'num'
            val2=exp2.value

        if (type1=='value' or 'const value' or 'num') and  (type2=='value' or 'const value' or 'num'):
            return Var('num',val1-val2)
        elif (type1=='pointer' and type2!='pointer') or (type1!='pointer' and type2=='pointer'):
            return Var('pointer',val1-val2)
        elif (type1=='array of' or type2=='array of'):
            sys.stderr.write(f'Cant minus with type array of\n')
            self.flagOperation = False
            return Var('num', 1)
        else:
            sys.stderr.write(f'Unknown error\n')
    def _mul(self, exp1: SyntaxTreeNode, exp2: SyntaxTreeNode):
        type1=''
        type2=''
        val1=0
        val2=0
        if exp1.type=='name':
            if self.symbol_table[self.scope][exp1.value].value!=None:
                type1=self.symbol_table[self.scope][exp1.value].type[0]
                val1=self.symbol_table[self.scope][exp1.value].value
            else:
                sys.stderr.write(f'Illigial operation: var  {exp1.value} does not have value\n')
                self.flagOperation = False
                return Var('num', 1)
        else:
            type1='num'
            val1=exp1.value
        if exp2.type=='name':
            if self.symbol_table[self.scope][exp2.value].value != None:
                type2 = self.symbol_table[self.scope][exp2.value].type[0]
                val2 = self.symbol_table[self.scope][exp2.value].value
            else:
                sys.stderr.write(f'Illigial operation: var  {exp2.value} does not have value\n')
                self.flagOperation = False
                return Var('num', 1)
        else:
            type2 = 'num'
            val2=exp2.value

        if (type1=='value' or 'const value' or 'num') and  (type2=='value' or 'const value' or 'num'):
            return Var('num',val1*val2)
        elif (type1=='pointer') or (type2=='pointer'):
            sys.stderr.write(f'Cant multiplication with type pointer\n')
            self.flagOperation = False
            return Var('num', 1)
        elif (type1=='array of' or type2=='array of'):
            sys.stderr.write(f'Cant multiplication with type array of\n')
            self.flagOperation = False
            return Var('num', 1)
        else:
            sys.stderr.write(f'Unknown error\n')
    def _div(self, exp1: SyntaxTreeNode, exp2: SyntaxTreeNode):
        type1=''
        type2=''
        val1=0
        val2=0
        if exp1.type=='name':
            if self.symbol_table[self.scope][exp1.value].value!=None:
                type1=self.symbol_table[self.scope][exp1.value].type[0]
                val1=self.symbol_table[self.scope][exp1.value].value
            else:
                sys.stderr.write(f'Illigial operation: var  {exp1.value} does not have value\n')
                self.flagOperation = False
                return Var('num', 1)
        else:
            type1='num'
            val1=exp1.value
        if exp2.type=='name':
            if self.symbol_table[self.scope][exp2.value].value != None:
                type2 = self.symbol_table[self.scope][exp2.value].type[0]
                val2 = self.symbol_table[self.scope][exp2.value].value
            else:
                sys.stderr.write(f'Illigial operation: var  {exp2.value} does not have value\n')
                self.flagOperation = False
                return Var('num', 1)
        else:
            type2 = 'num'
            val2=exp2.value

        if val2 == 0:
            sys.stderr.write(f'Zero divison\n')
            self.flagOperation = False
            return Var('num', 1)
        else:
            if (type1=='value' or 'const value' or 'num') and  (type2=='value' or 'const value' or 'num'):
                    return Var('num',int(val1/val2))
            elif (type1=='pointer') or (type2=='pointer'):
                sys.stderr.write(f'Cant multiply with type pointer\n')
                self.flagOperation = False
                return Var('num', 1)
            elif (type1=='array of' or type2=='array of'):
                sys.stderr.write(f'Cant minus with type array of\n')
                self.flagOperation = False
                return Var('num', 1)
            else:
                sys.stderr.write(f'Unknown error\n')
                self.flagOperation = False
                return Var('num', 1)
    def _mod(self, exp1: SyntaxTreeNode, exp2: SyntaxTreeNode):
        type1=''
        type2=''
        val1=0
        val2=0
        if exp1.type=='name':
            if self.symbol_table[self.scope][exp1.value].value!=None:
                type1=self.symbol_table[self.scope][exp1.value].type[0]
                val1=self.symbol_table[self.scope][exp1.value].value
            else:
                sys.stderr.write(f'Illigial operation: var  {exp1.value} does not have value\n')
                self.flagOperation = False
                return Var('num', 1)
        else:
            type1='num'
            val1=exp1.value
        if exp2.type=='name':
            if self.symbol_table[self.scope][exp2.value].value != None:
                type2 = self.symbol_table[self.scope][exp2.value].type[0]
                val2 = self.symbol_table[self.scope][exp2.value].value
            else:
                sys.stderr.write(f'Illigial operation: var  {exp2.value} does not have value\n')
                self.flagOperation = False
                return Var('num', 1)
        else:
            type2 = 'num'
            val2=exp2.value

        if val2 == 0:
            sys.stderr.write(f'Zero divison\n')
            self.flagOperation = False
            return Var('num', 1)
        else:
            if (type1=='value' or 'const value' or 'num') and  (type2=='value' or 'const value' or 'num'):
                    return Var('num',val1 % val2)
            elif (type1=='pointer') or (type2=='pointer'):
                sys.stderr.write(f'Cant multiply with type pointer\n')
                self.flagOperation = False
                return Var('num', 1)
            elif (type1=='array of' or type2=='array of'):
                sys.stderr.write(f'Cant minus with type array of\n')
                self.flagOperation = False
                return Var('num', 1)
            else:
                sys.stderr.write(f'Unknown error\n')
                self.flagOperation = False
                return Var('num', 1)





    def _assignment(self, node: SyntaxTreeNode):
        variable = node.children[0]
        expression = node.children[1]
        tab= self.symbol_table[self.scope][variable.value]
        if variable.value not in self.symbol_table[self.scope].keys():
            sys.stderr.write(f'Undeclared symbol\n')
        elif tab.type[0]=='const value' or tab.type[0]=='const array of' or tab.type[0]=='const pointer' \
            or tab.type[0]=='const pointer const':
                   sys.stderr.write(f'Const var {tab.type[0]}')
        else:
            if expression.type=='name':
               if  expression.value not in self.symbol_table[self.scope].keys():
                  sys.stderr.write(f'Undeclared symbol\n')
               else:
                     if (tab.type[0]=='value' and (self.symbol_table[self.scope][expression.value].type[0]=='const value' or 'value'))\
                            or (tab.type[0]=='pointer' and (self.symbol_table[self.scope][expression.value].type[0]=='const pointer' or 'pointer' or 'const pointer const')):
                        tab.value=self.symbol_table[self.scope][expression.value].value
            elif expression.type=='num':
                if (tab.type[0]=='value' or 'array of'):
                    tab.value = expression.value
                else:
                    sys.stderr.write(f'Error assignment num to {tab.type[0]}l\n')
            elif expression.type!='num' or 'name':
                val=self.interpreter_node(expression).value
                if self.flagOperation==True:
                    tab.value=val





    def _create_new_var(self, _type: [], name: str):
        print(name)
        type=copy.copy(_type)
        self.symbol_table[self.scope][name] = Var(type, None)

    def print_symbol(self):
        print(self.symbol_table)






txt=' value a=25;\n const value b=5;\n b=10+7*a;\n '
interpr=MyInterpreter()
interpr.interpreter(prog=txt)
interpr.print_symbol()







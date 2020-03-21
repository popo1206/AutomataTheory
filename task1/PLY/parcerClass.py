from lexerClass import Lexer
import ply.yacc as yacc
import sys

class Parser():
    tokens = Lexer.tokens

    def __init__(self):
        self._lexer = Lexer()
        self._parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self._a=dict()
        self._flag=False
        self._fRes=open('ResParser.txt','w')

    def check_string(self, s):
            self._flag = False
            res = self._parser.parse(s)
            return res


    def p_addr(self, p):
        """addr : MAILTO NAME SERVER ZONE NL
                | MAILTO NAME SERVER ZONE mm2 NL"""
        if len(p)==6:
            p[0]=p[1]+p[2]+p[3]+p[4]+p[5]
            self._flag=True
        elif len(p)==7:
            p[0] = p[1] + p[2] + p[3] + p[4] + p[5]+p[6]
            self._flag=True
        if self._a.get(p[2]) is None:
            self._a[p[2]] = 1
        else:
            self._a[p[2]] += 1

    def p_mm1(self,p):
        """mm1 : COMMA NAME SERVER ZONE """
        p[0]= p[1]+p[2]+p[3]+p[4]
        if self._a.get(p[2]) is None:
            self._a[p[2]] = 1
        else:
            self._a[p[2]] += 1

    def p_mm2_first(self,p):
        """mm2 : mm2 mm1 """
        p[0]=p[1]+p[2]

    def p_mm2_third(self,p):
        'mm2 : '
        p[0]=''

    def p_mm2_second(self, p):
        'mm2 : mm1'
        p[0]=p[1]

    def p_addr_zero_err_type(self, p):
        """addr : err_list NL"""
        p[0]=p[1]+p[2]



    def p_addr_third_err_type(self, p):
        """addr : MAILTO err_list NL"""
        p[0] = p[1] + p[2]+p[3]

    def p_addr_first_err_type(self, p):
        """addr : MAILTO NAME err_list NL"""
        p[0] = p[1] + p[2]+p[3]+p[4]

    def p_addr_second_err_type(self,p):
        """addr : MAILTO NAME SERVER err_list NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]+p[5]

    def p_addr_forth_err_type(self, p):
        """addr : MAILTO NAME SERVER ZONE err_list NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]+p[5]+p[6]

    def p_addr_fivth_err_type(self, p):
        '''addr : MAILTO NAME SERVER ZONE COMMA err_list NL'''
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]+p[7]

    def p_err_list_type3(self, p):
        """err_list : err_list err """
        p[0] = p[1]
        p[0] += p[2]

    def p_err_list_type2(self, p):
        """err_list : """
        p[0]=''


    def p_err_list_type1(self, p):
        """err_list : err"""
        p[0] = p[1]

    def p_err_1(self, p):
        """err : UNKNOWN """
        p[0] = p[1]

    def p_error(self, p):
        print('Unexpected token', p)

if __name__ == '__main__':
    parser = Parser()
    f = open('task1.txt', 'r')
    for line in f:
        parser.check_string(line)

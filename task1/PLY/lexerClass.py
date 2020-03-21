import ply.lex as lex
import re

class Lexer():
    states=(
        ('name','exclusive'),
        ('server','exclusive'),
        ('zone','exclusive')
    )
    tokens=(
        'MAILTO','NAME','SERVER','ZONE','NL','UNKNOWN','COMMA'
    )

    def __init__(self):
        self.lexer=lex.lex(module=self)

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def t_MAILTO(self, t):
        r'^(?mi)mailto:'
        if t.lexer.current_state() == 'INITIAL':
            t.lexer.begin('name')
        else:
            t.lexer.begin('INITIAL')
        return t

    def t_NL(self, t):
        r'(\n)'
        t.lexer.lineno+=len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_UNKNOWN(self, t):
        r'.+'
        return t

    def t_COMMA(self,t):
        r'\s '
        return t


    def t_name_NAME(self,t):
        r'([a-zA-Z0-9]{1,20})'
        t.lexer.begin('server')
        return t

    def t_name_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_name_UNKNOWN(self, t):
        r'.+'
        t.lexer.begin('INITIAL')
        return t


    def t_server_SERVER(self,t):
        r'@[a-zA-Z0-9]{1,20}'
        t.lexer.begin('zone')
        return t

    def t_server_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t
    def t_server_UNKNOWN(self, t):
        r'.+'
        t.lexer.begin('INITIAL')
        return t

    def t_zone_ZONE(self,t):
        r'\.[a-zA-Z]{1,5}'
        t.lexer.begin('zone')
        return t

    def t_zone_COMMA(self,t):
        r',\s'
        t.lexer.begin('name')
        return t

    def t_zone_NL(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_zone_UNKNOWN(self, t):
        r'.+'
        t.lexer.begin('INITIAL')
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_name_error(self, t):
        print("Illegal character in NAME '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_server_error(self, t):
        print("Illegal character in SERVER'%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_zone_error(self, t):
        print("Illegal character in ZONE'%s'" % t.value[0])
        t.lexer.begin('INITIAL')



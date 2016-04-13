# encoding: utf-8

import psycopg2

conn = psycopg2.connect(database='pyDoctor', user='mavignau', password='root')


class ParamAbm(object):
    '''list, add, modify and delete some tables using a CLI.
    Limited to use with text o char fields and single integer key'''

    def __init__(self, table, fields):
        self.table = table
        self.cols = fields.split(',')
        self.key = self.cols[0]
        val = ','.join(['%s'] * (len(self.cols) - 1))
        l_fields = ','.join(['"%s"' % f for f in self.cols[1:]])
        self.sql_sel = 'select "%s",%s from public."%s" order by "%s"' %\
            (self.key, l_fields, self.table, self.key)
        self.sql_add = 'insert into public."%s" (%s) values (%s)' %\
            (self.table, l_fields, val)
        self.sql_one = 'select %s from public."%s" where "%s"=%%s' %\
            (l_fields, self.table, self.key)
        self.sql_del = 'delete from public."%s" where "%s"=%%s' %\
            (self.table, self.key)
        pairs = ['"%s"=%%s' % f for f in self.cols[1:]]
        self.sql_mod = 'update public."%s" set %s where "%s"=%%s' %\
            (self.table, ','.join(pairs), self.key)
        self.options = {'a': self.add_reg,
                        'b': self.del_reg,
                        'm': self.mod_reg,
                        'l': self.listme}

    def __str__(self):
        'Listado de la tabla'
        cur = conn.cursor()
        cur.execute(self.sql_sel)
        sal = ['-' * 10 + '  Tabla %s  ' % self.table + '-' * 10]
        for idx, reg in enumerate(cur.fetchall()):
            if len(sal) == 1:
                sal.append('\t'.join(self.cols))
            sal.append('\t'.join([str(f) for f in reg]))
        return '\n'.join(sal)

    def listme(self):
        print self

    def get_reg(self):
        'Ingreso de los campos descriptivos'
        values = []
        for f in self.cols[1:]:
            data = raw_input('Ingrese valor para %s: ' % f)
            values.append(data.strip())
        return values

    def add_reg(self):
        'Agregado de un registro'
        cur = conn.cursor()
        cur.execute(self.sql_add, self.get_reg())
        conn.commit()

    def sel_reg(self):
        'Selección de una clave de registro'
        key = None
        while key is None:
            key = raw_input('Ingrese id del registro: ')
            if key and key.isdigit():
                key = int(key)
                cur = conn.cursor()
                cur.execute(self.sql_one, [key, ])
                if cur.fetchone():
                    return key
            print 'Debe ingresar un id válido'

    def del_reg(self):
        'Borrado del registro'
        key = self.sel_reg()
        if key:
            cur = conn.cursor()
            cur.execute(self.sql_del, [key, ])
            conn.commit()

    def mod_reg(self):
        'Modificación del registro'
        key = self.sel_reg()
        if key:
            cur = conn.cursor()
            cur.execute(self.sql_mod, self.get_reg() + [key, ])
            conn.commit()

    def get_opt(self):
        'Devuelve una opción de edición'
        opt = raw_input('Ingrese (L)istar, (A)gregar, ' +
                        '(B)orrar,(M)odificar o (F)inalizar: ')
        opt = opt.strip().lower()[0]
        return opt

    def run(self):
        'Pregunta para continuar con la edición'
        opt = ''
        while opt != 'f':
            opt = self.get_opt()
            if opt in self.options.keys():
                self.options[opt]()
            else:
                if opt != 'f':
                    print 'Error al elegir opcion'
        print 'Terminada la edicion de %s' % self.table


def main():
    'Permite elegir entre las posibles tablas para editar'
    options = [('Fuero', 'idFuero,Descripcion'),
               ('GrupoOperador', 'idGrupo,Descripcion'),
               ('TipoProceso', 'idTipoProceso,Descripcion'),
               ('TipoArchivo', 'idTipoArchivo,Descripcion')]
    opt = 100
    while opt:
        for idx, op in enumerate(options):
            print '%d)\t%s' % (idx + 1, op[0])
        opt = raw_input('Ingrese una tabla para editar (0 para salir):')
        if not opt or not opt.isdigit():
            print 'Opcion no valida'
            opt = 100
        else:
            opt = int(opt)
            if opt > len(options):
                print 'Opcion no valida'

            elif opt > 0:
                par = options[opt - 1]
                obj_Table = ParamAbm(par[0], par[1])
                print obj_Table
                obj_Table.run()


if __name__ == '__main__':
    main()

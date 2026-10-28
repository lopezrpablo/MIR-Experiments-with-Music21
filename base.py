# MIR-Experiments-with-Music21
# Copyright (C) 2026 Pablo López-Rocamora
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from collections import Counter, OrderedDict
from IPython.display import display, HTML

def print_newlines(df):
    return display( HTML( df.to_html().replace("\\n","<br>") ) )

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
    

def flat_values(dc):
    new_vals= list()
    new_dc = dict()
    vals = list(dc.values())
    keys = list(dc.keys())
    for i in vals:
        lista = list()
        for z in i:
            string = "\n".join(z)
            lista.append(string)

        new_vals.append(lista)
                    
    for i, z in zip(keys, new_vals):
        new_dc.update({i: z})
    
    return new_dc


def dic2txt(x, y, z):
    with open(x, 'w') as f:
        for n, i in enumerate(z):
            f.write(i + '\n')
            for key, value in y[n].items(): 
                f.write('%s:%s\n' % (key, value))
    f.close()
    return f

        
    

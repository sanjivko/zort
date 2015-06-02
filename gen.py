#!/usr/bin/python
class column:
    _name = "";
    _type = "";
    _is_primary = False
    def __init__(self, n, t):
        _name = n;
        _type = t;


		
class table:
    _columns = [];
    def addCols(self, n, t):
        c = column(n, t);
        _columns.append(c);



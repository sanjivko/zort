#!/usr/bin/python
import re;

class column:
    _name = "";
    _type = "";
    _is_primary = False
    def __init__(self, n, t):
        _name = n;
        _type = t;


		
class table:
	_columns = [];
	
	#addcols(name, type)
	def addCols(self, n, t):
		c = column(n, t);
		_columns.append(c);


class database:
	_tables = [];


def process_table_line(line):
	try:
		res = (re.match('CREATE TABLE ([a-zA-Z]+) *', line)).group(1);
		print "Got Table ",res
		return True;
	except:
		return False;


def process_col_line(line):
	tokens = re.split('\s+', line);
	#print tokens;
	print "-------------------------------------";
	print "got column", tokens[1]
	print "got type", tokens[2]


f = open('dbFile.sql', "r");

is_table_found = False;
for line in f:
	print line;
	if (process_table_line(line)):
		if (is_table_found):
			print "Error in parsing";
			sys.exit();
		is_table_found = True;
	elif (is_table_found):
		if (re.match("\);", line)):
			is_table_found = False;
		else:
			process_col_line(line);






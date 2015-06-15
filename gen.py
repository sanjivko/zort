#!/usr/bin/python
import re;
import sys;

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

#####Global structure 
#####that stores the tables
#####and columns as dictionary
all_tables = {};

if (len(sys.argv) != 2):
	print "File name not provided";
	sys.exit();
try:
	f = open(sys.argv[1], "r");
except Exception as e:
	print("Error:", str(e));
	sys.exit(1);

is_table_found = False;
for line in f:
	#print line;
	if (re.match("\);", line)):
		#End of table;
		is_table_found = False;
		continue;

	try:
		res = (re.match('CREATE TABLE ([a-zA-Z_]+) *', line)).group(1);
		print "Got Table ",res;
		if (is_table_found):
			print "Error in parsing";
			sys.exit(1);
		is_table_found = True;
		current_table = res;

		#Insert into the all tables var
		if res not in all_tables:
			all_tables[res] = {};
		else:
			print ("Error table:", res," Duplicate, ABORTING !!");
			sys.exit(1);
		continue;
	except:
		pass;

	if (is_table_found):
		tokens = re.split('\s+', line);
		#print tokens;
		print "-------------------------------------";
		print "got column", tokens[1]
		print "got type", tokens[2]






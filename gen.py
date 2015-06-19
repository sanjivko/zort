#!/usr/bin/python
import re
import sys
import pprint
import os
import shutil

###########################################
#   Global structure
#   that stores the tables
#   and columns as dictionary
###########################################
all_tables = {}
all_classes = {}


class column:
    _name = ""
    _type = ""
    _is_primary = False

    def __init__(self, n, t):
        _name = n
        _type = t


class table:
    _columns = []

# addcols(name, type)
def addCols(self, n, t):
    c = column(n, t)
    self._columns.append(c)

def write_classes_to_files():
    dir_name = "classes"
    if os.path.exists(dir_name):
        # dir_name = raw_input('classes dir already exists, enter another name:')
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)

    for k in all_classes.keys():
        print "Creating Class:" + k
        f = open(dir_name + "/" + k + ".hpp", "w")
        f.write('#ifndef __' + k + '_HPP__')
        f.write("\n")
        f.write('#define __' + k + '_HPP__')
        f.write("\n")

        f.write("class " + k + " {")
        f.write("\n")

        f.write("\tpublic:")
        f.write("\n")
        for l in all_classes[k]["public"].keys():
            f.write("\t\t" + l + all_classes[k]["public"][l])
            f.write("\n")

        f.write("\tprivate:")
        f.write("\n")
        for l in all_classes[k]["private"].keys():
            f.write("\t\t" + all_classes[k]["private"][l] + "  " + l+";")
            f.write("\n")
        f.write("}")
        f.write("\n")
        f.write("#endif")
        f.write("\n")


    #################################################
    # "class name": {
    #                 public: {
    #                            #functions#,
    #                            #fucntions#,
    #                            .
    #                            .
    #                         }
    #                 private: {
    #                            var1,
    #                            var2,
    #                            .
    #                            .
    #						   }
    #               }
def generate_classes():

    for k, v in all_tables.items():
        tab_name = k
        print tab_name
        class_key = 'AW_Table_' + tab_name
        if class_key not in all_classes:
            all_classes[class_key] = {"public": {}, "private": {}}
            for l, m in v.items():
                # Add private variable
                var_name = "m_col_" + l
                var_type = "string"
                if (m == "character"):
                    var_type = "string"
                if (m == "integer"):
                    var_type = "int"
                if (m == "date"):
                    var_type = "CDate"
                if (m == "timestamp"):
                    var_type = "string"
                if (m == "double"):
                    var_type = "int"

                all_classes[class_key]["private"][var_name] = var_type

                # Add get/set methods
                get_fn_name = var_type + " get_col_" + l + "()"
                set_fn_name = "void set_col_" + l + "(" + var_type + " val)"

                all_classes[class_key]["public"][get_fn_name] = "{return " + var_name + ";}"
                all_classes[class_key]["public"][set_fn_name] = "{" + var_name + " = val;}"
    # pprint.pprint(all_classes)
    write_classes_to_files()


if len(sys.argv) != 2:
    print "File name not provided"
    sys.exit()
try:
    f = open(sys.argv[1], "r")
except Exception as e:
    print("Error:", str(e))
    sys.exit(1)

is_table_found = False

current_table = ""

for line in f:
    # print line
    if re.match("\)", line):
        # End of table
        is_table_found = False
        continue

    try:
        res = (re.match('CREATE TABLE ([a-zA-Z_]+) *', line)).group(1)
        print "Got Table ", res
        if is_table_found:
            print "Error in parsing"
            sys.exit(1)
        is_table_found = True
        current_table = res

        # Insert into the all tables var
        if current_table not in all_tables:
            all_tables[current_table] = {}
        else:
            print ("Error table:(", res, ") Duplicate, ABORTING !!")
            sys.exit(1)
        continue
    except:
        pass

    if is_table_found:
        tokens = re.split('\s+', line)
        # print tokens
        print "-------------------------------------"
        print "got column", tokens[1]
        print "got type", tokens[2]
        col = tokens[1]
        dtype = tokens[2]

        if current_table in all_tables:
            if col in all_tables[current_table]:
                print "Error duplicate column name(", col, ") in table (", current_table, ")"
            else:
                all_tables[current_table][col] = dtype
        else:
            print "Table name (", current_table, ") not found"


    # pprint.pprint(all_tables)
    generate_classes()

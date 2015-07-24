def mem_asciiz(arg1):
	for i in arg1:
		memlist.append(format(ord(i), 'x'))

def mem_word(arg1):
	line = format(arg1,'0>4x');
	word_list = [line[i:i+2] for i in range(0, len(line), 2)]
	memlist.extend(word_list)

# import opcode dictionary
import csv
oplist_filename = 'opcodelist.csv'
reglist_filename = 'registerlist.csv'

with open(oplist_filename, 'rU') as f:
	reader = csv.reader(f)
	b6_opdict = {rows[0]:rows[1] for rows in reader}

with open(reglist_filename, 'rU') as f:
	reader = csv.reader(f)
	reg_namedict = {rows[0]:rows[1] for rows in reader}

# initialize all the registers
reg_list = 32*[0]

# import file from user
file = open('filename.txt','r')
flines = file.readlines()
arg = list()
op = list()
instructionlist = list()

# memlist is the memory stored in consecutive bytes
memlist = list()

for i,elem in enumerate(flines):
	cur_op = elem.split()[0]
	op.append(cur_op)
	arg.append(elem.split()[1].split(','))
num_lines = i + 1

# import all related functions
from funcmodule import *
dict_func = {'add': func_add , 'addi': func_addi, 'sub': func_sub}

for line in range(0,num_lines-1):
	instructionlist.append(b6_opdict[op[line].lower()])

il = instructionlist



for line in range(0, num_lines-1):
	cur_opcode = op[line].lower()
	print cur_opcode
	print arg
	dict_func[cur_opcode](arg[line], il)

	
# cur_op = 'ADD'
# cur_arg1 = '$0'
# cur_arg2 = '$1'
# cur_arg3 = '$2'
# cur_arg = [cur_arg1, cur_arg2, cur_arg3]
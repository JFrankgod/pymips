#!/usr/bin/python
# Filename: funcmodule.py

dict_reg = {'$0':100, '$1': 200, '$2': 300, '$3':400, '$4':500, '$5':600}

def func_add(cur_arg, instructionlist):
	print cur_arg
	print instructionlist
	dict_reg[cur_arg[0]] = dict_reg[cur_arg[1]] + dict_reg[cur_arg[2]]
	print dict_reg[cur_arg[0]]

def func_addu():
	print 'This is func_addu'

def func_sub(cur_arg, instructionlist):
	pass

def func_subu():
	pass

def func_addi():
	print 'This is func_addi'

def func_addiu():
	pass

def func_mult():
	pass

def func_multu():
	pass

def func_div():
	pass

def func_divu():
	pass

def func_lw():
	pass

def func_lh():
	pass


version = '0.1'

# End of funcmodule.py

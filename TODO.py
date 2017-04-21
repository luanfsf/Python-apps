#!/usr/bin/env python3
# encoding: utf-8

def main():
	'''
	Pseudocodigo

	iniciar e ler a lista principal
	exibir status 0 a 100
	exibir a lista principal
	exibir menu de acoes
		newtask
		editTask
		removeTask


	'''

def readDB():
	''' Ler o arquivo e para cada linha, ler tarefa e prioridade
	'''

todolist = []

with open('todos.db') as db:
	for line in db:
	   todolist.append(line.strip().split(';'))

	'''
	# Para ver itens por linha
	for i in range(len(display_list)):
		for j in range(len(display_list[i])):
			print(display_list[i][j] , end=",") # [i][j]
		print("")

	#print(len(display_list[0])) # Para ver numero de linhas (i)
	#print(len(display_list[0])) # Para ver numero de itens em cada linha (j)


	'''

def saveDB():

def formatTasks():
	'''
	UNIX
	┘ ┐ ┌ └ ┼ ─ ├ ┤ ┴ ┬ │

	DOS
	│	┤					    ╣║╗╝	┐
	└	┴	┬	├	─	┼		╚╔╩╦╠═╬
	┘	┌	┐
	'''

def endPrompt(): # end of line menu

def header():

def sortpriority():

def addTask():

class task ():
	# MAXIMUM TASKS 999
	# PRIORITY (RED,GREEN, YELLOW)
	# NUM-PRIORITY-111111111111111111111111111111111111111111111111111111111111
	# max 70 characteres

	def editTask():

	def removeTask():


if __name__ == '__main__':
	main()

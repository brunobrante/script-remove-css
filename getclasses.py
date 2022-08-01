import os
import re 

def getClassesInHTML(pathHTML):
	openFileHTML = open(os.path.expanduser(pathHTML), "r")
	fileHTML = openFileHTML.read()
	openFileHTML.close()

	regexJS = 'className={(.+?)}'
	allClassesHTML = re.findall(regexJS, fileHTML)

	# Limpando as classes
	listClasses = []
	for i in allClassesHTML:
		# Retirando o espaço do final da palavra e quebro a classe 
		splitList = i.rstrip(" ").split(" ")
		listClasses += splitList

	# Remover classes duplicadas
	listClasses = list(dict.fromkeys(listClasses))

	# Remover row, scroll, scroll_green, others
	# Apagando as classes que nao sao bem vindas com os prefixos ou inteiras
	classesRemove = []
	for removeItem in classesRemove: 
		for classItem in listClasses:
			if removeItem in classItem:
				listClasses.remove(removeItem)
	
	return listClasses


def getClassesInCSS(pathCSS): 
	openFileCSS = open(os.path.expanduser(pathCSS), "r")
	fileCSS = openFileCSS.read()
	openFileCSS.close()

	#regexCSS = '\.(.+) \{'
	regexCSS =  "(.+?)\{"
	allClassesCSS = re.findall(regexCSS, fileCSS)

	# Limpando as classes CSS
	listCSS = []
	for i in allClassesCSS:
		# Retirando o espaço do final da palavra e quebro a classe 
		splitList = i.lstrip("\t").rstrip(" ")
		if splitList.startswith("."): 
			listCSS.append(splitList)

	# Remover css duplicadas
	listCSS = list(dict.fromkeys(listCSS))
	return listCSS
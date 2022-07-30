import os
import re 
# "~/Desktop/Projects/partners-dashboard/src"
# "/components/Checkbox/index.js"
# "/components/Checkbox/Checkbox.module.css"
path = "~/Desktop/Projects/partners-dashboard/src"
# path = input("Qual é o path ? ")
pathFileJS = "/components/TableProducts/index.js"
#pathFileJS = input("Qual é o path do HTML ? ")
pathFileCSS = "/components/TableProducts/TableProducts.module.css"
#pathFileCSS = input("Qual é o path do CSS ? ")


openFileJS = open(os.path.expanduser(f"{path}{pathFileJS}"), "r")
fileJS = openFileJS.read()
openFileJS.close()

openFileCSS = open(os.path.expanduser(f"{path}{pathFileCSS}"), "r")
fileCSS = openFileCSS.read()
openFileCSS.close()

regexJS = 'class="(.+?)"'
allClassesJS = re.findall(regexJS, fileJS)

#regexCSS = '\.(.+) \{'
regexCSS =  "(.+?)\{"
allClassesCSS = re.findall(regexCSS, fileCSS)

# ----------------------------------------------------------
# Limpando as Classes
# ----------------------------------------------------------
listClasses = []
for i in allClassesJS:
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

# ----------------------------------------------------------
#          Limpando os CSS 
# ----------------------------------------------------------
listCSS = []
for i in allClassesCSS:
	# Retirando o espaço do final da palavra e quebro a classe 
	splitList = i.lstrip("\t").rstrip(" ")
	if splitList.startswith("."): 
		listCSS.append(splitList)

# Remover css duplicadas
listCSS = list(dict.fromkeys(listCSS))

# ----------------------------------------------------------
#          Comparando os arquivos
# ----------------------------------------------------------
print(listClasses)
print(listCSS)

# Verifico dentro as classes se bate com o css
# O CSS que nao bater com nenhuma classe eu descarto
# Eu crio uma result com as classes que não estao sendo usadas dentro do html

print("-------------------")
# Verifico os css que sao validos no HTML

listCSSRemove = []
for css in listCSS:
	# Dou um split nos css que tem mais de uma classe e retiro as tags html
	# e so deixo as classes
	cssSplit = [x for x in css.replace(":", " ").split(" ") if x.startswith(".")]
	for split in cssSplit:
		if split.lstrip(".") not in listClasses:
			listCSSRemove.append(css)

# Limpo items duplicados
listCSSRemove = list(dict.fromkeys(listCSSRemove))

# Retiro os CSS invalidos dentro da lista de css
listCSSKepp = [x for x in listCSS if x not in listCSSRemove]

# Verifico os css validos dentro do arquivo
newCSS = ""
for itemCSSKepp in listCSSKepp: 
	regex = itemCSSKepp + " \{(.|\n)*?\}"
	getCSS = re.search(regex, fileCSS).group(0)
	newCSS += getCSS + "\n\n"

if newCSS: 
	# Abro o arquivo CSS novamente e salvo
	f = open(os.path.expanduser(f"{path}{pathFileCSS}"), "w")
	f.write(newCSS)
	f.close()
	print("Removido as classes não utilizadas")
else:
	print("Todas as classes estão sendo usadas")	


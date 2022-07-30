import os
import re 

def removeUnsedCSS(listCSS,listHTML): 
	# Pego a lista de todos os arquivos
	listCSSRemove = []
	for css in listCSS:
		# Dou um split nos css que tem mais de uma classe e retiro as tags html
		# e so deixo as classes
		cssSplit = [x for x in css.replace(":", " ").split(" ") if x.startswith(".")]
		for split in cssSplit:
			if split.lstrip(".") not in listHTML:
				listCSSRemove.append(css)

	# Limpo items duplicados
	listCSSRemove = list(dict.fromkeys(listCSSRemove))

	# Retiro os CSS invalidos dentro da lista de css
	listCSSKeep = [x for x in listCSS if x not in listCSSRemove]
	return listCSSKeep

def rewriteFile(listCSSKeep, pathCSS): 
	# Verifico os CSS validos dentro do arquivo
	if(listCSSKeep): 
		f = open(os.path.expanduser(pathCSS), "r+")
		fileCSS = f.read()
		# Pego todos o css inteiro e salvo dentro do arquivo
		newCSS = ""
		for itemCSSKeep in listCSSKeep: 
			regex = itemCSSKeep + " \{(.|\n)*?\}"
			getCSS = re.search(regex, fileCSS).group(0)
			newCSS += getCSS + "\n\n"
		f.write(newCSS)
		f.close()
		print("Removido as classes não utilizadas")
	else:
		print("Todas as classes estão sendo usadas")	
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
	#listCSSKeep = [x for x in listCSS if x not in listCSSRemove]
	return listCSSRemove

def rewriteFile(listCSSRemove, pathCSS): 
	# Verifico os CSS validos dentro do arquivo
	print(listCSSRemove)
	if(listCSSRemove): 
		f = open(os.path.expanduser(pathCSS),'r+')
		fileCSS = f.read()
		#print(fileCSS)
		# Pego todos o css inteiro e salvo dentro do arquivo
		for itemCSSRemove in listCSSRemove: 
			regex = "^" + itemCSSRemove + " \{(.|\n)*?\}"
			fileCSS = re.sub(regex, "", fileCSS)
			
		print(fileCSS)
		f.seek(0)
		f.write(fileCSS)
		f.close()
		print("Removido as classes não utilizadas")
	else:
		print("Todas as classes estão sendo usadas")	
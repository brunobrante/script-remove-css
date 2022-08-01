from getclasses import getClassesInHTML, getClassesInCSS
from remove import removeUnsedCSS, rewriteFile

pathHTML = "~/Desktop/Projects/partners-dashboard/src/components/TableProducts/index.js"
#pathFileHTML = input("Qual é o path do HTML ? ")
pathCSS = "~/Desktop/Projects/partners-dashboard/src/components/TableProducts/TableProducts.module.css"
#pathFileCSS = input("Qual é o path do CSS ? ")

# Pego todos as classes dentro do HTML
listHTML = getClassesInHTML(pathHTML)
# Pego todas as classes dentro do CSS
listCSS = getClassesInCSS(pathCSS)

# Comparo os dois e retorno somente as classes do HTML que estão sendo utilizada
listCSSKeep = removeUnsedCSS(listCSS, listHTML)
# Reescrevo o arquivo novamente
# rewriteFile(listCSSKeep, pathCSS)


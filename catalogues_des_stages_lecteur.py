# -*- coding: utf-8 -*-

from classe_mobilite.classe_mobilite import *
import codecs

def lecture_stage(lu, titre, lire):
    lu.write('\\subsection{'+ titre +'}\n\n')
    lire = codecs.open(lire,'r',encoding='utf-8')
    lineIndex = 0
    element = []

    for line in lire:
        if lineIndex % 7 == 0: # gère le nom, prénom, institut
            lineIndex += 1
            if element:
                element = []
                lineIndex = 0
                lu.write('\\bigbreak')

        elif lineIndex - 1 % 7 == 0:
            element = ['\\textbf{', line[:-1],'}']
            lineIndex += 1

        elif lineIndex - 2 % 7 == 0: # gère la durée
            element = ['\\textit{Durée : }', line[:-1]]
            lineIndex += 1

        elif lineIndex - 3 % 7 == 0: # gère le tuteur
            element = ['\\textit{Tuteur : }\n', line[:-1]]
            lineIndex += 1

        elif lineIndex - 4 % 7 == 0: # gère les missions
            try:
                missions = line.split(';')
            except:
                missions = []
            if len(missions) > 1:
                element = ['\\textit{Mission(s) :}\n\n\\begin{itemize}\n\\item ', missions[0]]
                i = 1
                while i < len(missions):
                    element.append('\n\\item ')
                    element.append(missions[i][1:])
                    i += 1 
                element.append('\\end{itemize}')
            else:
                element = ['\\textit{Mission(s) : }', line[:-1]]
            lineIndex += 1

        elif lineIndex - 5 % 7 == 0: # gère l'adresse
            adresse = line.split(',')
            element = ['\\textit{Adresse : }\n\n', '\\begin{center}\n', adresse[0], '\n\n', adresse[1][1:], '\n\n', adresse[2][1:],'\\end{center}']
            lineIndex += 1
        elif lineIndex - 6 % 7 == 0: # gère le contact personnel
            element = ['\\textit{Contact personnel : }', line[:-1]]
            lineIndex += 1

        lu.write(''.join(element))
        lu.write('\n\n')

    lire.close()
    lu.write('\\newpage\n\n')

def lecture_mobilite(lu, mobilite):
    lu.write('\\textbf{'+mobilite.identite[:-1]+', en '+mobilite.annee[:-1]+' ('
             +mobilite.semestre[:-1]+') à '+mobilite.ville+'}\n\n')

    lu.write('Cours suivis :\n\n')
    cours_suivis = mobilite.cours[:-1].split(';')
    lu.write('\\begin{itemize}\n')
    for cours in cours_suivis:
        lu.write('\\item '+cours+'\n')
    lu.write('\\end{itemize}\n\n')

    lu.write('\\textit{Contact personnel :} '+mobilite.mail+'\n')


def Set_catalogue():
    lu = codecs.open('./catalogue_stage_latex.txt','w',encoding='utf-8')

# INTRODUCTION

    lu.write('\\documentclass{article}\n')
    lu.write('\\usepackage[utf8]{inputenc}\n')
    lu.write('\\usepackage[francais]{babel}\n')
    lu.write('\\usepackage[T1]{fontenc}')
    lu.write('\\setlength{\\parindent}{0pt}\n')
    lu.write('\\usepackage[top=2cm, bottom=2cm, left=2cm, right=2cm]{geometry}\n\n')

    lu.write('\\title{Catalogue des stages et mobilités effectués par les étudiants au CMI BSE de Nancy}\n')
    lu.write('\\author{AECMI Nancy}\n')
    lu.write('\\date{Juillet 2020}\n\n')

    lu.write('\\begin{document}\n\n')

    lu.write('\\maketitle\n\n')
    lu.write('Les stages et mobilités présentés dans ce catalogue sont classés dans chaque catégorie des plus récents aux plus anciens.\n\n')

    lu.write('\\renewcommand{\\contentsname}{Sommaire}\n\\tableofcontents\n\n')

    lu.write('\\newpage\n\n')
    lu.write('\\section{Catalogue des Stages}')

# STAGES DE L1
    lecture_stage(lu, 'Stages de première année - L1', './catalogues/catalogue_stage_l1.txt')

# STAGES DE L3
    lecture_stage(lu, 'Stages de troisième année - L3', './catalogues/catalogue_stage_l3.txt')

# STAGES DE M1
    lecture_stage(lu, 'Stages de quatrième année - M1', './catalogues/catalogue_stage_m1.txt')

# STAGES DE M2
    lecture_stage(lu, 'Stages de cinquième année - M2', './catalogues/catalogue_stage_m2.txt')

# MOBILITES INTERNATIONNALES

    lu.write('\\section{Catalogue des Mobilités}\n\n')
    lire = codecs.open('./catalogues/catalogue_mobilite.txt','r',encoding='utf-8')
    lineIndex = 0
    element = []
    mobilites = []

    for line in lire:
        #print('line:['+line+']')        
        if lineIndex % 7 == 0:
            if element:
                print(element)
                mobilites.append(Mobilite(element[0],element[1],element[2],
                    element[3],element[4],element[5],element[6]))
                element = []
            #print(line[:-1])
            element.append(line[:-1])
        elif (lineIndex - 3) % 7 == 0:
            split = line.split(',')
            #print('element 1 : '+ split[0])
            #print('element 2 : '+ split[1][1:-1])           
            element.append(split[0])
            element.append(split[1][1:-1])
        elif (lineIndex - 6) % 7 != 0:
            #print('element 3 : '+ line[:-1])
            element.append(line[:-1])
        print(lineIndex)
        lineIndex += 1
    mobilites.append(Mobilite(element[0],element[1],element[2],element[3],
        element[4],element[5],element[6]))

    existe = False
    pays = []
    for _ in mobilites:
        if pays:
            for x in pays:
                if _.pays[:-1] == x:
                    existe = True
                else:
                    existe = False
        if existe == False:
            pays.append(_.pays[:-1])
            print(pays)
    pays = sorted(pays)
    for x in pays:
        lu.write('\\subsection{Partir au '+x+'}\n\n')
        for _ in mobilites:
            print(_.pays)
            if _.pays[:-1] == x:
                lecture_mobilite(lu, _) #je ne comprends pas pourquoi ça m'écrit le truc 4 fois
    
            
    lire.close()
    lu.close()



Set_catalogue()

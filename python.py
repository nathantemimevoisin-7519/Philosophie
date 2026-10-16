import sqlite3

connexion = sqlite3.connect('philo.db')
curseur = connexion.cursor()
curseur.execute('SELECT citation, explication, auteur, date FROM citations')# WHERE chapitre="1"')
tab = []
for row in curseur:
    tab.append(row)
curseur.close()

curseur = connexion.cursor()
curseur.execute('SELECT * FROM philosophes')
tabP = []
for row in curseur:
    tabP.append(row)
curseur.close()

curseur = connexion.cursor()
curseur.execute('SELECT DISTINCT mot FROM définitions')
noms =[]
for row in curseur:
    noms.append(row)
curseur.close()
tabD = []
for mot in noms:
    curseur = connexion.cursor()
    curseur.execute(f"SELECT def FROM définitions WHERE mot = '{mot[0]}'")
    tabz = []
    for row in curseur:
        tabz.append(row)
    curseur.close()
    tabD.append([mot,tabz])

curseur = connexion.cursor()
curseur.execute('SELECT * FROM repères')
tabR = []
for row in curseur:
    tabR.append(row)
curseur.close()

connexion.close()

fichier = open("citations.css","w",encoding="utf-8")
fichier.write("body {  background-color: lavender;  display: grid;  grid-column-gap: 10px} \n .citation{  font-weight : bold;  grid-column: 1} \n .explication{grid-column: 2} \n.auteur{grid-column: 3}\n.date{grid-column: 4}")
fichier.close()
fichier = open("citations.html","w", encoding="utf-8")
fichier.write("<html>\n<head>\n<title>Citations Philo</title>\n<meta charset='utf-8'>\n<link rel='stylesheet' href='citations.css'/> \n</head>\n<body>\n")
for ligne in tab :
    fichier.write(f"<p class ='citation'> <> {ligne[0]} </p> \n")
    fichier.write(f"<p class ='explication'> => {ligne[1]} </p> \n")
    fichier.write(f"<p class ='auteur'> de {ligne[2]} </p> \n")
    fichier.write(f"<p class ='date'>  au {ligne[3]}ème siècle </p> \n")
fichier.write("<body>\n</html>")
fichier.close()

fichier = open("philosophes.css","w",encoding="utf-8")
fichier.write("body {  background-color: lavender;  display: flex;  grid-column-gap: 10px;  grid-row-gap: 10px;  flex-wrap: wrap;justify-content: center;}\n.philosophe{  display: grid;  grid-gap: 10px;  grid-template-rows: 100px 50px 20px 20px;  border: 2px dashed black;  padding: 5px;  border-radius: 10px;}\n.nom{  font-weight : bold;  grid-column: 1;  grid-row: 2;  align-self: anchor-center;}\n.siecle{  grid-column: 2;  grid-row: 2;  align-self: anchor-center;}\n.continent{  grid-column: 1;  grid-row: 3;  align-self: anchor-center;}\n.pays{  grid-column: 2;  grid-row: 3;  align-self: anchor-center;}.ville{  grid-column: 3;  grid-row: 3;  align-self: anchor-center;}\n.oeuvre{  grid-column: 3;  font-style : italic;  grid-row: 2;  overflow: auto;align-self: anchor-center;}\n.des{  grid-column: span 3;  grid-row: 4;  overflow: auto;  align-self: anchor-center;}\n.image{  grid-column: span 3;  height: 100px;  grid-row: 1;  justify-self: anchor-center;  align-self: anchor-center;}")
fichier.close()
fichier = open("philosophes.html","w", encoding="utf-8")
fichier.write("<html>\n<head>\n<title>Philosophes</title>\n<meta charset='utf-8'>\n<link rel='stylesheet' href='philosophes.css'/> \n</head>\n<body>\n <h1> Philosophes </h1>")
for philo in tabP :    
    nom, siecle, continent, pays, ville, oeuvre, des , lienImg = philo
  
    fichier.write(f"<div class = 'philosophe'>")
    fichier.write(f"<p class ='nom'>  {nom} </p> \n")
    fichier.write(f"<p class ='siecle'>  {siecle}ème siècle </p> \n")
    fichier.write(f"<p class ='continent'>  {continent} </p> \n")
    fichier.write(f"<p class ='pays'>   {pays} </p> \n")
    fichier.write(f"<p class ='ville'>  {ville} </p> \n")
    fichier.write(f"<p class ='oeuvre'>  {oeuvre} </p> \n")
    #fichier.write(f"<p class ='des'>   {des} </p> \n")
    fichier.write(f"<img src = '{lienImg}' alt='Photo' title = 'Photo d'époque 100% vraie' class = 'image'> ")
    fichier.write("</div>\n")
    
fichier.write("<body>\n</html>")
fichier.close()

fichier = open("reperes.css","w",encoding="utf-8")
fichier.write("body {background-color: lightgreen;  display: grid;  grid-column-gap: 10px} \n .mot{grid-column: 1;}\n .explication {grid-column: 2;}\n .motlie {grid-column:3;}")
fichier.close()
fichier = open("reperes.html","w",encoding="utf-8")
fichier.write("<html>\n<head>\n<title>Repères</title>\n<meta charset='utf-8'>\n<link rel='stylesheet' href='reperes.css'/> \n</head>\n<body>\n")
for ligne in tabR :
    fichier.write(f"<p class ='mot'> <> {ligne[0]} </p> \n")
    fichier.write(f"<p class ='explication'> => {ligne[1]} </p> \n")
    fichier.write(f"<p class ='motlie'> // {ligne[2]} </p> \n")
fichier.write("<body>\n</html>")
fichier.close()

fichier = open("definitions.css","w",encoding="utf-8")
fichier.write("body {background-color: lightcyan;display : grid; grid-row-gap: 10px; } \n .groupe{display: grid;  grid-column-gap: 10px;   grid-template-columns: 100px auto;grid-auto-rows : 50px; } \n.mot{grid-column: 1;}\n .def {grid-column: 2;}")
fichier.close()
fichier = open("definitions.html","w",encoding="utf-8")
fichier.write("<html>\n<head>\n<title>Définitions</title>\n<meta charset='utf-8'>\n<link rel='stylesheet' href='definitions.css'/> \n</head>\n<body>\n")
for ligne in tabD :
    fichier.write(f"<div class='groupe'>")
    fichier.write(f"<p class ='mot'> <> {ligne[0][0]} </p> \n")
    for defi in ligne[1]:
        fichier.write(f"<p class ='def'> => {defi[0]} </p> \n")
    fichier.write("</div>")
fichier.write("<body>\n</html>")
fichier.close()

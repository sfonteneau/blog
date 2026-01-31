---
title: "MAJ – Lutter contre les ransomwares"
date: "2016-03-09"
slug: "maj-lutter-contre-ransomwares"
lang: "fr"
key: "maj-lutter-contre-ransomwares"
---

![detecter-logiciel-espion](images/detecter-logiciel-espion-300x225.df85a3ac.jpg)


Il y a quelque temps j’avais fait un article « **Lutter contre les ransomwares »** :


> [Lutter contre les ransomwares](../lutter-contre-les-ransomware/index.html)
> 
> 


Aujourd’hui une petite mise a jour s’impose.


J’ai pris tous les ransomwares trouvées dans ma boite spam et j’ai commencé à les tester un par un.


**Ce qui change par rapport au dernier article, ce que je dois faire:**


– Ajout de l’extension JS a la liste des extensions non autorisées dans les GPO de restriction logiciel


– Blocage des MACRO dans Microsoft office avec les gpo (admx) fournis par Microsoft: https://www.microsoft.com/en-us/download/details.aspx?id=35554  

Basculer le **« Paramètre de notification de Macro VBA »** a **« Désactiver tout sans notification ».** Dans mon établissement, personne n’utilise les macros. Je n’ai donc pas d’utilités à les laisser activées


**Et bien sûr, maintenir son parc de logiciel à jour pour éviter qu’une faille de sécurité soit exploitée.** Exemple: (http://www.lemondeinformatique.fr/actualites/lire-adobe-corrige-24-failles-dans-flash-player-dont-celle-utilisee-par-les-ransomwares-64462.html)


### **Édit :**


Je me contente ici de décrire techniquement et froidement les méthodes.


**K3nny a retranscris plus proprement ce que j’ai écris ici :**


<http://reseaux85.fr/index.php?title=Strat%C3%A9gie_de_Restriction_Logiciel_et_Applocker>


**et ici :**


<http://reseaux85.fr/index.php?title=S%C3%A9curit%C3%A9_-_Crypto-Locker/Ransomware>

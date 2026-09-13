---
title: "Sécurités, mes préconisations …"
date: "2017-05-13"
slug: "securites-mes-preconisations"
lang: "fr"
key: "securites-mes-preconisations"
---

![Personnage tenant une pancarte « Safety First »](images/secu3.e84ba482.jpg)  

Bonjour à tous …


Petite mise à jour, et conseils de sécurité pour vos réseaux. Je suis conscient que tout n’est pas applicable.


 


**Préconisations pour les attaques frontales internet:**


- Vérifiez vos règles de parfeu sur votre fwall
- Toute application disponible sur internet doit être dans une DMZ, cela permet de limiter les dégâts si celui-ci se fait hacker. Le hacker pourra donc plus difficilement faire un rebond vers l’intérieur.
- Mise en place de fail2ban sur les services disponibles depuis l’extérieur.
- Mise en place de l’https pour éviter que les mots de passe ne transitent en clair sur les réseaux (facile avec let’s encrypt) puis forcer le passage par l’https.


 


**Préconisations pour la sécurité des postes utilisateurs:**


- Vos logiciels doivent être à jour !! –> Avec WAPT 😉
- Vos postes windows doivent également être à jour ! (au moins les correctifs de sécurité !)
- Vos serveurs linux doivent également être à jour.
- Les services (logiciels) installés sur vos serveurs doivent également être à jour.
- Vous devez mettre en place le SRP ! (stratégie de restriction logiciel)
	- Dans l’idéal un utilisateur ne doit pas pouvoir exécuter quelque chose dans un dossier où il a l’accès en écriture
- Désactiver les macros dans Microsoft Office et Libre Office ou les sécuriser.
- Désactiver l’exécution des js dans les lecteurs pdf (Adobe Reader)
- Bloquer avec le Firewall (Winfows ?) les ports de la machine laissés ouverts inutilement.


 


**Préconisations sur le téléchargement d’éléments dangereux :**


- Filtrer les pièces jointes dangereuses sur votre système d’email
- Mettre un système de proxy filtrant obligatoire.  

(impossibilité pour les utilisateurs de sortir directement sur internet)
- Dans l’idéal mettre en place un snort sur le fwall pour snifer et analyser les trams et bloquer les comportements étranges.


**Préconisations pour limiter les dégâts dans le cas où un ransomware a réussi a débuter une attaque:**


- Pour serveur de fichiers (samba), limitation des dégâts pour ransomware:
	- Mettre en place un audit de suppression des fichiers, avec samba : **vfs objects = full\_audit**
	- Mettre en place un fail2ban qui analyse les logs audit samba
	- Mettre en place un fichier detecte\_ransomware.doc sur le serveur de fichiers.
	- Dans les deux cas: si un comportement étrange est détecté (extension étrange ou suppression du fichier de détection), le fail2ban peut enclencher une action pour stopper l’attaque !
	- Ne pas donner aux utilisateurs plus d’accès que nécessaire aux différentes ressources. (Faire le tri dans les droits d’accès des utilisateurs) pour limiter les dégâts.
	- Bien évidement avoir des sauvegardes fonctionnelles !


 


**Préconisation pour les administrateurs réseaux:**


- Ne jamais utiliser un compte membre du groupe « domain admins » ! Faire un groupe uniquement administrateurs des postes.
- Vos utilisateurs ne doivent bien évidemment pas être administrateurs de leur poste ni membres du groupe domain admins…


 


**Sécurisation physique du poste de travail :**


- Dans le bios: Bloquer le démarrage sur le disque dur directement.
- Bloquer l’accès bios par un mot de passe
- Bloquer l’accès matériel (accès a la carte mère), sinon il devient facile de faire un reset mot de passe du bios…


 


**Sécuriser l’accès physique aux différents éléments actifs du réseau :**


- On parle ici de bloquer physiquement l’accès avec une porte et une clé ou autre…  🙂


 


**Sécurisation de l’accès au réseau:**


- Mise en place de 802.1X pour bloquer l’accès au réseau aux postes (pc portable) non autorisé.
- Même chose pour le wifi !


 **Communication utilisateurs  :**


- Il faut communiquer les risques aux utilisateurs !  Pour qu’ils soient méfiants !


**Veille Techno :**


- Tenez-vous au courant à travers les différents articles du net! La faille qu’utilise Wannacrypt a été rendue publique une semaine avant l’attaque de grande ampleur !
- Analyser les contenus bloqués par votre système d’email ou proxy. Mieux connaître son ennemi pour mieux se préparer aux attaques ! Votre système a bloqué une attaque, bloquera t-il les prochaines ?

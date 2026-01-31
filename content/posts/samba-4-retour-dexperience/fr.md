---
title: "Samba 4 retour d’expérience"
date: "2015-03-30"
slug: "samba-4-retour-dexperience"
lang: "fr"
key: "samba-4-retour-dexperience"
---

[![page_samba4](images/page_samba4.7eb97d89.png)](../wp-content/uploads/2015/03/page_samba4.png)


Dans mon précédent article j’ai parlé du prix exorbitant des licences Microsoft ; un simple Active Directory virtualisé coûte très cher !


Mais depuis l’arrivée de Samba 4 des alternatives fiables et offrant de nouvelles fonctionnalités existent !


Je vais vous parler de mon retour d’expérience sur Samba 4 ici :


Je l’utilise en deux serveurs virtuels :  

– Un serveur Active Directory (LDAP)  

– Un serveur de fichier


Samba 4 reprend les principaux outils d’active directory :  

GPO, ACL, DNS


Mais cumule aussi les avantages qui étaient présents sous Samba 3 :  

– pre-post exec (exécution de script avant ou après un accès au partage)  

– hide files (permet de cacher des fichiers sur un partage)  

– browseable (cacher un partage sans ajouter un $ comme sur les partages Windows)  

– Autorisation de partage par adresse IP  

– Utilisation de la variable %U pour le nom d’utilisateur et %G pour le groupe primaire, dans les noms de partage et chemin de fichier…  

– etc… etc …


Toute la partie Active Directory, DNS, GPO peut être gérée via la commande samba-tools ou mieux, par les Microsoft Management Console.


Voir fonctionnement ici :


[iframe src= »http://www.youtube.com/embed/mDWIAGCJe2E » width= »100% » height= »500″]


La partie partage à la Windows est également disponible!


Les applications que je connecte aujourd’hui à mon Samba 4 sont incapables de faire la différence entre un Active Directory et Samba 4


Mes préconisations restent de compiler son propre Samba 4, mais la société sernet à sorti son propre ISO déjà tout fait (pratique pour les novices ou pour tester sans trop se fouler)


Des sociétés comme [Tranquil IT](http://tranquil.it/ "Tranquil IT") proposent des formations et des aides à la migration.


Mon tuto ici :  

[http://wiki.lesfourmisduweb.org/index.php/Serveur\_Samba\_4](http://wiki.lesfourmisduweb.org/index.php/Serveur_Samba_4 "http://wiki.lesfourmisduweb.org/index.php/Serveur_Samba_4")

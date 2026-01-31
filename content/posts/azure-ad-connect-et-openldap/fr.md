---
title: "Azure Ad Connect et Openldap"
date: "2023-05-17"
slug: "azure-ad-connect-et-openldap"
lang: "fr"
key: "azure-ad-connect-et-openldap"
---

Read in : [![English](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAAmVBMVEViZsViZMJiYrf9gnL8eWrlYkjgYkjZYkj8/PujwPybvPz4+PetraBEgfo+fvo3efkydfkqcvj8Y2T8UlL8Q0P8MzP9k4Hz8/Lu7u4DdPj9/VrKysI9fPoDc/EAZ7z7IiLHYkjp6ekCcOTk5OIASbfY/v21takAJrT5Dg6sYkjc3Nn94t2RkYD+y8KeYkjs/v7l5fz0dF22YkjWvcOLAAAAgElEQVR4AR2KNULFQBgGZ5J13KGGKvc/Cw1uPe62eb9+Jr1EUBFHSgxxjP2Eca6AfUSfVlUfBvm1Ui1bqafctqMndNkXpb01h5TLx4b6TIXgwOCHfjv+/Pz+5vPRw7txGWT2h6yO0/GaYltIp5PT1dEpLNPL/SdWjYjAAZtvRPgHJX4Xio+DSrkAAAAASUVORK5CYII=) English](../en/azure-ad-connect-and-openldap/index.html)  

![](images/azuezopenldap.ebfbf4b9.png)


 


 


Bonjour a tous, encore un petit poste rapide,


Dans mon article précédent je vous présentai un script [azure ad connect samba4](https://github.com/sfonteneau/AzureADConnect_Samba4) écris en python et qui fonctionne sous linux pour synchroniser vos user/groupe/device vers azure ad.


Je viens également de  faire un nouveau projet presque identique au premier intitulé [AzureADConnect\_Ldap](https://github.com/sfonteneau/AzureADConnect_Ldap) qui permet de synchroniser des utilisateurs et groupes openldap (ou autre autre solution ldap similaire) vers azure ad. Pratique pour les organisations sans active directory (Microsoft ou samba4)


Attention ! Pour que la synchronisation des mot de passe fonctionne il faut que votre openldap possède le HASHNT (NTLM HASH) de l’utilisateur.  

L’attribut est souvent présent si vous avez le schema samba3 dans votre openldap et présent dans l’attribut « sambaNTPassword »


Il existe de nombreuses implémentations openldap, le script peut nécessiter quelques modifications pour répondre à vos besoins


Amusez vous bien !

---
title: "Azure Ad Connect et Openldap"
date: "2023-05-17"
slug: "azure-ad-connect-et-openldap"
lang: "fr"
key: "azure-ad-connect-et-openldap"
---

![](images/azuezopenldap.ebfbf4b9.png)

Bonjour a tous, encore un petit poste rapide,


Dans mon article précédent je vous présentai un script [azure ad connect samba4](https://github.com/sfonteneau/AzureADConnect_Samba4) écris en python et qui fonctionne sous linux pour synchroniser vos user/groupe/device vers azure ad.


Je viens également de  faire un nouveau projet presque identique au premier intitulé [AzureADConnect\_Ldap](https://github.com/sfonteneau/AzureADConnect_Ldap) qui permet de synchroniser des utilisateurs et groupes openldap (ou autre autre solution ldap similaire) vers azure ad. Pratique pour les organisations sans active directory (Microsoft ou samba4)


Attention ! Pour que la synchronisation des mot de passe fonctionne il faut que votre openldap possède le HASHNT (NTLM HASH) de l’utilisateur.  

L’attribut est souvent présent si vous avez le schema samba3 dans votre openldap et présent dans l’attribut « sambaNTPassword »


Il existe de nombreuses implémentations openldap, le script peut nécessiter quelques modifications pour répondre à vos besoins


Amusez vous bien !

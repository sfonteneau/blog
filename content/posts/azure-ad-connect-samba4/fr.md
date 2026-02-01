---
title: "Azure Ad Connect Samba4"
date: "2023-05-04"
slug: "azure-ad-connect-samba4"
lang: "fr"
key: "azure-ad-connect-samba4"
---

![](images/AAD-Logosamba.45d2448b.png)

Bonjour a tous


Cela fait bien longtemps que je n’est pas écris sur ce blog.


Récemment je suis tomber sur plusieurs article concernant le fonctionnement de la synchronisation des password active directory avec azure ad connect:

– [Microsoft how-password-hash-synchronization-works](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/connect/how-to-connect-password-hash-synchronization#how-password-hash-synchronization-works)

– [Dsinternals how-azure-active-directory-connect-syncs-passwords](https://www.dsinternals.com/en/how-azure-active-directory-connect-syncs-passwords/)


Le fonctionnement est le suivant : azure ad connect prend le hashnt encodé en utf16-le, et le rentre dans la fonction PBKDF2-HMAC-SHA256″ avec 1000 itérations un sel aléatoire


Ces même recherches m’ont amenez tomber sur le travail de Dr Nestori Syynimaa ([@DrAzureAD](https://twitter.com/DrAzureAD)):

[aadinternals long-passwords](https://aadinternals.com/post/long-passwords/)  qui permet a partir d’un simple script powershell d’envoyer un hashnt.

Je tente donc ma chance avec le powershell et je m’aperçois que cela fonctionne !

Le code de @DrAzureAD est opensource, je me dit donc… il y a sûrement possibilité de le convertir en python pour l’utiliser sous linux et donc avec samba.


Après analyse du code je comprend que microsoft communique avec en [WCF binary *xml*](https://fr.wikipedia.org/wiki/Windows_Communication_Foundation),

Bonne nouvelle [les spécification sont ouverte](https://learn.microsoft.com/en-us/openspecs/windows_protocols/mc-nbfx/94c66ea1-e79a-4364-af88-1fa7fef2cc33) et un projet python existe sur github : [python-wcfbin](https://github.com/ernw/python-wcfbin)


Je créer donc un repo git baptiser [AADInternals\_python](https://github.com/sfonteneau/AADInternals_python)  qui reprend [le code de AADInternals qui m’intéresse](https://github.com/Gerenios/AADInternals/blob/9cc2a3673248dbfaf0dccf960481e7830a395ea8/AzureADConnectAPI.ps1#L1087) pour le convertir en python. Après avoir tâtonner un peu… victoire, le code fonctionne !


Je m’aperçois ensuite que le projet AADInternals de [@DrAzureAD](https://twitter.com/DrAzureAD) reprend tout ce qui est nécessaire pour créer/supprimer des utilisateurs et des groupes a la mode azuread il me reste donc a porter le reste du code.


Mais dans mes tests, les serveur Microsoft répondent:


>  « The formatter threw an exception while trying to deserialize the message: There was an error while trying to deserialize parameter http://schemas.microsoft.com/online/aws/change/2010/01:syncRequest. The InnerException message was ‘Element ‘http://schemas.microsoft.com/2003/10/Serialization/Arrays:Value’ contains data from a type that maps to the name ‘:mustUnderstand’. The deserializer has no knowledge of any type that maps to this name. Consider using a DataContractResolver if you are using DataContractSerializer or add the type corresponding to ‘mustUnderstand’ to the list of known types – for example, by using the KnownTypeAttribute attribute or by adding it to the list of known types passed to the serializer.’. Please see InnerException for more details. »
> 
> 


Je comprend donc que c’est lib python-wcfbin qui serialize mal dans certain cas.


Je demande donc au boulot un petit coup de main a des dev plus expérimenter et notement a [AndreasLrx](https://github.com/AndreasLrx)  un stagiaire chez nous, (oui oui ils sont très bon les stagiaires chez nous !)


Et il trouve le problème, les spécifications de microsoft ne sont pas à jour ! Nous faisons même une pull request sur le projet d’origine : <https://github.com/ernw/python-wcfbin/pull/16>


J’ai maintenant tout ce qu’il faut pour construire un outils de synchronisation complet.


Je créer donc sur mon projet github un projet: [AzureADConnect\_Samba4](https://github.com/sfonteneau/AzureADConnect_Samba4)


Le projet est capable d’envoyer des groupe et utilisateurs ansi que d’envoyer des hashnt  (aadhash) a l’azure ad.


Le script conserve ensuite les dernières informations dans une base sqlite local,  il l’enverra a nouveau l’objet a azure ad uniquement si l’objet a été modifier depuis le dernier envoie.


**ATTENTION** Si vous avez déjà utiliser l’azure ad connect windows, vous devez bien identifier votre « sourceanchor » ou « immutableId » de votre configuration précédente.

Par défaut microsoft utilise l’[objectGUID](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/plan-connect-design-concepts#sourceanchorSourceAnchorAttr=objectGUID) avec [msDSConsistencyGuid](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/plan-connect-design-concepts#using-ms-ds-consistencyguid-as-sourceanchor), j’ai donc repris ce fonctionnement, cependant, en fonction des versions votre paramétrage peu être différent.

A vous donc de bien identifier votre sourceanchor pour ne pas créer de doublon et/ou mauvaise suppression.


Attention également, le script ne prend pas en charge le [password writeback](https://learn.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-sspr-writeback) !


En espérant que ce travail vous sera utile ! N’hésitez pas a me faire des retours !


Edit:


Depuis le 13/05/2023, le script gère également les Device (jonction hybrid)

---
title: "Self Service Password, google apps, office 365 et check password script"
date: "2016-07-21"
slug: "self-service-password-google-apps-office-365"
lang: "fr"
key: "self-service-password-google-apps-office-365"
---

![change-your-password-623x427](images/change-your-password-623x427.96ed022b.jpg)


Un petit article utile pour samba et Windows Active Directory


Dans mon établissement nous avons de plus en plus de classe portable (les élèves apporte leur propre pc portable).


Les identifiants et mot de passe pour accéder au wifi, owncloud, etc sont ceux de l’AD, si l’utilisateur veut changer son mot de passe, il doit se connecter a un pc du domaine pour le changer, pas pratique.


J’ai donc mis en place « Self Service Password »:  

<http://ltb-project.org/wiki/documentation/self-service-password>


C’est une page web qui permet de changer son mot de passe :


[![ssp_change_nooptions](images/ssp_change_nooptions-150x150.363d600b.png)](../wp-content/uploads/2016/07/ssp_change_nooptions.png)


 


Mais cet interface permet donc d’aller encore plus loin et pourrait bien vous changer la vie. En cas d’oublie de mot de passe, le système peut proposer plusieurs méthode pour le réinitialiser:


 


- Reset by questions
- Reset by mail challenge (token sent by mail)
- Reset by SMS (trough external Email 2 SMS service)


Quelques fonctions supplémentaire sont notamment disponible, notamment le fait de gérer plus finement la politique de mot de passe.


Un email peut également être envoyée après un changement de mot de passe afin de détecter des comportements malveillant.


Une dernière fonctionnalités est très intéressante : le posthock


Le posthook est un script où est envoyé le nom d’utilisateur et le mot de passe après le changement de mot de passe.


Je profite donc du posthock pour envoyer le nouveau mot de passe à mon google apps et mon office 365 avec samba4.


En effet, pour samba4, avant, j’envoyai les mot de passe via ce genre de script :  

<https://github.com/baboons/samba4-gaps>


Mais ce genre de script me force à stocker les mot de passe de façon réversible dans l’AD, et je n’aime pas trop ça…


L’autre méthode que j’ai envisager pour  samba est d’utiliser le  

« check password script », mais malheureusement cela ne fonctionne plus avec samba4 : <https://lists.samba.org/archive/samba/2016-June/200293.html>


**Edit 08/11/2016 :**  

**Le « check password script » semble être pris en charge dans la version 4.5 de samba. Malheureusement je n’ai pas trouvée de solution pour récupérer le nom d’utilisateur :-/**


Ce genre de système est quand même utile avec un active directory, en effet le système de synchronisation  des mot de passe office 365 synchronise les mot de passe toute les 15 minute il me semble. Avec les script office 365 que j’utilise, le changement est instantanée.


Voici donc mon script posthock pour google Apps et office 365:  

<https://github.com/sfonteneau/script_modify_password_googleapps_and_office365/>


Attention ! Pour que le script fonctionne, la politique de complexités de mot de passe doit être sur 8 caractère minimum et 16 maximum !


J’espère un jour que le « check password script » re-fonctionne a nouveau


 


**Edit 2019 :**


Voir : **[https://blog.lesfourmisduweb.org/samba4-password-synchro/](../samba4-password-synchro/index.html)**

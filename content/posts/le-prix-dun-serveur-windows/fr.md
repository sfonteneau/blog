---
title: "Le prix d’un serveur Windows"
date: "2015-03-28"
slug: "le-prix-dun-serveur-windows"
lang: "fr"
key: "le-prix-dun-serveur-windows"
---

![02748596-photo-verrou-drm](images/02748596-photo-verrou-drm1-300x225.e6f09edf.jpg)


Bonjour à tous !


J’ai (enfin) décidé de faire un article sur Samba 4, qui va venir bientôt.


Mais avant je sors un article « Le prix d’un serveur Windows » pour comprendre les économies potentielles !


Imaginons, je veux me faire un Windows Server avec Active Directory ; que dois-je payer ?


Une licence Windows Server :  

J’ai trouvé la licence 2012 R2 Standard à 668€ HT


Mais avoir une licence Windows Server ne suffit pas pour avoir l’autorisation de connecter des clients dessus (quelle ironie), il faut maintenant acheter des CALs.


Mais c’est quoi une CAL ? :


La CAL (Client Access Licenses) Windows Server est obligatoire, dès qu’il y a « authentification » d’un poste (device) ou d’un utilisateur (user) pour accéder aux services de base de Windows Server (Active Directory, partage de fichiers et/ou d’imprimantes, etc…).


La CAL par « user » est liée à un individu qui peut l’utiliser pour se connecter sur différents postes de travail.


La CAL par « device » est liée à un matériel et tous les utilisateurs de ce matériel peuvent l’utiliser.


Les versions des CAL utilisées doivent obligatoirement correspondre aux versions de Windows Server. (une CAL 2003 n’est pas valable pour Server 2008, **$$$** mais une CAL 2008 peut être downgradée pour un Server 2003)


En gros une licence Windows Server sans CAL ne sert à rien !


Plus d’infos ici : <http://hebergement.u-psud.fr/distribution/acheter-a-la-di/microsoft/21-cal-client-acces-licence-microsoft.html>


Certaines versions de Windows Server ne nécessitent pas de CALs ou en ont d’inclues. Voir ici :  

<http://www.microsoft.com/OEM/fr/licensing/productlicensing/Pages/server-cal.aspx#fbid=pWJXAn-6Z9m>


![tumblr_n0xm24qMfD1rb2l1co1_400](images/tumblr_n0xm24qMfD1rb2l1co1_4001-300x210.745a20ae.gif)  

Si vous avez plusieurs serveurs de virtualisation, (XenServer, Proxmox, VMware vSphere Hypervisor ou Microsoft Hyper-V), Microsoft vous demande de payer une licence de « déplacement » (si vous migrez vos serveurs virtuels d’un serveur physique à l’autre:


Plus d’infos ici :  

<http://blogs.technet.com/b/fesnouf/archive/2013/12/26/licensing-windows-2012-standard.aspx>


Article a suivre …

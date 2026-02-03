---
title: "Déploiement de windows sur un réseau informatique"
date: "2015-07-08"
slug: "deploy-windows-fog-pilote-wapt-kms"
lang: "fr"
key: "deploy-windows-fog-pilote-wapt-kms"
---

J’ai décidé de vous faire une petite compile de tout les tuto wiki utilisé.


Tout les tuto sont dispo sur [reseaux85.fr](http://reseaux85.fr/) dont je fais également partie  

Merci a tous les contributeurs (même les stagiaire 😉  si  si)


[![deploiement](images/deploiement.86bc018c.jpg)](../wp-content/uploads/2015/07/deploiement.jpg)


Donc voici ma procédure lors d’un déploiement (lien vers les wiki) :


[– Installation d’un serveur WAPT](https://doc.wapt.fr/)  

[– Installation d’un serveur FOG](http://reseaux85.fr/index.php?title=FOG_:_Installation_du_serveur_-_Cr%C3%A9ation_master_-_Upload) et [Configuration du serveur FOG](http://reseaux85.fr/index.php?title=Configuration_FOG)[– Installation d’un serveur KMS](http://reseaux85.fr/index.php?title=Installation_d%27un_serveur_KMS_-_Activation_des_Licences)  

– Installation d’un Windows 7 Vierge (avec cle générique KMS)  

– Mise a jour windows 7 avec windows update  

– Installation du client FOG (http://ipclientfog/fog/client)  

[– Récupération des drivers et injection des drivers dans mon win 7 vierge](http://reseaux85.fr/index.php?title=FOG_:_Image_Multi-pilotes)  

[– Exécution d’un sysprep](http://reseaux85.fr/index.php?title=FOG_:_Image_Multi-pilotes#SysPrep_-_R.C3.A9initialiser_le_SID)  

[– Upload du master Windows 7 Multi-pilotes sur le serveur FOG](http://reseaux85.fr/index.php?title=FOG_:_Installation_du_serveur_-_Cr%C3%A9ation_master_-_Upload#Proc.C3.A9dure_d.27Upload_du_poste_mod.C3.A8le.2Fmaitre)  

– [Mise en place du waptdeploy](http://dev.tranquil.it/wiki/WAPT_-_Déploiement_de_WAPT_par_GPO)– Déploiement de l’image avec FOG  

– Activation de windows 7 (et office) automatique avec KMS  

– Le client FOG renomme automatiquement le pc  

– Le client FOG entre automatiquement le pc dans le domaine  

– Application des GPO automatique (avec active directory ou [samba4](https://dev.tranquil.it/wiki/Samba4))  

– Au premier démarrage dans le domaine, le waptdeploy install wapt  

[– Wapt install ensuite tout les logiciels demandés](http://wiki.lesfourmisduweb.org/index.php/Installation_et_utilisation_Serveur_et_console_WAPT#Gestion_des_Pc_et_des_paquets_dans_la_console)– Utilisation  🙂  

– Mise à jour Windows avec wsus (pour économiser la bande passante)  

– Mise en place du SRP pour éviter de pourrir la machine.


L’avantage de ce type de fonctionnement (fog et wapt) c ‘est que en cas de « plantage » d’un poste, si le wake on lan est ok sur le poste. Je n’est même pas a bouger de mon bureau…  sauf pour du hardware.


 


[![INTRO_TEND2010](images/INTRO_TEND2010-300x200.814e6d12.jpg)](../wp-content/uploads/2015/07/INTRO_TEND2010.jpg)

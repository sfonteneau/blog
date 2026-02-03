---
title: "WAPT – apt-get pour Windows"
date: "2015-01-25"
slug: "wapt-apt-get-pour-windows"
lang: "fr"
key: "wapt-apt-get-pour-windows"
---

Je viens de découvrir un nouveau logiciel de déploiement : WAPT  

WAPT est une solution qui aide au quotidien en automatisant les installations, les désinstallations et les mises à jour de l’ensemble des logiciels d’un parc informatique.


[![800px-Schema-wapt.svg](images/800px-Schema-wapt.svg_-300x111.41a808a6.png)](../wp-content/uploads/2015/01/800px-Schema-wapt.svg_.png)


Il existe la version « WAPT Starter » que j’utilise pour les particuliers ou petite entreprise, (une utilisation vraiment copier-coller de APT sur linux), on installe les logiciels souhaités avec la petite interface web, et lorsqu’une mise à jour est dispo sur le dépot WAPT <http://wapt.tranquil.it/wapt>, le logiciel va vous proposer d’installer automatiquement toutes les mises à jour disponibles.


Avec la version « WAPT Serveur », vous pouvez gérer intégralement les logiciels à partir d’une console de gestion centrale avec votre propre dépôt privé.


Principe global de WAPT Serveur :  

Une fois le client WAPT installé, vous pouvez par exemple faire un groupe de paquet logiciel « pc\_service\_commercial » et « pc\_service\_compta » puis pousser l’installation sur les postes.


Vous avez ensuite possibilité entre plusieurs types d’installation :  

– L’installation immédiate  

– Les mises à jour à l’extinction du poste  

– Laisser l’utilisateur installer les mise à jour quand il le souhaite.


Dernier bonus :  

– WAPT permet les dépôts privés multi-site et les dépôts peuvent également être disponibles depuis l’extérieur. Toujours également super pratique pour les commerciaux toujours en ballade. Les paquets sont d’ailleurs téléchargés en local sur le poste lorsque une mise à jour est disponible, l’installation peut donc être faite en étant déconnecté du réseau.  

– Les paquets sont « partageables » par fichiers ou par dépôt publique, j’ai moi même fait mon propre dépôt publique : <http://wapt.lesfourmisduweb.org/>


Doc et présentation officielle :  

Doc vidéo : <http://doc.tranquil.it/co/portail.html>


Installation :  

Mon install (Wiki) : [http://wiki.lesfourmisduweb.org/index.php/Serveur\_WAPT](http://wiki.sono-syrius.fr/index.php/Serveur_WAPT)  

Wiki officiel :  <http://dev.tranquil.it/wiki/WAPT_-_apt-get_pour_Windows>

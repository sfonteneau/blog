---
title: "Laps, pvlan, partages administratifs, parfeu, limiter les attaques latérales…"
date: "2017-07-03"
slug: "laps-pvlan-partages-administratifs-limiter-attaques-laterales"
lang: "fr"
key: "laps-pvlan-partages-administratifs-limiter-attaques-laterales"
---

![](images/vaccin_anti_HPV.b0d9a88f.jpg)


### Le bilan


Nouveau venu dans les ransomware efficace: notpeyta


Nous allons regarder comment fonctionne peyta et essayer de tirer les enseignement du type de propagation et sécuriser nos réseau en conséquence…


Article Microsoft qui détail l’attaque :


https://blogs.technet.microsoft.com/mmpc/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/


Lorsque notpeyta réussi a infecter un poste, il tente de récupérer les mot de passe de la machine pour se propager sur les autre postes avec psexec via les partages administratif ouvert sur les autres postes.


On va voir dans ce post différente solutions pour bloquer cela.


### Désactiver les partages administratifs


Une méthode pour bloquer ce type de propagation est avant toute chose de supprimer les partages administratif ouvert sur les postes.  

Un paquet de mon dépôt fait cela : <https://wapt.lesfourmisduweb.org/tous-les-packages?recherche=smp-disabling-administrative>


### Mettre en place le pvlan


Une autre méthode est de mettre en place le pvlan sur les switch votre réseau. En effet, en règle général les postes n’ont aucune raison de se voir entre eux. Plus d’information : [https://fr.wikipedia.org/wiki/VLAN\_priv%C3%A9](https://fr.wikipedia.org/wiki/VLAN_privé)


### Activer LAPS


Une  recommandation  également est d’activer laps sur votre réseau.  

En effet nous utilisons malheureusement régulièrement pour des raison de facilitée les même mot de passe administrateur locaux sur tous les postes …  Si ce mot de passe est compromis c’est toute la sécurités de réseau qui est compromise. Laps permet donc de gérer automatiquement le mot de passe du compte « Administrateur » local de toutes les machines de votre domaine. Le mot de passe est changée régulièrement et deviens unique a chaque machine. Il est ensuite stockée dans un attribut spécifique sécurisée dans l’active directory.


- [Mettre en place laps sur un active directory microsoft windows server](https://www.it-connect.fr/securite-proteger-les-comptes-administrateur-local-avec-laps/)
- [Mettre en place laps avec un samba4](https://dev.tranquil.it/wiki/SAMBA_-_Proteger_les_comptes_administrateurs_locaux_avec_LAPS)


### Règles parfeu


Globalement, sur un client windows, il n’y a aucune raison pour qu’un port soit en écoute.sur celle-ci… C’est le meilleur moyen de limiter un attaque latérale. D’ailleurs, la prochaine version de wapt va se séparer de son port d’écoute 8088 pour basculer sur du websocket !


J’ai donc fait un paquet wapt qui bloque les différents port de windows ouvert par défaut sans réelle raison pour moi …


[Paquet wapt –> smp-add-rules-block-firewall](https://wapt.lesfourmisduweb.org/tous-les-packages?recherche=add-rules-block-firewall)

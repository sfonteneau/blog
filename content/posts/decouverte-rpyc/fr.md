---
title: "Découverte Rpyc"
date: "2020-06-27"
slug: "decouverte-rpyc"
lang: "fr"
key: "decouverte-rpyc"
---

![](images/Rpyc3-logo-medium.56e72187.png)


Il y a peu de temps j’ai découvert RPYC <https://rpyc.readthedocs.io/en/latest/>


L’outil est pratique pour piloter des machines a distance a travers ssh.


Pourquoi ne pas utiliser Ansible  ?


Disons que c’est une méthode différente.  

Ansible est très pratique (je l’utilise parfois), beaucoup de module et grosse communauté mais je préférerais écrire du python pour faire des boucle, des while etc, et je dois bien dire que je ne suis pas très fan du yaml …


RPYC permet de faire discuter deux connexion python ensemble, par exemple, je suis capable de créer une liste (python) sur un serveur1, de la récupérer sur mon poste (python local) pour la renvoyer via RPYC sur une connexion python du serveur2


Je découvre donc les possibilités, voici un bout de code d’exemple :


\_\_CODEBLOCK\_0\_\_


Dans l’exemple ici on a quelque chose d’intéressant, j’utilise rpyc.classic.upload\_package, en gros les serveurs sur lequel je me connecte n’ont pas le paquet ldap3, mais il est installé sur ma machine, du coup avec rpyc je le pousse dans la connexion python instancier avec rpyc, (je le l’install pas sur le serveur !), et du coup il est utilisable. teleport lui me permet d’envoyer une fonction sur le python distant pour ensuite l’executer sur le distant. J’aime bien l’idée.


Je découvre l’outil et je vois un potentiel intéressant. **Attention je n’ai pas fais de réel test en prod ni d’utilisation intensive**, mais j’aime bien l’idée.

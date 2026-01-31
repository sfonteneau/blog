---
title: "Apache Guacamole – Alternative au VPN pour vos utilisateurs"
date: "2017-06-29"
slug: "apache-guacamole-alternative-au-vpn-pour-vos-utilisateurs"
lang: "fr"
key: "apache-guacamole-alternative-au-vpn-pour-vos-utilisateurs"
---

![](images/guac-tricolor-300x300.4bd742ff.png)


Petite présentation rapide du produit même si plusieurs blog en parlent déjà.


Guacamole permet de proposer à vos utilisateurs une interface centralisée (web) pour des connections RDP, VNC, ssh.  Dans notre cas c’est surtout le remplacement d’une connexion RDP (trop vulnérable aux attaques) qui nous intéresse. Il peut être pratique par exemple pour proposer une alternative aux connections VPN.


Le but est de fournir à l’utilisateur une connexion RDP à un serveur TSE au travers d’une interface web.  Vous n’êtes donc plus dépendants d’un OS, l’utilisateur peut être sous, Windows, Linux ou Mac (potentiellement tablette et smartphone également). La connexion RDP sera affichée à travers le navigateur web en HTML5.


Guacamole peut être couplée a un LDAP/ActiveDirectory pour l’authentification. Il est également recommandé d’activer l’authentification double facteur pour plus de sécurité (SMS par exemple). Mettre en place un fail2ban pour bannir une IP en cas de trop nombreuses tentatives de connections échouées est recommandé.


Guacamole permet également de partager un écran. Vous pouvez partager votre écran guacamole en partageant un lien, puis définir si les utilisateurs connectés via ce lien pourront contrôler la machine ou non. Cela peut être très pratique pour faire des démos de produit par exemple.


Je propose guacamole pour  une alternative au VPN mais il peut également être une excellente solution dans une école pour proposer un accès à des applications Linux sur des postes windows et inversement !


Petite vidéo:

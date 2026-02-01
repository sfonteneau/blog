---
title: "Pourquoi il ne faut pas utiliser Squid en mode transparent ?"
date: "2015-04-15"
slug: "pourquoi-il-ne-faut-pas-utiliser-squid-en-mode-transparent"
lang: "fr"
key: "pourquoi-il-ne-faut-pas-utiliser-squid-en-mode-transparent"
---

[![c81f772e265991de09ad69a5a6dfb071](images/c81f772e265991de09ad69a5a6dfb071-300x173.b97ff849.jpg)](../wp-content/uploads/2015/04/c81f772e265991de09ad69a5a6dfb071.jpg)


Il faut tout d’abord expliquer la différence entre un surf via un proxy déclaré et un surf sans Proxy.


Lors d’un surf sans Proxy, l’ordinateur contacte directement le serveur qui héberge la page web demandée. Il demande l’IP au DNS puis contacte directement le serveur web en passant par la passerelle.


Dans le cas d’un Proxy déclaré dans le navigateur, la démarche est différente. Lors d’un surf, l’ordinateur ne contacte pas directement le serveur web qui héberge la page que l’on souhaite. Voilà ce qui se passe dans ce cas : Le navigateur constate qu’un Proxy et renseigné lors de la demande de toto.fr le navigateur de l’ordinateur dit :  

– Hey serveur Proxy 172.21.254.254:3128, peut-tu surfer pour moi et me donner la page web toto.fr ?


Le serveur Proxy répond :  

– Ok, voici la page que tu m’as demandé


Il est au milieu dans le schéma :


[![280px-Proxy_concept_en.svg](images/280px-Proxy_concept_en.svg_.751e60eb.png)](../wp-content/uploads/2015/04/280px-Proxy_concept_en.svg_.png)


Squid a donc une option de proxy transparent, cette option permet de se mettre à la place de la passerelle, ainsi l’ordinateur pense qu’il discute directement avec le serveur web. Ceci fonctionne très bien avec un surf HTTP, mais ne fonctionne pas du tout avec le protocole HTTPS


Pourquoi ?


Le protocole HTTPS sécurise et chiffre la connexion sur tous les sites les plus connus, il peut également vérifier que la connexion n’a pas été usurpée par un pirate. (vérification du nom de domaine, des certificats et validation par un certificat root). Bref ce protocole a été créé dans le but de protéger une connexion.


[![header_icon](images/header_icon.6f96c434.png)](../wp-content/uploads/2015/04/header_icon.png)


Squid est capable d’intercepter du surf SSL en mode transparent mais cela nécessite l’installation préalable d’un ça-root. Cette méthode n’est pas du tout appréciée par les sites web, car elle consiste a décrypter la connexion HTTPS en cours. De plus, certains sites web n’utilisent pas le SSL mais le [SNI](http://www.rackspace.com/knowledge_center/article/serving-secure-sites-with-sni-on-apache "SNI").


Cette méthode est considérée comme une attaque man in the middle :


[![sslmim](images/sslmim-300x149.3ca8be79.png)](../wp-content/uploads/2015/04/sslmim.png)


Des solutions comme [ALCASAR](http://www.alcasar.net/fr/telechargement?func=select&id=11 "Alcasar") existent, mais je ne suis pas fan.  

Elles loguent et bloquent avec les demandes DNS (Dnsmasq) combinée avec les demandes IP avec iptables, Squid et DansGuardian pour les connexions HTTP.


Les solutions de filtrage transparent proposées par SonicWALL fonctionnent également sur ce type de fonctionnement.


La solution que j’utilise :


La solution la plus propre que j’ai trouvé pour le moment est de déclarer le Proxy. Lorsque l’utilisateur n’a pas le proxy déclaré, il est redirigé vers une page qui lui indique comment configurer son navigateur ou son téléphone pour surfer sur cette connexion.


Suite dans un prochain article… Pour présenter une solution plus fiable !

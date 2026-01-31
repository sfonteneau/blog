---
title: "Wifi – FreeRadius 802.1x – Squid/SquidGuard"
date: "2016-03-27"
slug: "wifi-freeradius-802-1x-squid-squidguard"
lang: "fr"
key: "wifi-freeradius-802-1x-squid-squidguard"
---

![SKU288251-03](images/SKU288251-03-300x300.fad7a7fa.gif)


Il y a un moment maintenant déjà, j’avais fait un article « Pourquoi il ne faut pas utiliser Squid en mode transparent ? ». J’avais là ma solution de filtrage. Mais pas  forcément la solution d’authentification.


J’avais pensée utiliser packetfence, mais c’est plus une solution de NAC. Pfsense est intéressant également, mais ne convenait pas trop à mon projet. Packetfence est d’ailleurs trop gourmand en ressource.


Je suis donc partie sur le principe me faire ma solution faite main, voici une petite vidéo de présentation de ma solution :


https://www.youtube.com/watch?v=9ItnHyWaWMo


Principe de la solution :


Une borne wifi, avec une authentification wifi « wpa2 entreprise », cette borne est connectée a un freeradius, lui-même connecté a mon active directory (authentification ntlm). Le certificat choisi est un let’s encrypt. Avoir un certificat signé par un ca root déjà installée sur l’ordinateur est utile, en effet, lors de l’utilisation d’un certificat auto signée, il faut installer le ca root correspondent sur l’ordinateur client, ce qui du coup n’est pas pratique.


Une fois connectée sur le wifi. La configuration de proxy automatique fait son boulot pour les navigateurs configurée en « détection automatique de proxy ». Si ce n’est pas le cas (sur tous les smartphones), les utilisateurs sont redirigés vers une page qui leur indique comment activer la détection automatique ou le proxy manuel.


Du côté serveur, mon squid log les adresses MAC qui surf en http et https. Le Freeradius lui log les connexions wifi avec les noms d’utilisateur et les adresses mac associées. (voir vidéo)


Cette solution est intéressante, mais ne résout pas tous les problèmes.


Lors d’un changement de mot de passe, la connexion échoue.  

Ce qui est plutôt bon signe. Ce qui est moins cool par contre, c’est qu’il faut supprimer la connexion entrer a nouveau le mot de passe. C’est bien dommage. Aussi, les vieux appareils ne fonctionnent pas avec le 802.1x Dommage


Un des avantages de cette solution (ou désavantage) tout dépend de votre point de vue, c’est qu’une ré-authentification régulière n’est pas nécessaire. Du coup pour un smartphone qui va et vient, c’est super. Mais pour un pc qui appartient à plusieurs personnes ,ce n’est pas top …


Également, cette méthode ne permet pas de faire apparaître des conditions d’utilisation comme pour un portail captif. Je considère qu’un papier doit être signé lors de la distribution de l’identifiant et du mot de passe ou alors qu’un article doit apparaître dans la charte informatique.


Pour faire claire, je n’ai pas trouvé de solution parfaite, mais celle-ci me parait un bon compromis pour mon réseau.


Et l’avantage, c’est que cela consomme très peu de mémoire. Je peux faire tourner ceci sur un raspberry ^^


Aujourd’hui, je trouve qu’il n’y a pas de solution pour les hotspot wifi. Les portails captifs habituent les utilisateurs à outrepasser les avertissements de sécurité ssl et de plus cela ne fonctionne pas avec les technologies hsts (typiquement pour google qui est très souvent la page de démarrage de nombreux navigateurs) . Le 802.1x ne permet pas de faire accepter des conditions d’utilisation ou de faire une inscription sms avec une page web par exemple… Le 802.1x ne permet pas de faire accepter des conditions d’utilisation ou de faire une inscription sms avec une page web par exemple. Dans un monde où nous trouvons de plus en plus de « free wifi », il serait temps de trouver de vraies solutions pour protéger les utilisateurs **ET** le fournisseur d’accès internet.


[![141106073506427079](images/141106073506427079-150x150.d21da2ff.jpg)](../wp-content/uploads/2016/03/141106073506427079.jpg)


 Je vais faire un petit tuto sur mon wiki lorsque j’aurai un peu de temps


Edit 10/04/2016:  

[Le documentation est ici](https://wiki.lesfourmisduweb.org/radius_wifi.html)

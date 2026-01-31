---
title: "Bloquer le réseau Tor"
date: "2015-01-29"
slug: "bloquer-le-reseau-tor"
lang: "fr"
key: "bloquer-le-reseau-tor"
---

![tor_browser_logo__no_trans_background__by_j_bob-d5gjsad](images/tor_browser_logo__no_trans_background__by_j_bob-d5gjsad-300x184.aa975f6d.png)


Je travaille dans un lycée et un collège, autant dire que je doit empêcher mes lycéens et mes collégiens de surfer sur des sites non-pédagogiques…


Depuis un certain temps maintenant est arrivé « Tor Browser »  

Principe de fonctionnement du soft :  

– Pas besoin d’être administrateur de la machine pour le lancer.  

Au démarrage Tor va vous demander si votre réseau est équipé d’un proxy. Si vous cochez non il va essayer de contacter des « IP Tor »  à travers la passerelle configurée sur votre ordinateur et va scanner tout les ports qui peuvent potentiellement sortir sur internet.


La première sécurité est donc d’empêcher les clients de sortir sur directement sur internet et de mettre en place un proxy. Les clients ne pourront donc pas sortir sur internet sans passer par lui. Seul le proxy sera autorisé à sortir sur internet. Tor va donc scanner et ne jamais trouver de « porte de sortie ».


![jns_ch12-18](images/jns_ch12-18-300x157.c92ee60a.gif)


Mais Tor (s’il est bien configuré) peut aussi passer par un proxy pour contacter directement des « IP Tor ». Son principe de fonctionnement est le suivant :  

Tor contacte une adresse IP par le proxy et ne ferme pas la connexion, il la laisse ouverte et fait transiter la navigation Tor sur ce « tunnel » ouvert.


La solution est donc de bloquer avec Squid (ou autre) les connexions vers les IP de Tor


Par chance, ce site https://www.dan.me.uk/torlist/ liste la plupart des adresses IP Tor disponibles sur le net.


J’ai publié un petit tuto sur mon [wiki ici](https://wiki.lesfourmisduweb.org/blocktor.html)

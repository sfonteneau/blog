---
title: "Mon serveur de streaming vidéo à 0,8 GHz"
date: "2026-08-27"
slug: "streaming-video-vlc-xspf-nginx"
lang: "fr"
key: "streaming-video-vlc-xspf-nginx"
---

![vlc](images/vlcnginxxspf.png)

Bonjour à tous,

J’ai un petit serveur perso qui ne paie vraiment pas de mine : **0,8 GHz de CPU et 4 Go de RAM**.

À un moment, je me suis dit que ce serait pratique de l’utiliser aussi pour regarder les vidéos stockées dessus.

Le problème, c’est qu’avec une machine comme ça, les grosses solutions avec transcodage, interface web et tout le bazar, ce n’était pas vraiment une option.

Et puis je me suis rendu compte d’un truc tout bête : le lecteur vidéo, je l’avais déjà.

**VLC.**

Il me fallait juste un moyen simple de lui donner accès à mes vidéos.

C’est là que j’ai découvert **XSPF**, un format de playlist XML que VLC sait lire.

J’ai donc écrit un petit script Python, **[generate_xspf](https://github.com/sfonteneau/generate_xspf)**, qui parcourt mes dossiers et génère automatiquement une playlist avec les URLs de mes vidéos.

En gros :

```text
Vidéos → generate_xspf → playlist XSPF → VLC
```

Et pour servir les fichiers, j’utilise simplement **nginx**.

Le plus pratique, c’est qu’il suffit ensuite de donner directement à VLC l’URL HTTP du fichier XSPF.

Dans VLC, il suffit d’aller dans **« Ouvrir un flux réseau »** et de coller une URL du genre :

```text
https://mon-serveur/vlc.xspf
```

VLC récupère la playlist et affiche directement les vidéos disponibles.

## Et en fait… ça suffit

Il n’y a aucun transcodage côté serveur.

nginx envoie directement le fichier vidéo et **VLC le télécharge au fur et à mesure de la lecture**.

Pas besoin de récupérer le film entier avant de commencer à le regarder.

Et si je saute directement au milieu du film, VLC utilise les requêtes HTTP `Range` pour demander à nginx uniquement la partie du fichier dont il a besoin.

Donc même avec un tout petit serveur, la lecture reste fluide et le CPU n’a quasiment rien à faire.

C’est ça que j’aime bien dans ce système : le serveur ne fait presque rien.

Il sert des fichiers.

Et VLC fait le reste.

## Un client disponible partout

Autre avantage : **VLC est disponible sur pratiquement toutes les plateformes**.

Je peux donc utiliser la même URL XSPF depuis mon ordinateur ou mon téléphone, regarder la vidéo directement, ou l’envoyer vers un **Chromecast** depuis le téléphone.

Évidemment, comme il n’y a aucun transcodage, le format et les codecs doivent être supportés directement par l’appareil.

## Pas sexy, mais terriblement efficace

On ne va pas se mentir : ce n’est pas Netflix.

Pas de jaquettes, pas de grosse interface, pas de recommandations, pas de transcodage à la volée.

Juste :

**nginx, une playlist XSPF et VLC.**

Et pourtant, sur mon serveur à **0,8 GHz**, ça marche très bien.

J’avais fait ce petit outil il y a déjà un moment, et je me suis récemment rendu compte qu’il intéressait encore du monde.

Quand je montre le système à des gens, la réaction est souvent la même :

**« Ah ouais… mais c’est génial en fait. »**

Et c’est justement pour ça que je trouve cette solution sympa.

Ce n’est pas sophistiqué.

C’est juste simple, léger et efficace.

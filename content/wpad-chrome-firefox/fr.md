---
title: "Wpad Chrome Firefox et isInNet(myIpAddress()"
date: "2015-11-09"
slug: "wpad-chrome-firefox"
lang: "fr"
key: "wpad-chrome-firefox"
---

Petite article car j’ai été confronté a un soucis tout bête avec le wpad Chrome, Firefox et ie.


Je souhaitais utiliser un truc du genre :


if(isInNet(myIpAddress(), « 172.29.0.0 », « 255.255.0.0 »)) { return proxy\_no; }  

return proxy\_yes;


En gros, si tu est dans le vlan 172.29.0.0 tu n’applique pas le proxy. Mais pour tout le reste oui


Cela fonctionne parfaitement avec ie et firefox mais pas avec chrome 🙁


J’ai donc contacté google pour savoir pourquoi cela ne fonctionnait pas avec eux. Il s’agit en faite d’un bug:  <https://code.google.com/p/chromium/issues/detail?id=267101>


L’issue est ouverte depuis longtemps mais n’est pas réparée.


Google m’a quand même donnée une solution, utiliser isInNetEx :


if(isInNetEx(myIpAddress(), « 172.29.0.0 », « 255.255.0.0 »)) { return proxy\_no; }  

return proxy\_yes;


Super ! Maintenant ça fonctionne ! Bon par contre plus du tout avec Firefox …


[![ob_06116c_220-f-43166878-pf3admr4fspxhl3mi4x7fu7tkjooikqx](images/ob_06116c_220-f-43166878-pf3admr4fspxhl3mi4x7fu7tkjooikqx-300x200.9d8e4e94.jpg)](../wp-content/uploads/2015/11/ob_06116c_220-f-43166878-pf3admr4fspxhl3mi4x7fu7tkjooikqx.jpg)


La seul solution que j’ai trouvé est d’empêcher que Firefox entre dans la boucle if(isInNetEx(myIpAddress() pour ne pas le faire planter et donc déclarer tous les cas possibles.


if(isInNet(myIpAddress(), « 172.28.0.0 », « 255.255.0.0 »)) { return proxy\_yes; }  

if(isInNet(myIpAddress(), « 172.29.0.0 », « 255.255.0.0 »)) { return proxy\_no; }  

if(isInNetEx(myIpAddress(), « 172.28.0.0 », « 255.255.0.0 »)) { return proxy\_yes; }  

if(isInNetEx(myIpAddress(), « 172.29.0.0 », « 255.255.0.0 »)) { return proxy\_no; }


En gros il faut absolument que if(isInNet(myIpAddress() soit déclaré pour tous vos VLAN comme ceci, firefox s’arrêtera toujours a la première correspondance.

---
title: "Preshutdowntimeout, le timeout windows"
date: "2015-10-18"
slug: "preshutdowntimeout-le-timeout-windows"
lang: "fr"
key: "preshutdowntimeout-le-timeout-windows"
---

[![time_out-bras](images/time_out-bras-300x128.6b9c3268.jpg)](../wp-content/uploads/2015/10/time_out-bras.jpg)


Bonjour


Petit article rapide dans la catégorie **wapt**.


Je viens de découvrir la cle registre « Preshutdowntimeout » dans windows.


Je vous laisse lire la partie « Maximum wait time for Group Policy scripts » ainsi que la partie « Change History ».


<https://technet.microsoft.com/en-us/library/cc757265(v=ws.10).aspx>


Par défaut, windows va killer un script si il s’exécute plus de 15 minute (lors de l’exécution des script gpo) Ce qui est gênant avec le c:\wapt\waptexit.exe (installation a l’extinction) car celui ci est lancée avec les scripts GPO. J’ai déjà rencontrée des soucis avec Microsoft Office ou solidworks. Il va donc falloir modifier le timeout par défaut.


```
Je vais donc suivre les préconisations Microsoft :
Je modifie d'abord la GPO :

La GPO ordinateur --> Paramètre Windows --> Système --> Scripts --> 
Spécifier la durée d'attente maximale pour les scripts de stratégie de 
groupe et  Ici j'indique une valeur 0. Ceci signifie un timeout infinie
```

Ensuite j’augmente la valeur de :


*HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\services\gpsvc\PreshutdownTimeout*


Pour augmenter ce timeout. La valeur de la cle registre ne peu pas être modifiée en tant qu’administrateur.


*Elle doit être modifiée en compte system. Ça tombe bien, wapt peut installe en compte system lorsque qu’on ne le lance pas en ligne de commande !* 


*J’ai donc créer un paquet pour modifier cette valeur ici:*


smp-preshutdowntimeout  

http://wapt.lesfourmisduweb.org/wapt/


Par défaut, le paquet modifie la valeur du Preshutdowntimeout de 15min à –> 3H, vous trouverez d’autre valeur, a l’intérieur du setup.py !


Et c’est tout bon! c’est modifiée, j’ai créée un paquet de sleep de 40 minutes pour tester et c’est tout bon, ça marche !


Pour voir mon cheminement sur la mailling list wapt :


<http://lists.tranquil.it/pipermail/wapt/2015-October/001343.html>


Hubert a donc annoncée que cette valeur serait gérée ensuite par wapt avec un paramètre dans le wapt-get.ini


Simon

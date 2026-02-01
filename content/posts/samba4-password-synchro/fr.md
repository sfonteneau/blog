---
title: "Samba4 Password Synchro"
date: "2018-12-09"
slug: "samba4-password-synchro"
lang: "fr"
key: "samba4-password-synchro"
---

![](images/syncpassword.8eb6c67d.png)


Bonjour a tous


Petit article pour vous annoncer que je me suis enfin re-penché sur la synchronisation des mots de passe avec samba4:


Synchro des mots de passe avec google apps : <https://github.com/sfonteneau/samba4-gaps>


C’est clairement un dérivé de la version de [baboons](https://github.com/baboons/samba4-gaps). A la différence qu’il ne nécessite plus l’activation de « store-plaintext » dans samba4.  
Il demande en revanche l’activation de CryptSHA256 in smb.conf  
  
En comparaison avec le script de baboons, le nouveau script le renvoi pas tous les mot de passe au redémarrage de gaps puisque il vérifie si la valeur de pwdlastset a changé depuis le dernier envoi. Ce script peut clairement être modifé pour d’autre application acceptant CryptSHA256 ou CryptSHA512.


Je me suis également penché sur sur l’envoie de mot de passe a des applications qui ne supporte pas le CryptSHA256 ou CryptSHA512, comme Windows Azure …


La seul solution dans ce cas est de stocké le mot de passe de l’utilisateur en clair et donc d’utiliser le mode « store-plaintext » dans active directory.  
  
J’ai donc fais un script qui permet de récupérer les mot de passe en clair des utilisateurs et de les envoyés dans un script, puis une fois traité par celui-ci, le mot de passe en clair est supprimé:<https://github.com/sfonteneau/samba4-sync-password>


Dans le cas de windows azure le script précédent peut appeler un script de changement de mot de passe dans windows azure :  <https://github.com/sfonteneau/send_password_in_azure>  
  
Une fois le mot de passe correctement envoyé à windows azure celui-ci sera supprimé de samba.


En espérant que cela peut vous être utile !

---
title: "ADCS Linux"
date: "2025-09-24"
slug: "adcs-linux"
lang: "fr"
key: "adcs-linux"
---


Bonjour à tous,


J'ai démarré un nouveau projet sur mon [GitHub](https://github.com/sfonteneau/ADCS_python) : un serveur ADCS en Python.


Ce projet part d'un constat simple : certains clients ont besoin d'un **enrôlement automatique** sur leurs machines Windows, par exemple pour gérer du 802.1x. Windows sait le faire avec un ADCS. 
 Mais lorsque le client souhaite un serveur Linux (car il utilise déjà Samba4), il n'existe finalement pas beaucoup d'autres solutions clé en main.


Ce projet émule donc un **serveur d'inscription ADCS** (et non un client). 
 Il reproduit le comportement des points de terminaison d'inscription Web Microsoft ADCS (CEP/CES) pour gérer les demandes de certificat.


- **Politique d'inscription des certificats (CEP)** : expose un point de terminaison de politique pour fournir des modèles d'inscription et des informations sur l'autorité de certification aux clients.
- **Certificate Enrollment Services (CES)** : émule le service qui accepte les CSR et renvoie les certificats signés.


L'objectif est d'émuler un serveur d'inscription Web ADCS qui :


1. Fournit la politique CEP (modèles, CA, etc.) aux clients demandeurs.
2. Reçoit et valide les CSR PKCS#10.
3. Traite les soumissions via CES et renvoie les réponses signées.


Dans ce projet, les modèles de certificats ne sont pas déclarés en configuration classique. 
 Ils sont définis via des **callbacks Python**.


Chaque modèle est représenté par un module externe (par exemple `callbacks/user_template.py`) exposant deux fonctions obligatoires :


- **define\_template(app\_conf, kerberos\_user)** 
 → Décrit dynamiquement les propriétés du modèle (OID, EKU, KeyUsage, période de validité, etc.) en fonction de l'utilisateur ou du contexte.
- **emit\_certificate(...)** 
 → Prend le CSR et les métadonnées en entrée, applique les extensions nécessaires et émet le certificat signé par l'autorité de certification.


#### Pourquoi utiliser des callbacks ?


- Offre une **flexibilité maximale** : la logique du modèle peut dépendre des attributs Active Directory, de l'appartenance à un groupe, de politiques externes (API ERP) ou de toute règle métier.
- Évite de verrouiller le serveur CA dans des modèles statiques et prédéfinis.


#### Responsabilité en matière de sécurité


Cette conception transfère la plupart des contrôles de sécurité à l'auteur du callback. En pratique :


- Les contrôles d'éligibilité (qui est autorisé à obtenir quel type de certificat) doivent être implémentés à l'intérieur du callback.
- Si le callback n'applique pas de vérifications, tout utilisateur authentifié peut obtenir n'importe quel certificat renvoyé par le module.
- Le serveur Python ADCS n'impose pas de restrictions supplémentaires : il exécute simplement le callback et signe le résultat.


En bref : la **sécurité et l’application des règles d’émission** sont entièrement de la responsabilité du code du callback.


Le projet a été en grande partie **codé avec une IA** (pratique pour convertir des RFC Microsoft peu lisibles en code fonctionnel). 
 Le projet en est encore à ses débuts, mais n'hésitez pas à me faire des retours !

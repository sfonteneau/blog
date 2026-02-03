---
title: 'LAPS, PVLAN and admin shares: limiting lateral movement'
date: '2017-07-03'
slug: laps-pvlan-partages-administratifs-limiter-attaques-laterales
lang: en
key: laps-pvlan-partages-administratifs-limiter-attaques-laterales
---

![](images/vaccin_anti_HPV.b0d9a88f.jpg)

### Summary

A new effective ransomware showed up: **NotPetya**.

Let’s look at how it spreads and what we can do to harden networks accordingly.

Microsoft article detailing the attack:
https://blogs.technet.microsoft.com/mmpc/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/

When NotPetya manages to infect a workstation, it tries to recover passwords from the machine and then propagates to other machines using **PsExec** via **administrative shares** (C$, ADMIN$, etc.) that are open on other workstations.

Below are several ways to block this.

### Disable administrative shares

A first way to limit this propagation is to remove administrative shares from workstations.

A package from my repository does that:
https://wapt.lesfourmisduweb.org/tous-les-packages?recherche=smp-disabling-administrative

### Use PVLAN

Another method is to enable **private VLAN** (PVLAN) on your switches. In general, workstations have no reason to talk to each other directly.
More info: https://fr.wikipedia.org/wiki/VLAN_privé

### Enable LAPS

Another recommendation is to deploy **LAPS**.

Unfortunately, for convenience, we often use the same local administrator password on all workstations. If that password is compromised, the whole network is compromised. LAPS automatically manages the local “Administrator” password for all domain-joined machines. The password becomes unique per machine and is regularly rotated. It is stored in a dedicated, secured AD attribute.

- LAPS on Microsoft AD: https://www.it-connect.fr/securite-proteger-les-comptes-administrateur-local-avec-laps/
- LAPS with Samba4: https://dev.tranquil.it/wiki/SAMBA_-_Proteger_les_comptes_administrateurs_locaux_avec_LAPS

### Firewall rules

On a Windows client there is usually no good reason to have services listening on random ports. Closing unnecessary ports is one of the best ways to limit lateral movement. (And by the way, a future WAPT version was planned to move away from its listening port 8088 to websockets.)

I created a WAPT package that blocks several Windows ports that are open by default without a good reason (in my opinion):
https://wapt.lesfourmisduweb.org/tous-les-packages?recherche=add-rules-block-firewall

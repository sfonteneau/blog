---
title: Deploying Windows on a network (FOG + drivers + WAPT + KMS)
date: '2015-07-08'
slug: deploy-windows-fog-pilote-wapt-kms
lang: en
key: deploy-windows-fog-pilote-wapt-kms
---

I decided to compile the wiki tutorials I use during deployments.

All tutorials are available on http://reseaux85.fr/ (I contribute there too).
Thanks to all contributors (even interns 😉).

[![deploiement](images/deploiement.86bc018c.jpg)](../wp-content/uploads/2015/07/deploiement.jpg)

Here is my deployment procedure (links to the wiki):

- [Install a WAPT server](https://doc.wapt.fr/)
- Install a FOG server:
  - http://reseaux85.fr/index.php?title=FOG_:_Installation_du_serveur_-_Cr%C3%A9ation_master_-_Upload
  - http://reseaux85.fr/index.php?title=Configuration_FOG
- [Install a KMS server](http://reseaux85.fr/index.php?title=Installation_d%27un_serveur_KMS_-_Activation_des_Licences)
- Install a clean Windows 7 (with a generic KMS key)
- Update Windows 7 using Windows Update
- Install the FOG client (http://ipclientfog/fog/client)
- [Collect drivers and inject them into my clean Windows 7 image](http://reseaux85.fr/index.php?title=FOG_:_Image_Multi-pilotes)
- [Run sysprep](http://reseaux85.fr/index.php?title=FOG_:_Image_Multi-pilotes#SysPrep_-_R.C3.A9initialiser_le_SID)
- [Upload the multi‑driver Windows 7 master image to the FOG server](http://reseaux85.fr/index.php?title=FOG_:_Installation_du_serveur_-_Cr%C3%A9ation_master_-_Upload#Proc.C3.A9dure_d.27Upload_du_poste_mod.C3.A8le.2Fmaitre)
- [Deploy WAPT using waptdeploy (GPO)](http://dev.tranquil.it/wiki/WAPT_-_Déploiement_de_WAPT_par_GPO)
- Deploy the image with FOG
- Activate Windows 7 (and Office) automatically with KMS
- FOG client automatically renames the PC
- FOG client automatically joins the machine to the domain
- Apply GPOs (with Active Directory or [Samba4](https://dev.tranquil.it/wiki/Samba4))
- At first logon in the domain, waptdeploy installs WAPT
- [WAPT then installs all required software](http://wiki.lesfourmisduweb.org/index.php/Installation_et_utilisation_Serveur_et_console_WAPT#Gestion_des_Pc_et_des_paquets_dans_la_console)
- Done 🙂 
- Windows updates via WSUS (to save bandwidth)
- SRP (Software Restriction Policies) to avoid getting the machines trashed

The advantage of this setup (FOG + WAPT) is that if a workstation breaks and Wake‑on‑LAN is properly configured, I often don’t even need to leave my desk… except for hardware issues.

[![INTRO_TEND2010](images/INTRO_TEND2010-300x200.814e6d12.jpg)](../wp-content/uploads/2015/07/INTRO_TEND2010.jpg)

---
title: 'WAPT: apt‑get for Windows'
date: '2015-01-25'
slug: wapt-apt-get-pour-windows
lang: en
key: wapt-apt-get-pour-windows
---

I just discovered a new deployment tool: **WAPT**.

WAPT helps day‑to‑day operations by automating installations, uninstallations and updates of all software in an IT fleet.

[![800px-Schema-wapt.svg](images/800px-Schema-wapt.svg_-300x111.41a808a6.png)](../wp-content/uploads/2015/01/800px-Schema-wapt.svg_.png)

There is a “WAPT Starter” version that I use for individuals or small businesses (very close to APT on Linux): you install the desired software through a small web interface, and when updates are available in the WAPT repository (http://wapt.tranquil.it/wapt), it offers to install them automatically.

With “WAPT Server”, you can fully manage software from a central management console with your own private repository.

General idea of WAPT Server:

Once the WAPT client is installed, you can define groups like `pc_service_commercial` and `pc_service_compta` and push them to machines.

You can choose different deployment modes:
- Install immediately
- Install updates at shutdown
- Let the user install updates when they want

More bonuses:
- WAPT supports multi‑site private repositories, and repositories can be reachable from outside — very convenient for salespeople on the road.
- Packages are downloaded locally when an update is available; the installation can happen while disconnected from the network.
- Packages are shareable (file export or public repo). I have my own public repository:
  http://wapt.lesfourmisduweb.org/

Official documentation and presentation:
Video doc: http://doc.tranquil.it/co/portail.html

Installation:
My installation (wiki): http://wiki.sono-syrius.fr/index.php/Serveur_WAPT  
Official wiki: http://dev.tranquil.it/wiki/WAPT_-_apt-get_pour_Windows

---
title: Managing WAPT with an all‑in‑one package
date: '2016-12-17'
slug: gestion-wapt-all-in-one-package
lang: en
key: gestion-wapt-all-in-one-package
---

![All-in-one package illustration](images/AllInOneBox-1.9acb66db.jpg)

Hi — it’s been a while! Today, a WAPT post 🙂

I’d like to manage WAPT in a different way. Let’s forget the console for 30 seconds and create a WAPT package that installs… WAPT packages.

Before WAPT I used WPKG, and what I liked was managing packages based on workstation names.

We can do the same with WAPT. The idea is:
- Install on all machines a WAPT package named `tis-all-in-on-package`
- In that package, define which WAPT packages should be installed/removed/ignored, based on different tests

I built an example package here:
https://wapt.lesfourmisduweb.org/tous-les-packages?recherche=smp-all-in-one-package

It includes several examples you can reuse.

This lets you go as far as Python allows in the decision logic. When you manage a large fleet, it’s very convenient: **one single WAPT package drives the whole fleet**.

I know some of you want to manage software based on AD OUs — with this approach, it could be possible 😉

---
title: 'Update: fighting ransomware'
date: '2016-03-09'
slug: maj-lutter-contre-ransomwares
lang: en
key: maj-lutter-contre-ransomwares
---

![detecter-logiciel-espion](images/detecter-logiciel-espion-300x225.df85a3ac.jpg)

Some time ago I wrote a post: **“Fighting ransomware”**:

> [Fighting ransomware](../lutter-contre-les-ransomware/index.html)

Today, a small update is needed.

I collected ransomware samples from my spam inbox and started testing them one by one.

**What changes compared to the previous article (what I need to do):**
- Add the **.js** extension to the list of forbidden extensions in Software Restriction Policies GPOs
- Block **macros** in Microsoft Office using Microsoft’s ADMX GPO templates:
  https://www.microsoft.com/en-us/download/details.aspx?id=35554  
  Set **“VBA Macro Notification Settings”** to **“Disable all without notification”**. In my organization, nobody uses macros, so there’s no good reason to keep them enabled.
- And of course: keep software up to date so vulnerabilities can’t be exploited. Example:
  http://www.lemondeinformatique.fr/actualites/lire-adobe-corrige-24-failles-dans-flash-player-dont-celle-utilisee-par-les-ransomwares-64462.html

### Edit

I’m only describing technical methods here.

K3nny rewrote what I wrote here in a cleaner way:
http://reseaux85.fr/index.php?title=Strat%C3%A9gie_de_Restriction_Logiciel_et_Applocker

and here:
http://reseaux85.fr/index.php?title=S%C3%A9curit%C3%A9_-_Crypto-Locker/Ransomware

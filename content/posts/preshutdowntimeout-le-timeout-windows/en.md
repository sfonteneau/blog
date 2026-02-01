---
title: 'PreshutdownTimeout: Windows timeout for shutdown scripts'
date: '2015-10-18'
slug: preshutdowntimeout-le-timeout-windows
lang: en
key: preshutdowntimeout-le-timeout-windows
---

[![time_out-bras](images/time_out-bras-300x128.6b9c3268.jpg)](../wp-content/uploads/2015/10/time_out-bras.jpg)

Hello,

A quick post in the **WAPT** category.

I just discovered the `PreshutdownTimeout` registry key in Windows.

Read the sections “Maximum wait time for Group Policy scripts” and “Change History”:
https://technet.microsoft.com/en-us/library/cc757265(v=ws.10).aspx

By default, Windows kills a script if it runs longer than 15 minutes (when running GPO scripts). This is annoying with `c:\wapt\waptexit.exe` (install at shutdown) because it is launched through GPO scripts. I’ve already had issues with Microsoft Office or SolidWorks installations. So we need to change the default timeout.

```
I followed Microsoft recommendations:
First I changed the GPO:

Computer GPO → Windows Settings → System → Scripts →
"Specify maximum wait time for Group Policy scripts"
I set the value to 0, which means infinite timeout.
```

Then I increased:
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\gpsvc\PreshutdownTimeout`

The key can’t be modified as a normal administrator — it must be changed as SYSTEM. That’s convenient: WAPT installs as SYSTEM when it’s not run from the command line.

So I created a WAPT package to modify this value:

`smp-preshutdowntimeout`  
http://wapt.lesfourmisduweb.org/wapt/

By default, the package changes the timeout from 15 minutes to **3 hours** (other values are available inside `setup.py`).

Tested with a 40‑minute sleep package: it works!

My investigation on the WAPT mailing list:
http://lists.tranquil.it/pipermail/wapt/2015-October/001343.html

Hubert announced that the value would later be handled by WAPT via a parameter in `wapt-get.ini`.

Simon

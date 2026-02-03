---
title: 'OwnCloud: mounting WebDAV as a network drive on Windows'
date: '2016-04-07'
slug: owncloud-lecteur-reseau-webdav
lang: en
key: owncloud-lecteur-reseau-webdav
---

![webfolder](images/webfolder-150x150.a85e6894.jpg)

Another short post about an issue I ran into.

In my school we deployed an OwnCloud. It’s very useful for teachers and students from outside. With the desktop client on teachers’ personal computers, it’s perfect.

Internally, it’s more complicated. I first thought about exposing a Samba share and mapping a network drive, but permissions between Samba and OwnCloud can get messy.

A simpler solution: **WebDAV**.

On Windows, once mounted, WebDAV behaves like a network drive. Because it’s a standard, it’s also available on many mobile devices.

![16284069063_f3684ae5c2_o](images/16284069063_f3684ae5c2_o-150x150.a3befd06.png)

## Making WebDAV work on Windows

First: instead of changing the Windows `BasicAuthLevel` registry key like some sites suggest, I recommend using a Let’s Encrypt certificate. It’s free and at least gives you proper security.

### OwnCloud / Windows / ServerName

Make sure that when you browse to https://<owncloud-ip> you actually reach the OwnCloud site. In my case, I had several websites in the DMZ (`aide.lesfourmisduweb.org` and `cloud.lesfourmisduweb.org`) managed with `ServerName` and `ServerAlias` in `aide.conf` and `cloud.conf`.

Example:

ServerName cloud.lesfourmisduweb.org  
ServerAlias owncloud.lesfourmisduweb.org

If the requested site name is unknown, Apache serves the first virtual host alphabetically from:

`/etc/apache2/sites-enabled/`

So when I typed my IP, I landed on `aide.lesfourmisduweb.org`.

Back to OwnCloud WebDAV on Windows: it does not support **SNI** (Server Name Indication). As OwnCloud mentions:

> The Windows WebDAV Client might not support Server Name Indication (SNI) on encrypted connections…

So WebDAV fails.

To fix this, I renamed `cloud.conf` to `aaacloud.conf` so it becomes the first vhost.

That’s why it matters that https://<owncloud-ip> resolves to OwnCloud.

### Map the network drive

Once everything is set, from a Windows script you can do:

```
net use z: "https://cloud.lesfourmisduweb.org/remote.php/webdav/" /savecred /persistent:yes
```

Done — your WebDAV drive works.

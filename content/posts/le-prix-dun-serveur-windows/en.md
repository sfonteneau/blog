---
title: The cost of a Windows Server
date: '2015-03-28'
slug: le-prix-dun-serveur-windows
lang: en
key: le-prix-dun-serveur-windows
---

![02748596-photo-verrou-drm](images/02748596-photo-verrou-drm1-300x225.e6f09edf.jpg)

Hello everyone!

I finally decided to write a Samba 4 article (coming soon).

But first, here’s “The cost of a Windows Server” — to understand potential savings.

Let’s imagine I want a Windows Server with Active Directory. What do I need to pay?

## Windows Server license

I found Windows Server 2012 R2 Standard at **668€ (excl. VAT)**.

## CALs (Client Access Licenses)

But having a Windows Server license is not enough to legally connect clients to it (how ironic): you also have to buy CALs.

What’s a CAL?

A Windows Server CAL is required as soon as a workstation (device) or a user authenticates to access basic Windows Server services (Active Directory, file and/or print sharing, etc.).

- A **user CAL** is tied to a person and can be used across multiple devices.
- A **device CAL** is tied to a machine; any user of that machine can use it.

CAL versions must match the Windows Server version (a 2003 CAL is not valid for Server 2008, **$$$**… although a 2008 CAL can be downgraded for Server 2003).

In other words, a Windows Server license without CALs is useless.

More info:
http://hebergement.u-psud.fr/distribution/acheter-a-la-di/microsoft/21-cal-client-acces-licence-microsoft.html

Some Windows Server editions don’t need CALs or include some. See:
http://www.microsoft.com/OEM/fr/licensing/productlicensing/Pages/server-cal.aspx#fbid=pWJXAn-6Z9m

![tumblr_n0xm24qMfD1rb2l1co1_400](images/tumblr_n0xm24qMfD1rb2l1co1_4001-300x210.745a20ae.gif)

## Virtualization mobility licensing

If you have several virtualization servers (XenServer, Proxmox, VMware vSphere Hypervisor or Microsoft Hyper‑V), Microsoft may require a “mobility” license if you migrate VMs between physical hosts.

More info:
http://blogs.technet.com/b/fesnouf/archive/2013/12/26/licensing-windows-2012-standard.aspx

To be continued…

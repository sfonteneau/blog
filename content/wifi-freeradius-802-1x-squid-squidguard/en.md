---
title: 'Wi‑Fi auth & filtering: FreeRADIUS, 802.1X, Squid, SquidGuard'
date: '2016-03-27'
slug: wifi-freeradius-802-1x-squid-squidguard
lang: en
key: wifi-freeradius-802-1x-squid-squidguard
---

![Coffee mug decorated with a Wi-Fi symbol](images/SKU288251-03-300x300.fad7a7fa.gif)

Some time ago I wrote “Why you shouldn’t use Squid in transparent mode?”. That covered filtering — but not authentication.

I considered PacketFence, but it’s more of a NAC solution. pfSense is interesting too, but didn’t fit my project. PacketFence is also too resource‑hungry for what I wanted.

So I built my own “handmade” solution. Here’s a short presentation video:
https://www.youtube.com/watch?v=9ItnHyWaWMo

## Principle

A Wi‑Fi access point with **WPA2‑Enterprise** authentication connects to a FreeRADIUS server, itself connected to Active Directory (NTLM authentication). The certificate is a Let’s Encrypt one. Having a cert signed by a trusted root CA already installed on clients is useful: with self‑signed certs you must deploy your CA to all clients, which is annoying.

Once connected to Wi‑Fi, automatic proxy configuration does its job for browsers configured for “automatic proxy detection”. If not (often the case on smartphones), users are redirected to a page explaining how to enable auto‑detection or set the proxy manually.

On the server side, Squid logs MAC addresses browsing in HTTP/HTTPS. FreeRADIUS logs Wi‑Fi connections with usernames and associated MAC addresses (see video).

This setup is interesting, but it doesn’t solve everything.

When a user changes their password, the connection fails — which is good — but then the user often has to delete the Wi‑Fi profile and re‑enter the password. Too bad. Also, older devices don’t support 802.1X.

One advantage (or disadvantage, depending on your point of view): frequent re‑authentication is not required. For a smartphone coming and going, it’s great. For a shared PC, less great…

Also, this method does not allow you to show “terms of use” like a captive portal. I think users should sign an acceptable use policy when accounts are provided (or it should be in the IT charter).

To be clear: I didn’t find a perfect solution, but this seems like a good compromise for my network.

And it uses very little memory — it can run on a Raspberry Pi 🙂

Today, I feel there’s still no ideal solution for public Wi‑Fi hotspots. Captive portals teach users to bypass SSL warnings, and they don’t work well with HSTS (e.g., Google as a default start page). 802.1X can’t easily present terms or SMS registration pages either. In a world full of “free Wi‑Fi”, we need real solutions that protect users **and** Internet providers.

[![Browser warning page for an untrusted HTTPS certificate](images/141106073506427079-150x150.d21da2ff.jpg)](../wp-content/uploads/2016/03/141106073506427079.jpg)

I’ll write a wiki tutorial when I have some time.

Edit 2016‑04‑10:
Documentation is here: https://wiki.lesfourmisduweb.org/radius_wifi.html

---
title: Blocking the Tor network
date: '2015-01-29'
slug: bloquer-le-reseau-tor
lang: en
key: bloquer-le-reseau-tor
---

![tor_browser_logo__no_trans_background__by_j_bob-d5gjsad](images/tor_browser_logo__no_trans_background__by_j_bob-d5gjsad-300x184.aa975f6d.png)

I work in a high school and a middle school, which means I have to prevent students from browsing non‑educational websites…

For a while now, “Tor Browser” has been around.

How it works:
- It doesn’t require admin rights to run.
- At startup, Tor asks whether your network uses a proxy. If you answer “no”, it tries to contact Tor IPs through the default gateway and scans for any ports that can reach the Internet.

A first layer of protection is therefore to prevent clients from going directly to the Internet and to enforce a proxy. Only the proxy is allowed outbound access. Tor will scan and never find an exit.

![jns_ch12-18](images/jns_ch12-18-300x157.c92ee60a.gif)

But Tor can also work through a proxy (if configured). The principle is:
Tor contacts a Tor IP through the proxy and keeps the connection open, then tunnels Tor traffic through it.

So the solution is to block, in Squid (or another proxy), connections to Tor IP addresses.

Luckily, this site lists most public Tor IPs:
https://www.dan.me.uk/torlist/

I published a short tutorial on my wiki here:
https://wiki.lesfourmisduweb.org/blocktor.html

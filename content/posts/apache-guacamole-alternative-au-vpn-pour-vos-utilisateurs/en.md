---
title: Apache Guacamole – a VPN alternative for your users
date: '2017-06-29'
slug: apache-guacamole-alternative-au-vpn-pour-vos-utilisateurs
lang: en
key: apache-guacamole-alternative-au-vpn-pour-vos-utilisateurs
---

![](images/guac-tricolor-300x300.4bd742ff.png)

A quick introduction to a product that many blogs already talk about.

Guacamole provides your users with a centralized **web** interface for **RDP**, **VNC** and **SSH** connections. In my case, I’m mainly interested in replacing direct RDP exposure (too vulnerable to attacks). It can be a very practical alternative to classic VPN access.

The goal is to give the user an RDP session to a remote desktop server (TSE/RDS) through a web interface. You’re no longer tied to an OS: the user can be on Windows, Linux or macOS (and potentially tablets/smartphones too). The RDP session is displayed in the browser via HTML5.

Guacamole can be connected to LDAP/Active Directory for authentication. For better security, enable multi‑factor authentication (SMS, authenticator app, etc.) and consider fail2ban to block IPs after too many failed attempts.

Guacamole can also be used for screen sharing: you can share a link and decide whether viewers can control the machine or only watch. Handy for product demos.

I’m presenting Guacamole as a VPN alternative, but it can also be an excellent solution in schools to give access to Linux applications from Windows machines (and the other way around).

---
title: Why you shouldn’t use Squid in transparent mode
date: '2015-04-15'
slug: pourquoi-il-ne-faut-pas-utiliser-squid-en-mode-transparent
lang: en
key: pourquoi-il-ne-faut-pas-utiliser-squid-en-mode-transparent
---

[![c81f772e265991de09ad69a5a6dfb071](images/c81f772e265991de09ad69a5a6dfb071-300x173.b97ff849.jpg)](../wp-content/uploads/2015/04/c81f772e265991de09ad69a5a6dfb071.jpg)

First, you need to understand the difference between browsing with a declared proxy and browsing without a proxy.

### Without a proxy

The computer connects directly to the server hosting the requested website. It resolves the IP via DNS and then connects through the gateway.

### With a proxy configured in the browser

It’s different: the computer does **not** directly contact the destination server. The browser sees the proxy configuration and says:

- “Hey proxy server 172.21.254.254:3128, can you fetch toto.fr for me and give me the web page?”

The proxy replies:
- “OK, here is the page you requested.”

The proxy is in the middle:

[![280px-Proxy_concept_en.svg](images/280px-Proxy_concept_en.svg_.751e60eb.png)](../wp-content/uploads/2015/04/280px-Proxy_concept_en.svg_.png)

## Transparent proxy

Squid has a transparent proxy mode: it lets Squid sit in place of the gateway, so the computer *thinks* it talks directly to the website server.

This works fine for HTTP browsing, but it does **not** work well for HTTPS.

Why?

HTTPS encrypts and secures connections. It can verify that the connection hasn’t been spoofed (domain name verification, certificates, trusted root CA validation). The whole point is to protect the connection.

[![header_icon](images/header_icon.6f96c434.png)](../wp-content/uploads/2015/04/header_icon.png)

Squid can intercept SSL in transparent mode, but it requires pre‑installing a custom root CA. Websites don’t like that, because it means decrypting HTTPS traffic. Also, some sites rely on SNI:
http://www.rackspace.com/knowledge_center/article/serving-secure-sites-with-sni-on-apache

This is basically a man‑in‑the‑middle approach:

[![sslmim](images/sslmim-300x149.3ca8be79.png)](../wp-content/uploads/2015/04/sslmim.png)

Solutions like ALCASAR exist (http://www.alcasar.net/fr/telechargement?func=select&id=11), but I’m not a fan. They filter using DNS requests (dnsmasq) combined with IP requests (iptables), Squid and DansGuardian for HTTP.

Some transparent filtering approaches (e.g. SonicWALL) work similarly.

## The solution I use

The cleanest solution I’ve found is to **declare the proxy**. When a user isn’t configured to use the proxy, they get redirected to a page explaining how to configure their browser or phone.

More in a next post… with a more reliable solution.

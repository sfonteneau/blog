---
title: The rise of MITM SSL inspection
date: '2020-06-27'
slug: la-generalisation-du-filtrage-mitm
lang: en
key: la-generalisation-du-filtrage-mitm
---

![](images/wp-thumb.php_.9231a319.png)

During my many trips, I’ve noticed that **MITM SSL inspection** by firewalls is increasingly common in companies and public organizations. So I decided to talk about it.

## Background

Let’s go back to basics: why was HTTPS invented?

In companies, encrypting traffic to prevent attackers from capturing sensitive information became critical (especially for banks, e‑commerce, etc.).

How it works: the browser can verify it’s talking to the right server thanks to the website certificate. The connection is encrypted and unreadable by an attacker sitting on a router, for example. A small revolution: we can be confident we’re talking to the right server, over an encrypted channel.

## What is MITM filtering?

Most of the time, it’s your company firewall that behaves “like an attacker” and inspects all traffic to allow or block it.

### How does it work?

To inspect HTTPS content, you install the firewall certificate into the clients’ certificate stores (Windows store, Firefox, applications…). Then, while browsing, the firewall terminates TLS with its own key, decrypts and inspects traffic (passwords, emails, images — everything), then re‑encrypts it.

## What should we think about it?

I’m not blaming the concept… but you must be transparent with users and clearly inform them.

If you do MITM inspection, you need to be rigorous. The inspection device is often the firewall — and ironically it’s directly exposed to the Internet.

So you must (even more than usual) keep it fully updated: any security flaw is critical because it can lead to traffic decryption by an attacker.

Likewise, if you replace the device, ensure the private key has been wiped from the old unit before disposing of it.

Too often the feature is enabled without the admin realizing the responsibility they take toward users.

And of course, you should never ask users to install your inspection certificate on their personal devices (for guest Wi‑Fi for example). I’ve been asked to do that while traveling — my answer was a firm “no”.

## Conclusion

The goal is not to blame but to open a discussion on a practice that is becoming widespread. If you’re a user, talk about it with your sysadmin.

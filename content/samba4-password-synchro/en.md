---
title: 'Samba4: password synchronization'
date: '2018-12-09'
slug: samba4-password-synchro
lang: en
key: samba4-password-synchro
---

![](images/syncpassword.8eb6c67d.png)

Hello everyone,

A quick post to announce that I finally looked again at password synchronization with Samba4.

Password sync with Google Apps:
https://github.com/sfonteneau/samba4-gaps

This is clearly derived from [baboons’ version](https://github.com/baboons/samba4-gaps), but it no longer requires enabling `store-plaintext` in Samba4.  
It does require enabling `CryptSHA256` in `smb.conf`.

Compared to baboons’ script, this new one does not resend all passwords on restart: it checks whether `pwdLastSet` changed since the last sync. It can be adapted for other applications that accept CryptSHA256 or CryptSHA512.

I also looked at syncing passwords to applications that do not support CryptSHA256/CryptSHA512, like Windows Azure…

In that case, the only solution is to store user passwords in clear text, which means using `store-plaintext` in Active Directory.

I wrote a script that retrieves clear‑text passwords and passes them to another script; once processed, the clear‑text password is removed:
https://github.com/sfonteneau/samba4-sync-password

For Windows Azure, the previous script can call a password‑change script in Azure:
https://github.com/sfonteneau/send_password_in_azure

Once the password is properly sent to Azure, it is removed from Samba.

Hope this helps!

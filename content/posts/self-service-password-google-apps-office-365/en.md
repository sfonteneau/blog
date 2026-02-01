---
title: Self Service Password + sync to Google Apps and Office 365
date: '2016-07-21'
slug: self-service-password-google-apps-office-365
lang: en
key: self-service-password-google-apps-office-365
---

![change-your-password-623x427](images/change-your-password-623x427.96ed022b.jpg)

A useful post for Samba and Windows Active Directory.

In my organization we have more and more BYOD laptop classes (students bring their own laptop).

Credentials used for Wi‑Fi, OwnCloud, etc. are the AD ones. If a user wants to change their password, they must log on to a domain‑joined PC to do it — not convenient.

So I deployed **Self Service Password**:
http://ltb-project.org/wiki/documentation/self-service-password

It’s a web page that allows users to change their password:

[![ssp_change_nooptions](images/ssp_change_nooptions-150x150.363d600b.png)](../wp-content/uploads/2016/07/ssp_change_nooptions.png)

But it can go further. If a password is forgotten, it can offer multiple reset methods:
- Reset by questions
- Reset by mail challenge (token sent by email)
- Reset by SMS (through an external Email‑to‑SMS service)

Additional features include fine‑grained password policy management.

It can also send an email after a password change to detect suspicious behavior.

One feature is especially interesting: **posthook**.

A posthook is a script that receives the username and the new password after the change.

I use the posthook to send the new password to Google Apps and Office 365 with Samba4.

Previously, for Samba4, I used scripts like:
https://github.com/baboons/samba4-gaps

But that forces me to store passwords in a reversible way in AD, and I don’t like that.

Another approach would be `check password script`, but unfortunately it didn’t work with Samba4 at the time:
https://lists.samba.org/archive/samba/2016-June/200293.html

**Edit 2016‑11‑08:**  
**`check password script` seems supported in Samba 4.5, but I didn’t find a way to recover the username :-/**

This kind of system is very useful with AD. Office 365 password sync is not instant (every ~15 minutes). With the Office 365 scripts I use, the change is immediate.

Here is my posthook script for Google Apps and Office 365:
https://github.com/sfonteneau/script_modify_password_googleapps_and_office365/

Warning: for the script to work, the password complexity policy must be **8 characters minimum and 16 maximum**.

I hope `check password script` becomes fully usable again.

**Edit 2019:**  
See: https://blog.lesfourmisduweb.org/samba4-password-synchro/

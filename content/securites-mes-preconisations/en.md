---
title: 'Security: my recommendations'
date: '2017-05-13'
slug: securites-mes-preconisations
lang: en
key: securites-mes-preconisations
---

![Figure holding a Safety First sign](images/secu3.e84ba482.jpg)

Hello everyone…

Here are some security recommendations for your networks. I’m aware not everything is applicable everywhere.

## Protection against Internet‑facing attacks

- Review your firewall rules
- Any Internet‑exposed application should be placed in a DMZ to limit damage if it gets compromised (reduces pivoting inside)
- Deploy fail2ban on services exposed to the outside
- Use HTTPS to avoid passwords traveling in clear text (easy with Let’s Encrypt), and force HTTPS

## Endpoint security recommendations

- Keep software up to date (→ with WAPT 😉)
- Keep Windows workstations up to date (at least security patches)
- Keep Linux servers up to date
- Keep the services installed on servers up to date
- Deploy SRP (Software Restriction Policies)
  - Ideally, users should not be able to execute files from locations where they have write access
- Disable or secure macros in Microsoft Office and LibreOffice
- Disable JavaScript execution in PDF readers (e.g. Adobe Reader)
- Block unnecessary open ports with the firewall (Windows Firewall, etc.)

## Dangerous downloads / attachments

- Filter dangerous attachments on your email system
- Enforce a filtering proxy (users cannot go directly to the Internet)
- Ideally deploy an IDS (e.g. Snort) to inspect traffic and block suspicious behaviors

## Limiting damage when ransomware starts

For file servers (Samba):
- Enable deletion auditing with `vfs objects = full_audit`
- Use fail2ban to analyze Samba audit logs
- Deploy a canary file like `detecte_ransomware.doc` on shares  
  If suspicious behavior is detected (weird extensions, canary file deletion), fail2ban can trigger an action to stop the attack.
- Grant users only the access they really need (clean up permissions)
- Obviously: have working backups

## Admin practices

- Avoid using an account member of “Domain Admins” for daily operations; create dedicated admin groups for workstations
- Users should of course not be local admins or domain admins

## Physical security

- In BIOS: block booting from external media (USB/CD) and require a BIOS password
- Prevent easy physical access to the motherboard, otherwise BIOS passwords can often be reset

## Secure physical access to network equipment

- Lock rooms/cabinets, etc. 🙂

## Network access control

- Deploy 802.1X to block network access for unauthorized machines
- Same for Wi‑Fi

## User awareness

- Communicate risks to users so they stay cautious

## Tech watch

- Stay informed via online resources. The vulnerability exploited by WannaCry was public a week before the large‑scale attack.
- Analyze what your email/proxy blocks: know your enemy to prepare better. Your system blocked one attack — will it block the next ones?

---
title: 'WPAD: Chrome vs Firefox'
date: '2015-11-09'
slug: wpad-chrome-firefox
lang: en
key: wpad-chrome-firefox
---

A short post about a silly issue I hit with WPAD in Chrome, Firefox and IE.

I wanted to use something like:

```
if (isInNet(myIpAddress(), "172.29.0.0", "255.255.0.0")) { return proxy_no; }
return proxy_yes;
```

Meaning: if you’re in VLAN 172.29.0.0, don’t apply the proxy; otherwise do.

It works perfectly in IE and Firefox, but not in Chrome 🙁

I contacted Google to understand why. It’s a bug:
https://code.google.com/p/chromium/issues/detail?id=267101

The issue has been open for a long time.

Google suggested a workaround: use `isInNetEx`:

```
if (isInNetEx(myIpAddress(), "172.29.0.0", "255.255.0.0")) { return proxy_no; }
return proxy_yes;
```

Great — it works in Chrome now! But then it no longer works at all in Firefox…

[![ob_06116c_220-f-43166878-pf3admr4fspxhl3mi4x7fu7tkjooikqx](images/ob_06116c_220-f-43166878-pf3admr4fspxhl3mi4x7fu7tkjooikqx-300x200.9d8e4e94.jpg)](../wp-content/uploads/2015/11/ob_06116c_220-f-43166878-pf3admr4fspxhl3mi4x7fu7tkjooikqx.jpg)

The only solution I found was to make sure Firefox never enters the `isInNetEx(myIpAddress()` loop (to avoid crashing), and explicitly declare all possible cases.

Example:

```
if (isInNet(myIpAddress(), "172.28.0.0", "255.255.0.0")) { return proxy_yes; }
if (isInNet(myIpAddress(), "172.29.0.0", "255.255.0.0")) { return proxy_no; }

if (isInNetEx(myIpAddress(), "172.28.0.0", "255.255.0.0")) { return proxy_yes; }
if (isInNetEx(myIpAddress(), "172.29.0.0", "255.255.0.0")) { return proxy_no; }
```

In short: you must declare `isInNet(myIpAddress()` for all your VLANs like this. Firefox will always stop at the first match.

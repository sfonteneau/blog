---
title: "When nginx also needs to know the hardware"
date: "2026-09-13"
slug: "nginx-chacha20-old-cpu"
lang: "en"
key: "nginx-chacha20-hardware"
---

![Open padlock connected to electronic circuit traces](images/cpu.png)

Hello everyone,

In my [previous article](/en/streaming-video-vlc-xspf-nginx/), I talked about my famous VLC server running on an old **0.8 GHz CPU**.

At first, I quickly noticed that the **throughput was not that great**. Since the server does no transcoding, I started wondering what could be using so much CPU.

After looking a little closer, HTTPS quickly became suspicious.

This old processor has **no hardware AES acceleration**. AES-GCM works perfectly well, but it has to run in software, and on such a limited machine that can become expensive.

In this situation, **ChaCha20-Poly1305** is often a much better fit.

A simple benchmark already shows the difference:

```bash
openssl speed -evp aes-128-gcm
openssl speed -evp chacha20-poly1305
```

Another interesting detail is that nginx lets the client influence the cipher choice by default with `ssl_prefer_server_ciphers off`.

A modern PC may therefore prefer AES because it has AES-NI… while my poor 0.8 GHz server also has to compute AES, but without any hardware acceleration.

On this kind of machine, it can therefore make sense to configure nginx to **prefer ChaCha20-Poly1305 on the server side**.

For example:

```nginx
ssl_prefer_server_ciphers on;

ssl_ciphers 'ECDHE-ECDSA-CHACHA20-POLY1305:
             ECDHE-RSA-CHACHA20-POLY1305:
             ECDHE-ECDSA-AES128-GCM-SHA256:
             ECDHE-RSA-AES128-GCM-SHA256:
             ECDHE-ECDSA-AES256-GCM-SHA384:
             ECDHE-RSA-AES256-GCM-SHA384';

ssl_conf_command Ciphersuites     TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384;
```

This choice is not unusual either: [modern OpenSSH](https://man.openbsd.org/sshd_config#Ciphers) also puts ChaCha20-Poly1305 first in its default cipher list.

And if, like me, you enjoy **reusing old hardware** instead of throwing it away, this is exactly the kind of small detail that can give it a second life.

We often try to optimize software while forgetting about the hardware underneath it. On machines like this, the two really have to work together.

On an old CPU or a Raspberry Pi 4, ChaCha may be the better choice.

On a recent processor with AES-NI or ARM AES extensions, the opposite will often be true.

**Same software, same configuration, different hardware: very different performance.**

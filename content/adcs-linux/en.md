---
title: "ADCS Linux"
date: "2025-09-24"
slug: "adcs-linux"
lang: "en"
key: "adcs-linux"
---

![adcs_linux](images/adcs_linux.png)

Hello everyone,

I started a new project on my [GitHub](https://github.com/sfonteneau/ADCS_python) — an ADCS server written in Python.

This project comes from a simple observation: some customers need **automatic enrollment** on their Windows machines, for example to manage 802.1x. Windows can do this with an ADCS.
But when the customer wants a Linux server (because they already use Samba4), there ultimately aren’t many other turnkey solutions available.

This project therefore emulates an **ADCS enrollment server** (not a client).
It reproduces the behavior of Microsoft ADCS Web Enrollment endpoints (CEP/CES) to handle certificate requests.

- **Certificate Enrollment Policy (CEP)**: exposes a policy endpoint to provide enrollment templates and certificate authority information to clients.
- **Certificate Enrollment Services (CES)**: emulates the service that accepts CSRs and returns signed certificates.

The goal is to emulate an ADCS Web Enrollment server that:

1. Provides the CEP policy (templates, CA info, etc.) to requesting clients.
2. Receives and validates PKCS#10 CSRs.
3. Processes submissions through CES and returns signed responses.

In this project, certificate templates are not defined through a traditional configuration.
They are defined via **Python callbacks**.

Each template is represented by an external module (for example ``callbacks/user_template.py``) exposing two required functions:

- **define_template(app_conf, kerberos_user)**
  → Dynamically describes the template properties (OID, EKU, KeyUsage, validity period, etc.) depending on the user or context.
- **emit_certificate(...)**
  → Takes the CSR and metadata as input, applies the required extensions, and issues a certificate signed by the certificate authority.

Why use callbacks?
------------------

- Provides **maximum flexibility**: template logic can depend on Active Directory attributes, group membership, external policies (ERP API), or any business rule.
- Avoids locking the CA server into static, predefined templates.

Security responsibility
-----------------------

This design shifts most security controls to the callback author. In practice:

- Eligibility checks (who is allowed to get what kind of certificate) must be implemented inside the callback.
- If the callback does not apply checks, any authenticated user can obtain any certificate returned by the module.
- The Python ADCS server does not enforce additional restrictions: it simply executes the callback and signs the result.

In short: **security and enforcement of issuance rules** are entirely the responsibility of the callback code.

The project was largely **coded with AI** (handy for converting hard-to-read Microsoft RFCs into working code).
It’s still early days, but feel free to send feedback!

---
title: "ADCS Linux"
date: "2025-09-24"
slug: "adcs-linux"
lang: "en"
key: "azure-ad-connect-et-openldap-2"
---

Lire en : [![French](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAAmVBMVEViZsViZMJiYrf9gnL8eWrlYkjgYkjZYkj8/PujwPybvPz4+PetraBEgfo+fvo3efkydfkqcvj8Y2T8UlL8Q0P8MzP9k4Hz8/Lu7u4DdPj9/VrKysI9fPoDc/EAZ7z7IiLHYkjp6ekCcOTk5OIASbfY/v21takAJrT5Dg6sYkjc3Nn94t2RkYD+y8KeYkjs/v7l5fz0dF22YkjWvcOLAAAAgElEQVR4AR2KNULFQBgGZ5J13KGGKvc/Cw1uPe62eb9+Jr1EUBFHSgxxjP2Eca6AfUSfVlUfBvm1Ui1bqafctqMndNkXpb01h5TLx4b6TIXgwOCHfjv+/Pz+5vPRw7txGWT2h6yO0/GaYltIp5PT1dEpLNPL/SdWjYjAAZtvRPgHJX4Xio+DSrkAAAAASUVORK5CYII=) Français](../../adcs-linux/index.html)


Hello everyone,


I started a new project on my [GitHub](https://github.com/sfonteneau/adcs_python): a Python ADCS server.


This project comes from a simple observation: some clients need **automatic enrollment** on their Windows machines, for example to handle 802.1x. Windows can do this with an ADCS. 
 But when the client wants a Linux server (because they already use Samba4), there are not many turnkey solutions available.


This project therefore emulates an **ADCS enrollment server** (not a client). 
 It reproduces the behavior of Microsoft ADCS Web Enrollment endpoints (CEP/CES) to handle certificate requests.


- **Certificate Enrollment Policy (CEP)**: exposes a policy endpoint to provide enrollment templates and certification authority information to clients.
- **Certificate Enrollment Services (CES)**: emulates the service that accepts CSRs and returns signed certificates.


The goal is to emulate a Web ADCS enrollment server that:


1. Provides CEP policy (templates, CA, etc.) to requesting clients.
2. Receives and validates PKCS#10 CSRs.
3. Processes submissions via CES and returns signed responses.


In this project, certificate templates are not declared in the usual configuration. 
 They are defined via **Python callbacks**.


Each template is represented by an external module (for example `callbacks/user_template.py`) exposing two required functions:


- **define\_template(app\_conf, kerberos\_user)** 
 → Dynamically describes template properties (OID, EKU, KeyUsage, validity period, etc.) based on the user or context.
- **emit\_certificate(...)** 
 → Takes the CSR and metadata as input, applies the necessary extensions, and issues the certificate signed by the CA.


#### Why use callbacks?


- Offers **maximum flexibility**: the template logic can depend on Active Directory attributes, group membership, external policies (ERP API), or any business rule.
- Prevents locking the CA server into static, predefined templates.


#### Security responsibility


This design transfers most security controls to the callback author. In practice:


- Eligibility controls (who is allowed to obtain which type of certificate) must be implemented inside the callback.
- If the callback does not perform checks, any authenticated user can obtain any certificate returned by the module.
- The Python ADCS server imposes no additional restrictions: it simply executes the callback and signs the result.


In short: **security and enforcement of issuance rules** are entirely the responsibility of the callback code.


The project was largely **coded with AI assistance** (useful for converting unreadable Microsoft RFCs into functional code). 
 The project is still in its early stages, but feel free to send feedback!

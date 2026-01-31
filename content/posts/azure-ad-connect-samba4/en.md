---
title: "Azure Ad Connect Samba4"
date: "2023-05-06"
slug: "azure-ad-connect-samba4-2"
lang: "en"
key: "azure-ad-connect-samba4"
---

![](images/AAD-Logosamba.45d2448b.png)


Hello


It’s been a long time since I’ve written on this blog.


Recently I came across several articles about how active directory password synchronization works with azure ad connect:

– [Microsoft how-password-hash-synchronization-works](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/connect/how-to-connect-password-hash-synchronization#how-password-hash-synchronization-works)

– [Dsinternals how-azure-active-directory-connect-syncs-passwords](https://www.dsinternals.com/en/how-azure-active-directory-connect-syncs-passwords/)


The operation is as follows: azure ad connect takes the hashnt encoded in utf16-le, and enters it in the PBKDF2-HMAC-SHA256″ function with 1000 iterations and random salt


These same researches brought me to Dr Nestori Syynimaa ([@DrAzureAD](https://twitter.com/DrAzureAD)):

[aadinternals long-passwords](https://aadinternals.com/post/long-passwords/) work which allows from a simple powershell script to send a hashnt.

So I try my luck with the powershell and I see that it works!

The code of Dr [@DrAzureAD](https://twitter.com/DrAzureAD) is opensource, so I think… there is surely a possibility to convert it in python to use it under linux and thus with samba.


After analysis of the code I understand that microsoft communicates with [WCF binary *xml*](https://fr.wikipedia.org/wiki/Windows_Communication_Foundation)  ,


Good news [the specification is open](https://learn.microsoft.com/en-us/openspecs/windows_protocols/mc-nbfx/94c66ea1-e79a-4364-af88-1fa7fef2cc33) and a python project exists on github : [python-wcfbin](https://github.com/ernw/python-wcfbin)


So I create a git repo named [AADInternals\_python](https://github.com/sfonteneau/AADInternals_python) which takes [the AADInternals code I’m interested in](https://github.com/Gerenios/AADInternals/blob/9cc2a3673248dbfaf0dccf960481e7830a395ea8/AzureADConnectAPI.ps1#L1087) and converts it into python. After fumbling around a bit… victory, the code works!


I then realize that the AADInternals project from [@DrAzureAD](https://twitter.com/DrAzureAD) includes everything needed to create/delete users and groups a la azuread so I have to port the rest of the code.


But in my tests, Microsoft servers respond:


> “The formatter threw an exception while trying to deserialize the message: There was an error while trying to deserialize parameter http://schemas.microsoft.com/online/aws/change/2010/01:syncRequest. The InnerException message was ‘Element ‘http://schemas.microsoft.com/2003/10/Serialization/Arrays:Value’ contains data from a type that maps to the name ‘:mustUnderstand’. The deserializer has no knowledge of any type that maps to this name. Consider using a DataContractResolver if you are using DataContractSerializer or add the type corresponding to ‘mustUnderstand’ to the list of known types – for example, by using the KnownTypeAttribute attribute or by adding it to the list of known types passed to the serializer.’. Please see InnerException for more details.”
> 
> 


So I understand that it is lib python-wcfbin that serializes badly in some cases.


So I ask at work a little help to more experienced devs and especially to [AndreasLrx](https://github.com/AndreasLrx)


He finds the problem, the microsoft specs are not up to date! We even do a pull request on the original project: <https://github.com/ernw/python-wcfbin/pull/16>


I now have everything I need to build a complete synchronization tool.


So I create on my github project a project: [AzureADConnect\_Samba4](https://github.com/sfonteneau/AzureADConnect_Samba4)


The project is able to send groups and users ansi as well as send hashnt (aadhash) to the azure ad.


The script then stores the latest information in a local sqlite database, it will send the object back to azure ad only if the object has been modified since the last send.


**WARNING** if you have already used the azure ad connect windows, you must identify your “sourceanchor” or “immutableId” from your previous configuration.


By default microsoft uses [objectGUID](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/plan-connect-design-concepts#sourceanchorSourceAnchorAttr=objectGUID) with [msDSConsistencyGuid](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/plan-connect-design-concepts#using-ms-ds-consistencyguid-as-sourceanchor), so i did the same, however, depending on the version your settings may be different.

It’s up to you to identify your sourceanchor to avoid duplicates and/or bad deletions.


Also note that the script does not support the [password writeback](https://learn.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-sspr-writeback) !


I hope this work will be useful to you! Do not hesitate to send me feedback!


Edit :


As of 05/13/2023, script also manages hybrid join devices.

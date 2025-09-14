## CVE-2023-52927
 In the Linux kernel, the following vulnerability has been resolved:

netfilter: allow exp not to be removed in nf_ct_find_expectation

Currently nf_conntrack_in() calling nf_ct_find_expectation() will
remove the exp from the hash table. However, in some scenario, we
expect the exp not to be removed when the created ct will not be
confirmed, like in OVS and TC conntrack in the following patches.

This patch allows exp not to be removed by setting IPS_CONFIRMED
in the status of the tmpl.



- [https://github.com/seadragnol/CVE-2023-52927](https://github.com/seadragnol/CVE-2023-52927) :  ![starts](https://img.shields.io/github/stars/seadragnol/CVE-2023-52927.svg) ![forks](https://img.shields.io/github/forks/seadragnol/CVE-2023-52927.svg)

## CVE-2023-52709
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/KevinMitchell-OSWP-CISSP/CVE-2023-52709-PoC](https://github.com/KevinMitchell-OSWP-CISSP/CVE-2023-52709-PoC) :  ![starts](https://img.shields.io/github/stars/KevinMitchell-OSWP-CISSP/CVE-2023-52709-PoC.svg) ![forks](https://img.shields.io/github/forks/KevinMitchell-OSWP-CISSP/CVE-2023-52709-PoC.svg)

## CVE-2023-52654
 In the Linux kernel, the following vulnerability has been resolved:

io_uring/af_unix: disable sending io_uring over sockets

File reference cycles have caused lots of problems for io_uring
in the past, and it still doesn't work exactly right and races with
unix_stream_read_generic(). The safest fix would be to completely
disallow sending io_uring files via sockets via SCM_RIGHT, so there
are no possible cycles invloving registered files and thus rendering
SCM accounting on the io_uring side unnecessary.



- [https://github.com/FoxyProxys/CVE-2023-52654](https://github.com/FoxyProxys/CVE-2023-52654) :  ![starts](https://img.shields.io/github/stars/FoxyProxys/CVE-2023-52654.svg) ![forks](https://img.shields.io/github/forks/FoxyProxys/CVE-2023-52654.svg)

## CVE-2023-52251
 An issue discovered in provectus kafka-ui 0.4.0 through 0.7.1 allows remote attackers to execute arbitrary code via the q parameter of /api/clusters/local/topics/{topic}/messages.



- [https://github.com/BobTheShoplifter/CVE-2023-52251-POC](https://github.com/BobTheShoplifter/CVE-2023-52251-POC) :  ![starts](https://img.shields.io/github/stars/BobTheShoplifter/CVE-2023-52251-POC.svg) ![forks](https://img.shields.io/github/forks/BobTheShoplifter/CVE-2023-52251-POC.svg)

## CVE-2023-52160
 The implementation of PEAP in wpa_supplicant through 2.10 allows authentication bypass. For a successful attack, wpa_supplicant must be configured to not verify the network's TLS certificate during Phase 1 authentication, and an eap_peap_decrypt vulnerability can then be abused to skip Phase 2 authentication. The attack vector is sending an EAP-TLV Success packet instead of starting Phase 2. This allows an adversary to impersonate Enterprise Wi-Fi networks.



- [https://github.com/Helica-core/eap_pwn](https://github.com/Helica-core/eap_pwn) :  ![starts](https://img.shields.io/github/stars/Helica-core/eap_pwn.svg) ![forks](https://img.shields.io/github/forks/Helica-core/eap_pwn.svg)

## CVE-2023-52076
 Atril Document Viewer is the default document reader of the MATE desktop environment for Linux. A path traversal and arbitrary file write vulnerability exists in versions of Atril prior to 1.26.2. This vulnerability is capable of writing arbitrary files anywhere on the filesystem to which the user opening a crafted document has access. The only limitation is that this vulnerability cannot be exploited to overwrite existing files, but that doesn't stop an attacker from achieving Remote Command Execution on the target system. Version 1.26.2 of Atril contains a patch for this vulnerability.



- [https://github.com/febinrev/slippy-book-exploit](https://github.com/febinrev/slippy-book-exploit) :  ![starts](https://img.shields.io/github/stars/febinrev/slippy-book-exploit.svg) ![forks](https://img.shields.io/github/forks/febinrev/slippy-book-exploit.svg)

## CVE-2023-51810
 SQL injection vulnerability in StackIdeas EasyDiscuss v.5.0.5 and fixed in v.5.0.10 allows a remote attacker to obtain sensitive information via a crafted request to the search parameter in the Users module.



- [https://github.com/Pastea/CVE-2023-51810](https://github.com/Pastea/CVE-2023-51810) :  ![starts](https://img.shields.io/github/stars/Pastea/CVE-2023-51810.svg) ![forks](https://img.shields.io/github/forks/Pastea/CVE-2023-51810.svg)

## CVE-2023-51802
 Cross Site Scripting (XSS) vulnerability in the Simple Student Attendance System v.1.0 allows a remote attacker to execute arbitrary code via a crafted payload to the page or class_month parameter in the /php-attendance/attendance_report component.



- [https://github.com/geraldoalcantara/CVE-2023-51802](https://github.com/geraldoalcantara/CVE-2023-51802) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-51802.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-51802.svg)

## CVE-2023-51801
 SQL Injection vulnerability in the Simple Student Attendance System v.1.0 allows a remote attacker to execute arbitrary code via a crafted payload to the id parameter in the student_form.php and the class_form.php pages.



- [https://github.com/geraldoalcantara/CVE-2023-51801](https://github.com/geraldoalcantara/CVE-2023-51801) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-51801.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-51801.svg)

## CVE-2023-51800
 Cross Site Scripting (XSS) vulnerability in School Fees Management System v.1.0 allows a remote attacker to execute arbitrary code via a crafted payload to the main_settings component in the phone, address, bank, acc_name, acc_number parameters, new_class and cname parameter, add_new_parent function in the name email parameters, new_term function in the tname parameter, and the edit_student function in the name parameter.



- [https://github.com/geraldoalcantara/CVE-2023-51800](https://github.com/geraldoalcantara/CVE-2023-51800) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-51800.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-51800.svg)

## CVE-2023-51764
 Postfix through 3.8.5 allows SMTP smuggling unless configured with smtpd_data_restrictions=reject_unauth_pipelining and smtpd_discard_ehlo_keywords=chunking (or certain other options that exist in recent versions). Remote attackers can use a published exploitation technique to inject e-mail messages with a spoofed MAIL FROM address, allowing bypass of an SPF protection mechanism. This occurs because Postfix supports LF.CRLF but some other popular e-mail servers do not. To prevent attack variants (by always disallowing LF without CR), a different solution is required, such as the smtpd_forbid_bare_newline=yes option with a Postfix minimum version of 3.5.23, 3.6.13, 3.7.9, 3.8.4, or 3.9.



- [https://github.com/duy-31/CVE-2023-51764](https://github.com/duy-31/CVE-2023-51764) :  ![starts](https://img.shields.io/github/stars/duy-31/CVE-2023-51764.svg) ![forks](https://img.shields.io/github/forks/duy-31/CVE-2023-51764.svg)

- [https://github.com/eeenvik1/CVE-2023-51764](https://github.com/eeenvik1/CVE-2023-51764) :  ![starts](https://img.shields.io/github/stars/eeenvik1/CVE-2023-51764.svg) ![forks](https://img.shields.io/github/forks/eeenvik1/CVE-2023-51764.svg)

- [https://github.com/d4op/CVE-2023-51764-POC](https://github.com/d4op/CVE-2023-51764-POC) :  ![starts](https://img.shields.io/github/stars/d4op/CVE-2023-51764-POC.svg) ![forks](https://img.shields.io/github/forks/d4op/CVE-2023-51764-POC.svg)

- [https://github.com/Double-q1015/CVE-2023-51764](https://github.com/Double-q1015/CVE-2023-51764) :  ![starts](https://img.shields.io/github/stars/Double-q1015/CVE-2023-51764.svg) ![forks](https://img.shields.io/github/forks/Double-q1015/CVE-2023-51764.svg)

## CVE-2023-51698
 Atril is a simple multi-page document viewer. Atril is vulnerable to a critical Command Injection Vulnerability. This vulnerability gives the attacker immediate access to the target system when the target user opens a crafted document or clicks on a crafted link/URL using a maliciously crafted CBT document which is a TAR archive. A patch is available at commit ce41df6.



- [https://github.com/febinrev/atril_cbt-inject-exploit](https://github.com/febinrev/atril_cbt-inject-exploit) :  ![starts](https://img.shields.io/github/stars/febinrev/atril_cbt-inject-exploit.svg) ![forks](https://img.shields.io/github/forks/febinrev/atril_cbt-inject-exploit.svg)

## CVE-2023-51518
 Apache James prior to version 3.7.5 and 3.8.0 exposes a JMX endpoint on localhost subject to pre-authentication deserialisation of untrusted data.
Given a deserialisation gadjet, this could be leveraged as part of an exploit chain that could result in privilege escalation.
Note that by default JMX endpoint is only bound locally.

We recommend users to:
 - Upgrade to a non-vulnerable Apache James version

 - Run Apache James isolated from other processes (docker - dedicated virtual machine)
 - If possible turn off JMX





- [https://github.com/mbadanoiu/CVE-2023-51518](https://github.com/mbadanoiu/CVE-2023-51518) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2023-51518.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2023-51518.svg)

## CVE-2023-51504
 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Dan Dulaney Dan's Embedder for Google Calendar allows Stored XSS.This issue affects Dan's Embedder for Google Calendar: from n/a through 1.2.





- [https://github.com/Sybelle03/CVE-2023-51504](https://github.com/Sybelle03/CVE-2023-51504) :  ![starts](https://img.shields.io/github/stars/Sybelle03/CVE-2023-51504.svg) ![forks](https://img.shields.io/github/forks/Sybelle03/CVE-2023-51504.svg)

## CVE-2023-51467
 The vulnerability permits attackers to circumvent authentication processes, enabling them to remotely execute arbitrary code





- [https://github.com/gobysec/GobyVuls](https://github.com/gobysec/GobyVuls) :  ![starts](https://img.shields.io/github/stars/gobysec/GobyVuls.svg) ![forks](https://img.shields.io/github/forks/gobysec/GobyVuls.svg)

- [https://github.com/jakabakos/Apache-OFBiz-Authentication-Bypass](https://github.com/jakabakos/Apache-OFBiz-Authentication-Bypass) :  ![starts](https://img.shields.io/github/stars/jakabakos/Apache-OFBiz-Authentication-Bypass.svg) ![forks](https://img.shields.io/github/forks/jakabakos/Apache-OFBiz-Authentication-Bypass.svg)

- [https://github.com/ImuSpirit/CVE-2023-51467-Exploit](https://github.com/ImuSpirit/CVE-2023-51467-Exploit) :  ![starts](https://img.shields.io/github/stars/ImuSpirit/CVE-2023-51467-Exploit.svg) ![forks](https://img.shields.io/github/forks/ImuSpirit/CVE-2023-51467-Exploit.svg)

- [https://github.com/D0g3-8Bit/OFBiz-Attack](https://github.com/D0g3-8Bit/OFBiz-Attack) :  ![starts](https://img.shields.io/github/stars/D0g3-8Bit/OFBiz-Attack.svg) ![forks](https://img.shields.io/github/forks/D0g3-8Bit/OFBiz-Attack.svg)

- [https://github.com/Chocapikk/CVE-2023-51467](https://github.com/Chocapikk/CVE-2023-51467) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-51467.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-51467.svg)

- [https://github.com/K3ysTr0K3R/CVE-2023-51467-EXPLOIT](https://github.com/K3ysTr0K3R/CVE-2023-51467-EXPLOIT) :  ![starts](https://img.shields.io/github/stars/K3ysTr0K3R/CVE-2023-51467-EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/K3ysTr0K3R/CVE-2023-51467-EXPLOIT.svg)

- [https://github.com/vulncheck-oss/cve-2023-51467](https://github.com/vulncheck-oss/cve-2023-51467) :  ![starts](https://img.shields.io/github/stars/vulncheck-oss/cve-2023-51467.svg) ![forks](https://img.shields.io/github/forks/vulncheck-oss/cve-2023-51467.svg)

- [https://github.com/UserConnecting/Exploit-CVE-2023-49070-and-CVE-2023-51467-Apache-OFBiz](https://github.com/UserConnecting/Exploit-CVE-2023-49070-and-CVE-2023-51467-Apache-OFBiz) :  ![starts](https://img.shields.io/github/stars/UserConnecting/Exploit-CVE-2023-49070-and-CVE-2023-51467-Apache-OFBiz.svg) ![forks](https://img.shields.io/github/forks/UserConnecting/Exploit-CVE-2023-49070-and-CVE-2023-51467-Apache-OFBiz.svg)

- [https://github.com/ImuSpirit/CVE-2023-51467](https://github.com/ImuSpirit/CVE-2023-51467) :  ![starts](https://img.shields.io/github/stars/ImuSpirit/CVE-2023-51467.svg) ![forks](https://img.shields.io/github/forks/ImuSpirit/CVE-2023-51467.svg)

- [https://github.com/yukselberkay/CVE-2023-49070_CVE-2023-51467](https://github.com/yukselberkay/CVE-2023-49070_CVE-2023-51467) :  ![starts](https://img.shields.io/github/stars/yukselberkay/CVE-2023-49070_CVE-2023-51467.svg) ![forks](https://img.shields.io/github/forks/yukselberkay/CVE-2023-49070_CVE-2023-51467.svg)

- [https://github.com/Subha-BOO7/Exploit_CVE-2023-51467](https://github.com/Subha-BOO7/Exploit_CVE-2023-51467) :  ![starts](https://img.shields.io/github/stars/Subha-BOO7/Exploit_CVE-2023-51467.svg) ![forks](https://img.shields.io/github/forks/Subha-BOO7/Exploit_CVE-2023-51467.svg)

- [https://github.com/jakeotte/BadBizness-CVE-2023-51467](https://github.com/jakeotte/BadBizness-CVE-2023-51467) :  ![starts](https://img.shields.io/github/stars/jakeotte/BadBizness-CVE-2023-51467.svg) ![forks](https://img.shields.io/github/forks/jakeotte/BadBizness-CVE-2023-51467.svg)

- [https://github.com/Praison001/Apache-OFBiz-Auth-Bypass-and-RCE-Exploit-CVE-2023-49070-CVE-2023-51467](https://github.com/Praison001/Apache-OFBiz-Auth-Bypass-and-RCE-Exploit-CVE-2023-49070-CVE-2023-51467) :  ![starts](https://img.shields.io/github/stars/Praison001/Apache-OFBiz-Auth-Bypass-and-RCE-Exploit-CVE-2023-49070-CVE-2023-51467.svg) ![forks](https://img.shields.io/github/forks/Praison001/Apache-OFBiz-Auth-Bypass-and-RCE-Exploit-CVE-2023-49070-CVE-2023-51467.svg)

## CVE-2023-51448
 Cacti provides an operational monitoring and fault management framework. Version 1.2.25 has a Blind SQL Injection (SQLi) vulnerability within the SNMP Notification Receivers feature in the file `‘managers.php’`. An authenticated attacker with the “Settings/Utilities” permission can send a crafted HTTP GET request to the endpoint `‘/cacti/managers.php’` with an SQLi payload in the `‘selected_graphs_array’` HTTP GET parameter. As of time of publication, no patched versions exist.



- [https://github.com/jakabakos/CVE-2023-51448-cacti-sqli-poc](https://github.com/jakabakos/CVE-2023-51448-cacti-sqli-poc) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2023-51448-cacti-sqli-poc.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2023-51448-cacti-sqli-poc.svg)

## CVE-2023-51409
 Unrestricted Upload of File with Dangerous Type vulnerability in Jordy Meow AI Engine: ChatGPT Chatbot.This issue affects AI Engine: ChatGPT Chatbot: from n/a through 1.9.98.





- [https://github.com/RandomRobbieBF/CVE-2023-51409](https://github.com/RandomRobbieBF/CVE-2023-51409) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-51409.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-51409.svg)

- [https://github.com/Nxploited/CVE-2023-51409](https://github.com/Nxploited/CVE-2023-51409) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2023-51409.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2023-51409.svg)

## CVE-2023-51385
 In ssh in OpenSSH before 9.6, OS command injection might occur if a user name or host name has shell metacharacters, and this name is referenced by an expansion token in certain situations. For example, an untrusted Git repository can have a submodule with shell metacharacters in a user name or host name.



- [https://github.com/vin01/poc-proxycommand-vulnerable](https://github.com/vin01/poc-proxycommand-vulnerable) :  ![starts](https://img.shields.io/github/stars/vin01/poc-proxycommand-vulnerable.svg) ![forks](https://img.shields.io/github/forks/vin01/poc-proxycommand-vulnerable.svg)

- [https://github.com/LtmThink/CVE-2023-51385_test](https://github.com/LtmThink/CVE-2023-51385_test) :  ![starts](https://img.shields.io/github/stars/LtmThink/CVE-2023-51385_test.svg) ![forks](https://img.shields.io/github/forks/LtmThink/CVE-2023-51385_test.svg)

- [https://github.com/Le1a/CVE-2023-51385](https://github.com/Le1a/CVE-2023-51385) :  ![starts](https://img.shields.io/github/stars/Le1a/CVE-2023-51385.svg) ![forks](https://img.shields.io/github/forks/Le1a/CVE-2023-51385.svg)

- [https://github.com/WOOOOONG/CVE-2023-51385](https://github.com/WOOOOONG/CVE-2023-51385) :  ![starts](https://img.shields.io/github/stars/WOOOOONG/CVE-2023-51385.svg) ![forks](https://img.shields.io/github/forks/WOOOOONG/CVE-2023-51385.svg)

- [https://github.com/farliy-hacker/CVE-2023-51385](https://github.com/farliy-hacker/CVE-2023-51385) :  ![starts](https://img.shields.io/github/stars/farliy-hacker/CVE-2023-51385.svg) ![forks](https://img.shields.io/github/forks/farliy-hacker/CVE-2023-51385.svg)

- [https://github.com/thinkliving2020/CVE-2023-51385-](https://github.com/thinkliving2020/CVE-2023-51385-) :  ![starts](https://img.shields.io/github/stars/thinkliving2020/CVE-2023-51385-.svg) ![forks](https://img.shields.io/github/forks/thinkliving2020/CVE-2023-51385-.svg)

- [https://github.com/farliy-hacker/CVE-2023-51385-save](https://github.com/farliy-hacker/CVE-2023-51385-save) :  ![starts](https://img.shields.io/github/stars/farliy-hacker/CVE-2023-51385-save.svg) ![forks](https://img.shields.io/github/forks/farliy-hacker/CVE-2023-51385-save.svg)

- [https://github.com/2048JiaLi/CVE-2023-51385](https://github.com/2048JiaLi/CVE-2023-51385) :  ![starts](https://img.shields.io/github/stars/2048JiaLi/CVE-2023-51385.svg) ![forks](https://img.shields.io/github/forks/2048JiaLi/CVE-2023-51385.svg)

- [https://github.com/Sonicrrrr/CVE-2023-51385](https://github.com/Sonicrrrr/CVE-2023-51385) :  ![starts](https://img.shields.io/github/stars/Sonicrrrr/CVE-2023-51385.svg) ![forks](https://img.shields.io/github/forks/Sonicrrrr/CVE-2023-51385.svg)

- [https://github.com/julienbrs/exploit-CVE-2023-51385](https://github.com/julienbrs/exploit-CVE-2023-51385) :  ![starts](https://img.shields.io/github/stars/julienbrs/exploit-CVE-2023-51385.svg) ![forks](https://img.shields.io/github/forks/julienbrs/exploit-CVE-2023-51385.svg)

- [https://github.com/FeatherStark/CVE-2023-51385](https://github.com/FeatherStark/CVE-2023-51385) :  ![starts](https://img.shields.io/github/stars/FeatherStark/CVE-2023-51385.svg) ![forks](https://img.shields.io/github/forks/FeatherStark/CVE-2023-51385.svg)

- [https://github.com/uccu99/CVE-2023-51385](https://github.com/uccu99/CVE-2023-51385) :  ![starts](https://img.shields.io/github/stars/uccu99/CVE-2023-51385.svg) ![forks](https://img.shields.io/github/forks/uccu99/CVE-2023-51385.svg)

- [https://github.com/endasugrue/CVE-2023-51385_poc](https://github.com/endasugrue/CVE-2023-51385_poc) :  ![starts](https://img.shields.io/github/stars/endasugrue/CVE-2023-51385_poc.svg) ![forks](https://img.shields.io/github/forks/endasugrue/CVE-2023-51385_poc.svg)

- [https://github.com/c0deur/CVE-2023-51385](https://github.com/c0deur/CVE-2023-51385) :  ![starts](https://img.shields.io/github/stars/c0deur/CVE-2023-51385.svg) ![forks](https://img.shields.io/github/forks/c0deur/CVE-2023-51385.svg)

- [https://github.com/runooovb/CVE-2023-51385test](https://github.com/runooovb/CVE-2023-51385test) :  ![starts](https://img.shields.io/github/stars/runooovb/CVE-2023-51385test.svg) ![forks](https://img.shields.io/github/forks/runooovb/CVE-2023-51385test.svg)

- [https://github.com/watarium/poc-cve-2023-51385](https://github.com/watarium/poc-cve-2023-51385) :  ![starts](https://img.shields.io/github/stars/watarium/poc-cve-2023-51385.svg) ![forks](https://img.shields.io/github/forks/watarium/poc-cve-2023-51385.svg)

- [https://github.com/GroundCTL2MajorTom/CVE-2023-51385POC](https://github.com/GroundCTL2MajorTom/CVE-2023-51385POC) :  ![starts](https://img.shields.io/github/stars/GroundCTL2MajorTom/CVE-2023-51385POC.svg) ![forks](https://img.shields.io/github/forks/GroundCTL2MajorTom/CVE-2023-51385POC.svg)

- [https://github.com/MiningBot-eth/CVE-2023-51385-exploit](https://github.com/MiningBot-eth/CVE-2023-51385-exploit) :  ![starts](https://img.shields.io/github/stars/MiningBot-eth/CVE-2023-51385-exploit.svg) ![forks](https://img.shields.io/github/forks/MiningBot-eth/CVE-2023-51385-exploit.svg)

- [https://github.com/power1314520/CVE-2023-51385_test](https://github.com/power1314520/CVE-2023-51385_test) :  ![starts](https://img.shields.io/github/stars/power1314520/CVE-2023-51385_test.svg) ![forks](https://img.shields.io/github/forks/power1314520/CVE-2023-51385_test.svg)

- [https://github.com/GroundCTL2MajorTom/CVE-2023-51385P-POC](https://github.com/GroundCTL2MajorTom/CVE-2023-51385P-POC) :  ![starts](https://img.shields.io/github/stars/GroundCTL2MajorTom/CVE-2023-51385P-POC.svg) ![forks](https://img.shields.io/github/forks/GroundCTL2MajorTom/CVE-2023-51385P-POC.svg)

- [https://github.com/WLaoDuo/CVE-2023-51385_poc-test](https://github.com/WLaoDuo/CVE-2023-51385_poc-test) :  ![starts](https://img.shields.io/github/stars/WLaoDuo/CVE-2023-51385_poc-test.svg) ![forks](https://img.shields.io/github/forks/WLaoDuo/CVE-2023-51385_poc-test.svg)

- [https://github.com/julienbrs/malicious-exploit-CVE-2023-51385](https://github.com/julienbrs/malicious-exploit-CVE-2023-51385) :  ![starts](https://img.shields.io/github/stars/julienbrs/malicious-exploit-CVE-2023-51385.svg) ![forks](https://img.shields.io/github/forks/julienbrs/malicious-exploit-CVE-2023-51385.svg)

- [https://github.com/saarcastified/CVE-2023-51385---OpenSSH-ProxyCommand-Injection-PoC](https://github.com/saarcastified/CVE-2023-51385---OpenSSH-ProxyCommand-Injection-PoC) :  ![starts](https://img.shields.io/github/stars/saarcastified/CVE-2023-51385---OpenSSH-ProxyCommand-Injection-PoC.svg) ![forks](https://img.shields.io/github/forks/saarcastified/CVE-2023-51385---OpenSSH-ProxyCommand-Injection-PoC.svg)

## CVE-2023-51281
 Cross Site Scripting vulnerability in Customer Support System v.1.0 allows a remote attacker to escalate privileges via a crafted script firstname, "lastname", "middlename", "contact" and address parameters.



- [https://github.com/geraldoalcantara/CVE-2023-51281](https://github.com/geraldoalcantara/CVE-2023-51281) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-51281.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-51281.svg)

## CVE-2023-51214
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/chandraprarikraj/CVE-2023-51214](https://github.com/chandraprarikraj/CVE-2023-51214) :  ![starts](https://img.shields.io/github/stars/chandraprarikraj/CVE-2023-51214.svg) ![forks](https://img.shields.io/github/forks/chandraprarikraj/CVE-2023-51214.svg)

## CVE-2023-51127
 FLIR AX8 thermal sensor cameras up to and including 1.46.16 are vulnerable to Directory Traversal due to improper access restriction. This vulnerability allows an unauthenticated, remote attacker to obtain arbitrary sensitive file contents by uploading a specially crafted symbolic link file.



- [https://github.com/risuxx/CVE-2023-51127](https://github.com/risuxx/CVE-2023-51127) :  ![starts](https://img.shields.io/github/stars/risuxx/CVE-2023-51127.svg) ![forks](https://img.shields.io/github/forks/risuxx/CVE-2023-51127.svg)

## CVE-2023-51126
 Command injection vulnerability in /usr/www/res.php in FLIR AX8 up to 1.46.16 allows attackers to run arbitrary commands via the value parameter.



- [https://github.com/risuxx/CVE-2023-51126](https://github.com/risuxx/CVE-2023-51126) :  ![starts](https://img.shields.io/github/stars/risuxx/CVE-2023-51126.svg) ![forks](https://img.shields.io/github/forks/risuxx/CVE-2023-51126.svg)

## CVE-2023-51119
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/OscarAkaElvis/CVE-2023-51119](https://github.com/OscarAkaElvis/CVE-2023-51119) :  ![starts](https://img.shields.io/github/stars/OscarAkaElvis/CVE-2023-51119.svg) ![forks](https://img.shields.io/github/forks/OscarAkaElvis/CVE-2023-51119.svg)

## CVE-2023-51073
 An issue in Buffalo LS210D v.1.78-0.03 allows a remote attacker to execute arbitrary code via the Firmware Update Script at /etc/init.d/update_notifications.sh.



- [https://github.com/christopher-pace/CVE-2023-51073](https://github.com/christopher-pace/CVE-2023-51073) :  ![starts](https://img.shields.io/github/stars/christopher-pace/CVE-2023-51073.svg) ![forks](https://img.shields.io/github/forks/christopher-pace/CVE-2023-51073.svg)

## CVE-2023-51000
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Team-Byerus/CVE-2023-51000](https://github.com/Team-Byerus/CVE-2023-51000) :  ![starts](https://img.shields.io/github/stars/Team-Byerus/CVE-2023-51000.svg) ![forks](https://img.shields.io/github/forks/Team-Byerus/CVE-2023-51000.svg)

## CVE-2023-50917
 MajorDoMo (aka Major Domestic Module) before 0662e5e allows command execution via thumb.php shell metacharacters. NOTE: this is unrelated to the Majordomo mailing-list manager.



- [https://github.com/Chocapikk/CVE-2023-50917](https://github.com/Chocapikk/CVE-2023-50917) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-50917.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-50917.svg)

## CVE-2023-50868
 The Closest Encloser Proof aspect of the DNS protocol (in RFC 5155 when RFC 9276 guidance is skipped) allows remote attackers to cause a denial of service (CPU consumption for SHA-1 computations) via DNSSEC responses in a random subdomain attack, aka the "NSEC3" issue. The RFC 5155 specification implies that an algorithm must perform thousands of iterations of a hash function in certain situations.



- [https://github.com/Goethe-Universitat-Cybersecurity/NSEC3-Encloser-Attack](https://github.com/Goethe-Universitat-Cybersecurity/NSEC3-Encloser-Attack) :  ![starts](https://img.shields.io/github/stars/Goethe-Universitat-Cybersecurity/NSEC3-Encloser-Attack.svg) ![forks](https://img.shields.io/github/forks/Goethe-Universitat-Cybersecurity/NSEC3-Encloser-Attack.svg)

## CVE-2023-50780
 Apache ActiveMQ Artemis allows access to diagnostic information and controls through MBeans, which are also exposed through the authenticated Jolokia endpoint. Before version 2.29.0, this also included the Log4J2 MBean. This MBean is not meant for exposure to non-administrative users. This could eventually allow an authenticated attacker to write arbitrary files to the filesystem and indirectly achieve RCE.


Users are recommended to upgrade to version 2.29.0 or later, which fixes the issue.



- [https://github.com/mbadanoiu/CVE-2023-50780](https://github.com/mbadanoiu/CVE-2023-50780) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2023-50780.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2023-50780.svg)

## CVE-2023-50685
 An issue in Hipcam Cameras RealServer v.1.0 allows a remote attacker to cause a denial of service via a crafted script to the client_port parameter.



- [https://github.com/MaximilianJungblut/Hipcam-RTSP-Format-Validation-Vulnerability](https://github.com/MaximilianJungblut/Hipcam-RTSP-Format-Validation-Vulnerability) :  ![starts](https://img.shields.io/github/stars/MaximilianJungblut/Hipcam-RTSP-Format-Validation-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/MaximilianJungblut/Hipcam-RTSP-Format-Validation-Vulnerability.svg)

## CVE-2023-50643
 An issue in Evernote Evernote for MacOS v.10.68.2 allows a remote attacker to execute arbitrary code via the RunAsNode and enableNodeClilnspectArguments components.



- [https://github.com/giovannipajeu1/CVE-2023-50643](https://github.com/giovannipajeu1/CVE-2023-50643) :  ![starts](https://img.shields.io/github/stars/giovannipajeu1/CVE-2023-50643.svg) ![forks](https://img.shields.io/github/forks/giovannipajeu1/CVE-2023-50643.svg)

## CVE-2023-50596
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/chandraprarikraj/CVE-2023-50596](https://github.com/chandraprarikraj/CVE-2023-50596) :  ![starts](https://img.shields.io/github/stars/chandraprarikraj/CVE-2023-50596.svg) ![forks](https://img.shields.io/github/forks/chandraprarikraj/CVE-2023-50596.svg)

## CVE-2023-50564
 An arbitrary file upload vulnerability in the component /inc/modules_install.php of Pluck-CMS v4.7.18 allows attackers to execute arbitrary code via uploading a crafted ZIP file.



- [https://github.com/Rai2en/CVE-2023-50564_Pluck-v4.7.18_PoC](https://github.com/Rai2en/CVE-2023-50564_Pluck-v4.7.18_PoC) :  ![starts](https://img.shields.io/github/stars/Rai2en/CVE-2023-50564_Pluck-v4.7.18_PoC.svg) ![forks](https://img.shields.io/github/forks/Rai2en/CVE-2023-50564_Pluck-v4.7.18_PoC.svg)

- [https://github.com/xpltive/CVE-2023-50564](https://github.com/xpltive/CVE-2023-50564) :  ![starts](https://img.shields.io/github/stars/xpltive/CVE-2023-50564.svg) ![forks](https://img.shields.io/github/forks/xpltive/CVE-2023-50564.svg)

- [https://github.com/ipuig/CVE-2023-50564](https://github.com/ipuig/CVE-2023-50564) :  ![starts](https://img.shields.io/github/stars/ipuig/CVE-2023-50564.svg) ![forks](https://img.shields.io/github/forks/ipuig/CVE-2023-50564.svg)

- [https://github.com/glynzr/CVE-2023-50564](https://github.com/glynzr/CVE-2023-50564) :  ![starts](https://img.shields.io/github/stars/glynzr/CVE-2023-50564.svg) ![forks](https://img.shields.io/github/forks/glynzr/CVE-2023-50564.svg)

## CVE-2023-50465
 A stored cross-site scripting (XSS) vulnerability exists in Monica (aka MonicaHQ) 4.0.0 via an SVG document uploaded by an authenticated user.



- [https://github.com/Ev3rR3d/CVE-2023-50465](https://github.com/Ev3rR3d/CVE-2023-50465) :  ![starts](https://img.shields.io/github/stars/Ev3rR3d/CVE-2023-50465.svg) ![forks](https://img.shields.io/github/forks/Ev3rR3d/CVE-2023-50465.svg)

## CVE-2023-50387
 Certain DNSSEC aspects of the DNS protocol (in RFC 4033, 4034, 4035, 6840, and related RFCs) allow remote attackers to cause a denial of service (CPU consumption) via one or more DNSSEC responses, aka the "KeyTrap" issue. One of the concerns is that, when there is a zone with many DNSKEY and RRSIG records, the protocol specification implies that an algorithm must evaluate all combinations of DNSKEY and RRSIG records.



- [https://github.com/knqyf263/CVE-2023-50387](https://github.com/knqyf263/CVE-2023-50387) :  ![starts](https://img.shields.io/github/stars/knqyf263/CVE-2023-50387.svg) ![forks](https://img.shields.io/github/forks/knqyf263/CVE-2023-50387.svg)

- [https://github.com/Pablodiz/CVE-2023-50387](https://github.com/Pablodiz/CVE-2023-50387) :  ![starts](https://img.shields.io/github/stars/Pablodiz/CVE-2023-50387.svg) ![forks](https://img.shields.io/github/forks/Pablodiz/CVE-2023-50387.svg)

- [https://github.com/Meirelez/SSR-DNSSEC](https://github.com/Meirelez/SSR-DNSSEC) :  ![starts](https://img.shields.io/github/stars/Meirelez/SSR-DNSSEC.svg) ![forks](https://img.shields.io/github/forks/Meirelez/SSR-DNSSEC.svg)

## CVE-2023-50386
 Improper Control of Dynamically-Managed Code Resources, Unrestricted Upload of File with Dangerous Type, Inclusion of Functionality from Untrusted Control Sphere vulnerability in Apache Solr.This issue affects Apache Solr: from 6.0.0 through 8.11.2, from 9.0.0 before 9.4.1.

In the affected versions, Solr ConfigSets accepted Java jar and class files to be uploaded through the ConfigSets API.
When backing up Solr Collections, these configSet files would be saved to disk when using the LocalFileSystemRepository (the default for backups).
If the backup was saved to a directory that Solr uses in its ClassPath/ClassLoaders, then the jar and class files would be available to use with any ConfigSet, trusted or untrusted.

When Solr is run in a secure way (Authorization enabled), as is strongly suggested, this vulnerability is limited to extending the Backup permissions with the ability to add libraries.
Users are recommended to upgrade to version 8.11.3 or 9.4.1, which fix the issue.
In these versions, the following protections have been added:

  *  Users are no longer able to upload files to a configSet that could be executed via a Java ClassLoader.
  *  The Backup API restricts saving backups to directories that are used in the ClassLoader.



- [https://github.com/vvmdx/Apache-Solr-RCE_CVE-2023-50386_POC](https://github.com/vvmdx/Apache-Solr-RCE_CVE-2023-50386_POC) :  ![starts](https://img.shields.io/github/stars/vvmdx/Apache-Solr-RCE_CVE-2023-50386_POC.svg) ![forks](https://img.shields.io/github/forks/vvmdx/Apache-Solr-RCE_CVE-2023-50386_POC.svg)

## CVE-2023-50257
 eProsima Fast DDS (formerly Fast RTPS) is a C++ implementation of the Data Distribution Service standard of the Object Management Group. Even with the application of SROS2, due to the issue where the data (`p[UD]`) and `guid` values used to disconnect between nodes are not encrypted, a vulnerability has been discovered where a malicious attacker can forcibly disconnect a Subscriber and can deny a Subscriber attempting to connect. Afterwards, if the attacker sends the packet for disconnecting, which is data (`p[UD]`), to the Global Data Space (`239.255.0.1:7400`) using the said Publisher ID, all the Subscribers (Listeners) connected to the Publisher (Talker) will not receive any data and their connection will be disconnected. Moreover, if this disconnection packet is sent continuously, the Subscribers (Listeners) trying to connect will not be able to do so. Since the initial commit of the `SecurityManager.cpp` code (`init`, `on_process_handshake`) on Nov 8, 2016, the Disconnect Vulnerability in RTPS Packets Used by SROS2 has been present prior to versions 2.13.0, 2.12.2, 2.11.3, 2.10.3, and 2.6.7.



- [https://github.com/Jminis/CVE-2023-50257](https://github.com/Jminis/CVE-2023-50257) :  ![starts](https://img.shields.io/github/stars/Jminis/CVE-2023-50257.svg) ![forks](https://img.shields.io/github/forks/Jminis/CVE-2023-50257.svg)

## CVE-2023-50254
 Deepin Linux's default document reader `deepin-reader` software suffers from a serious vulnerability in versions prior to 6.0.7 due to a design flaw that leads to remote command execution via crafted docx document. This is a file overwrite vulnerability. Remote code execution (RCE) can be achieved by overwriting files like .bash_rc, .bash_login, etc. RCE will be triggered when the user opens the terminal. Version 6.0.7 contains a patch for the issue.



- [https://github.com/febinrev/deepin-linux_reader_RCE-exploit](https://github.com/febinrev/deepin-linux_reader_RCE-exploit) :  ![starts](https://img.shields.io/github/stars/febinrev/deepin-linux_reader_RCE-exploit.svg) ![forks](https://img.shields.io/github/forks/febinrev/deepin-linux_reader_RCE-exploit.svg)

## CVE-2023-50226
 Parallels Desktop Updater Link Following Local Privilege Escalation Vulnerability. This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability.

The specific flaw exists within the Updater service. By creating a symbolic link, an attacker can abuse the service to move arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.
. Was ZDI-CAN-21227.



- [https://github.com/kn32/parallels-file-move-privesc](https://github.com/kn32/parallels-file-move-privesc) :  ![starts](https://img.shields.io/github/stars/kn32/parallels-file-move-privesc.svg) ![forks](https://img.shields.io/github/forks/kn32/parallels-file-move-privesc.svg)

## CVE-2023-50164
 An attacker can manipulate file upload params to enable paths traversal and under some circumstances this can lead to uploading a malicious file which can be used to perform Remote Code Execution.
Users are recommended to upgrade to versions Struts 2.5.33 or Struts 6.3.0.2 or greater to fix this issue.



- [https://github.com/jakabakos/CVE-2023-50164-Apache-Struts-RCE](https://github.com/jakabakos/CVE-2023-50164-Apache-Struts-RCE) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2023-50164-Apache-Struts-RCE.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2023-50164-Apache-Struts-RCE.svg)

- [https://github.com/dwisiswant0/cve-2023-50164-poc](https://github.com/dwisiswant0/cve-2023-50164-poc) :  ![starts](https://img.shields.io/github/stars/dwisiswant0/cve-2023-50164-poc.svg) ![forks](https://img.shields.io/github/forks/dwisiswant0/cve-2023-50164-poc.svg)

- [https://github.com/Trackflaw/CVE-2023-50164-ApacheStruts2-Docker](https://github.com/Trackflaw/CVE-2023-50164-ApacheStruts2-Docker) :  ![starts](https://img.shields.io/github/stars/Trackflaw/CVE-2023-50164-ApacheStruts2-Docker.svg) ![forks](https://img.shields.io/github/forks/Trackflaw/CVE-2023-50164-ApacheStruts2-Docker.svg)

- [https://github.com/snyk-labs/CVE-2023-50164-POC](https://github.com/snyk-labs/CVE-2023-50164-POC) :  ![starts](https://img.shields.io/github/stars/snyk-labs/CVE-2023-50164-POC.svg) ![forks](https://img.shields.io/github/forks/snyk-labs/CVE-2023-50164-POC.svg)

- [https://github.com/bcdannyboy/CVE-2023-50164](https://github.com/bcdannyboy/CVE-2023-50164) :  ![starts](https://img.shields.io/github/stars/bcdannyboy/CVE-2023-50164.svg) ![forks](https://img.shields.io/github/forks/bcdannyboy/CVE-2023-50164.svg)

- [https://github.com/Trackflaw/CVE-2024-10924-Wordpress-Docker](https://github.com/Trackflaw/CVE-2024-10924-Wordpress-Docker) :  ![starts](https://img.shields.io/github/stars/Trackflaw/CVE-2024-10924-Wordpress-Docker.svg) ![forks](https://img.shields.io/github/forks/Trackflaw/CVE-2024-10924-Wordpress-Docker.svg)

- [https://github.com/sunnyvale-it/CVE-2023-50164-PoC](https://github.com/sunnyvale-it/CVE-2023-50164-PoC) :  ![starts](https://img.shields.io/github/stars/sunnyvale-it/CVE-2023-50164-PoC.svg) ![forks](https://img.shields.io/github/forks/sunnyvale-it/CVE-2023-50164-PoC.svg)

- [https://github.com/aaronm-sysdig/cve-2023-50164](https://github.com/aaronm-sysdig/cve-2023-50164) :  ![starts](https://img.shields.io/github/stars/aaronm-sysdig/cve-2023-50164.svg) ![forks](https://img.shields.io/github/forks/aaronm-sysdig/cve-2023-50164.svg)

- [https://github.com/helsecert/cve-2023-50164](https://github.com/helsecert/cve-2023-50164) :  ![starts](https://img.shields.io/github/stars/helsecert/cve-2023-50164.svg) ![forks](https://img.shields.io/github/forks/helsecert/cve-2023-50164.svg)

- [https://github.com/Thirukrishnan/CVE-2023-50164-Apache-Struts-RCE](https://github.com/Thirukrishnan/CVE-2023-50164-Apache-Struts-RCE) :  ![starts](https://img.shields.io/github/stars/Thirukrishnan/CVE-2023-50164-Apache-Struts-RCE.svg) ![forks](https://img.shields.io/github/forks/Thirukrishnan/CVE-2023-50164-Apache-Struts-RCE.svg)

- [https://github.com/minhbao15677/CVE-2023-50164](https://github.com/minhbao15677/CVE-2023-50164) :  ![starts](https://img.shields.io/github/stars/minhbao15677/CVE-2023-50164.svg) ![forks](https://img.shields.io/github/forks/minhbao15677/CVE-2023-50164.svg)

- [https://github.com/miles3719/cve-2023-50164](https://github.com/miles3719/cve-2023-50164) :  ![starts](https://img.shields.io/github/stars/miles3719/cve-2023-50164.svg) ![forks](https://img.shields.io/github/forks/miles3719/cve-2023-50164.svg)

- [https://github.com/AsfandAliMemon25/CVE-2023-50164Analysis-](https://github.com/AsfandAliMemon25/CVE-2023-50164Analysis-) :  ![starts](https://img.shields.io/github/stars/AsfandAliMemon25/CVE-2023-50164Analysis-.svg) ![forks](https://img.shields.io/github/forks/AsfandAliMemon25/CVE-2023-50164Analysis-.svg)

## CVE-2023-50132
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/sajaljat/CVE-2023-50132](https://github.com/sajaljat/CVE-2023-50132) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2023-50132.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2023-50132.svg)

## CVE-2023-50131
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/sajaljat/CVE-2023-50131](https://github.com/sajaljat/CVE-2023-50131) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2023-50131.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2023-50131.svg)

## CVE-2023-50094
 reNgine before 2.1.2 allows OS Command Injection if an adversary has a valid session ID. The attack places shell metacharacters in an api/tools/waf_detector/?url= string. The commands are executed as root via subprocess.check_output.



- [https://github.com/Zierax/CVE-2023-50094_POC](https://github.com/Zierax/CVE-2023-50094_POC) :  ![starts](https://img.shields.io/github/stars/Zierax/CVE-2023-50094_POC.svg) ![forks](https://img.shields.io/github/forks/Zierax/CVE-2023-50094_POC.svg)

## CVE-2023-50072
 A Stored Cross-Site Scripting (XSS) vulnerability exists in OpenKM version 7.1.40 (dbb6e88) With Professional Extension that allows an authenticated user to upload a note on a file which acts as a stored XSS payload. Any user who opens the note of a document file will trigger the XSS.



- [https://github.com/ahrixia/CVE-2023-50072](https://github.com/ahrixia/CVE-2023-50072) :  ![starts](https://img.shields.io/github/stars/ahrixia/CVE-2023-50072.svg) ![forks](https://img.shields.io/github/forks/ahrixia/CVE-2023-50072.svg)

## CVE-2023-50071
 Sourcecodester Customer Support System 1.0 has multiple SQL injection vulnerabilities in /customer_support/ajax.php?action=save_department via id or name.



- [https://github.com/geraldoalcantara/CVE-2023-50071](https://github.com/geraldoalcantara/CVE-2023-50071) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-50071.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-50071.svg)

## CVE-2023-50070
 Sourcecodester Customer Support System 1.0 has multiple SQL injection vulnerabilities in /customer_support/ajax.php?action=save_ticket via department_id, customer_id, and subject.



- [https://github.com/geraldoalcantara/CVE-2023-50070](https://github.com/geraldoalcantara/CVE-2023-50070) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-50070.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-50070.svg)

## CVE-2023-50029
 PHP Injection vulnerability in the module "M4 PDF Extensions" (m4pdf) up to version 3.3.2 from PrestaAddons for PrestaShop allows attackers to run arbitrary code via the M4PDF::saveTemplate() method.



- [https://github.com/absholi7ly/PHP-Injection-in-M4-PDF-Extensions](https://github.com/absholi7ly/PHP-Injection-in-M4-PDF-Extensions) :  ![starts](https://img.shields.io/github/stars/absholi7ly/PHP-Injection-in-M4-PDF-Extensions.svg) ![forks](https://img.shields.io/github/forks/absholi7ly/PHP-Injection-in-M4-PDF-Extensions.svg)

## CVE-2023-49989
 Hotel Booking Management v1.0 was discovered to contain a SQL injection vulnerability via the id parameter at update.php.



- [https://github.com/geraldoalcantara/CVE-2023-49989](https://github.com/geraldoalcantara/CVE-2023-49989) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49989.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49989.svg)

## CVE-2023-49988
 Hotel Booking Management v1.0 was discovered to contain a SQL injection vulnerability via the npss parameter at rooms.php.



- [https://github.com/geraldoalcantara/CVE-2023-49988](https://github.com/geraldoalcantara/CVE-2023-49988) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49988.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49988.svg)

## CVE-2023-49987
 A cross-site scripting (XSS) vulnerability in the component /management/term of School Fees Management System v1.0 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the tname parameter.



- [https://github.com/geraldoalcantara/CVE-2023-49987](https://github.com/geraldoalcantara/CVE-2023-49987) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49987.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49987.svg)

## CVE-2023-49986
 A cross-site scripting (XSS) vulnerability in the component /admin/parent of School Fees Management System 1.0 allow attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the name parameter.



- [https://github.com/geraldoalcantara/CVE-2023-49986](https://github.com/geraldoalcantara/CVE-2023-49986) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49986.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49986.svg)

## CVE-2023-49985
 A cross-site scripting (XSS) vulnerability in the component /management/class of School Fees Management System v1.0 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the cname parameter.



- [https://github.com/geraldoalcantara/CVE-2023-49985](https://github.com/geraldoalcantara/CVE-2023-49985) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49985.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49985.svg)

## CVE-2023-49984
 A cross-site scripting (XSS) vulnerability in the component /management/settings of School Fees Management System v1.0 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the name parameter.



- [https://github.com/geraldoalcantara/CVE-2023-49984](https://github.com/geraldoalcantara/CVE-2023-49984) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49984.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49984.svg)

## CVE-2023-49983
 A cross-site scripting (XSS) vulnerability in the component /management/class of School Fees Management System v1.0 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the name parameter.



- [https://github.com/geraldoalcantara/CVE-2023-49983](https://github.com/geraldoalcantara/CVE-2023-49983) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49983.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49983.svg)

## CVE-2023-49982
 Broken access control in the component /admin/management/users of School Fees Management System v1.0 allows attackers to escalate privileges and perform Administrative actions, including adding and deleting user accounts.



- [https://github.com/geraldoalcantara/CVE-2023-49982](https://github.com/geraldoalcantara/CVE-2023-49982) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49982.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49982.svg)

## CVE-2023-49981
 A directory listing vulnerability in School Fees Management System v1.0 allows attackers to list directories and sensitive files within the application without requiring authorization.



- [https://github.com/geraldoalcantara/CVE-2023-49981](https://github.com/geraldoalcantara/CVE-2023-49981) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49981.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49981.svg)

## CVE-2023-49980
 A directory listing vulnerability in Best Student Result Management System v1.0 allows attackers to list directories and sensitive files within the application without requiring authorization.



- [https://github.com/geraldoalcantara/CVE-2023-49980](https://github.com/geraldoalcantara/CVE-2023-49980) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49980.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49980.svg)

## CVE-2023-49979
 A directory listing vulnerability in Customer Support System v1 allows attackers to list directories and sensitive files within the application without requiring authorization.



- [https://github.com/geraldoalcantara/CVE-2023-49979](https://github.com/geraldoalcantara/CVE-2023-49979) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49979.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49979.svg)

## CVE-2023-49978
 Incorrect access control in Customer Support System v1 allows non-administrator users to access administrative pages and execute actions reserved for administrators.



- [https://github.com/geraldoalcantara/CVE-2023-49978](https://github.com/geraldoalcantara/CVE-2023-49978) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49978.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49978.svg)

## CVE-2023-49977
 A cross-site scripting (XSS) vulnerability in Customer Support System v1 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the address parameter at /customer_support/index.php?page=new_customer.



- [https://github.com/geraldoalcantara/CVE-2023-49977](https://github.com/geraldoalcantara/CVE-2023-49977) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49977.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49977.svg)

## CVE-2023-49976
 A cross-site scripting (XSS) vulnerability in Customer Support System v1 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the subject parameter at /customer_support/index.php?page=new_ticket.



- [https://github.com/geraldoalcantara/CVE-2023-49976](https://github.com/geraldoalcantara/CVE-2023-49976) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49976.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49976.svg)

## CVE-2023-49974
 A cross-site scripting (XSS) vulnerability in Customer Support System v1 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the contact parameter at /customer_support/index.php?page=customer_list.



- [https://github.com/geraldoalcantara/CVE-2023-49974](https://github.com/geraldoalcantara/CVE-2023-49974) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49974.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49974.svg)

## CVE-2023-49973
 A cross-site scripting (XSS) vulnerability in Customer Support System v1 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the email parameter at /customer_support/index.php?page=customer_list.



- [https://github.com/geraldoalcantara/CVE-2023-49973](https://github.com/geraldoalcantara/CVE-2023-49973) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49973.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49973.svg)

## CVE-2023-49971
 A cross-site scripting (XSS) vulnerability in Customer Support System v1 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the firstname parameter at /customer_support/index.php?page=customer_list.



- [https://github.com/geraldoalcantara/CVE-2023-49971](https://github.com/geraldoalcantara/CVE-2023-49971) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49971.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49971.svg)

## CVE-2023-49970
 Customer Support System v1 was discovered to contain a SQL injection vulnerability via the subject parameter at /customer_support/ajax.php?action=save_ticket.



- [https://github.com/geraldoalcantara/CVE-2023-49970](https://github.com/geraldoalcantara/CVE-2023-49970) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49970.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49970.svg)

## CVE-2023-49969
 Customer Support System v1 was discovered to contain a SQL injection vulnerability via the id parameter at /customer_support/index.php?page=edit_customer.



- [https://github.com/geraldoalcantara/CVE-2023-49969](https://github.com/geraldoalcantara/CVE-2023-49969) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49969.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49969.svg)

## CVE-2023-49968
 Customer Support System v1 was discovered to contain a SQL injection vulnerability via the id parameter at /customer_support/manage_department.php.



- [https://github.com/geraldoalcantara/CVE-2023-49968](https://github.com/geraldoalcantara/CVE-2023-49968) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49968.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49968.svg)

## CVE-2023-49965
 SpaceX Starlink Wi-Fi router Gen 2 before 2023.48.0 allows XSS via the ssid and password parameters on the Setup Page.



- [https://github.com/yoshida-git-ai/SpaceX-Starlink-Router-Gen-2-XSS](https://github.com/yoshida-git-ai/SpaceX-Starlink-Router-Gen-2-XSS) :  ![starts](https://img.shields.io/github/stars/yoshida-git-ai/SpaceX-Starlink-Router-Gen-2-XSS.svg) ![forks](https://img.shields.io/github/forks/yoshida-git-ai/SpaceX-Starlink-Router-Gen-2-XSS.svg)

## CVE-2023-49964
 An issue was discovered in Hyland Alfresco Community Edition through 7.2.0. By inserting malicious content in the folder.get.html.ftl file, an attacker may perform SSTI (Server-Side Template Injection) attacks, which can leverage FreeMarker exposed objects to bypass restrictions and achieve RCE (Remote Code Execution). NOTE: this issue exists because of an incomplete fix for CVE-2020-12873.



- [https://github.com/mbadanoiu/CVE-2023-49964](https://github.com/mbadanoiu/CVE-2023-49964) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2023-49964.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2023-49964.svg)

## CVE-2023-49954
 The CRM Integration in 3CX before 18.0.9.23 and 20 before 20.0.0.1494 allows SQL Injection via a first name, search string, or email address.



- [https://github.com/CVE-2023-49954/CVE-2023-49954.github.io](https://github.com/CVE-2023-49954/CVE-2023-49954.github.io) :  ![starts](https://img.shields.io/github/stars/CVE-2023-49954/CVE-2023-49954.github.io.svg) ![forks](https://img.shields.io/github/forks/CVE-2023-49954/CVE-2023-49954.github.io.svg)

## CVE-2023-49950
 The Jinja templating in Logpoint SIEM 6.10.0 through 7.x before 7.3.0 does not correctly sanitize log data being displayed when using a custom Jinja template in the Alert view. A remote attacker can craft a cross-site scripting (XSS) payload and send it to any system or device that sends logs to the SIEM. If an alert is created, the payload will execute upon the alert data being viewed with that template, which can lead to sensitive data disclosure.



- [https://github.com/shrikeinfosec/cve-2023-49950](https://github.com/shrikeinfosec/cve-2023-49950) :  ![starts](https://img.shields.io/github/stars/shrikeinfosec/cve-2023-49950.svg) ![forks](https://img.shields.io/github/forks/shrikeinfosec/cve-2023-49950.svg)

## CVE-2023-49606
 A use-after-free vulnerability exists in the HTTP Connection Headers parsing in Tinyproxy 1.11.1 and Tinyproxy 1.10.0. A specially crafted HTTP header can trigger reuse of previously freed memory, which leads to memory corruption and could lead to remote code execution. An attacker needs to make an unauthenticated HTTP request to trigger this vulnerability.



- [https://github.com/d0rb/CVE-2023-49606](https://github.com/d0rb/CVE-2023-49606) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-49606.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-49606.svg)

## CVE-2023-49548
 Customer Support System v1 was discovered to contain a SQL injection vulnerability via the lastname parameter at /customer_support/ajax.php?action=save_user.



- [https://github.com/geraldoalcantara/CVE-2023-49548](https://github.com/geraldoalcantara/CVE-2023-49548) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49548.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49548.svg)

## CVE-2023-49547
 Customer Support System v1 was discovered to contain a SQL injection vulnerability via the username parameter at /customer_support/ajax.php?action=login.



- [https://github.com/geraldoalcantara/CVE-2023-49547](https://github.com/geraldoalcantara/CVE-2023-49547) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49547.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49547.svg)

## CVE-2023-49546
 Customer Support System v1 was discovered to contain a SQL injection vulnerability via the email parameter at /customer_support/ajax.php.



- [https://github.com/geraldoalcantara/CVE-2023-49546](https://github.com/geraldoalcantara/CVE-2023-49546) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49546.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49546.svg)

## CVE-2023-49545
 A directory listing vulnerability in Customer Support System v1 allows attackers to list directories and sensitive files within the application without requiring authorization.



- [https://github.com/geraldoalcantara/CVE-2023-49545](https://github.com/geraldoalcantara/CVE-2023-49545) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49545.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49545.svg)

## CVE-2023-49544
 A local file inclusion (LFI) in Customer Support System v1 allows attackers to include internal PHP files and gain unauthorized acces via manipulation of the page= parameter at /customer_support/index.php.



- [https://github.com/geraldoalcantara/CVE-2023-49544](https://github.com/geraldoalcantara/CVE-2023-49544) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49544.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49544.svg)

## CVE-2023-49543
 Incorrect access control in Book Store Management System v1 allows attackers to access unauthorized pages and execute administrative functions without authenticating.



- [https://github.com/geraldoalcantara/CVE-2023-49543](https://github.com/geraldoalcantara/CVE-2023-49543) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49543.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49543.svg)

## CVE-2023-49540
 Book Store Management System v1.0 was discovered to contain a cross-site scripting (XSS) vulnerability in /bsms_ci/index.php/history. This vulnerability allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the history parameter.



- [https://github.com/geraldoalcantara/CVE-2023-49540](https://github.com/geraldoalcantara/CVE-2023-49540) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49540.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49540.svg)

## CVE-2023-49539
 Book Store Management System v1.0 was discovered to contain a cross-site scripting (XSS) vulnerability in /bsms_ci/index.php/category. This vulnerability allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the category parameter.



- [https://github.com/geraldoalcantara/CVE-2023-49539](https://github.com/geraldoalcantara/CVE-2023-49539) :  ![starts](https://img.shields.io/github/stars/geraldoalcantara/CVE-2023-49539.svg) ![forks](https://img.shields.io/github/forks/geraldoalcantara/CVE-2023-49539.svg)

## CVE-2023-49496
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/HuangYanQwQ/CVE-2023-49496](https://github.com/HuangYanQwQ/CVE-2023-49496) :  ![starts](https://img.shields.io/github/stars/HuangYanQwQ/CVE-2023-49496.svg) ![forks](https://img.shields.io/github/forks/HuangYanQwQ/CVE-2023-49496.svg)

## CVE-2023-49471
 Blind Server-Side Request Forgery (SSRF) vulnerability in karlomikus Bar Assistant before version 3.2.0 does not validate a parameter before making a request through Image::make(), which could allow authenticated remote attackers to execute arbitrary code.



- [https://github.com/zunak/CVE-2023-49471](https://github.com/zunak/CVE-2023-49471) :  ![starts](https://img.shields.io/github/stars/zunak/CVE-2023-49471.svg) ![forks](https://img.shields.io/github/forks/zunak/CVE-2023-49471.svg)

## CVE-2023-49438
 An open redirect vulnerability in the python package Flask-Security-Too =5.3.2 allows attackers to redirect unsuspecting users to malicious sites via a crafted URL by abusing the ?next parameter on the /login and /register routes.



- [https://github.com/brandon-t-elliott/CVE-2023-49438](https://github.com/brandon-t-elliott/CVE-2023-49438) :  ![starts](https://img.shields.io/github/stars/brandon-t-elliott/CVE-2023-49438.svg) ![forks](https://img.shields.io/github/forks/brandon-t-elliott/CVE-2023-49438.svg)

## CVE-2023-49339
 Ellucian Banner 9.17 allows Insecure Direct Object Reference (IDOR) via a modified bannerId to the /StudentSelfService/ssb/studentCard/retrieveData endpoint.



- [https://github.com/3zizme/CVE-2023-49339](https://github.com/3zizme/CVE-2023-49339) :  ![starts](https://img.shields.io/github/stars/3zizme/CVE-2023-49339.svg) ![forks](https://img.shields.io/github/forks/3zizme/CVE-2023-49339.svg)

## CVE-2023-49314
 Asana Desktop 2.1.0 on macOS allows code injection because of specific Electron Fuses. There is inadequate protection against code injection through settings such as RunAsNode and EnableNodeCliInspectArguments, and thus r3ggi/electroniz3r can be used to perform an attack.



- [https://github.com/louiselalanne/CVE-2023-49314](https://github.com/louiselalanne/CVE-2023-49314) :  ![starts](https://img.shields.io/github/stars/louiselalanne/CVE-2023-49314.svg) ![forks](https://img.shields.io/github/forks/louiselalanne/CVE-2023-49314.svg)

## CVE-2023-49313
 A dylib injection vulnerability in XMachOViewer 0.04 allows attackers to compromise integrity. By exploiting this, unauthorized code can be injected into the product's processes, potentially leading to remote control and unauthorized access to sensitive user data.



- [https://github.com/louiselalanne/CVE-2023-49313](https://github.com/louiselalanne/CVE-2023-49313) :  ![starts](https://img.shields.io/github/stars/louiselalanne/CVE-2023-49313.svg) ![forks](https://img.shields.io/github/forks/louiselalanne/CVE-2023-49313.svg)

## CVE-2023-49105
 An issue was discovered in ownCloud owncloud/core before 10.13.1. An attacker can access, modify, or delete any file without authentication if the username of a victim is known, and the victim has no signing-key configured. This occurs because pre-signed URLs can be accepted even when no signing-key is configured for the owner of the files. The earliest affected version is 10.6.0.



- [https://github.com/ambionics/owncloud-exploits](https://github.com/ambionics/owncloud-exploits) :  ![starts](https://img.shields.io/github/stars/ambionics/owncloud-exploits.svg) ![forks](https://img.shields.io/github/forks/ambionics/owncloud-exploits.svg)

## CVE-2023-49103
 An issue was discovered in ownCloud owncloud/graphapi 0.2.x before 0.2.1 and 0.3.x before 0.3.1. The graphapi app relies on a third-party GetPhpInfo.php library that provides a URL. When this URL is accessed, it reveals the configuration details of the PHP environment (phpinfo). This information includes all the environment variables of the webserver. In containerized deployments, these environment variables may include sensitive data such as the ownCloud admin password, mail server credentials, and license key. Simply disabling the graphapi app does not eliminate the vulnerability. Additionally, phpinfo exposes various other potentially sensitive configuration details that could be exploited by an attacker to gather information about the system. Therefore, even if ownCloud is not running in a containerized environment, this vulnerability should still be a cause for concern. Note that Docker containers from before February 2023 are not vulnerable to the credential disclosure.



- [https://github.com/creacitysec/CVE-2023-49103](https://github.com/creacitysec/CVE-2023-49103) :  ![starts](https://img.shields.io/github/stars/creacitysec/CVE-2023-49103.svg) ![forks](https://img.shields.io/github/forks/creacitysec/CVE-2023-49103.svg)

- [https://github.com/merlin-ke/OwnCloud-CVE-2023-49103](https://github.com/merlin-ke/OwnCloud-CVE-2023-49103) :  ![starts](https://img.shields.io/github/stars/merlin-ke/OwnCloud-CVE-2023-49103.svg) ![forks](https://img.shields.io/github/forks/merlin-ke/OwnCloud-CVE-2023-49103.svg)

- [https://github.com/d0rb/CVE-2023-49103](https://github.com/d0rb/CVE-2023-49103) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-49103.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-49103.svg)

## CVE-2023-49070
 Pre-auth RCE in Apache Ofbiz 18.12.09.

It's due to XML-RPC no longer maintained still present.
This issue affects Apache OFBiz: before 18.12.10. 
Users are recommended to upgrade to version 18.12.10



- [https://github.com/jakabakos/Apache-OFBiz-Authentication-Bypass](https://github.com/jakabakos/Apache-OFBiz-Authentication-Bypass) :  ![starts](https://img.shields.io/github/stars/jakabakos/Apache-OFBiz-Authentication-Bypass.svg) ![forks](https://img.shields.io/github/forks/jakabakos/Apache-OFBiz-Authentication-Bypass.svg)

- [https://github.com/abdoghazy2015/ofbiz-CVE-2023-49070-RCE-POC](https://github.com/abdoghazy2015/ofbiz-CVE-2023-49070-RCE-POC) :  ![starts](https://img.shields.io/github/stars/abdoghazy2015/ofbiz-CVE-2023-49070-RCE-POC.svg) ![forks](https://img.shields.io/github/forks/abdoghazy2015/ofbiz-CVE-2023-49070-RCE-POC.svg)

- [https://github.com/D0g3-8Bit/OFBiz-Attack](https://github.com/D0g3-8Bit/OFBiz-Attack) :  ![starts](https://img.shields.io/github/stars/D0g3-8Bit/OFBiz-Attack.svg) ![forks](https://img.shields.io/github/forks/D0g3-8Bit/OFBiz-Attack.svg)

- [https://github.com/UserConnecting/Exploit-CVE-2023-49070-and-CVE-2023-51467-Apache-OFBiz](https://github.com/UserConnecting/Exploit-CVE-2023-49070-and-CVE-2023-51467-Apache-OFBiz) :  ![starts](https://img.shields.io/github/stars/UserConnecting/Exploit-CVE-2023-49070-and-CVE-2023-51467-Apache-OFBiz.svg) ![forks](https://img.shields.io/github/forks/UserConnecting/Exploit-CVE-2023-49070-and-CVE-2023-51467-Apache-OFBiz.svg)

- [https://github.com/yukselberkay/CVE-2023-49070_CVE-2023-51467](https://github.com/yukselberkay/CVE-2023-49070_CVE-2023-51467) :  ![starts](https://img.shields.io/github/stars/yukselberkay/CVE-2023-49070_CVE-2023-51467.svg) ![forks](https://img.shields.io/github/forks/yukselberkay/CVE-2023-49070_CVE-2023-51467.svg)

- [https://github.com/0xrobiul/CVE-2023-49070](https://github.com/0xrobiul/CVE-2023-49070) :  ![starts](https://img.shields.io/github/stars/0xrobiul/CVE-2023-49070.svg) ![forks](https://img.shields.io/github/forks/0xrobiul/CVE-2023-49070.svg)

- [https://github.com/Praison001/Apache-OFBiz-Auth-Bypass-and-RCE-Exploit-CVE-2023-49070-CVE-2023-51467](https://github.com/Praison001/Apache-OFBiz-Auth-Bypass-and-RCE-Exploit-CVE-2023-49070-CVE-2023-51467) :  ![starts](https://img.shields.io/github/stars/Praison001/Apache-OFBiz-Auth-Bypass-and-RCE-Exploit-CVE-2023-49070-CVE-2023-51467.svg) ![forks](https://img.shields.io/github/forks/Praison001/Apache-OFBiz-Auth-Bypass-and-RCE-Exploit-CVE-2023-49070-CVE-2023-51467.svg)

## CVE-2023-49052
 File Upload vulnerability in Microweber v.2.0.4 allows a remote attacker to execute arbitrary code via a crafted script to the file upload function in the created forms component.



- [https://github.com/Cyber-Wo0dy/CVE-2023-49052](https://github.com/Cyber-Wo0dy/CVE-2023-49052) :  ![starts](https://img.shields.io/github/stars/Cyber-Wo0dy/CVE-2023-49052.svg) ![forks](https://img.shields.io/github/forks/Cyber-Wo0dy/CVE-2023-49052.svg)

## CVE-2023-49003
 An issue in simplemobiletools Simple Dialer 5.18.1 allows an attacker to bypass intended access restrictions via interaction with com.simplemobiletools.dialer.activities.DialerActivity.



- [https://github.com/actuator/com.simplemobiletools.dialer](https://github.com/actuator/com.simplemobiletools.dialer) :  ![starts](https://img.shields.io/github/stars/actuator/com.simplemobiletools.dialer.svg) ![forks](https://img.shields.io/github/forks/actuator/com.simplemobiletools.dialer.svg)

## CVE-2023-49002
 An issue in Xenom Technologies (sinous) Phone Dialer-voice Call Dialer v.1.2.5 allows an attacker to bypass intended access restrictions via interaction with com.funprime.calldialer.ui.activities.OutgoingActivity.



- [https://github.com/actuator/com.sinous.voice.dialer](https://github.com/actuator/com.sinous.voice.dialer) :  ![starts](https://img.shields.io/github/stars/actuator/com.sinous.voice.dialer.svg) ![forks](https://img.shields.io/github/forks/actuator/com.sinous.voice.dialer.svg)

## CVE-2023-48984
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/l00neyhacker/CVE-2023-48984](https://github.com/l00neyhacker/CVE-2023-48984) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2023-48984.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2023-48984.svg)

## CVE-2023-48983
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/tristao-marinho/CVE-2023-48983](https://github.com/tristao-marinho/CVE-2023-48983) :  ![starts](https://img.shields.io/github/stars/tristao-marinho/CVE-2023-48983.svg) ![forks](https://img.shields.io/github/forks/tristao-marinho/CVE-2023-48983.svg)

## CVE-2023-48982
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/tristao-marinho/CVE-2023-48982](https://github.com/tristao-marinho/CVE-2023-48982) :  ![starts](https://img.shields.io/github/stars/tristao-marinho/CVE-2023-48982.svg) ![forks](https://img.shields.io/github/forks/tristao-marinho/CVE-2023-48982.svg)

## CVE-2023-48981
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/tristao-marinho/CVE-2023-48981](https://github.com/tristao-marinho/CVE-2023-48981) :  ![starts](https://img.shields.io/github/stars/tristao-marinho/CVE-2023-48981.svg) ![forks](https://img.shields.io/github/forks/tristao-marinho/CVE-2023-48981.svg)

## CVE-2023-48974
 Cross Site Scripting vulnerability in Axigen WebMail prior to 10.3.3.61 allows a remote attacker to escalate privileges via a crafted script to the serverName_input parameter.



- [https://github.com/vinnie1717/CVE-2023-48974](https://github.com/vinnie1717/CVE-2023-48974) :  ![starts](https://img.shields.io/github/stars/vinnie1717/CVE-2023-48974.svg) ![forks](https://img.shields.io/github/forks/vinnie1717/CVE-2023-48974.svg)

## CVE-2023-48858
 A Cross-site scripting (XSS) vulnerability in login page php code in Armex ABO.CMS 5.9 allows remote attackers to inject arbitrary web script or HTML via the login.php? URL part.



- [https://github.com/Shumerez/CVE-2023-48858](https://github.com/Shumerez/CVE-2023-48858) :  ![starts](https://img.shields.io/github/stars/Shumerez/CVE-2023-48858.svg) ![forks](https://img.shields.io/github/forks/Shumerez/CVE-2023-48858.svg)

## CVE-2023-48849
 Ruijie EG Series Routers version EG_3.0(1)B11P216 and before allows unauthenticated attackers to remotely execute arbitrary code due to incorrect filtering.



- [https://github.com/delsploit/CVE-2023-48849](https://github.com/delsploit/CVE-2023-48849) :  ![starts](https://img.shields.io/github/stars/delsploit/CVE-2023-48849.svg) ![forks](https://img.shields.io/github/forks/delsploit/CVE-2023-48849.svg)

## CVE-2023-48842
 D-Link Go-RT-AC750 revA_v101b03 was discovered to contain a command injection vulnerability via the service parameter at hedwig.cgi.



- [https://github.com/creacitysec/CVE-2023-48842](https://github.com/creacitysec/CVE-2023-48842) :  ![starts](https://img.shields.io/github/stars/creacitysec/CVE-2023-48842.svg) ![forks](https://img.shields.io/github/forks/creacitysec/CVE-2023-48842.svg)

## CVE-2023-48795
 The SSH transport protocol with certain OpenSSH extensions, found in OpenSSH before 9.6 and other products, allows remote attackers to bypass integrity checks such that some packets are omitted (from the extension negotiation message), and a client and server may consequently end up with a connection for which some security features have been downgraded or disabled, aka a Terrapin attack. This occurs because the SSH Binary Packet Protocol (BPP), implemented by these extensions, mishandles the handshake phase and mishandles use of sequence numbers. For example, there is an effective attack against SSH's use of ChaCha20-Poly1305 (and CBC with Encrypt-then-MAC). The bypass occurs in chacha20-poly1305@openssh.com and (if CBC is used) the -etm@openssh.com MAC algorithms. This also affects Maverick Synergy Java SSH API before 3.1.0-SNAPSHOT, Dropbear through 2022.83, Ssh before 5.1.1 in Erlang/OTP, PuTTY before 0.80, AsyncSSH before 2.14.2, golang.org/x/crypto before 0.17.0, libssh before 0.10.6, libssh2 through 1.11.0, Thorn Tech SFTP Gateway before 3.4.6, Tera Term before 5.1, Paramiko before 3.4.0, jsch before 0.2.15, SFTPGo before 2.5.6, Netgate pfSense Plus through 23.09.1, Netgate pfSense CE through 2.7.2, HPN-SSH through 18.2.0, ProFTPD before 1.3.8b (and before 1.3.9rc2), ORYX CycloneSSH before 2.3.4, NetSarang XShell 7 before Build 0144, CrushFTP before 10.6.0, ConnectBot SSH library before 2.2.22, Apache MINA sshd through 2.11.0, sshj through 0.37.0, TinySSH through 20230101, trilead-ssh2 6401, LANCOM LCOS and LANconfig, FileZilla before 3.66.4, Nova before 11.8, PKIX-SSH before 14.4, SecureCRT before 9.4.3, Transmit5 before 5.10.4, Win32-OpenSSH before 9.5.0.0p1-Beta, WinSCP before 6.2.2, Bitvise SSH Server before 9.32, Bitvise SSH Client before 9.33, KiTTY through 0.76.1.13, the net-ssh gem 7.2.0 for Ruby, the mscdex ssh2 module before 1.15.0 for Node.js, the thrussh library before 0.35.1 for Rust, and the Russh crate before 0.40.2 for Rust.



- [https://github.com/RUB-NDS/Terrapin-Artifacts](https://github.com/RUB-NDS/Terrapin-Artifacts) :  ![starts](https://img.shields.io/github/stars/RUB-NDS/Terrapin-Artifacts.svg) ![forks](https://img.shields.io/github/forks/RUB-NDS/Terrapin-Artifacts.svg)

- [https://github.com/TrixSec/CVE-2023-48795](https://github.com/TrixSec/CVE-2023-48795) :  ![starts](https://img.shields.io/github/stars/TrixSec/CVE-2023-48795.svg) ![forks](https://img.shields.io/github/forks/TrixSec/CVE-2023-48795.svg)

- [https://github.com/Dr0xharakiri/CVE-2023-48795](https://github.com/Dr0xharakiri/CVE-2023-48795) :  ![starts](https://img.shields.io/github/stars/Dr0xharakiri/CVE-2023-48795.svg) ![forks](https://img.shields.io/github/forks/Dr0xharakiri/CVE-2023-48795.svg)

## CVE-2023-48788
 A improper neutralization of special elements used in an sql command ('sql injection') in Fortinet FortiClientEMS version 7.2.0 through 7.2.2, FortiClientEMS 7.0.1 through 7.0.10 allows attacker to execute unauthorized code or commands via specially crafted packets.



- [https://github.com/horizon3ai/CVE-2023-48788](https://github.com/horizon3ai/CVE-2023-48788) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2023-48788.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2023-48788.svg)

## CVE-2023-48777
 Unrestricted Upload of File with Dangerous Type vulnerability in Elementor.Com Elementor Website Builder.This issue affects Elementor Website Builder: from 3.3.0 through 3.18.1.





- [https://github.com/AkuCyberSec/Elementor-3.18.0-Upload-Path-Traversal-RCE-CVE-2023-48777](https://github.com/AkuCyberSec/Elementor-3.18.0-Upload-Path-Traversal-RCE-CVE-2023-48777) :  ![starts](https://img.shields.io/github/stars/AkuCyberSec/Elementor-3.18.0-Upload-Path-Traversal-RCE-CVE-2023-48777.svg) ![forks](https://img.shields.io/github/forks/AkuCyberSec/Elementor-3.18.0-Upload-Path-Traversal-RCE-CVE-2023-48777.svg)

## CVE-2023-48643
 Shrubbery tac_plus 2.x, 3.x. and 4.x through F4.0.4.28 allows unauthenticated Remote Command Execution. The product allows users to configure authorization checks as shell commands through the tac_plus.cfg configuration file. These are executed when a client sends an authorization request with a username that has pre-authorization directives configured. However, it is possible to inject additional commands into these checks because strings from TACACS+ packets are used as command-line arguments. If the installation lacks a a pre-shared secret (there is no pre-shared secret by default), then the injection can be triggered without authentication. (The attacker needs to know a username configured to use a pre-authorization command.) NOTE: this is related to CVE-2023-45239 but the issue is in the original Shrubbery product, not Meta's fork.



- [https://github.com/takeshixx/tac_plus-pre-auth-rce](https://github.com/takeshixx/tac_plus-pre-auth-rce) :  ![starts](https://img.shields.io/github/stars/takeshixx/tac_plus-pre-auth-rce.svg) ![forks](https://img.shields.io/github/forks/takeshixx/tac_plus-pre-auth-rce.svg)

## CVE-2023-48194
 Vulnerability in Tenda AC8v4 .V16.03.34.09 due to sscanf and the last digit of s8 being overwritten with \x0. After executing set_client_qos, control over the gp register can be obtained.



- [https://github.com/zt20xx/CVE-2023-48194](https://github.com/zt20xx/CVE-2023-48194) :  ![starts](https://img.shields.io/github/stars/zt20xx/CVE-2023-48194.svg) ![forks](https://img.shields.io/github/forks/zt20xx/CVE-2023-48194.svg)

## CVE-2023-48123
 An issue in Netgate pfSense Plus v.23.05.1 and before and pfSense CE v.2.7.0 allows a remote attacker to execute arbitrary code via a crafted request to the packet_capture.php file.



- [https://github.com/NHPT/CVE-2023-48123](https://github.com/NHPT/CVE-2023-48123) :  ![starts](https://img.shields.io/github/stars/NHPT/CVE-2023-48123.svg) ![forks](https://img.shields.io/github/forks/NHPT/CVE-2023-48123.svg)

## CVE-2023-48104
 Alinto SOGo before 5.9.1 is vulnerable to HTML Injection.



- [https://github.com/E1tex/CVE-2023-48104](https://github.com/E1tex/CVE-2023-48104) :  ![starts](https://img.shields.io/github/stars/E1tex/CVE-2023-48104.svg) ![forks](https://img.shields.io/github/forks/E1tex/CVE-2023-48104.svg)

## CVE-2023-48084
 Nagios XI before version 5.11.3 was discovered to contain a SQL injection vulnerability via the bulk modification tool.



- [https://github.com/Hamibubu/CVE-2023-48084](https://github.com/Hamibubu/CVE-2023-48084) :  ![starts](https://img.shields.io/github/stars/Hamibubu/CVE-2023-48084.svg) ![forks](https://img.shields.io/github/forks/Hamibubu/CVE-2023-48084.svg)

- [https://github.com/bucketcat/CVE-2023-48084](https://github.com/bucketcat/CVE-2023-48084) :  ![starts](https://img.shields.io/github/stars/bucketcat/CVE-2023-48084.svg) ![forks](https://img.shields.io/github/forks/bucketcat/CVE-2023-48084.svg)

## CVE-2023-48034
 An issue discovered in Acer Wireless Keyboard SK-9662 allows attacker in physical proximity to both decrypt wireless keystrokes and inject arbitrary keystrokes via use of weak encryption.



- [https://github.com/aprkr/CVE-2023-48034](https://github.com/aprkr/CVE-2023-48034) :  ![starts](https://img.shields.io/github/stars/aprkr/CVE-2023-48034.svg) ![forks](https://img.shields.io/github/forks/aprkr/CVE-2023-48034.svg)

## CVE-2023-48022
 Anyscale Ray 2.6.3 and 2.8.0 allows a remote attacker to execute arbitrary code via the job submission API. NOTE: the vendor's position is that this report is irrelevant because Ray, as stated in its documentation, is not intended for use outside of a strictly controlled network environment



- [https://github.com/jakabakos/ShadowRay-RCE-PoC-CVE-2023-48022](https://github.com/jakabakos/ShadowRay-RCE-PoC-CVE-2023-48022) :  ![starts](https://img.shields.io/github/stars/jakabakos/ShadowRay-RCE-PoC-CVE-2023-48022.svg) ![forks](https://img.shields.io/github/forks/jakabakos/ShadowRay-RCE-PoC-CVE-2023-48022.svg)

- [https://github.com/0x656565/CVE-2023-48022](https://github.com/0x656565/CVE-2023-48022) :  ![starts](https://img.shields.io/github/stars/0x656565/CVE-2023-48022.svg) ![forks](https://img.shields.io/github/forks/0x656565/CVE-2023-48022.svg)

## CVE-2023-47889
 The Android application BINHDRM26 com.bdrm.superreboot 1.0.3, exposes several critical actions through its exported broadcast receivers. These exposed actions can allow any app on the device to send unauthorized broadcasts, leading to unintended consequences. The vulnerability is particularly concerning because these actions include powering off, system reboot & entering recovery mode.



- [https://github.com/actuator/com.bdrm.superreboot](https://github.com/actuator/com.bdrm.superreboot) :  ![starts](https://img.shields.io/github/stars/actuator/com.bdrm.superreboot.svg) ![forks](https://img.shields.io/github/forks/actuator/com.bdrm.superreboot.svg)

## CVE-2023-47883
 The com.altamirano.fabricio.tvbrowser TV browser application through 4.5.1 for Android is vulnerable to JavaScript code execution via an explicit intent due to an exposed MainActivity.



- [https://github.com/actuator/com.altamirano.fabricio.tvbrowser](https://github.com/actuator/com.altamirano.fabricio.tvbrowser) :  ![starts](https://img.shields.io/github/stars/actuator/com.altamirano.fabricio.tvbrowser.svg) ![forks](https://img.shields.io/github/forks/actuator/com.altamirano.fabricio.tvbrowser.svg)

## CVE-2023-47882
 The Kami Vision YI IoT com.yunyi.smartcamera application through 4.1.9_20231127 for Android allows a remote attacker to execute arbitrary JavaScript code via an implicit intent to the com.ants360.yicamera.activity.WebViewActivity component.



- [https://github.com/actuator/yi](https://github.com/actuator/yi) :  ![starts](https://img.shields.io/github/stars/actuator/yi.svg) ![forks](https://img.shields.io/github/forks/actuator/yi.svg)

## CVE-2023-47840
 Improper Control of Generation of Code ('Code Injection') vulnerability in Qode Interactive Qode Essential Addons.This issue affects Qode Essential Addons: from n/a through 1.5.2.





- [https://github.com/RandomRobbieBF/CVE-2023-47840](https://github.com/RandomRobbieBF/CVE-2023-47840) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-47840.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-47840.svg)

## CVE-2023-47668
 Exposure of Sensitive Information to an Unauthorized Actor vulnerability in StellarWP Membership Plugin – Restrict Content plugin = 3.2.7 versions.



- [https://github.com/RandomRobbieBF/CVE-2023-47668](https://github.com/RandomRobbieBF/CVE-2023-47668) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-47668.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-47668.svg)

- [https://github.com/Nxploited/CVE-2023-47668](https://github.com/Nxploited/CVE-2023-47668) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2023-47668.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2023-47668.svg)

## CVE-2023-47564
 An incorrect permission assignment for critical resource vulnerability has been reported to affect Qsync Central. If exploited, the vulnerability could allow authenticated users to read or modify the resource via a network.

We have already fixed the vulnerability in the following versions:
Qsync Central 4.4.0.15 ( 2024/01/04 ) and later
Qsync Central 4.3.0.11 ( 2024/01/11 ) and later




- [https://github.com/C411e/CVE-2023-47564](https://github.com/C411e/CVE-2023-47564) :  ![starts](https://img.shields.io/github/stars/C411e/CVE-2023-47564.svg) ![forks](https://img.shields.io/github/forks/C411e/CVE-2023-47564.svg)

## CVE-2023-47529
 Exposure of Sensitive Information to an Unauthorized Actor vulnerability in ThemeIsle Cloud Templates & Patterns collection.This issue affects Cloud Templates & Patterns collection: from n/a through 1.2.2.





- [https://github.com/RandomRobbieBF/CVE-2023-47529](https://github.com/RandomRobbieBF/CVE-2023-47529) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-47529.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-47529.svg)

## CVE-2023-47504
 Improper Authentication vulnerability in Elementor Elementor Website Builder allows Accessing Functionality Not Properly Constrained by ACLs.This issue affects Elementor Website Builder: from n/a through 3.16.4.





- [https://github.com/davidxbors/CVE-2023-47504-POC](https://github.com/davidxbors/CVE-2023-47504-POC) :  ![starts](https://img.shields.io/github/stars/davidxbors/CVE-2023-47504-POC.svg) ![forks](https://img.shields.io/github/forks/davidxbors/CVE-2023-47504-POC.svg)

## CVE-2023-47464
 Insecure Permissions vulnerability in GL.iNet AX1800 version 4.0.0 before 4.5.0 allows a remote attacker to execute arbitrary code via the upload API function.



- [https://github.com/HadessCS/CVE-2023-47464](https://github.com/HadessCS/CVE-2023-47464) :  ![starts](https://img.shields.io/github/stars/HadessCS/CVE-2023-47464.svg) ![forks](https://img.shields.io/github/forks/HadessCS/CVE-2023-47464.svg)

## CVE-2023-47460
 SQL injection vulnerability in Knovos Discovery v.22.67.0 allows a remote attacker to execute arbitrary code via the /DiscoveryProcess/Service/Admin.svc/getGridColumnStructure component.



- [https://github.com/aleksey-vi/CVE-2023-47460](https://github.com/aleksey-vi/CVE-2023-47460) :  ![starts](https://img.shields.io/github/stars/aleksey-vi/CVE-2023-47460.svg) ![forks](https://img.shields.io/github/forks/aleksey-vi/CVE-2023-47460.svg)

## CVE-2023-47459
 An issue in Knovos Discovery v.22.67.0 allows a remote attacker to obtain sensitive information via the /DiscoveryReview/Service/CaseManagement.svc/GetProductSiteName component.



- [https://github.com/aleksey-vi/CVE-2023-47459](https://github.com/aleksey-vi/CVE-2023-47459) :  ![starts](https://img.shields.io/github/stars/aleksey-vi/CVE-2023-47459.svg) ![forks](https://img.shields.io/github/forks/aleksey-vi/CVE-2023-47459.svg)

## CVE-2023-47437
 A vulnerability has been identified in Pachno 1.0.6 allowing an authenticated attacker to execute a cross-site scripting (XSS) attack. The vulnerability exists due to inadequate input validation in the Project Description and comments, which enables an attacker to inject malicious java script.



- [https://github.com/herombey/CVE-2023-47437](https://github.com/herombey/CVE-2023-47437) :  ![starts](https://img.shields.io/github/stars/herombey/CVE-2023-47437.svg) ![forks](https://img.shields.io/github/forks/herombey/CVE-2023-47437.svg)

## CVE-2023-47400
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/LucasVanHaaren/CVE-2023-47400](https://github.com/LucasVanHaaren/CVE-2023-47400) :  ![starts](https://img.shields.io/github/stars/LucasVanHaaren/CVE-2023-47400.svg) ![forks](https://img.shields.io/github/forks/LucasVanHaaren/CVE-2023-47400.svg)

## CVE-2023-47355
 The com.eypcnnapps.quickreboot (aka Eyuep Can Yilmaz {ROOT] Quick Reboot) application 1.0.8 for Android has exposed broadcast receivers for PowerOff, Reboot, and Recovery (e.g., com.eypcnnapps.quickreboot.widget.PowerOff) that are susceptible to unauthorized broadcasts because of missing input validation.



- [https://github.com/actuator/com.eypcnnapps.quickreboot](https://github.com/actuator/com.eypcnnapps.quickreboot) :  ![starts](https://img.shields.io/github/stars/actuator/com.eypcnnapps.quickreboot.svg) ![forks](https://img.shields.io/github/forks/actuator/com.eypcnnapps.quickreboot.svg)

## CVE-2023-47354
 An issue in the PowerOffWidgetReceiver function of Super Reboot (Root) Recovery v1.0.3 allows attackers to arbitrarily reset or power off the device via a crafted intent



- [https://github.com/actuator/com.bdrm.superreboot](https://github.com/actuator/com.bdrm.superreboot) :  ![starts](https://img.shields.io/github/stars/actuator/com.bdrm.superreboot.svg) ![forks](https://img.shields.io/github/forks/actuator/com.bdrm.superreboot.svg)

## CVE-2023-47353
 An issue in the com.oneed.dvr.service.DownloadFirmwareService component of IMOU GO v1.0.11 allows attackers to force the download of arbitrary files.



- [https://github.com/actuator/imou](https://github.com/actuator/imou) :  ![starts](https://img.shields.io/github/stars/actuator/imou.svg) ![forks](https://img.shields.io/github/forks/actuator/imou.svg)

## CVE-2023-47352
 Technicolor TC8715D devices have predictable default WPA2 security passwords. An attacker who scans for SSID and BSSID values may be able to predict these passwords.



- [https://github.com/actuator/BSIDES-Security-Las-Vegas-2024](https://github.com/actuator/BSIDES-Security-Las-Vegas-2024) :  ![starts](https://img.shields.io/github/stars/actuator/BSIDES-Security-Las-Vegas-2024.svg) ![forks](https://img.shields.io/github/forks/actuator/BSIDES-Security-Las-Vegas-2024.svg)

## CVE-2023-47246
 In SysAid On-Premise before 23.3.36, a path traversal vulnerability leads to code execution after an attacker writes a file to the Tomcat webroot, as exploited in the wild in November 2023.



- [https://github.com/W01fh4cker/CVE-2023-47246-EXP](https://github.com/W01fh4cker/CVE-2023-47246-EXP) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/CVE-2023-47246-EXP.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/CVE-2023-47246-EXP.svg)

- [https://github.com/XiaomingX/cve-2023-47246-poc](https://github.com/XiaomingX/cve-2023-47246-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2023-47246-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2023-47246-poc.svg)

- [https://github.com/tucommenceapousser/CVE-2023-47246](https://github.com/tucommenceapousser/CVE-2023-47246) :  ![starts](https://img.shields.io/github/stars/tucommenceapousser/CVE-2023-47246.svg) ![forks](https://img.shields.io/github/forks/tucommenceapousser/CVE-2023-47246.svg)

- [https://github.com/rainbowhatrkn/CVE-2023-47246](https://github.com/rainbowhatrkn/CVE-2023-47246) :  ![starts](https://img.shields.io/github/stars/rainbowhatrkn/CVE-2023-47246.svg) ![forks](https://img.shields.io/github/forks/rainbowhatrkn/CVE-2023-47246.svg)

## CVE-2023-47218
 An OS command injection vulnerability has been reported to affect several QNAP operating system versions. If exploited, the vulnerability could allow users to execute commands via a network.

We have already fixed the vulnerability in the following versions:
QTS 5.1.5.2645 build 20240116 and later
QuTS hero h5.1.5.2647 build 20240118 and later
QuTScloud c5.1.5.2651 and later



- [https://github.com/passwa11/CVE-2023-47218](https://github.com/passwa11/CVE-2023-47218) :  ![starts](https://img.shields.io/github/stars/passwa11/CVE-2023-47218.svg) ![forks](https://img.shields.io/github/forks/passwa11/CVE-2023-47218.svg)

## CVE-2023-47179
 Missing Authorization vulnerability in ByConsole WooODT Lite allows Exploiting Incorrectly Configured Access Control Security Levels.This issue affects WooODT Lite: from n/a through 2.4.6.



- [https://github.com/RandomRobbieBF/CVE-2023-47179](https://github.com/RandomRobbieBF/CVE-2023-47179) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-47179.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-47179.svg)

## CVE-2023-47129
 Statmic is a core Laravel content management system Composer package. Prior to versions 3.4.13 and 4.33.0, on front-end forms with an asset upload field, PHP files crafted to look like images may be uploaded. This only affects forms using the "Forms" feature and not just _any_ arbitrary form. This does not affect the control panel. This issue has been patched in 3.4.13 and 4.33.0.




- [https://github.com/Cyber-Wo0dy/CVE-2023-47129](https://github.com/Cyber-Wo0dy/CVE-2023-47129) :  ![starts](https://img.shields.io/github/stars/Cyber-Wo0dy/CVE-2023-47129.svg) ![forks](https://img.shields.io/github/forks/Cyber-Wo0dy/CVE-2023-47129.svg)

## CVE-2023-47119
 Discourse is an open source platform for community discussion. Prior to version 3.1.3 of the `stable` branch and version 3.2.0.beta3 of the `beta` and `tests-passed` branches, some links can inject arbitrary HTML tags when rendered through our Onebox engine. The issue is patched in version 3.1.3 of the `stable` branch and version 3.2.0.beta3 of the `beta` and `tests-passed` branches. There are no known workarounds.



- [https://github.com/BaadMaro/CVE-2023-47119](https://github.com/BaadMaro/CVE-2023-47119) :  ![starts](https://img.shields.io/github/stars/BaadMaro/CVE-2023-47119.svg) ![forks](https://img.shields.io/github/forks/BaadMaro/CVE-2023-47119.svg)

- [https://github.com/Cristiano100/CVE-2023-47119](https://github.com/Cristiano100/CVE-2023-47119) :  ![starts](https://img.shields.io/github/stars/Cristiano100/CVE-2023-47119.svg) ![forks](https://img.shields.io/github/forks/Cristiano100/CVE-2023-47119.svg)

## CVE-2023-47108
 OpenTelemetry-Go Contrib is a collection of third-party packages for OpenTelemetry-Go. Prior to version 0.46.0, the grpc Unary Server Interceptor out of the box adds labels `net.peer.sock.addr` and `net.peer.sock.port` that have unbound cardinality. It leads to the server's potential memory exhaustion when many malicious requests are sent. An attacker can easily flood the peer address and port for requests. Version 0.46.0 contains a fix for this issue. As a workaround to stop being affected, a view removing the attributes can be used. The other possibility is to disable grpc metrics instrumentation by passing `otelgrpc.WithMeterProvider` option with `noop.NewMeterProvider`.



- [https://github.com/bahe-msft/govuln-CVE-2023-47108](https://github.com/bahe-msft/govuln-CVE-2023-47108) :  ![starts](https://img.shields.io/github/stars/bahe-msft/govuln-CVE-2023-47108.svg) ![forks](https://img.shields.io/github/forks/bahe-msft/govuln-CVE-2023-47108.svg)

## CVE-2023-47102
 UrBackup Server 2.5.31 allows brute-force enumeration of user accounts because a failure message confirms that a username is not valid.



- [https://github.com/quantiano/cve-2023-47102](https://github.com/quantiano/cve-2023-47102) :  ![starts](https://img.shields.io/github/stars/quantiano/cve-2023-47102.svg) ![forks](https://img.shields.io/github/forks/quantiano/cve-2023-47102.svg)

## CVE-2023-47014
 A Cross-Site Request Forgery (CSRF) vulnerability in Sourcecodester Sticky Notes App Using PHP with Source Code v.1.0 allows a local attacker to obtain sensitive information via a crafted payload to add-note.php.



- [https://github.com/emirhanerdogu/CVE-2023-47014-Sticky-Notes-App-Using-PHP-with-Source-Code-v1.0-CSRF-to-CORS](https://github.com/emirhanerdogu/CVE-2023-47014-Sticky-Notes-App-Using-PHP-with-Source-Code-v1.0-CSRF-to-CORS) :  ![starts](https://img.shields.io/github/stars/emirhanerdogu/CVE-2023-47014-Sticky-Notes-App-Using-PHP-with-Source-Code-v1.0-CSRF-to-CORS.svg) ![forks](https://img.shields.io/github/forks/emirhanerdogu/CVE-2023-47014-Sticky-Notes-App-Using-PHP-with-Source-Code-v1.0-CSRF-to-CORS.svg)

## CVE-2023-46998
 Cross Site Scripting vulnerability in BootBox Bootbox.js v.3.2 through 6.0 allows a remote attacker to execute arbitrary code via a crafted payload to alert(), confirm(), prompt() functions.



- [https://github.com/soy-oreocato/CVE-2023-46998](https://github.com/soy-oreocato/CVE-2023-46998) :  ![starts](https://img.shields.io/github/stars/soy-oreocato/CVE-2023-46998.svg) ![forks](https://img.shields.io/github/forks/soy-oreocato/CVE-2023-46998.svg)

## CVE-2023-46980
 An issue in Best Courier Management System v.1.0 allows a remote attacker to execute arbitrary code and escalate privileges via a crafted script to the userID parameter.



- [https://github.com/sajaljat/CVE-2023-46980](https://github.com/sajaljat/CVE-2023-46980) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2023-46980.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2023-46980.svg)

## CVE-2023-46974
 Cross Site Scripting vulnerability in Best Courier Management System v.1.000 allows a remote attacker to execute arbitrary code via a crafted payload to the page parameter in the URL.



- [https://github.com/yte121/CVE-2023-46974](https://github.com/yte121/CVE-2023-46974) :  ![starts](https://img.shields.io/github/stars/yte121/CVE-2023-46974.svg) ![forks](https://img.shields.io/github/forks/yte121/CVE-2023-46974.svg)

## CVE-2023-46954
 SQL Injection vulnerability in Relativity ODA LLC RelativityOne v.12.1.537.3 Patch 2 and earlier allows a remote attacker to execute arbitrary code via the name parameter.



- [https://github.com/jakedmurphy1/CVE-2023-46954](https://github.com/jakedmurphy1/CVE-2023-46954) :  ![starts](https://img.shields.io/github/stars/jakedmurphy1/CVE-2023-46954.svg) ![forks](https://img.shields.io/github/forks/jakedmurphy1/CVE-2023-46954.svg)

## CVE-2023-46948
 A reflected Cross-Site Scripting (XSS) vulnerability was found on Temenos T24 Browser R19.40 that enables a remote attacker to execute arbitrary JavaScript code via the skin parameter in the about.jsp and genrequest.jsp components.



- [https://github.com/AzraelsBlade/CVE-2023-46948](https://github.com/AzraelsBlade/CVE-2023-46948) :  ![starts](https://img.shields.io/github/stars/AzraelsBlade/CVE-2023-46948.svg) ![forks](https://img.shields.io/github/forks/AzraelsBlade/CVE-2023-46948.svg)

## CVE-2023-46919
 Phlox com.phlox.simpleserver (aka Simple HTTP Server) 1.8 and com.phlox.simpleserver.plus (aka Simple HTTP Server PLUS) 1.8.1-plus have a hardcoded aKySWb2jjrr4dzkYXczKRt7K (AES) encryption key. An attacker with physical access to the application's source code or binary can extract this key & use it decrypt the TLS secret.



- [https://github.com/actuator/com.phlox.simpleserver](https://github.com/actuator/com.phlox.simpleserver) :  ![starts](https://img.shields.io/github/stars/actuator/com.phlox.simpleserver.svg) ![forks](https://img.shields.io/github/forks/actuator/com.phlox.simpleserver.svg)

## CVE-2023-46918
 Phlox com.phlox.simpleserver.plus (aka Simple HTTP Server PLUS) 1.8.1-plus has an Android manifest file that contains an entry with the android:allowBackup attribute set to true. This could be leveraged by an attacker with physical access to the device.



- [https://github.com/actuator/com.phlox.simpleserver](https://github.com/actuator/com.phlox.simpleserver) :  ![starts](https://img.shields.io/github/stars/actuator/com.phlox.simpleserver.svg) ![forks](https://img.shields.io/github/forks/actuator/com.phlox.simpleserver.svg)

## CVE-2023-46870
 extcap/nrf_sniffer_ble.py, extcap/nrf_sniffer_ble.sh, extcap/SnifferAPI/*.py in Nordic Semiconductor nRF Sniffer for Bluetooth LE 3.0.0, 3.1.0, 4.0.0, 4.1.0, and 4.1.1 have set incorrect file permission, which allows attackers to do code execution via modified bash and python scripts.



- [https://github.com/Chapoly1305/CVE-2023-46870](https://github.com/Chapoly1305/CVE-2023-46870) :  ![starts](https://img.shields.io/github/stars/Chapoly1305/CVE-2023-46870.svg) ![forks](https://img.shields.io/github/forks/Chapoly1305/CVE-2023-46870.svg)

## CVE-2023-46865
 /api/v1/company/upload-logo in CompanyController.php in crater through 6.0.6 allows a superadmin to execute arbitrary PHP code by placing this code into an image/png IDAT chunk of a Company Logo image.



- [https://github.com/asylumdx/Crater-CVE-2023-46865-RCE](https://github.com/asylumdx/Crater-CVE-2023-46865-RCE) :  ![starts](https://img.shields.io/github/stars/asylumdx/Crater-CVE-2023-46865-RCE.svg) ![forks](https://img.shields.io/github/forks/asylumdx/Crater-CVE-2023-46865-RCE.svg)

## CVE-2023-46818
 An issue was discovered in ISPConfig before 3.2.11p1. PHP code injection can be achieved in the language file editor by an admin if admin_allow_langedit is enabled.



- [https://github.com/ajdumanhug/CVE-2023-46818](https://github.com/ajdumanhug/CVE-2023-46818) :  ![starts](https://img.shields.io/github/stars/ajdumanhug/CVE-2023-46818.svg) ![forks](https://img.shields.io/github/forks/ajdumanhug/CVE-2023-46818.svg)

- [https://github.com/blindma1den/CVE-2023-46818-Exploit](https://github.com/blindma1den/CVE-2023-46818-Exploit) :  ![starts](https://img.shields.io/github/stars/blindma1den/CVE-2023-46818-Exploit.svg) ![forks](https://img.shields.io/github/forks/blindma1den/CVE-2023-46818-Exploit.svg)

- [https://github.com/rvizx/CVE-2023-46818](https://github.com/rvizx/CVE-2023-46818) :  ![starts](https://img.shields.io/github/stars/rvizx/CVE-2023-46818.svg) ![forks](https://img.shields.io/github/forks/rvizx/CVE-2023-46818.svg)

- [https://github.com/ajdumanhug/CVE-2022-42092](https://github.com/ajdumanhug/CVE-2022-42092) :  ![starts](https://img.shields.io/github/stars/ajdumanhug/CVE-2022-42092.svg) ![forks](https://img.shields.io/github/forks/ajdumanhug/CVE-2022-42092.svg)

- [https://github.com/engranaabubakar/CVE-2023-46818](https://github.com/engranaabubakar/CVE-2023-46818) :  ![starts](https://img.shields.io/github/stars/engranaabubakar/CVE-2023-46818.svg) ![forks](https://img.shields.io/github/forks/engranaabubakar/CVE-2023-46818.svg)

- [https://github.com/vulnerk0/CVE-2023-46818](https://github.com/vulnerk0/CVE-2023-46818) :  ![starts](https://img.shields.io/github/stars/vulnerk0/CVE-2023-46818.svg) ![forks](https://img.shields.io/github/forks/vulnerk0/CVE-2023-46818.svg)

## CVE-2023-46813
 An issue was discovered in the Linux kernel before 6.5.9, exploitable by local users with userspace access to MMIO registers. Incorrect access checking in the #VC handler and instruction emulation of the SEV-ES emulation of MMIO accesses could lead to arbitrary write access to kernel memory (and thus privilege escalation). This depends on a race condition through which userspace can replace an instruction before the #VC handler reads it.



- [https://github.com/Freax13/cve-2023-46813-poc](https://github.com/Freax13/cve-2023-46813-poc) :  ![starts](https://img.shields.io/github/stars/Freax13/cve-2023-46813-poc.svg) ![forks](https://img.shields.io/github/forks/Freax13/cve-2023-46813-poc.svg)

## CVE-2023-46805
 An authentication bypass vulnerability in the web component of Ivanti ICS 9.x, 22.x and Ivanti Policy Secure allows a remote attacker to access restricted resources by bypassing control checks.



- [https://github.com/duy-31/CVE-2023-46805_CVE-2024-21887](https://github.com/duy-31/CVE-2023-46805_CVE-2024-21887) :  ![starts](https://img.shields.io/github/stars/duy-31/CVE-2023-46805_CVE-2024-21887.svg) ![forks](https://img.shields.io/github/forks/duy-31/CVE-2023-46805_CVE-2024-21887.svg)

- [https://github.com/Chocapikk/CVE-2023-46805](https://github.com/Chocapikk/CVE-2023-46805) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-46805.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-46805.svg)

- [https://github.com/seajaysec/Ivanti-Connect-Around-Scan](https://github.com/seajaysec/Ivanti-Connect-Around-Scan) :  ![starts](https://img.shields.io/github/stars/seajaysec/Ivanti-Connect-Around-Scan.svg) ![forks](https://img.shields.io/github/forks/seajaysec/Ivanti-Connect-Around-Scan.svg)

- [https://github.com/yoryio/CVE-2023-46805](https://github.com/yoryio/CVE-2023-46805) :  ![starts](https://img.shields.io/github/stars/yoryio/CVE-2023-46805.svg) ![forks](https://img.shields.io/github/forks/yoryio/CVE-2023-46805.svg)

- [https://github.com/cbeek-r7/CVE-2023-46805](https://github.com/cbeek-r7/CVE-2023-46805) :  ![starts](https://img.shields.io/github/stars/cbeek-r7/CVE-2023-46805.svg) ![forks](https://img.shields.io/github/forks/cbeek-r7/CVE-2023-46805.svg)

- [https://github.com/raminkarimkhani1996/CVE-2023-46805_CVE-2024-21887](https://github.com/raminkarimkhani1996/CVE-2023-46805_CVE-2024-21887) :  ![starts](https://img.shields.io/github/stars/raminkarimkhani1996/CVE-2023-46805_CVE-2024-21887.svg) ![forks](https://img.shields.io/github/forks/raminkarimkhani1996/CVE-2023-46805_CVE-2024-21887.svg)

- [https://github.com/w2xim3/CVE-2023-46805](https://github.com/w2xim3/CVE-2023-46805) :  ![starts](https://img.shields.io/github/stars/w2xim3/CVE-2023-46805.svg) ![forks](https://img.shields.io/github/forks/w2xim3/CVE-2023-46805.svg)

- [https://github.com/rxwx/pulse-meter](https://github.com/rxwx/pulse-meter) :  ![starts](https://img.shields.io/github/stars/rxwx/pulse-meter.svg) ![forks](https://img.shields.io/github/forks/rxwx/pulse-meter.svg)

- [https://github.com/mickdec/CVE-2023-46805_CVE-2024-21887_scan_grouped](https://github.com/mickdec/CVE-2023-46805_CVE-2024-21887_scan_grouped) :  ![starts](https://img.shields.io/github/stars/mickdec/CVE-2023-46805_CVE-2024-21887_scan_grouped.svg) ![forks](https://img.shields.io/github/forks/mickdec/CVE-2023-46805_CVE-2024-21887_scan_grouped.svg)

## CVE-2023-46747
 Undisclosed requests may bypass configuration utility authentication, allowing an attacker with network access to the BIG-IP system through the management port and/or self IP addresses to execute arbitrary system commands.  Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated



- [https://github.com/W01fh4cker/CVE-2023-46747-RCE](https://github.com/W01fh4cker/CVE-2023-46747-RCE) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/CVE-2023-46747-RCE.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/CVE-2023-46747-RCE.svg)

- [https://github.com/AliBrTab/CVE-2023-46747-POC](https://github.com/AliBrTab/CVE-2023-46747-POC) :  ![starts](https://img.shields.io/github/stars/AliBrTab/CVE-2023-46747-POC.svg) ![forks](https://img.shields.io/github/forks/AliBrTab/CVE-2023-46747-POC.svg)

- [https://github.com/nvansluis/test_cve-2023-46747](https://github.com/nvansluis/test_cve-2023-46747) :  ![starts](https://img.shields.io/github/stars/nvansluis/test_cve-2023-46747.svg) ![forks](https://img.shields.io/github/forks/nvansluis/test_cve-2023-46747.svg)

- [https://github.com/maniak-academy/Mitigate-CVE-2023-46747](https://github.com/maniak-academy/Mitigate-CVE-2023-46747) :  ![starts](https://img.shields.io/github/stars/maniak-academy/Mitigate-CVE-2023-46747.svg) ![forks](https://img.shields.io/github/forks/maniak-academy/Mitigate-CVE-2023-46747.svg)

- [https://github.com/vidura2/cve-2023-46747](https://github.com/vidura2/cve-2023-46747) :  ![starts](https://img.shields.io/github/stars/vidura2/cve-2023-46747.svg) ![forks](https://img.shields.io/github/forks/vidura2/cve-2023-46747.svg)

- [https://github.com/RevoltSecurities/CVE-2023-46747](https://github.com/RevoltSecurities/CVE-2023-46747) :  ![starts](https://img.shields.io/github/stars/RevoltSecurities/CVE-2023-46747.svg) ![forks](https://img.shields.io/github/forks/RevoltSecurities/CVE-2023-46747.svg)

- [https://github.com/cediegreyhat/BigFinger](https://github.com/cediegreyhat/BigFinger) :  ![starts](https://img.shields.io/github/stars/cediegreyhat/BigFinger.svg) ![forks](https://img.shields.io/github/forks/cediegreyhat/BigFinger.svg)

- [https://github.com/fu2x2000/CVE-2023-46747](https://github.com/fu2x2000/CVE-2023-46747) :  ![starts](https://img.shields.io/github/stars/fu2x2000/CVE-2023-46747.svg) ![forks](https://img.shields.io/github/forks/fu2x2000/CVE-2023-46747.svg)

- [https://github.com/rainbowhatrkn/CVE-2023-46747-RCE](https://github.com/rainbowhatrkn/CVE-2023-46747-RCE) :  ![starts](https://img.shields.io/github/stars/rainbowhatrkn/CVE-2023-46747-RCE.svg) ![forks](https://img.shields.io/github/forks/rainbowhatrkn/CVE-2023-46747-RCE.svg)

## CVE-2023-46694
 Vtenext 21.02 allows an authenticated attacker to upload arbitrary files, potentially enabling them to execute remote commands. This flaw exists due to the application's failure to enforce proper authentication controls when accessing the Ckeditor file manager functionality.



- [https://github.com/invisiblebyte/CVE-2023-46694](https://github.com/invisiblebyte/CVE-2023-46694) :  ![starts](https://img.shields.io/github/stars/invisiblebyte/CVE-2023-46694.svg) ![forks](https://img.shields.io/github/forks/invisiblebyte/CVE-2023-46694.svg)

## CVE-2023-46615
 Deserialization of Untrusted Data vulnerability in Kalli Dan. KD Coming Soon.This issue affects KD Coming Soon: from n/a through 1.7.





- [https://github.com/RandomRobbieBF/CVE-2023-46615](https://github.com/RandomRobbieBF/CVE-2023-46615) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-46615.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-46615.svg)

## CVE-2023-46604
 The Java OpenWire protocol marshaller is vulnerable to Remote Code 
Execution. This vulnerability may allow a remote attacker with network 
access to either a Java-based OpenWire broker or client to run arbitrary
 shell commands by manipulating serialized class types in the OpenWire 
protocol to cause either the client or the broker (respectively) to 
instantiate any class on the classpath.

Users are recommended to upgrade
 both brokers and clients to version 5.15.16, 5.16.7, 5.17.6, or 5.18.3 
which fixes this issue.



- [https://github.com/X1r0z/ActiveMQ-RCE](https://github.com/X1r0z/ActiveMQ-RCE) :  ![starts](https://img.shields.io/github/stars/X1r0z/ActiveMQ-RCE.svg) ![forks](https://img.shields.io/github/forks/X1r0z/ActiveMQ-RCE.svg)

- [https://github.com/SaumyajeetDas/CVE-2023-46604-RCE-Reverse-Shell-Apache-ActiveMQ](https://github.com/SaumyajeetDas/CVE-2023-46604-RCE-Reverse-Shell-Apache-ActiveMQ) :  ![starts](https://img.shields.io/github/stars/SaumyajeetDas/CVE-2023-46604-RCE-Reverse-Shell-Apache-ActiveMQ.svg) ![forks](https://img.shields.io/github/forks/SaumyajeetDas/CVE-2023-46604-RCE-Reverse-Shell-Apache-ActiveMQ.svg)

- [https://github.com/ImuSpirit/ActiveMQ_RCE_Pro_Max](https://github.com/ImuSpirit/ActiveMQ_RCE_Pro_Max) :  ![starts](https://img.shields.io/github/stars/ImuSpirit/ActiveMQ_RCE_Pro_Max.svg) ![forks](https://img.shields.io/github/forks/ImuSpirit/ActiveMQ_RCE_Pro_Max.svg)

- [https://github.com/evkl1d/CVE-2023-46604](https://github.com/evkl1d/CVE-2023-46604) :  ![starts](https://img.shields.io/github/stars/evkl1d/CVE-2023-46604.svg) ![forks](https://img.shields.io/github/forks/evkl1d/CVE-2023-46604.svg)

- [https://github.com/Arlenhiack/ActiveMQ-RCE-Exploit](https://github.com/Arlenhiack/ActiveMQ-RCE-Exploit) :  ![starts](https://img.shields.io/github/stars/Arlenhiack/ActiveMQ-RCE-Exploit.svg) ![forks](https://img.shields.io/github/forks/Arlenhiack/ActiveMQ-RCE-Exploit.svg)

- [https://github.com/trganda/ActiveMQ-RCE](https://github.com/trganda/ActiveMQ-RCE) :  ![starts](https://img.shields.io/github/stars/trganda/ActiveMQ-RCE.svg) ![forks](https://img.shields.io/github/forks/trganda/ActiveMQ-RCE.svg)

- [https://github.com/duck-sec/CVE-2023-46604-ActiveMQ-RCE-pseudoshell](https://github.com/duck-sec/CVE-2023-46604-ActiveMQ-RCE-pseudoshell) :  ![starts](https://img.shields.io/github/stars/duck-sec/CVE-2023-46604-ActiveMQ-RCE-pseudoshell.svg) ![forks](https://img.shields.io/github/forks/duck-sec/CVE-2023-46604-ActiveMQ-RCE-pseudoshell.svg)

- [https://github.com/justdoit-cai/CVE-2023-46604-Apache-ActiveMQ-RCE-exp](https://github.com/justdoit-cai/CVE-2023-46604-Apache-ActiveMQ-RCE-exp) :  ![starts](https://img.shields.io/github/stars/justdoit-cai/CVE-2023-46604-Apache-ActiveMQ-RCE-exp.svg) ![forks](https://img.shields.io/github/forks/justdoit-cai/CVE-2023-46604-Apache-ActiveMQ-RCE-exp.svg)

- [https://github.com/vulncheck-oss/cve-2023-46604](https://github.com/vulncheck-oss/cve-2023-46604) :  ![starts](https://img.shields.io/github/stars/vulncheck-oss/cve-2023-46604.svg) ![forks](https://img.shields.io/github/forks/vulncheck-oss/cve-2023-46604.svg)

- [https://github.com/h3x3h0g/ActiveMQ-RCE-CVE-2023-46604-Write-up](https://github.com/h3x3h0g/ActiveMQ-RCE-CVE-2023-46604-Write-up) :  ![starts](https://img.shields.io/github/stars/h3x3h0g/ActiveMQ-RCE-CVE-2023-46604-Write-up.svg) ![forks](https://img.shields.io/github/forks/h3x3h0g/ActiveMQ-RCE-CVE-2023-46604-Write-up.svg)

- [https://github.com/infokek/activemq-honeypot](https://github.com/infokek/activemq-honeypot) :  ![starts](https://img.shields.io/github/stars/infokek/activemq-honeypot.svg) ![forks](https://img.shields.io/github/forks/infokek/activemq-honeypot.svg)

- [https://github.com/NKeshawarz/CVE-2023-46604-RCE](https://github.com/NKeshawarz/CVE-2023-46604-RCE) :  ![starts](https://img.shields.io/github/stars/NKeshawarz/CVE-2023-46604-RCE.svg) ![forks](https://img.shields.io/github/forks/NKeshawarz/CVE-2023-46604-RCE.svg)

- [https://github.com/LiritoShawshark/CVE-2023-46604_ActiveMQ_RCE_Recurrence](https://github.com/LiritoShawshark/CVE-2023-46604_ActiveMQ_RCE_Recurrence) :  ![starts](https://img.shields.io/github/stars/LiritoShawshark/CVE-2023-46604_ActiveMQ_RCE_Recurrence.svg) ![forks](https://img.shields.io/github/forks/LiritoShawshark/CVE-2023-46604_ActiveMQ_RCE_Recurrence.svg)

- [https://github.com/dcm2406/CVE-Lab](https://github.com/dcm2406/CVE-Lab) :  ![starts](https://img.shields.io/github/stars/dcm2406/CVE-Lab.svg) ![forks](https://img.shields.io/github/forks/dcm2406/CVE-Lab.svg)

- [https://github.com/Anekant-Singhai/Exploits](https://github.com/Anekant-Singhai/Exploits) :  ![starts](https://img.shields.io/github/stars/Anekant-Singhai/Exploits.svg) ![forks](https://img.shields.io/github/forks/Anekant-Singhai/Exploits.svg)

- [https://github.com/mrpentst/CVE-2023-46604](https://github.com/mrpentst/CVE-2023-46604) :  ![starts](https://img.shields.io/github/stars/mrpentst/CVE-2023-46604.svg) ![forks](https://img.shields.io/github/forks/mrpentst/CVE-2023-46604.svg)

- [https://github.com/pulentoski/CVE-2023-46604](https://github.com/pulentoski/CVE-2023-46604) :  ![starts](https://img.shields.io/github/stars/pulentoski/CVE-2023-46604.svg) ![forks](https://img.shields.io/github/forks/pulentoski/CVE-2023-46604.svg)

- [https://github.com/minhangxiaohui/ActiveMQ_CVE-2023-46604](https://github.com/minhangxiaohui/ActiveMQ_CVE-2023-46604) :  ![starts](https://img.shields.io/github/stars/minhangxiaohui/ActiveMQ_CVE-2023-46604.svg) ![forks](https://img.shields.io/github/forks/minhangxiaohui/ActiveMQ_CVE-2023-46604.svg)

- [https://github.com/stegano5/ExploitScript-CVE-2023-46604](https://github.com/stegano5/ExploitScript-CVE-2023-46604) :  ![starts](https://img.shields.io/github/stars/stegano5/ExploitScript-CVE-2023-46604.svg) ![forks](https://img.shields.io/github/forks/stegano5/ExploitScript-CVE-2023-46604.svg)

- [https://github.com/thinkycx/activemq-rce-cve-2023-46604](https://github.com/thinkycx/activemq-rce-cve-2023-46604) :  ![starts](https://img.shields.io/github/stars/thinkycx/activemq-rce-cve-2023-46604.svg) ![forks](https://img.shields.io/github/forks/thinkycx/activemq-rce-cve-2023-46604.svg)

- [https://github.com/nitzanoligo/CVE-2023-46604-demo](https://github.com/nitzanoligo/CVE-2023-46604-demo) :  ![starts](https://img.shields.io/github/stars/nitzanoligo/CVE-2023-46604-demo.svg) ![forks](https://img.shields.io/github/forks/nitzanoligo/CVE-2023-46604-demo.svg)

- [https://github.com/CCIEVoice2009/CVE-2023-46604](https://github.com/CCIEVoice2009/CVE-2023-46604) :  ![starts](https://img.shields.io/github/stars/CCIEVoice2009/CVE-2023-46604.svg) ![forks](https://img.shields.io/github/forks/CCIEVoice2009/CVE-2023-46604.svg)

- [https://github.com/dcm2406/CVE-2023-46604](https://github.com/dcm2406/CVE-2023-46604) :  ![starts](https://img.shields.io/github/stars/dcm2406/CVE-2023-46604.svg) ![forks](https://img.shields.io/github/forks/dcm2406/CVE-2023-46604.svg)

- [https://github.com/hh-hunter/cve-2023-46604](https://github.com/hh-hunter/cve-2023-46604) :  ![starts](https://img.shields.io/github/stars/hh-hunter/cve-2023-46604.svg) ![forks](https://img.shields.io/github/forks/hh-hunter/cve-2023-46604.svg)

- [https://github.com/vjayant93/CVE-2023-46604-POC](https://github.com/vjayant93/CVE-2023-46604-POC) :  ![starts](https://img.shields.io/github/stars/vjayant93/CVE-2023-46604-POC.svg) ![forks](https://img.shields.io/github/forks/vjayant93/CVE-2023-46604-POC.svg)

- [https://github.com/tomasmussi/activemq-cve-2023-46604](https://github.com/tomasmussi/activemq-cve-2023-46604) :  ![starts](https://img.shields.io/github/stars/tomasmussi/activemq-cve-2023-46604.svg) ![forks](https://img.shields.io/github/forks/tomasmussi/activemq-cve-2023-46604.svg)

- [https://github.com/Mudoleto/Broker_ApacheMQ](https://github.com/Mudoleto/Broker_ApacheMQ) :  ![starts](https://img.shields.io/github/stars/Mudoleto/Broker_ApacheMQ.svg) ![forks](https://img.shields.io/github/forks/Mudoleto/Broker_ApacheMQ.svg)

- [https://github.com/mranv/honeypot.rs](https://github.com/mranv/honeypot.rs) :  ![starts](https://img.shields.io/github/stars/mranv/honeypot.rs.svg) ![forks](https://img.shields.io/github/forks/mranv/honeypot.rs.svg)

## CVE-2023-46501
 An issue in BoltWire v.6.03 allows a remote attacker to obtain sensitive information via a crafted payload to the view and change admin password function.



- [https://github.com/Cyber-Wo0dy/CVE-2023-46501](https://github.com/Cyber-Wo0dy/CVE-2023-46501) :  ![starts](https://img.shields.io/github/stars/Cyber-Wo0dy/CVE-2023-46501.svg) ![forks](https://img.shields.io/github/forks/Cyber-Wo0dy/CVE-2023-46501.svg)

## CVE-2023-46478
 An issue in minCal v.1.0.0 allows a remote attacker to execute arbitrary code via a crafted script to the customer_data parameter.



- [https://github.com/mr-xmen786/CVE-2023-46478](https://github.com/mr-xmen786/CVE-2023-46478) :  ![starts](https://img.shields.io/github/stars/mr-xmen786/CVE-2023-46478.svg) ![forks](https://img.shields.io/github/forks/mr-xmen786/CVE-2023-46478.svg)

## CVE-2023-46474
 File Upload vulnerability PMB v.7.4.8 allows a remote attacker to execute arbitrary code and escalate privileges via a crafted PHP file uploaded to the start_import.php file.



- [https://github.com/Xn2/CVE-2023-46474](https://github.com/Xn2/CVE-2023-46474) :  ![starts](https://img.shields.io/github/stars/Xn2/CVE-2023-46474.svg) ![forks](https://img.shields.io/github/forks/Xn2/CVE-2023-46474.svg)

## CVE-2023-46456
 In GL.iNET GL-AR300M routers with firmware 3.216 it is possible to inject arbitrary shell commands through the OpenVPN client file upload functionality.



- [https://github.com/cyberaz0r/GL.iNet-Multiple-Vulnerabilities](https://github.com/cyberaz0r/GL.iNet-Multiple-Vulnerabilities) :  ![starts](https://img.shields.io/github/stars/cyberaz0r/GL.iNet-Multiple-Vulnerabilities.svg) ![forks](https://img.shields.io/github/forks/cyberaz0r/GL.iNet-Multiple-Vulnerabilities.svg)

## CVE-2023-46455
 In GL.iNET GL-AR300M routers with firmware v4.3.7 it is possible to write arbitrary files through a path traversal attack in the OpenVPN client file upload functionality.



- [https://github.com/cyberaz0r/GL.iNet-Multiple-Vulnerabilities](https://github.com/cyberaz0r/GL.iNet-Multiple-Vulnerabilities) :  ![starts](https://img.shields.io/github/stars/cyberaz0r/GL.iNet-Multiple-Vulnerabilities.svg) ![forks](https://img.shields.io/github/forks/cyberaz0r/GL.iNet-Multiple-Vulnerabilities.svg)

## CVE-2023-46454
 In GL.iNET GL-AR300M routers with firmware v4.3.7, it is possible to inject arbitrary shell commands through a crafted package name in the package information functionality.



- [https://github.com/cyberaz0r/GL.iNet-Multiple-Vulnerabilities](https://github.com/cyberaz0r/GL.iNet-Multiple-Vulnerabilities) :  ![starts](https://img.shields.io/github/stars/cyberaz0r/GL.iNet-Multiple-Vulnerabilities.svg) ![forks](https://img.shields.io/github/forks/cyberaz0r/GL.iNet-Multiple-Vulnerabilities.svg)

## CVE-2023-46453
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/0x1x02/GLiNet-Router-Auth-Bypass](https://github.com/0x1x02/GLiNet-Router-Auth-Bypass) :  ![starts](https://img.shields.io/github/stars/0x1x02/GLiNet-Router-Auth-Bypass.svg) ![forks](https://img.shields.io/github/forks/0x1x02/GLiNet-Router-Auth-Bypass.svg)

## CVE-2023-46451
 Best Courier Management System v1.0 is vulnerable to Cross Site Scripting (XSS) in the change username field.



- [https://github.com/sajaljat/CVE-2023-46451](https://github.com/sajaljat/CVE-2023-46451) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2023-46451.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2023-46451.svg)

## CVE-2023-46450
 Sourcecodester Free and Open Source inventory management system 1.0 is vulnerable to Cross Site Scripting (XSS) via the Add supplier function.



- [https://github.com/yte121/-CVE-2023-46450](https://github.com/yte121/-CVE-2023-46450) :  ![starts](https://img.shields.io/github/stars/yte121/-CVE-2023-46450.svg) ![forks](https://img.shields.io/github/forks/yte121/-CVE-2023-46450.svg)

## CVE-2023-46449
 Sourcecodester Free and Open Source inventory management system v1.0 is vulnerable to Incorrect Access Control. An arbitrary user can change the password of another user and takeover the account via IDOR in the password change function.



- [https://github.com/sajaljat/CVE-2023-46449](https://github.com/sajaljat/CVE-2023-46449) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2023-46449.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2023-46449.svg)

## CVE-2023-46447
 The POPS! Rebel application 5.0 for Android, in POPS! Rebel Bluetooth Glucose Monitoring System, sends unencrypted glucose measurements over BLE.



- [https://github.com/actuator/rebel](https://github.com/actuator/rebel) :  ![starts](https://img.shields.io/github/stars/actuator/rebel.svg) ![forks](https://img.shields.io/github/forks/actuator/rebel.svg)

## CVE-2023-46446
 An issue in AsyncSSH before 2.14.1 allows attackers to control the remote end of an SSH client session via packet injection/removal and shell emulation, aka a "Rogue Session Attack."



- [https://github.com/RUB-NDS/Terrapin-Artifacts](https://github.com/RUB-NDS/Terrapin-Artifacts) :  ![starts](https://img.shields.io/github/stars/RUB-NDS/Terrapin-Artifacts.svg) ![forks](https://img.shields.io/github/forks/RUB-NDS/Terrapin-Artifacts.svg)

## CVE-2023-46445
 An issue in AsyncSSH before 2.14.1 allows attackers to control the extension info message (RFC 8308) via a man-in-the-middle attack, aka a "Rogue Extension Negotiation."



- [https://github.com/RUB-NDS/Terrapin-Artifacts](https://github.com/RUB-NDS/Terrapin-Artifacts) :  ![starts](https://img.shields.io/github/stars/RUB-NDS/Terrapin-Artifacts.svg) ![forks](https://img.shields.io/github/forks/RUB-NDS/Terrapin-Artifacts.svg)

## CVE-2023-46442
 An infinite loop in the retrieveActiveBody function of Soot before v4.4.1 under Java 8 allows attackers to cause a Denial of Service (DoS).



- [https://github.com/JAckLosingHeart/CVE-2023-46442_POC](https://github.com/JAckLosingHeart/CVE-2023-46442_POC) :  ![starts](https://img.shields.io/github/stars/JAckLosingHeart/CVE-2023-46442_POC.svg) ![forks](https://img.shields.io/github/forks/JAckLosingHeart/CVE-2023-46442_POC.svg)

## CVE-2023-46404
 PCRS = 3.11 (d0de1e) “Questions” page and “Code editor” page are vulnerable to remote code execution (RCE) by escaping Python sandboxing.



- [https://github.com/windecks/CVE-2023-46404](https://github.com/windecks/CVE-2023-46404) :  ![starts](https://img.shields.io/github/stars/windecks/CVE-2023-46404.svg) ![forks](https://img.shields.io/github/forks/windecks/CVE-2023-46404.svg)

## CVE-2023-46344
 A vulnerability in Solar-Log Base 15 Firmware 6.0.1 Build 161, and possibly other Solar-Log Base products, allows an attacker to escalate their privileges by exploiting a stored cross-site scripting (XSS) vulnerability in the switch group function under /#ilang=DE&b=c_smartenergy_swgroups in the web portal. The vulnerability can be exploited to gain the rights of an installer or PM, which can then be used to gain administrative access to the web portal and execute further attacks. NOTE: The vendor states that this vulnerability has been fixed with 3.0.0-60 11.10.2013 for SL 200, 500, 1000 / not existing for SL 250, 300, 1200, 2000, SL 50 Gateway, SL Base.



- [https://github.com/vinnie1717/CVE-2023-46344](https://github.com/vinnie1717/CVE-2023-46344) :  ![starts](https://img.shields.io/github/stars/vinnie1717/CVE-2023-46344.svg) ![forks](https://img.shields.io/github/forks/vinnie1717/CVE-2023-46344.svg)

## CVE-2023-46304
 modules/Users/models/Module.php in Vtiger CRM 7.5.0 allows a remote authenticated attacker to run arbitrary PHP code because an unprotected endpoint allows them to write this code to the config.inc.php file (executed on every page load).



- [https://github.com/jselliott/CVE-2023-46304](https://github.com/jselliott/CVE-2023-46304) :  ![starts](https://img.shields.io/github/stars/jselliott/CVE-2023-46304.svg) ![forks](https://img.shields.io/github/forks/jselliott/CVE-2023-46304.svg)

## CVE-2023-46298
 Next.js before 13.4.20-canary.13 lacks a cache-control header and thus empty prefetch responses may sometimes be cached by a CDN, causing a denial of service to all users requesting the same URL via that CDN.



- [https://github.com/EarthAngel666/x-middleware-exploit](https://github.com/EarthAngel666/x-middleware-exploit) :  ![starts](https://img.shields.io/github/stars/EarthAngel666/x-middleware-exploit.svg) ![forks](https://img.shields.io/github/forks/EarthAngel666/x-middleware-exploit.svg)

## CVE-2023-46197
 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in supsystic.Com Popup by Supsystic allows Relative Path Traversal.This issue affects Popup by Supsystic: from n/a through 1.10.19.



- [https://github.com/RandomRobbieBF/CVE-2023-46197](https://github.com/RandomRobbieBF/CVE-2023-46197) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-46197.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-46197.svg)

## CVE-2023-46022
 SQL Injection vulnerability in delete.php in Code-Projects Blood Bank 1.0 allows attackers to run arbitrary SQL commands via the 'bid' parameter.



- [https://github.com/ersinerenler/CVE-2023-46022-Code-Projects-Blood-Bank-1.0-OOB-SQL-Injection-Vulnerability](https://github.com/ersinerenler/CVE-2023-46022-Code-Projects-Blood-Bank-1.0-OOB-SQL-Injection-Vulnerability) :  ![starts](https://img.shields.io/github/stars/ersinerenler/CVE-2023-46022-Code-Projects-Blood-Bank-1.0-OOB-SQL-Injection-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/ersinerenler/CVE-2023-46022-Code-Projects-Blood-Bank-1.0-OOB-SQL-Injection-Vulnerability.svg)

## CVE-2023-46021
 SQL Injection vulnerability in cancel.php in Code-Projects Blood Bank 1.0 allows attackers to run arbitrary commands via the 'reqid' parameter.



- [https://github.com/ersinerenler/CVE-2023-46021-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability](https://github.com/ersinerenler/CVE-2023-46021-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability) :  ![starts](https://img.shields.io/github/stars/ersinerenler/CVE-2023-46021-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/ersinerenler/CVE-2023-46021-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability.svg)

## CVE-2023-46020
 Cross Site Scripting (XSS) in updateprofile.php in Code-Projects Blood Bank 1.0 allows attackers to run arbitrary code via the 'rename', 'remail', 'rphone' and 'rcity' parameters.



- [https://github.com/ersinerenler/CVE-2023-46020-Code-Projects-Blood-Bank-1.0-Stored-Cross-Site-Scripting-Vulnerability](https://github.com/ersinerenler/CVE-2023-46020-Code-Projects-Blood-Bank-1.0-Stored-Cross-Site-Scripting-Vulnerability) :  ![starts](https://img.shields.io/github/stars/ersinerenler/CVE-2023-46020-Code-Projects-Blood-Bank-1.0-Stored-Cross-Site-Scripting-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/ersinerenler/CVE-2023-46020-Code-Projects-Blood-Bank-1.0-Stored-Cross-Site-Scripting-Vulnerability.svg)

## CVE-2023-46019
 Cross Site Scripting (XSS) vulnerability in abs.php in Code-Projects Blood Bank 1.0 allows attackers to run arbitrary code via the 'error' parameter.



- [https://github.com/ersinerenler/CVE-2023-46019-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability](https://github.com/ersinerenler/CVE-2023-46019-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability) :  ![starts](https://img.shields.io/github/stars/ersinerenler/CVE-2023-46019-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/ersinerenler/CVE-2023-46019-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability.svg)

## CVE-2023-46018
 SQL injection vulnerability in receiverReg.php in Code-Projects Blood Bank 1.0 \allows attackers to run arbitrary SQL commands via 'remail' parameter.



- [https://github.com/ersinerenler/CVE-2023-46018-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability](https://github.com/ersinerenler/CVE-2023-46018-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability) :  ![starts](https://img.shields.io/github/stars/ersinerenler/CVE-2023-46018-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/ersinerenler/CVE-2023-46018-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability.svg)

## CVE-2023-46017
 SQL Injection vulnerability in receiverLogin.php in Code-Projects Blood Bank 1.0 allows attackers to run arbitrary SQL commands via 'remail' and 'rpassword' parameters.



- [https://github.com/ersinerenler/CVE-2023-46017-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability](https://github.com/ersinerenler/CVE-2023-46017-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability) :  ![starts](https://img.shields.io/github/stars/ersinerenler/CVE-2023-46017-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/ersinerenler/CVE-2023-46017-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability.svg)

## CVE-2023-46016
 Cross Site Scripting (XSS) in abs.php in Code-Projects Blood Bank 1.0 allows attackers to run arbitrary code via the 'search' parameter in the application URL.



- [https://github.com/ersinerenler/CVE-2023-46016-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability](https://github.com/ersinerenler/CVE-2023-46016-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability) :  ![starts](https://img.shields.io/github/stars/ersinerenler/CVE-2023-46016-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/ersinerenler/CVE-2023-46016-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability.svg)

## CVE-2023-46015
 Cross Site Scripting (XSS) vulnerability in index.php in Code-Projects Blood Bank 1.0 allows attackers to run arbitrary code via 'msg' parameter in application URL.



- [https://github.com/ersinerenler/CVE-2023-46015-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability](https://github.com/ersinerenler/CVE-2023-46015-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability) :  ![starts](https://img.shields.io/github/stars/ersinerenler/CVE-2023-46015-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/ersinerenler/CVE-2023-46015-Code-Projects-Blood-Bank-1.0-Reflected-Cross-Site-Scripting-Vulnerability.svg)

## CVE-2023-46014
 SQL Injection vulnerability in hospitalLogin.php in Code-Projects Blood Bank 1.0 allows attackers to run arbitrary SQL commands via 'hemail' and 'hpassword' parameters.



- [https://github.com/ersinerenler/CVE-2023-46014-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability](https://github.com/ersinerenler/CVE-2023-46014-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability) :  ![starts](https://img.shields.io/github/stars/ersinerenler/CVE-2023-46014-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/ersinerenler/CVE-2023-46014-Code-Projects-Blood-Bank-1.0-SQL-Injection-Vulnerability.svg)

## CVE-2023-46012
 Buffer Overflow vulnerability LINKSYS EA7500 3.0.1.207964 allows a remote attacker to execute arbitrary code via an HTTP request to the IGD UPnP.



- [https://github.com/dest-3/CVE-2023-46012](https://github.com/dest-3/CVE-2023-46012) :  ![starts](https://img.shields.io/github/stars/dest-3/CVE-2023-46012.svg) ![forks](https://img.shields.io/github/forks/dest-3/CVE-2023-46012.svg)

## CVE-2023-46003
 I-doit pro 25 and below is vulnerable to Cross Site Scripting (XSS) via index.php.



- [https://github.com/leekenghwa/CVE-2023-46003](https://github.com/leekenghwa/CVE-2023-46003) :  ![starts](https://img.shields.io/github/stars/leekenghwa/CVE-2023-46003.svg) ![forks](https://img.shields.io/github/forks/leekenghwa/CVE-2023-46003.svg)

## CVE-2023-45992
 A vulnerability in the web-based interface of the RUCKUS Cloudpath product on version 5.12 build 5538 or before to could allow a remote, unauthenticated attacker to execute persistent XSS and CSRF attacks against a user of the admin management interface. A successful attack, combined with a certain admin activity, could allow the attacker to gain full admin privileges on the exploited system.



- [https://github.com/harry935/CVE-2023-45992](https://github.com/harry935/CVE-2023-45992) :  ![starts](https://img.shields.io/github/stars/harry935/CVE-2023-45992.svg) ![forks](https://img.shields.io/github/forks/harry935/CVE-2023-45992.svg)

## CVE-2023-45966
 umputun remark42 version 1.12.1 and before has a Blind Server-Side Request Forgery (SSRF) vulnerability.



- [https://github.com/jet-pentest/CVE-2023-45966](https://github.com/jet-pentest/CVE-2023-45966) :  ![starts](https://img.shields.io/github/stars/jet-pentest/CVE-2023-45966.svg) ![forks](https://img.shields.io/github/forks/jet-pentest/CVE-2023-45966.svg)

## CVE-2023-45878
 GibbonEdu Gibbon version 25.0.1 and before allows Arbitrary File Write because rubrics_visualise_saveAjax.phps does not require authentication. The endpoint accepts the img, path, and gibbonPersonID parameters. The img parameter is expected to be a base64 encoded image. If the path parameter is set, the defined path is used as the destination folder, concatenated with the absolute path of the installation directory. The content of the img parameter is base64 decoded and written to the defined file path. This allows creation of PHP files that permit Remote Code Execution (unauthenticated).



- [https://github.com/Can0I0Ever0Enter/CVE-2023-45878](https://github.com/Can0I0Ever0Enter/CVE-2023-45878) :  ![starts](https://img.shields.io/github/stars/Can0I0Ever0Enter/CVE-2023-45878.svg) ![forks](https://img.shields.io/github/forks/Can0I0Ever0Enter/CVE-2023-45878.svg)

- [https://github.com/ulricvbs/gibbonlms-filewrite_rce](https://github.com/ulricvbs/gibbonlms-filewrite_rce) :  ![starts](https://img.shields.io/github/stars/ulricvbs/gibbonlms-filewrite_rce.svg) ![forks](https://img.shields.io/github/forks/ulricvbs/gibbonlms-filewrite_rce.svg)

## CVE-2023-45866
 Bluetooth HID Hosts in BlueZ may permit an unauthenticated Peripheral role HID Device to initiate and establish an encrypted connection, and accept HID keyboard reports, potentially permitting injection of HID messages when no user interaction has occurred in the Central role to authorize such access. An example affected package is bluez 5.64-0ubuntu1 in Ubuntu 22.04LTS. NOTE: in some cases, a CVE-2020-0556 mitigation would have already addressed this Bluetooth HID Hosts issue.



- [https://github.com/pentestfunctions/BlueDucky](https://github.com/pentestfunctions/BlueDucky) :  ![starts](https://img.shields.io/github/stars/pentestfunctions/BlueDucky.svg) ![forks](https://img.shields.io/github/forks/pentestfunctions/BlueDucky.svg)

- [https://github.com/Danyw24/blueXploit](https://github.com/Danyw24/blueXploit) :  ![starts](https://img.shields.io/github/stars/Danyw24/blueXploit.svg) ![forks](https://img.shields.io/github/forks/Danyw24/blueXploit.svg)

- [https://github.com/Eason-zz/BluetoothDucky](https://github.com/Eason-zz/BluetoothDucky) :  ![starts](https://img.shields.io/github/stars/Eason-zz/BluetoothDucky.svg) ![forks](https://img.shields.io/github/forks/Eason-zz/BluetoothDucky.svg)

- [https://github.com/cisnarfu/Bluepop](https://github.com/cisnarfu/Bluepop) :  ![starts](https://img.shields.io/github/stars/cisnarfu/Bluepop.svg) ![forks](https://img.shields.io/github/forks/cisnarfu/Bluepop.svg)

- [https://github.com/jjjjjjjj987/cve-2023-45866-py](https://github.com/jjjjjjjj987/cve-2023-45866-py) :  ![starts](https://img.shields.io/github/stars/jjjjjjjj987/cve-2023-45866-py.svg) ![forks](https://img.shields.io/github/forks/jjjjjjjj987/cve-2023-45866-py.svg)

- [https://github.com/xG3nesis/RustyInjector](https://github.com/xG3nesis/RustyInjector) :  ![starts](https://img.shields.io/github/stars/xG3nesis/RustyInjector.svg) ![forks](https://img.shields.io/github/forks/xG3nesis/RustyInjector.svg)

## CVE-2023-45857
 An issue discovered in Axios 1.5.1 inadvertently reveals the confidential XSRF-TOKEN stored in cookies by including it in the HTTP header X-XSRF-TOKEN for every request made to any host allowing attackers to view sensitive information.



- [https://github.com/fuyuooumi1027/CVE-2023-45857-Demo](https://github.com/fuyuooumi1027/CVE-2023-45857-Demo) :  ![starts](https://img.shields.io/github/stars/fuyuooumi1027/CVE-2023-45857-Demo.svg) ![forks](https://img.shields.io/github/forks/fuyuooumi1027/CVE-2023-45857-Demo.svg)

- [https://github.com/valentin-panov/CVE-2023-45857](https://github.com/valentin-panov/CVE-2023-45857) :  ![starts](https://img.shields.io/github/stars/valentin-panov/CVE-2023-45857.svg) ![forks](https://img.shields.io/github/forks/valentin-panov/CVE-2023-45857.svg)

- [https://github.com/intercept6/CVE-2023-45857-Demo](https://github.com/intercept6/CVE-2023-45857-Demo) :  ![starts](https://img.shields.io/github/stars/intercept6/CVE-2023-45857-Demo.svg) ![forks](https://img.shields.io/github/forks/intercept6/CVE-2023-45857-Demo.svg)

## CVE-2023-45828
 Missing Authorization vulnerability in RumbleTalk Ltd RumbleTalk Live Group Chat allows Exploiting Incorrectly Configured Access Control Security Levels.This issue affects RumbleTalk Live Group Chat: from n/a through 6.2.5.



- [https://github.com/RandomRobbieBF/CVE-2023-45828](https://github.com/RandomRobbieBF/CVE-2023-45828) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-45828.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-45828.svg)

## CVE-2023-45779
 In the APEX module framework of AOSP, there is a possible malicious update to platform components due to improperly used crypto. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation. More details on this can be found in the referenced links.




- [https://github.com/metaredteam/rtx-cve-2023-45779](https://github.com/metaredteam/rtx-cve-2023-45779) :  ![starts](https://img.shields.io/github/stars/metaredteam/rtx-cve-2023-45779.svg) ![forks](https://img.shields.io/github/forks/metaredteam/rtx-cve-2023-45779.svg)

## CVE-2023-45777
 In checkKeyIntentParceledCorrectly of AccountManagerService.java, there is a possible way to launch arbitrary activities using system privileges due to Parcel Mismatch. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/michalbednarski/TheLastBundleMismatch](https://github.com/michalbednarski/TheLastBundleMismatch) :  ![starts](https://img.shields.io/github/stars/michalbednarski/TheLastBundleMismatch.svg) ![forks](https://img.shields.io/github/forks/michalbednarski/TheLastBundleMismatch.svg)

## CVE-2023-45657
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in POSIMYTH Nexter allows SQL Injection.This issue affects Nexter: from n/a through 2.0.3.





- [https://github.com/RandomRobbieBF/CVE-2023-45657](https://github.com/RandomRobbieBF/CVE-2023-45657) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-45657.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-45657.svg)

## CVE-2023-45542
 Cross Site Scripting vulnerability in mooSocial 3.1.8 allows a remote attacker to obtain sensitive information via a crafted script to the q parameter in the Search function.



- [https://github.com/ahrixia/CVE-2023-45542](https://github.com/ahrixia/CVE-2023-45542) :  ![starts](https://img.shields.io/github/stars/ahrixia/CVE-2023-45542.svg) ![forks](https://img.shields.io/github/forks/ahrixia/CVE-2023-45542.svg)

## CVE-2023-45540
 An issue in Jorani Leave Management System 1.0.3 allows a remote attacker to execute arbitrary HTML code via a crafted script to the comment field of the List of Leave requests page.



- [https://github.com/SoundarXploit/CVE-2023-45540](https://github.com/SoundarXploit/CVE-2023-45540) :  ![starts](https://img.shields.io/github/stars/SoundarXploit/CVE-2023-45540.svg) ![forks](https://img.shields.io/github/forks/SoundarXploit/CVE-2023-45540.svg)

## CVE-2023-45503
 SQL Injection vulnerability in Macrob7 Macs CMS 1.1.4f, allows remote attackers to execute arbitrary code, cause a denial of service (DoS), escalate privileges, and obtain sensitive information via crafted payload to resetPassword, forgotPasswordProcess, saveUser, saveRole, deleteUser, deleteRole, deleteComment, deleteUser, allowComment, saveRole, forgotPasswordProcess, resetPassword, saveUser, addComment, saveRole, and saveUser endpoints.



- [https://github.com/ally-petitt/CVE-2023-45503](https://github.com/ally-petitt/CVE-2023-45503) :  ![starts](https://img.shields.io/github/stars/ally-petitt/CVE-2023-45503.svg) ![forks](https://img.shields.io/github/forks/ally-petitt/CVE-2023-45503.svg)

## CVE-2023-45471
 The QAD Search Server is vulnerable to Stored Cross-Site Scripting (XSS) in versions up to, and including, 1.0.0.315 due to insufficient checks on indexes. This makes it possible for unauthenticated attackers to create a new index and inject a malicious web script into its name, that will execute whenever a user accesses the search page.



- [https://github.com/mehdibelhajamor/CVE-2023-45471](https://github.com/mehdibelhajamor/CVE-2023-45471) :  ![starts](https://img.shields.io/github/stars/mehdibelhajamor/CVE-2023-45471.svg) ![forks](https://img.shields.io/github/forks/mehdibelhajamor/CVE-2023-45471.svg)

## CVE-2023-45288
 An attacker may cause an HTTP/2 endpoint to read arbitrary amounts of header data by sending an excessive number of CONTINUATION frames. Maintaining HPACK state requires parsing and processing all HEADERS and CONTINUATION frames on a connection. When a request's headers exceed MaxHeaderBytes, no memory is allocated to store the excess headers, but they are still parsed. This permits an attacker to cause an HTTP/2 endpoint to read arbitrary amounts of header data, all associated with a request which is going to be rejected. These headers can include Huffman-encoded data which is significantly more expensive for the receiver to decode than for an attacker to send. The fix sets a limit on the amount of excess header frames we will process before closing a connection.



- [https://github.com/hex0punk/cont-flood-poc](https://github.com/hex0punk/cont-flood-poc) :  ![starts](https://img.shields.io/github/stars/hex0punk/cont-flood-poc.svg) ![forks](https://img.shields.io/github/forks/hex0punk/cont-flood-poc.svg)

## CVE-2023-45239
 A lack of input validation exists in tac_plus prior to commit 4fdf178 which, when pre or post auth commands are enabled, allows an attacker who can control the username, rem-addr, or NAC address sent to tac_plus to inject shell commands and gain remote code execution on the tac_plus server.



- [https://github.com/takeshixx/tac_plus-pre-auth-rce](https://github.com/takeshixx/tac_plus-pre-auth-rce) :  ![starts](https://img.shields.io/github/stars/takeshixx/tac_plus-pre-auth-rce.svg) ![forks](https://img.shields.io/github/forks/takeshixx/tac_plus-pre-auth-rce.svg)

## CVE-2023-45185
 IBM i Access Client Solutions 1.1.2 through 1.1.4 and 1.1.4.3 through 1.1.9.3 could allow an attacker to execute remote code.  Due to improper authority checks the attacker could perform operations on the PC under the user's authority.  IBM X-Force ID:  268273.



- [https://github.com/afine-com/CVE-2023-45185](https://github.com/afine-com/CVE-2023-45185) :  ![starts](https://img.shields.io/github/stars/afine-com/CVE-2023-45185.svg) ![forks](https://img.shields.io/github/forks/afine-com/CVE-2023-45185.svg)

## CVE-2023-45184
 IBM i Access Client Solutions 1.1.2 through 1.1.4 and 1.1.4.3 through 1.1.9.3 could allow an attacker to obtain a decryption key due to improper authority checks.  IBM X-Force ID:  268270.



- [https://github.com/afine-com/CVE-2023-45184](https://github.com/afine-com/CVE-2023-45184) :  ![starts](https://img.shields.io/github/stars/afine-com/CVE-2023-45184.svg) ![forks](https://img.shields.io/github/forks/afine-com/CVE-2023-45184.svg)

## CVE-2023-45182
 
IBM i Access Client Solutions 1.1.2 through 1.1.4 and 1.1.4.3 through 1.1.9.3 is vulnerable to having its key for an encrypted password decoded. By somehow gaining access to the encrypted password, a local attacker could exploit this vulnerability to obtain the password to other systems. IBM X-Force ID: 268265.





- [https://github.com/afine-com/CVE-2023-45182](https://github.com/afine-com/CVE-2023-45182) :  ![starts](https://img.shields.io/github/stars/afine-com/CVE-2023-45182.svg) ![forks](https://img.shields.io/github/forks/afine-com/CVE-2023-45182.svg)

## CVE-2023-45158
 An OS command injection vulnerability exists in web2py 2.24.1 and earlier. When the product is configured to use notifySendHandler for logging (not the default configuration), a crafted web request may execute an arbitrary OS command on the web server using the product.



- [https://github.com/Evan-Zhangyf/CVE-2023-45158](https://github.com/Evan-Zhangyf/CVE-2023-45158) :  ![starts](https://img.shields.io/github/stars/Evan-Zhangyf/CVE-2023-45158.svg) ![forks](https://img.shields.io/github/forks/Evan-Zhangyf/CVE-2023-45158.svg)

## CVE-2023-45131
 Discourse is an open source platform for community discussion. New chat messages can be read by making an unauthenticated POST request to MessageBus. This issue is patched in the 3.1.1 stable and 3.2.0.beta2 versions of Discourse. Users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/ibrahmsql/CVE-2023-45131](https://github.com/ibrahmsql/CVE-2023-45131) :  ![starts](https://img.shields.io/github/stars/ibrahmsql/CVE-2023-45131.svg) ![forks](https://img.shields.io/github/forks/ibrahmsql/CVE-2023-45131.svg)

## CVE-2023-44976
 Hangzhou Shunwang Rentdrv2 before 2024-12-24 allows local users to terminate EDR processes and possibly have unspecified other impact via DeviceIoControl with control code 0x22E010, as exploited in the wild in October 2023.



- [https://github.com/keowu/BadRentdrv2](https://github.com/keowu/BadRentdrv2) :  ![starts](https://img.shields.io/github/stars/keowu/BadRentdrv2.svg) ![forks](https://img.shields.io/github/forks/keowu/BadRentdrv2.svg)

## CVE-2023-44962
 File Upload vulnerability in Koha Library Software 23.05.04 and before allows a remote attacker to read arbitrary files via the upload-cover-image.pl component.



- [https://github.com/LadyDarwe/Links.a](https://github.com/LadyDarwe/Links.a) :  ![starts](https://img.shields.io/github/stars/LadyDarwe/Links.a.svg) ![forks](https://img.shields.io/github/forks/LadyDarwe/Links.a.svg)

## CVE-2023-44813
 Cross Site Scripting (XSS) vulnerability in mooSocial v.3.1.8 allows a remote attacker to execute arbitrary code via a crafted payload to the mode parameter of the invite friend login function.



- [https://github.com/ahrixia/CVE-2023-44813](https://github.com/ahrixia/CVE-2023-44813) :  ![starts](https://img.shields.io/github/stars/ahrixia/CVE-2023-44813.svg) ![forks](https://img.shields.io/github/forks/ahrixia/CVE-2023-44813.svg)

## CVE-2023-44812
 Cross Site Scripting (XSS) vulnerability in mooSocial v.3.1.8 allows a remote attacker to execute arbitrary code via a crafted payload to the admin_redirect_url parameter of the user login function.



- [https://github.com/ahrixia/CVE-2023-44812](https://github.com/ahrixia/CVE-2023-44812) :  ![starts](https://img.shields.io/github/stars/ahrixia/CVE-2023-44812.svg) ![forks](https://img.shields.io/github/forks/ahrixia/CVE-2023-44812.svg)

## CVE-2023-44811
 Cross Site Request Forgery (CSRF) vulnerability in MooSocial v.3.1.8 allows a remote attacker to execute arbitrary code and obtain sensitive information via the admin Password Change Function.



- [https://github.com/ahrixia/CVE-2023-44811](https://github.com/ahrixia/CVE-2023-44811) :  ![starts](https://img.shields.io/github/stars/ahrixia/CVE-2023-44811.svg) ![forks](https://img.shields.io/github/forks/ahrixia/CVE-2023-44811.svg)

## CVE-2023-44771
 A Cross-Site Scripting (XSS) vulnerability in Zenario CMS v.9.4.59197 allows a local attacker to execute arbitrary code via a crafted script to the Page Layout.



- [https://github.com/sromanhu/CVE-2023-44771_ZenarioCMS--Stored-XSS---Page-Layout](https://github.com/sromanhu/CVE-2023-44771_ZenarioCMS--Stored-XSS---Page-Layout) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44771_ZenarioCMS--Stored-XSS---Page-Layout.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44771_ZenarioCMS--Stored-XSS---Page-Layout.svg)

## CVE-2023-44770
 A Cross-Site Scripting (XSS) vulnerability in Zenario CMS v.9.4.59197 allows an attacker to execute arbitrary code via a crafted script to the Organizer - Spare alias.



- [https://github.com/sromanhu/CVE-2023-44770_ZenarioCMS--Reflected-XSS---Organizer-Alias](https://github.com/sromanhu/CVE-2023-44770_ZenarioCMS--Reflected-XSS---Organizer-Alias) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44770_ZenarioCMS--Reflected-XSS---Organizer-Alias.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44770_ZenarioCMS--Reflected-XSS---Organizer-Alias.svg)

## CVE-2023-44769
 A Cross-Site Scripting (XSS) vulnerability in Zenario CMS v.9.4.59197 allows a local attacker to execute arbitrary code via a crafted script to the Spare aliases from Alias.



- [https://github.com/sromanhu/CVE-2023-44769_ZenarioCMS--Reflected-XSS---Alias](https://github.com/sromanhu/CVE-2023-44769_ZenarioCMS--Reflected-XSS---Alias) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44769_ZenarioCMS--Reflected-XSS---Alias.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44769_ZenarioCMS--Reflected-XSS---Alias.svg)

## CVE-2023-44767
 A File upload vulnerability in RiteCMS 3.0 allows a local attacker to upload a SVG file with XSS content.



- [https://github.com/sromanhu/CVE-2023-44767_RiteCMS-File-Upload--XSS---Filemanager](https://github.com/sromanhu/CVE-2023-44767_RiteCMS-File-Upload--XSS---Filemanager) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44767_RiteCMS-File-Upload--XSS---Filemanager.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44767_RiteCMS-File-Upload--XSS---Filemanager.svg)

## CVE-2023-44766
 A Cross Site Scripting (XSS) vulnerability in Concrete CMS v.9.2.1 allows an attacker to execute arbitrary code via a crafted script to the SEO - Extra from Page Settings. NOTE: the vendor disputes this because this SEO-related header change can only be made by an admin, and allowing an admin to place JavaScript there is an intentional customization feature.



- [https://github.com/sromanhu/CVE-2023-44766_ConcreteCMS-Stored-XSS---SEO](https://github.com/sromanhu/CVE-2023-44766_ConcreteCMS-Stored-XSS---SEO) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44766_ConcreteCMS-Stored-XSS---SEO.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44766_ConcreteCMS-Stored-XSS---SEO.svg)

## CVE-2023-44765
 A Cross Site Scripting (XSS) vulnerability in Concrete CMS versions 8.5.12 and below, and 9.0 through 9.2.1 allows an attacker to execute arbitrary code via a crafted script to Plural Handle of the Data Objects from System & Settings.



- [https://github.com/sromanhu/CVE-2023-44765_ConcreteCMS-Stored-XSS---Associations](https://github.com/sromanhu/CVE-2023-44765_ConcreteCMS-Stored-XSS---Associations) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44765_ConcreteCMS-Stored-XSS---Associations.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44765_ConcreteCMS-Stored-XSS---Associations.svg)

## CVE-2023-44764
 A Cross Site Scripting (XSS) vulnerability in Concrete CMS before 9.2.3 exists via the Name parameter during installation (aka Site of Installation or Settings).



- [https://github.com/sromanhu/CVE-2023-44764_ConcreteCMS-Stored-XSS---Site_Installation](https://github.com/sromanhu/CVE-2023-44764_ConcreteCMS-Stored-XSS---Site_Installation) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44764_ConcreteCMS-Stored-XSS---Site_Installation.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44764_ConcreteCMS-Stored-XSS---Site_Installation.svg)

## CVE-2023-44763
 Concrete CMS v9.2.1 is affected by an Arbitrary File Upload vulnerability via a Thumbnail file upload, which allows Cross-Site Scripting (XSS). NOTE: the vendor's position is that a customer is supposed to know that "pdf" should be excluded from the allowed file types, even though pdf is one of the allowed file types in the default configuration.



- [https://github.com/sromanhu/CVE-2023-44763_ConcreteCMS-Arbitrary-file-upload-Thumbnail](https://github.com/sromanhu/CVE-2023-44763_ConcreteCMS-Arbitrary-file-upload-Thumbnail) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44763_ConcreteCMS-Arbitrary-file-upload-Thumbnail.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44763_ConcreteCMS-Arbitrary-file-upload-Thumbnail.svg)

## CVE-2023-44762
 A Cross Site Scripting (XSS) vulnerability in Concrete CMS from versions 9.2.0 to 9.2.2 allows an attacker to execute arbitrary code via a crafted script to the Tags from Settings - Tags.



- [https://github.com/sromanhu/CVE-2023-44762_ConcreteCMS-Reflected-XSS---Tags](https://github.com/sromanhu/CVE-2023-44762_ConcreteCMS-Reflected-XSS---Tags) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44762_ConcreteCMS-Reflected-XSS---Tags.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44762_ConcreteCMS-Reflected-XSS---Tags.svg)

## CVE-2023-44761
 Multiple Cross Site Scripting (XSS) vulnerabilities in Concrete CMS versions affected to 8.5.13 and below, and 9.0.0 through 9.2.1 allow a local attacker to execute arbitrary code via a crafted script to the Forms of the Data objects.



- [https://github.com/sromanhu/CVE-2023-44761_ConcreteCMS-Stored-XSS---Forms](https://github.com/sromanhu/CVE-2023-44761_ConcreteCMS-Stored-XSS---Forms) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44761_ConcreteCMS-Stored-XSS---Forms.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44761_ConcreteCMS-Stored-XSS---Forms.svg)

## CVE-2023-44760
 Multiple Cross Site Scripting (XSS) vulnerabilities in Concrete CMS v.9.2.1 allow an attacker to execute arbitrary code via a crafted script to the Header and Footer Tracking Codes of the SEO & Statistics. NOTE: the vendor disputes this because these header/footer changes can only be made by an admin, and allowing an admin to place JavaScript there is an intentional customization feature. Also, the exploitation method claimed by "sromanhu" does not provide any access to a Concrete CMS session, because the Concrete CMS session cookie is configured as HttpOnly.



- [https://github.com/sromanhu/CVE-2023-44760_ConcreteCMS-Stored-XSS---TrackingCodes](https://github.com/sromanhu/CVE-2023-44760_ConcreteCMS-Stored-XSS---TrackingCodes) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44760_ConcreteCMS-Stored-XSS---TrackingCodes.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44760_ConcreteCMS-Stored-XSS---TrackingCodes.svg)

## CVE-2023-44758
 GDidees CMS 3.0 is affected by a Cross-Site Scripting (XSS) vulnerability that allows attackers to execute arbitrary code via a crafted payload to the Page Title.



- [https://github.com/sromanhu/CVE-2023-44758_GDidees-CMS-Stored-XSS---Title](https://github.com/sromanhu/CVE-2023-44758_GDidees-CMS-Stored-XSS---Title) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-44758_GDidees-CMS-Stored-XSS---Title.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-44758_GDidees-CMS-Stored-XSS---Title.svg)

## CVE-2023-44487
 The HTTP/2 protocol allows a denial of service (server resource consumption) because request cancellation can reset many streams quickly, as exploited in the wild in August through October 2023.



- [https://github.com/bcdannyboy/CVE-2023-44487](https://github.com/bcdannyboy/CVE-2023-44487) :  ![starts](https://img.shields.io/github/stars/bcdannyboy/CVE-2023-44487.svg) ![forks](https://img.shields.io/github/forks/bcdannyboy/CVE-2023-44487.svg)

- [https://github.com/secengjeff/rapidresetclient](https://github.com/secengjeff/rapidresetclient) :  ![starts](https://img.shields.io/github/stars/secengjeff/rapidresetclient.svg) ![forks](https://img.shields.io/github/forks/secengjeff/rapidresetclient.svg)

- [https://github.com/imabee101/CVE-2023-44487](https://github.com/imabee101/CVE-2023-44487) :  ![starts](https://img.shields.io/github/stars/imabee101/CVE-2023-44487.svg) ![forks](https://img.shields.io/github/forks/imabee101/CVE-2023-44487.svg)

- [https://github.com/studiogangster/CVE-2023-44487](https://github.com/studiogangster/CVE-2023-44487) :  ![starts](https://img.shields.io/github/stars/studiogangster/CVE-2023-44487.svg) ![forks](https://img.shields.io/github/forks/studiogangster/CVE-2023-44487.svg)

- [https://github.com/nxenon/cve-2023-44487](https://github.com/nxenon/cve-2023-44487) :  ![starts](https://img.shields.io/github/stars/nxenon/cve-2023-44487.svg) ![forks](https://img.shields.io/github/forks/nxenon/cve-2023-44487.svg)

- [https://github.com/threatlabindonesia/CVE-2023-44487-HTTP-2-Rapid-Reset-Exploit-PoC](https://github.com/threatlabindonesia/CVE-2023-44487-HTTP-2-Rapid-Reset-Exploit-PoC) :  ![starts](https://img.shields.io/github/stars/threatlabindonesia/CVE-2023-44487-HTTP-2-Rapid-Reset-Exploit-PoC.svg) ![forks](https://img.shields.io/github/forks/threatlabindonesia/CVE-2023-44487-HTTP-2-Rapid-Reset-Exploit-PoC.svg)

- [https://github.com/ndrscodes/http2-rst-stream-attacker](https://github.com/ndrscodes/http2-rst-stream-attacker) :  ![starts](https://img.shields.io/github/stars/ndrscodes/http2-rst-stream-attacker.svg) ![forks](https://img.shields.io/github/forks/ndrscodes/http2-rst-stream-attacker.svg)

- [https://github.com/ReToCode/golang-CVE-2023-44487](https://github.com/ReToCode/golang-CVE-2023-44487) :  ![starts](https://img.shields.io/github/stars/ReToCode/golang-CVE-2023-44487.svg) ![forks](https://img.shields.io/github/forks/ReToCode/golang-CVE-2023-44487.svg)

- [https://github.com/zanks08/cve-2023-44487-demo](https://github.com/zanks08/cve-2023-44487-demo) :  ![starts](https://img.shields.io/github/stars/zanks08/cve-2023-44487-demo.svg) ![forks](https://img.shields.io/github/forks/zanks08/cve-2023-44487-demo.svg)

- [https://github.com/pabloec20/rapidreset](https://github.com/pabloec20/rapidreset) :  ![starts](https://img.shields.io/github/stars/pabloec20/rapidreset.svg) ![forks](https://img.shields.io/github/forks/pabloec20/rapidreset.svg)

- [https://github.com/TYuan0816/cve-2023-44487](https://github.com/TYuan0816/cve-2023-44487) :  ![starts](https://img.shields.io/github/stars/TYuan0816/cve-2023-44487.svg) ![forks](https://img.shields.io/github/forks/TYuan0816/cve-2023-44487.svg)

- [https://github.com/sn130hk/CVE-2023-44487](https://github.com/sn130hk/CVE-2023-44487) :  ![starts](https://img.shields.io/github/stars/sn130hk/CVE-2023-44487.svg) ![forks](https://img.shields.io/github/forks/sn130hk/CVE-2023-44487.svg)

- [https://github.com/ByteHackr/CVE-2023-44487](https://github.com/ByteHackr/CVE-2023-44487) :  ![starts](https://img.shields.io/github/stars/ByteHackr/CVE-2023-44487.svg) ![forks](https://img.shields.io/github/forks/ByteHackr/CVE-2023-44487.svg)

- [https://github.com/sigridou/CVE-2023-44487-](https://github.com/sigridou/CVE-2023-44487-) :  ![starts](https://img.shields.io/github/stars/sigridou/CVE-2023-44487-.svg) ![forks](https://img.shields.io/github/forks/sigridou/CVE-2023-44487-.svg)

- [https://github.com/gmh5225/CVE_2023_44487-Rapid_Reset](https://github.com/gmh5225/CVE_2023_44487-Rapid_Reset) :  ![starts](https://img.shields.io/github/stars/gmh5225/CVE_2023_44487-Rapid_Reset.svg) ![forks](https://img.shields.io/github/forks/gmh5225/CVE_2023_44487-Rapid_Reset.svg)

- [https://github.com/moften/CVE-2023-44487-HTTP-2-Rapid-Reset-Attack](https://github.com/moften/CVE-2023-44487-HTTP-2-Rapid-Reset-Attack) :  ![starts](https://img.shields.io/github/stars/moften/CVE-2023-44487-HTTP-2-Rapid-Reset-Attack.svg) ![forks](https://img.shields.io/github/forks/moften/CVE-2023-44487-HTTP-2-Rapid-Reset-Attack.svg)

## CVE-2023-44452
 Linux Mint Xreader CBT File Parsing Argument Injection Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Mint Xreader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the parsing of CBT files. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current user. Was ZDI-CAN-22132.



- [https://github.com/febinrev/atril_cbt-inject-exploit](https://github.com/febinrev/atril_cbt-inject-exploit) :  ![starts](https://img.shields.io/github/stars/febinrev/atril_cbt-inject-exploit.svg) ![forks](https://img.shields.io/github/forks/febinrev/atril_cbt-inject-exploit.svg)

## CVE-2023-44451
 Linux Mint Xreader EPUB File Parsing Directory Traversal Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Mint Xreader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the parsing of EPUB files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user. Was ZDI-CAN-21897.



- [https://github.com/febinrev/slippy-book-exploit](https://github.com/febinrev/slippy-book-exploit) :  ![starts](https://img.shields.io/github/stars/febinrev/slippy-book-exploit.svg) ![forks](https://img.shields.io/github/forks/febinrev/slippy-book-exploit.svg)

## CVE-2023-44372
 Adobe Acrobat Reader versions 23.006.20360 (and earlier) and 20.005.30524 (and earlier) are affected by a Use After Free vulnerability that could result in arbitrary code execution in the context of the current user. Exploitation of this issue requires user interaction in that a victim must open a malicious file.



- [https://github.com/SpiralBL0CK/cve2023-44372](https://github.com/SpiralBL0CK/cve2023-44372) :  ![starts](https://img.shields.io/github/stars/SpiralBL0CK/cve2023-44372.svg) ![forks](https://img.shields.io/github/forks/SpiralBL0CK/cve2023-44372.svg)

## CVE-2023-44061
 File Upload vulnerability in Simple and Nice Shopping Cart Script v.1.0 allows a remote attacker to execute arbitrary code via the upload function in the edit profile component.



- [https://github.com/SoundarXploit/CVE-2023-44061](https://github.com/SoundarXploit/CVE-2023-44061) :  ![starts](https://img.shields.io/github/stars/SoundarXploit/CVE-2023-44061.svg) ![forks](https://img.shields.io/github/forks/SoundarXploit/CVE-2023-44061.svg)

## CVE-2023-43955
 The com.phlox.tvwebbrowser TV Bro application through 2.0.0 for Android mishandles external intents through WebView. This allows attackers to execute arbitrary code, create arbitrary files. and perform arbitrary downloads via JavaScript that uses takeBlobDownloadData.



- [https://github.com/actuator/com.phlox.tvwebbrowser](https://github.com/actuator/com.phlox.tvwebbrowser) :  ![starts](https://img.shields.io/github/stars/actuator/com.phlox.tvwebbrowser.svg) ![forks](https://img.shields.io/github/forks/actuator/com.phlox.tvwebbrowser.svg)

## CVE-2023-43879
 Rite CMS 3.0 has a Cross-Site scripting (XSS) vulnerability that allows attackers to execute arbitrary code via a crafted payload into the Global Content Blocks in the Administration Menu.



- [https://github.com/sromanhu/CVE-2023-43879-RiteCMS-Stored-XSS---GlobalContent](https://github.com/sromanhu/CVE-2023-43879-RiteCMS-Stored-XSS---GlobalContent) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43879-RiteCMS-Stored-XSS---GlobalContent.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43879-RiteCMS-Stored-XSS---GlobalContent.svg)

## CVE-2023-43878
 Rite CMS 3.0 has Multiple Cross-Site scripting (XSS) vulnerabilities that allow attackers to execute arbitrary code via a crafted payload into the Main Menu Items in the Administration Menu.



- [https://github.com/sromanhu/CVE-2023-43878-RiteCMS-Stored-XSS---MainMenu](https://github.com/sromanhu/CVE-2023-43878-RiteCMS-Stored-XSS---MainMenu) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43878-RiteCMS-Stored-XSS---MainMenu.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43878-RiteCMS-Stored-XSS---MainMenu.svg)

## CVE-2023-43877
 Rite CMS 3.0 has Multiple Cross-Site scripting (XSS) vulnerabilities that allow attackers to execute arbitrary code via a payload crafted in the Home Page fields in the Administration menu.



- [https://github.com/sromanhu/CVE-2023-43877-RiteCMS-Stored-XSS---Home](https://github.com/sromanhu/CVE-2023-43877-RiteCMS-Stored-XSS---Home) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43877-RiteCMS-Stored-XSS---Home.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43877-RiteCMS-Stored-XSS---Home.svg)

## CVE-2023-43876
 A Cross-Site Scripting (XSS) vulnerability in installation of October v.3.4.16 allows an attacker to execute arbitrary web scripts via a crafted payload injected into the dbhost field.



- [https://github.com/sromanhu/CVE-2023-43876-October-CMS-Reflected-XSS---Installation](https://github.com/sromanhu/CVE-2023-43876-October-CMS-Reflected-XSS---Installation) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43876-October-CMS-Reflected-XSS---Installation.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43876-October-CMS-Reflected-XSS---Installation.svg)

## CVE-2023-43875
 Multiple Cross-Site Scripting (XSS) vulnerabilities in installation of Subrion CMS v.4.2.1 allows a local attacker to execute arbitrary web scripts via a crafted payload injected into the dbhost, dbname, dbuser, adminusername and adminemail.



- [https://github.com/sromanhu/CVE-2023-43875-Subrion-CMS-Reflected-XSS---Installation](https://github.com/sromanhu/CVE-2023-43875-Subrion-CMS-Reflected-XSS---Installation) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43875-Subrion-CMS-Reflected-XSS---Installation.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43875-Subrion-CMS-Reflected-XSS---Installation.svg)

## CVE-2023-43874
 Multiple Cross Site Scripting (XSS) vulnerability in e017 CMS v.2.3.2 allows a local attacker to execute arbitrary code via a crafted script to the Copyright and Author fields in the Meta & Custom Tags Menu.



- [https://github.com/sromanhu/CVE-2023-43874-e107-CMS-Stored-XSS---MetaCustomTags](https://github.com/sromanhu/CVE-2023-43874-e107-CMS-Stored-XSS---MetaCustomTags) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43874-e107-CMS-Stored-XSS---MetaCustomTags.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43874-e107-CMS-Stored-XSS---MetaCustomTags.svg)

## CVE-2023-43873
 A Cross Site Scripting (XSS) vulnerability in e017 CMS v.2.3.2 allows a local attacker to execute arbitrary code via a crafted script to the Name filed in the Manage Menu.



- [https://github.com/sromanhu/CVE-2023-43873-e107-CMS-Stored-XSS---Manage](https://github.com/sromanhu/CVE-2023-43873-e107-CMS-Stored-XSS---Manage) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43873-e107-CMS-Stored-XSS---Manage.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43873-e107-CMS-Stored-XSS---Manage.svg)

## CVE-2023-43872
 A File upload vulnerability in CMSmadesimple v.2.2.18 allows a local attacker to upload a pdf file with hidden Cross Site Scripting (XSS).



- [https://github.com/sromanhu/CVE-2023-43872-CMSmadesimple-Arbitrary-File-Upload--XSS---File-Manager](https://github.com/sromanhu/CVE-2023-43872-CMSmadesimple-Arbitrary-File-Upload--XSS---File-Manager) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43872-CMSmadesimple-Arbitrary-File-Upload--XSS---File-Manager.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43872-CMSmadesimple-Arbitrary-File-Upload--XSS---File-Manager.svg)

## CVE-2023-43871
 A File upload vulnerability in WBCE v.1.6.1 allows a local attacker to upload a pdf file with hidden Cross Site Scripting (XSS).



- [https://github.com/sromanhu/CVE-2023-43871-WBCE-Arbitrary-File-Upload--XSS---Media](https://github.com/sromanhu/CVE-2023-43871-WBCE-Arbitrary-File-Upload--XSS---Media) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43871-WBCE-Arbitrary-File-Upload--XSS---Media.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43871-WBCE-Arbitrary-File-Upload--XSS---Media.svg)

## CVE-2023-43838
 An arbitrary file upload vulnerability in Personal Management System v1.4.64 allows attackers to execute arbitrary code via uploading a crafted SVG file into a user profile's avatar.



- [https://github.com/rootd4ddy/CVE-2023-43838](https://github.com/rootd4ddy/CVE-2023-43838) :  ![starts](https://img.shields.io/github/stars/rootd4ddy/CVE-2023-43838.svg) ![forks](https://img.shields.io/github/forks/rootd4ddy/CVE-2023-43838.svg)

## CVE-2023-43786
 A vulnerability was found in libX11 due to an infinite loop within the PutSubImage() function. This flaw allows a local user to consume all available system resources and cause a denial of service condition.



- [https://github.com/jfrog/jfrog-CVE-2023-43786-libX11_DoS](https://github.com/jfrog/jfrog-CVE-2023-43786-libX11_DoS) :  ![starts](https://img.shields.io/github/stars/jfrog/jfrog-CVE-2023-43786-libX11_DoS.svg) ![forks](https://img.shields.io/github/forks/jfrog/jfrog-CVE-2023-43786-libX11_DoS.svg)

## CVE-2023-43770
 Roundcube before 1.4.14, 1.5.x before 1.5.4, and 1.6.x before 1.6.3 allows XSS via text/plain e-mail messages with crafted links because of program/lib/Roundcube/rcube_string_replacer.php behavior.



- [https://github.com/s3cb0y/CVE-2023-43770-POC](https://github.com/s3cb0y/CVE-2023-43770-POC) :  ![starts](https://img.shields.io/github/stars/s3cb0y/CVE-2023-43770-POC.svg) ![forks](https://img.shields.io/github/forks/s3cb0y/CVE-2023-43770-POC.svg)

- [https://github.com/knight0x07/CVE-2023-43770-PoC](https://github.com/knight0x07/CVE-2023-43770-PoC) :  ![starts](https://img.shields.io/github/stars/knight0x07/CVE-2023-43770-PoC.svg) ![forks](https://img.shields.io/github/forks/knight0x07/CVE-2023-43770-PoC.svg)

- [https://github.com/skyllpro/CVE-2021-44026-PoC](https://github.com/skyllpro/CVE-2021-44026-PoC) :  ![starts](https://img.shields.io/github/stars/skyllpro/CVE-2021-44026-PoC.svg) ![forks](https://img.shields.io/github/forks/skyllpro/CVE-2021-44026-PoC.svg)

## CVE-2023-43757
 Inadequate encryption strength vulnerability in multiple routers provided by ELECOM CO.,LTD. and LOGITEC CORPORATION allows a network-adjacent unauthenticated attacker to guess the encryption key used for wireless LAN communication and intercept the communication. As for the affected products/versions, see the information provided by the vendor under [References] section.



- [https://github.com/sharmashreejaa/CVE-2023-43757](https://github.com/sharmashreejaa/CVE-2023-43757) :  ![starts](https://img.shields.io/github/stars/sharmashreejaa/CVE-2023-43757.svg) ![forks](https://img.shields.io/github/forks/sharmashreejaa/CVE-2023-43757.svg)

## CVE-2023-43654
 TorchServe is a tool for serving and scaling PyTorch models in production. TorchServe default configuration lacks proper input validation, enabling third parties to invoke remote HTTP download requests and write files to the disk. This issue could be taken advantage of to compromise the integrity of the system and sensitive data. This issue is present in versions 0.1.0 to 0.8.1. A user is able to load the model of their choice from any URL that they would like to use. The user of TorchServe is responsible for configuring both the allowed_urls and specifying the model URL to be used. A pull request to warn the user when the default value for allowed_urls is used has been merged in PR #2534. TorchServe release 0.8.2 includes this change. Users are advised to upgrade. There are no known workarounds for this issue.



- [https://github.com/OligoCyberSecurity/ShellTorchChecker](https://github.com/OligoCyberSecurity/ShellTorchChecker) :  ![starts](https://img.shields.io/github/stars/OligoCyberSecurity/ShellTorchChecker.svg) ![forks](https://img.shields.io/github/forks/OligoCyberSecurity/ShellTorchChecker.svg)

- [https://github.com/OligoCyberSecurity/CVE-2023-43654](https://github.com/OligoCyberSecurity/CVE-2023-43654) :  ![starts](https://img.shields.io/github/stars/OligoCyberSecurity/CVE-2023-43654.svg) ![forks](https://img.shields.io/github/forks/OligoCyberSecurity/CVE-2023-43654.svg)

## CVE-2023-43622
 An attacker, opening a HTTP/2 connection with an initial window size of 0, was able to block handling of that connection indefinitely in Apache HTTP Server. This could be used to exhaust worker resources in the server, similar to the well known "slow loris" attack pattern.
This has been fixed in version 2.4.58, so that such connection are terminated properly after the configured connection timeout.

This issue affects Apache HTTP Server: from 2.4.55 through 2.4.57.

Users are recommended to upgrade to version 2.4.58, which fixes the issue.



- [https://github.com/visudade/CVE-2023-43622](https://github.com/visudade/CVE-2023-43622) :  ![starts](https://img.shields.io/github/stars/visudade/CVE-2023-43622.svg) ![forks](https://img.shields.io/github/forks/visudade/CVE-2023-43622.svg)

## CVE-2023-43482
 A command execution vulnerability exists in the guest resource functionality of Tp-Link ER7206 Omada Gigabit VPN Router 1.3.0 build 20230322 Rel.70591. A specially crafted HTTP request can lead to arbitrary command execution. An attacker can make an authenticated HTTP request to trigger this vulnerability.



- [https://github.com/Mr-xn/CVE-2023-43482](https://github.com/Mr-xn/CVE-2023-43482) :  ![starts](https://img.shields.io/github/stars/Mr-xn/CVE-2023-43482.svg) ![forks](https://img.shields.io/github/forks/Mr-xn/CVE-2023-43482.svg)

## CVE-2023-43481
 An issue in Shenzhen TCL Browser TV Web BrowseHere (aka com.tcl.browser) 6.65.022_dab24cc6_231221_gp allows a remote attacker to execute arbitrary JavaScript code via the com.tcl.browser.portal.browse.activity.BrowsePageActivity component.



- [https://github.com/actuator/com.tcl.browser](https://github.com/actuator/com.tcl.browser) :  ![starts](https://img.shields.io/github/stars/actuator/com.tcl.browser.svg) ![forks](https://img.shields.io/github/forks/actuator/com.tcl.browser.svg)

## CVE-2023-43364
 main.py in Searchor before 2.4.2 uses eval on CLI input, which may cause unexpected code execution.



- [https://github.com/libertycityhacker/CVE-2023-43364-Exploit-CVE](https://github.com/libertycityhacker/CVE-2023-43364-Exploit-CVE) :  ![starts](https://img.shields.io/github/stars/libertycityhacker/CVE-2023-43364-Exploit-CVE.svg) ![forks](https://img.shields.io/github/forks/libertycityhacker/CVE-2023-43364-Exploit-CVE.svg)

## CVE-2023-43360
 Cross Site Scripting vulnerability in CMSmadesimple v.2.2.18 allows a local attacker to execute arbitrary code via a crafted script to the Top Directory parameter in the File Picker Menu component.



- [https://github.com/sromanhu/CVE-2023-43360-CMSmadesimple-Stored-XSS---File-Picker-extension](https://github.com/sromanhu/CVE-2023-43360-CMSmadesimple-Stored-XSS---File-Picker-extension) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43360-CMSmadesimple-Stored-XSS---File-Picker-extension.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43360-CMSmadesimple-Stored-XSS---File-Picker-extension.svg)

## CVE-2023-43359
 Cross Site Scripting vulnerability in CMSmadesimple v.2.2.18 allows a local attacker to execute arbitrary code via a crafted script to the Page Specific Metadata and Smarty data parameters in the Content Manager Menu component.



- [https://github.com/sromanhu/CVE-2023-43359-CMSmadesimple-Stored-XSS----Content-Manager](https://github.com/sromanhu/CVE-2023-43359-CMSmadesimple-Stored-XSS----Content-Manager) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43359-CMSmadesimple-Stored-XSS----Content-Manager.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43359-CMSmadesimple-Stored-XSS----Content-Manager.svg)

## CVE-2023-43358
 Cross Site Scripting vulnerability in CMSmadesimple v.2.2.18 allows a local attacker to execute arbitrary code via a crafted script to the Title parameter in the News Menu component.



- [https://github.com/sromanhu/CVE-2023-43358-CMSmadesimple-Stored-XSS---News](https://github.com/sromanhu/CVE-2023-43358-CMSmadesimple-Stored-XSS---News) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43358-CMSmadesimple-Stored-XSS---News.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43358-CMSmadesimple-Stored-XSS---News.svg)

## CVE-2023-43357
 Cross Site Scripting vulnerability in CMSmadesimple v.2.2.18 allows a local attacker to execute arbitrary code via a crafted script to the Title parameter in the Manage Shortcuts component.



- [https://github.com/sromanhu/CVE-2023-43357-CMSmadesimple-Stored-XSS---Shortcut](https://github.com/sromanhu/CVE-2023-43357-CMSmadesimple-Stored-XSS---Shortcut) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43357-CMSmadesimple-Stored-XSS---Shortcut.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43357-CMSmadesimple-Stored-XSS---Shortcut.svg)

## CVE-2023-43356
 Cross Site Scripting vulnerability in CMSmadesimple v.2.2.18 allows a local attacker to execute arbitrary code via a crafted script to the Global Meatadata parameter in the Global Settings Menu component.



- [https://github.com/sromanhu/CVE-2023-43356-CMSmadesimple-Stored-XSS---Global-Settings](https://github.com/sromanhu/CVE-2023-43356-CMSmadesimple-Stored-XSS---Global-Settings) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43356-CMSmadesimple-Stored-XSS---Global-Settings.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43356-CMSmadesimple-Stored-XSS---Global-Settings.svg)

## CVE-2023-43355
 Cross Site Scripting vulnerability in CMSmadesimple v.2.2.18 allows a local attacker to execute arbitrary code via a crafted script to the password and password again parameters in the My Preferences - Add user component.



- [https://github.com/sromanhu/CVE-2023-43355-CMSmadesimple-Reflected-XSS---Add-user](https://github.com/sromanhu/CVE-2023-43355-CMSmadesimple-Reflected-XSS---Add-user) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43355-CMSmadesimple-Reflected-XSS---Add-user.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43355-CMSmadesimple-Reflected-XSS---Add-user.svg)

## CVE-2023-43354
 Cross Site Scripting vulnerability in CMSmadesimple v.2.2.18 allows a local attacker to execute arbitrary code via a crafted script to the Profiles parameter in the Extensions -MicroTiny WYSIWYG editor component.



- [https://github.com/sromanhu/CVE-2023-43354-CMSmadesimple-Stored-XSS---MicroTIny-extension](https://github.com/sromanhu/CVE-2023-43354-CMSmadesimple-Stored-XSS---MicroTIny-extension) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43354-CMSmadesimple-Stored-XSS---MicroTIny-extension.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43354-CMSmadesimple-Stored-XSS---MicroTIny-extension.svg)

## CVE-2023-43353
 Cross Site Scripting vulnerability in CMSmadesimple v.2.2.18 allows a local attacker to execute arbitrary code via a crafted script to the extra parameter in the news menu component.



- [https://github.com/sromanhu/CVE-2023-43353-CMSmadesimple-Stored-XSS---News---Extra](https://github.com/sromanhu/CVE-2023-43353-CMSmadesimple-Stored-XSS---News---Extra) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43353-CMSmadesimple-Stored-XSS---News---Extra.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43353-CMSmadesimple-Stored-XSS---News---Extra.svg)

## CVE-2023-43352
 An issue in CMSmadesimple v.2.2.18 allows a local attacker to execute arbitrary code via a crafted payload to the Content Manager Menu component.



- [https://github.com/sromanhu/CVE-2023-43352-CMSmadesimple-SSTI--Content](https://github.com/sromanhu/CVE-2023-43352-CMSmadesimple-SSTI--Content) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43352-CMSmadesimple-SSTI--Content.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43352-CMSmadesimple-SSTI--Content.svg)

## CVE-2023-43346
 Cross-site scripting (XSS) vulnerability in opensolution Quick CMS v.6.7 allows a local attacker to execute arbitrary code via a crafted script to the Backend - Dashboard parameter in the Languages Menu component.



- [https://github.com/sromanhu/CVE-2023-43346-Quick-CMS-Stored-XSS---Languages-Backend](https://github.com/sromanhu/CVE-2023-43346-Quick-CMS-Stored-XSS---Languages-Backend) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43346-Quick-CMS-Stored-XSS---Languages-Backend.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43346-Quick-CMS-Stored-XSS---Languages-Backend.svg)

## CVE-2023-43345
 Cross-site scripting (XSS) vulnerability in opensolution Quick CMS v.6.7 allows a local attacker to execute arbitrary code via a crafted script to the Content - Name parameter in the Pages Menu component.



- [https://github.com/sromanhu/CVE-2023-43345-Quick-CMS-Stored-XSS---Pages-Content](https://github.com/sromanhu/CVE-2023-43345-Quick-CMS-Stored-XSS---Pages-Content) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43345-Quick-CMS-Stored-XSS---Pages-Content.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43345-Quick-CMS-Stored-XSS---Pages-Content.svg)

## CVE-2023-43344
 Cross-site scripting (XSS) vulnerability in opensolution Quick CMS v.6.7 allows a local attacker to execute arbitrary code via a crafted script to the SEO - Meta description parameter in the Pages Menu component.



- [https://github.com/sromanhu/CVE-2023-43344-Quick-CMS-Stored-XSS---SEO-Meta-description](https://github.com/sromanhu/CVE-2023-43344-Quick-CMS-Stored-XSS---SEO-Meta-description) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43344-Quick-CMS-Stored-XSS---SEO-Meta-description.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43344-Quick-CMS-Stored-XSS---SEO-Meta-description.svg)

## CVE-2023-43343
 Cross-site scripting (XSS) vulnerability in opensolution Quick CMS v.6.7 allows a local attacker to execute arbitrary code via a crafted script to the Files - Description parameter in the Pages Menu component.



- [https://github.com/sromanhu/CVE-2023-43343-Quick-CMS-Stored-XSS---Pages-Files](https://github.com/sromanhu/CVE-2023-43343-Quick-CMS-Stored-XSS---Pages-Files) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43343-Quick-CMS-Stored-XSS---Pages-Files.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43343-Quick-CMS-Stored-XSS---Pages-Files.svg)

## CVE-2023-43342
 Cross-site scripting (XSS) vulnerability in opensolution Quick CMS v.6.7 allows a local attacker to execute arbitrary code via a crafted script to the Languages Menu component.



- [https://github.com/sromanhu/CVE-2023-43342-Quick-CMS-Stored-XSS---Languages-Frontend](https://github.com/sromanhu/CVE-2023-43342-Quick-CMS-Stored-XSS---Languages-Frontend) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43342-Quick-CMS-Stored-XSS---Languages-Frontend.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43342-Quick-CMS-Stored-XSS---Languages-Frontend.svg)

## CVE-2023-43341
 Cross-site scripting (XSS) vulnerability in evolution evo v.3.2.3 allows a local attacker to execute arbitrary code via a crafted payload injected uid parameter.



- [https://github.com/sromanhu/CVE-2023-43341-Evolution-Reflected-XSS---Installation-Connection-](https://github.com/sromanhu/CVE-2023-43341-Evolution-Reflected-XSS---Installation-Connection-) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43341-Evolution-Reflected-XSS---Installation-Connection-.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43341-Evolution-Reflected-XSS---Installation-Connection-.svg)

## CVE-2023-43340
 Cross-site scripting (XSS) vulnerability in evolution v.3.2.3 allows a local attacker to execute arbitrary code via a crafted payload injected into the cmsadmin, cmsadminemail, cmspassword and cmspasswordconfim parameters



- [https://github.com/sromanhu/-CVE-2023-43340-Evolution-Reflected-XSS---Installation-Admin-Options](https://github.com/sromanhu/-CVE-2023-43340-Evolution-Reflected-XSS---Installation-Admin-Options) :  ![starts](https://img.shields.io/github/stars/sromanhu/-CVE-2023-43340-Evolution-Reflected-XSS---Installation-Admin-Options.svg) ![forks](https://img.shields.io/github/forks/sromanhu/-CVE-2023-43340-Evolution-Reflected-XSS---Installation-Admin-Options.svg)

## CVE-2023-43339
 Cross-Site Scripting (XSS) vulnerability in cmsmadesimple v.2.2.18 allows a local attacker to execute arbitrary code via a crafted payload injected into the Database Name, DataBase User or Database Port components.



- [https://github.com/sromanhu/CVE-2023-43339-CMSmadesimple-Reflected-XSS---Installation](https://github.com/sromanhu/CVE-2023-43339-CMSmadesimple-Reflected-XSS---Installation) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-43339-CMSmadesimple-Reflected-XSS---Installation.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-43339-CMSmadesimple-Reflected-XSS---Installation.svg)

## CVE-2023-43326
 A reflected cross-site scripting (XSS) vulnerability exisits in multiple url of mooSocial v3.1.8 allows attackers to steal user's session cookies and impersonate their account via a crafted URL.



- [https://github.com/ahrixia/CVE-2023-43326](https://github.com/ahrixia/CVE-2023-43326) :  ![starts](https://img.shields.io/github/stars/ahrixia/CVE-2023-43326.svg) ![forks](https://img.shields.io/github/forks/ahrixia/CVE-2023-43326.svg)

## CVE-2023-43325
 A reflected cross-site scripting (XSS) vulnerability in the data[redirect_url] parameter of mooSocial v3.1.8 allows attackers to steal user's session cookies and impersonate their account via a crafted URL.



- [https://github.com/ahrixia/CVE-2023-43325](https://github.com/ahrixia/CVE-2023-43325) :  ![starts](https://img.shields.io/github/stars/ahrixia/CVE-2023-43325.svg) ![forks](https://img.shields.io/github/forks/ahrixia/CVE-2023-43325.svg)

## CVE-2023-43323
 mooSocial 3.1.8 is vulnerable to external service interaction on post function. When executed, the server sends a HTTP and DNS request to external server. The Parameters effected are multiple - messageText, data[wall_photo], data[userShareVideo] and data[userShareLink].



- [https://github.com/ahrixia/CVE-2023-43323](https://github.com/ahrixia/CVE-2023-43323) :  ![starts](https://img.shields.io/github/stars/ahrixia/CVE-2023-43323.svg) ![forks](https://img.shields.io/github/forks/ahrixia/CVE-2023-43323.svg)

## CVE-2023-43318
 TP-Link JetStream Smart Switch TL-SG2210P 5.0 Build 20211201 allows attackers to escalate privileges via modification of the 'tid' and 'usrlvl' values in GET requests.



- [https://github.com/str2ver/CVE-2023-43318](https://github.com/str2ver/CVE-2023-43318) :  ![starts](https://img.shields.io/github/stars/str2ver/CVE-2023-43318.svg) ![forks](https://img.shields.io/github/forks/str2ver/CVE-2023-43318.svg)

## CVE-2023-43317
 An issue in Coign CRM Portal v.06.06 allows a remote attacker to escalate privileges via the userPermissionsList parameter in Session Storage component.



- [https://github.com/amjadali-110/CVE-2023-43317](https://github.com/amjadali-110/CVE-2023-43317) :  ![starts](https://img.shields.io/github/stars/amjadali-110/CVE-2023-43317.svg) ![forks](https://img.shields.io/github/forks/amjadali-110/CVE-2023-43317.svg)

## CVE-2023-43292
 Cross Site Scripting vulnerability in My Food Recipe Using PHP with Source Code v.1.0 allows a local attacker to execute arbitrary code via a crafted payload to the Recipe Name, Procedure, and ingredients parameters.



- [https://github.com/ASR511-OO7/CVE-2023-43292](https://github.com/ASR511-OO7/CVE-2023-43292) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-43292.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-43292.svg)

## CVE-2023-43284
 D-Link Wireless MU-MIMO Gigabit AC1200 Router DIR-846 100A53DBR-Retail devices allow an authenticated remote attacker to execute arbitrary code via an unspecified manipulation of the QoS POST parameter.



- [https://github.com/MateusTesser/CVE-2023-43284](https://github.com/MateusTesser/CVE-2023-43284) :  ![starts](https://img.shields.io/github/stars/MateusTesser/CVE-2023-43284.svg) ![forks](https://img.shields.io/github/forks/MateusTesser/CVE-2023-43284.svg)

## CVE-2023-43263
 A Cross-site scripting (XSS) vulnerability in Froala Editor v.4.1.1 allows attackers to execute arbitrary code via the Markdown component.



- [https://github.com/b0marek/CVE-2023-43263](https://github.com/b0marek/CVE-2023-43263) :  ![starts](https://img.shields.io/github/stars/b0marek/CVE-2023-43263.svg) ![forks](https://img.shields.io/github/forks/b0marek/CVE-2023-43263.svg)

## CVE-2023-43261
 An information disclosure in Milesight UR5X, UR32L, UR32, UR35, UR41 before v35.3.0.7 allows attackers to access sensitive router components.



- [https://github.com/win3zz/CVE-2023-43261](https://github.com/win3zz/CVE-2023-43261) :  ![starts](https://img.shields.io/github/stars/win3zz/CVE-2023-43261.svg) ![forks](https://img.shields.io/github/forks/win3zz/CVE-2023-43261.svg)

## CVE-2023-43208
 NextGen Healthcare Mirth Connect before version 4.4.1 is vulnerable to unauthenticated remote code execution. Note that this vulnerability is caused by the incomplete patch of CVE-2023-37679.



- [https://github.com/K3ysTr0K3R/CVE-2023-43208-EXPLOIT](https://github.com/K3ysTr0K3R/CVE-2023-43208-EXPLOIT) :  ![starts](https://img.shields.io/github/stars/K3ysTr0K3R/CVE-2023-43208-EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/K3ysTr0K3R/CVE-2023-43208-EXPLOIT.svg)

- [https://github.com/jakabakos/CVE-2023-43208-mirth-connect-rce-poc](https://github.com/jakabakos/CVE-2023-43208-mirth-connect-rce-poc) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2023-43208-mirth-connect-rce-poc.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2023-43208-mirth-connect-rce-poc.svg)

- [https://github.com/Avento/CVE-2023-43208_Detection_PoC](https://github.com/Avento/CVE-2023-43208_Detection_PoC) :  ![starts](https://img.shields.io/github/stars/Avento/CVE-2023-43208_Detection_PoC.svg) ![forks](https://img.shields.io/github/forks/Avento/CVE-2023-43208_Detection_PoC.svg)

- [https://github.com/J4F9S5D2Q7/CVE-2023-43208-MIRTHCONNECT](https://github.com/J4F9S5D2Q7/CVE-2023-43208-MIRTHCONNECT) :  ![starts](https://img.shields.io/github/stars/J4F9S5D2Q7/CVE-2023-43208-MIRTHCONNECT.svg) ![forks](https://img.shields.io/github/forks/J4F9S5D2Q7/CVE-2023-43208-MIRTHCONNECT.svg)

## CVE-2023-43177
 CrushFTP prior to 10.5.1 is vulnerable to Improperly Controlled Modification of Dynamically-Determined Object Attributes.



- [https://github.com/the-emmons/CVE-2023-43177](https://github.com/the-emmons/CVE-2023-43177) :  ![starts](https://img.shields.io/github/stars/the-emmons/CVE-2023-43177.svg) ![forks](https://img.shields.io/github/forks/the-emmons/CVE-2023-43177.svg)

## CVE-2023-43154
 In Macrob7 Macs Framework Content Management System (CMS) 1.1.4f, loose comparison in "isValidLogin()" function during login attempt results in PHP type confusion vulnerability that leads to authentication bypass and takeover of the administrator account.



- [https://github.com/ally-petitt/CVE-2023-43154-PoC](https://github.com/ally-petitt/CVE-2023-43154-PoC) :  ![starts](https://img.shields.io/github/stars/ally-petitt/CVE-2023-43154-PoC.svg) ![forks](https://img.shields.io/github/forks/ally-petitt/CVE-2023-43154-PoC.svg)

## CVE-2023-43149
 SPA-Cart 1.9.0.3 is vulnerable to Cross Site Request Forgery (CSRF) that allows a remote attacker to add an admin user with role status.



- [https://github.com/MinoTauro2020/CVE-2023-43149](https://github.com/MinoTauro2020/CVE-2023-43149) :  ![starts](https://img.shields.io/github/stars/MinoTauro2020/CVE-2023-43149.svg) ![forks](https://img.shields.io/github/forks/MinoTauro2020/CVE-2023-43149.svg)

## CVE-2023-43148
 SPA-Cart 1.9.0.3 has a Cross Site Request Forgery (CSRF) vulnerability that allows a remote attacker to delete all accounts.



- [https://github.com/MinoTauro2020/CVE-2023-43147](https://github.com/MinoTauro2020/CVE-2023-43147) :  ![starts](https://img.shields.io/github/stars/MinoTauro2020/CVE-2023-43147.svg) ![forks](https://img.shields.io/github/forks/MinoTauro2020/CVE-2023-43147.svg)

- [https://github.com/MinoTauro2020/CVE-2023-43148](https://github.com/MinoTauro2020/CVE-2023-43148) :  ![starts](https://img.shields.io/github/stars/MinoTauro2020/CVE-2023-43148.svg) ![forks](https://img.shields.io/github/forks/MinoTauro2020/CVE-2023-43148.svg)

## CVE-2023-43147
 PHPJabbers Limo Booking Software 1.0 is vulnerable to Cross Site Request Forgery (CSRF) to add an admin user via the Add Users Function, aka an index.php?controller=pjAdminUsers&action=pjActionCreate URI.



- [https://github.com/MinoTauro2020/CVE-2023-43147](https://github.com/MinoTauro2020/CVE-2023-43147) :  ![starts](https://img.shields.io/github/stars/MinoTauro2020/CVE-2023-43147.svg) ![forks](https://img.shields.io/github/forks/MinoTauro2020/CVE-2023-43147.svg)

## CVE-2023-43144
 Projectworldsl Assets-management-system-in-php 1.0 is vulnerable to SQL Injection via the "id" parameter in delete.php.



- [https://github.com/Pegasus0xx/CVE-2023-43144](https://github.com/Pegasus0xx/CVE-2023-43144) :  ![starts](https://img.shields.io/github/stars/Pegasus0xx/CVE-2023-43144.svg) ![forks](https://img.shields.io/github/forks/Pegasus0xx/CVE-2023-43144.svg)

## CVE-2023-43115
 In Artifex Ghostscript through 10.01.2, gdevijs.c in GhostPDL can lead to remote code execution via crafted PostScript documents because they can switch to the IJS device, or change the IjsServer parameter, after SAFER has been activated. NOTE: it is a documented risk that the IJS server can be specified on a gs command line (the IJS device inherently must execute a command to start the IJS server).



- [https://github.com/jostaub/ghostscript-CVE-2023-43115](https://github.com/jostaub/ghostscript-CVE-2023-43115) :  ![starts](https://img.shields.io/github/stars/jostaub/ghostscript-CVE-2023-43115.svg) ![forks](https://img.shields.io/github/forks/jostaub/ghostscript-CVE-2023-43115.svg)

## CVE-2023-43040
 IBM Spectrum Fusion HCI 2.5.2 through 2.7.2 could allow an attacker to perform unauthorized actions in RGW for Ceph due to improper bucket access.  IBM X-Force ID:  266807.



- [https://github.com/riza/CVE-2023-43040](https://github.com/riza/CVE-2023-43040) :  ![starts](https://img.shields.io/github/stars/riza/CVE-2023-43040.svg) ![forks](https://img.shields.io/github/forks/riza/CVE-2023-43040.svg)

## CVE-2023-42931
 The issue was addressed with improved checks. This issue is fixed in macOS Ventura 13.6.3, macOS Sonoma 14.2, macOS Monterey 12.7.2. A process may gain admin privileges without proper authentication.



- [https://github.com/d0rb/CVE-2023-42931](https://github.com/d0rb/CVE-2023-42931) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-42931.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-42931.svg)

- [https://github.com/tageniu/CVE-2023-42931](https://github.com/tageniu/CVE-2023-42931) :  ![starts](https://img.shields.io/github/stars/tageniu/CVE-2023-42931.svg) ![forks](https://img.shields.io/github/forks/tageniu/CVE-2023-42931.svg)

## CVE-2023-42914
 The issue was addressed with improved memory handling. This issue is fixed in macOS Sonoma 14.2, iOS 17.2 and iPadOS 17.2, watchOS 10.2, macOS Ventura 13.6.3, tvOS 17.2, iOS 16.7.3 and iPadOS 16.7.3, macOS Monterey 12.7.2. An app may be able to break out of its sandbox.



- [https://github.com/synacktiv/CVE-2023-32413](https://github.com/synacktiv/CVE-2023-32413) :  ![starts](https://img.shields.io/github/stars/synacktiv/CVE-2023-32413.svg) ![forks](https://img.shields.io/github/forks/synacktiv/CVE-2023-32413.svg)

## CVE-2023-42860
 A permissions issue was addressed with additional restrictions. This issue is fixed in macOS Sonoma 14.1, macOS Monterey 12.7.1, macOS Ventura 13.6.1. An app may be able to modify protected parts of the file system.



- [https://github.com/Trigii/CVE-2023-42860](https://github.com/Trigii/CVE-2023-42860) :  ![starts](https://img.shields.io/github/stars/Trigii/CVE-2023-42860.svg) ![forks](https://img.shields.io/github/forks/Trigii/CVE-2023-42860.svg)

## CVE-2023-42820
 JumpServer is an open source bastion host. This vulnerability is due to exposing the random number seed to the API, potentially allowing the randomly generated verification codes to be replayed, which could lead to password resets. If MFA is enabled users are not affect. Users not using local authentication are also not affected. Users are advised to upgrade to either version 2.28.19 or to 3.6.5. There are no known workarounds or this issue.



- [https://github.com/tarihub/blackjump](https://github.com/tarihub/blackjump) :  ![starts](https://img.shields.io/github/stars/tarihub/blackjump.svg) ![forks](https://img.shields.io/github/forks/tarihub/blackjump.svg)

- [https://github.com/C1ph3rX13/CVE-2023-42820](https://github.com/C1ph3rX13/CVE-2023-42820) :  ![starts](https://img.shields.io/github/stars/C1ph3rX13/CVE-2023-42820.svg) ![forks](https://img.shields.io/github/forks/C1ph3rX13/CVE-2023-42820.svg)

- [https://github.com/Startr4ck/cve-2023-42820](https://github.com/Startr4ck/cve-2023-42820) :  ![starts](https://img.shields.io/github/stars/Startr4ck/cve-2023-42820.svg) ![forks](https://img.shields.io/github/forks/Startr4ck/cve-2023-42820.svg)

## CVE-2023-42819
 JumpServer is an open source bastion host. Logged-in users can access and modify the contents of any file on the system. A user can use the 'Job-Template' menu and create a playbook named 'test'. Get the playbook id from the detail page, like 'e0adabef-c38f-492d-bd92-832bacc3df5f'. An attacker can exploit the directory traversal flaw using the provided URL to access and retrieve the contents of the file. `https://jumpserver-ip/api/v1/ops/playbook/e0adabef-c38f-492d-bd92-832bacc3df5f/file/?key=../../../../../../../etc/passwd` a similar method to modify the file content is also present. This issue has been addressed in version 3.6.5. Users are advised to upgrade. There are no known workarounds for this vulnerability.




- [https://github.com/C1ph3rX13/CVE-2023-42819](https://github.com/C1ph3rX13/CVE-2023-42819) :  ![starts](https://img.shields.io/github/stars/C1ph3rX13/CVE-2023-42819.svg) ![forks](https://img.shields.io/github/forks/C1ph3rX13/CVE-2023-42819.svg)

## CVE-2023-42793
 In JetBrains TeamCity before 2023.05.4 authentication bypass leading to RCE on TeamCity Server was possible



- [https://github.com/H454NSec/CVE-2023-42793](https://github.com/H454NSec/CVE-2023-42793) :  ![starts](https://img.shields.io/github/stars/H454NSec/CVE-2023-42793.svg) ![forks](https://img.shields.io/github/forks/H454NSec/CVE-2023-42793.svg)

- [https://github.com/B4l3rI0n/CVE-2023-42793](https://github.com/B4l3rI0n/CVE-2023-42793) :  ![starts](https://img.shields.io/github/stars/B4l3rI0n/CVE-2023-42793.svg) ![forks](https://img.shields.io/github/forks/B4l3rI0n/CVE-2023-42793.svg)

- [https://github.com/Zenmovie/CVE-2023-42793](https://github.com/Zenmovie/CVE-2023-42793) :  ![starts](https://img.shields.io/github/stars/Zenmovie/CVE-2023-42793.svg) ![forks](https://img.shields.io/github/forks/Zenmovie/CVE-2023-42793.svg)

- [https://github.com/hotplugin0x01/CVE-2023-42793](https://github.com/hotplugin0x01/CVE-2023-42793) :  ![starts](https://img.shields.io/github/stars/hotplugin0x01/CVE-2023-42793.svg) ![forks](https://img.shields.io/github/forks/hotplugin0x01/CVE-2023-42793.svg)

- [https://github.com/HusenjanDev/CVE-2023-42793](https://github.com/HusenjanDev/CVE-2023-42793) :  ![starts](https://img.shields.io/github/stars/HusenjanDev/CVE-2023-42793.svg) ![forks](https://img.shields.io/github/forks/HusenjanDev/CVE-2023-42793.svg)

- [https://github.com/junnythemarksman/CVE-2023-42793](https://github.com/junnythemarksman/CVE-2023-42793) :  ![starts](https://img.shields.io/github/stars/junnythemarksman/CVE-2023-42793.svg) ![forks](https://img.shields.io/github/forks/junnythemarksman/CVE-2023-42793.svg)

- [https://github.com/whoamins/CVE-2023-42793](https://github.com/whoamins/CVE-2023-42793) :  ![starts](https://img.shields.io/github/stars/whoamins/CVE-2023-42793.svg) ![forks](https://img.shields.io/github/forks/whoamins/CVE-2023-42793.svg)

- [https://github.com/johnossawy/CVE-2023-42793_POC](https://github.com/johnossawy/CVE-2023-42793_POC) :  ![starts](https://img.shields.io/github/stars/johnossawy/CVE-2023-42793_POC.svg) ![forks](https://img.shields.io/github/forks/johnossawy/CVE-2023-42793_POC.svg)

- [https://github.com/jakehomb/cve-2023-42793](https://github.com/jakehomb/cve-2023-42793) :  ![starts](https://img.shields.io/github/stars/jakehomb/cve-2023-42793.svg) ![forks](https://img.shields.io/github/forks/jakehomb/cve-2023-42793.svg)

- [https://github.com/syaifulandy/Nuclei-Template-CVE-2023-42793.yaml](https://github.com/syaifulandy/Nuclei-Template-CVE-2023-42793.yaml) :  ![starts](https://img.shields.io/github/stars/syaifulandy/Nuclei-Template-CVE-2023-42793.yaml.svg) ![forks](https://img.shields.io/github/forks/syaifulandy/Nuclei-Template-CVE-2023-42793.yaml.svg)

- [https://github.com/LeHeron/TC_test](https://github.com/LeHeron/TC_test) :  ![starts](https://img.shields.io/github/stars/LeHeron/TC_test.svg) ![forks](https://img.shields.io/github/forks/LeHeron/TC_test.svg)

- [https://github.com/StanleyJobsonAU/GhostTown](https://github.com/StanleyJobsonAU/GhostTown) :  ![starts](https://img.shields.io/github/stars/StanleyJobsonAU/GhostTown.svg) ![forks](https://img.shields.io/github/forks/StanleyJobsonAU/GhostTown.svg)

## CVE-2023-42789
 A out-of-bounds write in Fortinet FortiOS 7.4.0 through 7.4.1, 7.2.0 through 7.2.5, 7.0.0 through 7.0.12, 6.4.0 through 6.4.14, 6.2.0 through 6.2.15, FortiProxy 7.4.0, 7.2.0 through 7.2.6, 7.0.0 through 7.0.12, 2.0.0 through 2.0.13 allows attacker to execute unauthorized code or commands via specially crafted HTTP requests.



- [https://github.com/jhonnybonny/CVE-2023-42789](https://github.com/jhonnybonny/CVE-2023-42789) :  ![starts](https://img.shields.io/github/stars/jhonnybonny/CVE-2023-42789.svg) ![forks](https://img.shields.io/github/forks/jhonnybonny/CVE-2023-42789.svg)

## CVE-2023-42471
 The wave.ai.browser application through 1.0.35 for Android allows a remote attacker to execute arbitrary JavaScript code via a crafted intent. It contains a manifest entry that exports the wave.ai.browser.ui.splash.SplashScreen activity. This activity uses a WebView component to display web content and doesn't adequately validate or sanitize the URI or any extra data passed in the intent by a third party application (with no permissions).



- [https://github.com/actuator/wave.ai.browser](https://github.com/actuator/wave.ai.browser) :  ![starts](https://img.shields.io/github/stars/actuator/wave.ai.browser.svg) ![forks](https://img.shields.io/github/forks/actuator/wave.ai.browser.svg)

## CVE-2023-42470
 The Imou Life com.mm.android.smartlifeiot application through 6.8.0 for Android allows Remote Code Execution via a crafted intent to an exported component. This relates to the com.mm.android.easy4ip.MainActivity activity. JavaScript execution is enabled in the WebView, and direct web content loading occurs.



- [https://github.com/actuator/imou](https://github.com/actuator/imou) :  ![starts](https://img.shields.io/github/stars/actuator/imou.svg) ![forks](https://img.shields.io/github/forks/actuator/imou.svg)

## CVE-2023-42469
 The com.full.dialer.top.secure.encrypted application through 1.0.1 for Android enables any installed application (with no permissions) to place phone calls without user interaction by sending a crafted intent via the com.full.dialer.top.secure.encrypted.activities.DialerActivity component.



- [https://github.com/actuator/com.full.dialer.top.secure.encrypted](https://github.com/actuator/com.full.dialer.top.secure.encrypted) :  ![starts](https://img.shields.io/github/stars/actuator/com.full.dialer.top.secure.encrypted.svg) ![forks](https://img.shields.io/github/forks/actuator/com.full.dialer.top.secure.encrypted.svg)

## CVE-2023-42468
 The com.cutestudio.colordialer application through 2.1.8-2 for Android allows a remote attacker to initiate phone calls without user consent, because of improper export of the com.cutestudio.dialer.activities.DialerActivity component. A third-party application (without any permissions) can craft an intent targeting com.cutestudio.dialer.activities.DialerActivity via the android.intent.action.CALL action in conjunction with a tel: URI, thereby placing a phone call.



- [https://github.com/actuator/com.cutestudio.colordialer](https://github.com/actuator/com.cutestudio.colordialer) :  ![starts](https://img.shields.io/github/stars/actuator/com.cutestudio.colordialer.svg) ![forks](https://img.shields.io/github/forks/actuator/com.cutestudio.colordialer.svg)

## CVE-2023-42442
 JumpServer is an open source bastion host and a professional operation and maintenance security audit system. Starting in version 3.0.0 and prior to versions 3.5.5 and 3.6.4, session replays can download without authentication. Session replays stored in S3, OSS, or other cloud storage are not affected. The api `/api/v1/terminal/sessions/` permission control is broken and can be accessed anonymously. SessionViewSet permission classes set to `[RBACPermission | IsSessionAssignee]`, relation is or, so any permission matched will be allowed. Versions 3.5.5 and 3.6.4 have a fix. After upgrading, visit the api `$HOST/api/v1/terminal/sessions/?limit=1`. The expected http response code is 401 (`not_authenticated`).




- [https://github.com/tarihub/blackjump](https://github.com/tarihub/blackjump) :  ![starts](https://img.shields.io/github/stars/tarihub/blackjump.svg) ![forks](https://img.shields.io/github/forks/tarihub/blackjump.svg)

- [https://github.com/HolyGu/CVE-2023-42442](https://github.com/HolyGu/CVE-2023-42442) :  ![starts](https://img.shields.io/github/stars/HolyGu/CVE-2023-42442.svg) ![forks](https://img.shields.io/github/forks/HolyGu/CVE-2023-42442.svg)

- [https://github.com/C1ph3rX13/CVE-2023-42442](https://github.com/C1ph3rX13/CVE-2023-42442) :  ![starts](https://img.shields.io/github/stars/C1ph3rX13/CVE-2023-42442.svg) ![forks](https://img.shields.io/github/forks/C1ph3rX13/CVE-2023-42442.svg)

## CVE-2023-42426
 Cross-site scripting (XSS) vulnerability in Froala Froala Editor v.4.1.1 allows remote attackers to execute arbitrary code via the 'Insert link' parameter in the 'Insert Image' component.



- [https://github.com/b0marek/CVE-2023-42426](https://github.com/b0marek/CVE-2023-42426) :  ![starts](https://img.shields.io/github/stars/b0marek/CVE-2023-42426.svg) ![forks](https://img.shields.io/github/forks/b0marek/CVE-2023-42426.svg)

## CVE-2023-42413
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/chenghao-hao/cve-2023-42413](https://github.com/chenghao-hao/cve-2023-42413) :  ![starts](https://img.shields.io/github/stars/chenghao-hao/cve-2023-42413.svg) ![forks](https://img.shields.io/github/forks/chenghao-hao/cve-2023-42413.svg)

## CVE-2023-42362
 An arbitrary file upload vulnerability in Teller Web App v.4.4.0 allows a remote attacker to execute arbitrary commands and obtain sensitive information via uploading a crafted file.



- [https://github.com/Mr-n0b3dy/CVE-2023-42362](https://github.com/Mr-n0b3dy/CVE-2023-42362) :  ![starts](https://img.shields.io/github/stars/Mr-n0b3dy/CVE-2023-42362.svg) ![forks](https://img.shields.io/github/forks/Mr-n0b3dy/CVE-2023-42362.svg)

## CVE-2023-42308
 Cross Site Scripting (XSS) vulnerability in Manage Fastrack Subjects in Code-Projects Exam Form Submission 1.0 allows attackers to run arbitrary code via the "Subject Name" and "Subject Code" Section.



- [https://github.com/ASR511-OO7/CVE-2023-42308](https://github.com/ASR511-OO7/CVE-2023-42308) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-42308.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-42308.svg)

## CVE-2023-42307
 Cross Site Scripting (XSS) vulnerability in Code-Projects Exam Form Submission 1.0 allows attackers to run arbitrary code via "Subject Name" and "Subject Code" section.



- [https://github.com/ASR511-OO7/CVE-2023-42307](https://github.com/ASR511-OO7/CVE-2023-42307) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-42307.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-42307.svg)

## CVE-2023-42284
 Blind SQL injection in api_version parameter in Tyk Gateway version 5.0.3 allows attacker to access and dump the database via a crafted SQL query.



- [https://github.com/andreysanyuk/CVE-2023-42284](https://github.com/andreysanyuk/CVE-2023-42284) :  ![starts](https://img.shields.io/github/stars/andreysanyuk/CVE-2023-42284.svg) ![forks](https://img.shields.io/github/forks/andreysanyuk/CVE-2023-42284.svg)

## CVE-2023-42283
 Blind SQL injection in api_id parameter in Tyk Gateway version 5.0.3 allows attacker to access and dump the database via a crafted SQL query.



- [https://github.com/andreysanyuk/CVE-2023-42283](https://github.com/andreysanyuk/CVE-2023-42283) :  ![starts](https://img.shields.io/github/stars/andreysanyuk/CVE-2023-42283.svg) ![forks](https://img.shields.io/github/forks/andreysanyuk/CVE-2023-42283.svg)

## CVE-2023-42222
 WebCatalog before 49.0 is vulnerable to Incorrect Access Control. WebCatalog calls the Electron shell.openExternal function without verifying that the URL is for an http or https resource, in some circumstances.



- [https://github.com/itssixtyn3in/CVE-2023-42222](https://github.com/itssixtyn3in/CVE-2023-42222) :  ![starts](https://img.shields.io/github/stars/itssixtyn3in/CVE-2023-42222.svg) ![forks](https://img.shields.io/github/forks/itssixtyn3in/CVE-2023-42222.svg)

## CVE-2023-41993
 The issue was addressed with improved checks. This issue is fixed in macOS Sonoma 14. Processing web content may lead to arbitrary code execution. Apple is aware of a report that this issue may have been actively exploited against versions of iOS before iOS 16.7.



- [https://github.com/po6ix/POC-for-CVE-2023-41993](https://github.com/po6ix/POC-for-CVE-2023-41993) :  ![starts](https://img.shields.io/github/stars/po6ix/POC-for-CVE-2023-41993.svg) ![forks](https://img.shields.io/github/forks/po6ix/POC-for-CVE-2023-41993.svg)

- [https://github.com/hrtowii/cve-2023-41993-test](https://github.com/hrtowii/cve-2023-41993-test) :  ![starts](https://img.shields.io/github/stars/hrtowii/cve-2023-41993-test.svg) ![forks](https://img.shields.io/github/forks/hrtowii/cve-2023-41993-test.svg)

- [https://github.com/0x06060606/CVE-2023-41993](https://github.com/0x06060606/CVE-2023-41993) :  ![starts](https://img.shields.io/github/stars/0x06060606/CVE-2023-41993.svg) ![forks](https://img.shields.io/github/forks/0x06060606/CVE-2023-41993.svg)

- [https://github.com/Mangaia/cve-test](https://github.com/Mangaia/cve-test) :  ![starts](https://img.shields.io/github/stars/Mangaia/cve-test.svg) ![forks](https://img.shields.io/github/forks/Mangaia/cve-test.svg)

- [https://github.com/J3Ss0u/CVE-2023-41993](https://github.com/J3Ss0u/CVE-2023-41993) :  ![starts](https://img.shields.io/github/stars/J3Ss0u/CVE-2023-41993.svg) ![forks](https://img.shields.io/github/forks/J3Ss0u/CVE-2023-41993.svg)

## CVE-2023-41992
 The issue was addressed with improved checks. This issue is fixed in macOS Monterey 12.7, iOS 16.7 and iPadOS 16.7, macOS Ventura 13.6. A local attacker may be able to elevate their privileges. Apple is aware of a report that this issue may have been actively exploited against versions of iOS before iOS 16.7.



- [https://github.com/WHW0x455/CVE-2023-41992](https://github.com/WHW0x455/CVE-2023-41992) :  ![starts](https://img.shields.io/github/stars/WHW0x455/CVE-2023-41992.svg) ![forks](https://img.shields.io/github/forks/WHW0x455/CVE-2023-41992.svg)

## CVE-2023-41991
 A certificate validation issue was addressed. This issue is fixed in macOS Ventura 13.6, iOS 16.7 and iPadOS 16.7. A malicious app may be able to bypass signature validation. Apple is aware of a report that this issue may have been actively exploited against versions of iOS before iOS 16.7.



- [https://github.com/Zenyith/CVE-2023-41991](https://github.com/Zenyith/CVE-2023-41991) :  ![starts](https://img.shields.io/github/stars/Zenyith/CVE-2023-41991.svg) ![forks](https://img.shields.io/github/forks/Zenyith/CVE-2023-41991.svg)

## CVE-2023-41892
 Craft CMS is a platform for creating digital experiences. This is a high-impact, low-complexity attack vector. Users running Craft installations before 4.4.15 are encouraged to update to at least that version to mitigate the issue. This issue has been fixed in Craft CMS 4.4.15.



- [https://github.com/0xfalafel/CraftCMS_CVE-2023-41892](https://github.com/0xfalafel/CraftCMS_CVE-2023-41892) :  ![starts](https://img.shields.io/github/stars/0xfalafel/CraftCMS_CVE-2023-41892.svg) ![forks](https://img.shields.io/github/forks/0xfalafel/CraftCMS_CVE-2023-41892.svg)

- [https://github.com/diegaccio/Craft-CMS-Exploit](https://github.com/diegaccio/Craft-CMS-Exploit) :  ![starts](https://img.shields.io/github/stars/diegaccio/Craft-CMS-Exploit.svg) ![forks](https://img.shields.io/github/forks/diegaccio/Craft-CMS-Exploit.svg)

- [https://github.com/zaenhaxor/CVE-2023-41892](https://github.com/zaenhaxor/CVE-2023-41892) :  ![starts](https://img.shields.io/github/stars/zaenhaxor/CVE-2023-41892.svg) ![forks](https://img.shields.io/github/forks/zaenhaxor/CVE-2023-41892.svg)

- [https://github.com/acesoyeo/CVE-2023-41892](https://github.com/acesoyeo/CVE-2023-41892) :  ![starts](https://img.shields.io/github/stars/acesoyeo/CVE-2023-41892.svg) ![forks](https://img.shields.io/github/forks/acesoyeo/CVE-2023-41892.svg)

- [https://github.com/CERTologists/HTTP-Request-for-PHP-object-injection-attack-on-CVE-2023-41892](https://github.com/CERTologists/HTTP-Request-for-PHP-object-injection-attack-on-CVE-2023-41892) :  ![starts](https://img.shields.io/github/stars/CERTologists/HTTP-Request-for-PHP-object-injection-attack-on-CVE-2023-41892.svg) ![forks](https://img.shields.io/github/forks/CERTologists/HTTP-Request-for-PHP-object-injection-attack-on-CVE-2023-41892.svg)

## CVE-2023-41772
 Win32k Elevation of Privilege Vulnerability



- [https://github.com/R41N3RZUF477/CVE-2023-41772](https://github.com/R41N3RZUF477/CVE-2023-41772) :  ![starts](https://img.shields.io/github/stars/R41N3RZUF477/CVE-2023-41772.svg) ![forks](https://img.shields.io/github/forks/R41N3RZUF477/CVE-2023-41772.svg)

## CVE-2023-41717
 Inappropriate file type control in Zscaler Proxy versions 3.6.1.25 and prior allows local attackers to bypass file download/upload restrictions.



- [https://github.com/federella/CVE-2023-41717](https://github.com/federella/CVE-2023-41717) :  ![starts](https://img.shields.io/github/stars/federella/CVE-2023-41717.svg) ![forks](https://img.shields.io/github/forks/federella/CVE-2023-41717.svg)

## CVE-2023-41652
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in David F. Carr RSVPMaker rsvpmaker allows SQL Injection.This issue affects RSVPMaker: from n/a through 10.6.6.





- [https://github.com/RandomRobbieBF/CVE-2023-41652](https://github.com/RandomRobbieBF/CVE-2023-41652) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-41652.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-41652.svg)

## CVE-2023-41646
 Buttercup v2.20.3 allows attackers to obtain the hash of the master password for the password manager via accessing the file /vaults.json/



- [https://github.com/tristao-io/CVE-2023-41646](https://github.com/tristao-io/CVE-2023-41646) :  ![starts](https://img.shields.io/github/stars/tristao-io/CVE-2023-41646.svg) ![forks](https://img.shields.io/github/forks/tristao-io/CVE-2023-41646.svg)

## CVE-2023-41623
 Emlog version pro2.1.14 was discovered to contain a SQL injection vulnerability via the uid parameter at /admin/media.php.



- [https://github.com/GhostBalladw/wuhaozhe-s-CVE](https://github.com/GhostBalladw/wuhaozhe-s-CVE) :  ![starts](https://img.shields.io/github/stars/GhostBalladw/wuhaozhe-s-CVE.svg) ![forks](https://img.shields.io/github/forks/GhostBalladw/wuhaozhe-s-CVE.svg)

## CVE-2023-41593
 Multiple cross-site scripting (XSS) vulnerabilities in Dairy Farm Shop Management System Using PHP and MySQL v1.1 allow attackers to execute arbitrary web scripts and HTML via a crafted payload injected into the Category and Category Field parameters.



- [https://github.com/MATRIXDEVIL/CVE](https://github.com/MATRIXDEVIL/CVE) :  ![starts](https://img.shields.io/github/stars/MATRIXDEVIL/CVE.svg) ![forks](https://img.shields.io/github/forks/MATRIXDEVIL/CVE.svg)

## CVE-2023-41575
 Multiple stored cross-site scripting (XSS) vulnerabilities in /bbdms/sign-up.php of Blood Bank & Donor Management v2.2 allow attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the Full Name, Message, or Address parameters.



- [https://github.com/SoundarXploit/Stored-xss](https://github.com/SoundarXploit/Stored-xss) :  ![starts](https://img.shields.io/github/stars/SoundarXploit/Stored-xss.svg) ![forks](https://img.shields.io/github/forks/SoundarXploit/Stored-xss.svg)

## CVE-2023-41535
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Sh33talUmath/CVE-2023-41535](https://github.com/Sh33talUmath/CVE-2023-41535) :  ![starts](https://img.shields.io/github/stars/Sh33talUmath/CVE-2023-41535.svg) ![forks](https://img.shields.io/github/forks/Sh33talUmath/CVE-2023-41535.svg)

## CVE-2023-41534
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Sh33talUmath/CVE-2023-41534](https://github.com/Sh33talUmath/CVE-2023-41534) :  ![starts](https://img.shields.io/github/stars/Sh33talUmath/CVE-2023-41534.svg) ![forks](https://img.shields.io/github/forks/Sh33talUmath/CVE-2023-41534.svg)

## CVE-2023-41533
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Sh33talUmath/CVE-2023-41533](https://github.com/Sh33talUmath/CVE-2023-41533) :  ![starts](https://img.shields.io/github/stars/Sh33talUmath/CVE-2023-41533.svg) ![forks](https://img.shields.io/github/forks/Sh33talUmath/CVE-2023-41533.svg)

## CVE-2023-41508
 A hard coded password in Super Store Finder v3.6 allows attackers to access the administration panel.



- [https://github.com/redblueteam/CVE-2023-41508](https://github.com/redblueteam/CVE-2023-41508) :  ![starts](https://img.shields.io/github/stars/redblueteam/CVE-2023-41508.svg) ![forks](https://img.shields.io/github/forks/redblueteam/CVE-2023-41508.svg)

## CVE-2023-41507
 Super Store Finder v3.6 was discovered to contain multiple SQL injection vulnerabilities in the store locator component via the products, distance, lat, and lng parameters.



- [https://github.com/redblueteam/CVE-2023-41507](https://github.com/redblueteam/CVE-2023-41507) :  ![starts](https://img.shields.io/github/stars/redblueteam/CVE-2023-41507.svg) ![forks](https://img.shields.io/github/forks/redblueteam/CVE-2023-41507.svg)

## CVE-2023-41506
 An arbitrary file upload vulnerability in the Update/Edit Student's Profile Picture function of Student Enrollment In PHP v1.0 allows attackers to execute arbitrary code via uploading a crafted PHP file.



- [https://github.com/ASR511-OO7/CVE-2023-41506](https://github.com/ASR511-OO7/CVE-2023-41506) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41506.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41506.svg)

## CVE-2023-41505
 An arbitrary file upload vulnerability in the Add Student's Profile Picture function of Student Enrollment In PHP v1.0 allows attackers to execute arbitrary code via uploading a crafted PHP file.



- [https://github.com/ASR511-OO7/CVE-2023-41505](https://github.com/ASR511-OO7/CVE-2023-41505) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41505.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41505.svg)

## CVE-2023-41504
 SQL Injection vulnerability in Student Enrollment In PHP 1.0 allows attackers to run arbitrary code via the Student Search function.



- [https://github.com/ASR511-OO7/CVE-2023-41504](https://github.com/ASR511-OO7/CVE-2023-41504) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41504.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41504.svg)

## CVE-2023-41503
 Student Enrollment In PHP v1.0 was discovered to contain a SQL injection vulnerability via the Login function.



- [https://github.com/ASR511-OO7/CVE-2023-41503](https://github.com/ASR511-OO7/CVE-2023-41503) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41503.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41503.svg)

## CVE-2023-41501
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/ASR511-OO7/CVE-2023-41501](https://github.com/ASR511-OO7/CVE-2023-41501) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41501.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41501.svg)

## CVE-2023-41500
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/ASR511-OO7/CVE-2023-41500](https://github.com/ASR511-OO7/CVE-2023-41500) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41500.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41500.svg)

## CVE-2023-41499
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/ASR511-OO7/CVE-2023-41499](https://github.com/ASR511-OO7/CVE-2023-41499) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41499.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41499.svg)

## CVE-2023-41498
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/ASR511-OO7/CVE-2023-41498](https://github.com/ASR511-OO7/CVE-2023-41498) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41498.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41498.svg)

## CVE-2023-41497
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/ASR511-OO7/CVE-2023-41497](https://github.com/ASR511-OO7/CVE-2023-41497) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41497.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41497.svg)

## CVE-2023-41474
 Directory Traversal vulnerability in Ivanti Avalanche 6.3.4.153 allows a remote authenticated attacker to obtain sensitive information via the javax.faces.resource component.



- [https://github.com/JBalanza/CVE-2023-41474](https://github.com/JBalanza/CVE-2023-41474) :  ![starts](https://img.shields.io/github/stars/JBalanza/CVE-2023-41474.svg) ![forks](https://img.shields.io/github/forks/JBalanza/CVE-2023-41474.svg)

## CVE-2023-41436
 Cross Site Scripting vulnerability in CSZCMS v.1.3.0 allows a local attacker to execute arbitrary code via a crafted script to the Additional Meta Tag parameter in the Pages Content Menu component.



- [https://github.com/sromanhu/CVE-2023-41436-CSZ-CMS-Stored-XSS---Pages-Content](https://github.com/sromanhu/CVE-2023-41436-CSZ-CMS-Stored-XSS---Pages-Content) :  ![starts](https://img.shields.io/github/stars/sromanhu/CVE-2023-41436-CSZ-CMS-Stored-XSS---Pages-Content.svg) ![forks](https://img.shields.io/github/forks/sromanhu/CVE-2023-41436-CSZ-CMS-Stored-XSS---Pages-Content.svg)

## CVE-2023-41425
 Cross Site Scripting vulnerability in Wonder CMS v.3.2.0 thru v.3.4.2 allows a remote attacker to execute arbitrary code via a crafted script uploaded to the installModule component.



- [https://github.com/prodigiousMind/CVE-2023-41425](https://github.com/prodigiousMind/CVE-2023-41425) :  ![starts](https://img.shields.io/github/stars/prodigiousMind/CVE-2023-41425.svg) ![forks](https://img.shields.io/github/forks/prodigiousMind/CVE-2023-41425.svg)

- [https://github.com/Tea-On/CVE-2023-41425-RCE-WonderCMS-4.3.2](https://github.com/Tea-On/CVE-2023-41425-RCE-WonderCMS-4.3.2) :  ![starts](https://img.shields.io/github/stars/Tea-On/CVE-2023-41425-RCE-WonderCMS-4.3.2.svg) ![forks](https://img.shields.io/github/forks/Tea-On/CVE-2023-41425-RCE-WonderCMS-4.3.2.svg)

- [https://github.com/Diegomjx/CVE-2023-41425-WonderCMS-Authenticated-RCE](https://github.com/Diegomjx/CVE-2023-41425-WonderCMS-Authenticated-RCE) :  ![starts](https://img.shields.io/github/stars/Diegomjx/CVE-2023-41425-WonderCMS-Authenticated-RCE.svg) ![forks](https://img.shields.io/github/forks/Diegomjx/CVE-2023-41425-WonderCMS-Authenticated-RCE.svg)

- [https://github.com/charlesgargasson/CVE-2023-41425](https://github.com/charlesgargasson/CVE-2023-41425) :  ![starts](https://img.shields.io/github/stars/charlesgargasson/CVE-2023-41425.svg) ![forks](https://img.shields.io/github/forks/charlesgargasson/CVE-2023-41425.svg)

- [https://github.com/xpltive/CVE-2023-41425](https://github.com/xpltive/CVE-2023-41425) :  ![starts](https://img.shields.io/github/stars/xpltive/CVE-2023-41425.svg) ![forks](https://img.shields.io/github/forks/xpltive/CVE-2023-41425.svg)

- [https://github.com/becrevex/CVE-2023-41425](https://github.com/becrevex/CVE-2023-41425) :  ![starts](https://img.shields.io/github/stars/becrevex/CVE-2023-41425.svg) ![forks](https://img.shields.io/github/forks/becrevex/CVE-2023-41425.svg)

- [https://github.com/0x0d3ad/CVE-2023-41425](https://github.com/0x0d3ad/CVE-2023-41425) :  ![starts](https://img.shields.io/github/stars/0x0d3ad/CVE-2023-41425.svg) ![forks](https://img.shields.io/github/forks/0x0d3ad/CVE-2023-41425.svg)

## CVE-2023-41362
 MyBB before 1.8.36 allows Code Injection by users with certain high privileges. Templates in Admin CP intentionally use eval, and there was some validation of the input to eval, but type juggling interfered with this when using PCRE within PHP.



- [https://github.com/SorceryIE/CVE-2023-41362_MyBB_ACP_RCE](https://github.com/SorceryIE/CVE-2023-41362_MyBB_ACP_RCE) :  ![starts](https://img.shields.io/github/stars/SorceryIE/CVE-2023-41362_MyBB_ACP_RCE.svg) ![forks](https://img.shields.io/github/forks/SorceryIE/CVE-2023-41362_MyBB_ACP_RCE.svg)

## CVE-2023-41320
 GLPI stands for Gestionnaire Libre de Parc Informatique is a Free Asset and IT Management Software package, that provides ITIL Service Desk features, licenses tracking and software auditing. UI layout preferences management can be hijacked to lead to SQL injection. This injection can be use to takeover an administrator account. Users are advised to upgrade to version 10.0.10. There are no known workarounds for this vulnerability.



- [https://github.com/Guilhem7/CVE_2023_41320](https://github.com/Guilhem7/CVE_2023_41320) :  ![starts](https://img.shields.io/github/stars/Guilhem7/CVE_2023_41320.svg) ![forks](https://img.shields.io/github/forks/Guilhem7/CVE_2023_41320.svg)

## CVE-2023-41266
 A path traversal vulnerability found in Qlik Sense Enterprise for Windows for versions May 2023 Patch 3 and earlier, February 2023 Patch 7 and earlier, November 2022 Patch 10 and earlier, and August 2022 Patch 12 and earlier allows an unauthenticated remote attacker to generate an anonymous session. This allows them to transmit HTTP requests to unauthorized endpoints. This is fixed in August 2023 IR, May 2023 Patch 4, February 2023 Patch 8, November 2022 Patch 11, and August 2022 Patch 13.



- [https://github.com/praetorian-inc/zeroqlik-detect](https://github.com/praetorian-inc/zeroqlik-detect) :  ![starts](https://img.shields.io/github/stars/praetorian-inc/zeroqlik-detect.svg) ![forks](https://img.shields.io/github/forks/praetorian-inc/zeroqlik-detect.svg)

## CVE-2023-41265
 An HTTP Request Tunneling vulnerability found in Qlik Sense Enterprise for Windows for versions May 2023 Patch 3 and earlier, February 2023 Patch 7 and earlier, November 2022 Patch 10 and earlier, and August 2022 Patch 12 and earlier allows a remote attacker to elevate their privilege by tunneling HTTP requests in the raw HTTP request. This allows them to send requests that get executed by the backend server hosting the repository application. This is fixed in August 2023 IR, May 2023 Patch 4, February 2023 Patch 8, November 2022 Patch 11, and August 2022 Patch 13.



- [https://github.com/praetorian-inc/zeroqlik-detect](https://github.com/praetorian-inc/zeroqlik-detect) :  ![starts](https://img.shields.io/github/stars/praetorian-inc/zeroqlik-detect.svg) ![forks](https://img.shields.io/github/forks/praetorian-inc/zeroqlik-detect.svg)

## CVE-2023-41080
 URL Redirection to Untrusted Site ('Open Redirect') vulnerability in FORM authentication feature Apache Tomcat.This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.0-M10, from 10.1.0-M1 through 10.0.12, from 9.0.0-M1 through 9.0.79 and from 8.5.0 through 8.5.92.
Older, EOL versions may also be affected.


The vulnerability is limited to the ROOT (default) web application.



- [https://github.com/shiomiyan/CVE-2023-41080](https://github.com/shiomiyan/CVE-2023-41080) :  ![starts](https://img.shields.io/github/stars/shiomiyan/CVE-2023-41080.svg) ![forks](https://img.shields.io/github/forks/shiomiyan/CVE-2023-41080.svg)

## CVE-2023-41064
 A buffer overflow issue was addressed with improved memory handling. This issue is fixed in iOS 16.6.1 and iPadOS 16.6.1, macOS Monterey 12.6.9, macOS Ventura 13.5.2, iOS 15.7.9 and iPadOS 15.7.9, macOS Big Sur 11.7.10. Processing a maliciously crafted image may lead to arbitrary code execution. Apple is aware of a report that this issue may have been actively exploited.



- [https://github.com/MrR0b0t19/CVE-2023-41064](https://github.com/MrR0b0t19/CVE-2023-41064) :  ![starts](https://img.shields.io/github/stars/MrR0b0t19/CVE-2023-41064.svg) ![forks](https://img.shields.io/github/forks/MrR0b0t19/CVE-2023-41064.svg)

- [https://github.com/K4Der11000/k4_cve-2023-41064](https://github.com/K4Der11000/k4_cve-2023-41064) :  ![starts](https://img.shields.io/github/stars/K4Der11000/k4_cve-2023-41064.svg) ![forks](https://img.shields.io/github/forks/K4Der11000/k4_cve-2023-41064.svg)

- [https://github.com/sarsaeroth/CVE-2023-41064-POC](https://github.com/sarsaeroth/CVE-2023-41064-POC) :  ![starts](https://img.shields.io/github/stars/sarsaeroth/CVE-2023-41064-POC.svg) ![forks](https://img.shields.io/github/forks/sarsaeroth/CVE-2023-41064-POC.svg)

- [https://github.com/MrR0b0t19/vulnerabilidad-LibWebP-CVE-2023-41064](https://github.com/MrR0b0t19/vulnerabilidad-LibWebP-CVE-2023-41064) :  ![starts](https://img.shields.io/github/stars/MrR0b0t19/vulnerabilidad-LibWebP-CVE-2023-41064.svg) ![forks](https://img.shields.io/github/forks/MrR0b0t19/vulnerabilidad-LibWebP-CVE-2023-41064.svg)

## CVE-2023-41015
 code-projects.org Online Job Portal 1.0 is vulnerable to SQL Injection via /Employer/DeleteJob.php?JobId=1.



- [https://github.com/ASR511-OO7/CVE-2023-41015](https://github.com/ASR511-OO7/CVE-2023-41015) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41015.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41015.svg)

## CVE-2023-41014
 code-projects.org Online Job Portal 1.0 is vulnerable to SQL Injection via the Username parameter for "Employer."



- [https://github.com/ASR511-OO7/CVE-2023-41014](https://github.com/ASR511-OO7/CVE-2023-41014) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41014.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41014.svg)

## CVE-2023-40989
 SQL injection vulnerbility in jeecgboot jeecg-boot v 3.0, 3.5.3 that allows a remote attacker to execute arbitrary code via a crafted request to the report/jeecgboot/jmreport/queryFieldBySql component.



- [https://github.com/Zone1-Z/CVE-2023-40989](https://github.com/Zone1-Z/CVE-2023-40989) :  ![starts](https://img.shields.io/github/stars/Zone1-Z/CVE-2023-40989.svg) ![forks](https://img.shields.io/github/forks/Zone1-Z/CVE-2023-40989.svg)

## CVE-2023-40933
 A SQL injection vulnerability in Nagios XI v5.11.1 and below allows authenticated attackers with announcement banner configuration privileges to execute arbitrary SQL commands via the ID parameter sent to the update_banner_message() function.



- [https://github.com/sealldeveloper/CVE-2023-40933-PoC](https://github.com/sealldeveloper/CVE-2023-40933-PoC) :  ![starts](https://img.shields.io/github/stars/sealldeveloper/CVE-2023-40933-PoC.svg) ![forks](https://img.shields.io/github/forks/sealldeveloper/CVE-2023-40933-PoC.svg)

## CVE-2023-40931
 A SQL injection vulnerability in Nagios XI from version 5.11.0 up to and including 5.11.1 allows authenticated attackers to execute arbitrary SQL commands via the ID parameter in the POST request to /nagiosxi/admin/banner_message-ajaxhelper.php



- [https://github.com/sealldeveloper/CVE-2023-40931-PoC](https://github.com/sealldeveloper/CVE-2023-40931-PoC) :  ![starts](https://img.shields.io/github/stars/sealldeveloper/CVE-2023-40931-PoC.svg) ![forks](https://img.shields.io/github/forks/sealldeveloper/CVE-2023-40931-PoC.svg)

- [https://github.com/G4sp4rCS/CVE-2023-40931-POC](https://github.com/G4sp4rCS/CVE-2023-40931-POC) :  ![starts](https://img.shields.io/github/stars/G4sp4rCS/CVE-2023-40931-POC.svg) ![forks](https://img.shields.io/github/forks/G4sp4rCS/CVE-2023-40931-POC.svg)

- [https://github.com/datboi6942/Nagios-XI-s-CVE-2023-40931-Exploit](https://github.com/datboi6942/Nagios-XI-s-CVE-2023-40931-Exploit) :  ![starts](https://img.shields.io/github/stars/datboi6942/Nagios-XI-s-CVE-2023-40931-Exploit.svg) ![forks](https://img.shields.io/github/forks/datboi6942/Nagios-XI-s-CVE-2023-40931-Exploit.svg)

## CVE-2023-40930
 An issue in the directory /system/bin/blkid of Skyworth v3.0 allows attackers to perform a directory traversal via mounting the Udisk to /mnt/.



- [https://github.com/NSnidie/CVE-2023-40930](https://github.com/NSnidie/CVE-2023-40930) :  ![starts](https://img.shields.io/github/stars/NSnidie/CVE-2023-40930.svg) ![forks](https://img.shields.io/github/forks/NSnidie/CVE-2023-40930.svg)

## CVE-2023-40924
 SolarView Compact  6.00 is vulnerable to Directory Traversal.



- [https://github.com/Yobing1/CVE-2023-40924](https://github.com/Yobing1/CVE-2023-40924) :  ![starts](https://img.shields.io/github/stars/Yobing1/CVE-2023-40924.svg) ![forks](https://img.shields.io/github/forks/Yobing1/CVE-2023-40924.svg)

## CVE-2023-40869
 Cross Site Scripting vulnerability in mooSocial mooSocial Software 3.1.6 and 3.1.7 allows a remote attacker to execute arbitrary code via a crafted script to the edit_menu, copuon, and group_categorias functions.



- [https://github.com/MinoTauro2020/CVE-2023-40869](https://github.com/MinoTauro2020/CVE-2023-40869) :  ![starts](https://img.shields.io/github/stars/MinoTauro2020/CVE-2023-40869.svg) ![forks](https://img.shields.io/github/forks/MinoTauro2020/CVE-2023-40869.svg)

## CVE-2023-40868
 Cross Site Request Forgery vulnerability in mooSocial MooSocial Software v.Demo allows a remote attacker to execute arbitrary code via the Delete Account and Deactivate functions.



- [https://github.com/MinoTauro2020/CVE-2023-40868](https://github.com/MinoTauro2020/CVE-2023-40868) :  ![starts](https://img.shields.io/github/stars/MinoTauro2020/CVE-2023-40868.svg) ![forks](https://img.shields.io/github/forks/MinoTauro2020/CVE-2023-40868.svg)

## CVE-2023-40626
 The language file parsing process could be manipulated to expose environment variables. Environment variables might contain sensible information.



- [https://github.com/TLWebdesign/Joomla-3.10.12-languagehelper-hotfix](https://github.com/TLWebdesign/Joomla-3.10.12-languagehelper-hotfix) :  ![starts](https://img.shields.io/github/stars/TLWebdesign/Joomla-3.10.12-languagehelper-hotfix.svg) ![forks](https://img.shields.io/github/forks/TLWebdesign/Joomla-3.10.12-languagehelper-hotfix.svg)

## CVE-2023-40600
 Exposure of Sensitive Information to an Unauthorized Actor vulnerability in Exactly WWW EWWW Image Optimizer. It works only when debug.log is turned on.This issue affects EWWW Image Optimizer: from n/a through 7.2.0.





- [https://github.com/RandomRobbieBF/CVE-2023-40600](https://github.com/RandomRobbieBF/CVE-2023-40600) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-40600.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-40600.svg)

## CVE-2023-40477
 RARLAB WinRAR Recovery Volume Improper Validation of Array Index Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of RARLAB WinRAR. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the processing of recovery volumes. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process. Was ZDI-CAN-21233.



- [https://github.com/wildptr-io/Winrar-CVE-2023-40477-POC](https://github.com/wildptr-io/Winrar-CVE-2023-40477-POC) :  ![starts](https://img.shields.io/github/stars/wildptr-io/Winrar-CVE-2023-40477-POC.svg) ![forks](https://img.shields.io/github/forks/wildptr-io/Winrar-CVE-2023-40477-POC.svg)

- [https://github.com/winkler-winsen/Scan_WinRAR](https://github.com/winkler-winsen/Scan_WinRAR) :  ![starts](https://img.shields.io/github/stars/winkler-winsen/Scan_WinRAR.svg) ![forks](https://img.shields.io/github/forks/winkler-winsen/Scan_WinRAR.svg)

## CVE-2023-40459
 








The
ACEManager component of ALEOS 4.16 and earlier does not adequately perform
input sanitization during authentication, which could potentially result in a
Denial of Service (DoS) condition for ACEManager without impairing other router
functions. ACEManager recovers from the DoS condition by restarting within ten
seconds of becoming unavailable.










- [https://github.com/majidmc2/CVE-2023-40459](https://github.com/majidmc2/CVE-2023-40459) :  ![starts](https://img.shields.io/github/stars/majidmc2/CVE-2023-40459.svg) ![forks](https://img.shields.io/github/forks/majidmc2/CVE-2023-40459.svg)

## CVE-2023-40429
 A permissions issue was addressed with improved validation. This issue is fixed in tvOS 17, iOS 17 and iPadOS 17, watchOS 10, macOS Sonoma 14. An app may be able to access sensitive user data.



- [https://github.com/biscuitehh/cve-2023-40429-ez-device-name](https://github.com/biscuitehh/cve-2023-40429-ez-device-name) :  ![starts](https://img.shields.io/github/stars/biscuitehh/cve-2023-40429-ez-device-name.svg) ![forks](https://img.shields.io/github/forks/biscuitehh/cve-2023-40429-ez-device-name.svg)

## CVE-2023-40362
 An issue was discovered in CentralSquare Click2Gov Building Permit before October 2023. Lack of access control protections allows remote attackers to arbitrarily delete the contractors from any user's account when the user ID and contractor information is known.



- [https://github.com/ally-petitt/CVE-2023-40362](https://github.com/ally-petitt/CVE-2023-40362) :  ![starts](https://img.shields.io/github/stars/ally-petitt/CVE-2023-40362.svg) ![forks](https://img.shields.io/github/forks/ally-petitt/CVE-2023-40362.svg)

## CVE-2023-40361
 SECUDOS Qiata (DOMOS OS) 4.13 has Insecure Permissions for the previewRm.sh daily cronjob. To exploit this, an attacker needs access as a low-privileged user to the underlying DOMOS system. Every user on the system has write permission for previewRm.sh, which is executed by the root user.



- [https://github.com/vianic/CVE-2023-40361](https://github.com/vianic/CVE-2023-40361) :  ![starts](https://img.shields.io/github/stars/vianic/CVE-2023-40361.svg) ![forks](https://img.shields.io/github/forks/vianic/CVE-2023-40361.svg)

## CVE-2023-40355
 Cross Site Scripting (XSS) vulnerability in Axigen versions 10.3.3.0 before 10.3.3.59, 10.4.0 before 10.4.19, and 10.5.0 before 10.5.5, allows authenticated attackers to execute arbitrary code and obtain sensitive information via the logic for switching between the Standard and Ajax versions.



- [https://github.com/ace-83/CVE-2023-40355](https://github.com/ace-83/CVE-2023-40355) :  ![starts](https://img.shields.io/github/stars/ace-83/CVE-2023-40355.svg) ![forks](https://img.shields.io/github/forks/ace-83/CVE-2023-40355.svg)

## CVE-2023-40297
 Stakater Forecastle 1.0.139 and before allows %5C../ directory traversal in the website component.



- [https://github.com/sahar042/CVE-2023-40297](https://github.com/sahar042/CVE-2023-40297) :  ![starts](https://img.shields.io/github/stars/sahar042/CVE-2023-40297.svg) ![forks](https://img.shields.io/github/forks/sahar042/CVE-2023-40297.svg)

## CVE-2023-40296
 async-sockets-cpp through 0.3.1 has a stack-based buffer overflow in ReceiveFrom and Receive in udpsocket.hpp when processing malformed UDP packets.



- [https://github.com/Halcy0nic/CVE-2023-40296](https://github.com/Halcy0nic/CVE-2023-40296) :  ![starts](https://img.shields.io/github/stars/Halcy0nic/CVE-2023-40296.svg) ![forks](https://img.shields.io/github/forks/Halcy0nic/CVE-2023-40296.svg)

## CVE-2023-40295
 libboron in Boron 2.0.8 has a heap-based buffer overflow in ur_strInitUtf8 at string.c.



- [https://github.com/Halcy0nic/CVE-2023-40294-and-CVE-2023-40295](https://github.com/Halcy0nic/CVE-2023-40294-and-CVE-2023-40295) :  ![starts](https://img.shields.io/github/stars/Halcy0nic/CVE-2023-40294-and-CVE-2023-40295.svg) ![forks](https://img.shields.io/github/forks/Halcy0nic/CVE-2023-40294-and-CVE-2023-40295.svg)

## CVE-2023-40294
 libboron in Boron 2.0.8 has a heap-based buffer overflow in ur_parseBlockI at i_parse_blk.c.



- [https://github.com/Halcy0nic/CVE-2023-40294-and-CVE-2023-40295](https://github.com/Halcy0nic/CVE-2023-40294-and-CVE-2023-40295) :  ![starts](https://img.shields.io/github/stars/Halcy0nic/CVE-2023-40294-and-CVE-2023-40295.svg) ![forks](https://img.shields.io/github/forks/Halcy0nic/CVE-2023-40294-and-CVE-2023-40295.svg)

## CVE-2023-40133
 In multiple locations of DialogFillUi.java, there is a possible way to view another user's images due to a confused deputy. This could lead to local information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/uthrasri/frame_CVE-2023-40133_136_137](https://github.com/uthrasri/frame_CVE-2023-40133_136_137) :  ![starts](https://img.shields.io/github/stars/uthrasri/frame_CVE-2023-40133_136_137.svg) ![forks](https://img.shields.io/github/forks/uthrasri/frame_CVE-2023-40133_136_137.svg)

## CVE-2023-40130
 In onBindingDied of CallRedirectionProcessor.java, there is a possible permission bypass due to a logic error in the code. This could lead to local escalation of privilege and background activity launch with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/wrlu/CVE-2023-40130](https://github.com/wrlu/CVE-2023-40130) :  ![starts](https://img.shields.io/github/stars/wrlu/CVE-2023-40130.svg) ![forks](https://img.shields.io/github/forks/wrlu/CVE-2023-40130.svg)

## CVE-2023-40127
 In multiple locations, there is a possible way to access screenshots due to a confused deputy. This could lead to local information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/Trinadh465/CVE-2023-40127](https://github.com/Trinadh465/CVE-2023-40127) :  ![starts](https://img.shields.io/github/stars/Trinadh465/CVE-2023-40127.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/CVE-2023-40127.svg)

- [https://github.com/RenukaSelvar/packages_providers_MediaProvider_CVE-2023-40127](https://github.com/RenukaSelvar/packages_providers_MediaProvider_CVE-2023-40127) :  ![starts](https://img.shields.io/github/stars/RenukaSelvar/packages_providers_MediaProvider_CVE-2023-40127.svg) ![forks](https://img.shields.io/github/forks/RenukaSelvar/packages_providers_MediaProvider_CVE-2023-40127.svg)

- [https://github.com/saurabh2088/platform_packages_providers_MediaProvider_CVE-2023-40127](https://github.com/saurabh2088/platform_packages_providers_MediaProvider_CVE-2023-40127) :  ![starts](https://img.shields.io/github/stars/saurabh2088/platform_packages_providers_MediaProvider_CVE-2023-40127.svg) ![forks](https://img.shields.io/github/forks/saurabh2088/platform_packages_providers_MediaProvider_CVE-2023-40127.svg)

- [https://github.com/RenukaSelvar/platform_packages_providers_MediaProvider_CVE-2023-40127](https://github.com/RenukaSelvar/platform_packages_providers_MediaProvider_CVE-2023-40127) :  ![starts](https://img.shields.io/github/stars/RenukaSelvar/platform_packages_providers_MediaProvider_CVE-2023-40127.svg) ![forks](https://img.shields.io/github/forks/RenukaSelvar/platform_packages_providers_MediaProvider_CVE-2023-40127.svg)

- [https://github.com/Trinadh465/platform_packages_providers_MediaProvider_CVE-2023-40127](https://github.com/Trinadh465/platform_packages_providers_MediaProvider_CVE-2023-40127) :  ![starts](https://img.shields.io/github/stars/Trinadh465/platform_packages_providers_MediaProvider_CVE-2023-40127.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/platform_packages_providers_MediaProvider_CVE-2023-40127.svg)

## CVE-2023-40109
 In createFromParcel of UsbConfiguration.java, there is a possible background activity launch (BAL) due to a permissions bypass. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is needed for exploitation.



- [https://github.com/uthrasri/CVE-2023-40109](https://github.com/uthrasri/CVE-2023-40109) :  ![starts](https://img.shields.io/github/stars/uthrasri/CVE-2023-40109.svg) ![forks](https://img.shields.io/github/forks/uthrasri/CVE-2023-40109.svg)

## CVE-2023-40084
 In run of MDnsSdListener.cpp, there is a possible memory corruption due to a use after free. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/Trinadh465/platform_system_netd_AOSP10_r33_CVE-2023-40084](https://github.com/Trinadh465/platform_system_netd_AOSP10_r33_CVE-2023-40084) :  ![starts](https://img.shields.io/github/stars/Trinadh465/platform_system_netd_AOSP10_r33_CVE-2023-40084.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/platform_system_netd_AOSP10_r33_CVE-2023-40084.svg)

## CVE-2023-40044
 In WS_FTP Server versions prior to 8.7.4 and 8.8.2, a pre-authenticated attacker could leverage a .NET deserialization vulnerability in the Ad Hoc Transfer module to execute remote commands on the underlying WS_FTP Server operating system.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/kenbuckler/WS_FTP-CVE-2023-40044](https://github.com/kenbuckler/WS_FTP-CVE-2023-40044) :  ![starts](https://img.shields.io/github/stars/kenbuckler/WS_FTP-CVE-2023-40044.svg) ![forks](https://img.shields.io/github/forks/kenbuckler/WS_FTP-CVE-2023-40044.svg)

## CVE-2023-40039
 An issue was discovered on ARRIS TG852G, TG862G, and TG1672G devices. A remote attacker (in proximity to a Wi-Fi network) can derive the default WPA2-PSK value by observing a beacon frame.



- [https://github.com/actuator/BSIDES-Security-Las-Vegas-2024](https://github.com/actuator/BSIDES-Security-Las-Vegas-2024) :  ![starts](https://img.shields.io/github/stars/actuator/BSIDES-Security-Las-Vegas-2024.svg) ![forks](https://img.shields.io/github/forks/actuator/BSIDES-Security-Las-Vegas-2024.svg)

## CVE-2023-40038
 Arris DG860A and DG1670A devices have predictable default WPA2 PSKs that could lead to unauthorized remote access. (They use the first 6 characters of the SSID and the last 6 characters of the BSSID, decrementing the last digit.)



- [https://github.com/actuator/BSIDES-Security-Las-Vegas-2024](https://github.com/actuator/BSIDES-Security-Las-Vegas-2024) :  ![starts](https://img.shields.io/github/stars/actuator/BSIDES-Security-Las-Vegas-2024.svg) ![forks](https://img.shields.io/github/forks/actuator/BSIDES-Security-Las-Vegas-2024.svg)

## CVE-2023-40037
 Apache NiFi 1.21.0 through 1.23.0 support JDBC and JNDI JMS access in several Processors and Controller Services with connection URL validation that does not provide sufficient protection against crafted inputs. An authenticated and authorized user can bypass connection URL validation using custom input formatting. The resolution enhances connection URL validation and introduces validation for additional related properties. Upgrading to Apache NiFi 1.23.1 is the recommended mitigation.



- [https://github.com/mbadanoiu/CVE-2023-40037](https://github.com/mbadanoiu/CVE-2023-40037) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2023-40037.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2023-40037.svg)

## CVE-2023-40031
 Notepad++ is a free and open-source source code editor. Versions 8.5.6 and prior are vulnerable to heap buffer write overflow in `Utf8_16_Read::convert`. This issue may lead to arbitrary code execution. As of time of publication, no known patches are available in existing versions of Notepad++.



- [https://github.com/webraybtl/CVE-2023-40031](https://github.com/webraybtl/CVE-2023-40031) :  ![starts](https://img.shields.io/github/stars/webraybtl/CVE-2023-40031.svg) ![forks](https://img.shields.io/github/forks/webraybtl/CVE-2023-40031.svg)

## CVE-2023-40028
 Ghost is an open source content management system. Versions prior to 5.59.1 are subject to a vulnerability which allows authenticated users to upload files that are symlinks. This can be exploited to perform an arbitrary file read of any file on the host operating system. Site administrators can check for exploitation of this issue by looking for unknown symlinks within Ghost's `content/` folder. Version 5.59.1 contains a fix for this issue. All users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/0xyassine/CVE-2023-40028](https://github.com/0xyassine/CVE-2023-40028) :  ![starts](https://img.shields.io/github/stars/0xyassine/CVE-2023-40028.svg) ![forks](https://img.shields.io/github/forks/0xyassine/CVE-2023-40028.svg)

- [https://github.com/0xDTC/Ghost-5.58-Arbitrary-File-Read-CVE-2023-40028](https://github.com/0xDTC/Ghost-5.58-Arbitrary-File-Read-CVE-2023-40028) :  ![starts](https://img.shields.io/github/stars/0xDTC/Ghost-5.58-Arbitrary-File-Read-CVE-2023-40028.svg) ![forks](https://img.shields.io/github/forks/0xDTC/Ghost-5.58-Arbitrary-File-Read-CVE-2023-40028.svg)

- [https://github.com/monke443/CVE-2023-40028](https://github.com/monke443/CVE-2023-40028) :  ![starts](https://img.shields.io/github/stars/monke443/CVE-2023-40028.svg) ![forks](https://img.shields.io/github/forks/monke443/CVE-2023-40028.svg)

- [https://github.com/rvizx/CVE-2023-40028](https://github.com/rvizx/CVE-2023-40028) :  ![starts](https://img.shields.io/github/stars/rvizx/CVE-2023-40028.svg) ![forks](https://img.shields.io/github/forks/rvizx/CVE-2023-40028.svg)

- [https://github.com/buutt3rf1y/CVE-2023-40028](https://github.com/buutt3rf1y/CVE-2023-40028) :  ![starts](https://img.shields.io/github/stars/buutt3rf1y/CVE-2023-40028.svg) ![forks](https://img.shields.io/github/forks/buutt3rf1y/CVE-2023-40028.svg)

- [https://github.com/sudlit/CVE-2023-40028](https://github.com/sudlit/CVE-2023-40028) :  ![starts](https://img.shields.io/github/stars/sudlit/CVE-2023-40028.svg) ![forks](https://img.shields.io/github/forks/sudlit/CVE-2023-40028.svg)

## CVE-2023-40000
 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in LiteSpeed Technologies LiteSpeed Cache allows Stored XSS.This issue affects LiteSpeed Cache: from n/a through 5.7.





- [https://github.com/rxerium/CVE-2023-40000](https://github.com/rxerium/CVE-2023-40000) :  ![starts](https://img.shields.io/github/stars/rxerium/CVE-2023-40000.svg) ![forks](https://img.shields.io/github/forks/rxerium/CVE-2023-40000.svg)

- [https://github.com/quantiom/litespeed-cache-xss-poc](https://github.com/quantiom/litespeed-cache-xss-poc) :  ![starts](https://img.shields.io/github/stars/quantiom/litespeed-cache-xss-poc.svg) ![forks](https://img.shields.io/github/forks/quantiom/litespeed-cache-xss-poc.svg)

- [https://github.com/iveresk/cve-2023-40000](https://github.com/iveresk/cve-2023-40000) :  ![starts](https://img.shields.io/github/stars/iveresk/cve-2023-40000.svg) ![forks](https://img.shields.io/github/forks/iveresk/cve-2023-40000.svg)

## CVE-2023-39910
 The cryptocurrency wallet entropy seeding mechanism used in Libbitcoin Explorer 3.0.0 through 3.6.0 is weak, aka the Milk Sad issue. The use of an mt19937 Mersenne Twister PRNG restricts the internal entropy to 32 bits regardless of settings. This allows remote attackers to recover any wallet private keys generated from "bx seed" entropy output and steal funds. (Affected users need to move funds to a secure new cryptocurrency wallet.) NOTE: the vendor's position is that there was sufficient documentation advising against "bx seed" but others disagree. NOTE: this was exploited in the wild in June and July 2023.



- [https://github.com/z1ph1us/MilkSad-Mnemonic-Generator](https://github.com/z1ph1us/MilkSad-Mnemonic-Generator) :  ![starts](https://img.shields.io/github/stars/z1ph1us/MilkSad-Mnemonic-Generator.svg) ![forks](https://img.shields.io/github/forks/z1ph1us/MilkSad-Mnemonic-Generator.svg)

## CVE-2023-39725
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/anky-123/CVE-2023-39725](https://github.com/anky-123/CVE-2023-39725) :  ![starts](https://img.shields.io/github/stars/anky-123/CVE-2023-39725.svg) ![forks](https://img.shields.io/github/forks/anky-123/CVE-2023-39725.svg)

## CVE-2023-39714
 Multiple cross-site scripting (XSS) vulnerabilities in Free and Open Source Inventory Management System v1.0 allows attackers to execute arbitrary web scripts or HTML via injecting a crafted payload into the Name, Address, and Company parameters under the Add New Member section.



- [https://github.com/Arajawat007/CVE-2023-39714](https://github.com/Arajawat007/CVE-2023-39714) :  ![starts](https://img.shields.io/github/stars/Arajawat007/CVE-2023-39714.svg) ![forks](https://img.shields.io/github/forks/Arajawat007/CVE-2023-39714.svg)

## CVE-2023-39712
 Multiple cross-site scripting (XSS) vulnerabilities in Free and Open Source Inventory Management System v1.0 allows attackers to execute arbitrary web scripts or HTML via injecting a crafted payload into the Name, Address, and Company parameters under the Add New Put section.



- [https://github.com/Arajawat007/CVE-2023-39712](https://github.com/Arajawat007/CVE-2023-39712) :  ![starts](https://img.shields.io/github/stars/Arajawat007/CVE-2023-39712.svg) ![forks](https://img.shields.io/github/forks/Arajawat007/CVE-2023-39712.svg)

## CVE-2023-39711
 Multiple cross-site scripting (XSS) vulnerabilities in Free and Open Source Inventory Management System v1.0 allows attackers to execute arbitrary web scripts or HTML via injecting a crafted payload into the Subtotal and Paidbill parameters under the Add New Put section.



- [https://github.com/Arajawat007/CVE-2023-39711](https://github.com/Arajawat007/CVE-2023-39711) :  ![starts](https://img.shields.io/github/stars/Arajawat007/CVE-2023-39711.svg) ![forks](https://img.shields.io/github/forks/Arajawat007/CVE-2023-39711.svg)

## CVE-2023-39710
 Multiple cross-site scripting (XSS) vulnerabilities in Free and Open Source Inventory Management System v1.0 allows attackers to execute arbitrary web scripts or HTML via injecting a crafted payload into the Name, Address, and Company parameters under the Add Customer section.



- [https://github.com/Arajawat007/CVE-2023-39710](https://github.com/Arajawat007/CVE-2023-39710) :  ![starts](https://img.shields.io/github/stars/Arajawat007/CVE-2023-39710.svg) ![forks](https://img.shields.io/github/forks/Arajawat007/CVE-2023-39710.svg)

## CVE-2023-39709
 Multiple cross-site scripting (XSS) vulnerabilities in Free and Open Source Inventory Management System v1.0 allows attackers to execute arbitrary web scripts or HTML via injecting a crafted payload into the Name, Address, and Company parameters under the Add Member section.



- [https://github.com/Arajawat007/CVE-2023-39709](https://github.com/Arajawat007/CVE-2023-39709) :  ![starts](https://img.shields.io/github/stars/Arajawat007/CVE-2023-39709.svg) ![forks](https://img.shields.io/github/forks/Arajawat007/CVE-2023-39709.svg)

## CVE-2023-39708
 A stored cross-site scripting (XSS) vulnerability in Free and Open Source Inventory Management System v1.0 allows attackers to execute arbitrary web scripts or HTML via injecting a crafted payload into the Add New parameter under the New Buy section.



- [https://github.com/Arajawat007/CVE-2023-39708](https://github.com/Arajawat007/CVE-2023-39708) :  ![starts](https://img.shields.io/github/stars/Arajawat007/CVE-2023-39708.svg) ![forks](https://img.shields.io/github/forks/Arajawat007/CVE-2023-39708.svg)

## CVE-2023-39707
 A stored cross-site scripting (XSS) vulnerability in Free and Open Source Inventory Management System v1.0 allows attackers to execute arbitrary web scripts or HTML via injecting a crafted payload into the Add Expense parameter under the Expense section.



- [https://github.com/Arajawat007/CVE-2023-39707](https://github.com/Arajawat007/CVE-2023-39707) :  ![starts](https://img.shields.io/github/stars/Arajawat007/CVE-2023-39707.svg) ![forks](https://img.shields.io/github/forks/Arajawat007/CVE-2023-39707.svg)

## CVE-2023-39593
 Insecure permissions in the sys_exec function of MariaDB v10.5 allows authenticated attackers to execute arbitrary commands with elevated privileges. NOTE: this is disputed by the MariaDB Foundation because no privilege boundary is crossed.



- [https://github.com/Ant1sec-ops/CVE-2023-39593](https://github.com/Ant1sec-ops/CVE-2023-39593) :  ![starts](https://img.shields.io/github/stars/Ant1sec-ops/CVE-2023-39593.svg) ![forks](https://img.shields.io/github/forks/Ant1sec-ops/CVE-2023-39593.svg)

## CVE-2023-39539
 
AMI AptioV contains a vulnerability in BIOS where a User may cause an unrestricted upload of a PNG Logo file with dangerous type by Local access. A successful exploit of this vulnerability may lead to a loss of Confidentiality, Integrity, and/or Availability. 









- [https://github.com/AdamWen230/CVE-2023-39539-PoC](https://github.com/AdamWen230/CVE-2023-39539-PoC) :  ![starts](https://img.shields.io/github/stars/AdamWen230/CVE-2023-39539-PoC.svg) ![forks](https://img.shields.io/github/forks/AdamWen230/CVE-2023-39539-PoC.svg)

## CVE-2023-39527
 PrestaShop is an open source e-commerce web application. Versions prior to 1.7.8.10, 8.0.5, and 8.1.1 are vulnerable to cross-site scripting through the `isCleanHTML` method. Versions 1.7.8.10, 8.0.5, and 8.1.1 contain a patch. There are no known workarounds.



- [https://github.com/dnkhack/fixcve2023_39526_2023_39527](https://github.com/dnkhack/fixcve2023_39526_2023_39527) :  ![starts](https://img.shields.io/github/stars/dnkhack/fixcve2023_39526_2023_39527.svg) ![forks](https://img.shields.io/github/forks/dnkhack/fixcve2023_39526_2023_39527.svg)

## CVE-2023-39526
 PrestaShop is an open source e-commerce web application. Versions prior to 1.7.8.10, 8.0.5, and 8.1.1 are vulnerable to remote code execution through SQL injection and arbitrary file write in the back office. Versions 1.7.8.10, 8.0.5, and 8.1.1 contain a patch. There are no known workarounds.



- [https://github.com/dnkhack/fixcve2023_39526_2023_39527](https://github.com/dnkhack/fixcve2023_39526_2023_39527) :  ![starts](https://img.shields.io/github/stars/dnkhack/fixcve2023_39526_2023_39527.svg) ![forks](https://img.shields.io/github/forks/dnkhack/fixcve2023_39526_2023_39527.svg)

## CVE-2023-39362
 Cacti is an open source operational monitoring and fault management framework. In Cacti 1.2.24, under certain conditions, an authenticated privileged user, can use a malicious string in the SNMP options of a Device, performing command injection and obtaining remote code execution on the underlying server. The `lib/snmp.php` file has a set of functions, with similar behavior, that accept in input some variables and place them into an `exec` call without a proper escape or validation. This issue has been addressed in version 1.2.25. Users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/jakabakos/CVE-2023-39362-cacti-snmp-command-injection-poc](https://github.com/jakabakos/CVE-2023-39362-cacti-snmp-command-injection-poc) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2023-39362-cacti-snmp-command-injection-poc.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2023-39362-cacti-snmp-command-injection-poc.svg)

- [https://github.com/m3ssap0/cacti-rce-snmp-options-vulnerable-application](https://github.com/m3ssap0/cacti-rce-snmp-options-vulnerable-application) :  ![starts](https://img.shields.io/github/stars/m3ssap0/cacti-rce-snmp-options-vulnerable-application.svg) ![forks](https://img.shields.io/github/forks/m3ssap0/cacti-rce-snmp-options-vulnerable-application.svg)

## CVE-2023-39361
 Cacti is an open source operational monitoring and fault management framework. Affected versions are subject to a SQL injection discovered in graph_view.php. Since guest users can access graph_view.php without authentication by default, if guest users are being utilized in an enabled state, there could be the potential for significant damage. Attackers may exploit this vulnerability, and there may be possibilities for actions such as the usurpation of administrative privileges or remote code execution. This issue has been addressed in version 1.2.25. Users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/HPT-Intern-Task-Submission/CVE-2023-39361](https://github.com/HPT-Intern-Task-Submission/CVE-2023-39361) :  ![starts](https://img.shields.io/github/stars/HPT-Intern-Task-Submission/CVE-2023-39361.svg) ![forks](https://img.shields.io/github/forks/HPT-Intern-Task-Submission/CVE-2023-39361.svg)

- [https://github.com/ChoDeokCheol/CVE-2023-39361](https://github.com/ChoDeokCheol/CVE-2023-39361) :  ![starts](https://img.shields.io/github/stars/ChoDeokCheol/CVE-2023-39361.svg) ![forks](https://img.shields.io/github/forks/ChoDeokCheol/CVE-2023-39361.svg)

## CVE-2023-39320
 The go.mod toolchain directive, introduced in Go 1.21, can be leveraged to execute scripts and binaries relative to the root of the module when the "go" command was executed within the module. This applies to modules downloaded using the "go" command from the module proxy, as well as modules downloaded directly using VCS software.



- [https://github.com/ayrustogaru/cve-2023-39320](https://github.com/ayrustogaru/cve-2023-39320) :  ![starts](https://img.shields.io/github/stars/ayrustogaru/cve-2023-39320.svg) ![forks](https://img.shields.io/github/forks/ayrustogaru/cve-2023-39320.svg)

## CVE-2023-39144
 Element55 KnowMore appliances version 21 and older was discovered to store passwords in plaintext.



- [https://github.com/cduram/CVE-2023-39144](https://github.com/cduram/CVE-2023-39144) :  ![starts](https://img.shields.io/github/stars/cduram/CVE-2023-39144.svg) ![forks](https://img.shields.io/github/forks/cduram/CVE-2023-39144.svg)

## CVE-2023-39141
 webui-aria2 commit 4fe2e was discovered to contain a path traversal vulnerability.



- [https://github.com/MartiSabate/CVE-2023-39141-LFI-enumerator](https://github.com/MartiSabate/CVE-2023-39141-LFI-enumerator) :  ![starts](https://img.shields.io/github/stars/MartiSabate/CVE-2023-39141-LFI-enumerator.svg) ![forks](https://img.shields.io/github/forks/MartiSabate/CVE-2023-39141-LFI-enumerator.svg)

## CVE-2023-39115
 install/aiz-uploader/upload in Campcodes Online Matrimonial Website System Script 3.3 allows XSS via a crafted SVG document.



- [https://github.com/Raj789-sec/CVE-2023-39115](https://github.com/Raj789-sec/CVE-2023-39115) :  ![starts](https://img.shields.io/github/stars/Raj789-sec/CVE-2023-39115.svg) ![forks](https://img.shields.io/github/forks/Raj789-sec/CVE-2023-39115.svg)

## CVE-2023-39063
 Buffer Overflow vulnerability in RaidenFTPD 2.4.4005 allows a local attacker to execute arbitrary code via the Server name field of the Step by step setup wizard.



- [https://github.com/AndreGNogueira/CVE-2023-39063](https://github.com/AndreGNogueira/CVE-2023-39063) :  ![starts](https://img.shields.io/github/stars/AndreGNogueira/CVE-2023-39063.svg) ![forks](https://img.shields.io/github/forks/AndreGNogueira/CVE-2023-39063.svg)

## CVE-2023-39062
 Cross Site Scripting vulnerability in Spipu HTML2PDF before v.5.2.8 allows a remote attacker to execute arbitrary code via a crafted script to the forms.php.



- [https://github.com/afine-com/CVE-2023-39062](https://github.com/afine-com/CVE-2023-39062) :  ![starts](https://img.shields.io/github/stars/afine-com/CVE-2023-39062.svg) ![forks](https://img.shields.io/github/forks/afine-com/CVE-2023-39062.svg)

## CVE-2023-39025
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/BenTheCyberOne/CVE-2023-39024-5-POC](https://github.com/BenTheCyberOne/CVE-2023-39024-5-POC) :  ![starts](https://img.shields.io/github/stars/BenTheCyberOne/CVE-2023-39024-5-POC.svg) ![forks](https://img.shields.io/github/forks/BenTheCyberOne/CVE-2023-39024-5-POC.svg)

## CVE-2023-39024
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/BenTheCyberOne/CVE-2023-39024-5-POC](https://github.com/BenTheCyberOne/CVE-2023-39024-5-POC) :  ![starts](https://img.shields.io/github/stars/BenTheCyberOne/CVE-2023-39024-5-POC.svg) ![forks](https://img.shields.io/github/forks/BenTheCyberOne/CVE-2023-39024-5-POC.svg)

## CVE-2023-38891
 SQL injection vulnerability in Vtiger CRM v.7.5.0 allows a remote authenticated attacker to escalate privileges via the getQueryColumnsList function in ReportRun.php.



- [https://github.com/jselliott/CVE-2023-38891](https://github.com/jselliott/CVE-2023-38891) :  ![starts](https://img.shields.io/github/stars/jselliott/CVE-2023-38891.svg) ![forks](https://img.shields.io/github/forks/jselliott/CVE-2023-38891.svg)

## CVE-2023-38890
 Online Shopping Portal Project 3.1 allows remote attackers to execute arbitrary SQL commands/queries via the login form, leading to unauthorized access and potential data manipulation. This vulnerability arises due to insufficient validation of user-supplied input in the username field, enabling SQL Injection attacks.



- [https://github.com/akshadjoshi/CVE-2023-38890](https://github.com/akshadjoshi/CVE-2023-38890) :  ![starts](https://img.shields.io/github/stars/akshadjoshi/CVE-2023-38890.svg) ![forks](https://img.shields.io/github/forks/akshadjoshi/CVE-2023-38890.svg)

## CVE-2023-38840
 Bitwarden Desktop 2023.7.0 and below allows an attacker with local access to obtain sensitive information via the Bitwarden.exe process.



- [https://github.com/markuta/bw-dump](https://github.com/markuta/bw-dump) :  ![starts](https://img.shields.io/github/stars/markuta/bw-dump.svg) ![forks](https://img.shields.io/github/forks/markuta/bw-dump.svg)

## CVE-2023-38836
 File Upload vulnerability in BoidCMS v.2.0.0 allows a remote attacker to execute arbitrary code by adding a GIF header to bypass MIME type checks.



- [https://github.com/1337kid/CVE-2023-38836](https://github.com/1337kid/CVE-2023-38836) :  ![starts](https://img.shields.io/github/stars/1337kid/CVE-2023-38836.svg) ![forks](https://img.shields.io/github/forks/1337kid/CVE-2023-38836.svg)

## CVE-2023-38831
 RARLAB WinRAR before 6.23 allows attackers to execute arbitrary code when a user attempts to view a benign file within a ZIP archive. The issue occurs because a ZIP archive may include a benign file (such as an ordinary .JPG file) and also a folder that has the same name as the benign file, and the contents of the folder (which may include executable content) are processed during an attempt to access only the benign file. This was exploited in the wild in April through October 2023.



- [https://github.com/b1tg/CVE-2023-38831-winrar-exploit](https://github.com/b1tg/CVE-2023-38831-winrar-exploit) :  ![starts](https://img.shields.io/github/stars/b1tg/CVE-2023-38831-winrar-exploit.svg) ![forks](https://img.shields.io/github/forks/b1tg/CVE-2023-38831-winrar-exploit.svg)

- [https://github.com/Garck3h/cve-2023-38831](https://github.com/Garck3h/cve-2023-38831) :  ![starts](https://img.shields.io/github/stars/Garck3h/cve-2023-38831.svg) ![forks](https://img.shields.io/github/forks/Garck3h/cve-2023-38831.svg)

- [https://github.com/ignis-sec/CVE-2023-38831-RaRCE](https://github.com/ignis-sec/CVE-2023-38831-RaRCE) :  ![starts](https://img.shields.io/github/stars/ignis-sec/CVE-2023-38831-RaRCE.svg) ![forks](https://img.shields.io/github/forks/ignis-sec/CVE-2023-38831-RaRCE.svg)

- [https://github.com/BoredHackerBlog/winrar_CVE-2023-38831_lazy_poc](https://github.com/BoredHackerBlog/winrar_CVE-2023-38831_lazy_poc) :  ![starts](https://img.shields.io/github/stars/BoredHackerBlog/winrar_CVE-2023-38831_lazy_poc.svg) ![forks](https://img.shields.io/github/forks/BoredHackerBlog/winrar_CVE-2023-38831_lazy_poc.svg)

- [https://github.com/HDCE-inc/CVE-2023-38831](https://github.com/HDCE-inc/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/HDCE-inc/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/HDCE-inc/CVE-2023-38831.svg)

- [https://github.com/knight0x07/WinRAR-Code-Execution-Vulnerability-CVE-2023-38831](https://github.com/knight0x07/WinRAR-Code-Execution-Vulnerability-CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/knight0x07/WinRAR-Code-Execution-Vulnerability-CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/knight0x07/WinRAR-Code-Execution-Vulnerability-CVE-2023-38831.svg)

- [https://github.com/Maalfer/CVE-2023-38831_ReverseShell_Winrar-RCE](https://github.com/Maalfer/CVE-2023-38831_ReverseShell_Winrar-RCE) :  ![starts](https://img.shields.io/github/stars/Maalfer/CVE-2023-38831_ReverseShell_Winrar-RCE.svg) ![forks](https://img.shields.io/github/forks/Maalfer/CVE-2023-38831_ReverseShell_Winrar-RCE.svg)

- [https://github.com/xaitax/WinRAR-CVE-2023-38831](https://github.com/xaitax/WinRAR-CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/xaitax/WinRAR-CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/xaitax/WinRAR-CVE-2023-38831.svg)

- [https://github.com/MorDavid/CVE-2023-38831-Winrar-Exploit-Generator-POC](https://github.com/MorDavid/CVE-2023-38831-Winrar-Exploit-Generator-POC) :  ![starts](https://img.shields.io/github/stars/MorDavid/CVE-2023-38831-Winrar-Exploit-Generator-POC.svg) ![forks](https://img.shields.io/github/forks/MorDavid/CVE-2023-38831-Winrar-Exploit-Generator-POC.svg)

- [https://github.com/ahmed-fa7im/CVE-2023-38831-winrar-expoit-simple-Poc](https://github.com/ahmed-fa7im/CVE-2023-38831-winrar-expoit-simple-Poc) :  ![starts](https://img.shields.io/github/stars/ahmed-fa7im/CVE-2023-38831-winrar-expoit-simple-Poc.svg) ![forks](https://img.shields.io/github/forks/ahmed-fa7im/CVE-2023-38831-winrar-expoit-simple-Poc.svg)

- [https://github.com/youmulijiang/evil-winrar](https://github.com/youmulijiang/evil-winrar) :  ![starts](https://img.shields.io/github/stars/youmulijiang/evil-winrar.svg) ![forks](https://img.shields.io/github/forks/youmulijiang/evil-winrar.svg)

- [https://github.com/Malwareman007/CVE-2023-38831](https://github.com/Malwareman007/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/Malwareman007/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/Malwareman007/CVE-2023-38831.svg)

- [https://github.com/z3r0sw0rd/CVE-2023-38831-PoC](https://github.com/z3r0sw0rd/CVE-2023-38831-PoC) :  ![starts](https://img.shields.io/github/stars/z3r0sw0rd/CVE-2023-38831-PoC.svg) ![forks](https://img.shields.io/github/forks/z3r0sw0rd/CVE-2023-38831-PoC.svg)

- [https://github.com/PascalAsch/CVE-2023-38831-KQL](https://github.com/PascalAsch/CVE-2023-38831-KQL) :  ![starts](https://img.shields.io/github/stars/PascalAsch/CVE-2023-38831-KQL.svg) ![forks](https://img.shields.io/github/forks/PascalAsch/CVE-2023-38831-KQL.svg)

- [https://github.com/UnHackerEnCapital/PDFernetRemotelo](https://github.com/UnHackerEnCapital/PDFernetRemotelo) :  ![starts](https://img.shields.io/github/stars/UnHackerEnCapital/PDFernetRemotelo.svg) ![forks](https://img.shields.io/github/forks/UnHackerEnCapital/PDFernetRemotelo.svg)

- [https://github.com/xk-mt/WinRAR-Vulnerability-recurrence-tutorial](https://github.com/xk-mt/WinRAR-Vulnerability-recurrence-tutorial) :  ![starts](https://img.shields.io/github/stars/xk-mt/WinRAR-Vulnerability-recurrence-tutorial.svg) ![forks](https://img.shields.io/github/forks/xk-mt/WinRAR-Vulnerability-recurrence-tutorial.svg)

- [https://github.com/akhomlyuk/cve-2023-38831](https://github.com/akhomlyuk/cve-2023-38831) :  ![starts](https://img.shields.io/github/stars/akhomlyuk/cve-2023-38831.svg) ![forks](https://img.shields.io/github/forks/akhomlyuk/cve-2023-38831.svg)

- [https://github.com/malvika-thakur/CVE-2023-38831](https://github.com/malvika-thakur/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/malvika-thakur/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/malvika-thakur/CVE-2023-38831.svg)

- [https://github.com/Mich-ele/CVE-2023-38831-winrar](https://github.com/Mich-ele/CVE-2023-38831-winrar) :  ![starts](https://img.shields.io/github/stars/Mich-ele/CVE-2023-38831-winrar.svg) ![forks](https://img.shields.io/github/forks/Mich-ele/CVE-2023-38831-winrar.svg)

- [https://github.com/ameerpornillos/CVE-2023-38831-WinRAR-Exploit](https://github.com/ameerpornillos/CVE-2023-38831-WinRAR-Exploit) :  ![starts](https://img.shields.io/github/stars/ameerpornillos/CVE-2023-38831-WinRAR-Exploit.svg) ![forks](https://img.shields.io/github/forks/ameerpornillos/CVE-2023-38831-WinRAR-Exploit.svg)

- [https://github.com/SugiB3o/Keylog_CVE2023-38831](https://github.com/SugiB3o/Keylog_CVE2023-38831) :  ![starts](https://img.shields.io/github/stars/SugiB3o/Keylog_CVE2023-38831.svg) ![forks](https://img.shields.io/github/forks/SugiB3o/Keylog_CVE2023-38831.svg)

- [https://github.com/IR-HuntGuardians/CVE-2023-38831-HUNT](https://github.com/IR-HuntGuardians/CVE-2023-38831-HUNT) :  ![starts](https://img.shields.io/github/stars/IR-HuntGuardians/CVE-2023-38831-HUNT.svg) ![forks](https://img.shields.io/github/forks/IR-HuntGuardians/CVE-2023-38831-HUNT.svg)

- [https://github.com/RonF98/CVE-2023-38831-POC](https://github.com/RonF98/CVE-2023-38831-POC) :  ![starts](https://img.shields.io/github/stars/RonF98/CVE-2023-38831-POC.svg) ![forks](https://img.shields.io/github/forks/RonF98/CVE-2023-38831-POC.svg)

- [https://github.com/r1yaz/winDED](https://github.com/r1yaz/winDED) :  ![starts](https://img.shields.io/github/stars/r1yaz/winDED.svg) ![forks](https://img.shields.io/github/forks/r1yaz/winDED.svg)

- [https://github.com/MaorBuskila/Windows-X64-RAT](https://github.com/MaorBuskila/Windows-X64-RAT) :  ![starts](https://img.shields.io/github/stars/MaorBuskila/Windows-X64-RAT.svg) ![forks](https://img.shields.io/github/forks/MaorBuskila/Windows-X64-RAT.svg)

- [https://github.com/kuyrathdaro/winrar-cve-2023-38831](https://github.com/kuyrathdaro/winrar-cve-2023-38831) :  ![starts](https://img.shields.io/github/stars/kuyrathdaro/winrar-cve-2023-38831.svg) ![forks](https://img.shields.io/github/forks/kuyrathdaro/winrar-cve-2023-38831.svg)

- [https://github.com/SpamixOfficial/CVE-2023-38831](https://github.com/SpamixOfficial/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/SpamixOfficial/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/SpamixOfficial/CVE-2023-38831.svg)

- [https://github.com/elefantesagradodeluzinfinita/cve-2023-38831](https://github.com/elefantesagradodeluzinfinita/cve-2023-38831) :  ![starts](https://img.shields.io/github/stars/elefantesagradodeluzinfinita/cve-2023-38831.svg) ![forks](https://img.shields.io/github/forks/elefantesagradodeluzinfinita/cve-2023-38831.svg)

- [https://github.com/ruycr4ft/CVE-2023-38831](https://github.com/ruycr4ft/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/ruycr4ft/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/ruycr4ft/CVE-2023-38831.svg)

- [https://github.com/yezzfusl/cve_2023_38831_scanner](https://github.com/yezzfusl/cve_2023_38831_scanner) :  ![starts](https://img.shields.io/github/stars/yezzfusl/cve_2023_38831_scanner.svg) ![forks](https://img.shields.io/github/forks/yezzfusl/cve_2023_38831_scanner.svg)

- [https://github.com/s4m98/winrar-cve-2023-38831-poc-gen](https://github.com/s4m98/winrar-cve-2023-38831-poc-gen) :  ![starts](https://img.shields.io/github/stars/s4m98/winrar-cve-2023-38831-poc-gen.svg) ![forks](https://img.shields.io/github/forks/s4m98/winrar-cve-2023-38831-poc-gen.svg)

- [https://github.com/Ben1B3astt/CVE-2023-38831_ReverseShell_Winrar](https://github.com/Ben1B3astt/CVE-2023-38831_ReverseShell_Winrar) :  ![starts](https://img.shields.io/github/stars/Ben1B3astt/CVE-2023-38831_ReverseShell_Winrar.svg) ![forks](https://img.shields.io/github/forks/Ben1B3astt/CVE-2023-38831_ReverseShell_Winrar.svg)

- [https://github.com/TranKuBao/winrar_CVE2023-38831](https://github.com/TranKuBao/winrar_CVE2023-38831) :  ![starts](https://img.shields.io/github/stars/TranKuBao/winrar_CVE2023-38831.svg) ![forks](https://img.shields.io/github/forks/TranKuBao/winrar_CVE2023-38831.svg)

- [https://github.com/an040702/CVE-2023-38831](https://github.com/an040702/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/an040702/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/an040702/CVE-2023-38831.svg)

- [https://github.com/kehrijksen/CVE-2023-38831](https://github.com/kehrijksen/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/kehrijksen/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/kehrijksen/CVE-2023-38831.svg)

- [https://github.com/asepsaepdin/CVE-2023-38831](https://github.com/asepsaepdin/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/asepsaepdin/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/asepsaepdin/CVE-2023-38831.svg)

- [https://github.com/sh770/CVE-2023-38831](https://github.com/sh770/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/sh770/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/sh770/CVE-2023-38831.svg)

- [https://github.com/thegr1ffyn/CVE-2023-38831](https://github.com/thegr1ffyn/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/thegr1ffyn/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/thegr1ffyn/CVE-2023-38831.svg)

- [https://github.com/RomainBayle08/CVE-2023-38831](https://github.com/RomainBayle08/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/RomainBayle08/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/RomainBayle08/CVE-2023-38831.svg)

- [https://github.com/GOTonyGO/CVE-2023-38831-winrar](https://github.com/GOTonyGO/CVE-2023-38831-winrar) :  ![starts](https://img.shields.io/github/stars/GOTonyGO/CVE-2023-38831-winrar.svg) ![forks](https://img.shields.io/github/forks/GOTonyGO/CVE-2023-38831-winrar.svg)

- [https://github.com/Nielk74/CVE-2023-38831](https://github.com/Nielk74/CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/Nielk74/CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/Nielk74/CVE-2023-38831.svg)

- [https://github.com/MyStuffYT/CVE-2023-38831-POC](https://github.com/MyStuffYT/CVE-2023-38831-POC) :  ![starts](https://img.shields.io/github/stars/MyStuffYT/CVE-2023-38831-POC.svg) ![forks](https://img.shields.io/github/forks/MyStuffYT/CVE-2023-38831-POC.svg)

- [https://github.com/khanhtranngoccva/cve-2023-38831-poc](https://github.com/khanhtranngoccva/cve-2023-38831-poc) :  ![starts](https://img.shields.io/github/stars/khanhtranngoccva/cve-2023-38831-poc.svg) ![forks](https://img.shields.io/github/forks/khanhtranngoccva/cve-2023-38831-poc.svg)

- [https://github.com/VictoriousKnight/CVE-2023-38831_Exploit](https://github.com/VictoriousKnight/CVE-2023-38831_Exploit) :  ![starts](https://img.shields.io/github/stars/VictoriousKnight/CVE-2023-38831_Exploit.svg) ![forks](https://img.shields.io/github/forks/VictoriousKnight/CVE-2023-38831_Exploit.svg)

- [https://github.com/h3xecute/SideCopy-Exploits-CVE-2023-38831](https://github.com/h3xecute/SideCopy-Exploits-CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/h3xecute/SideCopy-Exploits-CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/h3xecute/SideCopy-Exploits-CVE-2023-38831.svg)

- [https://github.com/Fa1c0n35/CVE-2023-38831-winrar-exploit](https://github.com/Fa1c0n35/CVE-2023-38831-winrar-exploit) :  ![starts](https://img.shields.io/github/stars/Fa1c0n35/CVE-2023-38831-winrar-exploit.svg) ![forks](https://img.shields.io/github/forks/Fa1c0n35/CVE-2023-38831-winrar-exploit.svg)

- [https://github.com/imbyter/imbyter-WinRAR_CVE-2023-38831](https://github.com/imbyter/imbyter-WinRAR_CVE-2023-38831) :  ![starts](https://img.shields.io/github/stars/imbyter/imbyter-WinRAR_CVE-2023-38831.svg) ![forks](https://img.shields.io/github/forks/imbyter/imbyter-WinRAR_CVE-2023-38831.svg)

- [https://github.com/ML-K-eng/CVE-2023-38831-Exploit-and-Detection](https://github.com/ML-K-eng/CVE-2023-38831-Exploit-and-Detection) :  ![starts](https://img.shields.io/github/stars/ML-K-eng/CVE-2023-38831-Exploit-and-Detection.svg) ![forks](https://img.shields.io/github/forks/ML-K-eng/CVE-2023-38831-Exploit-and-Detection.svg)

- [https://github.com/solomon12354/VolleyballSquid-----CVE-2023-38831-and-Bypass-UAC](https://github.com/solomon12354/VolleyballSquid-----CVE-2023-38831-and-Bypass-UAC) :  ![starts](https://img.shields.io/github/stars/solomon12354/VolleyballSquid-----CVE-2023-38831-and-Bypass-UAC.svg) ![forks](https://img.shields.io/github/forks/solomon12354/VolleyballSquid-----CVE-2023-38831-and-Bypass-UAC.svg)

- [https://github.com/Tolu12wani/Demonstration-of-CVE-2023-38831-via-Reverse-Shell-Execution](https://github.com/Tolu12wani/Demonstration-of-CVE-2023-38831-via-Reverse-Shell-Execution) :  ![starts](https://img.shields.io/github/stars/Tolu12wani/Demonstration-of-CVE-2023-38831-via-Reverse-Shell-Execution.svg) ![forks](https://img.shields.io/github/forks/Tolu12wani/Demonstration-of-CVE-2023-38831-via-Reverse-Shell-Execution.svg)

- [https://github.com/Hirusha-N/CVE-2021-34527-CVE-2023-38831-and-CVE-2023-32784](https://github.com/Hirusha-N/CVE-2021-34527-CVE-2023-38831-and-CVE-2023-32784) :  ![starts](https://img.shields.io/github/stars/Hirusha-N/CVE-2021-34527-CVE-2023-38831-and-CVE-2023-32784.svg) ![forks](https://img.shields.io/github/forks/Hirusha-N/CVE-2021-34527-CVE-2023-38831-and-CVE-2023-32784.svg)

## CVE-2023-38829
 An issue in NETIS SYSTEMS WF2409E v.3.6.42541 allows a remote attacker to execute arbitrary code via the ping and traceroute functions of the diagnostic tools component in the admin management interface.



- [https://github.com/adhikara13/CVE-2023-38829-NETIS-WF2409E](https://github.com/adhikara13/CVE-2023-38829-NETIS-WF2409E) :  ![starts](https://img.shields.io/github/stars/adhikara13/CVE-2023-38829-NETIS-WF2409E.svg) ![forks](https://img.shields.io/github/forks/adhikara13/CVE-2023-38829-NETIS-WF2409E.svg)

- [https://github.com/Victorique-123/CVE-2023-38829-NETIS-WF2409E_Report](https://github.com/Victorique-123/CVE-2023-38829-NETIS-WF2409E_Report) :  ![starts](https://img.shields.io/github/stars/Victorique-123/CVE-2023-38829-NETIS-WF2409E_Report.svg) ![forks](https://img.shields.io/github/forks/Victorique-123/CVE-2023-38829-NETIS-WF2409E_Report.svg)

## CVE-2023-38822
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/TraiLeR2/Corsair---DLL-Planting-CVE-2023-38822](https://github.com/TraiLeR2/Corsair---DLL-Planting-CVE-2023-38822) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/Corsair---DLL-Planting-CVE-2023-38822.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/Corsair---DLL-Planting-CVE-2023-38822.svg)

## CVE-2023-38821
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/TraiLeR2/CoD-MW-Warzone-2---CVE-2023-38821](https://github.com/TraiLeR2/CoD-MW-Warzone-2---CVE-2023-38821) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/CoD-MW-Warzone-2---CVE-2023-38821.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/CoD-MW-Warzone-2---CVE-2023-38821.svg)

## CVE-2023-38820
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/TraiLeR2/DLL-Planting-Slack-4.33.73-CVE-2023-38820](https://github.com/TraiLeR2/DLL-Planting-Slack-4.33.73-CVE-2023-38820) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/DLL-Planting-Slack-4.33.73-CVE-2023-38820.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/DLL-Planting-Slack-4.33.73-CVE-2023-38820.svg)

## CVE-2023-38817
 An issue in Inspect Element Ltd Echo.ac v.5.2.1.0 allows a local attacker to gain privileges via a crafted command to the echo_driver.sys component. NOTE: the vendor's position is that the reported ability for user-mode applications to execute code as NT AUTHORITY\SYSTEM was "deactivated by Microsoft itself."



- [https://github.com/vxcall/kur](https://github.com/vxcall/kur) :  ![starts](https://img.shields.io/github/stars/vxcall/kur.svg) ![forks](https://img.shields.io/github/forks/vxcall/kur.svg)

## CVE-2023-38743
 Zoho ManageEngine ADManager Plus before Build 7200 allows admin users to execute commands on the host machine.



- [https://github.com/PetrusViet/CVE-2023-38743](https://github.com/PetrusViet/CVE-2023-38743) :  ![starts](https://img.shields.io/github/stars/PetrusViet/CVE-2023-38743.svg) ![forks](https://img.shields.io/github/forks/PetrusViet/CVE-2023-38743.svg)

## CVE-2023-38646
 Metabase open source before 0.46.6.1 and Metabase Enterprise before 1.46.6.1 allow attackers to execute arbitrary commands on the server, at the server's privilege level. Authentication is not required for exploitation. The other fixed versions are 0.45.4.1, 1.45.4.1, 0.44.7.1, 1.44.7.1, 0.43.7.2, and 1.43.7.2.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/Boogipop/MetabaseRceTools](https://github.com/Boogipop/MetabaseRceTools) :  ![starts](https://img.shields.io/github/stars/Boogipop/MetabaseRceTools.svg) ![forks](https://img.shields.io/github/forks/Boogipop/MetabaseRceTools.svg)

- [https://github.com/robotmikhro/CVE-2023-38646](https://github.com/robotmikhro/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/robotmikhro/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/robotmikhro/CVE-2023-38646.svg)

- [https://github.com/securezeron/CVE-2023-38646](https://github.com/securezeron/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/securezeron/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/securezeron/CVE-2023-38646.svg)

- [https://github.com/0xrobiul/CVE-2023-38646](https://github.com/0xrobiul/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/0xrobiul/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/0xrobiul/CVE-2023-38646.svg)

- [https://github.com/shamo0/CVE-2023-38646-PoC](https://github.com/shamo0/CVE-2023-38646-PoC) :  ![starts](https://img.shields.io/github/stars/shamo0/CVE-2023-38646-PoC.svg) ![forks](https://img.shields.io/github/forks/shamo0/CVE-2023-38646-PoC.svg)

- [https://github.com/Pyr0sec/CVE-2023-38646](https://github.com/Pyr0sec/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/Pyr0sec/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/Pyr0sec/CVE-2023-38646.svg)

- [https://github.com/kh4sh3i/CVE-2023-38646](https://github.com/kh4sh3i/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/kh4sh3i/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/kh4sh3i/CVE-2023-38646.svg)

- [https://github.com/Pumpkin-Garden/POC_Metabase_CVE-2023-38646](https://github.com/Pumpkin-Garden/POC_Metabase_CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/Pumpkin-Garden/POC_Metabase_CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/Pumpkin-Garden/POC_Metabase_CVE-2023-38646.svg)

- [https://github.com/XiaomingX/cve-2023-38646-poc](https://github.com/XiaomingX/cve-2023-38646-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2023-38646-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2023-38646-poc.svg)

- [https://github.com/nickswink/CVE-2023-38646](https://github.com/nickswink/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/nickswink/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/nickswink/CVE-2023-38646.svg)

- [https://github.com/Chocapikk/CVE-2023-38646](https://github.com/Chocapikk/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-38646.svg)

- [https://github.com/Red4mber/CVE-2023-38646](https://github.com/Red4mber/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/Red4mber/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/Red4mber/CVE-2023-38646.svg)

- [https://github.com/Xuxfff/CVE-2023-38646-Poc](https://github.com/Xuxfff/CVE-2023-38646-Poc) :  ![starts](https://img.shields.io/github/stars/Xuxfff/CVE-2023-38646-Poc.svg) ![forks](https://img.shields.io/github/forks/Xuxfff/CVE-2023-38646-Poc.svg)

- [https://github.com/Anekant-Singhai/Exploits](https://github.com/Anekant-Singhai/Exploits) :  ![starts](https://img.shields.io/github/stars/Anekant-Singhai/Exploits.svg) ![forks](https://img.shields.io/github/forks/Anekant-Singhai/Exploits.svg)

- [https://github.com/Zenmovie/CVE-2023-38646](https://github.com/Zenmovie/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/Zenmovie/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/Zenmovie/CVE-2023-38646.svg)

- [https://github.com/fidjiw/CVE-2023-38646-POC](https://github.com/fidjiw/CVE-2023-38646-POC) :  ![starts](https://img.shields.io/github/stars/fidjiw/CVE-2023-38646-POC.svg) ![forks](https://img.shields.io/github/forks/fidjiw/CVE-2023-38646-POC.svg)

- [https://github.com/alexandre-pecorilla/CVE-2023-38646](https://github.com/alexandre-pecorilla/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/alexandre-pecorilla/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/alexandre-pecorilla/CVE-2023-38646.svg)

- [https://github.com/UserConnecting/Exploit-CVE-2023-38646-Metabase](https://github.com/UserConnecting/Exploit-CVE-2023-38646-Metabase) :  ![starts](https://img.shields.io/github/stars/UserConnecting/Exploit-CVE-2023-38646-Metabase.svg) ![forks](https://img.shields.io/github/forks/UserConnecting/Exploit-CVE-2023-38646-Metabase.svg)

- [https://github.com/0utl4nder/Another-Metabase-RCE-CVE-2023-38646](https://github.com/0utl4nder/Another-Metabase-RCE-CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/0utl4nder/Another-Metabase-RCE-CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/0utl4nder/Another-Metabase-RCE-CVE-2023-38646.svg)

- [https://github.com/Micky1warrior/metabase-pre-auth-rce-poc](https://github.com/Micky1warrior/metabase-pre-auth-rce-poc) :  ![starts](https://img.shields.io/github/stars/Micky1warrior/metabase-pre-auth-rce-poc.svg) ![forks](https://img.shields.io/github/forks/Micky1warrior/metabase-pre-auth-rce-poc.svg)

- [https://github.com/birdm4nw/CVE-2023-38646](https://github.com/birdm4nw/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/birdm4nw/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/birdm4nw/CVE-2023-38646.svg)

- [https://github.com/asepsaepdin/CVE-2023-38646](https://github.com/asepsaepdin/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/asepsaepdin/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/asepsaepdin/CVE-2023-38646.svg)

- [https://github.com/raytheon0x21/CVE-2023-38646](https://github.com/raytheon0x21/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/raytheon0x21/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/raytheon0x21/CVE-2023-38646.svg)

- [https://github.com/threatHNTR/CVE-2023-38646](https://github.com/threatHNTR/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/threatHNTR/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/threatHNTR/CVE-2023-38646.svg)

- [https://github.com/passwa11/CVE-2023-38646](https://github.com/passwa11/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/passwa11/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/passwa11/CVE-2023-38646.svg)

- [https://github.com/Ego1stoo/CVE-2023-38646](https://github.com/Ego1stoo/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/Ego1stoo/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/Ego1stoo/CVE-2023-38646.svg)

- [https://github.com/yxl2001/CVE-2023-38646](https://github.com/yxl2001/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/yxl2001/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/yxl2001/CVE-2023-38646.svg)

- [https://github.com/BreezeGalaxy/CVE-2023-38646](https://github.com/BreezeGalaxy/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/BreezeGalaxy/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/BreezeGalaxy/CVE-2023-38646.svg)

- [https://github.com/Mrunalkaran/CVE-2023-38646](https://github.com/Mrunalkaran/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/Mrunalkaran/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/Mrunalkaran/CVE-2023-38646.svg)

- [https://github.com/AnvithLobo/CVE-2023-38646](https://github.com/AnvithLobo/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/AnvithLobo/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/AnvithLobo/CVE-2023-38646.svg)

- [https://github.com/DaniTheHack3r/CVE-2023-38646](https://github.com/DaniTheHack3r/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/DaniTheHack3r/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/DaniTheHack3r/CVE-2023-38646.svg)

- [https://github.com/junnythemarksman/CVE-2023-38646](https://github.com/junnythemarksman/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/junnythemarksman/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/junnythemarksman/CVE-2023-38646.svg)

- [https://github.com/j0yb0y0h/CVE-2023-38646](https://github.com/j0yb0y0h/CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/j0yb0y0h/CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/j0yb0y0h/CVE-2023-38646.svg)

- [https://github.com/adriyansyah-mf/CVE-2023-38646--Metabase-](https://github.com/adriyansyah-mf/CVE-2023-38646--Metabase-) :  ![starts](https://img.shields.io/github/stars/adriyansyah-mf/CVE-2023-38646--Metabase-.svg) ![forks](https://img.shields.io/github/forks/adriyansyah-mf/CVE-2023-38646--Metabase-.svg)

- [https://github.com/acesoyeo/METABASE-RCE-CVE-2023-38646-](https://github.com/acesoyeo/METABASE-RCE-CVE-2023-38646-) :  ![starts](https://img.shields.io/github/stars/acesoyeo/METABASE-RCE-CVE-2023-38646-.svg) ![forks](https://img.shields.io/github/forks/acesoyeo/METABASE-RCE-CVE-2023-38646-.svg)

- [https://github.com/Shisones/MetabaseRCE_CVE-2023-38646](https://github.com/Shisones/MetabaseRCE_CVE-2023-38646) :  ![starts](https://img.shields.io/github/stars/Shisones/MetabaseRCE_CVE-2023-38646.svg) ![forks](https://img.shields.io/github/forks/Shisones/MetabaseRCE_CVE-2023-38646.svg)

- [https://github.com/JayRyz/CVE-2023-38646-PoC-Metabase](https://github.com/JayRyz/CVE-2023-38646-PoC-Metabase) :  ![starts](https://img.shields.io/github/stars/JayRyz/CVE-2023-38646-PoC-Metabase.svg) ![forks](https://img.shields.io/github/forks/JayRyz/CVE-2023-38646-PoC-Metabase.svg)

- [https://github.com/Any3ite/cve-2023-38646-metabase-ReverseShell](https://github.com/Any3ite/cve-2023-38646-metabase-ReverseShell) :  ![starts](https://img.shields.io/github/stars/Any3ite/cve-2023-38646-metabase-ReverseShell.svg) ![forks](https://img.shields.io/github/forks/Any3ite/cve-2023-38646-metabase-ReverseShell.svg)

- [https://github.com/CN016/Metabase-H2-CVE-2023-38646-](https://github.com/CN016/Metabase-H2-CVE-2023-38646-) :  ![starts](https://img.shields.io/github/stars/CN016/Metabase-H2-CVE-2023-38646-.svg) ![forks](https://img.shields.io/github/forks/CN016/Metabase-H2-CVE-2023-38646-.svg)

- [https://github.com/m3m0o/metabase-pre-auth-rce-poc](https://github.com/m3m0o/metabase-pre-auth-rce-poc) :  ![starts](https://img.shields.io/github/stars/m3m0o/metabase-pre-auth-rce-poc.svg) ![forks](https://img.shields.io/github/forks/m3m0o/metabase-pre-auth-rce-poc.svg)

## CVE-2023-38632
 async-sockets-cpp through 0.3.1 has a stack-based buffer overflow in tcpsocket.hpp when processing malformed TCP packets.



- [https://github.com/Halcy0nic/CVE-2023-38632](https://github.com/Halcy0nic/CVE-2023-38632) :  ![starts](https://img.shields.io/github/stars/Halcy0nic/CVE-2023-38632.svg) ![forks](https://img.shields.io/github/forks/Halcy0nic/CVE-2023-38632.svg)

## CVE-2023-38609
 An injection issue was addressed with improved input validation. This issue is fixed in macOS Ventura 13.5. An app may be able to bypass certain Privacy preferences.



- [https://github.com/mc-17/CVE-2023-38609](https://github.com/mc-17/CVE-2023-38609) :  ![starts](https://img.shields.io/github/stars/mc-17/CVE-2023-38609.svg) ![forks](https://img.shields.io/github/forks/mc-17/CVE-2023-38609.svg)

## CVE-2023-38600
 The issue was addressed with improved checks. This issue is fixed in iOS 16.6 and iPadOS 16.6, tvOS 16.6, macOS Ventura 13.5, Safari 16.6, watchOS 9.6. Processing web content may lead to arbitrary code execution.



- [https://github.com/afrojack1/cve202338600test.github.io](https://github.com/afrojack1/cve202338600test.github.io) :  ![starts](https://img.shields.io/github/stars/afrojack1/cve202338600test.github.io.svg) ![forks](https://img.shields.io/github/forks/afrojack1/cve202338600test.github.io.svg)

## CVE-2023-38571
 This issue was addressed with improved validation of symlinks. This issue is fixed in macOS Big Sur 11.7.9, macOS Monterey 12.6.8, macOS Ventura 13.5. An app may be able to bypass Privacy preferences.



- [https://github.com/gergelykalman/CVE-2023-38571-a-macOS-TCC-bypass-in-Music-and-TV](https://github.com/gergelykalman/CVE-2023-38571-a-macOS-TCC-bypass-in-Music-and-TV) :  ![starts](https://img.shields.io/github/stars/gergelykalman/CVE-2023-38571-a-macOS-TCC-bypass-in-Music-and-TV.svg) ![forks](https://img.shields.io/github/forks/gergelykalman/CVE-2023-38571-a-macOS-TCC-bypass-in-Music-and-TV.svg)

## CVE-2023-38545
 This flaw makes curl overflow a heap based buffer in the SOCKS5 proxy
handshake.

When curl is asked to pass along the host name to the SOCKS5 proxy to allow
that to resolve the address instead of it getting done by curl itself, the
maximum length that host name can be is 255 bytes.

If the host name is detected to be longer, curl switches to local name
resolving and instead passes on the resolved address only. Due to this bug,
the local variable that means "let the host resolve the name" could get the
wrong value during a slow SOCKS5 handshake, and contrary to the intention,
copy the too long host name to the target buffer instead of copying just the
resolved address there.

The target buffer being a heap based buffer, and the host name coming from the
URL that curl has been told to operate with.



- [https://github.com/d0rb/CVE-2023-38545](https://github.com/d0rb/CVE-2023-38545) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-38545.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-38545.svg)

- [https://github.com/UTsweetyfish/CVE-2023-38545](https://github.com/UTsweetyfish/CVE-2023-38545) :  ![starts](https://img.shields.io/github/stars/UTsweetyfish/CVE-2023-38545.svg) ![forks](https://img.shields.io/github/forks/UTsweetyfish/CVE-2023-38545.svg)

- [https://github.com/imfht/CVE-2023-38545](https://github.com/imfht/CVE-2023-38545) :  ![starts](https://img.shields.io/github/stars/imfht/CVE-2023-38545.svg) ![forks](https://img.shields.io/github/forks/imfht/CVE-2023-38545.svg)

- [https://github.com/fatmo666/CVE-2023-38545-libcurl-SOCKS5-heap-buffer-overflow](https://github.com/fatmo666/CVE-2023-38545-libcurl-SOCKS5-heap-buffer-overflow) :  ![starts](https://img.shields.io/github/stars/fatmo666/CVE-2023-38545-libcurl-SOCKS5-heap-buffer-overflow.svg) ![forks](https://img.shields.io/github/forks/fatmo666/CVE-2023-38545-libcurl-SOCKS5-heap-buffer-overflow.svg)

- [https://github.com/vanigori/CVE-2023-38545-sample](https://github.com/vanigori/CVE-2023-38545-sample) :  ![starts](https://img.shields.io/github/stars/vanigori/CVE-2023-38545-sample.svg) ![forks](https://img.shields.io/github/forks/vanigori/CVE-2023-38545-sample.svg)

- [https://github.com/bcdannyboy/CVE-2023-38545](https://github.com/bcdannyboy/CVE-2023-38545) :  ![starts](https://img.shields.io/github/stars/bcdannyboy/CVE-2023-38545.svg) ![forks](https://img.shields.io/github/forks/bcdannyboy/CVE-2023-38545.svg)

- [https://github.com/dbrugman/CVE-2023-38545-POC](https://github.com/dbrugman/CVE-2023-38545-POC) :  ![starts](https://img.shields.io/github/stars/dbrugman/CVE-2023-38545-POC.svg) ![forks](https://img.shields.io/github/forks/dbrugman/CVE-2023-38545-POC.svg)

- [https://github.com/Yang-Shun-Yu/CVE-2023-38545](https://github.com/Yang-Shun-Yu/CVE-2023-38545) :  ![starts](https://img.shields.io/github/stars/Yang-Shun-Yu/CVE-2023-38545.svg) ![forks](https://img.shields.io/github/forks/Yang-Shun-Yu/CVE-2023-38545.svg)

- [https://github.com/nphuang/NS-Project-2024-Spring](https://github.com/nphuang/NS-Project-2024-Spring) :  ![starts](https://img.shields.io/github/stars/nphuang/NS-Project-2024-Spring.svg) ![forks](https://img.shields.io/github/forks/nphuang/NS-Project-2024-Spring.svg)

## CVE-2023-38497
 Cargo downloads the Rust project’s dependencies and compiles the project. Cargo prior to version 0.72.2, bundled with Rust prior to version 1.71.1, did not respect the umask when extracting crate archives on UNIX-like systems. If the user downloaded a crate containing files writeable by any local user, another local user could exploit this to change the source code compiled and executed by the current user. To prevent existing cached extractions from being exploitable, the Cargo binary version 0.72.2 included in Rust 1.71.1 or later will purge caches generated by older Cargo versions automatically. As a workaround, configure one's system to prevent other local users from accessing the Cargo directory, usually located in `~/.cargo`.



- [https://github.com/lucas-cauhe/cargo-perm](https://github.com/lucas-cauhe/cargo-perm) :  ![starts](https://img.shields.io/github/stars/lucas-cauhe/cargo-perm.svg) ![forks](https://img.shields.io/github/forks/lucas-cauhe/cargo-perm.svg)

## CVE-2023-38490
 Kirby is a content management system. A vulnerability in versions prior to 3.5.8.3, 3.6.6.3, 3.7.5.2, 3.8.4.1, and 3.9.6 only affects Kirby sites that use the `Xml` data handler (e.g. `Data::decode($string, 'xml')`) or the `Xml::parse()` method in site or plugin code. The Kirby core does not use any of the affected methods.

XML External Entities (XXE) is a little used feature in the XML markup language that allows to include data from external files in an XML structure. If the name of the external file can be controlled by an attacker, this becomes a vulnerability that can be abused for various system impacts like the disclosure of internal or confidential data that is stored on the server (arbitrary file disclosure) or to perform network requests on behalf of the server (server-side request forgery, SSRF).

Kirby's `Xml::parse()` method used PHP's `LIBXML_NOENT` constant, which enabled the processing of XML external entities during the parsing operation. The `Xml::parse()` method is used in the `Xml` data handler (e.g. `Data::decode($string, 'xml')`). Both the vulnerable method and the data handler are not used in the Kirby core. However they may be used in site or plugin code, e.g. to parse RSS feeds or other XML files. If those files are of an external origin (e.g. uploaded by a user or retrieved from an external URL), attackers may be able to include an external entity in the XML file that will then be processed in the parsing process. Kirby sites that don't use XML parsing in site or plugin code are *not* affected.

The problem has been patched in Kirby 3.5.8.3, 3.6.6.3, 3.7.5.2, 3.8.4.1, and 3.9.6. In all of the mentioned releases, the maintainers have removed the `LIBXML_NOENT` constant as processing of external entities is out of scope of the parsing logic. This protects all uses of the method against the described vulnerability.



- [https://github.com/Acceis/exploit-CVE-2023-38490](https://github.com/Acceis/exploit-CVE-2023-38490) :  ![starts](https://img.shields.io/github/stars/Acceis/exploit-CVE-2023-38490.svg) ![forks](https://img.shields.io/github/forks/Acceis/exploit-CVE-2023-38490.svg)

## CVE-2023-38434
 xHTTP 72f812d has a double free in close_connection in xhttp.c via a malformed HTTP request method.



- [https://github.com/Halcy0nic/CVE-2023-38434](https://github.com/Halcy0nic/CVE-2023-38434) :  ![starts](https://img.shields.io/github/stars/Halcy0nic/CVE-2023-38434.svg) ![forks](https://img.shields.io/github/forks/Halcy0nic/CVE-2023-38434.svg)

## CVE-2023-38408
 The PKCS#11 feature in ssh-agent in OpenSSH before 9.3p2 has an insufficiently trustworthy search path, leading to remote code execution if an agent is forwarded to an attacker-controlled system. (Code in /usr/lib is not necessarily safe for loading into ssh-agent.) NOTE: this issue exists because of an incomplete fix for CVE-2016-10009.



- [https://github.com/kali-mx/CVE-2023-38408](https://github.com/kali-mx/CVE-2023-38408) :  ![starts](https://img.shields.io/github/stars/kali-mx/CVE-2023-38408.svg) ![forks](https://img.shields.io/github/forks/kali-mx/CVE-2023-38408.svg)

- [https://github.com/LucasPDiniz/CVE-2023-38408](https://github.com/LucasPDiniz/CVE-2023-38408) :  ![starts](https://img.shields.io/github/stars/LucasPDiniz/CVE-2023-38408.svg) ![forks](https://img.shields.io/github/forks/LucasPDiniz/CVE-2023-38408.svg)

- [https://github.com/classic130/CVE-2023-38408](https://github.com/classic130/CVE-2023-38408) :  ![starts](https://img.shields.io/github/stars/classic130/CVE-2023-38408.svg) ![forks](https://img.shields.io/github/forks/classic130/CVE-2023-38408.svg)

- [https://github.com/mrtacojr/CVE-2023-38408](https://github.com/mrtacojr/CVE-2023-38408) :  ![starts](https://img.shields.io/github/stars/mrtacojr/CVE-2023-38408.svg) ![forks](https://img.shields.io/github/forks/mrtacojr/CVE-2023-38408.svg)

- [https://github.com/TX-One/CVE-2023-38408](https://github.com/TX-One/CVE-2023-38408) :  ![starts](https://img.shields.io/github/stars/TX-One/CVE-2023-38408.svg) ![forks](https://img.shields.io/github/forks/TX-One/CVE-2023-38408.svg)

- [https://github.com/Adel2411/cyber-combat](https://github.com/Adel2411/cyber-combat) :  ![starts](https://img.shields.io/github/stars/Adel2411/cyber-combat.svg) ![forks](https://img.shields.io/github/forks/Adel2411/cyber-combat.svg)

- [https://github.com/wxrdnx/CVE-2023-38408](https://github.com/wxrdnx/CVE-2023-38408) :  ![starts](https://img.shields.io/github/stars/wxrdnx/CVE-2023-38408.svg) ![forks](https://img.shields.io/github/forks/wxrdnx/CVE-2023-38408.svg)

## CVE-2023-38146
 Windows Themes Remote Code Execution Vulnerability



- [https://github.com/exploits-forsale/themebleed](https://github.com/exploits-forsale/themebleed) :  ![starts](https://img.shields.io/github/stars/exploits-forsale/themebleed.svg) ![forks](https://img.shields.io/github/forks/exploits-forsale/themebleed.svg)

- [https://github.com/Jnnshschl/CVE-2023-38146](https://github.com/Jnnshschl/CVE-2023-38146) :  ![starts](https://img.shields.io/github/stars/Jnnshschl/CVE-2023-38146.svg) ![forks](https://img.shields.io/github/forks/Jnnshschl/CVE-2023-38146.svg)

- [https://github.com/Durge5/ThemeBleedPy](https://github.com/Durge5/ThemeBleedPy) :  ![starts](https://img.shields.io/github/stars/Durge5/ThemeBleedPy.svg) ![forks](https://img.shields.io/github/forks/Durge5/ThemeBleedPy.svg)

## CVE-2023-38120
 Adtran SR400ac ping Command Injection Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adtran SR400ac routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed.

The specific flaw exists within the ping command, which is available over JSON-RPC. A crafted host parameter can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code in the context of root.
. Was ZDI-CAN-20525.



- [https://github.com/warber0x/CVE-2023-38120](https://github.com/warber0x/CVE-2023-38120) :  ![starts](https://img.shields.io/github/stars/warber0x/CVE-2023-38120.svg) ![forks](https://img.shields.io/github/forks/warber0x/CVE-2023-38120.svg)

## CVE-2023-38041
 A logged in user may elevate its permissions by abusing a Time-of-Check to Time-of-Use (TOCTOU) race condition. When a particular process flow is initiated, an attacker can exploit this condition to gain unauthorized elevated privileges on the affected system.



- [https://github.com/ewilded/CVE-2023-38041-POC](https://github.com/ewilded/CVE-2023-38041-POC) :  ![starts](https://img.shields.io/github/stars/ewilded/CVE-2023-38041-POC.svg) ![forks](https://img.shields.io/github/forks/ewilded/CVE-2023-38041-POC.svg)

## CVE-2023-38039
 When curl retrieves an HTTP response, it stores the incoming headers so that
they can be accessed later via the libcurl headers API.

However, curl did not have a limit in how many or how large headers it would
accept in a response, allowing a malicious server to stream an endless series
of headers and eventually cause curl to run out of heap memory.



- [https://github.com/Smartkeyss/CVE-2023-38039](https://github.com/Smartkeyss/CVE-2023-38039) :  ![starts](https://img.shields.io/github/stars/Smartkeyss/CVE-2023-38039.svg) ![forks](https://img.shields.io/github/forks/Smartkeyss/CVE-2023-38039.svg)

## CVE-2023-38035
 A security vulnerability in MICS Admin Portal in Ivanti MobileIron Sentry versions 9.18.0 and below, which may allow an attacker to bypass authentication controls on the administrative interface due to an insufficiently restrictive Apache HTTPD configuration.



- [https://github.com/horizon3ai/CVE-2023-38035](https://github.com/horizon3ai/CVE-2023-38035) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2023-38035.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2023-38035.svg)

- [https://github.com/LeakIX/sentryexploit](https://github.com/LeakIX/sentryexploit) :  ![starts](https://img.shields.io/github/stars/LeakIX/sentryexploit.svg) ![forks](https://img.shields.io/github/forks/LeakIX/sentryexploit.svg)

- [https://github.com/mind2hex/CVE-2023-38035-MobileIron-RCE](https://github.com/mind2hex/CVE-2023-38035-MobileIron-RCE) :  ![starts](https://img.shields.io/github/stars/mind2hex/CVE-2023-38035-MobileIron-RCE.svg) ![forks](https://img.shields.io/github/forks/mind2hex/CVE-2023-38035-MobileIron-RCE.svg)

## CVE-2023-37979
 Unauth. Reflected Cross-Site Scripting (XSS) vulnerability in Saturday Drive Ninja Forms Contact Form plugin = 3.6.25 versions.



- [https://github.com/Mehran-Seifalinia/CVE-2023-37979](https://github.com/Mehran-Seifalinia/CVE-2023-37979) :  ![starts](https://img.shields.io/github/stars/Mehran-Seifalinia/CVE-2023-37979.svg) ![forks](https://img.shields.io/github/forks/Mehran-Seifalinia/CVE-2023-37979.svg)

- [https://github.com/d0rb/CVE-2023-37979](https://github.com/d0rb/CVE-2023-37979) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-37979.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-37979.svg)

## CVE-2023-37941
 If an attacker gains write access to the Apache Superset metadata database, they could persist a specifically crafted Python object that may lead to remote code execution on Superset's web backend.

The Superset metadata db is an 'internal' component that is typically 
only accessible directly by the system administrator and the superset 
process itself. Gaining access to that database should
 be difficult and require significant privileges.

This vulnerability impacts Apache Superset versions 1.5.0 up to and including 2.1.0. Users are recommended to upgrade to version 2.1.1 or later.



- [https://github.com/Barroqueiro/CVE-2023-37941](https://github.com/Barroqueiro/CVE-2023-37941) :  ![starts](https://img.shields.io/github/stars/Barroqueiro/CVE-2023-37941.svg) ![forks](https://img.shields.io/github/forks/Barroqueiro/CVE-2023-37941.svg)

## CVE-2023-37903
 vm2 is an open source vm/sandbox for Node.js. In vm2 for versions up to and including 3.9.19, Node.js custom inspect function allows attackers to escape the sandbox and run arbitrary code. This may result in Remote Code Execution, assuming the attacker has arbitrary code execution primitive inside the context of vm2 sandbox. There are no patches and no known workarounds. Users are advised to find an alternative software.



- [https://github.com/7h3h4ckv157/CVE-2023-37903](https://github.com/7h3h4ckv157/CVE-2023-37903) :  ![starts](https://img.shields.io/github/stars/7h3h4ckv157/CVE-2023-37903.svg) ![forks](https://img.shields.io/github/forks/7h3h4ckv157/CVE-2023-37903.svg)

## CVE-2023-37800
 DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: none. Reason: This candidate was withdrawn by its CNA. Further investigation showed that it was not a security issue. Notes: none.



- [https://github.com/TraiLeR2/CVE-2023-37800](https://github.com/TraiLeR2/CVE-2023-37800) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/CVE-2023-37800.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/CVE-2023-37800.svg)

## CVE-2023-37790
 Jaspersoft Clarity PPM version 14.3.0.298 was discovered to contain an arbitrary file upload vulnerability via the Profile Picture Upload function.



- [https://github.com/kaizensecurity/CVE-2023-37790](https://github.com/kaizensecurity/CVE-2023-37790) :  ![starts](https://img.shields.io/github/stars/kaizensecurity/CVE-2023-37790.svg) ![forks](https://img.shields.io/github/forks/kaizensecurity/CVE-2023-37790.svg)

## CVE-2023-37786
 Multiple cross-site scripting (XSS) vulnerabilities in Geeklog v2.2.2 allow attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the Mail Settings[backend], Mail Settings[host], Mail Settings[port] and Mail Settings[auth] parameters of the /admin/configuration.php.



- [https://github.com/Phamchie/CVE-2023-37786](https://github.com/Phamchie/CVE-2023-37786) :  ![starts](https://img.shields.io/github/stars/Phamchie/CVE-2023-37786.svg) ![forks](https://img.shields.io/github/forks/Phamchie/CVE-2023-37786.svg)

## CVE-2023-37779
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/jyoti818680/CVE-2023-37779](https://github.com/jyoti818680/CVE-2023-37779) :  ![starts](https://img.shields.io/github/stars/jyoti818680/CVE-2023-37779.svg) ![forks](https://img.shields.io/github/forks/jyoti818680/CVE-2023-37779.svg)

## CVE-2023-37778
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/jyoti818680/CVE-2023-37778](https://github.com/jyoti818680/CVE-2023-37778) :  ![starts](https://img.shields.io/github/stars/jyoti818680/CVE-2023-37778.svg) ![forks](https://img.shields.io/github/forks/jyoti818680/CVE-2023-37778.svg)

## CVE-2023-37772
 Online Shopping Portal Project v3.1 was discovered to contain a SQL injection vulnerability via the Email parameter at /shopping/login.php.



- [https://github.com/anky-123/CVE-2023-37772](https://github.com/anky-123/CVE-2023-37772) :  ![starts](https://img.shields.io/github/stars/anky-123/CVE-2023-37772.svg) ![forks](https://img.shields.io/github/forks/anky-123/CVE-2023-37772.svg)

## CVE-2023-37771
 Art Gallery Management System v1.0 contains a SQL injection vulnerability via the cid parameter at /agms/product.php.



- [https://github.com/anky-123/CVE-2023-37771](https://github.com/anky-123/CVE-2023-37771) :  ![starts](https://img.shields.io/github/stars/anky-123/CVE-2023-37771.svg) ![forks](https://img.shields.io/github/forks/anky-123/CVE-2023-37771.svg)

## CVE-2023-37756
 I-doit pro 25 and below and I-doit open 25 and below employ weak password requirements for Administrator account creation. Attackers are able to easily guess users' passwords via a bruteforce attack.



- [https://github.com/leekenghwa/CVE-2023-37756-CWE-521-lead-to-malicious-plugin-upload-in-the-i-doit-Pro-25-and-below](https://github.com/leekenghwa/CVE-2023-37756-CWE-521-lead-to-malicious-plugin-upload-in-the-i-doit-Pro-25-and-below) :  ![starts](https://img.shields.io/github/stars/leekenghwa/CVE-2023-37756-CWE-521-lead-to-malicious-plugin-upload-in-the-i-doit-Pro-25-and-below.svg) ![forks](https://img.shields.io/github/forks/leekenghwa/CVE-2023-37756-CWE-521-lead-to-malicious-plugin-upload-in-the-i-doit-Pro-25-and-below.svg)

## CVE-2023-37755
 i-doit pro 25 and below and I-doit open 25 and below are configured with insecure default administrator credentials, and there is no warning or prompt to ask users to change the default password and account name. Unauthenticated attackers can exploit this vulnerability to obtain Administrator privileges, resulting in them being able to perform arbitrary system operations or cause a Denial of Service (DoS).



- [https://github.com/leekenghwa/CVE-2023-37755---Hardcoded-Admin-Credential-in-i-doit-Pro-25-and-below](https://github.com/leekenghwa/CVE-2023-37755---Hardcoded-Admin-Credential-in-i-doit-Pro-25-and-below) :  ![starts](https://img.shields.io/github/stars/leekenghwa/CVE-2023-37755---Hardcoded-Admin-Credential-in-i-doit-Pro-25-and-below.svg) ![forks](https://img.shields.io/github/forks/leekenghwa/CVE-2023-37755---Hardcoded-Admin-Credential-in-i-doit-Pro-25-and-below.svg)

## CVE-2023-37739
 i-doit Pro v25 and below was discovered to be vulnerable to path traversal.



- [https://github.com/leekenghwa/CVE-2023-37739---Path-Traversal-in-i-doit-Pro-25-and-below](https://github.com/leekenghwa/CVE-2023-37739---Path-Traversal-in-i-doit-Pro-25-and-below) :  ![starts](https://img.shields.io/github/stars/leekenghwa/CVE-2023-37739---Path-Traversal-in-i-doit-Pro-25-and-below.svg) ![forks](https://img.shields.io/github/forks/leekenghwa/CVE-2023-37739---Path-Traversal-in-i-doit-Pro-25-and-below.svg)

## CVE-2023-37625
 A stored cross-site scripting (XSS) vulnerability in Netbox v3.4.7 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the Custom Link templates.



- [https://github.com/benjaminpsinclair/Netbox-CVE-2023-37625](https://github.com/benjaminpsinclair/Netbox-CVE-2023-37625) :  ![starts](https://img.shields.io/github/stars/benjaminpsinclair/Netbox-CVE-2023-37625.svg) ![forks](https://img.shields.io/github/forks/benjaminpsinclair/Netbox-CVE-2023-37625.svg)

## CVE-2023-37621
 DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: none. Reason: This candidate was withdrawn by its CNA. Further investigation showed that it was not a security issue. Notes: none.



- [https://github.com/MY0723/CNVD-2022-27366__CVE-2023-37621](https://github.com/MY0723/CNVD-2022-27366__CVE-2023-37621) :  ![starts](https://img.shields.io/github/stars/MY0723/CNVD-2022-27366__CVE-2023-37621.svg) ![forks](https://img.shields.io/github/forks/MY0723/CNVD-2022-27366__CVE-2023-37621.svg)

## CVE-2023-37599
 An issue in issabel-pbx v.4.0.0-6 allows a remote attacker to obtain sensitive information via the modules directory



- [https://github.com/sahiloj/CVE-2023-37599](https://github.com/sahiloj/CVE-2023-37599) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-37599.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-37599.svg)

## CVE-2023-37598
 A Cross Site Request Forgery (CSRF) vulnerability in issabel-pbx v.4.0.0-6 allows a remote attacker to cause a denial of service via the delete new virtual fax function.



- [https://github.com/sahiloj/CVE-2023-37598](https://github.com/sahiloj/CVE-2023-37598) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-37598.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-37598.svg)

## CVE-2023-37597
 Cross Site Request Forgery (CSRF) vulnerability in issabel-pbx v.4.0.0-6 allows a remote attacker to cause a denial of service via the delete user grouplist function.



- [https://github.com/sahiloj/CVE-2023-37597](https://github.com/sahiloj/CVE-2023-37597) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-37597.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-37597.svg)

## CVE-2023-37596
 Cross Site Request Forgery (CSRF) vulnerability in issabel-pbx v.4.0.0-6 allows a remote attacker to cause a denial of service via a crafted script to the deleteuser function.



- [https://github.com/sahiloj/CVE-2023-37596](https://github.com/sahiloj/CVE-2023-37596) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-37596.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-37596.svg)

## CVE-2023-37582
 The RocketMQ NameServer component still has a remote command execution vulnerability as the CVE-2023-33246 issue was not completely fixed in version 5.1.1. 

When NameServer address are leaked on the extranet and lack permission verification, an attacker can exploit this vulnerability by using the update configuration function on the NameServer component to execute commands as the system users that RocketMQ is running as. 

It is recommended for users to upgrade their NameServer version to 5.1.2 or above for RocketMQ 5.x or 4.9.7 or above for RocketMQ 4.x to prevent these attacks.



- [https://github.com/Malayke/CVE-2023-37582_EXPLOIT](https://github.com/Malayke/CVE-2023-37582_EXPLOIT) :  ![starts](https://img.shields.io/github/stars/Malayke/CVE-2023-37582_EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/Malayke/CVE-2023-37582_EXPLOIT.svg)

- [https://github.com/laishouchao/Apache-RocketMQ-RCE-CVE-2023-37582-poc](https://github.com/laishouchao/Apache-RocketMQ-RCE-CVE-2023-37582-poc) :  ![starts](https://img.shields.io/github/stars/laishouchao/Apache-RocketMQ-RCE-CVE-2023-37582-poc.svg) ![forks](https://img.shields.io/github/forks/laishouchao/Apache-RocketMQ-RCE-CVE-2023-37582-poc.svg)

## CVE-2023-37478
 pnpm is a package manager. It is possible to construct a tarball that, when installed via npm or parsed by the registry is safe, but when installed via pnpm is malicious, due to how pnpm parses tar archives. This can result in a package that appears safe on the npm registry or when installed via npm being replaced with a compromised or malicious version when installed via pnpm. This issue has been patched in version(s) 7.33.4 and 8.6.8.



- [https://github.com/li-minhao/CVE-2023-37478-Demo](https://github.com/li-minhao/CVE-2023-37478-Demo) :  ![starts](https://img.shields.io/github/stars/li-minhao/CVE-2023-37478-Demo.svg) ![forks](https://img.shields.io/github/forks/li-minhao/CVE-2023-37478-Demo.svg)

- [https://github.com/TrevorGKann/CVE-2023-37478_npm_vs_pnpm](https://github.com/TrevorGKann/CVE-2023-37478_npm_vs_pnpm) :  ![starts](https://img.shields.io/github/stars/TrevorGKann/CVE-2023-37478_npm_vs_pnpm.svg) ![forks](https://img.shields.io/github/forks/TrevorGKann/CVE-2023-37478_npm_vs_pnpm.svg)

## CVE-2023-37474
 Copyparty is a portable file server. Versions prior to 1.8.2 are subject to a path traversal vulnerability detected in the `.cpr` subfolder. The Path Traversal attack technique allows an attacker access to files, directories, and commands that reside outside the web document root directory. This issue has been addressed in commit `043e3c7d` which has been included in release 1.8.2. Users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/ilqarli27/CVE-2023-37474](https://github.com/ilqarli27/CVE-2023-37474) :  ![starts](https://img.shields.io/github/stars/ilqarli27/CVE-2023-37474.svg) ![forks](https://img.shields.io/github/forks/ilqarli27/CVE-2023-37474.svg)

## CVE-2023-37467
 Discourse is an open source discussion platform. Prior to version 3.1.0.beta7 of the `beta` and `tests-passed` branches, a CSP (Content Security Policy) nonce reuse vulnerability was discovered could allow cross-site scripting (XSS) attacks to bypass CSP protection for anonymous (i.e. unauthenticated) users. There are no known XSS vectors at the moment, but should one be discovered, this vulnerability would allow the XSS attack to bypass CSP and execute successfully. This vulnerability isn't applicable to logged-in users. Version 3.1.0.beta7 contains a patch. The stable branch doesn't have this vulnerability. A workaround to prevent the vulnerability is to disable Google Tag Manager, i.e., unset the `gtm container id` setting.



- [https://github.com/ibrahmsql/CVE-2023-37467](https://github.com/ibrahmsql/CVE-2023-37467) :  ![starts](https://img.shields.io/github/stars/ibrahmsql/CVE-2023-37467.svg) ![forks](https://img.shields.io/github/forks/ibrahmsql/CVE-2023-37467.svg)

## CVE-2023-37250
 Unity Parsec has a TOCTOU race condition that permits local attackers to escalate privileges to SYSTEM if Parsec was installed in "Per User" mode. The application intentionally launches DLLs from a user-owned directory but intended to always perform integrity verification of those DLLs. This affects Parsec Loader versions through 8. Parsec Loader 9 is a fixed version.



- [https://github.com/ewilded/CVE-2023-37250-POC](https://github.com/ewilded/CVE-2023-37250-POC) :  ![starts](https://img.shields.io/github/stars/ewilded/CVE-2023-37250-POC.svg) ![forks](https://img.shields.io/github/forks/ewilded/CVE-2023-37250-POC.svg)

## CVE-2023-37191
 A stored cross-site scripting (XSS) vulnerability in Issabel issabel-pbx v.4.0.0-6 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the Group and Description parameters.



- [https://github.com/sahiloj/CVE-2023-37191](https://github.com/sahiloj/CVE-2023-37191) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-37191.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-37191.svg)

## CVE-2023-37190
 A stored cross-site scripting (XSS) vulnerability in Issabel issabel-pbx v.4.0.0-6 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the Virtual Fax Name and Caller ID Name parameters under the New Virtual Fax feature.



- [https://github.com/sahiloj/CVE-2023-37190](https://github.com/sahiloj/CVE-2023-37190) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-37190.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-37190.svg)

## CVE-2023-37189
 A stored cross site scripting (XSS) vulnerability in index.php?menu=billing_rates of Issabel PBX version 4 allows attackers to execute arbitrary web scripts or HTML via a crafted payload entered into the Name or Prefix fields under the Create New Rate module.



- [https://github.com/sahiloj/CVE-2023-37189](https://github.com/sahiloj/CVE-2023-37189) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-37189.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-37189.svg)

## CVE-2023-37164
 Diafan CMS v6.0 was discovered to contain a reflected cross-site scripting via the cat_id parameter at /shop/?module=shop&action=search.



- [https://github.com/ilqarli27/CVE-2023-37164](https://github.com/ilqarli27/CVE-2023-37164) :  ![starts](https://img.shields.io/github/stars/ilqarli27/CVE-2023-37164.svg) ![forks](https://img.shields.io/github/forks/ilqarli27/CVE-2023-37164.svg)

## CVE-2023-37073
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Hamza0X/CVE-2023-37073](https://github.com/Hamza0X/CVE-2023-37073) :  ![starts](https://img.shields.io/github/stars/Hamza0X/CVE-2023-37073.svg) ![forks](https://img.shields.io/github/forks/Hamza0X/CVE-2023-37073.svg)

## CVE-2023-37070
 Code Projects Hospital Information System 1.0 is vulnerable to Cross Site Scripting (XSS)



- [https://github.com/riteshs4hu/My-CVE](https://github.com/riteshs4hu/My-CVE) :  ![starts](https://img.shields.io/github/stars/riteshs4hu/My-CVE.svg) ![forks](https://img.shields.io/github/forks/riteshs4hu/My-CVE.svg)

## CVE-2023-37069
 Code-Projects Online Hospital Management System V1.0 is vulnerable to SQL Injection (SQLI) attacks, which allow an attacker to manipulate the SQL queries executed by the application. The application fails to properly validate user-supplied input in the login id and password fields during the login process, enabling an attacker to inject malicious SQL code.



- [https://github.com/riteshs4hu/My-CVE](https://github.com/riteshs4hu/My-CVE) :  ![starts](https://img.shields.io/github/stars/riteshs4hu/My-CVE.svg) ![forks](https://img.shields.io/github/forks/riteshs4hu/My-CVE.svg)

## CVE-2023-37068
 Code-Projects Gym Management System V1.0 allows remote attackers to execute arbitrary SQL commands via the login form, leading to unauthorized access and potential data manipulation. This vulnerability arises due to insufficient validation of user-supplied input in the username and password fields, enabling SQL Injection attacks.



- [https://github.com/riteshs4hu/My-CVE](https://github.com/riteshs4hu/My-CVE) :  ![starts](https://img.shields.io/github/stars/riteshs4hu/My-CVE.svg) ![forks](https://img.shields.io/github/forks/riteshs4hu/My-CVE.svg)

## CVE-2023-36900
 Windows Common Log File System Driver Elevation of Privilege Vulnerability



- [https://github.com/RomanRybachek/CVE-2023-36900](https://github.com/RomanRybachek/CVE-2023-36900) :  ![starts](https://img.shields.io/github/stars/RomanRybachek/CVE-2023-36900.svg) ![forks](https://img.shields.io/github/forks/RomanRybachek/CVE-2023-36900.svg)

## CVE-2023-36899
 ASP.NET Elevation of Privilege Vulnerability



- [https://github.com/midisec/CVE-2023-36899](https://github.com/midisec/CVE-2023-36899) :  ![starts](https://img.shields.io/github/stars/midisec/CVE-2023-36899.svg) ![forks](https://img.shields.io/github/forks/midisec/CVE-2023-36899.svg)

- [https://github.com/d0rb/CVE-2023-36899](https://github.com/d0rb/CVE-2023-36899) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-36899.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-36899.svg)

## CVE-2023-36884
 Windows Search Remote Code Execution Vulnerability



- [https://github.com/jakabakos/CVE-2023-36884-MS-Office-HTML-RCE](https://github.com/jakabakos/CVE-2023-36884-MS-Office-HTML-RCE) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2023-36884-MS-Office-HTML-RCE.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2023-36884-MS-Office-HTML-RCE.svg)

- [https://github.com/Maxwitat/CVE-2023-36884-Scripts-for-Intune-Remediation-SCCM-Compliance-Baseline](https://github.com/Maxwitat/CVE-2023-36884-Scripts-for-Intune-Remediation-SCCM-Compliance-Baseline) :  ![starts](https://img.shields.io/github/stars/Maxwitat/CVE-2023-36884-Scripts-for-Intune-Remediation-SCCM-Compliance-Baseline.svg) ![forks](https://img.shields.io/github/forks/Maxwitat/CVE-2023-36884-Scripts-for-Intune-Remediation-SCCM-Compliance-Baseline.svg)

- [https://github.com/tarraschk/CVE-2023-36884-Checker](https://github.com/tarraschk/CVE-2023-36884-Checker) :  ![starts](https://img.shields.io/github/stars/tarraschk/CVE-2023-36884-Checker.svg) ![forks](https://img.shields.io/github/forks/tarraschk/CVE-2023-36884-Checker.svg)

- [https://github.com/zerosorai/CVE-2023-36884](https://github.com/zerosorai/CVE-2023-36884) :  ![starts](https://img.shields.io/github/stars/zerosorai/CVE-2023-36884.svg) ![forks](https://img.shields.io/github/forks/zerosorai/CVE-2023-36884.svg)

- [https://github.com/ridsoliveira/Fix-CVE-2023-36884](https://github.com/ridsoliveira/Fix-CVE-2023-36884) :  ![starts](https://img.shields.io/github/stars/ridsoliveira/Fix-CVE-2023-36884.svg) ![forks](https://img.shields.io/github/forks/ridsoliveira/Fix-CVE-2023-36884.svg)

- [https://github.com/raresteak/CVE-2023-36884](https://github.com/raresteak/CVE-2023-36884) :  ![starts](https://img.shields.io/github/stars/raresteak/CVE-2023-36884.svg) ![forks](https://img.shields.io/github/forks/raresteak/CVE-2023-36884.svg)

- [https://github.com/deepinstinct/Storm0978-RomCom-Campaign](https://github.com/deepinstinct/Storm0978-RomCom-Campaign) :  ![starts](https://img.shields.io/github/stars/deepinstinct/Storm0978-RomCom-Campaign.svg) ![forks](https://img.shields.io/github/forks/deepinstinct/Storm0978-RomCom-Campaign.svg)

- [https://github.com/ToddMaxey/CVE-2023-36884](https://github.com/ToddMaxey/CVE-2023-36884) :  ![starts](https://img.shields.io/github/stars/ToddMaxey/CVE-2023-36884.svg) ![forks](https://img.shields.io/github/forks/ToddMaxey/CVE-2023-36884.svg)

- [https://github.com/or2me/CVE-2023-36884_patcher](https://github.com/or2me/CVE-2023-36884_patcher) :  ![starts](https://img.shields.io/github/stars/or2me/CVE-2023-36884_patcher.svg) ![forks](https://img.shields.io/github/forks/or2me/CVE-2023-36884_patcher.svg)

## CVE-2023-36874
 Windows Error Reporting Service Elevation of Privilege Vulnerability



- [https://github.com/Wh04m1001/CVE-2023-36874](https://github.com/Wh04m1001/CVE-2023-36874) :  ![starts](https://img.shields.io/github/stars/Wh04m1001/CVE-2023-36874.svg) ![forks](https://img.shields.io/github/forks/Wh04m1001/CVE-2023-36874.svg)

- [https://github.com/Octoberfest7/CVE-2023-36874_BOF](https://github.com/Octoberfest7/CVE-2023-36874_BOF) :  ![starts](https://img.shields.io/github/stars/Octoberfest7/CVE-2023-36874_BOF.svg) ![forks](https://img.shields.io/github/forks/Octoberfest7/CVE-2023-36874_BOF.svg)

- [https://github.com/d0rb/CVE-2023-36874](https://github.com/d0rb/CVE-2023-36874) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-36874.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-36874.svg)

- [https://github.com/crisprss/CVE-2023-36874](https://github.com/crisprss/CVE-2023-36874) :  ![starts](https://img.shields.io/github/stars/crisprss/CVE-2023-36874.svg) ![forks](https://img.shields.io/github/forks/crisprss/CVE-2023-36874.svg)

## CVE-2023-36847
 A Missing Authentication for Critical Function vulnerability in Juniper Networks Junos OS on EX Series allows an unauthenticated, network-based attacker to cause limited impact to the file system integrity.





With a specific request to installAppPackage.php that doesn't require authentication an attacker is able to upload arbitrary files via J-Web, leading to a loss of 

integrity

for a certain 

part of the file system, which may allow chaining to other vulnerabilities.


This issue affects Juniper Networks Junos OS on EX Series:



  *  All versions prior to 20.4R3-S8;
  *  21.1 versions 21.1R1 and later;
  *  21.2 versions prior to 21.2R3-S6;
  *  21.3 versions 

prior to 

 21.3R3-S5;
  *  21.4 versions 

prior to 

21.4R3-S4;
  *  22.1 versions 

prior to 

22.1R3-S3;
  *  22.2 versions 

prior to 

22.2R3-S1;
  *  22.3 versions 

prior to 

22.3R2-S2, 22.3R3;
  *  22.4 versions 

prior to 

22.4R2-S1, 22.4R3.








- [https://github.com/r3dcl1ff/CVE-2023-36844_Juniper_RCE](https://github.com/r3dcl1ff/CVE-2023-36844_Juniper_RCE) :  ![starts](https://img.shields.io/github/stars/r3dcl1ff/CVE-2023-36844_Juniper_RCE.svg) ![forks](https://img.shields.io/github/forks/r3dcl1ff/CVE-2023-36844_Juniper_RCE.svg)

## CVE-2023-36846
 A Missing Authentication for Critical Function vulnerability in Juniper Networks Junos OS on SRX Series allows an unauthenticated, network-based attacker to cause limited impact to the file system integrity.



With a specific request to user.php that doesn't require authentication an attacker is able to upload arbitrary files via J-Web, leading to a loss of 

integrity

for a certain 

part of the file system, which may allow chaining to other vulnerabilities.


This issue affects Juniper Networks Junos OS on SRX Series:



  *  All versions prior to 20.4R3-S8;
  *  21.1 versions 21.1R1 and later;
  *  21.2 versions prior to 21.2R3-S6;
  *  21.3 versions 

prior to 

 21.3R3-S5;
  *  21.4 versions 

prior to 

21.4R3-S5;
  *  22.1 versions 

prior to 

22.1R3-S3;
  *  22.2 versions 

prior to 

22.2R3-S2;
  *  22.3 versions 

prior to 

22.3R2-S2, 22.3R3;
  *  22.4 versions 

prior to 

22.4R2-S1, 22.4R3.








- [https://github.com/r3dcl1ff/CVE-2023-36844_Juniper_RCE](https://github.com/r3dcl1ff/CVE-2023-36844_Juniper_RCE) :  ![starts](https://img.shields.io/github/stars/r3dcl1ff/CVE-2023-36844_Juniper_RCE.svg) ![forks](https://img.shields.io/github/forks/r3dcl1ff/CVE-2023-36844_Juniper_RCE.svg)

- [https://github.com/Chocapikk/CVE-2023-36846](https://github.com/Chocapikk/CVE-2023-36846) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-36846.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-36846.svg)

- [https://github.com/iveresk/CVE-2023-36845-6-](https://github.com/iveresk/CVE-2023-36845-6-) :  ![starts](https://img.shields.io/github/stars/iveresk/CVE-2023-36845-6-.svg) ![forks](https://img.shields.io/github/forks/iveresk/CVE-2023-36845-6-.svg)

## CVE-2023-36845
 A PHP External Variable Modification vulnerability in J-Web of Juniper Networks Junos OS on EX Series 

and SRX Series 

allows an unauthenticated, network-based attacker to remotely execute code.

Using a crafted request which sets the variable PHPRC an attacker is able to modify the PHP execution environment allowing the injection und execution of code.


This issue affects Juniper Networks Junos OS on EX Series


and 


SRX Series:



  *  All versions prior to 

20.4R3-S9;
  *  21.1 versions 21.1R1 and later;
  *  21.2 versions prior to 21.2R3-S7;
  *  21.3 versions prior to 21.3R3-S5;
  *  21.4 versions prior to 21.4R3-S5;
  *  22.1 versions 

prior to 

22.1R3-S4;
  *  22.2 versions 

prior to 

22.2R3-S2;
  *  22.3 versions 

prior to 

22.3R2-S2, 22.3R3-S1;
  *  22.4 versions 

prior to 

22.4R2-S1, 22.4R3;
  *  23.2 versions prior to 23.2R1-S1, 23.2R2.



- [https://github.com/vulncheck-oss/cve-2023-36845-scanner](https://github.com/vulncheck-oss/cve-2023-36845-scanner) :  ![starts](https://img.shields.io/github/stars/vulncheck-oss/cve-2023-36845-scanner.svg) ![forks](https://img.shields.io/github/forks/vulncheck-oss/cve-2023-36845-scanner.svg)

- [https://github.com/kljunowsky/CVE-2023-36845](https://github.com/kljunowsky/CVE-2023-36845) :  ![starts](https://img.shields.io/github/stars/kljunowsky/CVE-2023-36845.svg) ![forks](https://img.shields.io/github/forks/kljunowsky/CVE-2023-36845.svg)

- [https://github.com/Asbawy/Automation-for-Juniper-cve-2023-36845](https://github.com/Asbawy/Automation-for-Juniper-cve-2023-36845) :  ![starts](https://img.shields.io/github/stars/Asbawy/Automation-for-Juniper-cve-2023-36845.svg) ![forks](https://img.shields.io/github/forks/Asbawy/Automation-for-Juniper-cve-2023-36845.svg)

- [https://github.com/ak1t4/CVE-2023-36845](https://github.com/ak1t4/CVE-2023-36845) :  ![starts](https://img.shields.io/github/stars/ak1t4/CVE-2023-36845.svg) ![forks](https://img.shields.io/github/forks/ak1t4/CVE-2023-36845.svg)

- [https://github.com/r3dcl1ff/CVE-2023-36844_Juniper_RCE](https://github.com/r3dcl1ff/CVE-2023-36844_Juniper_RCE) :  ![starts](https://img.shields.io/github/stars/r3dcl1ff/CVE-2023-36844_Juniper_RCE.svg) ![forks](https://img.shields.io/github/forks/r3dcl1ff/CVE-2023-36844_Juniper_RCE.svg)

- [https://github.com/cyberh3als/CVE-2023-36845-POC](https://github.com/cyberh3als/CVE-2023-36845-POC) :  ![starts](https://img.shields.io/github/stars/cyberh3als/CVE-2023-36845-POC.svg) ![forks](https://img.shields.io/github/forks/cyberh3als/CVE-2023-36845-POC.svg)

- [https://github.com/zaenhaxor/CVE-2023-36845](https://github.com/zaenhaxor/CVE-2023-36845) :  ![starts](https://img.shields.io/github/stars/zaenhaxor/CVE-2023-36845.svg) ![forks](https://img.shields.io/github/forks/zaenhaxor/CVE-2023-36845.svg)

- [https://github.com/e11i0t4lders0n/CVE-2023-36845](https://github.com/e11i0t4lders0n/CVE-2023-36845) :  ![starts](https://img.shields.io/github/stars/e11i0t4lders0n/CVE-2023-36845.svg) ![forks](https://img.shields.io/github/forks/e11i0t4lders0n/CVE-2023-36845.svg)

- [https://github.com/halencarjunior/CVE-2023-36845](https://github.com/halencarjunior/CVE-2023-36845) :  ![starts](https://img.shields.io/github/stars/halencarjunior/CVE-2023-36845.svg) ![forks](https://img.shields.io/github/forks/halencarjunior/CVE-2023-36845.svg)

- [https://github.com/simrotion13/CVE-2023-36845](https://github.com/simrotion13/CVE-2023-36845) :  ![starts](https://img.shields.io/github/stars/simrotion13/CVE-2023-36845.svg) ![forks](https://img.shields.io/github/forks/simrotion13/CVE-2023-36845.svg)

- [https://github.com/jahithoque/Juniper-CVE-2023-36845-Mass-Hunting](https://github.com/jahithoque/Juniper-CVE-2023-36845-Mass-Hunting) :  ![starts](https://img.shields.io/github/stars/jahithoque/Juniper-CVE-2023-36845-Mass-Hunting.svg) ![forks](https://img.shields.io/github/forks/jahithoque/Juniper-CVE-2023-36845-Mass-Hunting.svg)

- [https://github.com/ifconfig-me/CVE-2023-36845](https://github.com/ifconfig-me/CVE-2023-36845) :  ![starts](https://img.shields.io/github/stars/ifconfig-me/CVE-2023-36845.svg) ![forks](https://img.shields.io/github/forks/ifconfig-me/CVE-2023-36845.svg)

- [https://github.com/toanln-cov/CVE-2023-36845](https://github.com/toanln-cov/CVE-2023-36845) :  ![starts](https://img.shields.io/github/stars/toanln-cov/CVE-2023-36845.svg) ![forks](https://img.shields.io/github/forks/toanln-cov/CVE-2023-36845.svg)

- [https://github.com/iveresk/CVE-2023-36845-6-](https://github.com/iveresk/CVE-2023-36845-6-) :  ![starts](https://img.shields.io/github/stars/iveresk/CVE-2023-36845-6-.svg) ![forks](https://img.shields.io/github/forks/iveresk/CVE-2023-36845-6-.svg)

- [https://github.com/P4x1s/ansible-cve-2023-36845](https://github.com/P4x1s/ansible-cve-2023-36845) :  ![starts](https://img.shields.io/github/stars/P4x1s/ansible-cve-2023-36845.svg) ![forks](https://img.shields.io/github/forks/P4x1s/ansible-cve-2023-36845.svg)

- [https://github.com/0xNehru/CVE-2023-36845-Juniper-Vulnerability](https://github.com/0xNehru/CVE-2023-36845-Juniper-Vulnerability) :  ![starts](https://img.shields.io/github/stars/0xNehru/CVE-2023-36845-Juniper-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/0xNehru/CVE-2023-36845-Juniper-Vulnerability.svg)

- [https://github.com/Vignesh2712/Automation-for-Juniper-cve-2023-36845](https://github.com/Vignesh2712/Automation-for-Juniper-cve-2023-36845) :  ![starts](https://img.shields.io/github/stars/Vignesh2712/Automation-for-Juniper-cve-2023-36845.svg) ![forks](https://img.shields.io/github/forks/Vignesh2712/Automation-for-Juniper-cve-2023-36845.svg)

- [https://github.com/cyb3rzest/Juniper-Bug-Automation-CVE-2023-36845](https://github.com/cyb3rzest/Juniper-Bug-Automation-CVE-2023-36845) :  ![starts](https://img.shields.io/github/stars/cyb3rzest/Juniper-Bug-Automation-CVE-2023-36845.svg) ![forks](https://img.shields.io/github/forks/cyb3rzest/Juniper-Bug-Automation-CVE-2023-36845.svg)

- [https://github.com/CharonDefalt/Juniper-exploit-CVE-2023-36845](https://github.com/CharonDefalt/Juniper-exploit-CVE-2023-36845) :  ![starts](https://img.shields.io/github/stars/CharonDefalt/Juniper-exploit-CVE-2023-36845.svg) ![forks](https://img.shields.io/github/forks/CharonDefalt/Juniper-exploit-CVE-2023-36845.svg)

## CVE-2023-36844
 A PHP External Variable Modification vulnerability in J-Web of Juniper Networks Junos OS on EX Series allows an unauthenticated, network-based attacker to control certain, important environment variables.

Using a crafted request an attacker is able to modify 

certain PHP environment variables leading to partial loss of integrity, which may allow chaining to other vulnerabilities.
This issue affects Juniper Networks Junos OS on EX Series:



  *  All versions prior to 20.4R3-S9;
  *  21.1 versions 21.1R1 and later;
  *  21.2 versions prior to 21.2R3-S7;
  *  21.3 versions 

prior to 

 21.3R3-S5;
  *  21.4 versions 

prior to 

21.4R3-S5;
  *  22.1 versions 

prior to 

22.1R3-S4;
  *  22.2 versions 

prior to 

22.2R3-S2;
  *  22.3 versions 

prior to 22.3R3-S1;
  *  22.4 versions 

prior to 

22.4R2-S2, 22.4R3;
  *  23.2 versions prior to 

23.2R1-S1, 23.2R2.



- [https://github.com/watchtowrlabs/juniper-rce_cve-2023-36844](https://github.com/watchtowrlabs/juniper-rce_cve-2023-36844) :  ![starts](https://img.shields.io/github/stars/watchtowrlabs/juniper-rce_cve-2023-36844.svg) ![forks](https://img.shields.io/github/forks/watchtowrlabs/juniper-rce_cve-2023-36844.svg)

- [https://github.com/r3dcl1ff/CVE-2023-36844_Juniper_RCE](https://github.com/r3dcl1ff/CVE-2023-36844_Juniper_RCE) :  ![starts](https://img.shields.io/github/stars/r3dcl1ff/CVE-2023-36844_Juniper_RCE.svg) ![forks](https://img.shields.io/github/forks/r3dcl1ff/CVE-2023-36844_Juniper_RCE.svg)

- [https://github.com/ThatNotEasy/CVE-2023-36844](https://github.com/ThatNotEasy/CVE-2023-36844) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2023-36844.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2023-36844.svg)

## CVE-2023-36812
 OpenTSDB is a open source, distributed, scalable Time Series Database (TSDB). OpenTSDB is vulnerable to Remote Code Execution vulnerability by writing user-controlled input to Gnuplot configuration file and running Gnuplot with the generated configuration. This issue has been patched in  commit `07c4641471c` and further refined in commit `fa88d3e4b`. These patches are available in the `2.4.2` release. Users are advised to upgrade. User unable to upgrade may disable Gunuplot via the config option`tsd.core.enable_ui = true` and remove the shell files `mygnuplot.bat` and `mygnuplot.sh`.



- [https://github.com/ErikWynter/opentsdb_key_cmd_injection](https://github.com/ErikWynter/opentsdb_key_cmd_injection) :  ![starts](https://img.shields.io/github/stars/ErikWynter/opentsdb_key_cmd_injection.svg) ![forks](https://img.shields.io/github/forks/ErikWynter/opentsdb_key_cmd_injection.svg)

## CVE-2023-36802
 Microsoft Streaming Service Proxy Elevation of Privilege Vulnerability



- [https://github.com/chompie1337/Windows_MSKSSRV_LPE_CVE-2023-36802](https://github.com/chompie1337/Windows_MSKSSRV_LPE_CVE-2023-36802) :  ![starts](https://img.shields.io/github/stars/chompie1337/Windows_MSKSSRV_LPE_CVE-2023-36802.svg) ![forks](https://img.shields.io/github/forks/chompie1337/Windows_MSKSSRV_LPE_CVE-2023-36802.svg)

- [https://github.com/Nero22k/cve-2023-36802](https://github.com/Nero22k/cve-2023-36802) :  ![starts](https://img.shields.io/github/stars/Nero22k/cve-2023-36802.svg) ![forks](https://img.shields.io/github/forks/Nero22k/cve-2023-36802.svg)

- [https://github.com/x0rb3l/CVE-2023-36802-MSKSSRV-LPE](https://github.com/x0rb3l/CVE-2023-36802-MSKSSRV-LPE) :  ![starts](https://img.shields.io/github/stars/x0rb3l/CVE-2023-36802-MSKSSRV-LPE.svg) ![forks](https://img.shields.io/github/forks/x0rb3l/CVE-2023-36802-MSKSSRV-LPE.svg)

- [https://github.com/4zur-0312/CVE-2023-36802](https://github.com/4zur-0312/CVE-2023-36802) :  ![starts](https://img.shields.io/github/stars/4zur-0312/CVE-2023-36802.svg) ![forks](https://img.shields.io/github/forks/4zur-0312/CVE-2023-36802.svg)

## CVE-2023-36745
 Microsoft Exchange Server Remote Code Execution Vulnerability



- [https://github.com/N1k0la-T/CVE-2023-36745](https://github.com/N1k0la-T/CVE-2023-36745) :  ![starts](https://img.shields.io/github/stars/N1k0la-T/CVE-2023-36745.svg) ![forks](https://img.shields.io/github/forks/N1k0la-T/CVE-2023-36745.svg)

## CVE-2023-36723
 Windows Container Manager Service Elevation of Privilege Vulnerability



- [https://github.com/Wh04m1001/CVE-2023-36723](https://github.com/Wh04m1001/CVE-2023-36723) :  ![starts](https://img.shields.io/github/stars/Wh04m1001/CVE-2023-36723.svg) ![forks](https://img.shields.io/github/forks/Wh04m1001/CVE-2023-36723.svg)

## CVE-2023-36664
 Artifex Ghostscript through 10.01.2 mishandles permission validation for pipe devices (with the %pipe% prefix or the | pipe character prefix).



- [https://github.com/jakabakos/CVE-2023-36664-Ghostscript-command-injection](https://github.com/jakabakos/CVE-2023-36664-Ghostscript-command-injection) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2023-36664-Ghostscript-command-injection.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2023-36664-Ghostscript-command-injection.svg)

- [https://github.com/jeanchpt/CVE-2023-36664](https://github.com/jeanchpt/CVE-2023-36664) :  ![starts](https://img.shields.io/github/stars/jeanchpt/CVE-2023-36664.svg) ![forks](https://img.shields.io/github/forks/jeanchpt/CVE-2023-36664.svg)

- [https://github.com/churamanib/CVE-2023-36664-Ghostscript-command-injection](https://github.com/churamanib/CVE-2023-36664-Ghostscript-command-injection) :  ![starts](https://img.shields.io/github/stars/churamanib/CVE-2023-36664-Ghostscript-command-injection.svg) ![forks](https://img.shields.io/github/forks/churamanib/CVE-2023-36664-Ghostscript-command-injection.svg)

- [https://github.com/winkler-winsen/Scan_GhostScript](https://github.com/winkler-winsen/Scan_GhostScript) :  ![starts](https://img.shields.io/github/stars/winkler-winsen/Scan_GhostScript.svg) ![forks](https://img.shields.io/github/forks/winkler-winsen/Scan_GhostScript.svg)

## CVE-2023-36645
 SQL injection vulnerability in ITB-GmbH TradePro v9.5, allows remote attackers to run SQL queries via oordershow component in customer function.



- [https://github.com/caffeinated-labs/CVE-2023-36645](https://github.com/caffeinated-labs/CVE-2023-36645) :  ![starts](https://img.shields.io/github/stars/caffeinated-labs/CVE-2023-36645.svg) ![forks](https://img.shields.io/github/forks/caffeinated-labs/CVE-2023-36645.svg)

## CVE-2023-36644
 Incorrect Access Control in ITB-GmbH TradePro v9.5, allows remote attackers to receive all order confirmations from the online shop via the printmail plugin.



- [https://github.com/caffeinated-labs/CVE-2023-36644](https://github.com/caffeinated-labs/CVE-2023-36644) :  ![starts](https://img.shields.io/github/stars/caffeinated-labs/CVE-2023-36644.svg) ![forks](https://img.shields.io/github/forks/caffeinated-labs/CVE-2023-36644.svg)

## CVE-2023-36643
 Incorrect Access Control in ITB-GmbH TradePro v9.5, allows remote attackers to receive all orders from the online shop via oordershow component in customer function.



- [https://github.com/caffeinated-labs/CVE-2023-36643](https://github.com/caffeinated-labs/CVE-2023-36643) :  ![starts](https://img.shields.io/github/stars/caffeinated-labs/CVE-2023-36643.svg) ![forks](https://img.shields.io/github/forks/caffeinated-labs/CVE-2023-36643.svg)

## CVE-2023-36531
 Missing Authorization vulnerability in LiquidPoll LiquidPoll – Advanced Polls for Creators and Brands allows Exploiting Incorrectly Configured Access Control Security Levels.This issue affects LiquidPoll – Advanced Polls for Creators and Brands: from n/a through 3.3.68.



- [https://github.com/RandomRobbieBF/CVE-2023-36531](https://github.com/RandomRobbieBF/CVE-2023-36531) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-36531.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-36531.svg)

## CVE-2023-36427
 Windows Hyper-V Elevation of Privilege Vulnerability



- [https://github.com/tandasat/CVE-2023-36427](https://github.com/tandasat/CVE-2023-36427) :  ![starts](https://img.shields.io/github/stars/tandasat/CVE-2023-36427.svg) ![forks](https://img.shields.io/github/forks/tandasat/CVE-2023-36427.svg)

## CVE-2023-36424
 Windows Common Log File System Driver Elevation of Privilege Vulnerability



- [https://github.com/zerozenxlabs/CVE-2023-36424](https://github.com/zerozenxlabs/CVE-2023-36424) :  ![starts](https://img.shields.io/github/stars/zerozenxlabs/CVE-2023-36424.svg) ![forks](https://img.shields.io/github/forks/zerozenxlabs/CVE-2023-36424.svg)

## CVE-2023-36407
 Windows Hyper-V Elevation of Privilege Vulnerability



- [https://github.com/pwndorei/CVE-2023-36407](https://github.com/pwndorei/CVE-2023-36407) :  ![starts](https://img.shields.io/github/stars/pwndorei/CVE-2023-36407.svg) ![forks](https://img.shields.io/github/forks/pwndorei/CVE-2023-36407.svg)

- [https://github.com/zha0/CVE-2023-36407](https://github.com/zha0/CVE-2023-36407) :  ![starts](https://img.shields.io/github/stars/zha0/CVE-2023-36407.svg) ![forks](https://img.shields.io/github/forks/zha0/CVE-2023-36407.svg)

## CVE-2023-36319
 File Upload vulnerability in Openupload Stable v.0.4.3 allows a remote attacker to execute arbitrary code via the action parameter of the compress-inc.php file.



- [https://github.com/Lowalu/CVE-2023-36319](https://github.com/Lowalu/CVE-2023-36319) :  ![starts](https://img.shields.io/github/stars/Lowalu/CVE-2023-36319.svg) ![forks](https://img.shields.io/github/forks/Lowalu/CVE-2023-36319.svg)

## CVE-2023-36281
 An issue in langchain v.0.0.171 allows a remote attacker to execute arbitrary code via a JSON file to load_prompt. This is related to __subclasses__ or a template.



- [https://github.com/tagomaru/CVE-2023-36281](https://github.com/tagomaru/CVE-2023-36281) :  ![starts](https://img.shields.io/github/stars/tagomaru/CVE-2023-36281.svg) ![forks](https://img.shields.io/github/forks/tagomaru/CVE-2023-36281.svg)

## CVE-2023-36250
 CSV Injection vulnerability in GNOME time tracker version 3.0.2, allows local attackers to execute arbitrary code via crafted .tsv file when creating a new record.



- [https://github.com/BrunoTeixeira1996/CVE-2023-36250](https://github.com/BrunoTeixeira1996/CVE-2023-36250) :  ![starts](https://img.shields.io/github/stars/BrunoTeixeira1996/CVE-2023-36250.svg) ![forks](https://img.shields.io/github/forks/BrunoTeixeira1996/CVE-2023-36250.svg)

## CVE-2023-36169
 DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: none. Reason: This candidate was withdrawn by its CNA. Further investigation showed that it was not a security issue. Notes: none.



- [https://github.com/TraiLeR2/CVE-2023-36169](https://github.com/TraiLeR2/CVE-2023-36169) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/CVE-2023-36169.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/CVE-2023-36169.svg)

## CVE-2023-36168
 DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: none. Reason: This candidate was withdrawn by its CNA. Further investigation showed that it was not a security issue. Notes: none.



- [https://github.com/TraiLeR2/CVE-2023-36168](https://github.com/TraiLeR2/CVE-2023-36168) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/CVE-2023-36168.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/CVE-2023-36168.svg)

## CVE-2023-36165
 DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: none. Reason: This candidate was withdrawn by its CNA. Further investigation showed that it was not a security issue. Notes: none.



- [https://github.com/TraiLeR2/CVE-2023-36165](https://github.com/TraiLeR2/CVE-2023-36165) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/CVE-2023-36165.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/CVE-2023-36165.svg)

## CVE-2023-36164
 DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: none. Reason: This candidate was withdrawn by its CNA. Further investigation showed that it was not a security issue. Notes: none.



- [https://github.com/TraiLeR2/CVE-2023-36164](https://github.com/TraiLeR2/CVE-2023-36164) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/CVE-2023-36164.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/CVE-2023-36164.svg)

## CVE-2023-36163
 Cross Site Scripting vulnerability in IP-DOT BuildaGate v.BuildaGate5 allows a remote attacker to execute arbitrary code via a crafted script to the mc parameter of the URL.



- [https://github.com/TraiLeR2/CVE-2023-36163](https://github.com/TraiLeR2/CVE-2023-36163) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/CVE-2023-36163.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/CVE-2023-36163.svg)

## CVE-2023-36159
 Cross Site Scripting (XSS) vulnerability in sourcecodester Lost and Found Information System 1.0 allows remote attackers to run arbitrary code via the First Name, Middle Name and Last Name fields on the Create User page.



- [https://github.com/unknown00759/CVE-2023-36159](https://github.com/unknown00759/CVE-2023-36159) :  ![starts](https://img.shields.io/github/stars/unknown00759/CVE-2023-36159.svg) ![forks](https://img.shields.io/github/forks/unknown00759/CVE-2023-36159.svg)

## CVE-2023-36158
 Cross Site Scripting (XSS) vulnerability in sourcecodester Toll Tax Management System 1.0 allows remote attackers to run arbitrary code via the First Name and Last Name fields on the My Account page.



- [https://github.com/unknown00759/CVE-2023-36158](https://github.com/unknown00759/CVE-2023-36158) :  ![starts](https://img.shields.io/github/stars/unknown00759/CVE-2023-36158.svg) ![forks](https://img.shields.io/github/forks/unknown00759/CVE-2023-36158.svg)

## CVE-2023-36146
 A Stored Cross-Site Scripting (XSS) vulnerability was found in Multilaser RE 170 using firmware 2.2.6733.



- [https://github.com/leonardobg/CVE-2023-36146](https://github.com/leonardobg/CVE-2023-36146) :  ![starts](https://img.shields.io/github/stars/leonardobg/CVE-2023-36146.svg) ![forks](https://img.shields.io/github/forks/leonardobg/CVE-2023-36146.svg)

## CVE-2023-36144
 An authentication bypass in Intelbras Switch SG 2404 MR in firmware 1.00.54 allows an unauthenticated attacker to download the backup file of the device, exposing critical information about the device configuration.



- [https://github.com/leonardobg/CVE-2023-36144](https://github.com/leonardobg/CVE-2023-36144) :  ![starts](https://img.shields.io/github/stars/leonardobg/CVE-2023-36144.svg) ![forks](https://img.shields.io/github/forks/leonardobg/CVE-2023-36144.svg)

## CVE-2023-36143
 Maxprint Maxlink 1200G v3.4.11E has an OS command injection vulnerability in the "Diagnostic tool" functionality of the device.



- [https://github.com/RobinTrigon/CVE-2023-36143](https://github.com/RobinTrigon/CVE-2023-36143) :  ![starts](https://img.shields.io/github/stars/RobinTrigon/CVE-2023-36143.svg) ![forks](https://img.shields.io/github/forks/RobinTrigon/CVE-2023-36143.svg)

- [https://github.com/leonardobg/CVE-2023-36143](https://github.com/leonardobg/CVE-2023-36143) :  ![starts](https://img.shields.io/github/stars/leonardobg/CVE-2023-36143.svg) ![forks](https://img.shields.io/github/forks/leonardobg/CVE-2023-36143.svg)

## CVE-2023-36123
 Directory Traversal vulnerability in Hex-Dragon Plain Craft Launcher 2 version Alpha 1.3.9, allows local attackers to execute arbitrary code and gain sensitive information.



- [https://github.com/9Bakabaka/CVE-2023-36123](https://github.com/9Bakabaka/CVE-2023-36123) :  ![starts](https://img.shields.io/github/stars/9Bakabaka/CVE-2023-36123.svg) ![forks](https://img.shields.io/github/forks/9Bakabaka/CVE-2023-36123.svg)

## CVE-2023-36109
 Buffer Overflow vulnerability in JerryScript version 3.0, allows remote attackers to execute arbitrary code via ecma_stringbuilder_append_raw component at /jerry-core/ecma/base/ecma-helpers-string.c.



- [https://github.com/Limesss/CVE-2023-36109](https://github.com/Limesss/CVE-2023-36109) :  ![starts](https://img.shields.io/github/stars/Limesss/CVE-2023-36109.svg) ![forks](https://img.shields.io/github/forks/Limesss/CVE-2023-36109.svg)

## CVE-2023-36085
 The sisqualWFM 7.1.319.103 thru 7.1.319.111 for Android, has a host header injection vulnerability in its "/sisqualIdentityServer/core/" endpoint. By modifying the HTTP Host header, an attacker can change webpage links and even redirect users to arbitrary or malicious locations. This can lead to phishing attacks, malware distribution, and unauthorized access to sensitive resources.



- [https://github.com/omershaik0/CVE-2023-36085_SISQUALWFM-Host-Header-Injection](https://github.com/omershaik0/CVE-2023-36085_SISQUALWFM-Host-Header-Injection) :  ![starts](https://img.shields.io/github/stars/omershaik0/CVE-2023-36085_SISQUALWFM-Host-Header-Injection.svg) ![forks](https://img.shields.io/github/forks/omershaik0/CVE-2023-36085_SISQUALWFM-Host-Header-Injection.svg)

## CVE-2023-36076
 SQL Injection vulnerability in smanga version 3.1.9 and earlier, allows remote attackers to execute arbitrary code and gain sensitive information via mediaId, mangaId, and userId parameters in php/history/add.php.



- [https://github.com/deIndra/CVE-2023-36076](https://github.com/deIndra/CVE-2023-36076) :  ![starts](https://img.shields.io/github/stars/deIndra/CVE-2023-36076.svg) ![forks](https://img.shields.io/github/forks/deIndra/CVE-2023-36076.svg)

## CVE-2023-36025
 Windows SmartScreen Security Feature Bypass Vulnerability



- [https://github.com/ka7ana/CVE-2023-36025](https://github.com/ka7ana/CVE-2023-36025) :  ![starts](https://img.shields.io/github/stars/ka7ana/CVE-2023-36025.svg) ![forks](https://img.shields.io/github/forks/ka7ana/CVE-2023-36025.svg)

- [https://github.com/J466Y/test_CVE-2023-36025](https://github.com/J466Y/test_CVE-2023-36025) :  ![starts](https://img.shields.io/github/stars/J466Y/test_CVE-2023-36025.svg) ![forks](https://img.shields.io/github/forks/J466Y/test_CVE-2023-36025.svg)

- [https://github.com/coolman6942o/-EXPLOIT-CVE-2023-36025](https://github.com/coolman6942o/-EXPLOIT-CVE-2023-36025) :  ![starts](https://img.shields.io/github/stars/coolman6942o/-EXPLOIT-CVE-2023-36025.svg) ![forks](https://img.shields.io/github/forks/coolman6942o/-EXPLOIT-CVE-2023-36025.svg)

## CVE-2023-36003
 XAML Diagnostics Elevation of Privilege Vulnerability



- [https://github.com/m417z/CVE-2023-36003-POC](https://github.com/m417z/CVE-2023-36003-POC) :  ![starts](https://img.shields.io/github/stars/m417z/CVE-2023-36003-POC.svg) ![forks](https://img.shields.io/github/forks/m417z/CVE-2023-36003-POC.svg)

- [https://github.com/baph0m3th/CVE-2023-36003](https://github.com/baph0m3th/CVE-2023-36003) :  ![starts](https://img.shields.io/github/stars/baph0m3th/CVE-2023-36003.svg) ![forks](https://img.shields.io/github/forks/baph0m3th/CVE-2023-36003.svg)

## CVE-2023-36000
 A missing authorization check in the MacOS agent configuration endpoint of the Insider Threat Management Server enables an anonymous attacker on an adjacent network to obtain sensitive information. Successful exploitation requires an attacker to first obtain a valid agent authentication token. All versions before 7.14.3 are affected.



- [https://github.com/s3mPr1linux/CVE_2023_360003_POC](https://github.com/s3mPr1linux/CVE_2023_360003_POC) :  ![starts](https://img.shields.io/github/stars/s3mPr1linux/CVE_2023_360003_POC.svg) ![forks](https://img.shields.io/github/forks/s3mPr1linux/CVE_2023_360003_POC.svg)

## CVE-2023-35985
 An arbitrary file creation vulnerability exists in the Javascript exportDataObject API of Foxit Reader 12.1.3.15356 due to a failure to properly validate a dangerous extension. A specially crafted malicious file can create files at arbitrary locations, which can lead to arbitrary code execution. An attacker needs to trick the user into opening the malicious file to trigger this vulnerability. Exploitation is also possible if a user visits a specially-crafted malicious site if the browser plugin extension is enabled.



- [https://github.com/SpiralBL0CK/-CVE-2023-35985](https://github.com/SpiralBL0CK/-CVE-2023-35985) :  ![starts](https://img.shields.io/github/stars/SpiralBL0CK/-CVE-2023-35985.svg) ![forks](https://img.shields.io/github/forks/SpiralBL0CK/-CVE-2023-35985.svg)

- [https://github.com/N00BIER/CVE-2023-35985](https://github.com/N00BIER/CVE-2023-35985) :  ![starts](https://img.shields.io/github/stars/N00BIER/CVE-2023-35985.svg) ![forks](https://img.shields.io/github/forks/N00BIER/CVE-2023-35985.svg)

## CVE-2023-35936
 Pandoc is a Haskell library for converting from one markup format to another, and a command-line tool that uses this library. Starting in version 1.13 and prior to version 3.1.4, Pandoc is susceptible to an arbitrary file write vulnerability, which can be triggered by providing a specially crafted image element in the input when generating files using the `--extract-media` option or outputting to PDF format. This vulnerability allows an attacker to create or overwrite arbitrary files on the system ,depending on the privileges of the process running pandoc. It only affects systems that pass untrusted user input to pandoc and allow pandoc to be used to produce a PDF or with the `--extract-media` option.

The fix is to unescape the percent-encoding prior to checking that the resource is not above the working directory, and prior to extracting the extension.  Some code for checking that the path is below the working directory was flawed in a similar way and has also been fixed. Note that the `--sandbox` option, which only affects IO done by readers and writers themselves, does not block this vulnerability. The vulnerability is patched in pandoc 3.1.4. As a workaround, audit the pandoc command and disallow PDF output and the `--extract-media` option.



- [https://github.com/entroychang/CodiMD-RCE](https://github.com/entroychang/CodiMD-RCE) :  ![starts](https://img.shields.io/github/stars/entroychang/CodiMD-RCE.svg) ![forks](https://img.shields.io/github/forks/entroychang/CodiMD-RCE.svg)

## CVE-2023-35885
 CloudPanel 2 before 2.3.1 has insecure file-manager cookie authentication.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/datackmy/FallingSkies-CVE-2023-35885](https://github.com/datackmy/FallingSkies-CVE-2023-35885) :  ![starts](https://img.shields.io/github/stars/datackmy/FallingSkies-CVE-2023-35885.svg) ![forks](https://img.shields.io/github/forks/datackmy/FallingSkies-CVE-2023-35885.svg)

- [https://github.com/Chocapikk/CVE-2023-35885](https://github.com/Chocapikk/CVE-2023-35885) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-35885.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-35885.svg)

## CVE-2023-35844
 packages/backend/src/routers in Lightdash before 0.510.3 has insecure file endpoints, e.g., they allow .. directory traversal and do not ensure that an intended file extension (.csv or .png) is used.



- [https://github.com/Lserein/CVE-2023-35844](https://github.com/Lserein/CVE-2023-35844) :  ![starts](https://img.shields.io/github/stars/Lserein/CVE-2023-35844.svg) ![forks](https://img.shields.io/github/forks/Lserein/CVE-2023-35844.svg)

## CVE-2023-35843
 NocoDB through 0.106.0 (or 0.109.1) has a path traversal vulnerability that allows an unauthenticated attacker to access arbitrary files on the server by manipulating the path parameter of the /download route. This vulnerability could allow an attacker to access sensitive files and data on the server, including configuration files, source code, and other sensitive information.



- [https://github.com/Lserein/CVE-2023-35843](https://github.com/Lserein/CVE-2023-35843) :  ![starts](https://img.shields.io/github/stars/Lserein/CVE-2023-35843.svg) ![forks](https://img.shields.io/github/forks/Lserein/CVE-2023-35843.svg)

- [https://github.com/b3nguang/CVE-2023-35843](https://github.com/b3nguang/CVE-2023-35843) :  ![starts](https://img.shields.io/github/stars/b3nguang/CVE-2023-35843.svg) ![forks](https://img.shields.io/github/forks/b3nguang/CVE-2023-35843.svg)

## CVE-2023-35840
 _joinPath in elFinderVolumeLocalFileSystem.class.php in elFinder before 2.1.62 allows path traversal in the PHP LocalVolumeDriver connector.



- [https://github.com/afine-com/CVE-2023-35840](https://github.com/afine-com/CVE-2023-35840) :  ![starts](https://img.shields.io/github/stars/afine-com/CVE-2023-35840.svg) ![forks](https://img.shields.io/github/forks/afine-com/CVE-2023-35840.svg)

## CVE-2023-35828
 An issue was discovered in the Linux kernel before 6.3.2. A use-after-free was found in renesas_usb3_remove in drivers/usb/gadget/udc/renesas_usb3.c.



- [https://github.com/Trinadh465/linux-4.19.72_CVE-2023-35828](https://github.com/Trinadh465/linux-4.19.72_CVE-2023-35828) :  ![starts](https://img.shields.io/github/stars/Trinadh465/linux-4.19.72_CVE-2023-35828.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/linux-4.19.72_CVE-2023-35828.svg)

## CVE-2023-35813
 Multiple Sitecore products allow remote code execution. This affects Experience Manager, Experience Platform, and Experience Commerce through 10.3.



- [https://github.com/aalexpereira/CVE-2023-35813](https://github.com/aalexpereira/CVE-2023-35813) :  ![starts](https://img.shields.io/github/stars/aalexpereira/CVE-2023-35813.svg) ![forks](https://img.shields.io/github/forks/aalexpereira/CVE-2023-35813.svg)

- [https://github.com/BagheeraAltered/CVE-2023-35813-PoC](https://github.com/BagheeraAltered/CVE-2023-35813-PoC) :  ![starts](https://img.shields.io/github/stars/BagheeraAltered/CVE-2023-35813-PoC.svg) ![forks](https://img.shields.io/github/forks/BagheeraAltered/CVE-2023-35813-PoC.svg)

## CVE-2023-35803
 IQ Engine before 10.6r2 on Extreme Network AP devices has a Buffer Overflow.



- [https://github.com/lachlan2k/CVE-2023-35803](https://github.com/lachlan2k/CVE-2023-35803) :  ![starts](https://img.shields.io/github/stars/lachlan2k/CVE-2023-35803.svg) ![forks](https://img.shields.io/github/forks/lachlan2k/CVE-2023-35803.svg)

## CVE-2023-35801
 A directory traversal vulnerability in Safe Software FME Server before 2022.2.5 allows an attacker to bypass validation when editing a network-based resource connection, resulting in the unauthorized reading and writing of arbitrary files. Successful exploitation requires an attacker to have access to a user account with write privileges. FME Flow 2023.0 is also a fixed version.



- [https://github.com/trustcves/CVE-2023-35801](https://github.com/trustcves/CVE-2023-35801) :  ![starts](https://img.shields.io/github/stars/trustcves/CVE-2023-35801.svg) ![forks](https://img.shields.io/github/forks/trustcves/CVE-2023-35801.svg)

## CVE-2023-35794
 An issue was discovered in Cassia Access Controller 2.1.1.2303271039. The Web SSH terminal endpoint (spawned console) can be accessed without authentication. Specifically, there is no session cookie validation on the Access Controller; instead, there is only Basic Authentication to the SSH console.



- [https://github.com/Dodge-MPTC/CVE-2023-35794-WebSSH-Hijacking](https://github.com/Dodge-MPTC/CVE-2023-35794-WebSSH-Hijacking) :  ![starts](https://img.shields.io/github/stars/Dodge-MPTC/CVE-2023-35794-WebSSH-Hijacking.svg) ![forks](https://img.shields.io/github/forks/Dodge-MPTC/CVE-2023-35794-WebSSH-Hijacking.svg)

## CVE-2023-35793
 An issue was discovered in Cassia Access Controller 2.1.1.2303271039. Establishing a web SSH session to gateways is vulnerable to Cross Site Request Forgery (CSRF) attacks.



- [https://github.com/Dodge-MPTC/CVE-2023-35793-CSRF-On-Web-SSH](https://github.com/Dodge-MPTC/CVE-2023-35793-CSRF-On-Web-SSH) :  ![starts](https://img.shields.io/github/stars/Dodge-MPTC/CVE-2023-35793-CSRF-On-Web-SSH.svg) ![forks](https://img.shields.io/github/forks/Dodge-MPTC/CVE-2023-35793-CSRF-On-Web-SSH.svg)

## CVE-2023-35744
 D-Link DAP-2622 DDP Configuration Restore Server IPv6 Address Stack-based Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-2622 routers. Authentication is not required to exploit this vulnerability.

The specific flaw exists within the DDP service. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.
. Was ZDI-CAN-20071.



- [https://github.com/ADSSA-IT/CVE-2023-35744](https://github.com/ADSSA-IT/CVE-2023-35744) :  ![starts](https://img.shields.io/github/stars/ADSSA-IT/CVE-2023-35744.svg) ![forks](https://img.shields.io/github/forks/ADSSA-IT/CVE-2023-35744.svg)

## CVE-2023-35687
 In MtpPropertyValue of MtpProperty.h, there is a possible memory corruption due to a use after free. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/pazhanivel07/frameworks_av_AOSP_10_r33_CVE-2023-35687_CVE-2023-35679](https://github.com/pazhanivel07/frameworks_av_AOSP_10_r33_CVE-2023-35687_CVE-2023-35679) :  ![starts](https://img.shields.io/github/stars/pazhanivel07/frameworks_av_AOSP_10_r33_CVE-2023-35687_CVE-2023-35679.svg) ![forks](https://img.shields.io/github/forks/pazhanivel07/frameworks_av_AOSP_10_r33_CVE-2023-35687_CVE-2023-35679.svg)

## CVE-2023-35679
 In MtpPropertyValue of MtpProperty.h, there is a possible out of bounds read due to uninitialized data. This could lead to local information disclosure with no additional execution privileges needed. User interaction is needed for exploitation.



- [https://github.com/pazhanivel07/frameworks_av_AOSP_10_r33_CVE-2023-35687_CVE-2023-35679](https://github.com/pazhanivel07/frameworks_av_AOSP_10_r33_CVE-2023-35687_CVE-2023-35679) :  ![starts](https://img.shields.io/github/stars/pazhanivel07/frameworks_av_AOSP_10_r33_CVE-2023-35687_CVE-2023-35679.svg) ![forks](https://img.shields.io/github/forks/pazhanivel07/frameworks_av_AOSP_10_r33_CVE-2023-35687_CVE-2023-35679.svg)

## CVE-2023-35674
 In onCreate of WindowState.java, there is a possible way to launch a background activity due to a logic error in the code. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/Thampakon/CVE-2023-35674](https://github.com/Thampakon/CVE-2023-35674) :  ![starts](https://img.shields.io/github/stars/Thampakon/CVE-2023-35674.svg) ![forks](https://img.shields.io/github/forks/Thampakon/CVE-2023-35674.svg)

## CVE-2023-35671
 In onHostEmulationData of HostEmulationManager.java, there is a possible way for a general purpose NFC reader to read the full card number and expiry details when the device is in locked screen mode due to a logic error in the code. This could lead to local information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/MrTiz/CVE-2023-35671](https://github.com/MrTiz/CVE-2023-35671) :  ![starts](https://img.shields.io/github/stars/MrTiz/CVE-2023-35671.svg) ![forks](https://img.shields.io/github/forks/MrTiz/CVE-2023-35671.svg)

## CVE-2023-35636
 Microsoft Outlook Information Disclosure Vulnerability



- [https://github.com/duy-31/CVE-2023-35636](https://github.com/duy-31/CVE-2023-35636) :  ![starts](https://img.shields.io/github/stars/duy-31/CVE-2023-35636.svg) ![forks](https://img.shields.io/github/forks/duy-31/CVE-2023-35636.svg)

## CVE-2023-35086
 
It is identified a format string vulnerability in ASUS RT-AX56U V2 & RT-AC86U. This vulnerability is caused by directly using input as a format string when calling syslog in logmessage_normal function, in the do_detwan_cgi module of httpd. A remote attacker with administrator privilege can exploit this vulnerability to perform remote arbitrary code execution, arbitrary system operation or disrupt service.

This issue affects RT-AX56U V2: 3.0.0.4.386_50460; RT-AC86U: 3.0.0.4_386_51529.





- [https://github.com/tin-z/CVE-2023-35086-POC](https://github.com/tin-z/CVE-2023-35086-POC) :  ![starts](https://img.shields.io/github/stars/tin-z/CVE-2023-35086-POC.svg) ![forks](https://img.shields.io/github/forks/tin-z/CVE-2023-35086-POC.svg)

## CVE-2023-35085
 An integer overflow vulnerability in all UniFi Access Points and Switches, excluding the Switch Flex Mini, with SNMP Monitoring and default settings enabled could allow a Remote Code Execution (RCE).

 

Affected Products:
All UniFi Access Points (Version 6.5.50 and earlier)
All UniFi Switches (Version 6.5.32 and earlier) 
-USW Flex Mini excluded.
 

Mitigation:
Update UniFi Access Points to Version 6.5.62 or later.
Update the UniFi Switches to Version 6.5.59 or later.



- [https://github.com/maoruiQa/CVE-2023-35085-POC-EXP](https://github.com/maoruiQa/CVE-2023-35085-POC-EXP) :  ![starts](https://img.shields.io/github/stars/maoruiQa/CVE-2023-35085-POC-EXP.svg) ![forks](https://img.shields.io/github/forks/maoruiQa/CVE-2023-35085-POC-EXP.svg)

## CVE-2023-35082
 An authentication bypass vulnerability in Ivanti EPMM 11.10 and older, allows unauthorized users to access restricted functionality or resources of the application without proper authentication. This vulnerability is unique to CVE-2023-35078 announced earlier.



- [https://github.com/Chocapikk/CVE-2023-35082](https://github.com/Chocapikk/CVE-2023-35082) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-35082.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-35082.svg)

## CVE-2023-35080
 A vulnerability has been identified in the Ivanti Secure Access Windows client, which could allow a locally authenticated attacker to exploit a vulnerable configuration, potentially leading to various security risks, including the escalation of privileges, denial of service, or information disclosure.



- [https://github.com/tijme/ivanti-cve-2023-35080-privilege-escalation-bof](https://github.com/tijme/ivanti-cve-2023-35080-privilege-escalation-bof) :  ![starts](https://img.shields.io/github/stars/tijme/ivanti-cve-2023-35080-privilege-escalation-bof.svg) ![forks](https://img.shields.io/github/forks/tijme/ivanti-cve-2023-35080-privilege-escalation-bof.svg)

- [https://github.com/HopHouse/Ivanti-Pulse_VPN-Client_Exploit-CVE-2023-35080_Privilege-escalation](https://github.com/HopHouse/Ivanti-Pulse_VPN-Client_Exploit-CVE-2023-35080_Privilege-escalation) :  ![starts](https://img.shields.io/github/stars/HopHouse/Ivanti-Pulse_VPN-Client_Exploit-CVE-2023-35080_Privilege-escalation.svg) ![forks](https://img.shields.io/github/forks/HopHouse/Ivanti-Pulse_VPN-Client_Exploit-CVE-2023-35080_Privilege-escalation.svg)

## CVE-2023-35078
 An authentication bypass vulnerability in Ivanti EPMM allows unauthorized users to access restricted functionality or resources of the application without proper authentication.



- [https://github.com/vchan-in/CVE-2023-35078-Exploit-POC](https://github.com/vchan-in/CVE-2023-35078-Exploit-POC) :  ![starts](https://img.shields.io/github/stars/vchan-in/CVE-2023-35078-Exploit-POC.svg) ![forks](https://img.shields.io/github/forks/vchan-in/CVE-2023-35078-Exploit-POC.svg)

- [https://github.com/lager1/CVE-2023-35078](https://github.com/lager1/CVE-2023-35078) :  ![starts](https://img.shields.io/github/stars/lager1/CVE-2023-35078.svg) ![forks](https://img.shields.io/github/forks/lager1/CVE-2023-35078.svg)

- [https://github.com/raytheon0x21/CVE-2023-35078](https://github.com/raytheon0x21/CVE-2023-35078) :  ![starts](https://img.shields.io/github/stars/raytheon0x21/CVE-2023-35078.svg) ![forks](https://img.shields.io/github/forks/raytheon0x21/CVE-2023-35078.svg)

- [https://github.com/emanueldosreis/nmap-CVE-2023-35078-Exploit](https://github.com/emanueldosreis/nmap-CVE-2023-35078-Exploit) :  ![starts](https://img.shields.io/github/stars/emanueldosreis/nmap-CVE-2023-35078-Exploit.svg) ![forks](https://img.shields.io/github/forks/emanueldosreis/nmap-CVE-2023-35078-Exploit.svg)

- [https://github.com/synfinner/CVE-2023-35078](https://github.com/synfinner/CVE-2023-35078) :  ![starts](https://img.shields.io/github/stars/synfinner/CVE-2023-35078.svg) ![forks](https://img.shields.io/github/forks/synfinner/CVE-2023-35078.svg)

- [https://github.com/Blue-number/CVE-2023-35078](https://github.com/Blue-number/CVE-2023-35078) :  ![starts](https://img.shields.io/github/stars/Blue-number/CVE-2023-35078.svg) ![forks](https://img.shields.io/github/forks/Blue-number/CVE-2023-35078.svg)

## CVE-2023-35001
 Linux Kernel nftables Out-Of-Bounds Read/Write Vulnerability; nft_byteorder poorly handled vm register contents when CAP_NET_ADMIN is in any user or network namespace



- [https://github.com/synacktiv/CVE-2023-35001](https://github.com/synacktiv/CVE-2023-35001) :  ![starts](https://img.shields.io/github/stars/synacktiv/CVE-2023-35001.svg) ![forks](https://img.shields.io/github/forks/synacktiv/CVE-2023-35001.svg)

- [https://github.com/syedhafiz1234/nftables-oob-read-write-exploit-CVE-2023-35001-](https://github.com/syedhafiz1234/nftables-oob-read-write-exploit-CVE-2023-35001-) :  ![starts](https://img.shields.io/github/stars/syedhafiz1234/nftables-oob-read-write-exploit-CVE-2023-35001-.svg) ![forks](https://img.shields.io/github/forks/syedhafiz1234/nftables-oob-read-write-exploit-CVE-2023-35001-.svg)

- [https://github.com/mrbrelax/Exploit_CVE-2023-35001](https://github.com/mrbrelax/Exploit_CVE-2023-35001) :  ![starts](https://img.shields.io/github/stars/mrbrelax/Exploit_CVE-2023-35001.svg) ![forks](https://img.shields.io/github/forks/mrbrelax/Exploit_CVE-2023-35001.svg)

## CVE-2023-34992
 A improper neutralization of special elements used in an os command ('os command injection') in Fortinet FortiSIEM version 7.0.0 and 6.7.0 through 6.7.5 and 6.6.0 through 6.6.3 and 6.5.0 through 6.5.1 and 6.4.0 through 6.4.2 allows attacker to execute unauthorized code or commands via crafted API requests.



- [https://github.com/horizon3ai/CVE-2023-34992](https://github.com/horizon3ai/CVE-2023-34992) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2023-34992.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2023-34992.svg)

- [https://github.com/d0rb/CVE-2023-34992-Checker](https://github.com/d0rb/CVE-2023-34992-Checker) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-34992-Checker.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-34992-Checker.svg)

## CVE-2023-34965
 SSPanel-Uim 2023.3 does not restrict access to the /link/ interface which can lead to a leak of user information.



- [https://github.com/AgentY0/CVE-2023-34965](https://github.com/AgentY0/CVE-2023-34965) :  ![starts](https://img.shields.io/github/stars/AgentY0/CVE-2023-34965.svg) ![forks](https://img.shields.io/github/forks/AgentY0/CVE-2023-34965.svg)

## CVE-2023-34960
 A command injection vulnerability in the wsConvertPpt component of Chamilo v1.11.* up to v1.11.18 allows attackers to execute arbitrary commands via a SOAP API call with a crafted PowerPoint name.



- [https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance](https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance) :  ![starts](https://img.shields.io/github/stars/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg) ![forks](https://img.shields.io/github/forks/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg)

- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/Aituglo/CVE-2023-34960](https://github.com/Aituglo/CVE-2023-34960) :  ![starts](https://img.shields.io/github/stars/Aituglo/CVE-2023-34960.svg) ![forks](https://img.shields.io/github/forks/Aituglo/CVE-2023-34960.svg)

- [https://github.com/ThatNotEasy/CVE-2023-34960](https://github.com/ThatNotEasy/CVE-2023-34960) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2023-34960.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2023-34960.svg)

- [https://github.com/Mantodkaz/CVE-2023-34960](https://github.com/Mantodkaz/CVE-2023-34960) :  ![starts](https://img.shields.io/github/stars/Mantodkaz/CVE-2023-34960.svg) ![forks](https://img.shields.io/github/forks/Mantodkaz/CVE-2023-34960.svg)

- [https://github.com/Jenderal92/CHAMILO-CVE-2023-34960](https://github.com/Jenderal92/CHAMILO-CVE-2023-34960) :  ![starts](https://img.shields.io/github/stars/Jenderal92/CHAMILO-CVE-2023-34960.svg) ![forks](https://img.shields.io/github/forks/Jenderal92/CHAMILO-CVE-2023-34960.svg)

- [https://github.com/YongYe-Security/CVE-2023-34960](https://github.com/YongYe-Security/CVE-2023-34960) :  ![starts](https://img.shields.io/github/stars/YongYe-Security/CVE-2023-34960.svg) ![forks](https://img.shields.io/github/forks/YongYe-Security/CVE-2023-34960.svg)

- [https://github.com/tucommenceapousser/CVE-2023-34960-ex](https://github.com/tucommenceapousser/CVE-2023-34960-ex) :  ![starts](https://img.shields.io/github/stars/tucommenceapousser/CVE-2023-34960-ex.svg) ![forks](https://img.shields.io/github/forks/tucommenceapousser/CVE-2023-34960-ex.svg)

## CVE-2023-34924
 H3C Magic B1STW B1STV100R012 was discovered to contain a stack overflow via the function SetAPInfoById. This vulnerability allows attackers to cause a Denial of Service (DoS) via a crafted POST request.



- [https://github.com/ChrisL0tus/CVE-2023-34924](https://github.com/ChrisL0tus/CVE-2023-34924) :  ![starts](https://img.shields.io/github/stars/ChrisL0tus/CVE-2023-34924.svg) ![forks](https://img.shields.io/github/forks/ChrisL0tus/CVE-2023-34924.svg)

## CVE-2023-34853
 Buffer Overflow vulnerability in Supermicro motherboard X12DPG-QR 1.4b allows local attackers to hijack control flow via manipulation of SmcSecurityEraseSetupVar variable.



- [https://github.com/risuxx/CVE-2023-34853](https://github.com/risuxx/CVE-2023-34853) :  ![starts](https://img.shields.io/github/stars/risuxx/CVE-2023-34853.svg) ![forks](https://img.shields.io/github/forks/risuxx/CVE-2023-34853.svg)

## CVE-2023-34852
 PublicCMS =V4.0.202302 is vulnerable to Insecure Permissions.



- [https://github.com/funny-kill/CVE-2023-34852](https://github.com/funny-kill/CVE-2023-34852) :  ![starts](https://img.shields.io/github/stars/funny-kill/CVE-2023-34852.svg) ![forks](https://img.shields.io/github/forks/funny-kill/CVE-2023-34852.svg)

## CVE-2023-34845
 Bludit v3.14.1 was discovered to contain an arbitrary file upload vulnerability in the component /admin/new-content. This vulnerability allows attackers to execute arbitrary web scripts or HTML via uploading a crafted SVG file. NOTE: the product's security model is that users are trusted by the administrator to insert arbitrary content (users cannot create their own accounts through self-registration).



- [https://github.com/r4vanan/CVE-2023-34845](https://github.com/r4vanan/CVE-2023-34845) :  ![starts](https://img.shields.io/github/stars/r4vanan/CVE-2023-34845.svg) ![forks](https://img.shields.io/github/forks/r4vanan/CVE-2023-34845.svg)

## CVE-2023-34843
 Traggo Server 0.3.0 is vulnerable to directory traversal via a crafted GET request.



- [https://github.com/rootd4ddy/CVE-2023-34843](https://github.com/rootd4ddy/CVE-2023-34843) :  ![starts](https://img.shields.io/github/stars/rootd4ddy/CVE-2023-34843.svg) ![forks](https://img.shields.io/github/forks/rootd4ddy/CVE-2023-34843.svg)

## CVE-2023-34840
 angular-ui-notification v0.1.0, v0.2.0, and v0.3.6 was discovered to contain a cross-site scripting (XSS) vulnerability.



- [https://github.com/Xh4H/CVE-2023-34840](https://github.com/Xh4H/CVE-2023-34840) :  ![starts](https://img.shields.io/github/stars/Xh4H/CVE-2023-34840.svg) ![forks](https://img.shields.io/github/forks/Xh4H/CVE-2023-34840.svg)

## CVE-2023-34839
 A Cross Site Request Forgery (CSRF) vulnerability in Issabel issabel-pbx v.4.0.0-6 allows a remote attacker to gain privileges via a Custom CSRF exploit to create new user function in the application.



- [https://github.com/sahiloj/CVE-2023-34839](https://github.com/sahiloj/CVE-2023-34839) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-34839.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-34839.svg)

## CVE-2023-34838
 A Cross Site Scripting vulnerability in Microworld Technologies eScan Management console v.14.0.1400.2281 allows a remote attacker to execute arbitrary code via a crafted script to the Description parameter.



- [https://github.com/sahiloj/CVE-2023-34838](https://github.com/sahiloj/CVE-2023-34838) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-34838.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-34838.svg)

## CVE-2023-34837
 A Cross Site Scripting vulnerability in Microworld Technologies eScan Management console v.14.0.1400.2281 allows a remote attacker to execute arbitrary code via a vulnerable parameter GrpPath.



- [https://github.com/sahiloj/CVE-2023-34837](https://github.com/sahiloj/CVE-2023-34837) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-34837.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-34837.svg)

## CVE-2023-34836
 A Cross Site Scripting vulnerability in Microworld Technologies eScan Management console v.14.0.1400.2281 allows a remote attacker to execute arbitrary code via a crafted script to the Dtltyp and ListName parameters.



- [https://github.com/sahiloj/CVE-2023-34836](https://github.com/sahiloj/CVE-2023-34836) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-34836.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-34836.svg)

## CVE-2023-34835
 A Cross Site Scripting vulnerability in Microworld Technologies eScan Management console v.14.0.1400.2281 allows a remote attacker to execute arbitrary JavaScript code via a vulnerable delete_file parameter.



- [https://github.com/sahiloj/CVE-2023-34835](https://github.com/sahiloj/CVE-2023-34835) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-34835.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-34835.svg)

## CVE-2023-34830
 i-doit Open v24 was discovered to contain a reflected cross-site scripting (XSS) vulnerability via the timeout parameter on the login page.



- [https://github.com/leekenghwa/CVE-2023-34830---Reflected-XSS-found-in-I-doit-Open-v24-and-below](https://github.com/leekenghwa/CVE-2023-34830---Reflected-XSS-found-in-I-doit-Open-v24-and-below) :  ![starts](https://img.shields.io/github/stars/leekenghwa/CVE-2023-34830---Reflected-XSS-found-in-I-doit-Open-v24-and-below.svg) ![forks](https://img.shields.io/github/forks/leekenghwa/CVE-2023-34830---Reflected-XSS-found-in-I-doit-Open-v24-and-below.svg)

## CVE-2023-34732
 An issue in the userId parameter in the change password function of Flytxt NEON-dX v0.0.1-SNAPSHOT-6.9-qa-2-9-g5502a0c allows attackers to execute brute force attacks to discover user passwords.



- [https://github.com/saykino/CVE-2023-34732](https://github.com/saykino/CVE-2023-34732) :  ![starts](https://img.shields.io/github/stars/saykino/CVE-2023-34732.svg) ![forks](https://img.shields.io/github/forks/saykino/CVE-2023-34732.svg)

## CVE-2023-34634
 Greenshot 1.2.10 and below allows arbitrary code execution because .NET content is insecurely deserialized when a .greenshot file is opened.



- [https://github.com/radman404/CVE-2023-34634](https://github.com/radman404/CVE-2023-34634) :  ![starts](https://img.shields.io/github/stars/radman404/CVE-2023-34634.svg) ![forks](https://img.shields.io/github/forks/radman404/CVE-2023-34634.svg)

## CVE-2023-34600
 Adiscon LogAnalyzer v4.1.13 and before is vulnerable to SQL Injection.



- [https://github.com/costacoco/Adiscon](https://github.com/costacoco/Adiscon) :  ![starts](https://img.shields.io/github/stars/costacoco/Adiscon.svg) ![forks](https://img.shields.io/github/forks/costacoco/Adiscon.svg)

## CVE-2023-34599
 Multiple Cross-Site Scripting (XSS) vulnerabilities have been identified in Gibbon v25.0.0, which enable attackers to execute arbitrary Javascript code.



- [https://github.com/maddsec/CVE-2023-34599](https://github.com/maddsec/CVE-2023-34599) :  ![starts](https://img.shields.io/github/stars/maddsec/CVE-2023-34599.svg) ![forks](https://img.shields.io/github/forks/maddsec/CVE-2023-34599.svg)

## CVE-2023-34598
 Gibbon v25.0.0 is vulnerable to a Local File Inclusion (LFI) where it's possible to include the content of several files present in the installation folder in the server's response.



- [https://github.com/maddsec/CVE-2023-34598](https://github.com/maddsec/CVE-2023-34598) :  ![starts](https://img.shields.io/github/stars/maddsec/CVE-2023-34598.svg) ![forks](https://img.shields.io/github/forks/maddsec/CVE-2023-34598.svg)

- [https://github.com/Lserein/CVE-2023-34598](https://github.com/Lserein/CVE-2023-34598) :  ![starts](https://img.shields.io/github/stars/Lserein/CVE-2023-34598.svg) ![forks](https://img.shields.io/github/forks/Lserein/CVE-2023-34598.svg)

## CVE-2023-34584
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/fu2x2000/-CVE-2023-34584](https://github.com/fu2x2000/-CVE-2023-34584) :  ![starts](https://img.shields.io/github/stars/fu2x2000/-CVE-2023-34584.svg) ![forks](https://img.shields.io/github/forks/fu2x2000/-CVE-2023-34584.svg)

## CVE-2023-34537
 A Reflected XSS was discovered in HotelDruid version 3.0.5, an attacker can issue malicious code/command on affected webpage's parameter to trick user on browser and/or exfiltrate data.



- [https://github.com/leekenghwa/CVE-2023-34537---XSS-reflected--found-in-HotelDruid-3.0.5](https://github.com/leekenghwa/CVE-2023-34537---XSS-reflected--found-in-HotelDruid-3.0.5) :  ![starts](https://img.shields.io/github/stars/leekenghwa/CVE-2023-34537---XSS-reflected--found-in-HotelDruid-3.0.5.svg) ![forks](https://img.shields.io/github/forks/leekenghwa/CVE-2023-34537---XSS-reflected--found-in-HotelDruid-3.0.5.svg)

## CVE-2023-34468
 The DBCPConnectionPool and HikariCPConnectionPool Controller Services in Apache NiFi 0.0.2 through 1.21.0 allow an authenticated and authorized user to configure a Database URL with the H2 driver that enables custom code execution.

The resolution validates the Database URL and rejects H2 JDBC locations.

You are recommended to upgrade to version 1.22.0 or later which fixes this issue.



- [https://github.com/mbadanoiu/CVE-2023-34468](https://github.com/mbadanoiu/CVE-2023-34468) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2023-34468.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2023-34468.svg)

- [https://github.com/mbadanoiu/CVE-2023-40037](https://github.com/mbadanoiu/CVE-2023-40037) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2023-40037.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2023-40037.svg)

## CVE-2023-34362
 In Progress MOVEit Transfer before 2021.0.6 (13.0.6), 2021.1.4 (13.1.4), 2022.0.4 (14.0.4), 2022.1.5 (14.1.5), and 2023.0.1 (15.0.1), a SQL injection vulnerability has been found in the MOVEit Transfer web application that could allow an unauthenticated attacker to gain access to MOVEit Transfer's database. Depending on the database engine being used (MySQL, Microsoft SQL Server, or Azure SQL), an attacker may be able to infer information about the structure and contents of the database, and execute SQL statements that alter or delete database elements. NOTE: this is exploited in the wild in May and June 2023; exploitation of unpatched systems can occur via HTTP or HTTPS. All versions (e.g., 2020.0 and 2019x) before the five explicitly mentioned versions are affected, including older unsupported versions.



- [https://github.com/horizon3ai/CVE-2023-34362](https://github.com/horizon3ai/CVE-2023-34362) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2023-34362.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2023-34362.svg)

- [https://github.com/sfewer-r7/CVE-2023-34362](https://github.com/sfewer-r7/CVE-2023-34362) :  ![starts](https://img.shields.io/github/stars/sfewer-r7/CVE-2023-34362.svg) ![forks](https://img.shields.io/github/forks/sfewer-r7/CVE-2023-34362.svg)

- [https://github.com/Malwareman007/CVE-2023-34362](https://github.com/Malwareman007/CVE-2023-34362) :  ![starts](https://img.shields.io/github/stars/Malwareman007/CVE-2023-34362.svg) ![forks](https://img.shields.io/github/forks/Malwareman007/CVE-2023-34362.svg)

- [https://github.com/kenbuckler/MOVEit-CVE-2023-34362](https://github.com/kenbuckler/MOVEit-CVE-2023-34362) :  ![starts](https://img.shields.io/github/stars/kenbuckler/MOVEit-CVE-2023-34362.svg) ![forks](https://img.shields.io/github/forks/kenbuckler/MOVEit-CVE-2023-34362.svg)

- [https://github.com/deepinstinct/MOVEit_CVE-2023-34362_IOCs](https://github.com/deepinstinct/MOVEit_CVE-2023-34362_IOCs) :  ![starts](https://img.shields.io/github/stars/deepinstinct/MOVEit_CVE-2023-34362_IOCs.svg) ![forks](https://img.shields.io/github/forks/deepinstinct/MOVEit_CVE-2023-34362_IOCs.svg)

- [https://github.com/errorfiathck/MOVEit-Exploit](https://github.com/errorfiathck/MOVEit-Exploit) :  ![starts](https://img.shields.io/github/stars/errorfiathck/MOVEit-Exploit.svg) ![forks](https://img.shields.io/github/forks/errorfiathck/MOVEit-Exploit.svg)

- [https://github.com/toorandom/moveit-payload-decrypt-CVE-2023-34362](https://github.com/toorandom/moveit-payload-decrypt-CVE-2023-34362) :  ![starts](https://img.shields.io/github/stars/toorandom/moveit-payload-decrypt-CVE-2023-34362.svg) ![forks](https://img.shields.io/github/forks/toorandom/moveit-payload-decrypt-CVE-2023-34362.svg)

- [https://github.com/aditibv/MOVEit-CVE-2023-34362](https://github.com/aditibv/MOVEit-CVE-2023-34362) :  ![starts](https://img.shields.io/github/stars/aditibv/MOVEit-CVE-2023-34362.svg) ![forks](https://img.shields.io/github/forks/aditibv/MOVEit-CVE-2023-34362.svg)

- [https://github.com/lithuanian-g/cve-2023-34362-iocs](https://github.com/lithuanian-g/cve-2023-34362-iocs) :  ![starts](https://img.shields.io/github/stars/lithuanian-g/cve-2023-34362-iocs.svg) ![forks](https://img.shields.io/github/forks/lithuanian-g/cve-2023-34362-iocs.svg)

- [https://github.com/Chinyemba-ck/MOVEit-CVE-2023-34362](https://github.com/Chinyemba-ck/MOVEit-CVE-2023-34362) :  ![starts](https://img.shields.io/github/stars/Chinyemba-ck/MOVEit-CVE-2023-34362.svg) ![forks](https://img.shields.io/github/forks/Chinyemba-ck/MOVEit-CVE-2023-34362.svg)

- [https://github.com/Naveenbana5250/CVE-2023-34362-Defense-Package](https://github.com/Naveenbana5250/CVE-2023-34362-Defense-Package) :  ![starts](https://img.shields.io/github/stars/Naveenbana5250/CVE-2023-34362-Defense-Package.svg) ![forks](https://img.shields.io/github/forks/Naveenbana5250/CVE-2023-34362-Defense-Package.svg)

- [https://github.com/glen-pearson/MoveIT-CVE-2023-34362-RCE](https://github.com/glen-pearson/MoveIT-CVE-2023-34362-RCE) :  ![starts](https://img.shields.io/github/stars/glen-pearson/MoveIT-CVE-2023-34362-RCE.svg) ![forks](https://img.shields.io/github/forks/glen-pearson/MoveIT-CVE-2023-34362-RCE.svg)

## CVE-2023-34312
 In Tencent QQ through 9.7.8.29039 and TIM through 3.4.7.22084, QQProtect.exe and QQProtectEngine.dll do not validate pointers from inter-process communication, which leads to a write-what-where condition.



- [https://github.com/vi3t1/qq-tim-elevation](https://github.com/vi3t1/qq-tim-elevation) :  ![starts](https://img.shields.io/github/stars/vi3t1/qq-tim-elevation.svg) ![forks](https://img.shields.io/github/forks/vi3t1/qq-tim-elevation.svg)

- [https://github.com/lan1oc/CVE-2023-34312-exp](https://github.com/lan1oc/CVE-2023-34312-exp) :  ![starts](https://img.shields.io/github/stars/lan1oc/CVE-2023-34312-exp.svg) ![forks](https://img.shields.io/github/forks/lan1oc/CVE-2023-34312-exp.svg)

## CVE-2023-34212
 The JndiJmsConnectionFactoryProvider Controller Service, along with the ConsumeJMS and PublishJMS Processors, in Apache NiFi 1.8.0 through 1.21.0 allow an authenticated and authorized user to configure URL and library properties that enable deserialization of untrusted data from a remote location.

The resolution validates the JNDI URL and restricts locations to a set of allowed schemes.

You are recommended to upgrade to version 1.22.0 or later which fixes this issue.



- [https://github.com/mbadanoiu/CVE-2023-34212](https://github.com/mbadanoiu/CVE-2023-34212) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2023-34212.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2023-34212.svg)

- [https://github.com/mbadanoiu/CVE-2023-40037](https://github.com/mbadanoiu/CVE-2023-40037) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2023-40037.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2023-40037.svg)

## CVE-2023-34194
 StringEqual in TiXmlDeclaration::Parse in tinyxmlparser.cpp in TinyXML through 2.6.2 has a reachable assertion (and application exit) via a crafted XML document with a '\0' located after whitespace.



- [https://github.com/vm2mv/tinyxml](https://github.com/vm2mv/tinyxml) :  ![starts](https://img.shields.io/github/stars/vm2mv/tinyxml.svg) ![forks](https://img.shields.io/github/forks/vm2mv/tinyxml.svg)

## CVE-2023-34152
 A vulnerability was found in ImageMagick. This security flaw cause a remote code execution vulnerability in OpenBlob with --enable-pipes configured.



- [https://github.com/overgrowncarrot1/ImageTragick_CVE-2023-34152](https://github.com/overgrowncarrot1/ImageTragick_CVE-2023-34152) :  ![starts](https://img.shields.io/github/stars/overgrowncarrot1/ImageTragick_CVE-2023-34152.svg) ![forks](https://img.shields.io/github/forks/overgrowncarrot1/ImageTragick_CVE-2023-34152.svg)

- [https://github.com/SudoIndividual/CVE-2023-34152](https://github.com/SudoIndividual/CVE-2023-34152) :  ![starts](https://img.shields.io/github/stars/SudoIndividual/CVE-2023-34152.svg) ![forks](https://img.shields.io/github/forks/SudoIndividual/CVE-2023-34152.svg)

## CVE-2023-34124
 The authentication mechanism in SonicWall GMS and Analytics Web Services had insufficient checks, allowing authentication bypass. This issue affects GMS: 9.3.2-SP1 and earlier versions; Analytics: 2.5.0.4-R7 and earlier versions.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

## CVE-2023-34096
 Thruk is a multibackend monitoring webinterface which currently supports Naemon, Icinga, Shinken and Nagios as backends. In versions 3.06 and prior, the file `panorama.pm` is vulnerable to a Path Traversal vulnerability which allows an attacker to upload a file to any folder which has write permissions on the affected system. The parameter location is not filtered, validated or sanitized and it accepts any kind of characters. For a path traversal attack, the only characters required were the dot (`.`) and the slash (`/`). A fix is available in version 3.06.2.



- [https://github.com/galoget/Thruk-CVE-2023-34096](https://github.com/galoget/Thruk-CVE-2023-34096) :  ![starts](https://img.shields.io/github/stars/galoget/Thruk-CVE-2023-34096.svg) ![forks](https://img.shields.io/github/forks/galoget/Thruk-CVE-2023-34096.svg)

## CVE-2023-34051
 VMware Aria Operations for Logs contains an authentication bypass vulnerability. An unauthenticated, malicious actor can inject files into the operating system of an impacted appliance which can result in remote code execution.




- [https://github.com/horizon3ai/CVE-2023-34051](https://github.com/horizon3ai/CVE-2023-34051) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2023-34051.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2023-34051.svg)

## CVE-2023-34050
 









In spring AMQP versions 1.0.0 to
2.4.16 and 3.0.0 to 3.0.9 , allowed list patterns for deserializable class
names were added to Spring AMQP, allowing users to lock down deserialization of
data in messages from untrusted sources; however by default, when no allowed
list was provided, all classes could be deserialized.



Specifically, an application is
vulnerable if




   *  the
     SimpleMessageConverter or SerializerMessageConverter is used

   *  the user
     does not configure allowed list patterns

   *  untrusted
     message originators gain permissions to write messages to the RabbitMQ
     broker to send malicious content













- [https://github.com/X1r0z/spring-amqp-deserialization](https://github.com/X1r0z/spring-amqp-deserialization) :  ![starts](https://img.shields.io/github/stars/X1r0z/spring-amqp-deserialization.svg) ![forks](https://img.shields.io/github/forks/X1r0z/spring-amqp-deserialization.svg)

## CVE-2023-34040
 In Spring for Apache Kafka 3.0.9 and earlier and versions 2.9.10 and earlier, a possible deserialization attack vector existed, but only if unusual configuration was applied. An attacker would have to construct a malicious serialized object in one of the deserialization exception record headers.

Specifically, an application is vulnerable when all of the following are true:

  *  The user does not configure an ErrorHandlingDeserializer for the key and/or value of the record
  *  The user explicitly sets container properties checkDeserExWhenKeyNull and/or checkDeserExWhenValueNull container properties to true.
  *  The user allows untrusted sources to publish to a Kafka topic


By default, these properties are false, and the container only attempts to deserialize the headers if an ErrorHandlingDeserializer is configured. The ErrorHandlingDeserializer prevents the vulnerability by removing any such malicious headers before processing the record.






- [https://github.com/Contrast-Security-OSS/Spring-Kafka-POC-CVE-2023-34040](https://github.com/Contrast-Security-OSS/Spring-Kafka-POC-CVE-2023-34040) :  ![starts](https://img.shields.io/github/stars/Contrast-Security-OSS/Spring-Kafka-POC-CVE-2023-34040.svg) ![forks](https://img.shields.io/github/forks/Contrast-Security-OSS/Spring-Kafka-POC-CVE-2023-34040.svg)

- [https://github.com/pyn3rd/CVE-2023-34040](https://github.com/pyn3rd/CVE-2023-34040) :  ![starts](https://img.shields.io/github/stars/pyn3rd/CVE-2023-34040.svg) ![forks](https://img.shields.io/github/forks/pyn3rd/CVE-2023-34040.svg)

- [https://github.com/huyennhat-dev/cve-2023-34040](https://github.com/huyennhat-dev/cve-2023-34040) :  ![starts](https://img.shields.io/github/stars/huyennhat-dev/cve-2023-34040.svg) ![forks](https://img.shields.io/github/forks/huyennhat-dev/cve-2023-34040.svg)

- [https://github.com/buiduchoang24/CVE-2023-34040](https://github.com/buiduchoang24/CVE-2023-34040) :  ![starts](https://img.shields.io/github/stars/buiduchoang24/CVE-2023-34040.svg) ![forks](https://img.shields.io/github/forks/buiduchoang24/CVE-2023-34040.svg)

## CVE-2023-34039
 Aria Operations for Networks contains an Authentication Bypass vulnerability due to a lack of unique cryptographic key generation. A malicious actor with network access to Aria Operations for Networks could bypass SSH authentication to gain access to the Aria Operations for Networks CLI.



- [https://github.com/sinsinology/CVE-2023-34039](https://github.com/sinsinology/CVE-2023-34039) :  ![starts](https://img.shields.io/github/stars/sinsinology/CVE-2023-34039.svg) ![forks](https://img.shields.io/github/forks/sinsinology/CVE-2023-34039.svg)

- [https://github.com/Cyb3rEnthusiast/CVE-2023-34039](https://github.com/Cyb3rEnthusiast/CVE-2023-34039) :  ![starts](https://img.shields.io/github/stars/Cyb3rEnthusiast/CVE-2023-34039.svg) ![forks](https://img.shields.io/github/forks/Cyb3rEnthusiast/CVE-2023-34039.svg)

- [https://github.com/syedhafiz1234/CVE-2023-34039](https://github.com/syedhafiz1234/CVE-2023-34039) :  ![starts](https://img.shields.io/github/stars/syedhafiz1234/CVE-2023-34039.svg) ![forks](https://img.shields.io/github/forks/syedhafiz1234/CVE-2023-34039.svg)

- [https://github.com/ayb-blc/metasploit-cve2023-34039-disclosure](https://github.com/ayb-blc/metasploit-cve2023-34039-disclosure) :  ![starts](https://img.shields.io/github/stars/ayb-blc/metasploit-cve2023-34039-disclosure.svg) ![forks](https://img.shields.io/github/forks/ayb-blc/metasploit-cve2023-34039-disclosure.svg)

- [https://github.com/CharonDefalt/CVE-2023-34039](https://github.com/CharonDefalt/CVE-2023-34039) :  ![starts](https://img.shields.io/github/stars/CharonDefalt/CVE-2023-34039.svg) ![forks](https://img.shields.io/github/forks/CharonDefalt/CVE-2023-34039.svg)

- [https://github.com/adminxb/CVE-2023-34039](https://github.com/adminxb/CVE-2023-34039) :  ![starts](https://img.shields.io/github/stars/adminxb/CVE-2023-34039.svg) ![forks](https://img.shields.io/github/forks/adminxb/CVE-2023-34039.svg)

## CVE-2023-34035
 Spring Security versions 5.8 prior to 5.8.5, 6.0 prior to 6.0.5, and 6.1 prior to 6.1.2 could be susceptible to authorization rule misconfiguration if the application uses requestMatchers(String) and multiple servlets, one of them being Spring MVC’s DispatcherServlet. (DispatcherServlet is a Spring MVC component that maps HTTP endpoints to methods on @Controller-annotated classes.)

Specifically, an application is vulnerable when all of the following are true:

  *  Spring MVC is on the classpath
  *  Spring Security is securing more than one servlet in a single application (one of them being Spring MVC’s DispatcherServlet)
  *  The application uses requestMatchers(String) to refer to endpoints that are not Spring MVC endpoints


An application is not vulnerable if any of the following is true:

  *  The application does not have Spring MVC on the classpath
  *  The application secures no servlets other than Spring MVC’s DispatcherServlet
  *  The application uses requestMatchers(String) only for Spring MVC endpoints







- [https://github.com/jzheaux/cve-2023-34035-mitigations](https://github.com/jzheaux/cve-2023-34035-mitigations) :  ![starts](https://img.shields.io/github/stars/jzheaux/cve-2023-34035-mitigations.svg) ![forks](https://img.shields.io/github/forks/jzheaux/cve-2023-34035-mitigations.svg)

- [https://github.com/mouadk/CVE-2023-34035-Poc](https://github.com/mouadk/CVE-2023-34035-Poc) :  ![starts](https://img.shields.io/github/stars/mouadk/CVE-2023-34035-Poc.svg) ![forks](https://img.shields.io/github/forks/mouadk/CVE-2023-34035-Poc.svg)

## CVE-2023-34034
 Using "**" as a pattern in Spring Security configuration 
for WebFlux creates a mismatch in pattern matching between Spring 
Security and Spring WebFlux, and the potential for a security bypass.





- [https://github.com/hotblac/cve-2023-34034](https://github.com/hotblac/cve-2023-34034) :  ![starts](https://img.shields.io/github/stars/hotblac/cve-2023-34034.svg) ![forks](https://img.shields.io/github/forks/hotblac/cve-2023-34034.svg)

## CVE-2023-33977
 Kiwi TCMS is an open source test management system for both manual and automated testing. Kiwi TCMS allows users to upload attachments to test plans, test cases, etc. Earlier versions of Kiwi TCMS had introduced upload validators in order to prevent potentially dangerous files from being uploaded and Content-Security-Policy definition to prevent cross-site-scripting attacks. The upload validation checks were not 100% robust which left the possibility to circumvent them and upload a potentially dangerous file which allows execution of arbitrary JavaScript in the browser. Additionally we've discovered that Nginx's `proxy_pass` directive will strip some headers negating protections built into Kiwi TCMS when served behind a reverse proxy. This issue has been addressed in version 12.4. Users are advised to upgrade. Users unable to upgrade who are serving Kiwi TCMS behind a reverse proxy should make sure that additional header values are still passed to the client browser. If they aren't redefining them inside the proxy configuration.



- [https://github.com/mnqazi/CVE-2023-33977](https://github.com/mnqazi/CVE-2023-33977) :  ![starts](https://img.shields.io/github/stars/mnqazi/CVE-2023-33977.svg) ![forks](https://img.shields.io/github/forks/mnqazi/CVE-2023-33977.svg)

## CVE-2023-33902
 In bluetooth service, there is a missing permission check. This could lead to local information disclosure with no additional execution privileges needed.



- [https://github.com/uthrasri/CVE-2023-33902_single_file](https://github.com/uthrasri/CVE-2023-33902_single_file) :  ![starts](https://img.shields.io/github/stars/uthrasri/CVE-2023-33902_single_file.svg) ![forks](https://img.shields.io/github/forks/uthrasri/CVE-2023-33902_single_file.svg)

## CVE-2023-33831
 A remote command execution (RCE) vulnerability in the /api/runscript endpoint of FUXA 1.1.13 allows attackers to execute arbitrary commands via a crafted POST request.



- [https://github.com/rodolfomarianocy/Unauthenticated-RCE-FUXA-CVE-2023-33831](https://github.com/rodolfomarianocy/Unauthenticated-RCE-FUXA-CVE-2023-33831) :  ![starts](https://img.shields.io/github/stars/rodolfomarianocy/Unauthenticated-RCE-FUXA-CVE-2023-33831.svg) ![forks](https://img.shields.io/github/forks/rodolfomarianocy/Unauthenticated-RCE-FUXA-CVE-2023-33831.svg)

## CVE-2023-33829
 A stored cross-site scripting (XSS) vulnerability in Cloudogu GmbH SCM Manager v1.2 to v1.60 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the Description text field.



- [https://github.com/P4x1s/CVE-2023-33829-POC](https://github.com/P4x1s/CVE-2023-33829-POC) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2023-33829-POC.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2023-33829-POC.svg)

- [https://github.com/n3gox/CVE-2023-33829](https://github.com/n3gox/CVE-2023-33829) :  ![starts](https://img.shields.io/github/stars/n3gox/CVE-2023-33829.svg) ![forks](https://img.shields.io/github/forks/n3gox/CVE-2023-33829.svg)

## CVE-2023-33817
 hoteldruid v3.0.5 was discovered to contain a SQL injection vulnerability.



- [https://github.com/leekenghwa/CVE-2023-33817---SQL-Injection-found-in-HotelDruid-3.0.5](https://github.com/leekenghwa/CVE-2023-33817---SQL-Injection-found-in-HotelDruid-3.0.5) :  ![starts](https://img.shields.io/github/stars/leekenghwa/CVE-2023-33817---SQL-Injection-found-in-HotelDruid-3.0.5.svg) ![forks](https://img.shields.io/github/forks/leekenghwa/CVE-2023-33817---SQL-Injection-found-in-HotelDruid-3.0.5.svg)

## CVE-2023-33802
 A buffer overflow in SumatraPDF Reader v3.4.6 allows attackers to cause a Denial of Service (DoS) via a crafted text file.



- [https://github.com/CDACesec/CVE-2023-33802](https://github.com/CDACesec/CVE-2023-33802) :  ![starts](https://img.shields.io/github/stars/CDACesec/CVE-2023-33802.svg) ![forks](https://img.shields.io/github/forks/CDACesec/CVE-2023-33802.svg)

## CVE-2023-33782
 D-Link DIR-842V2 v1.0.3 was discovered to contain a command injection vulnerability via the iperf3 diagnostics function.



- [https://github.com/s0tr/CVE-2023-33782](https://github.com/s0tr/CVE-2023-33782) :  ![starts](https://img.shields.io/github/stars/s0tr/CVE-2023-33782.svg) ![forks](https://img.shields.io/github/forks/s0tr/CVE-2023-33782.svg)

## CVE-2023-33781
 An issue in D-Link DIR-842V2 v1.0.3 allows attackers to execute arbitrary commands via importing a crafted file.



- [https://github.com/s0tr/CVE-2023-33781](https://github.com/s0tr/CVE-2023-33781) :  ![starts](https://img.shields.io/github/stars/s0tr/CVE-2023-33781.svg) ![forks](https://img.shields.io/github/forks/s0tr/CVE-2023-33781.svg)

## CVE-2023-33768
 Incorrect signature verification of the firmware during the Device Firmware Update process of Belkin Wemo Smart Plug WSP080 v1.2 allows attackers to cause a Denial of Service (DoS) via a crafted firmware file.



- [https://github.com/purseclab/CVE-2023-33768](https://github.com/purseclab/CVE-2023-33768) :  ![starts](https://img.shields.io/github/stars/purseclab/CVE-2023-33768.svg) ![forks](https://img.shields.io/github/forks/purseclab/CVE-2023-33768.svg)

- [https://github.com/Fr0stM0urne/CVE-2023-33768](https://github.com/Fr0stM0urne/CVE-2023-33768) :  ![starts](https://img.shields.io/github/stars/Fr0stM0urne/CVE-2023-33768.svg) ![forks](https://img.shields.io/github/forks/Fr0stM0urne/CVE-2023-33768.svg)

## CVE-2023-33747
 CloudPanel v2.2.2 allows attackers to execute a path traversal.



- [https://github.com/0xWhoami35/CloudPanel-CVE-2023-33747](https://github.com/0xWhoami35/CloudPanel-CVE-2023-33747) :  ![starts](https://img.shields.io/github/stars/0xWhoami35/CloudPanel-CVE-2023-33747.svg) ![forks](https://img.shields.io/github/forks/0xWhoami35/CloudPanel-CVE-2023-33747.svg)

## CVE-2023-33733
 Reportlab up to v3.6.12 allows attackers to execute arbitrary code via supplying a crafted PDF file.



- [https://github.com/c53elyas/CVE-2023-33733](https://github.com/c53elyas/CVE-2023-33733) :  ![starts](https://img.shields.io/github/stars/c53elyas/CVE-2023-33733.svg) ![forks](https://img.shields.io/github/forks/c53elyas/CVE-2023-33733.svg)

- [https://github.com/L41KAA/CVE-2023-33733-Exploit-PoC](https://github.com/L41KAA/CVE-2023-33733-Exploit-PoC) :  ![starts](https://img.shields.io/github/stars/L41KAA/CVE-2023-33733-Exploit-PoC.svg) ![forks](https://img.shields.io/github/forks/L41KAA/CVE-2023-33733-Exploit-PoC.svg)

- [https://github.com/buiduchoang24/CVE-2023-33733](https://github.com/buiduchoang24/CVE-2023-33733) :  ![starts](https://img.shields.io/github/stars/buiduchoang24/CVE-2023-33733.svg) ![forks](https://img.shields.io/github/forks/buiduchoang24/CVE-2023-33733.svg)

- [https://github.com/onion2203/Lab_Reportlab](https://github.com/onion2203/Lab_Reportlab) :  ![starts](https://img.shields.io/github/stars/onion2203/Lab_Reportlab.svg) ![forks](https://img.shields.io/github/forks/onion2203/Lab_Reportlab.svg)

- [https://github.com/hoangbui24/CVE-2023-33733](https://github.com/hoangbui24/CVE-2023-33733) :  ![starts](https://img.shields.io/github/stars/hoangbui24/CVE-2023-33733.svg) ![forks](https://img.shields.io/github/forks/hoangbui24/CVE-2023-33733.svg)

## CVE-2023-33732
 Cross Site Scripting (XSS) in the New Policy form in Microworld Technologies eScan management console 14.0.1400.2281 allows a remote attacker to inject arbitrary code via the vulnerable parameters type, txtPolicyType, and Deletefileval.



- [https://github.com/sahiloj/CVE-2023-33732](https://github.com/sahiloj/CVE-2023-33732) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-33732.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-33732.svg)

## CVE-2023-33731
 Reflected Cross Site Scripting (XSS) in the view dashboard detail feature in Microworld Technologies eScan management console 14.0.1400.2281 allows remote attacker to inject arbitrary code via the URL directly.



- [https://github.com/sahiloj/CVE-2023-33731](https://github.com/sahiloj/CVE-2023-33731) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-33731.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-33731.svg)

## CVE-2023-33730
 Privilege Escalation in the "GetUserCurrentPwd" function in Microworld Technologies eScan Management Console 14.0.1400.2281 allows any remote attacker to retrieve password of any admin or normal user in plain text format.



- [https://github.com/sahiloj/CVE-2023-33730](https://github.com/sahiloj/CVE-2023-33730) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-33730.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-33730.svg)

## CVE-2023-33677
 Sourcecodester Lost and Found Information System's Version 1.0 is vulnerable to unauthenticated SQL Injection at "?page=items/view&id=*".



- [https://github.com/ASR511-OO7/CVE-2023-33677](https://github.com/ASR511-OO7/CVE-2023-33677) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-33677.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-33677.svg)

## CVE-2023-33676
 Sourcecodester Lost and Found Information System's Version 1.0 is vulnerable to unauthenticated SQL Injection at "?page=items/view&id=*" which can be escalated to the remote command execution.



- [https://github.com/ASR511-OO7/CVE-2023-33676](https://github.com/ASR511-OO7/CVE-2023-33676) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-33676.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-33676.svg)

## CVE-2023-33675
 Tenda AC8V4.0-V16.03.34.06 was discovered to contain a stack overflow via the time parameter in the get_parentControl_list_Info function.



- [https://github.com/retr0reg/tenda-ac8v4-rop](https://github.com/retr0reg/tenda-ac8v4-rop) :  ![starts](https://img.shields.io/github/stars/retr0reg/tenda-ac8v4-rop.svg) ![forks](https://img.shields.io/github/forks/retr0reg/tenda-ac8v4-rop.svg)

## CVE-2023-33669
 Tenda AC8V4.0-V16.03.34.06 was discovered to contain a stack overflow via the timeZone parameter in the sub_44db3c function.



- [https://github.com/retr0reg/tenda-ac8v4-rop](https://github.com/retr0reg/tenda-ac8v4-rop) :  ![starts](https://img.shields.io/github/stars/retr0reg/tenda-ac8v4-rop.svg) ![forks](https://img.shields.io/github/forks/retr0reg/tenda-ac8v4-rop.svg)

## CVE-2023-33668
 DigiExam up to v14.0.2 lacks integrity checks for native modules, allowing attackers to access PII and takeover accounts on shared computers.



- [https://github.com/lodi-g/CVE-2023-33668](https://github.com/lodi-g/CVE-2023-33668) :  ![starts](https://img.shields.io/github/stars/lodi-g/CVE-2023-33668.svg) ![forks](https://img.shields.io/github/forks/lodi-g/CVE-2023-33668.svg)

## CVE-2023-33617
 An OS Command Injection vulnerability in Parks Fiberlink 210 firmware version V2.1.14_X000 was found via the /boaform/admin/formPing target_addr parameter.



- [https://github.com/Chocapikk/CVE-2023-33617](https://github.com/Chocapikk/CVE-2023-33617) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-33617.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-33617.svg)

- [https://github.com/tucommenceapousser/CVE-2023-33617](https://github.com/tucommenceapousser/CVE-2023-33617) :  ![starts](https://img.shields.io/github/stars/tucommenceapousser/CVE-2023-33617.svg) ![forks](https://img.shields.io/github/forks/tucommenceapousser/CVE-2023-33617.svg)

## CVE-2023-33592
 Lost and Found Information System v1.0 was discovered to contain a SQL injection vulnerability via the component /php-lfis/admin/?page=system_info/contact_information.



- [https://github.com/ChineseOldboy/CVE-2023-33592](https://github.com/ChineseOldboy/CVE-2023-33592) :  ![starts](https://img.shields.io/github/stars/ChineseOldboy/CVE-2023-33592.svg) ![forks](https://img.shields.io/github/forks/ChineseOldboy/CVE-2023-33592.svg)

## CVE-2023-33570
 Bagisto v1.5.1 is vulnerable to Server-Side Template Injection (SSTI).



- [https://github.com/Trangdz/bagisto_ssti_cve_2023_33570](https://github.com/Trangdz/bagisto_ssti_cve_2023_33570) :  ![starts](https://img.shields.io/github/stars/Trangdz/bagisto_ssti_cve_2023_33570.svg) ![forks](https://img.shields.io/github/forks/Trangdz/bagisto_ssti_cve_2023_33570.svg)

## CVE-2023-33517
 carRental 1.0 is vulnerable to Incorrect Access Control (Arbitrary File Read on the Back-end System).



- [https://github.com/wushigudan/CVE-2023-33517](https://github.com/wushigudan/CVE-2023-33517) :  ![starts](https://img.shields.io/github/stars/wushigudan/CVE-2023-33517.svg) ![forks](https://img.shields.io/github/forks/wushigudan/CVE-2023-33517.svg)

## CVE-2023-33477
 In Harmonic NSG 9000-6G devices, an authenticated remote user can obtain source code by directly requesting a special path.



- [https://github.com/Skr11lex/CVE-2023-33477](https://github.com/Skr11lex/CVE-2023-33477) :  ![starts](https://img.shields.io/github/stars/Skr11lex/CVE-2023-33477.svg) ![forks](https://img.shields.io/github/forks/Skr11lex/CVE-2023-33477.svg)

## CVE-2023-33476
 ReadyMedia (MiniDLNA) versions from 1.1.15 up to 1.3.2 is vulnerable to Buffer Overflow. The vulnerability is caused by incorrect validation logic when handling HTTP requests using chunked transport encoding. This results in other code later using attacker-controlled chunk values that exceed the length of the allocated buffer, resulting in out-of-bounds read/write.



- [https://github.com/mellow-hype/cve-2023-33476](https://github.com/mellow-hype/cve-2023-33476) :  ![starts](https://img.shields.io/github/stars/mellow-hype/cve-2023-33476.svg) ![forks](https://img.shields.io/github/forks/mellow-hype/cve-2023-33476.svg)

## CVE-2023-33410
 Minical 1.0.0 and earlier contains a CSV injection vulnerability which allows an attacker to execute remote code. The vulnerability exists due to insufficient input validation on the Customer Name field in the Accounting module that is used to construct a CSV file.



- [https://github.com/Thirukrishnan/CVE-2023-33410](https://github.com/Thirukrishnan/CVE-2023-33410) :  ![starts](https://img.shields.io/github/stars/Thirukrishnan/CVE-2023-33410.svg) ![forks](https://img.shields.io/github/forks/Thirukrishnan/CVE-2023-33410.svg)

## CVE-2023-33409
 Minical 1.0.0 is vulnerable to Cross Site Request Forgery (CSRF) via minical/public/application/controllers/settings/company.php.



- [https://github.com/Thirukrishnan/CVE-2023-33409](https://github.com/Thirukrishnan/CVE-2023-33409) :  ![starts](https://img.shields.io/github/stars/Thirukrishnan/CVE-2023-33409.svg) ![forks](https://img.shields.io/github/forks/Thirukrishnan/CVE-2023-33409.svg)

## CVE-2023-33408
 Minical 1.0.0 is vulnerable to Cross Site Scripting (XSS). The vulnerability exists due to insufficient input validation in the application's user input handling in the security_helper.php file.



- [https://github.com/Thirukrishnan/CVE-2023-33408](https://github.com/Thirukrishnan/CVE-2023-33408) :  ![starts](https://img.shields.io/github/stars/Thirukrishnan/CVE-2023-33408.svg) ![forks](https://img.shields.io/github/forks/Thirukrishnan/CVE-2023-33408.svg)

## CVE-2023-33405
 Blogengine.net 3.3.8.0 and earlier is vulnerable to Open Redirect.



- [https://github.com/hacip/CVE-2023-33405](https://github.com/hacip/CVE-2023-33405) :  ![starts](https://img.shields.io/github/stars/hacip/CVE-2023-33405.svg) ![forks](https://img.shields.io/github/forks/hacip/CVE-2023-33405.svg)

## CVE-2023-33404
 An Unrestricted Upload vulnerability, due to insufficient validation on UploadControlled.cs file, in BlogEngine.Net version 3.3.8.0 and earlier allows remote attackers to execute remote code.



- [https://github.com/hacip/CVE-2023-33404](https://github.com/hacip/CVE-2023-33404) :  ![starts](https://img.shields.io/github/stars/hacip/CVE-2023-33404.svg) ![forks](https://img.shields.io/github/forks/hacip/CVE-2023-33404.svg)

## CVE-2023-33381
 A command injection vulnerability was found in the ping functionality of the MitraStar GPT-2741GNAC router (firmware version AR_g5.8_110WVN0b7_2). The vulnerability allows an authenticated user to execute arbitrary OS commands by sending specially crafted input to the router via the ping function.



- [https://github.com/duality084/CVE-2023-33381-MitraStar-GPT-2741GNAC](https://github.com/duality084/CVE-2023-33381-MitraStar-GPT-2741GNAC) :  ![starts](https://img.shields.io/github/stars/duality084/CVE-2023-33381-MitraStar-GPT-2741GNAC.svg) ![forks](https://img.shields.io/github/forks/duality084/CVE-2023-33381-MitraStar-GPT-2741GNAC.svg)

## CVE-2023-33253
 LabCollector 6.0 though 6.15 allows remote code execution. An authenticated remote low-privileged user can upload an executable PHP file and execute system commands. The vulnerability is in the message function, and is due to insufficient validation of the file (such as shell.jpg.php.shell) being sent.



- [https://github.com/Toxich4/CVE-2023-33253](https://github.com/Toxich4/CVE-2023-33253) :  ![starts](https://img.shields.io/github/stars/Toxich4/CVE-2023-33253.svg) ![forks](https://img.shields.io/github/forks/Toxich4/CVE-2023-33253.svg)

## CVE-2023-33246
 For RocketMQ versions 5.1.0 and below, under certain conditions, there is a risk of remote command execution. 

Several components of RocketMQ, including NameServer, Broker, and Controller, are leaked on the extranet and lack permission verification, an attacker can exploit this vulnerability by using the update configuration function to execute commands as the system users that RocketMQ is running as. Additionally, an attacker can achieve the same effect by forging the RocketMQ protocol content. 

To prevent these attacks, users are recommended to upgrade to version 5.1.1 or above for using RocketMQ 5.x or 4.9.6 or above for using RocketMQ 4.x .



- [https://github.com/SuperZero/CVE-2023-33246](https://github.com/SuperZero/CVE-2023-33246) :  ![starts](https://img.shields.io/github/stars/SuperZero/CVE-2023-33246.svg) ![forks](https://img.shields.io/github/forks/SuperZero/CVE-2023-33246.svg)

- [https://github.com/Malayke/CVE-2023-33246_RocketMQ_RCE_EXPLOIT](https://github.com/Malayke/CVE-2023-33246_RocketMQ_RCE_EXPLOIT) :  ![starts](https://img.shields.io/github/stars/Malayke/CVE-2023-33246_RocketMQ_RCE_EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/Malayke/CVE-2023-33246_RocketMQ_RCE_EXPLOIT.svg)

- [https://github.com/Le1a/CVE-2023-33246](https://github.com/Le1a/CVE-2023-33246) :  ![starts](https://img.shields.io/github/stars/Le1a/CVE-2023-33246.svg) ![forks](https://img.shields.io/github/forks/Le1a/CVE-2023-33246.svg)

- [https://github.com/I5N0rth/CVE-2023-33246](https://github.com/I5N0rth/CVE-2023-33246) :  ![starts](https://img.shields.io/github/stars/I5N0rth/CVE-2023-33246.svg) ![forks](https://img.shields.io/github/forks/I5N0rth/CVE-2023-33246.svg)

- [https://github.com/vulncheck-oss/fetch-broker-conf](https://github.com/vulncheck-oss/fetch-broker-conf) :  ![starts](https://img.shields.io/github/stars/vulncheck-oss/fetch-broker-conf.svg) ![forks](https://img.shields.io/github/forks/vulncheck-oss/fetch-broker-conf.svg)

- [https://github.com/4mazing/CVE-2023-33246-Copy](https://github.com/4mazing/CVE-2023-33246-Copy) :  ![starts](https://img.shields.io/github/stars/4mazing/CVE-2023-33246-Copy.svg) ![forks](https://img.shields.io/github/forks/4mazing/CVE-2023-33246-Copy.svg)

- [https://github.com/P4x1s/CVE-2023-33246](https://github.com/P4x1s/CVE-2023-33246) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2023-33246.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2023-33246.svg)

- [https://github.com/0xKayala/CVE-2023-33246](https://github.com/0xKayala/CVE-2023-33246) :  ![starts](https://img.shields.io/github/stars/0xKayala/CVE-2023-33246.svg) ![forks](https://img.shields.io/github/forks/0xKayala/CVE-2023-33246.svg)

- [https://github.com/d0rb/CVE-2023-33246](https://github.com/d0rb/CVE-2023-33246) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-33246.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-33246.svg)

- [https://github.com/PavilionQ/CVE-2023-33246-mitigation](https://github.com/PavilionQ/CVE-2023-33246-mitigation) :  ![starts](https://img.shields.io/github/stars/PavilionQ/CVE-2023-33246-mitigation.svg) ![forks](https://img.shields.io/github/forks/PavilionQ/CVE-2023-33246-mitigation.svg)

- [https://github.com/MkJos/CVE-2023-33246_RocketMQ_RCE_EXP](https://github.com/MkJos/CVE-2023-33246_RocketMQ_RCE_EXP) :  ![starts](https://img.shields.io/github/stars/MkJos/CVE-2023-33246_RocketMQ_RCE_EXP.svg) ![forks](https://img.shields.io/github/forks/MkJos/CVE-2023-33246_RocketMQ_RCE_EXP.svg)

- [https://github.com/Sumitpathania03/Apache-RocketMQ-CVE-2023-33246-](https://github.com/Sumitpathania03/Apache-RocketMQ-CVE-2023-33246-) :  ![starts](https://img.shields.io/github/stars/Sumitpathania03/Apache-RocketMQ-CVE-2023-33246-.svg) ![forks](https://img.shields.io/github/forks/Sumitpathania03/Apache-RocketMQ-CVE-2023-33246-.svg)

## CVE-2023-33243
 RedTeam Pentesting discovered that the web interface of STARFACE as well as its REST API allows authentication using the SHA512 hash of the password instead of the cleartext password. While storing password hashes instead of cleartext passwords in an application's database generally has become best practice to protect users' passwords in case of a database compromise, this is rendered ineffective when allowing to authenticate using the password hash.



- [https://github.com/RedTeamPentesting/CVE-2023-33243](https://github.com/RedTeamPentesting/CVE-2023-33243) :  ![starts](https://img.shields.io/github/stars/RedTeamPentesting/CVE-2023-33243.svg) ![forks](https://img.shields.io/github/forks/RedTeamPentesting/CVE-2023-33243.svg)

## CVE-2023-33242
 Crypto wallets implementing the Lindell17 TSS protocol might allow an attacker to extract the full ECDSA private key by exfiltrating a single bit in every signature attempt (256 in total) because of not adhering to the paper's security proof's assumption regarding handling aborts after a failed signature.



- [https://github.com/d0rb/CVE-2023-33242](https://github.com/d0rb/CVE-2023-33242) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-33242.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-33242.svg)

## CVE-2023-33105
 Transient DOS in WLAN Host and Firmware when large number of open authentication frames are sent with an invalid transaction sequence number.



- [https://github.com/D3adP3nguin/CVE-2023-33105-Transient-DOS-in-WLAN-Host-and-Firmware](https://github.com/D3adP3nguin/CVE-2023-33105-Transient-DOS-in-WLAN-Host-and-Firmware) :  ![starts](https://img.shields.io/github/stars/D3adP3nguin/CVE-2023-33105-Transient-DOS-in-WLAN-Host-and-Firmware.svg) ![forks](https://img.shields.io/github/forks/D3adP3nguin/CVE-2023-33105-Transient-DOS-in-WLAN-Host-and-Firmware.svg)

## CVE-2023-32961
 Unauth. Reflected Cross-Site Scripting (XSS) vulnerability in Katie Seaborn Zotpress plugin = 7.3.3 versions.



- [https://github.com/LOURC0D3/CVE-2023-32961](https://github.com/LOURC0D3/CVE-2023-32961) :  ![starts](https://img.shields.io/github/stars/LOURC0D3/CVE-2023-32961.svg) ![forks](https://img.shields.io/github/forks/LOURC0D3/CVE-2023-32961.svg)

## CVE-2023-32784
 In KeePass 2.x before 2.54, it is possible to recover the cleartext master password from a memory dump, even when a workspace is locked or no longer running. The memory dump can be a KeePass process dump, swap file (pagefile.sys), hibernation file (hiberfil.sys), or RAM dump of the entire system. The first character cannot be recovered. In 2.54, there is different API usage and/or random string insertion for mitigation.



- [https://github.com/vdohney/keepass-password-dumper](https://github.com/vdohney/keepass-password-dumper) :  ![starts](https://img.shields.io/github/stars/vdohney/keepass-password-dumper.svg) ![forks](https://img.shields.io/github/forks/vdohney/keepass-password-dumper.svg)

- [https://github.com/z-jxy/keepass_dump](https://github.com/z-jxy/keepass_dump) :  ![starts](https://img.shields.io/github/stars/z-jxy/keepass_dump.svg) ![forks](https://img.shields.io/github/forks/z-jxy/keepass_dump.svg)

- [https://github.com/und3sc0n0c1d0/BruteForce-to-KeePass](https://github.com/und3sc0n0c1d0/BruteForce-to-KeePass) :  ![starts](https://img.shields.io/github/stars/und3sc0n0c1d0/BruteForce-to-KeePass.svg) ![forks](https://img.shields.io/github/forks/und3sc0n0c1d0/BruteForce-to-KeePass.svg)

- [https://github.com/mister-turtle/cve-2023-32784](https://github.com/mister-turtle/cve-2023-32784) :  ![starts](https://img.shields.io/github/stars/mister-turtle/cve-2023-32784.svg) ![forks](https://img.shields.io/github/forks/mister-turtle/cve-2023-32784.svg)

- [https://github.com/CTM1/CVE-2023-32784-keepass-linux](https://github.com/CTM1/CVE-2023-32784-keepass-linux) :  ![starts](https://img.shields.io/github/stars/CTM1/CVE-2023-32784-keepass-linux.svg) ![forks](https://img.shields.io/github/forks/CTM1/CVE-2023-32784-keepass-linux.svg)

- [https://github.com/1ocho3/NCL_V](https://github.com/1ocho3/NCL_V) :  ![starts](https://img.shields.io/github/stars/1ocho3/NCL_V.svg) ![forks](https://img.shields.io/github/forks/1ocho3/NCL_V.svg)

- [https://github.com/LeDocteurDesBits/cve-2023-32784](https://github.com/LeDocteurDesBits/cve-2023-32784) :  ![starts](https://img.shields.io/github/stars/LeDocteurDesBits/cve-2023-32784.svg) ![forks](https://img.shields.io/github/forks/LeDocteurDesBits/cve-2023-32784.svg)

- [https://github.com/dawnl3ss/CVE-2023-32784](https://github.com/dawnl3ss/CVE-2023-32784) :  ![starts](https://img.shields.io/github/stars/dawnl3ss/CVE-2023-32784.svg) ![forks](https://img.shields.io/github/forks/dawnl3ss/CVE-2023-32784.svg)

- [https://github.com/le01s/poc-CVE-2023-32784](https://github.com/le01s/poc-CVE-2023-32784) :  ![starts](https://img.shields.io/github/stars/le01s/poc-CVE-2023-32784.svg) ![forks](https://img.shields.io/github/forks/le01s/poc-CVE-2023-32784.svg)

- [https://github.com/Cmadhushanka/CVE-2023-32784-Exploitation](https://github.com/Cmadhushanka/CVE-2023-32784-Exploitation) :  ![starts](https://img.shields.io/github/stars/Cmadhushanka/CVE-2023-32784-Exploitation.svg) ![forks](https://img.shields.io/github/forks/Cmadhushanka/CVE-2023-32784-Exploitation.svg)

- [https://github.com/dev0558/CVE-2023-32784-EXPLOIT-REPORT](https://github.com/dev0558/CVE-2023-32784-EXPLOIT-REPORT) :  ![starts](https://img.shields.io/github/stars/dev0558/CVE-2023-32784-EXPLOIT-REPORT.svg) ![forks](https://img.shields.io/github/forks/dev0558/CVE-2023-32784-EXPLOIT-REPORT.svg)

- [https://github.com/Hirusha-N/CVE-2021-34527-CVE-2023-38831-and-CVE-2023-32784](https://github.com/Hirusha-N/CVE-2021-34527-CVE-2023-38831-and-CVE-2023-32784) :  ![starts](https://img.shields.io/github/stars/Hirusha-N/CVE-2021-34527-CVE-2023-38831-and-CVE-2023-32784.svg) ![forks](https://img.shields.io/github/forks/Hirusha-N/CVE-2021-34527-CVE-2023-38831-and-CVE-2023-32784.svg)

- [https://github.com/hau-zy/KeePass-dump-py](https://github.com/hau-zy/KeePass-dump-py) :  ![starts](https://img.shields.io/github/stars/hau-zy/KeePass-dump-py.svg) ![forks](https://img.shields.io/github/forks/hau-zy/KeePass-dump-py.svg)

## CVE-2023-32749
 Pydio Cells allows users by default to create so-called external users in order to share files with them. By modifying the HTTP request sent when creating such an external user, it is possible to assign the new user arbitrary roles. By assigning all roles to a newly created user, access to all cells and non-personal workspaces is granted.



- [https://github.com/xcr-19/CVE-2023-32749](https://github.com/xcr-19/CVE-2023-32749) :  ![starts](https://img.shields.io/github/stars/xcr-19/CVE-2023-32749.svg) ![forks](https://img.shields.io/github/forks/xcr-19/CVE-2023-32749.svg)

## CVE-2023-32707
 In versions of Splunk Enterprise below 9.0.5, 8.2.11, and 8.1.14, and Splunk Cloud Platform below version 9.0.2303.100, a low-privileged user who holds a role that has the ‘edit_user’ capability assigned to it can escalate their privileges to that of the admin user by providing specially crafted web requests.



- [https://github.com/9xN/CVE-2023-32707](https://github.com/9xN/CVE-2023-32707) :  ![starts](https://img.shields.io/github/stars/9xN/CVE-2023-32707.svg) ![forks](https://img.shields.io/github/forks/9xN/CVE-2023-32707.svg)

## CVE-2023-32681
 Requests is a HTTP library. Since Requests 2.3.0, Requests has been leaking Proxy-Authorization headers to destination servers when redirected to an HTTPS endpoint. This is a product of how we use `rebuild_proxies` to reattach the `Proxy-Authorization` header to requests. For HTTP connections sent through the tunnel, the proxy will identify the header in the request itself and remove it prior to forwarding to the destination server. However when sent over HTTPS, the `Proxy-Authorization` header must be sent in the CONNECT request as the proxy has no visibility into the tunneled request. This results in Requests forwarding proxy credentials to the destination server unintentionally, allowing a malicious actor to potentially exfiltrate sensitive information. This issue has been patched in version 2.31.0.



- [https://github.com/hardikmodha/POC-CVE-2023-32681](https://github.com/hardikmodha/POC-CVE-2023-32681) :  ![starts](https://img.shields.io/github/stars/hardikmodha/POC-CVE-2023-32681.svg) ![forks](https://img.shields.io/github/forks/hardikmodha/POC-CVE-2023-32681.svg)

## CVE-2023-32629
 Local privilege escalation vulnerability in Ubuntu Kernels overlayfs ovl_copy_up_meta_inode_data skip permission checks when calling ovl_do_setxattr on Ubuntu kernels



- [https://github.com/g1vi/CVE-2023-2640-CVE-2023-32629](https://github.com/g1vi/CVE-2023-2640-CVE-2023-32629) :  ![starts](https://img.shields.io/github/stars/g1vi/CVE-2023-2640-CVE-2023-32629.svg) ![forks](https://img.shields.io/github/forks/g1vi/CVE-2023-2640-CVE-2023-32629.svg)

- [https://github.com/ThrynSec/CVE-2023-32629-CVE-2023-2640---POC-Escalation](https://github.com/ThrynSec/CVE-2023-32629-CVE-2023-2640---POC-Escalation) :  ![starts](https://img.shields.io/github/stars/ThrynSec/CVE-2023-32629-CVE-2023-2640---POC-Escalation.svg) ![forks](https://img.shields.io/github/forks/ThrynSec/CVE-2023-32629-CVE-2023-2640---POC-Escalation.svg)

- [https://github.com/luanoliveira350/GameOverlayFS](https://github.com/luanoliveira350/GameOverlayFS) :  ![starts](https://img.shields.io/github/stars/luanoliveira350/GameOverlayFS.svg) ![forks](https://img.shields.io/github/forks/luanoliveira350/GameOverlayFS.svg)

- [https://github.com/OllaPapito/gameoverlay](https://github.com/OllaPapito/gameoverlay) :  ![starts](https://img.shields.io/github/stars/OllaPapito/gameoverlay.svg) ![forks](https://img.shields.io/github/forks/OllaPapito/gameoverlay.svg)

- [https://github.com/kaotickj/Check-for-CVE-2023-32629-GameOver-lay](https://github.com/kaotickj/Check-for-CVE-2023-32629-GameOver-lay) :  ![starts](https://img.shields.io/github/stars/kaotickj/Check-for-CVE-2023-32629-GameOver-lay.svg) ![forks](https://img.shields.io/github/forks/kaotickj/Check-for-CVE-2023-32629-GameOver-lay.svg)

- [https://github.com/k4but0/Ubuntu-LPE](https://github.com/k4but0/Ubuntu-LPE) :  ![starts](https://img.shields.io/github/stars/k4but0/Ubuntu-LPE.svg) ![forks](https://img.shields.io/github/forks/k4but0/Ubuntu-LPE.svg)

- [https://github.com/musorblyat/CVE-2023-2640-CVE-2023-32629](https://github.com/musorblyat/CVE-2023-2640-CVE-2023-32629) :  ![starts](https://img.shields.io/github/stars/musorblyat/CVE-2023-2640-CVE-2023-32629.svg) ![forks](https://img.shields.io/github/forks/musorblyat/CVE-2023-2640-CVE-2023-32629.svg)

- [https://github.com/johnlettman/juju-scripts](https://github.com/johnlettman/juju-scripts) :  ![starts](https://img.shields.io/github/stars/johnlettman/juju-scripts.svg) ![forks](https://img.shields.io/github/forks/johnlettman/juju-scripts.svg)

- [https://github.com/Nkipohcs/CVE-2023-2640-CVE-2023-32629](https://github.com/Nkipohcs/CVE-2023-2640-CVE-2023-32629) :  ![starts](https://img.shields.io/github/stars/Nkipohcs/CVE-2023-2640-CVE-2023-32629.svg) ![forks](https://img.shields.io/github/forks/Nkipohcs/CVE-2023-2640-CVE-2023-32629.svg)

- [https://github.com/xS9NTX/CVE-2023-32629-CVE-2023-2640-Ubuntu-Privilege-Escalation-POC](https://github.com/xS9NTX/CVE-2023-32629-CVE-2023-2640-Ubuntu-Privilege-Escalation-POC) :  ![starts](https://img.shields.io/github/stars/xS9NTX/CVE-2023-32629-CVE-2023-2640-Ubuntu-Privilege-Escalation-POC.svg) ![forks](https://img.shields.io/github/forks/xS9NTX/CVE-2023-32629-CVE-2023-2640-Ubuntu-Privilege-Escalation-POC.svg)

- [https://github.com/filippo-zullo98/phpMyAdmin-RCE-Exploit-Lab](https://github.com/filippo-zullo98/phpMyAdmin-RCE-Exploit-Lab) :  ![starts](https://img.shields.io/github/stars/filippo-zullo98/phpMyAdmin-RCE-Exploit-Lab.svg) ![forks](https://img.shields.io/github/forks/filippo-zullo98/phpMyAdmin-RCE-Exploit-Lab.svg)

## CVE-2023-32590
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Daniel Söderström / Sidney van de Stouwe Subscribe to Category.This issue affects Subscribe to Category: from n/a through 2.7.4.





- [https://github.com/RandomRobbieBF/CVE-2023-32590](https://github.com/RandomRobbieBF/CVE-2023-32590) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-32590.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-32590.svg)

## CVE-2023-32571
 Dynamic Linq 1.0.7.10 through 1.2.25 before 1.3.0 allows attackers to execute arbitrary code and commands when untrusted input to methods including Where, Select, OrderBy is parsed.



- [https://github.com/Tris0n/CVE-2023-32571-POC](https://github.com/Tris0n/CVE-2023-32571-POC) :  ![starts](https://img.shields.io/github/stars/Tris0n/CVE-2023-32571-POC.svg) ![forks](https://img.shields.io/github/forks/Tris0n/CVE-2023-32571-POC.svg)

- [https://github.com/vert16x/CVE-2023-32571-POC](https://github.com/vert16x/CVE-2023-32571-POC) :  ![starts](https://img.shields.io/github/stars/vert16x/CVE-2023-32571-POC.svg) ![forks](https://img.shields.io/github/forks/vert16x/CVE-2023-32571-POC.svg)

## CVE-2023-32560
 An attacker can send a specially crafted message to the Wavelink Avalanche Manager, which could result in service disruption or arbitrary code execution.

Thanks to a Researcher at Tenable for finding and reporting.

Fixed in version 6.4.1.



- [https://github.com/x0rb3l/CVE-2023-32560](https://github.com/x0rb3l/CVE-2023-32560) :  ![starts](https://img.shields.io/github/stars/x0rb3l/CVE-2023-32560.svg) ![forks](https://img.shields.io/github/forks/x0rb3l/CVE-2023-32560.svg)

## CVE-2023-32434
 An integer overflow was addressed with improved input validation. This issue is fixed in watchOS 9.5.2, macOS Big Sur 11.7.8, iOS 15.7.7 and iPadOS 15.7.7, macOS Monterey 12.6.7, watchOS 8.8.1, iOS 16.5.1 and iPadOS 16.5.1, macOS Ventura 13.4.1. An app may be able to execute arbitrary code with kernel privileges. Apple is aware of a report that this issue may have been actively exploited against versions of iOS released before iOS 15.7.



- [https://github.com/rkrakesh524/oob_entry](https://github.com/rkrakesh524/oob_entry) :  ![starts](https://img.shields.io/github/stars/rkrakesh524/oob_entry.svg) ![forks](https://img.shields.io/github/forks/rkrakesh524/oob_entry.svg)

## CVE-2023-32428
 This issue was addressed with improved file handling. This issue is fixed in macOS Ventura 13.4, tvOS 16.5, iOS 16.5 and iPadOS 16.5, watchOS 9.5. An app may be able to gain root privileges.



- [https://github.com/gergelykalman/CVE-2023-32428-a-macOS-LPE-via-MallocStackLogging](https://github.com/gergelykalman/CVE-2023-32428-a-macOS-LPE-via-MallocStackLogging) :  ![starts](https://img.shields.io/github/stars/gergelykalman/CVE-2023-32428-a-macOS-LPE-via-MallocStackLogging.svg) ![forks](https://img.shields.io/github/forks/gergelykalman/CVE-2023-32428-a-macOS-LPE-via-MallocStackLogging.svg)

## CVE-2023-32422
 This issue was addressed by adding additional SQLite logging restrictions. This issue is fixed in iOS 16.5 and iPadOS 16.5, tvOS 16.5, macOS Ventura 13.4. An app may be able to bypass Privacy preferences.



- [https://github.com/gergelykalman/CVE-2023-32422-a-macOS-TCC-bypass-in-sqlite](https://github.com/gergelykalman/CVE-2023-32422-a-macOS-TCC-bypass-in-sqlite) :  ![starts](https://img.shields.io/github/stars/gergelykalman/CVE-2023-32422-a-macOS-TCC-bypass-in-sqlite.svg) ![forks](https://img.shields.io/github/forks/gergelykalman/CVE-2023-32422-a-macOS-TCC-bypass-in-sqlite.svg)

## CVE-2023-32413
 A race condition was addressed with improved state handling. This issue is fixed in watchOS 9.5, tvOS 16.5, macOS Ventura 13.4, iOS 15.7.6 and iPadOS 15.7.6, macOS Big Sur 11.7.7, macOS Monterey 12.6.6, iOS 16.5 and iPadOS 16.5. An app may be able to gain root privileges.



- [https://github.com/synacktiv/CVE-2023-32413](https://github.com/synacktiv/CVE-2023-32413) :  ![starts](https://img.shields.io/github/stars/synacktiv/CVE-2023-32413.svg) ![forks](https://img.shields.io/github/forks/synacktiv/CVE-2023-32413.svg)

## CVE-2023-32407
 A logic issue was addressed with improved state management. This issue is fixed in watchOS 9.5, tvOS 16.5, macOS Ventura 13.4, iOS 15.7.6 and iPadOS 15.7.6, macOS Big Sur 11.7.7, macOS Monterey 12.6.6, iOS 16.5 and iPadOS 16.5. An app may be able to bypass Privacy preferences.



- [https://github.com/gergelykalman/CVE-2023-32407-a-macOS-TCC-bypass-in-Metal](https://github.com/gergelykalman/CVE-2023-32407-a-macOS-TCC-bypass-in-Metal) :  ![starts](https://img.shields.io/github/stars/gergelykalman/CVE-2023-32407-a-macOS-TCC-bypass-in-Metal.svg) ![forks](https://img.shields.io/github/forks/gergelykalman/CVE-2023-32407-a-macOS-TCC-bypass-in-Metal.svg)

## CVE-2023-32364
 A logic issue was addressed with improved restrictions. This issue is fixed in macOS Ventura 13.5. A sandboxed process may be able to circumvent sandbox restrictions.



- [https://github.com/gergelykalman/CVE-2023-32364-macos-app-sandbox-escape](https://github.com/gergelykalman/CVE-2023-32364-macos-app-sandbox-escape) :  ![starts](https://img.shields.io/github/stars/gergelykalman/CVE-2023-32364-macos-app-sandbox-escape.svg) ![forks](https://img.shields.io/github/forks/gergelykalman/CVE-2023-32364-macos-app-sandbox-escape.svg)

## CVE-2023-32353
 A logic issue was addressed with improved checks. This issue is fixed in iTunes 12.12.9 for Windows. An app may be able to elevate privileges.



- [https://github.com/86x/CVE-2023-32353-PoC](https://github.com/86x/CVE-2023-32353-PoC) :  ![starts](https://img.shields.io/github/stars/86x/CVE-2023-32353-PoC.svg) ![forks](https://img.shields.io/github/forks/86x/CVE-2023-32353-PoC.svg)

## CVE-2023-32315
 Openfire is an XMPP server licensed under the Open Source Apache License. Openfire's administrative console, a web-based application, was found to be vulnerable to a path traversal attack via the setup environment. This permitted an unauthenticated user to use the unauthenticated Openfire Setup Environment in an already configured Openfire environment to access restricted pages in the Openfire Admin Console reserved for administrative users. This vulnerability affects all versions of Openfire that have been released since April 2015, starting with version 3.10.0. The problem has been patched in Openfire release 4.7.5 and 4.6.8, and further improvements will be included in the yet-to-be released first version on the 4.8 branch (which is expected to be version 4.8.0). Users are advised to upgrade. If an Openfire upgrade isn’t available for a specific release, or isn’t quickly actionable, users may see the linked github advisory (GHSA-gw42-f939-fhvm) for mitigation advice.



- [https://github.com/tangxiaofeng7/CVE-2023-32315-Openfire-Bypass](https://github.com/tangxiaofeng7/CVE-2023-32315-Openfire-Bypass) :  ![starts](https://img.shields.io/github/stars/tangxiaofeng7/CVE-2023-32315-Openfire-Bypass.svg) ![forks](https://img.shields.io/github/forks/tangxiaofeng7/CVE-2023-32315-Openfire-Bypass.svg)

- [https://github.com/miko550/CVE-2023-32315](https://github.com/miko550/CVE-2023-32315) :  ![starts](https://img.shields.io/github/stars/miko550/CVE-2023-32315.svg) ![forks](https://img.shields.io/github/forks/miko550/CVE-2023-32315.svg)

- [https://github.com/bingtangbanli/VulnerabilityTools](https://github.com/bingtangbanli/VulnerabilityTools) :  ![starts](https://img.shields.io/github/stars/bingtangbanli/VulnerabilityTools.svg) ![forks](https://img.shields.io/github/forks/bingtangbanli/VulnerabilityTools.svg)

- [https://github.com/K3ysTr0K3R/CVE-2023-32315-EXPLOIT](https://github.com/K3ysTr0K3R/CVE-2023-32315-EXPLOIT) :  ![starts](https://img.shields.io/github/stars/K3ysTr0K3R/CVE-2023-32315-EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/K3ysTr0K3R/CVE-2023-32315-EXPLOIT.svg)

- [https://github.com/ThatNotEasy/CVE-2023-32315](https://github.com/ThatNotEasy/CVE-2023-32315) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2023-32315.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2023-32315.svg)

- [https://github.com/izzz0/CVE-2023-32315-POC](https://github.com/izzz0/CVE-2023-32315-POC) :  ![starts](https://img.shields.io/github/stars/izzz0/CVE-2023-32315-POC.svg) ![forks](https://img.shields.io/github/forks/izzz0/CVE-2023-32315-POC.svg)

- [https://github.com/gibran-abdillah/CVE-2023-32315](https://github.com/gibran-abdillah/CVE-2023-32315) :  ![starts](https://img.shields.io/github/stars/gibran-abdillah/CVE-2023-32315.svg) ![forks](https://img.shields.io/github/forks/gibran-abdillah/CVE-2023-32315.svg)

- [https://github.com/5rGJ5aCh5oCq5YW9/CVE-2023-32315exp](https://github.com/5rGJ5aCh5oCq5YW9/CVE-2023-32315exp) :  ![starts](https://img.shields.io/github/stars/5rGJ5aCh5oCq5YW9/CVE-2023-32315exp.svg) ![forks](https://img.shields.io/github/forks/5rGJ5aCh5oCq5YW9/CVE-2023-32315exp.svg)

- [https://github.com/ohnonoyesyes/CVE-2023-32315](https://github.com/ohnonoyesyes/CVE-2023-32315) :  ![starts](https://img.shields.io/github/stars/ohnonoyesyes/CVE-2023-32315.svg) ![forks](https://img.shields.io/github/forks/ohnonoyesyes/CVE-2023-32315.svg)

- [https://github.com/CN016/Openfire-RCE-CVE-2023-32315-](https://github.com/CN016/Openfire-RCE-CVE-2023-32315-) :  ![starts](https://img.shields.io/github/stars/CN016/Openfire-RCE-CVE-2023-32315-.svg) ![forks](https://img.shields.io/github/forks/CN016/Openfire-RCE-CVE-2023-32315-.svg)

- [https://github.com/pulentoski/Explotacion-CVE-2023-32315-Openfire](https://github.com/pulentoski/Explotacion-CVE-2023-32315-Openfire) :  ![starts](https://img.shields.io/github/stars/pulentoski/Explotacion-CVE-2023-32315-Openfire.svg) ![forks](https://img.shields.io/github/forks/pulentoski/Explotacion-CVE-2023-32315-Openfire.svg)

## CVE-2023-32314
 vm2 is a sandbox that can run untrusted code with Node's built-in modules. A sandbox escape vulnerability exists in vm2 for versions up to and including 3.9.17. It abuses an unexpected creation of a host object based on the specification of `Proxy`. As a result a threat actor can bypass the sandbox protections to gain remote code execution rights on the host running the sandbox. This vulnerability was patched in the release of version `3.9.18` of `vm2`. Users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/AdarkSt/Honeypot_Smart_Infrastructure](https://github.com/AdarkSt/Honeypot_Smart_Infrastructure) :  ![starts](https://img.shields.io/github/stars/AdarkSt/Honeypot_Smart_Infrastructure.svg) ![forks](https://img.shields.io/github/forks/AdarkSt/Honeypot_Smart_Infrastructure.svg)

## CVE-2023-32309
 PyMdown Extensions is a set of extensions for the `Python-Markdown` markdown project. In affected versions an arbitrary file read is possible when using include file syntax. By using the syntax `--8--"/etc/passwd"` or `--8--"/proc/self/environ"` the content of these files will be rendered in the generated documentation. Additionally, a path relative to a specified, allowed base path can also be used to render the content of a file outside the specified base paths: `--8-- "../../../../etc/passwd"`. Within the Snippets extension, there exists a `base_path` option but the implementation is vulnerable to Directory Traversal. The vulnerable section exists in `get_snippet_path(self, path)` lines 155 to 174 in snippets.py. Any readable file on the host where the plugin is executing may have its content exposed. This can impact any use of Snippets that exposes the use of Snippets to external users. It is never recommended to use Snippets to process user-facing, dynamic content. It is designed to process known content on the backend under the control of the host, but if someone were to accidentally enable it for user-facing content, undesired information could be exposed. This issue has been addressed in version 10.0. Users are advised to upgrade. Users unable to upgrade may restrict relative paths by filtering input.



- [https://github.com/itlabbet/CVE-2023-32309](https://github.com/itlabbet/CVE-2023-32309) :  ![starts](https://img.shields.io/github/stars/itlabbet/CVE-2023-32309.svg) ![forks](https://img.shields.io/github/forks/itlabbet/CVE-2023-32309.svg)

## CVE-2023-32243
 Improper Authentication vulnerability in WPDeveloper Essential Addons for Elementor allows Privilege Escalation. This issue affects Essential Addons for Elementor: from 5.4.0 through 5.7.1.



- [https://github.com/RandomRobbieBF/CVE-2023-32243](https://github.com/RandomRobbieBF/CVE-2023-32243) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-32243.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-32243.svg)

- [https://github.com/Jenderal92/WP-CVE-2023-32243](https://github.com/Jenderal92/WP-CVE-2023-32243) :  ![starts](https://img.shields.io/github/stars/Jenderal92/WP-CVE-2023-32243.svg) ![forks](https://img.shields.io/github/forks/Jenderal92/WP-CVE-2023-32243.svg)

- [https://github.com/gbrsh/CVE-2023-32243](https://github.com/gbrsh/CVE-2023-32243) :  ![starts](https://img.shields.io/github/stars/gbrsh/CVE-2023-32243.svg) ![forks](https://img.shields.io/github/forks/gbrsh/CVE-2023-32243.svg)

- [https://github.com/shaoyu521/Mass-CVE-2023-32243](https://github.com/shaoyu521/Mass-CVE-2023-32243) :  ![starts](https://img.shields.io/github/stars/shaoyu521/Mass-CVE-2023-32243.svg) ![forks](https://img.shields.io/github/forks/shaoyu521/Mass-CVE-2023-32243.svg)

- [https://github.com/thatonesecguy/Wordpress-Vulnerability-Identification-Scripts](https://github.com/thatonesecguy/Wordpress-Vulnerability-Identification-Scripts) :  ![starts](https://img.shields.io/github/stars/thatonesecguy/Wordpress-Vulnerability-Identification-Scripts.svg) ![forks](https://img.shields.io/github/forks/thatonesecguy/Wordpress-Vulnerability-Identification-Scripts.svg)

- [https://github.com/little44n1o/cve-2023-32243](https://github.com/little44n1o/cve-2023-32243) :  ![starts](https://img.shields.io/github/stars/little44n1o/cve-2023-32243.svg) ![forks](https://img.shields.io/github/forks/little44n1o/cve-2023-32243.svg)

- [https://github.com/YouGina/CVE-2023-32243](https://github.com/YouGina/CVE-2023-32243) :  ![starts](https://img.shields.io/github/stars/YouGina/CVE-2023-32243.svg) ![forks](https://img.shields.io/github/forks/YouGina/CVE-2023-32243.svg)

- [https://github.com/manavvedawala2/CVE-2023-32243-POC](https://github.com/manavvedawala2/CVE-2023-32243-POC) :  ![starts](https://img.shields.io/github/stars/manavvedawala2/CVE-2023-32243-POC.svg) ![forks](https://img.shields.io/github/forks/manavvedawala2/CVE-2023-32243-POC.svg)

- [https://github.com/manavvedawala2/CVE-2023-32243-proof-of-concept](https://github.com/manavvedawala2/CVE-2023-32243-proof-of-concept) :  ![starts](https://img.shields.io/github/stars/manavvedawala2/CVE-2023-32243-proof-of-concept.svg) ![forks](https://img.shields.io/github/forks/manavvedawala2/CVE-2023-32243-proof-of-concept.svg)

- [https://github.com/manavvedawala/CVE-2023-32243-proof-of-concept](https://github.com/manavvedawala/CVE-2023-32243-proof-of-concept) :  ![starts](https://img.shields.io/github/stars/manavvedawala/CVE-2023-32243-proof-of-concept.svg) ![forks](https://img.shields.io/github/forks/manavvedawala/CVE-2023-32243-proof-of-concept.svg)

- [https://github.com/dev0558/CVE-2023-32243-Detection-and-Mitigation-in-WordPress](https://github.com/dev0558/CVE-2023-32243-Detection-and-Mitigation-in-WordPress) :  ![starts](https://img.shields.io/github/stars/dev0558/CVE-2023-32243-Detection-and-Mitigation-in-WordPress.svg) ![forks](https://img.shields.io/github/forks/dev0558/CVE-2023-32243-Detection-and-Mitigation-in-WordPress.svg)

## CVE-2023-32235
 Ghost before 5.42.1 allows remote attackers to read arbitrary files within the active theme's folder via /assets/built%2F..%2F..%2F/ directory traversal. This occurs in frontend/web/middleware/static-theme.js.



- [https://github.com/AXRoux/Ghost-Path-Traversal-CVE-2023-32235-](https://github.com/AXRoux/Ghost-Path-Traversal-CVE-2023-32235-) :  ![starts](https://img.shields.io/github/stars/AXRoux/Ghost-Path-Traversal-CVE-2023-32235-.svg) ![forks](https://img.shields.io/github/forks/AXRoux/Ghost-Path-Traversal-CVE-2023-32235-.svg)

## CVE-2023-32233
 In the Linux kernel through 6.3.1, a use-after-free in Netfilter nf_tables when processing batch requests can be abused to perform arbitrary read and write operations on kernel memory. Unprivileged local users can obtain root privileges. This occurs because anonymous sets are mishandled.



- [https://github.com/Liuk3r/CVE-2023-32233](https://github.com/Liuk3r/CVE-2023-32233) :  ![starts](https://img.shields.io/github/stars/Liuk3r/CVE-2023-32233.svg) ![forks](https://img.shields.io/github/forks/Liuk3r/CVE-2023-32233.svg)

- [https://github.com/oferchen/POC-CVE-2023-32233](https://github.com/oferchen/POC-CVE-2023-32233) :  ![starts](https://img.shields.io/github/stars/oferchen/POC-CVE-2023-32233.svg) ![forks](https://img.shields.io/github/forks/oferchen/POC-CVE-2023-32233.svg)

- [https://github.com/PIDAN-HEIDASHUAI/CVE-2023-32233](https://github.com/PIDAN-HEIDASHUAI/CVE-2023-32233) :  ![starts](https://img.shields.io/github/stars/PIDAN-HEIDASHUAI/CVE-2023-32233.svg) ![forks](https://img.shields.io/github/forks/PIDAN-HEIDASHUAI/CVE-2023-32233.svg)

- [https://github.com/void0red/CVE-2023-32233](https://github.com/void0red/CVE-2023-32233) :  ![starts](https://img.shields.io/github/stars/void0red/CVE-2023-32233.svg) ![forks](https://img.shields.io/github/forks/void0red/CVE-2023-32233.svg)

- [https://github.com/RogelioPumajulca/TEST-CVE-2023-32233](https://github.com/RogelioPumajulca/TEST-CVE-2023-32233) :  ![starts](https://img.shields.io/github/stars/RogelioPumajulca/TEST-CVE-2023-32233.svg) ![forks](https://img.shields.io/github/forks/RogelioPumajulca/TEST-CVE-2023-32233.svg)

## CVE-2023-32174
 Unified Automation UaGateway NodeManagerOpcUa Use-After-Free Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Unified Automation UaGateway. Authentication is required to exploit this vulnerability when the product is in its default configuration.

The specific flaw exists within the handling of NodeManagerOpcUa objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.
. Was ZDI-CAN-20577.



- [https://github.com/0vercl0k/pwn2own2023-miami](https://github.com/0vercl0k/pwn2own2023-miami) :  ![starts](https://img.shields.io/github/stars/0vercl0k/pwn2own2023-miami.svg) ![forks](https://img.shields.io/github/forks/0vercl0k/pwn2own2023-miami.svg)

## CVE-2023-32173
 Unified Automation UaGateway AddServer XML Injection Denial-of-Service Vulnerability. This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Unified Automation UaGateway. Authentication is required to exploit this vulnerability when the product is in its default configuration.

The specific flaw exists within the implementation of the AddServer method. By specifying crafted arguments, an attacker can cause invalid characters to be inserted into an XML configuration file. An attacker can leverage this vulnerability to create a persistent denial-of-service condition on the system. 
. Was ZDI-CAN-20576.



- [https://github.com/0vercl0k/pwn2own2023-miami](https://github.com/0vercl0k/pwn2own2023-miami) :  ![starts](https://img.shields.io/github/stars/0vercl0k/pwn2own2023-miami.svg) ![forks](https://img.shields.io/github/forks/0vercl0k/pwn2own2023-miami.svg)

## CVE-2023-32171
 Unified Automation UaGateway OPC UA Server Null Pointer Dereference Denial-of-Service Vulnerability. This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Unified Automation UaGateway. Authentication is required to exploit this vulnerability.

The specific flaw exists within the ImportCsv method. A crafted XML payload can cause a null pointer dereference. An attacker can leverage this vulnerability to create a denial-of-service condition on the system. Was ZDI-CAN-20495.



- [https://github.com/0vercl0k/pwn2own2023-miami](https://github.com/0vercl0k/pwn2own2023-miami) :  ![starts](https://img.shields.io/github/stars/0vercl0k/pwn2own2023-miami.svg) ![forks](https://img.shields.io/github/forks/0vercl0k/pwn2own2023-miami.svg)

## CVE-2023-32170
 Unified Automation UaGateway OPC UA Server Improper Input Validation Denial-of-Service Vulnerability. This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Unified Automation UaGateway. User interaction is required to exploit this vulnerability in that the target must choose to accept a client certificate.

The specific flaw exists within the processing of client certificates. The issue results from the lack of proper validation of certificate data. An attacker can leverage this vulnerability to create a denial-of-service condition on the system. Was ZDI-CAN-20494.



- [https://github.com/0vercl0k/pwn2own2023-miami](https://github.com/0vercl0k/pwn2own2023-miami) :  ![starts](https://img.shields.io/github/stars/0vercl0k/pwn2own2023-miami.svg) ![forks](https://img.shields.io/github/forks/0vercl0k/pwn2own2023-miami.svg)

## CVE-2023-32163
 Wacom Drivers for Windows Link Following Local Privilege Escalation Vulnerability. This vulnerability allows local attackers to escalate privileges on affected installations of Wacom Drivers for Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability.

The specific flaw exists within the Tablet Service. By creating a symbolic link, an attacker can abuse the service to create a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM. Was ZDI-CAN-16857.



- [https://github.com/LucaBarile/ZDI-CAN-16857](https://github.com/LucaBarile/ZDI-CAN-16857) :  ![starts](https://img.shields.io/github/stars/LucaBarile/ZDI-CAN-16857.svg) ![forks](https://img.shields.io/github/forks/LucaBarile/ZDI-CAN-16857.svg)

## CVE-2023-32117
 Missing Authorization vulnerability in SoftLab Integrate Google Drive allows Exploiting Incorrectly Configured Access Control Security Levels.This issue affects Integrate Google Drive: from n/a through 1.1.99.



- [https://github.com/RandomRobbieBF/CVE-2023-32117](https://github.com/RandomRobbieBF/CVE-2023-32117) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-32117.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-32117.svg)

## CVE-2023-32073
 WWBN AVideo is an open source video platform. In versions 12.4 and prior, a command injection vulnerability exists at `plugin/CloneSite/cloneClient.json.php` which allows Remote Code Execution if you CloneSite Plugin. This is a bypass to the fix for CVE-2023-30854, which affects WWBN AVideo up to version 12.3. This issue is patched in commit 1df4af01f80d56ff2c4c43b89d0bac151e7fb6e3.



- [https://github.com/jmrcsnchz/CVE-2023-32073](https://github.com/jmrcsnchz/CVE-2023-32073) :  ![starts](https://img.shields.io/github/stars/jmrcsnchz/CVE-2023-32073.svg) ![forks](https://img.shields.io/github/forks/jmrcsnchz/CVE-2023-32073.svg)

## CVE-2023-32031
 Microsoft Exchange Server Remote Code Execution Vulnerability



- [https://github.com/Avento/CVE-2023-32031](https://github.com/Avento/CVE-2023-32031) :  ![starts](https://img.shields.io/github/stars/Avento/CVE-2023-32031.svg) ![forks](https://img.shields.io/github/forks/Avento/CVE-2023-32031.svg)

## CVE-2023-31902
 RPA Technology Mobile Mouse 3.6.0.4 is vulnerable to Remote Code Execution (RCE).



- [https://github.com/blue0x1/mobilemouse-exploit](https://github.com/blue0x1/mobilemouse-exploit) :  ![starts](https://img.shields.io/github/stars/blue0x1/mobilemouse-exploit.svg) ![forks](https://img.shields.io/github/forks/blue0x1/mobilemouse-exploit.svg)

## CVE-2023-31853
 Cudy LT400 1.13.4 is vulnerable Cross Site Scripting (XSS) in /cgi-bin/luci/admin/network/bandwidth via the icon parameter.



- [https://github.com/CalfCrusher/CVE-2023-31853](https://github.com/CalfCrusher/CVE-2023-31853) :  ![starts](https://img.shields.io/github/stars/CalfCrusher/CVE-2023-31853.svg) ![forks](https://img.shields.io/github/forks/CalfCrusher/CVE-2023-31853.svg)

## CVE-2023-31852
 Cudy LT400 1.13.4 is vulnerable to Cross Site Scripting (XSS) in cgi-bin/luci/admin/network/wireless/config via the iface parameter.



- [https://github.com/CalfCrusher/CVE-2023-31852](https://github.com/CalfCrusher/CVE-2023-31852) :  ![starts](https://img.shields.io/github/stars/CalfCrusher/CVE-2023-31852.svg) ![forks](https://img.shields.io/github/forks/CalfCrusher/CVE-2023-31852.svg)

## CVE-2023-31851
 Cudy LT400 1.13.4 is has a cross-site scripting (XSS) vulnerability in /cgi-bin/luci/admin/network/wireless/status via the iface parameter.



- [https://github.com/CalfCrusher/CVE-2023-31851](https://github.com/CalfCrusher/CVE-2023-31851) :  ![starts](https://img.shields.io/github/stars/CalfCrusher/CVE-2023-31851.svg) ![forks](https://img.shields.io/github/forks/CalfCrusher/CVE-2023-31851.svg)

## CVE-2023-31779
 Wekan v6.84 and earlier is vulnerable to Cross Site Scripting (XSS). An attacker with user privilege on kanban board can insert JavaScript code in in "Reaction to comment" feature.



- [https://github.com/jet-pentest/CVE-2023-31779](https://github.com/jet-pentest/CVE-2023-31779) :  ![starts](https://img.shields.io/github/stars/jet-pentest/CVE-2023-31779.svg) ![forks](https://img.shields.io/github/forks/jet-pentest/CVE-2023-31779.svg)

## CVE-2023-31756
 A command injection vulnerability exists in the administrative web portal in TP-Link Archer VR1600V devices running firmware Versions = 0.1.0. 0.9.1 v5006.0 Build 220518 Rel.32480n which allows remote attackers, authenticated to the administrative web portal as an administrator user to open an operating system level shell via the 'X_TP_IfName' parameter.



- [https://github.com/StanleyJobsonAU/LongBow](https://github.com/StanleyJobsonAU/LongBow) :  ![starts](https://img.shields.io/github/stars/StanleyJobsonAU/LongBow.svg) ![forks](https://img.shields.io/github/forks/StanleyJobsonAU/LongBow.svg)

## CVE-2023-31753
 SQL injection vulnerability in diskusi.php in eNdonesia 8.7, allows an attacker to execute arbitrary SQL commands via the "rid=" parameter.



- [https://github.com/khmk2k/CVE-2023-31753](https://github.com/khmk2k/CVE-2023-31753) :  ![starts](https://img.shields.io/github/stars/khmk2k/CVE-2023-31753.svg) ![forks](https://img.shields.io/github/forks/khmk2k/CVE-2023-31753.svg)

## CVE-2023-31747
 Wondershare Filmora 12 (Build 12.2.1.2088) was discovered to contain an unquoted service path vulnerability via the component NativePushService. This vulnerability allows attackers to launch processes with elevated privileges.



- [https://github.com/msd0pe-1/CVE-2023-31747](https://github.com/msd0pe-1/CVE-2023-31747) :  ![starts](https://img.shields.io/github/stars/msd0pe-1/CVE-2023-31747.svg) ![forks](https://img.shields.io/github/forks/msd0pe-1/CVE-2023-31747.svg)

## CVE-2023-31726
 AList 3.15.1 is vulnerable to Incorrect Access Control, which can be exploited by attackers to obtain sensitive information.



- [https://github.com/J6451/CVE-2023-31726](https://github.com/J6451/CVE-2023-31726) :  ![starts](https://img.shields.io/github/stars/J6451/CVE-2023-31726.svg) ![forks](https://img.shields.io/github/forks/J6451/CVE-2023-31726.svg)

## CVE-2023-31719
 FUXA = 1.1.12 is vulnerable to SQL Injection via /api/signin.



- [https://github.com/MateusTesser/CVE-2023-31719](https://github.com/MateusTesser/CVE-2023-31719) :  ![starts](https://img.shields.io/github/stars/MateusTesser/CVE-2023-31719.svg) ![forks](https://img.shields.io/github/forks/MateusTesser/CVE-2023-31719.svg)

## CVE-2023-31718
 FUXA = 1.1.12 is vulnerable to Local via Inclusion via /api/download.



- [https://github.com/MateusTesser/CVE-2023-31718](https://github.com/MateusTesser/CVE-2023-31718) :  ![starts](https://img.shields.io/github/stars/MateusTesser/CVE-2023-31718.svg) ![forks](https://img.shields.io/github/forks/MateusTesser/CVE-2023-31718.svg)

## CVE-2023-31717
 A SQL Injection attack in FUXA = 1.1.12 allows exfiltration of confidential information from the database.



- [https://github.com/MateusTesser/CVE-2023-31717](https://github.com/MateusTesser/CVE-2023-31717) :  ![starts](https://img.shields.io/github/stars/MateusTesser/CVE-2023-31717.svg) ![forks](https://img.shields.io/github/forks/MateusTesser/CVE-2023-31717.svg)

## CVE-2023-31716
 FUXA = 1.1.12 has a Local File Inclusion vulnerability via file=fuxa.log



- [https://github.com/MateusTesser/CVE-2023-31716](https://github.com/MateusTesser/CVE-2023-31716) :  ![starts](https://img.shields.io/github/stars/MateusTesser/CVE-2023-31716.svg) ![forks](https://img.shields.io/github/forks/MateusTesser/CVE-2023-31716.svg)

## CVE-2023-31714
 Chitor-CMS before v1.1.2 was discovered to contain multiple SQL injection vulnerabilities.



- [https://github.com/msd0pe-1/CVE-2023-31714](https://github.com/msd0pe-1/CVE-2023-31714) :  ![starts](https://img.shields.io/github/stars/msd0pe-1/CVE-2023-31714.svg) ![forks](https://img.shields.io/github/forks/msd0pe-1/CVE-2023-31714.svg)

## CVE-2023-31711
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/HritikThapa7/CVE-2023-31711](https://github.com/HritikThapa7/CVE-2023-31711) :  ![starts](https://img.shields.io/github/stars/HritikThapa7/CVE-2023-31711.svg) ![forks](https://img.shields.io/github/forks/HritikThapa7/CVE-2023-31711.svg)

## CVE-2023-31705
 A Reflected Cross-site scripting (XSS) vulnerability in Sourcecodester Task Reminder System 1.0 allows an authenticated user to inject malicious javascript into the page parameter.



- [https://github.com/d34dun1c02n/CVE-2023-31705](https://github.com/d34dun1c02n/CVE-2023-31705) :  ![starts](https://img.shields.io/github/stars/d34dun1c02n/CVE-2023-31705.svg) ![forks](https://img.shields.io/github/forks/d34dun1c02n/CVE-2023-31705.svg)

## CVE-2023-31704
 Sourcecodester Online Computer and Laptop Store 1.0 is vulnerable to Incorrect Access Control, which allows remote attackers to elevate privileges to the administrator's role.



- [https://github.com/d34dun1c02n/CVE-2023-31704](https://github.com/d34dun1c02n/CVE-2023-31704) :  ![starts](https://img.shields.io/github/stars/d34dun1c02n/CVE-2023-31704.svg) ![forks](https://img.shields.io/github/forks/d34dun1c02n/CVE-2023-31704.svg)

## CVE-2023-31703
 Cross Site Scripting (XSS) in the edit user form in Microworld Technologies eScan management console 14.0.1400.2281 allows remote attacker to inject arbitrary code via the from parameter.



- [https://github.com/sahiloj/CVE-2023-31703](https://github.com/sahiloj/CVE-2023-31703) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-31703.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-31703.svg)

## CVE-2023-31702
 SQL injection in the View User Profile in MicroWorld eScan Management Console 14.0.1400.2281 allows remote attacker to dump entire database and gain windows XP command shell to perform code execution on database server via GetUserCurrentPwd?UsrId=1.



- [https://github.com/sahiloj/CVE-2023-31702](https://github.com/sahiloj/CVE-2023-31702) :  ![starts](https://img.shields.io/github/stars/sahiloj/CVE-2023-31702.svg) ![forks](https://img.shields.io/github/forks/sahiloj/CVE-2023-31702.svg)

- [https://github.com/2019000102494/CVE-2023-31702](https://github.com/2019000102494/CVE-2023-31702) :  ![starts](https://img.shields.io/github/stars/2019000102494/CVE-2023-31702.svg) ![forks](https://img.shields.io/github/forks/2019000102494/CVE-2023-31702.svg)

## CVE-2023-31664
 A reflected cross-site scripting (XSS) vulnerability in /authenticationendpoint/login.do of WSO2 API Manager before 4.2.0 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the tenantDomain parameter.



- [https://github.com/adilkhan7/CVE-2023-31664](https://github.com/adilkhan7/CVE-2023-31664) :  ![starts](https://img.shields.io/github/stars/adilkhan7/CVE-2023-31664.svg) ![forks](https://img.shields.io/github/forks/adilkhan7/CVE-2023-31664.svg)

## CVE-2023-31634
 In TeslaMate before 1.27.2, there is unauthorized access to port 4000 for remote viewing and operation of user data. After accessing the IP address for the TeslaMate instance, an attacker can switch the port to 3000 to enter Grafana for remote operations. At that time, the default username and password can be used to enter the Grafana management console without logging in, a related issue to CVE-2022-23126.



- [https://github.com/iSee857/CVE-2023-31634](https://github.com/iSee857/CVE-2023-31634) :  ![starts](https://img.shields.io/github/stars/iSee857/CVE-2023-31634.svg) ![forks](https://img.shields.io/github/forks/iSee857/CVE-2023-31634.svg)

## CVE-2023-31606
 A Regular Expression Denial of Service (ReDoS) issue was discovered in the sanitize_html function of redcloth gem v4.0.0. This vulnerability allows attackers to cause a Denial of Service (DoS) via supplying a crafted payload.



- [https://github.com/merbinr/CVE-2023-31606](https://github.com/merbinr/CVE-2023-31606) :  ![starts](https://img.shields.io/github/stars/merbinr/CVE-2023-31606.svg) ![forks](https://img.shields.io/github/forks/merbinr/CVE-2023-31606.svg)

## CVE-2023-31595
 IC Realtime ICIP-P2012T 2.420 is vulnerable to Incorrect Access Control via unauthenticated port access.



- [https://github.com/Yozarseef95/CVE-2023-31595](https://github.com/Yozarseef95/CVE-2023-31595) :  ![starts](https://img.shields.io/github/stars/Yozarseef95/CVE-2023-31595.svg) ![forks](https://img.shields.io/github/forks/Yozarseef95/CVE-2023-31595.svg)

## CVE-2023-31594
 IC Realtime ICIP-P2012T 2.420 is vulnerable to Incorrect Access Control via an exposed HTTP channel using VLC network.



- [https://github.com/Yozarseef95/CVE-2023-31594](https://github.com/Yozarseef95/CVE-2023-31594) :  ![starts](https://img.shields.io/github/stars/Yozarseef95/CVE-2023-31594.svg) ![forks](https://img.shields.io/github/forks/Yozarseef95/CVE-2023-31594.svg)

## CVE-2023-31584
 GitHub repository cu/silicon commit a9ef36 was discovered to contain a reflected cross-site scripting (XSS) vulnerability via the User Input field.



- [https://github.com/rootd4ddy/CVE-2023-43838](https://github.com/rootd4ddy/CVE-2023-43838) :  ![starts](https://img.shields.io/github/stars/rootd4ddy/CVE-2023-43838.svg) ![forks](https://img.shields.io/github/forks/rootd4ddy/CVE-2023-43838.svg)

- [https://github.com/rootd4ddy/CVE-2023-31584](https://github.com/rootd4ddy/CVE-2023-31584) :  ![starts](https://img.shields.io/github/stars/rootd4ddy/CVE-2023-31584.svg) ![forks](https://img.shields.io/github/forks/rootd4ddy/CVE-2023-31584.svg)

## CVE-2023-31546
 Cross Site Scripting (XSS) vulnerability in DedeBIZ v6.0.3 allows attackers to run arbitrary code via the search feature.



- [https://github.com/ran9ege/CVE-2023-31546](https://github.com/ran9ege/CVE-2023-31546) :  ![starts](https://img.shields.io/github/stars/ran9ege/CVE-2023-31546.svg) ![forks](https://img.shields.io/github/forks/ran9ege/CVE-2023-31546.svg)

## CVE-2023-31541
 A unrestricted file upload vulnerability was discovered in the ‘Browse and upload images’ feature of the CKEditor v1.2.3 plugin for Redmine, which allows arbitrary files to be uploaded to the server.



- [https://github.com/DreamD2v/CVE-2023-31541](https://github.com/DreamD2v/CVE-2023-31541) :  ![starts](https://img.shields.io/github/stars/DreamD2v/CVE-2023-31541.svg) ![forks](https://img.shields.io/github/forks/DreamD2v/CVE-2023-31541.svg)

## CVE-2023-31497
 Incorrect access control in Quick Heal Technologies Limited Seqrite Endpoint Security (EPS) all versions prior to v8.0 allows attackers to escalate privileges to root via supplying a crafted binary to the target system.



- [https://github.com/0xInfection/EPScalate](https://github.com/0xInfection/EPScalate) :  ![starts](https://img.shields.io/github/stars/0xInfection/EPScalate.svg) ![forks](https://img.shields.io/github/forks/0xInfection/EPScalate.svg)

## CVE-2023-31446
 In Cassia Gateway firmware XC1000_2.1.1.2303082218 and XC2000_2.1.1.2303090947, the queueUrl parameter in /bypass/config is not sanitized. This leads to injecting Bash code and executing it with root privileges on device startup.



- [https://github.com/Dodge-MPTC/CVE-2023-31446-Remote-Code-Execution](https://github.com/Dodge-MPTC/CVE-2023-31446-Remote-Code-Execution) :  ![starts](https://img.shields.io/github/stars/Dodge-MPTC/CVE-2023-31446-Remote-Code-Execution.svg) ![forks](https://img.shields.io/github/forks/Dodge-MPTC/CVE-2023-31446-Remote-Code-Execution.svg)

## CVE-2023-31445
 Cassia Access controller before 2.1.1.2203171453, was discovered to have a unprivileged -information disclosure vulnerability that allows read-only users have the ability to enumerate all other users and discover e-mail addresses, phone numbers, and privileges of all other users.



- [https://github.com/Dodge-MPTC/CVE-2023-31445-Unprivileged-Information-Disclosure](https://github.com/Dodge-MPTC/CVE-2023-31445-Unprivileged-Information-Disclosure) :  ![starts](https://img.shields.io/github/stars/Dodge-MPTC/CVE-2023-31445-Unprivileged-Information-Disclosure.svg) ![forks](https://img.shields.io/github/forks/Dodge-MPTC/CVE-2023-31445-Unprivileged-Information-Disclosure.svg)

## CVE-2023-31443
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/MaherAzzouzi/CVE-2023-31443](https://github.com/MaherAzzouzi/CVE-2023-31443) :  ![starts](https://img.shields.io/github/stars/MaherAzzouzi/CVE-2023-31443.svg) ![forks](https://img.shields.io/github/forks/MaherAzzouzi/CVE-2023-31443.svg)

## CVE-2023-31435
 Multiple components (such as Onlinetemplate-Verwaltung, Liste aller Teilbereiche, Umfragen anzeigen, and questionnaire previews) in evasys before 8.2 Build 2286 and 9.x before 9.0 Build 2401 allow authenticated attackers to read and write to unauthorized data by accessing functions directly.



- [https://github.com/trustcves/CVE-2023-31435](https://github.com/trustcves/CVE-2023-31435) :  ![starts](https://img.shields.io/github/stars/trustcves/CVE-2023-31435.svg) ![forks](https://img.shields.io/github/forks/trustcves/CVE-2023-31435.svg)

## CVE-2023-31434
 The parameters nutzer_titel, nutzer_vn, and nutzer_nn in the user profile, and langID and ONLINEID in direct links, in evasys before 8.2 Build 2286 and 9.x before 9.0 Build 2401 do not validate input, which allows authenticated attackers to inject HTML Code and XSS payloads in multiple locations.



- [https://github.com/trustcves/CVE-2023-31434](https://github.com/trustcves/CVE-2023-31434) :  ![starts](https://img.shields.io/github/stars/trustcves/CVE-2023-31434.svg) ![forks](https://img.shields.io/github/forks/trustcves/CVE-2023-31434.svg)

## CVE-2023-31433
 A SQL injection issue in Logbuch in evasys before 8.2 Build 2286 and 9.x before 9.0 Build 2401 allows authenticated attackers to execute SQL statements via the welche parameter.



- [https://github.com/trustcves/CVE-2023-31433](https://github.com/trustcves/CVE-2023-31433) :  ![starts](https://img.shields.io/github/stars/trustcves/CVE-2023-31433.svg) ![forks](https://img.shields.io/github/forks/trustcves/CVE-2023-31433.svg)

## CVE-2023-31419
 A flaw was discovered in Elasticsearch, affecting the _search API that allowed a specially crafted query string to cause a Stack Overflow and ultimately a Denial of Service.



- [https://github.com/sqrtZeroKnowledge/Elasticsearch-Exploit-CVE-2023-31419](https://github.com/sqrtZeroKnowledge/Elasticsearch-Exploit-CVE-2023-31419) :  ![starts](https://img.shields.io/github/stars/sqrtZeroKnowledge/Elasticsearch-Exploit-CVE-2023-31419.svg) ![forks](https://img.shields.io/github/forks/sqrtZeroKnowledge/Elasticsearch-Exploit-CVE-2023-31419.svg)

- [https://github.com/u238/Elasticsearch-CVE-2023-31419](https://github.com/u238/Elasticsearch-CVE-2023-31419) :  ![starts](https://img.shields.io/github/stars/u238/Elasticsearch-CVE-2023-31419.svg) ![forks](https://img.shields.io/github/forks/u238/Elasticsearch-CVE-2023-31419.svg)

## CVE-2023-31355
 Improper restriction of write operations in SNP firmware could allow a malicious hypervisor to overwrite a guest's UMC seed potentially allowing reading of memory from a decommissioned guest.



- [https://github.com/Freax13/cve-2023-31355-poc](https://github.com/Freax13/cve-2023-31355-poc) :  ![starts](https://img.shields.io/github/stars/Freax13/cve-2023-31355-poc.svg) ![forks](https://img.shields.io/github/forks/Freax13/cve-2023-31355-poc.svg)

## CVE-2023-31346
 Failure to initialize
memory in SEV Firmware may allow a privileged attacker to access stale data
from other guests.




















- [https://github.com/Freax13/cve-2023-31346-poc](https://github.com/Freax13/cve-2023-31346-poc) :  ![starts](https://img.shields.io/github/stars/Freax13/cve-2023-31346-poc.svg) ![forks](https://img.shields.io/github/forks/Freax13/cve-2023-31346-poc.svg)

## CVE-2023-31320
 Improper input validation in the AMD RadeonTM Graphics display driver may allow an attacker to corrupt the display potentially resulting in denial of service.
















- [https://github.com/whypet/CVE-2023-31320](https://github.com/whypet/CVE-2023-31320) :  ![starts](https://img.shields.io/github/stars/whypet/CVE-2023-31320.svg) ![forks](https://img.shields.io/github/forks/whypet/CVE-2023-31320.svg)

## CVE-2023-31290
 Trust Wallet Core before 3.1.1, as used in the Trust Wallet browser extension before 0.0.183, allows theft of funds because the entropy is 32 bits, as exploited in the wild in December 2022 and March 2023. This occurs because the mt19937 Mersenne Twister takes a single 32-bit value as an input seed, resulting in only four billion possible mnemonics. The affected versions of the browser extension are 0.0.172 through 0.0.182. To steal funds efficiently, an attacker can identify all Ethereum addresses created since the 0.0.172 release, and check whether they are Ethereum addresses that could have been created by this extension. To respond to the risk, affected users need to upgrade the product version and also move funds to a new wallet address.



- [https://github.com/ohexa/py_trustwallet_wasm](https://github.com/ohexa/py_trustwallet_wasm) :  ![starts](https://img.shields.io/github/stars/ohexa/py_trustwallet_wasm.svg) ![forks](https://img.shields.io/github/forks/ohexa/py_trustwallet_wasm.svg)

## CVE-2023-31070
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/bugprove/cve-2023-31070](https://github.com/bugprove/cve-2023-31070) :  ![starts](https://img.shields.io/github/stars/bugprove/cve-2023-31070.svg) ![forks](https://img.shields.io/github/forks/bugprove/cve-2023-31070.svg)

## CVE-2023-30943
 The vulnerability was found Moodle which exists because the application allows a user to control path of the older to create in TinyMCE loaders. A remote user can send a specially crafted HTTP request and create arbitrary folders on the system.



- [https://github.com/d0rb/CVE-2023-30943](https://github.com/d0rb/CVE-2023-30943) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-30943.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-30943.svg)

- [https://github.com/Chocapikk/CVE-2023-30943](https://github.com/Chocapikk/CVE-2023-30943) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-30943.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-30943.svg)

- [https://github.com/RubyCat1337/CVE-2023-30943](https://github.com/RubyCat1337/CVE-2023-30943) :  ![starts](https://img.shields.io/github/stars/RubyCat1337/CVE-2023-30943.svg) ![forks](https://img.shields.io/github/forks/RubyCat1337/CVE-2023-30943.svg)

## CVE-2023-30861
 Flask is a lightweight WSGI web application framework. When all of the following conditions are met, a response containing data intended for one client may be cached and subsequently sent by the proxy to other clients. If the proxy also caches `Set-Cookie` headers, it may send one client's `session` cookie to other clients. The severity depends on the application's use of the session and the proxy's behavior regarding cookies. The risk depends on all these conditions being met.

1. The application must be hosted behind a caching proxy that does not strip cookies or ignore responses with cookies.
2. The application sets `session.permanent = True`
3. The application does not access or modify the session at any point during a request.
4. `SESSION_REFRESH_EACH_REQUEST` enabled (the default).
5. The application does not set a `Cache-Control` header to indicate that a page is private or should not be cached.

This happens because vulnerable versions of Flask only set the `Vary: Cookie` header when the session is accessed or modified, not when it is refreshed (re-sent to update the expiration) without being accessed or modified. This issue has been fixed in versions 2.3.2 and 2.2.5.



- [https://github.com/fromitive/cve-2023-30861-poc](https://github.com/fromitive/cve-2023-30861-poc) :  ![starts](https://img.shields.io/github/stars/fromitive/cve-2023-30861-poc.svg) ![forks](https://img.shields.io/github/forks/fromitive/cve-2023-30861-poc.svg)

## CVE-2023-30854
 AVideo is an open source video platform. Prior to version 12.4, an OS Command Injection vulnerability in an authenticated endpoint `/plugin/CloneSite/cloneClient.json.php` allows attackers to achieve Remote Code Execution. This issue is fixed in version 12.4.



- [https://github.com/jmrcsnchz/CVE-2023-30854](https://github.com/jmrcsnchz/CVE-2023-30854) :  ![starts](https://img.shields.io/github/stars/jmrcsnchz/CVE-2023-30854.svg) ![forks](https://img.shields.io/github/forks/jmrcsnchz/CVE-2023-30854.svg)

## CVE-2023-30845
 ESPv2 is a service proxy that provides API management capabilities using Google Service Infrastructure. ESPv2 2.20.0 through 2.42.0 contains an authentication bypass vulnerability. API clients can craft a malicious `X-HTTP-Method-Override` header value to bypass JWT authentication in specific cases.

ESPv2 allows malicious requests to bypass authentication if both the conditions are true: The requested HTTP method is **not** in the API service definition (OpenAPI spec or gRPC `google.api.http` proto annotations, and the specified `X-HTTP-Method-Override` is a valid HTTP method in the API service definition. ESPv2 will forward the request to your backend without checking the JWT. Attackers can craft requests with a malicious `X-HTTP-Method-Override` value that allows them to bypass specifying JWTs. Restricting API access with API keys works as intended and is not affected by this vulnerability.

Upgrade deployments to release v2.43.0 or higher to receive a patch. This release ensures that JWT authentication occurs, even when the caller specifies `x-http-method-override`. `x-http-method-override` is still supported by v2.43.0+. API clients can continue sending this header to ESPv2.



- [https://github.com/himori123/-CVE-2023-30845](https://github.com/himori123/-CVE-2023-30845) :  ![starts](https://img.shields.io/github/stars/himori123/-CVE-2023-30845.svg) ![forks](https://img.shields.io/github/forks/himori123/-CVE-2023-30845.svg)

- [https://github.com/jayluxferro/ESPv2](https://github.com/jayluxferro/ESPv2) :  ![starts](https://img.shields.io/github/stars/jayluxferro/ESPv2.svg) ![forks](https://img.shields.io/github/forks/jayluxferro/ESPv2.svg)

## CVE-2023-30839
 PrestaShop is an Open Source e-commerce web application. Versions prior to 8.0.4 and 1.7.8.9 contain a SQL filtering vulnerability. A BO user can write, update, and delete in the database, even without having specific rights. PrestaShop 8.0.4 and 1.7.8.9 contain a patch for this issue. There are no known workarounds.



- [https://github.com/drkbcn/lblfixer_cve_2023_30839](https://github.com/drkbcn/lblfixer_cve_2023_30839) :  ![starts](https://img.shields.io/github/stars/drkbcn/lblfixer_cve_2023_30839.svg) ![forks](https://img.shields.io/github/forks/drkbcn/lblfixer_cve_2023_30839.svg)

## CVE-2023-30800
 The web server used by MikroTik RouterOS version 6 is affected by a heap memory corruption issue. A remote and unauthenticated attacker can corrupt the server's heap memory by sending a crafted HTTP request. As a result, the web interface crashes and is immediately restarted. The issue was fixed in RouterOS 6.49.10 stable. RouterOS version 7 is not affected.




- [https://github.com/griffinsectio/CVE-2023-30800_PoC](https://github.com/griffinsectio/CVE-2023-30800_PoC) :  ![starts](https://img.shields.io/github/stars/griffinsectio/CVE-2023-30800_PoC.svg) ![forks](https://img.shields.io/github/forks/griffinsectio/CVE-2023-30800_PoC.svg)

- [https://github.com/griffinsectio/CVE-2023-30800_PoC_go](https://github.com/griffinsectio/CVE-2023-30800_PoC_go) :  ![starts](https://img.shields.io/github/stars/griffinsectio/CVE-2023-30800_PoC_go.svg) ![forks](https://img.shields.io/github/forks/griffinsectio/CVE-2023-30800_PoC_go.svg)

## CVE-2023-30777
 Unauth. Reflected Cross-Site Scripting (XSS) vulnerability in WP Engine Advanced Custom Fields Pro, WP Engine Advanced Custom Fields plugins = 6.1.5 versions.



- [https://github.com/Alucard0x1/CVE-2023-30777](https://github.com/Alucard0x1/CVE-2023-30777) :  ![starts](https://img.shields.io/github/stars/Alucard0x1/CVE-2023-30777.svg) ![forks](https://img.shields.io/github/forks/Alucard0x1/CVE-2023-30777.svg)

## CVE-2023-30765
 ​Delta Electronics InfraSuite Device Master versions prior to 1.0.7 contain improper access controls that could allow an attacker to alter privilege management configurations, resulting in privilege escalation.



- [https://github.com/0xfml/CVE-2023-30765](https://github.com/0xfml/CVE-2023-30765) :  ![starts](https://img.shields.io/github/stars/0xfml/CVE-2023-30765.svg) ![forks](https://img.shields.io/github/forks/0xfml/CVE-2023-30765.svg)

## CVE-2023-30547
 vm2 is a sandbox that can run untrusted code with whitelisted Node's built-in modules. There exists a vulnerability in exception sanitization of vm2 for versions up to 3.9.16, allowing attackers to raise an unsanitized host exception inside `handleException()` which can be used to escape the sandbox and run arbitrary code in host context. This vulnerability was patched in the release of version `3.9.17` of `vm2`. There are no known workarounds for this vulnerability. Users are advised to upgrade.



- [https://github.com/rvizx/CVE-2023-30547](https://github.com/rvizx/CVE-2023-30547) :  ![starts](https://img.shields.io/github/stars/rvizx/CVE-2023-30547.svg) ![forks](https://img.shields.io/github/forks/rvizx/CVE-2023-30547.svg)

- [https://github.com/Cur1iosity/CVE-2023-30547](https://github.com/Cur1iosity/CVE-2023-30547) :  ![starts](https://img.shields.io/github/stars/Cur1iosity/CVE-2023-30547.svg) ![forks](https://img.shields.io/github/forks/Cur1iosity/CVE-2023-30547.svg)

- [https://github.com/user0x1337/CVE-2023-30547](https://github.com/user0x1337/CVE-2023-30547) :  ![starts](https://img.shields.io/github/stars/user0x1337/CVE-2023-30547.svg) ![forks](https://img.shields.io/github/forks/user0x1337/CVE-2023-30547.svg)

- [https://github.com/junnythemarksman/CVE-2023-30547](https://github.com/junnythemarksman/CVE-2023-30547) :  ![starts](https://img.shields.io/github/stars/junnythemarksman/CVE-2023-30547.svg) ![forks](https://img.shields.io/github/forks/junnythemarksman/CVE-2023-30547.svg)

## CVE-2023-30545
 PrestaShop is an Open Source e-commerce web application. Prior to versions 8.0.4 and 1.7.8.9, it is possible for a user with access to the SQL Manager (Advanced Options - Database) to arbitrarily read any file on the operating system when using SQL function `LOAD_FILE` in a `SELECT` request. This gives the user access to critical information. A patch is available in PrestaShop 8.0.4 and PS 1.7.8.9




- [https://github.com/drkbcn/lblfixer_cve_2023_30839](https://github.com/drkbcn/lblfixer_cve_2023_30839) :  ![starts](https://img.shields.io/github/stars/drkbcn/lblfixer_cve_2023_30839.svg) ![forks](https://img.shields.io/github/forks/drkbcn/lblfixer_cve_2023_30839.svg)

## CVE-2023-30533
 SheetJS Community Edition before 0.19.3 allows Prototype Pollution via a crafted file. In other words. 0.19.2 and earlier are affected, whereas 0.19.3 and later are unaffected.



- [https://github.com/BenEdridge/CVE-2023-30533](https://github.com/BenEdridge/CVE-2023-30533) :  ![starts](https://img.shields.io/github/stars/BenEdridge/CVE-2023-30533.svg) ![forks](https://img.shields.io/github/forks/BenEdridge/CVE-2023-30533.svg)

## CVE-2023-30459
 SmartPTT SCADA 1.1.0.0 allows remote code execution (when the attacker has administrator privileges) by writing a malicious C# script and executing it on the server (via server settings in the administrator control panel on port 8101, by default).



- [https://github.com/Toxich4/CVE-2023-30459](https://github.com/Toxich4/CVE-2023-30459) :  ![starts](https://img.shields.io/github/stars/Toxich4/CVE-2023-30459.svg) ![forks](https://img.shields.io/github/forks/Toxich4/CVE-2023-30459.svg)

## CVE-2023-30458
 A username enumeration issue was discovered in Medicine Tracker System 1.0. The login functionality allows a malicious user to guess a valid username due to a different response time from invalid usernames. When one enters a valid username, the response time increases depending on the length of the supplied password.



- [https://github.com/d34dun1c02n/CVE-2023-30458](https://github.com/d34dun1c02n/CVE-2023-30458) :  ![starts](https://img.shields.io/github/stars/d34dun1c02n/CVE-2023-30458.svg) ![forks](https://img.shields.io/github/forks/d34dun1c02n/CVE-2023-30458.svg)

## CVE-2023-30383
 TP-LINK Archer C50v2 Archer C50(US)_V2_160801, TP-LINK Archer C20v1 Archer_C20_V1_150707, and TP-LINK Archer C2v1 Archer_C2_US__V1_170228 were discovered to contain a buffer overflow which may lead to a Denial of Service (DoS) when parsing crafted data.



- [https://github.com/a2ure123/CVE-2023-30383](https://github.com/a2ure123/CVE-2023-30383) :  ![starts](https://img.shields.io/github/stars/a2ure123/CVE-2023-30383.svg) ![forks](https://img.shields.io/github/forks/a2ure123/CVE-2023-30383.svg)

## CVE-2023-30367
 Multi-Remote Next Generation Connection Manager (mRemoteNG) is free software that enables users to store and manage multi-protocol connection configurations to remotely connect to systems. mRemoteNG configuration files can be stored in an encrypted state on disk. mRemoteNG version = v1.76.20 and = 1.77.3-dev loads configuration files in plain text into memory (after decrypting them if necessary) at application start-up, even if no connection has been established yet. This allows attackers to access contents of configuration files in plain text through a memory dump and thus compromise user credentials when no custom password encryption key has been set. This also bypasses the connection configuration file encryption setting by dumping already decrypted configurations from memory.



- [https://github.com/S1lkys/CVE-2023-30367-mRemoteNG-password-dumper](https://github.com/S1lkys/CVE-2023-30367-mRemoteNG-password-dumper) :  ![starts](https://img.shields.io/github/stars/S1lkys/CVE-2023-30367-mRemoteNG-password-dumper.svg) ![forks](https://img.shields.io/github/forks/S1lkys/CVE-2023-30367-mRemoteNG-password-dumper.svg)

## CVE-2023-30347
 Cross Site Scripting (XSS) vulnerability in Neox Contact Center 2.3.9, via the serach_sms_api_name parameter to the SMA API search.



- [https://github.com/huzefa2212/CVE-2023-30347](https://github.com/huzefa2212/CVE-2023-30347) :  ![starts](https://img.shields.io/github/stars/huzefa2212/CVE-2023-30347.svg) ![forks](https://img.shields.io/github/forks/huzefa2212/CVE-2023-30347.svg)

## CVE-2023-30258
 Command Injection vulnerability in MagnusSolution magnusbilling 6.x and 7.x allows remote attackers to run arbitrary commands via unauthenticated HTTP request.



- [https://github.com/AdityaBhatt3010/TryHackMe-Room-Walkthrough-Billing](https://github.com/AdityaBhatt3010/TryHackMe-Room-Walkthrough-Billing) :  ![starts](https://img.shields.io/github/stars/AdityaBhatt3010/TryHackMe-Room-Walkthrough-Billing.svg) ![forks](https://img.shields.io/github/forks/AdityaBhatt3010/TryHackMe-Room-Walkthrough-Billing.svg)

- [https://github.com/gy741/CVE-2023-30258-setup](https://github.com/gy741/CVE-2023-30258-setup) :  ![starts](https://img.shields.io/github/stars/gy741/CVE-2023-30258-setup.svg) ![forks](https://img.shields.io/github/forks/gy741/CVE-2023-30258-setup.svg)

## CVE-2023-30256
 Cross Site Scripting vulnerability found in Webkil QloApps v.1.5.2 allows a remote attacker to obtain sensitive information via the back and email_create parameters in the AuthController.php file.



- [https://github.com/ahrixia/CVE-2023-30256](https://github.com/ahrixia/CVE-2023-30256) :  ![starts](https://img.shields.io/github/stars/ahrixia/CVE-2023-30256.svg) ![forks](https://img.shields.io/github/forks/ahrixia/CVE-2023-30256.svg)

## CVE-2023-30253
 Dolibarr before 17.0.1 allows remote code execution by an authenticated user via an uppercase manipulation: ?PHP instead of ?php in injected data.



- [https://github.com/nikn0laty/Exploit-for-Dolibarr-17.0.0-CVE-2023-30253](https://github.com/nikn0laty/Exploit-for-Dolibarr-17.0.0-CVE-2023-30253) :  ![starts](https://img.shields.io/github/stars/nikn0laty/Exploit-for-Dolibarr-17.0.0-CVE-2023-30253.svg) ![forks](https://img.shields.io/github/forks/nikn0laty/Exploit-for-Dolibarr-17.0.0-CVE-2023-30253.svg)

- [https://github.com/dollarboysushil/Dolibarr-17.0.0-Exploit-CVE-2023-30253](https://github.com/dollarboysushil/Dolibarr-17.0.0-Exploit-CVE-2023-30253) :  ![starts](https://img.shields.io/github/stars/dollarboysushil/Dolibarr-17.0.0-Exploit-CVE-2023-30253.svg) ![forks](https://img.shields.io/github/forks/dollarboysushil/Dolibarr-17.0.0-Exploit-CVE-2023-30253.svg)

- [https://github.com/Rubikcuv5/cve-2023-30253](https://github.com/Rubikcuv5/cve-2023-30253) :  ![starts](https://img.shields.io/github/stars/Rubikcuv5/cve-2023-30253.svg) ![forks](https://img.shields.io/github/forks/Rubikcuv5/cve-2023-30253.svg)

- [https://github.com/g4nkd/CVE-2023-30253-PoC](https://github.com/g4nkd/CVE-2023-30253-PoC) :  ![starts](https://img.shields.io/github/stars/g4nkd/CVE-2023-30253-PoC.svg) ![forks](https://img.shields.io/github/forks/g4nkd/CVE-2023-30253-PoC.svg)

- [https://github.com/andria-dev/DolibabyPhp](https://github.com/andria-dev/DolibabyPhp) :  ![starts](https://img.shields.io/github/stars/andria-dev/DolibabyPhp.svg) ![forks](https://img.shields.io/github/forks/andria-dev/DolibabyPhp.svg)

- [https://github.com/04Shivam/CVE-2023-30253-Exploit](https://github.com/04Shivam/CVE-2023-30253-Exploit) :  ![starts](https://img.shields.io/github/stars/04Shivam/CVE-2023-30253-Exploit.svg) ![forks](https://img.shields.io/github/forks/04Shivam/CVE-2023-30253-Exploit.svg)

## CVE-2023-30226
 An issue was discovered in function get_gnu_verneed in rizinorg Rizin prior to 0.5.0 verneed_entry allows attackers to cause a denial of service via crafted elf file.



- [https://github.com/ifyGecko/CVE-2023-30226](https://github.com/ifyGecko/CVE-2023-30226) :  ![starts](https://img.shields.io/github/stars/ifyGecko/CVE-2023-30226.svg) ![forks](https://img.shields.io/github/forks/ifyGecko/CVE-2023-30226.svg)

## CVE-2023-30212
 OURPHP = 7.2.0 is vulnerale to Cross Site Scripting (XSS) via /client/manage/ourphp_out.php.



- [https://github.com/libasmon/Exploite-CVE-2023-30212-Vulnerability](https://github.com/libasmon/Exploite-CVE-2023-30212-Vulnerability) :  ![starts](https://img.shields.io/github/stars/libasmon/Exploite-CVE-2023-30212-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/libasmon/Exploite-CVE-2023-30212-Vulnerability.svg)

- [https://github.com/kuttappu123/CVE-2023-30212-LAB](https://github.com/kuttappu123/CVE-2023-30212-LAB) :  ![starts](https://img.shields.io/github/stars/kuttappu123/CVE-2023-30212-LAB.svg) ![forks](https://img.shields.io/github/forks/kuttappu123/CVE-2023-30212-LAB.svg)

- [https://github.com/VisDev23/Vulnerable-Docker--CVE-2023-30212-](https://github.com/VisDev23/Vulnerable-Docker--CVE-2023-30212-) :  ![starts](https://img.shields.io/github/stars/VisDev23/Vulnerable-Docker--CVE-2023-30212-.svg) ![forks](https://img.shields.io/github/forks/VisDev23/Vulnerable-Docker--CVE-2023-30212-.svg)

- [https://github.com/Rishipatidar/CVE-2023-30212-POC-DOCKER-FILE](https://github.com/Rishipatidar/CVE-2023-30212-POC-DOCKER-FILE) :  ![starts](https://img.shields.io/github/stars/Rishipatidar/CVE-2023-30212-POC-DOCKER-FILE.svg) ![forks](https://img.shields.io/github/forks/Rishipatidar/CVE-2023-30212-POC-DOCKER-FILE.svg)

- [https://github.com/libas7994/CVE-2023-30212](https://github.com/libas7994/CVE-2023-30212) :  ![starts](https://img.shields.io/github/stars/libas7994/CVE-2023-30212.svg) ![forks](https://img.shields.io/github/forks/libas7994/CVE-2023-30212.svg)

- [https://github.com/AAsh035/CVE-2023-30212](https://github.com/AAsh035/CVE-2023-30212) :  ![starts](https://img.shields.io/github/stars/AAsh035/CVE-2023-30212.svg) ![forks](https://img.shields.io/github/forks/AAsh035/CVE-2023-30212.svg)

- [https://github.com/sungmin20/cve-2023-30212](https://github.com/sungmin20/cve-2023-30212) :  ![starts](https://img.shields.io/github/stars/sungmin20/cve-2023-30212.svg) ![forks](https://img.shields.io/github/forks/sungmin20/cve-2023-30212.svg)

- [https://github.com/libas7994/Exploit-the-CVE-2023-30212-vulnerability](https://github.com/libas7994/Exploit-the-CVE-2023-30212-vulnerability) :  ![starts](https://img.shields.io/github/stars/libas7994/Exploit-the-CVE-2023-30212-vulnerability.svg) ![forks](https://img.shields.io/github/forks/libas7994/Exploit-the-CVE-2023-30212-vulnerability.svg)

- [https://github.com/libasv/Exploite-CVE-2023-30212-vulnerability](https://github.com/libasv/Exploite-CVE-2023-30212-vulnerability) :  ![starts](https://img.shields.io/github/stars/libasv/Exploite-CVE-2023-30212-vulnerability.svg) ![forks](https://img.shields.io/github/forks/libasv/Exploite-CVE-2023-30212-vulnerability.svg)

- [https://github.com/kai-iszz/CVE-2023-30212](https://github.com/kai-iszz/CVE-2023-30212) :  ![starts](https://img.shields.io/github/stars/kai-iszz/CVE-2023-30212.svg) ![forks](https://img.shields.io/github/forks/kai-iszz/CVE-2023-30212.svg)

- [https://github.com/arunsnap/CVE-2023-30212-POC](https://github.com/arunsnap/CVE-2023-30212-POC) :  ![starts](https://img.shields.io/github/stars/arunsnap/CVE-2023-30212-POC.svg) ![forks](https://img.shields.io/github/forks/arunsnap/CVE-2023-30212-POC.svg)

- [https://github.com/mallutrojan/CVE-2023-30212-Lab](https://github.com/mallutrojan/CVE-2023-30212-Lab) :  ![starts](https://img.shields.io/github/stars/mallutrojan/CVE-2023-30212-Lab.svg) ![forks](https://img.shields.io/github/forks/mallutrojan/CVE-2023-30212-Lab.svg)

- [https://github.com/Anandhu990/CVE-2023-30212-iab](https://github.com/Anandhu990/CVE-2023-30212-iab) :  ![starts](https://img.shields.io/github/stars/Anandhu990/CVE-2023-30212-iab.svg) ![forks](https://img.shields.io/github/forks/Anandhu990/CVE-2023-30212-iab.svg)

- [https://github.com/Anandhu990/CVE-2023-30212_lab](https://github.com/Anandhu990/CVE-2023-30212_lab) :  ![starts](https://img.shields.io/github/stars/Anandhu990/CVE-2023-30212_lab.svg) ![forks](https://img.shields.io/github/forks/Anandhu990/CVE-2023-30212_lab.svg)

- [https://github.com/Anandhu990/r-CVE-2023-30212-lab](https://github.com/Anandhu990/r-CVE-2023-30212-lab) :  ![starts](https://img.shields.io/github/stars/Anandhu990/r-CVE-2023-30212-lab.svg) ![forks](https://img.shields.io/github/forks/Anandhu990/r-CVE-2023-30212-lab.svg)

- [https://github.com/Anandhu990/r-CVE-2023-30212--lab](https://github.com/Anandhu990/r-CVE-2023-30212--lab) :  ![starts](https://img.shields.io/github/stars/Anandhu990/r-CVE-2023-30212--lab.svg) ![forks](https://img.shields.io/github/forks/Anandhu990/r-CVE-2023-30212--lab.svg)

- [https://github.com/MaThEw-ViNcEnT/CVE-2023-30212-OURPHP-Vulnerability](https://github.com/MaThEw-ViNcEnT/CVE-2023-30212-OURPHP-Vulnerability) :  ![starts](https://img.shields.io/github/stars/MaThEw-ViNcEnT/CVE-2023-30212-OURPHP-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/MaThEw-ViNcEnT/CVE-2023-30212-OURPHP-Vulnerability.svg)

- [https://github.com/libasmon/Vulnerable-Docker-Environment-CVE-2023-30212](https://github.com/libasmon/Vulnerable-Docker-Environment-CVE-2023-30212) :  ![starts](https://img.shields.io/github/stars/libasmon/Vulnerable-Docker-Environment-CVE-2023-30212.svg) ![forks](https://img.shields.io/github/forks/libasmon/Vulnerable-Docker-Environment-CVE-2023-30212.svg)

- [https://github.com/JasaluRah/Creating-a-Vulnerable-Docker-Environment-CVE-2023-30212-](https://github.com/JasaluRah/Creating-a-Vulnerable-Docker-Environment-CVE-2023-30212-) :  ![starts](https://img.shields.io/github/stars/JasaluRah/Creating-a-Vulnerable-Docker-Environment-CVE-2023-30212-.svg) ![forks](https://img.shields.io/github/forks/JasaluRah/Creating-a-Vulnerable-Docker-Environment-CVE-2023-30212-.svg)

- [https://github.com/libasmon/-create-a-vulnerable-Docker-environment-that-is-susceptible-to-CVE-2023-30212](https://github.com/libasmon/-create-a-vulnerable-Docker-environment-that-is-susceptible-to-CVE-2023-30212) :  ![starts](https://img.shields.io/github/stars/libasmon/-create-a-vulnerable-Docker-environment-that-is-susceptible-to-CVE-2023-30212.svg) ![forks](https://img.shields.io/github/forks/libasmon/-create-a-vulnerable-Docker-environment-that-is-susceptible-to-CVE-2023-30212.svg)

## CVE-2023-30190
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/MojithaR/CVE-2023-30190-FOLLINA](https://github.com/MojithaR/CVE-2023-30190-FOLLINA) :  ![starts](https://img.shields.io/github/stars/MojithaR/CVE-2023-30190-FOLLINA.svg) ![forks](https://img.shields.io/github/forks/MojithaR/CVE-2023-30190-FOLLINA.svg)

## CVE-2023-30185
 CRMEB v4.4 to v4.6 was discovered to contain an arbitrary file upload vulnerability via the component \attachment\SystemAttachmentServices.php.



- [https://github.com/c7w1n/CVE-2023-30185](https://github.com/c7w1n/CVE-2023-30185) :  ![starts](https://img.shields.io/github/stars/c7w1n/CVE-2023-30185.svg) ![forks](https://img.shields.io/github/forks/c7w1n/CVE-2023-30185.svg)

## CVE-2023-30146
 Assmann Digitus Plug&View IP Camera HT-IP211HDP, version 2.000.022 allows unauthenticated attackers to download a copy of the camera's settings and the administrator credentials.



- [https://github.com/L1-0/CVE-2023-30146](https://github.com/L1-0/CVE-2023-30146) :  ![starts](https://img.shields.io/github/stars/L1-0/CVE-2023-30146.svg) ![forks](https://img.shields.io/github/forks/L1-0/CVE-2023-30146.svg)

## CVE-2023-30145
 Camaleon CMS v2.7.0 was discovered to contain a Server-Side Template Injection (SSTI) vulnerability via the formats parameter.



- [https://github.com/paragbagul111/CVE-2023-30145](https://github.com/paragbagul111/CVE-2023-30145) :  ![starts](https://img.shields.io/github/stars/paragbagul111/CVE-2023-30145.svg) ![forks](https://img.shields.io/github/forks/paragbagul111/CVE-2023-30145.svg)

## CVE-2023-30092
 SourceCodester Online Pizza Ordering System v1.0 is vulnerable to SQL Injection via the QTY parameter.



- [https://github.com/nawed20002/CVE-2023-30092](https://github.com/nawed20002/CVE-2023-30092) :  ![starts](https://img.shields.io/github/stars/nawed20002/CVE-2023-30092.svg) ![forks](https://img.shields.io/github/forks/nawed20002/CVE-2023-30092.svg)

## CVE-2023-30033
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/phucodeexp/CVE-2023-30033](https://github.com/phucodeexp/CVE-2023-30033) :  ![starts](https://img.shields.io/github/stars/phucodeexp/CVE-2023-30033.svg) ![forks](https://img.shields.io/github/forks/phucodeexp/CVE-2023-30033.svg)

## CVE-2023-29983
 Cross Site Scripting vulnerability found in Maximilian Vogt cmaps v.8.0 allows a remote attacker to execute arbitrary code via the auditlog tab in the admin panel.



- [https://github.com/zPrototype/CVE-2023-29983](https://github.com/zPrototype/CVE-2023-29983) :  ![starts](https://img.shields.io/github/stars/zPrototype/CVE-2023-29983.svg) ![forks](https://img.shields.io/github/forks/zPrototype/CVE-2023-29983.svg)

## CVE-2023-29929
 Buffer Overflow vulnerability found in Kemptechnologies Loadmaster before v.7.2.60.0 allows a remote attacker to casue a denial of service via the libkemplink.so, isreverse library.



- [https://github.com/YSaxon/CVE-2023-29929](https://github.com/YSaxon/CVE-2023-29929) :  ![starts](https://img.shields.io/github/stars/YSaxon/CVE-2023-29929.svg) ![forks](https://img.shields.io/github/forks/YSaxon/CVE-2023-29929.svg)

## CVE-2023-29923
 PowerJob V4.3.1 is vulnerable to Insecure Permissions. via the list job interface.



- [https://github.com/1820112015/CVE-2023-29923](https://github.com/1820112015/CVE-2023-29923) :  ![starts](https://img.shields.io/github/stars/1820112015/CVE-2023-29923.svg) ![forks](https://img.shields.io/github/forks/1820112015/CVE-2023-29923.svg)

- [https://github.com/P4x1s/CVE-2023-29923-Scan](https://github.com/P4x1s/CVE-2023-29923-Scan) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2023-29923-Scan.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2023-29923-Scan.svg)

- [https://github.com/Le1a/CVE-2023-29923](https://github.com/Le1a/CVE-2023-29923) :  ![starts](https://img.shields.io/github/stars/Le1a/CVE-2023-29923.svg) ![forks](https://img.shields.io/github/forks/Le1a/CVE-2023-29923.svg)

## CVE-2023-29922
 PowerJob V4.3.1 is vulnerable to Incorrect Access Control via the create user/save interface.



- [https://github.com/1820112015/CVE-2023-29923](https://github.com/1820112015/CVE-2023-29923) :  ![starts](https://img.shields.io/github/stars/1820112015/CVE-2023-29923.svg) ![forks](https://img.shields.io/github/forks/1820112015/CVE-2023-29923.svg)

- [https://github.com/P4x1s/CVE-2023-29923-Scan](https://github.com/P4x1s/CVE-2023-29923-Scan) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2023-29923-Scan.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2023-29923-Scan.svg)

- [https://github.com/CN016/Powerjob-CVE-2023-29922-](https://github.com/CN016/Powerjob-CVE-2023-29922-) :  ![starts](https://img.shields.io/github/stars/CN016/Powerjob-CVE-2023-29922-.svg) ![forks](https://img.shields.io/github/forks/CN016/Powerjob-CVE-2023-29922-.svg)

## CVE-2023-29919
 SolarView Compact = 6.0 is vulnerable to Insecure Permissions. Any file on the server can be read or modified because texteditor.php is not restricted.



- [https://github.com/xiaosed/CVE-2023-29919](https://github.com/xiaosed/CVE-2023-29919) :  ![starts](https://img.shields.io/github/stars/xiaosed/CVE-2023-29919.svg) ![forks](https://img.shields.io/github/forks/xiaosed/CVE-2023-29919.svg)

## CVE-2023-29839
 A Stored Cross Site Scripting (XSS) vulnerability exists in multiple pages of Hotel Druid version 3.0.4, which allows arbitrary execution of commands. The vulnerable fields are Surname, Name, and Nickname in the Document function.



- [https://github.com/jichngan/CVE-2023-29839](https://github.com/jichngan/CVE-2023-29839) :  ![starts](https://img.shields.io/github/stars/jichngan/CVE-2023-29839.svg) ![forks](https://img.shields.io/github/forks/jichngan/CVE-2023-29839.svg)

## CVE-2023-29809
 SQL injection vulnerability found in Maximilian Vogt companymaps (cmaps) v.8.0 allows a remote attacker to execute arbitrary code via a crafted script in the request.



- [https://github.com/zPrototype/CVE-2023-29809](https://github.com/zPrototype/CVE-2023-29809) :  ![starts](https://img.shields.io/github/stars/zPrototype/CVE-2023-29809.svg) ![forks](https://img.shields.io/github/forks/zPrototype/CVE-2023-29809.svg)

## CVE-2023-29808
 Cross Site Scripting (XSS) vulnerability in vogtmh cmaps (companymaps) 8.0 allows attackers to execute arbitrary code.



- [https://github.com/zPrototype/CVE-2023-29808](https://github.com/zPrototype/CVE-2023-29808) :  ![starts](https://img.shields.io/github/stars/zPrototype/CVE-2023-29808.svg) ![forks](https://img.shields.io/github/forks/zPrototype/CVE-2023-29808.svg)

## CVE-2023-29489
 An issue was discovered in cPanel before 11.109.9999.116. XSS can occur on the cpsrvd error page via an invalid webcall ID, aka SEC-669. The fixed versions are 11.109.9999.116, 11.108.0.13, 11.106.0.18, and 11.102.0.31.



- [https://github.com/0-d3y/CVE-2023-29489](https://github.com/0-d3y/CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/0-d3y/CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/0-d3y/CVE-2023-29489.svg)

- [https://github.com/whalebone7/EagleEye](https://github.com/whalebone7/EagleEye) :  ![starts](https://img.shields.io/github/stars/whalebone7/EagleEye.svg) ![forks](https://img.shields.io/github/forks/whalebone7/EagleEye.svg)

- [https://github.com/mdaseem03/cpanel_xss_2023](https://github.com/mdaseem03/cpanel_xss_2023) :  ![starts](https://img.shields.io/github/stars/mdaseem03/cpanel_xss_2023.svg) ![forks](https://img.shields.io/github/forks/mdaseem03/cpanel_xss_2023.svg)

- [https://github.com/xKore123/cPanel-CVE-2023-29489](https://github.com/xKore123/cPanel-CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/xKore123/cPanel-CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/xKore123/cPanel-CVE-2023-29489.svg)

- [https://github.com/ipk1/CVE-2023-29489.py](https://github.com/ipk1/CVE-2023-29489.py) :  ![starts](https://img.shields.io/github/stars/ipk1/CVE-2023-29489.py.svg) ![forks](https://img.shields.io/github/forks/ipk1/CVE-2023-29489.py.svg)

- [https://github.com/Makurorororororororo/Validate-CVE-2023-29489-scanner-](https://github.com/Makurorororororororo/Validate-CVE-2023-29489-scanner-) :  ![starts](https://img.shields.io/github/stars/Makurorororororororo/Validate-CVE-2023-29489-scanner-.svg) ![forks](https://img.shields.io/github/forks/Makurorororororororo/Validate-CVE-2023-29489-scanner-.svg)

- [https://github.com/Thuankobtcode/CVE-2023-29489](https://github.com/Thuankobtcode/CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/Thuankobtcode/CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/Thuankobtcode/CVE-2023-29489.svg)

- [https://github.com/Abdullah7-ma/CVE-2023-29489](https://github.com/Abdullah7-ma/CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/Abdullah7-ma/CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/Abdullah7-ma/CVE-2023-29489.svg)

- [https://github.com/some-man1/CVE-2023-29489](https://github.com/some-man1/CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/some-man1/CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/some-man1/CVE-2023-29489.svg)

- [https://github.com/tucommenceapousser/CVE-2023-29489](https://github.com/tucommenceapousser/CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/tucommenceapousser/CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/tucommenceapousser/CVE-2023-29489.svg)

- [https://github.com/md-thalal/CVE-2023-29489](https://github.com/md-thalal/CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/md-thalal/CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/md-thalal/CVE-2023-29489.svg)

- [https://github.com/Mostafa-Elguerdawi/CVE-2023-29489](https://github.com/Mostafa-Elguerdawi/CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/Mostafa-Elguerdawi/CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/Mostafa-Elguerdawi/CVE-2023-29489.svg)

- [https://github.com/Cappricio-Securities/CVE-2023-29489](https://github.com/Cappricio-Securities/CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2023-29489.svg)

- [https://github.com/SynixCyberCrimeMy/CVE-2023-29489](https://github.com/SynixCyberCrimeMy/CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/SynixCyberCrimeMy/CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/SynixCyberCrimeMy/CVE-2023-29489.svg)

- [https://github.com/learnerboy88/CVE-2023-29489](https://github.com/learnerboy88/CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/learnerboy88/CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/learnerboy88/CVE-2023-29489.svg)

- [https://github.com/ViperM4sk/cpanel-xss-177](https://github.com/ViperM4sk/cpanel-xss-177) :  ![starts](https://img.shields.io/github/stars/ViperM4sk/cpanel-xss-177.svg) ![forks](https://img.shields.io/github/forks/ViperM4sk/cpanel-xss-177.svg)

- [https://github.com/S4muraiMelayu1337/CVE-2023-29489](https://github.com/S4muraiMelayu1337/CVE-2023-29489) :  ![starts](https://img.shields.io/github/stars/S4muraiMelayu1337/CVE-2023-29489.svg) ![forks](https://img.shields.io/github/forks/S4muraiMelayu1337/CVE-2023-29489.svg)

- [https://github.com/tucommenceapousser/CVE-2023-29489.py](https://github.com/tucommenceapousser/CVE-2023-29489.py) :  ![starts](https://img.shields.io/github/stars/tucommenceapousser/CVE-2023-29489.py.svg) ![forks](https://img.shields.io/github/forks/tucommenceapousser/CVE-2023-29489.py.svg)

- [https://github.com/Mostafa-Elguerdawi/CVE-2023-29489.yaml](https://github.com/Mostafa-Elguerdawi/CVE-2023-29489.yaml) :  ![starts](https://img.shields.io/github/stars/Mostafa-Elguerdawi/CVE-2023-29489.yaml.svg) ![forks](https://img.shields.io/github/forks/Mostafa-Elguerdawi/CVE-2023-29489.yaml.svg)

- [https://github.com/prasad-1808/tool-29489](https://github.com/prasad-1808/tool-29489) :  ![starts](https://img.shields.io/github/stars/prasad-1808/tool-29489.svg) ![forks](https://img.shields.io/github/forks/prasad-1808/tool-29489.svg)

## CVE-2023-29484
 In Terminalfour before 8.3.16, misconfigured LDAP users are able to login with an invalid password.



- [https://github.com/SangPenyalang/CVE2023-29484](https://github.com/SangPenyalang/CVE2023-29484) :  ![starts](https://img.shields.io/github/stars/SangPenyalang/CVE2023-29484.svg) ![forks](https://img.shields.io/github/forks/SangPenyalang/CVE2023-29484.svg)

## CVE-2023-29478
 BiblioCraft before 2.4.6 does not sanitize path-traversal characters in filenames, allowing restricted write access to almost anywhere on the filesystem. This includes the Minecraft mods folder, which results in code execution.



- [https://github.com/Exopteron/BiblioRCE](https://github.com/Exopteron/BiblioRCE) :  ![starts](https://img.shields.io/github/stars/Exopteron/BiblioRCE.svg) ![forks](https://img.shields.io/github/forks/Exopteron/BiblioRCE.svg)

## CVE-2023-29439
 Unauth. Reflected Cross-Site Scripting (XSS) vulnerability in FooPlugins FooGallery plugin = 2.2.35 versions.



- [https://github.com/LOURC0D3/CVE-2023-29439](https://github.com/LOURC0D3/CVE-2023-29439) :  ![starts](https://img.shields.io/github/stars/LOURC0D3/CVE-2023-29439.svg) ![forks](https://img.shields.io/github/forks/LOURC0D3/CVE-2023-29439.svg)

## CVE-2023-29421
 An issue was discovered in libbzip3.a in bzip3 before 1.2.3. There is an out-of-bounds write in bz3_decode_block.



- [https://github.com/MarcusGutierrez/complex-vulnerabilities](https://github.com/MarcusGutierrez/complex-vulnerabilities) :  ![starts](https://img.shields.io/github/stars/MarcusGutierrez/complex-vulnerabilities.svg) ![forks](https://img.shields.io/github/forks/MarcusGutierrez/complex-vulnerabilities.svg)

## CVE-2023-29409
 Extremely large RSA keys in certificate chains can cause a client/server to expend significant CPU time verifying signatures. With fix, the size of RSA keys transmitted during handshakes is restricted to = 8192 bits. Based on a survey of publicly trusted RSA keys, there are currently only three certificates in circulation with keys larger than this, and all three appear to be test certificates that are not actively deployed. It is possible there are larger keys in use in private PKIs, but we target the web PKI, so causing breakage here in the interests of increasing the default safety of users of crypto/tls seems reasonable.



- [https://github.com/mateusz834/CVE-2023-29409](https://github.com/mateusz834/CVE-2023-29409) :  ![starts](https://img.shields.io/github/stars/mateusz834/CVE-2023-29409.svg) ![forks](https://img.shields.io/github/forks/mateusz834/CVE-2023-29409.svg)

## CVE-2023-29406
 The HTTP/1 client does not fully validate the contents of the Host header. A maliciously crafted Host header can inject additional headers or entire requests. With fix, the HTTP/1 client now refuses to send requests containing an invalid Request.Host or Request.URL.Host value.



- [https://github.com/LuizGustavoP/EP3_Redes](https://github.com/LuizGustavoP/EP3_Redes) :  ![starts](https://img.shields.io/github/stars/LuizGustavoP/EP3_Redes.svg) ![forks](https://img.shields.io/github/forks/LuizGustavoP/EP3_Redes.svg)

## CVE-2023-29374
 In LangChain through 0.0.131, the LLMMathChain chain allows prompt injection attacks that can execute arbitrary code via the Python exec method.



- [https://github.com/ckloh720/cve2023-29374](https://github.com/ckloh720/cve2023-29374) :  ![starts](https://img.shields.io/github/stars/ckloh720/cve2023-29374.svg) ![forks](https://img.shields.io/github/forks/ckloh720/cve2023-29374.svg)

## CVE-2023-29360
 Microsoft Streaming Service Elevation of Privilege Vulnerability



- [https://github.com/Nero22k/cve-2023-29360](https://github.com/Nero22k/cve-2023-29360) :  ![starts](https://img.shields.io/github/stars/Nero22k/cve-2023-29360.svg) ![forks](https://img.shields.io/github/forks/Nero22k/cve-2023-29360.svg)

## CVE-2023-29357
 Microsoft SharePoint Server Elevation of Privilege Vulnerability



- [https://github.com/Chocapikk/CVE-2023-29357](https://github.com/Chocapikk/CVE-2023-29357) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-29357.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-29357.svg)

- [https://github.com/LuemmelSec/CVE-2023-29357](https://github.com/LuemmelSec/CVE-2023-29357) :  ![starts](https://img.shields.io/github/stars/LuemmelSec/CVE-2023-29357.svg) ![forks](https://img.shields.io/github/forks/LuemmelSec/CVE-2023-29357.svg)

- [https://github.com/Guillaume-Risch/cve-2023-29357-Sharepoint](https://github.com/Guillaume-Risch/cve-2023-29357-Sharepoint) :  ![starts](https://img.shields.io/github/stars/Guillaume-Risch/cve-2023-29357-Sharepoint.svg) ![forks](https://img.shields.io/github/forks/Guillaume-Risch/cve-2023-29357-Sharepoint.svg)

- [https://github.com/Jev1337/CVE-2023-29357-Check](https://github.com/Jev1337/CVE-2023-29357-Check) :  ![starts](https://img.shields.io/github/stars/Jev1337/CVE-2023-29357-Check.svg) ![forks](https://img.shields.io/github/forks/Jev1337/CVE-2023-29357-Check.svg)

- [https://github.com/KeyStrOke95/CVE-2023-29357-ExE](https://github.com/KeyStrOke95/CVE-2023-29357-ExE) :  ![starts](https://img.shields.io/github/stars/KeyStrOke95/CVE-2023-29357-ExE.svg) ![forks](https://img.shields.io/github/forks/KeyStrOke95/CVE-2023-29357-ExE.svg)

## CVE-2023-29343
 SysInternals Sysmon for Windows Elevation of Privilege Vulnerability



- [https://github.com/Wh04m1001/CVE-2023-29343](https://github.com/Wh04m1001/CVE-2023-29343) :  ![starts](https://img.shields.io/github/stars/Wh04m1001/CVE-2023-29343.svg) ![forks](https://img.shields.io/github/forks/Wh04m1001/CVE-2023-29343.svg)

## CVE-2023-29336
 Win32k Elevation of Privilege Vulnerability



- [https://github.com/m-cetin/CVE-2023-29336](https://github.com/m-cetin/CVE-2023-29336) :  ![starts](https://img.shields.io/github/stars/m-cetin/CVE-2023-29336.svg) ![forks](https://img.shields.io/github/forks/m-cetin/CVE-2023-29336.svg)

## CVE-2023-29325
 Windows OLE Remote Code Execution Vulnerability



- [https://github.com/a-bazi/test-CVE-2023-29325](https://github.com/a-bazi/test-CVE-2023-29325) :  ![starts](https://img.shields.io/github/stars/a-bazi/test-CVE-2023-29325.svg) ![forks](https://img.shields.io/github/forks/a-bazi/test-CVE-2023-29325.svg)

- [https://github.com/a-bazi/test2-CVE-2023-29325](https://github.com/a-bazi/test2-CVE-2023-29325) :  ![starts](https://img.shields.io/github/stars/a-bazi/test2-CVE-2023-29325.svg) ![forks](https://img.shields.io/github/forks/a-bazi/test2-CVE-2023-29325.svg)

## CVE-2023-29324
 Windows MSHTML Platform Security Feature Bypass Vulnerability



- [https://github.com/OLeDouxEt/CVE-2023-29324_Patch_Deploy](https://github.com/OLeDouxEt/CVE-2023-29324_Patch_Deploy) :  ![starts](https://img.shields.io/github/stars/OLeDouxEt/CVE-2023-29324_Patch_Deploy.svg) ![forks](https://img.shields.io/github/forks/OLeDouxEt/CVE-2023-29324_Patch_Deploy.svg)

## CVE-2023-29084
 Zoho ManageEngine ADManager Plus before 7181 allows for authenticated users to exploit command injection via Proxy settings.



- [https://github.com/ohnonoyesyes/CVE-2023-29084](https://github.com/ohnonoyesyes/CVE-2023-29084) :  ![starts](https://img.shields.io/github/stars/ohnonoyesyes/CVE-2023-29084.svg) ![forks](https://img.shields.io/github/forks/ohnonoyesyes/CVE-2023-29084.svg)

## CVE-2023-29017
 vm2 is a sandbox that can run untrusted code with whitelisted Node's built-in modules. Prior to version 3.9.15, vm2 was not properly handling host objects passed to `Error.prepareStackTrace` in case of unhandled async errors. A threat actor could bypass the sandbox protections to gain remote code execution rights on the host running the sandbox. This vulnerability was patched in the release of version 3.9.15 of vm2. There are no known workarounds.



- [https://github.com/timb-machine-mirrors/seongil-wi-CVE-2023-29017](https://github.com/timb-machine-mirrors/seongil-wi-CVE-2023-29017) :  ![starts](https://img.shields.io/github/stars/timb-machine-mirrors/seongil-wi-CVE-2023-29017.svg) ![forks](https://img.shields.io/github/forks/timb-machine-mirrors/seongil-wi-CVE-2023-29017.svg)

- [https://github.com/passwa11/CVE-2023-29017-reverse-shell](https://github.com/passwa11/CVE-2023-29017-reverse-shell) :  ![starts](https://img.shields.io/github/stars/passwa11/CVE-2023-29017-reverse-shell.svg) ![forks](https://img.shields.io/github/forks/passwa11/CVE-2023-29017-reverse-shell.svg)

## CVE-2023-29007
 Git is a revision control system. Prior to versions 2.30.9, 2.31.8, 2.32.7, 2.33.8, 2.34.8, 2.35.8, 2.36.6, 2.37.7, 2.38.5, 2.39.3, and 2.40.1, a specially crafted `.gitmodules` file with submodule URLs that are longer than 1024 characters can used to exploit a bug in `config.c::git_config_copy_or_rename_section_in_file()`. This bug can be used to inject arbitrary configuration into a user's `$GIT_DIR/config` when attempting to remove the configuration section associated with that submodule. When the attacker injects configuration values which specify executables to run (such as `core.pager`, `core.editor`, `core.sshCommand`, etc.) this can lead to a remote code execution. A fix A fix is available in versions 2.30.9, 2.31.8, 2.32.7, 2.33.8, 2.34.8, 2.35.8, 2.36.6, 2.37.7, 2.38.5, 2.39.3, and 2.40.1. As a workaround, avoid running `git submodule deinit` on untrusted repositories or without prior inspection of any submodule sections in `$GIT_DIR/config`.



- [https://github.com/ethiack/CVE-2023-29007](https://github.com/ethiack/CVE-2023-29007) :  ![starts](https://img.shields.io/github/stars/ethiack/CVE-2023-29007.svg) ![forks](https://img.shields.io/github/forks/ethiack/CVE-2023-29007.svg)

- [https://github.com/x-Defender/CVE-2023-29007_win-version](https://github.com/x-Defender/CVE-2023-29007_win-version) :  ![starts](https://img.shields.io/github/stars/x-Defender/CVE-2023-29007_win-version.svg) ![forks](https://img.shields.io/github/forks/x-Defender/CVE-2023-29007_win-version.svg)

- [https://github.com/omespino/CVE-2023-29007](https://github.com/omespino/CVE-2023-29007) :  ![starts](https://img.shields.io/github/stars/omespino/CVE-2023-29007.svg) ![forks](https://img.shields.io/github/forks/omespino/CVE-2023-29007.svg)

## CVE-2023-28810
 Some access control/intercom products have unauthorized modification of device network configuration vulnerabilities. Attackers can modify device network configuration by sending specific data packets to the vulnerable interface within the same local network.



- [https://github.com/skylightcyber/CVE-2023-28810](https://github.com/skylightcyber/CVE-2023-28810) :  ![starts](https://img.shields.io/github/stars/skylightcyber/CVE-2023-28810.svg) ![forks](https://img.shields.io/github/forks/skylightcyber/CVE-2023-28810.svg)

## CVE-2023-28772
 An issue was discovered in the Linux kernel before 5.13.3. lib/seq_buf.c has a seq_buf_putmem_hex buffer overflow.



- [https://github.com/Satheesh575555/linux-4.1.15_CVE-2023-28772](https://github.com/Satheesh575555/linux-4.1.15_CVE-2023-28772) :  ![starts](https://img.shields.io/github/stars/Satheesh575555/linux-4.1.15_CVE-2023-28772.svg) ![forks](https://img.shields.io/github/forks/Satheesh575555/linux-4.1.15_CVE-2023-28772.svg)

- [https://github.com/Trinadh465/linux-4.1.15_CVE-2023-28772](https://github.com/Trinadh465/linux-4.1.15_CVE-2023-28772) :  ![starts](https://img.shields.io/github/stars/Trinadh465/linux-4.1.15_CVE-2023-28772.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/linux-4.1.15_CVE-2023-28772.svg)

## CVE-2023-28771
 Improper error message handling in Zyxel ZyWALL/USG series firmware versions 4.60 through 4.73, VPN series firmware versions 4.60 through 5.35, USG FLEX series firmware versions 4.60 through 5.35, and ATP series firmware versions 4.60 through 5.35, which could allow an unauthenticated attacker to execute some OS commands remotely by sending crafted packets to an affected device.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/benjaminhays/CVE-2023-28771-PoC](https://github.com/benjaminhays/CVE-2023-28771-PoC) :  ![starts](https://img.shields.io/github/stars/benjaminhays/CVE-2023-28771-PoC.svg) ![forks](https://img.shields.io/github/forks/benjaminhays/CVE-2023-28771-PoC.svg)

- [https://github.com/JinParkmida/cve-2023-28771-demo](https://github.com/JinParkmida/cve-2023-28771-demo) :  ![starts](https://img.shields.io/github/stars/JinParkmida/cve-2023-28771-demo.svg) ![forks](https://img.shields.io/github/forks/JinParkmida/cve-2023-28771-demo.svg)

## CVE-2023-28588
 Transient DOS in Bluetooth Host while rfc slot allocation.



- [https://github.com/Trinadh465/CVE-2023-28588](https://github.com/Trinadh465/CVE-2023-28588) :  ![starts](https://img.shields.io/github/stars/Trinadh465/CVE-2023-28588.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/CVE-2023-28588.svg)

- [https://github.com/uthrasri/CVE-2023-28588_system_bt](https://github.com/uthrasri/CVE-2023-28588_system_bt) :  ![starts](https://img.shields.io/github/stars/uthrasri/CVE-2023-28588_system_bt.svg) ![forks](https://img.shields.io/github/forks/uthrasri/CVE-2023-28588_system_bt.svg)

- [https://github.com/uthrasri/CVE-2023-28588](https://github.com/uthrasri/CVE-2023-28588) :  ![starts](https://img.shields.io/github/stars/uthrasri/CVE-2023-28588.svg) ![forks](https://img.shields.io/github/forks/uthrasri/CVE-2023-28588.svg)

- [https://github.com/uthrasri/CVE-2023-28588_Singlefile](https://github.com/uthrasri/CVE-2023-28588_Singlefile) :  ![starts](https://img.shields.io/github/stars/uthrasri/CVE-2023-28588_Singlefile.svg) ![forks](https://img.shields.io/github/forks/uthrasri/CVE-2023-28588_Singlefile.svg)

- [https://github.com/uthrasri/G2.5_CVE-2023-28588](https://github.com/uthrasri/G2.5_CVE-2023-28588) :  ![starts](https://img.shields.io/github/stars/uthrasri/G2.5_CVE-2023-28588.svg) ![forks](https://img.shields.io/github/forks/uthrasri/G2.5_CVE-2023-28588.svg)

- [https://github.com/uthrasri/CVE-2023-28588_G2.5_singlefile](https://github.com/uthrasri/CVE-2023-28588_G2.5_singlefile) :  ![starts](https://img.shields.io/github/stars/uthrasri/CVE-2023-28588_G2.5_singlefile.svg) ![forks](https://img.shields.io/github/forks/uthrasri/CVE-2023-28588_G2.5_singlefile.svg)

## CVE-2023-28467
 In MyBB before 1.8.34, there is XSS in the User CP module via the user email field.



- [https://github.com/ahmetaltuntas/CVE-2023-28467](https://github.com/ahmetaltuntas/CVE-2023-28467) :  ![starts](https://img.shields.io/github/stars/ahmetaltuntas/CVE-2023-28467.svg) ![forks](https://img.shields.io/github/forks/ahmetaltuntas/CVE-2023-28467.svg)

## CVE-2023-28447
 Smarty is a template engine for PHP. In affected versions smarty did not properly escape javascript code. An attacker could exploit this vulnerability to execute arbitrary JavaScript code in the context of the user's browser session. This may lead to unauthorized access to sensitive user data, manipulation of the web application's behavior, or unauthorized actions performed on behalf of the user. Users are advised to upgrade to either version 3.1.48 or to 4.3.1 to resolve this issue. There are no known workarounds for this vulnerability.



- [https://github.com/drkbcn/lblfixer_cve_2023_28447](https://github.com/drkbcn/lblfixer_cve_2023_28447) :  ![starts](https://img.shields.io/github/stars/drkbcn/lblfixer_cve_2023_28447.svg) ![forks](https://img.shields.io/github/forks/drkbcn/lblfixer_cve_2023_28447.svg)

## CVE-2023-28434
 Minio is a Multi-Cloud Object Storage framework. Prior to RELEASE.2023-03-20T20-16-18Z, an attacker can use crafted requests to bypass metadata bucket name checking and put an object into any bucket while processing `PostPolicyBucket`. To carry out this attack, the attacker requires credentials with `arn:aws:s3:::*` permission, as well as enabled Console API access. This issue has been patched in RELEASE.2023-03-20T20-16-18Z. As a workaround, enable browser API access and turn off `MINIO_BROWSER=off`. 




- [https://github.com/AbelChe/evil_minio](https://github.com/AbelChe/evil_minio) :  ![starts](https://img.shields.io/github/stars/AbelChe/evil_minio.svg) ![forks](https://img.shields.io/github/forks/AbelChe/evil_minio.svg)

- [https://github.com/Mr-xn/CVE-2023-28432](https://github.com/Mr-xn/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/Mr-xn/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/Mr-xn/CVE-2023-28432.svg)

## CVE-2023-28432
 Minio is a Multi-Cloud Object Storage framework. In a cluster deployment starting with RELEASE.2019-12-17T23-16-33Z and prior to RELEASE.2023-03-20T20-16-18Z, MinIO returns all environment variables, including `MINIO_SECRET_KEY`
and `MINIO_ROOT_PASSWORD`, resulting in information disclosure. All users of distributed deployment are impacted. All users are advised to upgrade to RELEASE.2023-03-20T20-16-18Z.



- [https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance](https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance) :  ![starts](https://img.shields.io/github/stars/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg) ![forks](https://img.shields.io/github/forks/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg)

- [https://github.com/MzzdToT/CVE-2023-28432](https://github.com/MzzdToT/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/MzzdToT/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/MzzdToT/CVE-2023-28432.svg)

- [https://github.com/Mr-xn/CVE-2023-28432](https://github.com/Mr-xn/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/Mr-xn/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/Mr-xn/CVE-2023-28432.svg)

- [https://github.com/acheiii/CVE-2023-28432](https://github.com/acheiii/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/acheiii/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/acheiii/CVE-2023-28432.svg)

- [https://github.com/gobysec/CVE-2023-28432](https://github.com/gobysec/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/gobysec/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/gobysec/CVE-2023-28432.svg)

- [https://github.com/Cuerz/CVE-2023-28432](https://github.com/Cuerz/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/Cuerz/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/Cuerz/CVE-2023-28432.svg)

- [https://github.com/bingtangbanli/VulnerabilityTools](https://github.com/bingtangbanli/VulnerabilityTools) :  ![starts](https://img.shields.io/github/stars/bingtangbanli/VulnerabilityTools.svg) ![forks](https://img.shields.io/github/forks/bingtangbanli/VulnerabilityTools.svg)

- [https://github.com/Okaytc/minio_unauth_check](https://github.com/Okaytc/minio_unauth_check) :  ![starts](https://img.shields.io/github/stars/Okaytc/minio_unauth_check.svg) ![forks](https://img.shields.io/github/forks/Okaytc/minio_unauth_check.svg)

- [https://github.com/yTxZx/CVE-2023-28432](https://github.com/yTxZx/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/yTxZx/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/yTxZx/CVE-2023-28432.svg)

- [https://github.com/Chocapikk/CVE-2023-28432](https://github.com/Chocapikk/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-28432.svg)

- [https://github.com/steponeerror/Cve-2023-28432-](https://github.com/steponeerror/Cve-2023-28432-) :  ![starts](https://img.shields.io/github/stars/steponeerror/Cve-2023-28432-.svg) ![forks](https://img.shields.io/github/forks/steponeerror/Cve-2023-28432-.svg)

- [https://github.com/Romanc9/Gui-poc-test](https://github.com/Romanc9/Gui-poc-test) :  ![starts](https://img.shields.io/github/stars/Romanc9/Gui-poc-test.svg) ![forks](https://img.shields.io/github/forks/Romanc9/Gui-poc-test.svg)

- [https://github.com/xk-mt/CVE-2023-28432](https://github.com/xk-mt/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/xk-mt/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/xk-mt/CVE-2023-28432.svg)

- [https://github.com/BitWiz4rd/CVE-2023-28432](https://github.com/BitWiz4rd/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/BitWiz4rd/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/BitWiz4rd/CVE-2023-28432.svg)

- [https://github.com/netuseradministrator/CVE-2023-28432](https://github.com/netuseradministrator/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/netuseradministrator/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/netuseradministrator/CVE-2023-28432.svg)

- [https://github.com/C1ph3rX13/CVE-2023-28432](https://github.com/C1ph3rX13/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/C1ph3rX13/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/C1ph3rX13/CVE-2023-28432.svg)

- [https://github.com/LHXHL/Minio-CVE-2023-28432](https://github.com/LHXHL/Minio-CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/LHXHL/Minio-CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/LHXHL/Minio-CVE-2023-28432.svg)

- [https://github.com/TaroballzChen/CVE-2023-28432-metasploit-scanner](https://github.com/TaroballzChen/CVE-2023-28432-metasploit-scanner) :  ![starts](https://img.shields.io/github/stars/TaroballzChen/CVE-2023-28432-metasploit-scanner.svg) ![forks](https://img.shields.io/github/forks/TaroballzChen/CVE-2023-28432-metasploit-scanner.svg)

- [https://github.com/unam4/CVE-2023-28432-minio_update_rce](https://github.com/unam4/CVE-2023-28432-minio_update_rce) :  ![starts](https://img.shields.io/github/stars/unam4/CVE-2023-28432-minio_update_rce.svg) ![forks](https://img.shields.io/github/forks/unam4/CVE-2023-28432-minio_update_rce.svg)

- [https://github.com/NET-Flowers/CVE-2023-28432](https://github.com/NET-Flowers/CVE-2023-28432) :  ![starts](https://img.shields.io/github/stars/NET-Flowers/CVE-2023-28432.svg) ![forks](https://img.shields.io/github/forks/NET-Flowers/CVE-2023-28432.svg)

- [https://github.com/h0ng10/CVE-2023-28432_docker](https://github.com/h0ng10/CVE-2023-28432_docker) :  ![starts](https://img.shields.io/github/stars/h0ng10/CVE-2023-28432_docker.svg) ![forks](https://img.shields.io/github/forks/h0ng10/CVE-2023-28432_docker.svg)

- [https://github.com/CHINA-china/MinIO_CVE-2023-28432_EXP](https://github.com/CHINA-china/MinIO_CVE-2023-28432_EXP) :  ![starts](https://img.shields.io/github/stars/CHINA-china/MinIO_CVE-2023-28432_EXP.svg) ![forks](https://img.shields.io/github/forks/CHINA-china/MinIO_CVE-2023-28432_EXP.svg)

## CVE-2023-28354
 An issue was discovered in Opsview Monitor Agent 6.8. An unauthenticated remote attacker can call check_nrpe against affected targets, specifying known NRPE plugins, which in default installations are configured to accept command control characters and pass them to command-line interpreters for NRPE plugin execution. This allows the attacker to escape NRPE plugin execution and execute commands remotely on the target as NT_AUTHORITY\SYSTEM.



- [https://github.com/stormfleet/CVE-2023-28354](https://github.com/stormfleet/CVE-2023-28354) :  ![starts](https://img.shields.io/github/stars/stormfleet/CVE-2023-28354.svg) ![forks](https://img.shields.io/github/forks/stormfleet/CVE-2023-28354.svg)

## CVE-2023-28343
 OS command injection affects Altenergy Power Control Software C1.2.5 via shell metacharacters in the index.php/management/set_timezone timezone parameter, because of set_timezone in models/management_model.php.



- [https://github.com/superzerosec/CVE-2023-28343](https://github.com/superzerosec/CVE-2023-28343) :  ![starts](https://img.shields.io/github/stars/superzerosec/CVE-2023-28343.svg) ![forks](https://img.shields.io/github/forks/superzerosec/CVE-2023-28343.svg)

- [https://github.com/gobysec/CVE-2023-28343](https://github.com/gobysec/CVE-2023-28343) :  ![starts](https://img.shields.io/github/stars/gobysec/CVE-2023-28343.svg) ![forks](https://img.shields.io/github/forks/gobysec/CVE-2023-28343.svg)

- [https://github.com/hba343434/CVE-2023-28343](https://github.com/hba343434/CVE-2023-28343) :  ![starts](https://img.shields.io/github/stars/hba343434/CVE-2023-28343.svg) ![forks](https://img.shields.io/github/forks/hba343434/CVE-2023-28343.svg)

## CVE-2023-28330
 Insufficient sanitizing in backup resulted in an arbitrary file read risk. The capability to access this feature is only available to teachers, managers and admins by default.



- [https://github.com/cli-ish/CVE-2023-28330](https://github.com/cli-ish/CVE-2023-28330) :  ![starts](https://img.shields.io/github/stars/cli-ish/CVE-2023-28330.svg) ![forks](https://img.shields.io/github/forks/cli-ish/CVE-2023-28330.svg)

## CVE-2023-28329
 Insufficient validation of profile field availability condition resulted in an SQL injection risk (by default only available to teachers and managers).



- [https://github.com/cli-ish/CVE-2023-28329](https://github.com/cli-ish/CVE-2023-28329) :  ![starts](https://img.shields.io/github/stars/cli-ish/CVE-2023-28329.svg) ![forks](https://img.shields.io/github/forks/cli-ish/CVE-2023-28329.svg)

## CVE-2023-28303
 Windows Snipping Tool Information Disclosure Vulnerability



- [https://github.com/frankthetank-music/Acropalypse-Multi-Tool](https://github.com/frankthetank-music/Acropalypse-Multi-Tool) :  ![starts](https://img.shields.io/github/stars/frankthetank-music/Acropalypse-Multi-Tool.svg) ![forks](https://img.shields.io/github/forks/frankthetank-music/Acropalypse-Multi-Tool.svg)

- [https://github.com/qixils/AntiCropalypse](https://github.com/qixils/AntiCropalypse) :  ![starts](https://img.shields.io/github/stars/qixils/AntiCropalypse.svg) ![forks](https://img.shields.io/github/forks/qixils/AntiCropalypse.svg)

- [https://github.com/m31r0n/SnipRecover-CLI](https://github.com/m31r0n/SnipRecover-CLI) :  ![starts](https://img.shields.io/github/stars/m31r0n/SnipRecover-CLI.svg) ![forks](https://img.shields.io/github/forks/m31r0n/SnipRecover-CLI.svg)

## CVE-2023-28293
 Windows Kernel Elevation of Privilege Vulnerability



- [https://github.com/HexilionLabs/CVE-2023-28293](https://github.com/HexilionLabs/CVE-2023-28293) :  ![starts](https://img.shields.io/github/stars/HexilionLabs/CVE-2023-28293.svg) ![forks](https://img.shields.io/github/forks/HexilionLabs/CVE-2023-28293.svg)

## CVE-2023-28269
 Windows Boot Manager Security Feature Bypass Vulnerability



- [https://github.com/Wack0/dubiousdisk](https://github.com/Wack0/dubiousdisk) :  ![starts](https://img.shields.io/github/stars/Wack0/dubiousdisk.svg) ![forks](https://img.shields.io/github/forks/Wack0/dubiousdisk.svg)

## CVE-2023-28252
 Windows Common Log File System Driver Elevation of Privilege Vulnerability



- [https://github.com/fortra/CVE-2023-28252](https://github.com/fortra/CVE-2023-28252) :  ![starts](https://img.shields.io/github/stars/fortra/CVE-2023-28252.svg) ![forks](https://img.shields.io/github/forks/fortra/CVE-2023-28252.svg)

- [https://github.com/duck-sec/CVE-2023-28252-Compiled-exe](https://github.com/duck-sec/CVE-2023-28252-Compiled-exe) :  ![starts](https://img.shields.io/github/stars/duck-sec/CVE-2023-28252-Compiled-exe.svg) ![forks](https://img.shields.io/github/forks/duck-sec/CVE-2023-28252-Compiled-exe.svg)

- [https://github.com/byt3n33dl3/CLFS](https://github.com/byt3n33dl3/CLFS) :  ![starts](https://img.shields.io/github/stars/byt3n33dl3/CLFS.svg) ![forks](https://img.shields.io/github/forks/byt3n33dl3/CLFS.svg)

- [https://github.com/bkstephen/Compiled-PoC-Binary-For-CVE-2023-28252](https://github.com/bkstephen/Compiled-PoC-Binary-For-CVE-2023-28252) :  ![starts](https://img.shields.io/github/stars/bkstephen/Compiled-PoC-Binary-For-CVE-2023-28252.svg) ![forks](https://img.shields.io/github/forks/bkstephen/Compiled-PoC-Binary-For-CVE-2023-28252.svg)

- [https://github.com/Danasuley/CVE-2023-28252-](https://github.com/Danasuley/CVE-2023-28252-) :  ![starts](https://img.shields.io/github/stars/Danasuley/CVE-2023-28252-.svg) ![forks](https://img.shields.io/github/forks/Danasuley/CVE-2023-28252-.svg)

- [https://github.com/Vulmatch/CVE-2023-28252](https://github.com/Vulmatch/CVE-2023-28252) :  ![starts](https://img.shields.io/github/stars/Vulmatch/CVE-2023-28252.svg) ![forks](https://img.shields.io/github/forks/Vulmatch/CVE-2023-28252.svg)

- [https://github.com/726232111/CVE-2023-28252](https://github.com/726232111/CVE-2023-28252) :  ![starts](https://img.shields.io/github/stars/726232111/CVE-2023-28252.svg) ![forks](https://img.shields.io/github/forks/726232111/CVE-2023-28252.svg)

## CVE-2023-28249
 Windows Boot Manager Security Feature Bypass Vulnerability



- [https://github.com/Wack0/dubiousdisk](https://github.com/Wack0/dubiousdisk) :  ![starts](https://img.shields.io/github/stars/Wack0/dubiousdisk.svg) ![forks](https://img.shields.io/github/forks/Wack0/dubiousdisk.svg)

## CVE-2023-28244
 Windows Kerberos Elevation of Privilege Vulnerability



- [https://github.com/sk3w/cve-2023-28244](https://github.com/sk3w/cve-2023-28244) :  ![starts](https://img.shields.io/github/stars/sk3w/cve-2023-28244.svg) ![forks](https://img.shields.io/github/forks/sk3w/cve-2023-28244.svg)

## CVE-2023-28231
 DHCP Server Service Remote Code Execution Vulnerability



- [https://github.com/TheHermione/CVE-2023-28231](https://github.com/TheHermione/CVE-2023-28231) :  ![starts](https://img.shields.io/github/stars/TheHermione/CVE-2023-28231.svg) ![forks](https://img.shields.io/github/forks/TheHermione/CVE-2023-28231.svg)

## CVE-2023-28229
 Windows CNG Key Isolation Service Elevation of Privilege Vulnerability



- [https://github.com/Y3A/CVE-2023-28229](https://github.com/Y3A/CVE-2023-28229) :  ![starts](https://img.shields.io/github/stars/Y3A/CVE-2023-28229.svg) ![forks](https://img.shields.io/github/forks/Y3A/CVE-2023-28229.svg)

- [https://github.com/byt3n33dl3/CrackKeyIso](https://github.com/byt3n33dl3/CrackKeyIso) :  ![starts](https://img.shields.io/github/stars/byt3n33dl3/CrackKeyIso.svg) ![forks](https://img.shields.io/github/forks/byt3n33dl3/CrackKeyIso.svg)

## CVE-2023-28218
 Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability



- [https://github.com/h1bAna/CVE-2023-28218](https://github.com/h1bAna/CVE-2023-28218) :  ![starts](https://img.shields.io/github/stars/h1bAna/CVE-2023-28218.svg) ![forks](https://img.shields.io/github/forks/h1bAna/CVE-2023-28218.svg)

## CVE-2023-28206
 An out-of-bounds write issue was addressed with improved input validation. This issue is fixed in macOS Monterey 12.6.5, iOS 16.4.1 and iPadOS 16.4.1, macOS Ventura 13.3.1, iOS 15.7.5 and iPadOS 15.7.5, macOS Big Sur 11.7.6. An app may be able to execute arbitrary code with kernel privileges. Apple is aware of a report that this issue may have been actively exploited.



- [https://github.com/acceleratortroll/acceleratortroll](https://github.com/acceleratortroll/acceleratortroll) :  ![starts](https://img.shields.io/github/stars/acceleratortroll/acceleratortroll.svg) ![forks](https://img.shields.io/github/forks/acceleratortroll/acceleratortroll.svg)

## CVE-2023-28205
 A use after free issue was addressed with improved memory management. This issue is fixed in Safari 16.4.1, iOS 15.7.5 and iPadOS 15.7.5, iOS 16.4.1 and iPadOS 16.4.1, macOS Ventura 13.3.1. Processing maliciously crafted web content may lead to arbitrary code execution. Apple is aware of a report that this issue may have been actively exploited.



- [https://github.com/ntfargo/uaf-2023-28205](https://github.com/ntfargo/uaf-2023-28205) :  ![starts](https://img.shields.io/github/stars/ntfargo/uaf-2023-28205.svg) ![forks](https://img.shields.io/github/forks/ntfargo/uaf-2023-28205.svg)

## CVE-2023-28197
 An access issue was addressed with additional sandbox restrictions. This issue is fixed in macOS Ventura 13.3, macOS Big Sur 11.7.5, macOS Monterey 12.6.4. An app may be able to access user-sensitive data.



- [https://github.com/spotlightishere/inputcontrol](https://github.com/spotlightishere/inputcontrol) :  ![starts](https://img.shields.io/github/stars/spotlightishere/inputcontrol.svg) ![forks](https://img.shields.io/github/forks/spotlightishere/inputcontrol.svg)

## CVE-2023-28121
 An issue in WooCommerce Payments plugin for WordPress (versions 5.6.1 and lower) allows an unauthenticated attacker to send requests on behalf of an elevated user, like administrator. This allows a remote, unauthenticated attacker to gain admin access on a site that has the affected version of the plugin activated.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/gbrsh/CVE-2023-28121](https://github.com/gbrsh/CVE-2023-28121) :  ![starts](https://img.shields.io/github/stars/gbrsh/CVE-2023-28121.svg) ![forks](https://img.shields.io/github/forks/gbrsh/CVE-2023-28121.svg)

- [https://github.com/im-hanzou/Mass-CVE-2023-28121](https://github.com/im-hanzou/Mass-CVE-2023-28121) :  ![starts](https://img.shields.io/github/stars/im-hanzou/Mass-CVE-2023-28121.svg) ![forks](https://img.shields.io/github/forks/im-hanzou/Mass-CVE-2023-28121.svg)

- [https://github.com/rio128128/Mass-CVE-2023-28121-kdoec](https://github.com/rio128128/Mass-CVE-2023-28121-kdoec) :  ![starts](https://img.shields.io/github/stars/rio128128/Mass-CVE-2023-28121-kdoec.svg) ![forks](https://img.shields.io/github/forks/rio128128/Mass-CVE-2023-28121-kdoec.svg)

- [https://github.com/Jenderal92/WP-CVE-2023-28121](https://github.com/Jenderal92/WP-CVE-2023-28121) :  ![starts](https://img.shields.io/github/stars/Jenderal92/WP-CVE-2023-28121.svg) ![forks](https://img.shields.io/github/forks/Jenderal92/WP-CVE-2023-28121.svg)

- [https://github.com/1337nemojj/CVE-2023-28121](https://github.com/1337nemojj/CVE-2023-28121) :  ![starts](https://img.shields.io/github/stars/1337nemojj/CVE-2023-28121.svg) ![forks](https://img.shields.io/github/forks/1337nemojj/CVE-2023-28121.svg)

- [https://github.com/C04LA/CVE-2023-28121](https://github.com/C04LA/CVE-2023-28121) :  ![starts](https://img.shields.io/github/stars/C04LA/CVE-2023-28121.svg) ![forks](https://img.shields.io/github/forks/C04LA/CVE-2023-28121.svg)

- [https://github.com/sug4r-wr41th/CVE-2023-28121](https://github.com/sug4r-wr41th/CVE-2023-28121) :  ![starts](https://img.shields.io/github/stars/sug4r-wr41th/CVE-2023-28121.svg) ![forks](https://img.shields.io/github/forks/sug4r-wr41th/CVE-2023-28121.svg)

## CVE-2023-27997
 A heap-based buffer overflow vulnerability [CWE-122] in FortiOS version 7.2.4 and below, version 7.0.11 and below, version 6.4.12 and below, version 6.0.16 and below and FortiProxy version 7.2.3 and below, version 7.0.9 and below, version 2.0.12 and below, version 1.2 all versions, version 1.1 all versions SSL-VPN may allow a remote attacker to execute arbitrary code or commands via specifically crafted requests.



- [https://github.com/BishopFox/CVE-2023-27997-check](https://github.com/BishopFox/CVE-2023-27997-check) :  ![starts](https://img.shields.io/github/stars/BishopFox/CVE-2023-27997-check.svg) ![forks](https://img.shields.io/github/forks/BishopFox/CVE-2023-27997-check.svg)

- [https://github.com/lexfo/xortigate-cve-2023-27997](https://github.com/lexfo/xortigate-cve-2023-27997) :  ![starts](https://img.shields.io/github/stars/lexfo/xortigate-cve-2023-27997.svg) ![forks](https://img.shields.io/github/forks/lexfo/xortigate-cve-2023-27997.svg)

- [https://github.com/rio128128/CVE-2023-27997-POC](https://github.com/rio128128/CVE-2023-27997-POC) :  ![starts](https://img.shields.io/github/stars/rio128128/CVE-2023-27997-POC.svg) ![forks](https://img.shields.io/github/forks/rio128128/CVE-2023-27997-POC.svg)

- [https://github.com/delsploit/CVE-2023-27997](https://github.com/delsploit/CVE-2023-27997) :  ![starts](https://img.shields.io/github/stars/delsploit/CVE-2023-27997.svg) ![forks](https://img.shields.io/github/forks/delsploit/CVE-2023-27997.svg)

- [https://github.com/TechinsightsPro/ShodanFortiOS](https://github.com/TechinsightsPro/ShodanFortiOS) :  ![starts](https://img.shields.io/github/stars/TechinsightsPro/ShodanFortiOS.svg) ![forks](https://img.shields.io/github/forks/TechinsightsPro/ShodanFortiOS.svg)

- [https://github.com/imbas007/CVE-2023-27997-Check](https://github.com/imbas007/CVE-2023-27997-Check) :  ![starts](https://img.shields.io/github/stars/imbas007/CVE-2023-27997-Check.svg) ![forks](https://img.shields.io/github/forks/imbas007/CVE-2023-27997-Check.svg)

- [https://github.com/puckiestyle/cve-2023-27997](https://github.com/puckiestyle/cve-2023-27997) :  ![starts](https://img.shields.io/github/stars/puckiestyle/cve-2023-27997.svg) ![forks](https://img.shields.io/github/forks/puckiestyle/cve-2023-27997.svg)

- [https://github.com/Cyb3rEnthusiast/CVE-2023-27997](https://github.com/Cyb3rEnthusiast/CVE-2023-27997) :  ![starts](https://img.shields.io/github/stars/Cyb3rEnthusiast/CVE-2023-27997.svg) ![forks](https://img.shields.io/github/forks/Cyb3rEnthusiast/CVE-2023-27997.svg)

- [https://github.com/node011/CVE-2023-27997-POC](https://github.com/node011/CVE-2023-27997-POC) :  ![starts](https://img.shields.io/github/stars/node011/CVE-2023-27997-POC.svg) ![forks](https://img.shields.io/github/forks/node011/CVE-2023-27997-POC.svg)

- [https://github.com/onurkerembozkurt/fgt-cve-2023-27997-exploit](https://github.com/onurkerembozkurt/fgt-cve-2023-27997-exploit) :  ![starts](https://img.shields.io/github/stars/onurkerembozkurt/fgt-cve-2023-27997-exploit.svg) ![forks](https://img.shields.io/github/forks/onurkerembozkurt/fgt-cve-2023-27997-exploit.svg)

## CVE-2023-27842
 Insecure Permissions vulnerability found in Extplorer File manager eXtplorer v.2.1.15 allows a remote attacker to execute arbitrary code via the index.php compenent



- [https://github.com/cowsecurity/CVE-2023-27842](https://github.com/cowsecurity/CVE-2023-27842) :  ![starts](https://img.shields.io/github/stars/cowsecurity/CVE-2023-27842.svg) ![forks](https://img.shields.io/github/forks/cowsecurity/CVE-2023-27842.svg)

- [https://github.com/tristao-io/CVE-2023-27842](https://github.com/tristao-io/CVE-2023-27842) :  ![starts](https://img.shields.io/github/stars/tristao-io/CVE-2023-27842.svg) ![forks](https://img.shields.io/github/forks/tristao-io/CVE-2023-27842.svg)

## CVE-2023-27748
 BlackVue DR750-2CH LTE v.1.012_2022.10.26 does not employ authenticity check for uploaded firmware. This can allow attackers to upload crafted firmware which contains backdoors and enables arbitrary code execution.



- [https://github.com/eyJhb/blackvue-cve-2023](https://github.com/eyJhb/blackvue-cve-2023) :  ![starts](https://img.shields.io/github/stars/eyJhb/blackvue-cve-2023.svg) ![forks](https://img.shields.io/github/forks/eyJhb/blackvue-cve-2023.svg)

## CVE-2023-27747
 BlackVue DR750-2CH LTE v.1.012_2022.10.26 does not employ authentication in its web server. This vulnerability allows attackers to access sensitive information such as configurations and recordings.



- [https://github.com/eyJhb/blackvue-cve-2023](https://github.com/eyJhb/blackvue-cve-2023) :  ![starts](https://img.shields.io/github/stars/eyJhb/blackvue-cve-2023.svg) ![forks](https://img.shields.io/github/forks/eyJhb/blackvue-cve-2023.svg)

## CVE-2023-27746
 BlackVue DR750-2CH LTE v.1.012_2022.10.26 was discovered to contain a weak default passphrase which can be easily cracked via a brute force attack if the WPA2 handshake is intercepted.



- [https://github.com/eyJhb/blackvue-cve-2023](https://github.com/eyJhb/blackvue-cve-2023) :  ![starts](https://img.shields.io/github/stars/eyJhb/blackvue-cve-2023.svg) ![forks](https://img.shields.io/github/forks/eyJhb/blackvue-cve-2023.svg)

## CVE-2023-27742
 IDURAR ERP/CRM v1 was discovered to contain a SQL injection vulnerability via the component /api/login.



- [https://github.com/G37SYS73M/CVE-2023-27742](https://github.com/G37SYS73M/CVE-2023-27742) :  ![starts](https://img.shields.io/github/stars/G37SYS73M/CVE-2023-27742.svg) ![forks](https://img.shields.io/github/forks/G37SYS73M/CVE-2023-27742.svg)

## CVE-2023-27704
 Void Tools Everything lower than v1.4.1.1022 was discovered to contain a Regular Expression Denial of Service (ReDoS).



- [https://github.com/happy0717/CVE-2023-27704](https://github.com/happy0717/CVE-2023-27704) :  ![starts](https://img.shields.io/github/stars/happy0717/CVE-2023-27704.svg) ![forks](https://img.shields.io/github/forks/happy0717/CVE-2023-27704.svg)

## CVE-2023-27703
 The Android version of pikpak v1.29.2 was discovered to contain an information leak via the debug interface.



- [https://github.com/happy0717/CVE-2023-27703](https://github.com/happy0717/CVE-2023-27703) :  ![starts](https://img.shields.io/github/stars/happy0717/CVE-2023-27703.svg) ![forks](https://img.shields.io/github/forks/happy0717/CVE-2023-27703.svg)

## CVE-2023-27587
 ReadtoMyShoe, a web app that lets users upload articles and listen to them later, generates an error message containing sensitive information prior to commit 8533b01. If an error occurs when adding an article, the website shows the user an error message. If the error originates from the Google Cloud TTS request, then it will include the full URL of the request. The request URL contains the Google Cloud API key. This has been patched in commit 8533b01. Upgrading should be accompanied by deleting the current GCP API key and issuing a new one. There are no known workarounds.



- [https://github.com/vagnerd/CVE-2023-27587-PoC](https://github.com/vagnerd/CVE-2023-27587-PoC) :  ![starts](https://img.shields.io/github/stars/vagnerd/CVE-2023-27587-PoC.svg) ![forks](https://img.shields.io/github/forks/vagnerd/CVE-2023-27587-PoC.svg)

## CVE-2023-27566
 Cubism Core in Live2D Cubism Editor 4.2.03 allows out-of-bounds write via a crafted Section Offset Table or Count Info Table in an MOC3 file.



- [https://github.com/OpenL2D/moc3ingbird](https://github.com/OpenL2D/moc3ingbird) :  ![starts](https://img.shields.io/github/stars/OpenL2D/moc3ingbird.svg) ![forks](https://img.shields.io/github/forks/OpenL2D/moc3ingbird.svg)

## CVE-2023-27564
 The n8n package 0.218.0 for Node.js allows Information Disclosure.



- [https://github.com/david-botelho-mariano/exploit-CVE-2023-27564](https://github.com/david-botelho-mariano/exploit-CVE-2023-27564) :  ![starts](https://img.shields.io/github/stars/david-botelho-mariano/exploit-CVE-2023-27564.svg) ![forks](https://img.shields.io/github/forks/david-botelho-mariano/exploit-CVE-2023-27564.svg)

## CVE-2023-27532
 Vulnerability in Veeam Backup & Replication component allows encrypted credentials stored in the configuration database to be obtained. This may lead to gaining access to the backup infrastructure hosts.



- [https://github.com/sfewer-r7/CVE-2023-27532](https://github.com/sfewer-r7/CVE-2023-27532) :  ![starts](https://img.shields.io/github/stars/sfewer-r7/CVE-2023-27532.svg) ![forks](https://img.shields.io/github/forks/sfewer-r7/CVE-2023-27532.svg)

- [https://github.com/horizon3ai/CVE-2023-27532](https://github.com/horizon3ai/CVE-2023-27532) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2023-27532.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2023-27532.svg)

- [https://github.com/puckiestyle/CVE-2023-27532-RCE-Only](https://github.com/puckiestyle/CVE-2023-27532-RCE-Only) :  ![starts](https://img.shields.io/github/stars/puckiestyle/CVE-2023-27532-RCE-Only.svg) ![forks](https://img.shields.io/github/forks/puckiestyle/CVE-2023-27532-RCE-Only.svg)

## CVE-2023-27524
 Session Validation attacks in Apache Superset versions up to and including 2.0.1. Installations that have not altered the default configured SECRET_KEY according to installation instructions allow for an attacker to authenticate and access unauthorized resources. This does not affect Superset administrators who have changed the default value for SECRET_KEY config.

All superset installations should always set a unique secure random SECRET_KEY. Your SECRET_KEY is used to securely sign all session cookies and encrypting sensitive information on the database.
Add a strong SECRET_KEY to your `superset_config.py` file like:

SECRET_KEY = YOUR_OWN_RANDOM_GENERATED_SECRET_KEY

Alternatively you can set it with `SUPERSET_SECRET_KEY` environment variable.




- [https://github.com/horizon3ai/CVE-2023-27524](https://github.com/horizon3ai/CVE-2023-27524) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2023-27524.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2023-27524.svg)

- [https://github.com/jakabakos/CVE-2023-27524-Apache-Superset-Auth-Bypass-and-RCE](https://github.com/jakabakos/CVE-2023-27524-Apache-Superset-Auth-Bypass-and-RCE) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2023-27524-Apache-Superset-Auth-Bypass-and-RCE.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2023-27524-Apache-Superset-Auth-Bypass-and-RCE.svg)

- [https://github.com/Okaytc/Superset_auth_bypass_check](https://github.com/Okaytc/Superset_auth_bypass_check) :  ![starts](https://img.shields.io/github/stars/Okaytc/Superset_auth_bypass_check.svg) ![forks](https://img.shields.io/github/forks/Okaytc/Superset_auth_bypass_check.svg)

- [https://github.com/TardC/CVE-2023-27524](https://github.com/TardC/CVE-2023-27524) :  ![starts](https://img.shields.io/github/stars/TardC/CVE-2023-27524.svg) ![forks](https://img.shields.io/github/forks/TardC/CVE-2023-27524.svg)

- [https://github.com/ThatNotEasy/CVE-2023-27524](https://github.com/ThatNotEasy/CVE-2023-27524) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2023-27524.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2023-27524.svg)

- [https://github.com/ZZ-SOCMAP/CVE-2023-27524](https://github.com/ZZ-SOCMAP/CVE-2023-27524) :  ![starts](https://img.shields.io/github/stars/ZZ-SOCMAP/CVE-2023-27524.svg) ![forks](https://img.shields.io/github/forks/ZZ-SOCMAP/CVE-2023-27524.svg)

- [https://github.com/Cappricio-Securities/CVE-2023-27524](https://github.com/Cappricio-Securities/CVE-2023-27524) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2023-27524.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2023-27524.svg)

- [https://github.com/karthi-the-hacker/CVE-2023-27524](https://github.com/karthi-the-hacker/CVE-2023-27524) :  ![starts](https://img.shields.io/github/stars/karthi-the-hacker/CVE-2023-27524.svg) ![forks](https://img.shields.io/github/forks/karthi-the-hacker/CVE-2023-27524.svg)

- [https://github.com/necroteddy/CVE-2023-27524](https://github.com/necroteddy/CVE-2023-27524) :  ![starts](https://img.shields.io/github/stars/necroteddy/CVE-2023-27524.svg) ![forks](https://img.shields.io/github/forks/necroteddy/CVE-2023-27524.svg)

- [https://github.com/h1n4mx0/Research-CVE-2023-27524](https://github.com/h1n4mx0/Research-CVE-2023-27524) :  ![starts](https://img.shields.io/github/stars/h1n4mx0/Research-CVE-2023-27524.svg) ![forks](https://img.shields.io/github/forks/h1n4mx0/Research-CVE-2023-27524.svg)

- [https://github.com/MaanVader/CVE-2023-27524-POC](https://github.com/MaanVader/CVE-2023-27524-POC) :  ![starts](https://img.shields.io/github/stars/MaanVader/CVE-2023-27524-POC.svg) ![forks](https://img.shields.io/github/forks/MaanVader/CVE-2023-27524-POC.svg)

- [https://github.com/CN016/Apache-Superset-SECRET_KEY-CVE-2023-27524-](https://github.com/CN016/Apache-Superset-SECRET_KEY-CVE-2023-27524-) :  ![starts](https://img.shields.io/github/stars/CN016/Apache-Superset-SECRET_KEY-CVE-2023-27524-.svg) ![forks](https://img.shields.io/github/forks/CN016/Apache-Superset-SECRET_KEY-CVE-2023-27524-.svg)

## CVE-2023-27470
 BASupSrvcUpdater.exe in N-able Take Control Agent through 7.0.41.1141 before 7.0.43 has a TOCTOU Race Condition via a pseudo-symlink at %PROGRAMDATA%\GetSupportService_N-Central\PushUpdates, leading to arbitrary file deletion.



- [https://github.com/3lp4tr0n/CVE-2023-27470_Exercise](https://github.com/3lp4tr0n/CVE-2023-27470_Exercise) :  ![starts](https://img.shields.io/github/stars/3lp4tr0n/CVE-2023-27470_Exercise.svg) ![forks](https://img.shields.io/github/forks/3lp4tr0n/CVE-2023-27470_Exercise.svg)

## CVE-2023-27372
 SPIP before 4.2.1 allows Remote Code Execution via form values in the public area because serialization is mishandled. The fixed versions are 3.2.18, 4.0.10, 4.1.8, and 4.2.1.



- [https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance](https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance) :  ![starts](https://img.shields.io/github/stars/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg) ![forks](https://img.shields.io/github/forks/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg)

- [https://github.com/nuts7/CVE-2023-27372](https://github.com/nuts7/CVE-2023-27372) :  ![starts](https://img.shields.io/github/stars/nuts7/CVE-2023-27372.svg) ![forks](https://img.shields.io/github/forks/nuts7/CVE-2023-27372.svg)

- [https://github.com/Chocapikk/CVE-2023-27372](https://github.com/Chocapikk/CVE-2023-27372) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-27372.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-27372.svg)

- [https://github.com/0SPwn/CVE-2023-27372-PoC](https://github.com/0SPwn/CVE-2023-27372-PoC) :  ![starts](https://img.shields.io/github/stars/0SPwn/CVE-2023-27372-PoC.svg) ![forks](https://img.shields.io/github/forks/0SPwn/CVE-2023-27372-PoC.svg)

- [https://github.com/ThatNotEasy/CVE-2023-27372](https://github.com/ThatNotEasy/CVE-2023-27372) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2023-27372.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2023-27372.svg)

- [https://github.com/izzz0/CVE-2023-27372-POC](https://github.com/izzz0/CVE-2023-27372-POC) :  ![starts](https://img.shields.io/github/stars/izzz0/CVE-2023-27372-POC.svg) ![forks](https://img.shields.io/github/forks/izzz0/CVE-2023-27372-POC.svg)

- [https://github.com/1Ronkkeli/spip-cve-2023-27372-rce](https://github.com/1Ronkkeli/spip-cve-2023-27372-rce) :  ![starts](https://img.shields.io/github/stars/1Ronkkeli/spip-cve-2023-27372-rce.svg) ![forks](https://img.shields.io/github/forks/1Ronkkeli/spip-cve-2023-27372-rce.svg)

- [https://github.com/G01d3nW01f/cve-2023-27372](https://github.com/G01d3nW01f/cve-2023-27372) :  ![starts](https://img.shields.io/github/stars/G01d3nW01f/cve-2023-27372.svg) ![forks](https://img.shields.io/github/forks/G01d3nW01f/cve-2023-27372.svg)

- [https://github.com/dream434/CVE-2023-27372](https://github.com/dream434/CVE-2023-27372) :  ![starts](https://img.shields.io/github/stars/dream434/CVE-2023-27372.svg) ![forks](https://img.shields.io/github/forks/dream434/CVE-2023-27372.svg)

- [https://github.com/redboltsec/CVE-2023-27372-PoC](https://github.com/redboltsec/CVE-2023-27372-PoC) :  ![starts](https://img.shields.io/github/stars/redboltsec/CVE-2023-27372-PoC.svg) ![forks](https://img.shields.io/github/forks/redboltsec/CVE-2023-27372-PoC.svg)

## CVE-2023-27363
 Foxit PDF Reader exportXFAData Exposed Dangerous Method Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the exportXFAData method. The application exposes a JavaScript interface that allows writing arbitrary files. An attacker can leverage this vulnerability to execute code in the context of the current user. Was ZDI-CAN-19697.



- [https://github.com/webraybtl/CVE-2023-27363](https://github.com/webraybtl/CVE-2023-27363) :  ![starts](https://img.shields.io/github/stars/webraybtl/CVE-2023-27363.svg) ![forks](https://img.shields.io/github/forks/webraybtl/CVE-2023-27363.svg)

- [https://github.com/qwqdanchun/CVE-2023-27363](https://github.com/qwqdanchun/CVE-2023-27363) :  ![starts](https://img.shields.io/github/stars/qwqdanchun/CVE-2023-27363.svg) ![forks](https://img.shields.io/github/forks/qwqdanchun/CVE-2023-27363.svg)

- [https://github.com/CN016/-Foxit-PDF-CVE-2023-27363-](https://github.com/CN016/-Foxit-PDF-CVE-2023-27363-) :  ![starts](https://img.shields.io/github/stars/CN016/-Foxit-PDF-CVE-2023-27363-.svg) ![forks](https://img.shields.io/github/forks/CN016/-Foxit-PDF-CVE-2023-27363-.svg)

## CVE-2023-27350
 This vulnerability allows remote attackers to bypass authentication on affected installations of PaperCut NG 22.0.5 (Build 63914). Authentication is not required to exploit this vulnerability. The specific flaw exists within the SetupCompleted class. The issue results from improper access control. An attacker can leverage this vulnerability to bypass authentication and execute arbitrary code in the context of SYSTEM. Was ZDI-CAN-18987.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/horizon3ai/CVE-2023-27350](https://github.com/horizon3ai/CVE-2023-27350) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2023-27350.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2023-27350.svg)

- [https://github.com/imancybersecurity/CVE-2023-27350-POC](https://github.com/imancybersecurity/CVE-2023-27350-POC) :  ![starts](https://img.shields.io/github/stars/imancybersecurity/CVE-2023-27350-POC.svg) ![forks](https://img.shields.io/github/forks/imancybersecurity/CVE-2023-27350-POC.svg)

- [https://github.com/adhikara13/CVE-2023-27350](https://github.com/adhikara13/CVE-2023-27350) :  ![starts](https://img.shields.io/github/stars/adhikara13/CVE-2023-27350.svg) ![forks](https://img.shields.io/github/forks/adhikara13/CVE-2023-27350.svg)

- [https://github.com/MaanVader/CVE-2023-27350-POC](https://github.com/MaanVader/CVE-2023-27350-POC) :  ![starts](https://img.shields.io/github/stars/MaanVader/CVE-2023-27350-POC.svg) ![forks](https://img.shields.io/github/forks/MaanVader/CVE-2023-27350-POC.svg)

- [https://github.com/ThatNotEasy/CVE-2023-27350](https://github.com/ThatNotEasy/CVE-2023-27350) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2023-27350.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2023-27350.svg)

- [https://github.com/Jenderal92/CVE-2023-27350](https://github.com/Jenderal92/CVE-2023-27350) :  ![starts](https://img.shields.io/github/stars/Jenderal92/CVE-2023-27350.svg) ![forks](https://img.shields.io/github/forks/Jenderal92/CVE-2023-27350.svg)

- [https://github.com/0xB0y426/CVE-2023-27350-PoC](https://github.com/0xB0y426/CVE-2023-27350-PoC) :  ![starts](https://img.shields.io/github/stars/0xB0y426/CVE-2023-27350-PoC.svg) ![forks](https://img.shields.io/github/forks/0xB0y426/CVE-2023-27350-PoC.svg)

- [https://github.com/ASG-CASTLE/CVE-2023-27350](https://github.com/ASG-CASTLE/CVE-2023-27350) :  ![starts](https://img.shields.io/github/stars/ASG-CASTLE/CVE-2023-27350.svg) ![forks](https://img.shields.io/github/forks/ASG-CASTLE/CVE-2023-27350.svg)

- [https://github.com/Royall-Researchers/CVE-2023-27350](https://github.com/Royall-Researchers/CVE-2023-27350) :  ![starts](https://img.shields.io/github/stars/Royall-Researchers/CVE-2023-27350.svg) ![forks](https://img.shields.io/github/forks/Royall-Researchers/CVE-2023-27350.svg)

- [https://github.com/rasan2001/CVE-2023-27350-Ongoing-Exploitation-of-PaperCut-Remote-Code-Execution-Vulnerability](https://github.com/rasan2001/CVE-2023-27350-Ongoing-Exploitation-of-PaperCut-Remote-Code-Execution-Vulnerability) :  ![starts](https://img.shields.io/github/stars/rasan2001/CVE-2023-27350-Ongoing-Exploitation-of-PaperCut-Remote-Code-Execution-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/rasan2001/CVE-2023-27350-Ongoing-Exploitation-of-PaperCut-Remote-Code-Execution-Vulnerability.svg)

## CVE-2023-27328
 Parallels Desktop Toolgate XML Injection Local Privilege Escalation Vulnerability. This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability.

The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of a user-supplied string before using it to construct an XML document. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor. Was ZDI-CAN-19187.



- [https://github.com/kn32/parallels-plist-escape](https://github.com/kn32/parallels-plist-escape) :  ![starts](https://img.shields.io/github/stars/kn32/parallels-plist-escape.svg) ![forks](https://img.shields.io/github/forks/kn32/parallels-plist-escape.svg)

## CVE-2023-27327
 Parallels Desktop Toolgate Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability. This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability.

The specific flaw exists within the Toolgate component. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the current user on the host system. Was ZDI-CAN-18964.



- [https://github.com/kn32/parallels-plist-escape](https://github.com/kn32/parallels-plist-escape) :  ![starts](https://img.shields.io/github/stars/kn32/parallels-plist-escape.svg) ![forks](https://img.shields.io/github/forks/kn32/parallels-plist-escape.svg)

## CVE-2023-27326
 Parallels Desktop Toolgate Directory Traversal Local Privilege Escalation Vulnerability. This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability.

The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the current user on the host system.
. Was ZDI-CAN-18933.



- [https://github.com/Impalabs/CVE-2023-27326](https://github.com/Impalabs/CVE-2023-27326) :  ![starts](https://img.shields.io/github/stars/Impalabs/CVE-2023-27326.svg) ![forks](https://img.shields.io/github/forks/Impalabs/CVE-2023-27326.svg)

- [https://github.com/Malwareman007/CVE-2023-27326](https://github.com/Malwareman007/CVE-2023-27326) :  ![starts](https://img.shields.io/github/stars/Malwareman007/CVE-2023-27326.svg) ![forks](https://img.shields.io/github/forks/Malwareman007/CVE-2023-27326.svg)

## CVE-2023-27216
 An issue found in D-Link DSL-3782 v.1.03 allows remote authenticated users to execute arbitrary code as root via the network settings page.



- [https://github.com/HoangREALER/CVE-2023-27216](https://github.com/HoangREALER/CVE-2023-27216) :  ![starts](https://img.shields.io/github/stars/HoangREALER/CVE-2023-27216.svg) ![forks](https://img.shields.io/github/forks/HoangREALER/CVE-2023-27216.svg)

- [https://github.com/FzBacon/CVE-2023-27216_D-Link_DSL-3782_Router_command_injection](https://github.com/FzBacon/CVE-2023-27216_D-Link_DSL-3782_Router_command_injection) :  ![starts](https://img.shields.io/github/stars/FzBacon/CVE-2023-27216_D-Link_DSL-3782_Router_command_injection.svg) ![forks](https://img.shields.io/github/forks/FzBacon/CVE-2023-27216_D-Link_DSL-3782_Router_command_injection.svg)

## CVE-2023-27163
 request-baskets up to v1.2.1 was discovered to contain a Server-Side Request Forgery (SSRF) via the component /api/baskets/{name}. This vulnerability allows attackers to access network resources and sensitive information via a crafted API request.



- [https://github.com/entr0pie/CVE-2023-27163](https://github.com/entr0pie/CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/entr0pie/CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/entr0pie/CVE-2023-27163.svg)

- [https://github.com/samh4cks/CVE-2023-27163-InternalProber](https://github.com/samh4cks/CVE-2023-27163-InternalProber) :  ![starts](https://img.shields.io/github/stars/samh4cks/CVE-2023-27163-InternalProber.svg) ![forks](https://img.shields.io/github/forks/samh4cks/CVE-2023-27163-InternalProber.svg)

- [https://github.com/seanrdev/cve-2023-27163](https://github.com/seanrdev/cve-2023-27163) :  ![starts](https://img.shields.io/github/stars/seanrdev/cve-2023-27163.svg) ![forks](https://img.shields.io/github/forks/seanrdev/cve-2023-27163.svg)

- [https://github.com/thomas-osgood/CVE-2023-27163](https://github.com/thomas-osgood/CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/thomas-osgood/CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/thomas-osgood/CVE-2023-27163.svg)

- [https://github.com/rvizx/CVE-2023-27163](https://github.com/rvizx/CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/rvizx/CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/rvizx/CVE-2023-27163.svg)

- [https://github.com/MasterCode112/CVE-2023-27163](https://github.com/MasterCode112/CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/MasterCode112/CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/MasterCode112/CVE-2023-27163.svg)

- [https://github.com/Rubioo02/CVE-2023-27163](https://github.com/Rubioo02/CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/Rubioo02/CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/Rubioo02/CVE-2023-27163.svg)

- [https://github.com/HusenjanDev/CVE-2023-27163-AND-Mailtrail-v0.53](https://github.com/HusenjanDev/CVE-2023-27163-AND-Mailtrail-v0.53) :  ![starts](https://img.shields.io/github/stars/HusenjanDev/CVE-2023-27163-AND-Mailtrail-v0.53.svg) ![forks](https://img.shields.io/github/forks/HusenjanDev/CVE-2023-27163-AND-Mailtrail-v0.53.svg)

- [https://github.com/davuXVI/CVE-2023-27163](https://github.com/davuXVI/CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/davuXVI/CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/davuXVI/CVE-2023-27163.svg)

- [https://github.com/ThickCoco/CVE-2023-27163-POC](https://github.com/ThickCoco/CVE-2023-27163-POC) :  ![starts](https://img.shields.io/github/stars/ThickCoco/CVE-2023-27163-POC.svg) ![forks](https://img.shields.io/github/forks/ThickCoco/CVE-2023-27163-POC.svg)

- [https://github.com/KharimMchatta/basketcraft](https://github.com/KharimMchatta/basketcraft) :  ![starts](https://img.shields.io/github/stars/KharimMchatta/basketcraft.svg) ![forks](https://img.shields.io/github/forks/KharimMchatta/basketcraft.svg)

- [https://github.com/overgrowncarrot1/CVE-2023-27163](https://github.com/overgrowncarrot1/CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/overgrowncarrot1/CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/overgrowncarrot1/CVE-2023-27163.svg)

- [https://github.com/lukehebe/CVE-2023-27163](https://github.com/lukehebe/CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/lukehebe/CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/lukehebe/CVE-2023-27163.svg)

- [https://github.com/madhavmehndiratta/CVE-2023-27163](https://github.com/madhavmehndiratta/CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/madhavmehndiratta/CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/madhavmehndiratta/CVE-2023-27163.svg)

- [https://github.com/cowsecurity/CVE-2023-27163](https://github.com/cowsecurity/CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/cowsecurity/CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/cowsecurity/CVE-2023-27163.svg)

- [https://github.com/Hamibubu/CVE-2023-27163](https://github.com/Hamibubu/CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/Hamibubu/CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/Hamibubu/CVE-2023-27163.svg)

- [https://github.com/G4sp4rCS/htb-sau-automated](https://github.com/G4sp4rCS/htb-sau-automated) :  ![starts](https://img.shields.io/github/stars/G4sp4rCS/htb-sau-automated.svg) ![forks](https://img.shields.io/github/forks/G4sp4rCS/htb-sau-automated.svg)

- [https://github.com/J0ey17/Exploit_CVE-2023-27163](https://github.com/J0ey17/Exploit_CVE-2023-27163) :  ![starts](https://img.shields.io/github/stars/J0ey17/Exploit_CVE-2023-27163.svg) ![forks](https://img.shields.io/github/forks/J0ey17/Exploit_CVE-2023-27163.svg)

- [https://github.com/Rishabh-Kumar-Cyber-Sec/CVE-2023-27163-ssrf-to-port-scanning](https://github.com/Rishabh-Kumar-Cyber-Sec/CVE-2023-27163-ssrf-to-port-scanning) :  ![starts](https://img.shields.io/github/stars/Rishabh-Kumar-Cyber-Sec/CVE-2023-27163-ssrf-to-port-scanning.svg) ![forks](https://img.shields.io/github/forks/Rishabh-Kumar-Cyber-Sec/CVE-2023-27163-ssrf-to-port-scanning.svg)

## CVE-2023-27100
 Improper restriction of excessive authentication attempts in the SSHGuard component of Netgate pfSense Plus software v22.05.1 and pfSense CE software v2.6.0 allows attackers to bypass brute force protection mechanisms via crafted web requests.



- [https://github.com/DarokNET/CVE-2023-27100](https://github.com/DarokNET/CVE-2023-27100) :  ![starts](https://img.shields.io/github/stars/DarokNET/CVE-2023-27100.svg) ![forks](https://img.shields.io/github/forks/DarokNET/CVE-2023-27100.svg)

- [https://github.com/fabdotnet/CVE-2023-27100](https://github.com/fabdotnet/CVE-2023-27100) :  ![starts](https://img.shields.io/github/stars/fabdotnet/CVE-2023-27100.svg) ![forks](https://img.shields.io/github/forks/fabdotnet/CVE-2023-27100.svg)

## CVE-2023-27035
 An issue discovered in Obsidian Canvas 1.1.9 allows remote attackers to send desktop notifications, record user audio and other unspecified impacts via embedded website on the canvas page.



- [https://github.com/fivex3/CVE-2023-27035](https://github.com/fivex3/CVE-2023-27035) :  ![starts](https://img.shields.io/github/stars/fivex3/CVE-2023-27035.svg) ![forks](https://img.shields.io/github/forks/fivex3/CVE-2023-27035.svg)

## CVE-2023-26984
 An issue in the password reset function of Peppermint v0.2.4 allows attackers to access the emails and passwords of the Tickets page via a crafted request.



- [https://github.com/bypazs/CVE-2023-26984](https://github.com/bypazs/CVE-2023-26984) :  ![starts](https://img.shields.io/github/stars/bypazs/CVE-2023-26984.svg) ![forks](https://img.shields.io/github/forks/bypazs/CVE-2023-26984.svg)

## CVE-2023-26982
 Trudesk v1.2.6 was discovered to contain a stored cross-site scripting (XSS) vulnerability via the Add Tags parameter under the Create Ticket function.



- [https://github.com/bypazs/CVE-2023-26982](https://github.com/bypazs/CVE-2023-26982) :  ![starts](https://img.shields.io/github/stars/bypazs/CVE-2023-26982.svg) ![forks](https://img.shields.io/github/forks/bypazs/CVE-2023-26982.svg)

- [https://github.com/bypazs/Duplicate-of-CVE-2023-26982](https://github.com/bypazs/Duplicate-of-CVE-2023-26982) :  ![starts](https://img.shields.io/github/stars/bypazs/Duplicate-of-CVE-2023-26982.svg) ![forks](https://img.shields.io/github/forks/bypazs/Duplicate-of-CVE-2023-26982.svg)

## CVE-2023-26976
 Tenda AC6 v15.03.05.09_multi was discovered to contain a stack overflow via the ssid parameter in the form_fast_setting_wifi_set function.



- [https://github.com/FzBacon/CVE-2023-26976_tenda_AC6_stack_overflow](https://github.com/FzBacon/CVE-2023-26976_tenda_AC6_stack_overflow) :  ![starts](https://img.shields.io/github/stars/FzBacon/CVE-2023-26976_tenda_AC6_stack_overflow.svg) ![forks](https://img.shields.io/github/forks/FzBacon/CVE-2023-26976_tenda_AC6_stack_overflow.svg)

## CVE-2023-26866
 GreenPacket OH736's WR-1200 Indoor Unit, OT-235 with firmware versions M-IDU-1.6.0.3_V1.1 and MH-46360-2.0.3-R5-GP respectively are vulnerable to remote command injection. Commands are executed using pre-login execution and executed with root privileges allowing complete takeover.



- [https://github.com/lionelmusonza/CVE-2023-26866](https://github.com/lionelmusonza/CVE-2023-26866) :  ![starts](https://img.shields.io/github/stars/lionelmusonza/CVE-2023-26866.svg) ![forks](https://img.shields.io/github/forks/lionelmusonza/CVE-2023-26866.svg)

## CVE-2023-26852
 An arbitrary file upload vulnerability in the upload plugin of Textpattern v4.8.8 and below allows attackers to execute arbitrary code by uploading a crafted PHP file.



- [https://github.com/leekenghwa/CVE-2023-26852-Textpattern-v4.8.8-and-](https://github.com/leekenghwa/CVE-2023-26852-Textpattern-v4.8.8-and-) :  ![starts](https://img.shields.io/github/stars/leekenghwa/CVE-2023-26852-Textpattern-v4.8.8-and-.svg) ![forks](https://img.shields.io/github/forks/leekenghwa/CVE-2023-26852-Textpattern-v4.8.8-and-.svg)

## CVE-2023-26818
 Telegram 9.3.1 and 9.4.0 allows attackers to access restricted files, microphone ,or video recording via the DYLD_INSERT_LIBRARIES flag.



- [https://github.com/Zeyad-Azima/CVE-2023-26818](https://github.com/Zeyad-Azima/CVE-2023-26818) :  ![starts](https://img.shields.io/github/stars/Zeyad-Azima/CVE-2023-26818.svg) ![forks](https://img.shields.io/github/forks/Zeyad-Azima/CVE-2023-26818.svg)

## CVE-2023-26692
 ZCBS Zijper Collectie Beheer Systeem (ZCBS), Zijper Publication Management System (ZPBS), and Zijper Image Bank Management System (ZBBS) 4.14k is vulnerable to Cross Site Scripting (XSS).



- [https://github.com/bigzooooz/CVE-2023-26692](https://github.com/bigzooooz/CVE-2023-26692) :  ![starts](https://img.shields.io/github/stars/bigzooooz/CVE-2023-26692.svg) ![forks](https://img.shields.io/github/forks/bigzooooz/CVE-2023-26692.svg)

## CVE-2023-26609
 ABUS TVIP 20000-21150 devices allows remote attackers to execute arbitrary code via shell metacharacters in the /cgi-bin/mft/wireless_mft ap field.



- [https://github.com/D1G17/CVE-2023-26609](https://github.com/D1G17/CVE-2023-26609) :  ![starts](https://img.shields.io/github/stars/D1G17/CVE-2023-26609.svg) ![forks](https://img.shields.io/github/forks/D1G17/CVE-2023-26609.svg)

## CVE-2023-26607
 In the Linux kernel 6.0.8, there is an out-of-bounds read in ntfs_attr_find in fs/ntfs/attrib.c.



- [https://github.com/Trinadh465/linux-4.1.15_CVE-2023-26607](https://github.com/Trinadh465/linux-4.1.15_CVE-2023-26607) :  ![starts](https://img.shields.io/github/stars/Trinadh465/linux-4.1.15_CVE-2023-26607.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/linux-4.1.15_CVE-2023-26607.svg)

## CVE-2023-26604
 systemd before 247 does not adequately block local privilege escalation for some Sudo configurations, e.g., plausible sudoers files in which the "systemctl status" command may be executed. Specifically, systemd does not set LESSSECURE to 1, and thus other programs may be launched from the less program. This presents a substantial security risk when running systemctl from Sudo, because less executes as root when the terminal size is too small to show the complete systemctl output.



- [https://github.com/Zenmovie/CVE-2023-26604](https://github.com/Zenmovie/CVE-2023-26604) :  ![starts](https://img.shields.io/github/stars/Zenmovie/CVE-2023-26604.svg) ![forks](https://img.shields.io/github/forks/Zenmovie/CVE-2023-26604.svg)

## CVE-2023-26602
 ASUS ASMB8 iKVM firmware through 1.14.51 allows remote attackers to execute arbitrary code by using SNMP to create extensions, as demonstrated by snmpset for NET-SNMP-EXTEND-MIB with /bin/sh for command execution.



- [https://github.com/D1G17/CVE-2023-26602](https://github.com/D1G17/CVE-2023-26602) :  ![starts](https://img.shields.io/github/stars/D1G17/CVE-2023-26602.svg) ![forks](https://img.shields.io/github/forks/D1G17/CVE-2023-26602.svg)

## CVE-2023-26563
 The Syncfusion EJ2 Node File Provider 0102271 is vulnerable to filesystem-server.js directory traversal. As a result, an unauthenticated attacker can: - On Windows, list files in any directory, read any file, delete any file, upload any file to any directory accessible by the web server. - On Linux, read any file, download any directory, delete any file, upload any file to any directory accessible by the web server.



- [https://github.com/RupturaInfoSec/CVE-2023-26563-26564-26565](https://github.com/RupturaInfoSec/CVE-2023-26563-26564-26565) :  ![starts](https://img.shields.io/github/stars/RupturaInfoSec/CVE-2023-26563-26564-26565.svg) ![forks](https://img.shields.io/github/forks/RupturaInfoSec/CVE-2023-26563-26564-26565.svg)

## CVE-2023-26469
 In Jorani 1.0.0, an attacker could leverage path traversal to access files and execute code on the server.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/d0rb/CVE-2023-26469](https://github.com/d0rb/CVE-2023-26469) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-26469.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-26469.svg)

## CVE-2023-26360
 Adobe ColdFusion versions 2018 Update 15 (and earlier) and 2021 Update 5 (and earlier) are affected by an Improper Access Control vulnerability that could result in arbitrary code execution in the context of the current user. Exploitation of this issue does not require user interaction.



- [https://github.com/yosef0x01/CVE-2023-26360](https://github.com/yosef0x01/CVE-2023-26360) :  ![starts](https://img.shields.io/github/stars/yosef0x01/CVE-2023-26360.svg) ![forks](https://img.shields.io/github/forks/yosef0x01/CVE-2023-26360.svg)

- [https://github.com/jakabakos/CVE-2023-26360-adobe-coldfusion-rce-exploit](https://github.com/jakabakos/CVE-2023-26360-adobe-coldfusion-rce-exploit) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2023-26360-adobe-coldfusion-rce-exploit.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2023-26360-adobe-coldfusion-rce-exploit.svg)

- [https://github.com/issamjr/CVE-2023-26360](https://github.com/issamjr/CVE-2023-26360) :  ![starts](https://img.shields.io/github/stars/issamjr/CVE-2023-26360.svg) ![forks](https://img.shields.io/github/forks/issamjr/CVE-2023-26360.svg)

## CVE-2023-26269
 Apache James server version 3.7.3 and earlier provides a JMX management service without authentication by default. This allows privilege escalation by a 
malicious local user.

Administrators are advised to disable JMX, or set up a JMX password.

Note that version 3.7.4 onward will set up a JMX password automatically for Guice users.



- [https://github.com/mbadanoiu/CVE-2023-26269](https://github.com/mbadanoiu/CVE-2023-26269) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2023-26269.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2023-26269.svg)

- [https://github.com/mbadanoiu/MAL-010](https://github.com/mbadanoiu/MAL-010) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/MAL-010.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/MAL-010.svg)

## CVE-2023-26262
 An issue was discovered in Sitecore XP/XM 10.3. As an authenticated Sitecore user, a unrestricted language file upload vulnerability exists the can lead to direct code execution on the content management (CM) server.



- [https://github.com/istern/CVE-2023-26262](https://github.com/istern/CVE-2023-26262) :  ![starts](https://img.shields.io/github/stars/istern/CVE-2023-26262.svg) ![forks](https://img.shields.io/github/forks/istern/CVE-2023-26262.svg)

## CVE-2023-26258
 Arcserve UDP through 9.0.6034 allows authentication bypass. The method getVersionInfo at WebServiceImpl/services/FlashServiceImpl leaks the AuthUUID token. This token can be used at /WebServiceImpl/services/VirtualStandbyServiceImpl to obtain a valid session. This session can be used to execute any task as administrator.



- [https://github.com/mdsecactivebreach/CVE-2023-26258-ArcServe](https://github.com/mdsecactivebreach/CVE-2023-26258-ArcServe) :  ![starts](https://img.shields.io/github/stars/mdsecactivebreach/CVE-2023-26258-ArcServe.svg) ![forks](https://img.shields.io/github/forks/mdsecactivebreach/CVE-2023-26258-ArcServe.svg)

## CVE-2023-26256
 An unauthenticated path traversal vulnerability affects the "STAGIL Navigation for Jira - Menu & Themes" plugin before 2.0.52 for Jira. By modifying the fileName parameter to the snjFooterNavigationConfig endpoint, it is possible to traverse and read the file system.



- [https://github.com/0x7eTeam/CVE-2023-26256](https://github.com/0x7eTeam/CVE-2023-26256) :  ![starts](https://img.shields.io/github/stars/0x7eTeam/CVE-2023-26256.svg) ![forks](https://img.shields.io/github/forks/0x7eTeam/CVE-2023-26256.svg)

- [https://github.com/jcad123/CVE-2023-26256](https://github.com/jcad123/CVE-2023-26256) :  ![starts](https://img.shields.io/github/stars/jcad123/CVE-2023-26256.svg) ![forks](https://img.shields.io/github/forks/jcad123/CVE-2023-26256.svg)

- [https://github.com/xhs-d/CVE-2023-26256](https://github.com/xhs-d/CVE-2023-26256) :  ![starts](https://img.shields.io/github/stars/xhs-d/CVE-2023-26256.svg) ![forks](https://img.shields.io/github/forks/xhs-d/CVE-2023-26256.svg)

- [https://github.com/qs119/CVE-2023-26256](https://github.com/qs119/CVE-2023-26256) :  ![starts](https://img.shields.io/github/stars/qs119/CVE-2023-26256.svg) ![forks](https://img.shields.io/github/forks/qs119/CVE-2023-26256.svg)

## CVE-2023-26255
 An unauthenticated path traversal vulnerability affects the "STAGIL Navigation for Jira - Menu & Themes" plugin before 2.0.52 for Jira. By modifying the fileName parameter to the snjCustomDesignConfig endpoint, it is possible to traverse and read the file system.



- [https://github.com/0x7eTeam/CVE-2023-26256](https://github.com/0x7eTeam/CVE-2023-26256) :  ![starts](https://img.shields.io/github/stars/0x7eTeam/CVE-2023-26256.svg) ![forks](https://img.shields.io/github/forks/0x7eTeam/CVE-2023-26256.svg)

- [https://github.com/jcad123/CVE-2023-26256](https://github.com/jcad123/CVE-2023-26256) :  ![starts](https://img.shields.io/github/stars/jcad123/CVE-2023-26256.svg) ![forks](https://img.shields.io/github/forks/jcad123/CVE-2023-26256.svg)

- [https://github.com/tucommenceapousser/CVE-2023-26255-Exp](https://github.com/tucommenceapousser/CVE-2023-26255-Exp) :  ![starts](https://img.shields.io/github/stars/tucommenceapousser/CVE-2023-26255-Exp.svg) ![forks](https://img.shields.io/github/forks/tucommenceapousser/CVE-2023-26255-Exp.svg)

- [https://github.com/Nian-Stars/CVE-2023-26255-6](https://github.com/Nian-Stars/CVE-2023-26255-6) :  ![starts](https://img.shields.io/github/stars/Nian-Stars/CVE-2023-26255-6.svg) ![forks](https://img.shields.io/github/forks/Nian-Stars/CVE-2023-26255-6.svg)

## CVE-2023-26144
 Versions of the package graphql from 16.3.0 and before 16.8.1 are vulnerable to Denial of Service (DoS) due to insufficient checks in the OverlappingFieldsCanBeMergedRule.ts file when parsing large queries. This vulnerability allows an attacker to degrade system performance.**Note:** It was not proven that this vulnerability can crash the process.



- [https://github.com/tadhglewis/apollo-koa-minimal](https://github.com/tadhglewis/apollo-koa-minimal) :  ![starts](https://img.shields.io/github/stars/tadhglewis/apollo-koa-minimal.svg) ![forks](https://img.shields.io/github/forks/tadhglewis/apollo-koa-minimal.svg)

## CVE-2023-26136
 Versions of the package tough-cookie before 4.1.3 are vulnerable to Prototype Pollution due to improper handling of Cookies when using CookieJar in rejectPublicSuffixes=false mode. This issue arises from the manner in which the objects are initialized.



- [https://github.com/CUCUMBERanOrSNCompany/SealSecurityAssignment](https://github.com/CUCUMBERanOrSNCompany/SealSecurityAssignment) :  ![starts](https://img.shields.io/github/stars/CUCUMBERanOrSNCompany/SealSecurityAssignment.svg) ![forks](https://img.shields.io/github/forks/CUCUMBERanOrSNCompany/SealSecurityAssignment.svg)

- [https://github.com/guy2610/tough-cookie-patch-cve-2023-26136](https://github.com/guy2610/tough-cookie-patch-cve-2023-26136) :  ![starts](https://img.shields.io/github/stars/guy2610/tough-cookie-patch-cve-2023-26136.svg) ![forks](https://img.shields.io/github/forks/guy2610/tough-cookie-patch-cve-2023-26136.svg)

- [https://github.com/ronmadar/Open-Source-Seal-Security](https://github.com/ronmadar/Open-Source-Seal-Security) :  ![starts](https://img.shields.io/github/stars/ronmadar/Open-Source-Seal-Security.svg) ![forks](https://img.shields.io/github/forks/ronmadar/Open-Source-Seal-Security.svg)

## CVE-2023-26067
 Certain Lexmark devices through 2023-02-19 mishandle Input Validation (issue 1 of 4).



- [https://github.com/horizon3ai/CVE-2023-26067](https://github.com/horizon3ai/CVE-2023-26067) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2023-26067.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2023-26067.svg)

## CVE-2023-26049
 Jetty is a java based web server and servlet engine. Nonstandard cookie parsing in Jetty may allow an attacker to smuggle cookies within other cookies, or otherwise perform unintended behavior by tampering with the cookie parsing mechanism. If Jetty sees a cookie VALUE that starts with `"` (double quote), it will continue to read the cookie string until it sees a closing quote -- even if a semicolon is encountered. So, a cookie header such as: `DISPLAY_LANGUAGE="b; JSESSIONID=1337; c=d"` will be parsed as one cookie, with the name DISPLAY_LANGUAGE and a value of b; JSESSIONID=1337; c=d instead of 3 separate cookies. This has security implications because if, say, JSESSIONID is an HttpOnly cookie, and the DISPLAY_LANGUAGE cookie value is rendered on the page, an attacker can smuggle the JSESSIONID cookie into the DISPLAY_LANGUAGE cookie and thereby exfiltrate it. This is significant when an intermediary is enacting some policy based on cookies, so a smuggled cookie can bypass that policy yet still be seen by the Jetty server or its logging system. This issue has been addressed in versions 9.4.51, 10.0.14, 11.0.14, and 12.0.0.beta0 and users are advised to upgrade. There are no known workarounds for this issue.



- [https://github.com/uthrasri/jetty-9.4.31.v20200723_CVE-2023-26049](https://github.com/uthrasri/jetty-9.4.31.v20200723_CVE-2023-26049) :  ![starts](https://img.shields.io/github/stars/uthrasri/jetty-9.4.31.v20200723_CVE-2023-26049.svg) ![forks](https://img.shields.io/github/forks/uthrasri/jetty-9.4.31.v20200723_CVE-2023-26049.svg)

## CVE-2023-26048
 Jetty is a java based web server and servlet engine. In affected versions servlets with multipart support (e.g. annotated with `@MultipartConfig`) that call `HttpServletRequest.getParameter()` or `HttpServletRequest.getParts()` may cause `OutOfMemoryError` when the client sends a multipart request with a part that has a name but no filename and very large content. This happens even with the default settings of `fileSizeThreshold=0` which should stream the whole part content to disk. An attacker client may send a large multipart request and cause the server to throw `OutOfMemoryError`. However, the server may be able to recover after the `OutOfMemoryError` and continue its service -- although it may take some time. This issue has been patched in versions 9.4.51, 10.0.14, and 11.0.14. Users are advised to upgrade. Users unable to upgrade may set the multipart parameter `maxRequestSize` which must be set to a non-negative value, so the whole multipart content is limited (although still read into memory).



- [https://github.com/Trinadh465/jetty_9.4.31_CVE-2023-26048](https://github.com/Trinadh465/jetty_9.4.31_CVE-2023-26048) :  ![starts](https://img.shields.io/github/stars/Trinadh465/jetty_9.4.31_CVE-2023-26048.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/jetty_9.4.31_CVE-2023-26048.svg)

## CVE-2023-26035
 ZoneMinder is a free, open source Closed-circuit television software application for Linux which supports IP, USB and Analog cameras. Versions prior to 1.36.33 and 1.37.33 are vulnerable to Unauthenticated Remote Code Execution via Missing Authorization. There are no permissions check on the snapshot action, which expects an id to fetch an existing monitor but can be passed an object to create a new one instead. TriggerOn ends up calling shell_exec using the supplied Id. This issue is fixed in This issue is fixed in versions 1.36.33 and 1.37.33.



- [https://github.com/rvizx/CVE-2023-26035](https://github.com/rvizx/CVE-2023-26035) :  ![starts](https://img.shields.io/github/stars/rvizx/CVE-2023-26035.svg) ![forks](https://img.shields.io/github/forks/rvizx/CVE-2023-26035.svg)

- [https://github.com/heapbytes/CVE-2023-26035](https://github.com/heapbytes/CVE-2023-26035) :  ![starts](https://img.shields.io/github/stars/heapbytes/CVE-2023-26035.svg) ![forks](https://img.shields.io/github/forks/heapbytes/CVE-2023-26035.svg)

- [https://github.com/Yuma-Tsushima07/CVE-2023-26035](https://github.com/Yuma-Tsushima07/CVE-2023-26035) :  ![starts](https://img.shields.io/github/stars/Yuma-Tsushima07/CVE-2023-26035.svg) ![forks](https://img.shields.io/github/forks/Yuma-Tsushima07/CVE-2023-26035.svg)

- [https://github.com/0xfalafel/zoneminder_CVE-2023-26035](https://github.com/0xfalafel/zoneminder_CVE-2023-26035) :  ![starts](https://img.shields.io/github/stars/0xfalafel/zoneminder_CVE-2023-26035.svg) ![forks](https://img.shields.io/github/forks/0xfalafel/zoneminder_CVE-2023-26035.svg)

- [https://github.com/m3m0o/zoneminder-snapshots-rce-poc](https://github.com/m3m0o/zoneminder-snapshots-rce-poc) :  ![starts](https://img.shields.io/github/stars/m3m0o/zoneminder-snapshots-rce-poc.svg) ![forks](https://img.shields.io/github/forks/m3m0o/zoneminder-snapshots-rce-poc.svg)

## CVE-2023-26025
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/ka7ana/CVE-2023-36025](https://github.com/ka7ana/CVE-2023-36025) :  ![starts](https://img.shields.io/github/stars/ka7ana/CVE-2023-36025.svg) ![forks](https://img.shields.io/github/forks/ka7ana/CVE-2023-36025.svg)

## CVE-2023-25950
 HTTP request/response smuggling vulnerability in HAProxy version 2.7.0, and 2.6.1 to 2.6.7 allows a remote attacker to alter a legitimate user's request. As a result, the attacker may obtain sensitive information or cause a denial-of-service (DoS) condition.



- [https://github.com/dhmosfunk/HTTP3ONSTEROIDS](https://github.com/dhmosfunk/HTTP3ONSTEROIDS) :  ![starts](https://img.shields.io/github/stars/dhmosfunk/HTTP3ONSTEROIDS.svg) ![forks](https://img.shields.io/github/forks/dhmosfunk/HTTP3ONSTEROIDS.svg)

## CVE-2023-25826
 Due to insufficient validation of parameters passed to the legacy HTTP query API, it is possible to inject crafted OS commands into multiple parameters and execute malicious code on the OpenTSDB host system. This exploit exists due to an incomplete fix that was made when this vulnerability was previously disclosed as CVE-2020-35476. Regex validation that was implemented to restrict allowed input to the query API does not work as intended, allowing crafted commands to bypass validation.



- [https://github.com/ErikWynter/opentsdb_key_cmd_injection](https://github.com/ErikWynter/opentsdb_key_cmd_injection) :  ![starts](https://img.shields.io/github/stars/ErikWynter/opentsdb_key_cmd_injection.svg) ![forks](https://img.shields.io/github/forks/ErikWynter/opentsdb_key_cmd_injection.svg)

## CVE-2023-25813
 Sequelize is a Node.js ORM tool. In versions prior to 6.19.1 a SQL injection exploit exists related to replacements. Parameters which are passed through replacements are not properly escaped which can lead to arbitrary SQL injection depending on the specific queries in use. The issue has been fixed in Sequelize 6.19.1. Users are advised to upgrade. Users unable to upgrade should not use the `replacements` and the `where` option in the same query.



- [https://github.com/White-BAO/CVE-2023-25813](https://github.com/White-BAO/CVE-2023-25813) :  ![starts](https://img.shields.io/github/stars/White-BAO/CVE-2023-25813.svg) ![forks](https://img.shields.io/github/forks/White-BAO/CVE-2023-25813.svg)

- [https://github.com/pbj2647/CVE-2023-25813](https://github.com/pbj2647/CVE-2023-25813) :  ![starts](https://img.shields.io/github/stars/pbj2647/CVE-2023-25813.svg) ![forks](https://img.shields.io/github/forks/pbj2647/CVE-2023-25813.svg)

- [https://github.com/sea-middle/cve-2023-25813](https://github.com/sea-middle/cve-2023-25813) :  ![starts](https://img.shields.io/github/stars/sea-middle/cve-2023-25813.svg) ![forks](https://img.shields.io/github/forks/sea-middle/cve-2023-25813.svg)

- [https://github.com/numbbvi/CVE-2023-25813](https://github.com/numbbvi/CVE-2023-25813) :  ![starts](https://img.shields.io/github/stars/numbbvi/CVE-2023-25813.svg) ![forks](https://img.shields.io/github/forks/numbbvi/CVE-2023-25813.svg)

- [https://github.com/bde574786/Sequelize-1day-CVE-2023-25813](https://github.com/bde574786/Sequelize-1day-CVE-2023-25813) :  ![starts](https://img.shields.io/github/stars/bde574786/Sequelize-1day-CVE-2023-25813.svg) ![forks](https://img.shields.io/github/forks/bde574786/Sequelize-1day-CVE-2023-25813.svg)

## CVE-2023-25725
 HAProxy before 2.7.3 may allow a bypass of access control because HTTP/1 headers are inadvertently lost in some situations, aka "request smuggling." The HTTP header parsers in HAProxy may accept empty header field names, which could be used to truncate the list of HTTP headers and thus make some headers disappear after being parsed and processed for HTTP/1.0 and HTTP/1.1. For HTTP/2 and HTTP/3, the impact is limited because the headers disappear before being parsed and processed, as if they had not been sent by the client. The fixed versions are 2.7.3, 2.6.9, 2.5.12, 2.4.22, 2.2.29, and 2.0.31.



- [https://github.com/sgwgsw/LAB-CVE-2023-25725](https://github.com/sgwgsw/LAB-CVE-2023-25725) :  ![starts](https://img.shields.io/github/stars/sgwgsw/LAB-CVE-2023-25725.svg) ![forks](https://img.shields.io/github/forks/sgwgsw/LAB-CVE-2023-25725.svg)

## CVE-2023-25690
 Some mod_proxy configurations on Apache HTTP Server versions 2.4.0 through 2.4.55 allow a HTTP Request Smuggling attack.




Configurations are affected when mod_proxy is enabled along with some form of RewriteRule
 or ProxyPassMatch in which a non-specific pattern matches
 some portion of the user-supplied request-target (URL) data and is then
 re-inserted into the proxied request-target using variable 
substitution. For example, something like:




RewriteEngine on
RewriteRule "^/here/(.*)" "http://example.com:8080/elsewhere?$1"; [P]
ProxyPassReverse /here/ http://example.com:8080/


Request splitting/smuggling could result in bypass of access controls in the proxy server, proxying unintended URLs to existing origin servers, and cache poisoning. Users are recommended to update to at least version 2.4.56 of Apache HTTP Server.



- [https://github.com/dhmosfunk/CVE-2023-25690-POC](https://github.com/dhmosfunk/CVE-2023-25690-POC) :  ![starts](https://img.shields.io/github/stars/dhmosfunk/CVE-2023-25690-POC.svg) ![forks](https://img.shields.io/github/forks/dhmosfunk/CVE-2023-25690-POC.svg)

- [https://github.com/thanhlam-attt/CVE-2023-25690](https://github.com/thanhlam-attt/CVE-2023-25690) :  ![starts](https://img.shields.io/github/stars/thanhlam-attt/CVE-2023-25690.svg) ![forks](https://img.shields.io/github/forks/thanhlam-attt/CVE-2023-25690.svg)

- [https://github.com/tbachvarova/linux-apache-fix-mod_rewrite-spaceInURL](https://github.com/tbachvarova/linux-apache-fix-mod_rewrite-spaceInURL) :  ![starts](https://img.shields.io/github/stars/tbachvarova/linux-apache-fix-mod_rewrite-spaceInURL.svg) ![forks](https://img.shields.io/github/forks/tbachvarova/linux-apache-fix-mod_rewrite-spaceInURL.svg)

- [https://github.com/oOCyginXOo/CVE-2023-25690-POC](https://github.com/oOCyginXOo/CVE-2023-25690-POC) :  ![starts](https://img.shields.io/github/stars/oOCyginXOo/CVE-2023-25690-POC.svg) ![forks](https://img.shields.io/github/forks/oOCyginXOo/CVE-2023-25690-POC.svg)

## CVE-2023-25610
 A buffer underwrite ('buffer underflow') vulnerability in the administrative interface of Fortinet FortiOS version 7.2.0 through 7.2.3, version 7.0.0 through 7.0.6, version 6.4.0 through 6.4.11 and version 6.2.12 and below, FortiProxy version 7.2.0 through 7.2.2, version 7.0.0 through 7.0.8, version 2.0.12 and below and FortiOS-6K7K version 7.0.5, version 6.4.0 through 6.4.10 and version 6.2.0 through 6.2.10 and below allows a remote unauthenticated attacker to execute arbitrary code or commands via specifically crafted requests.



- [https://github.com/qi4L/CVE-2023-25610](https://github.com/qi4L/CVE-2023-25610) :  ![starts](https://img.shields.io/github/stars/qi4L/CVE-2023-25610.svg) ![forks](https://img.shields.io/github/forks/qi4L/CVE-2023-25610.svg)

## CVE-2023-25292
 Reflected Cross Site Scripting (XSS) in Intermesh BV Group-Office version 6.6.145, allows attackers to gain escalated privileges and gain sensitive information via the GO_LANGUAGE cookie.



- [https://github.com/tucommenceapousser/CVE-2023-25292](https://github.com/tucommenceapousser/CVE-2023-25292) :  ![starts](https://img.shields.io/github/stars/tucommenceapousser/CVE-2023-25292.svg) ![forks](https://img.shields.io/github/forks/tucommenceapousser/CVE-2023-25292.svg)

- [https://github.com/brainkok/CVE-2023-25292](https://github.com/brainkok/CVE-2023-25292) :  ![starts](https://img.shields.io/github/stars/brainkok/CVE-2023-25292.svg) ![forks](https://img.shields.io/github/forks/brainkok/CVE-2023-25292.svg)

## CVE-2023-25263
 In Stimulsoft Designer (Desktop) 2023.1.5, and 2023.1.4, once an attacker decompiles the Stimulsoft.report.dll the attacker is able to decrypt any connectionstring stored in .mrt files since a static secret is used. The secret does not differ between the tested versions and different operating systems.



- [https://github.com/trustcves/CVE-2023-25263](https://github.com/trustcves/CVE-2023-25263) :  ![starts](https://img.shields.io/github/stars/trustcves/CVE-2023-25263.svg) ![forks](https://img.shields.io/github/forks/trustcves/CVE-2023-25263.svg)

## CVE-2023-25262
 Stimulsoft GmbH Stimulsoft Designer (Web) 2023.1.3 is vulnerable to Server Side Request Forgery (SSRF). TThe Reporting Designer (Web) offers the possibility to embed sources from external locations. If the user chooses an external location, the request to that resource is performed by the server rather than the client. Therefore, the server causes outbound traffic and potentially imports data. An attacker may also leverage this behaviour to exfiltrate data of machines on the internal network of the server hosting the Stimulsoft Reporting Designer (Web).



- [https://github.com/trustcves/CVE-2023-25262](https://github.com/trustcves/CVE-2023-25262) :  ![starts](https://img.shields.io/github/stars/trustcves/CVE-2023-25262.svg) ![forks](https://img.shields.io/github/forks/trustcves/CVE-2023-25262.svg)

## CVE-2023-25261
 Certain Stimulsoft GmbH products are affected by: Remote Code Execution. This affects Stimulsoft Designer (Desktop) 2023.1.4 and Stimulsoft Designer (Web) 2023.1.3 and Stimulsoft Viewer (Web) 2023.1.3. Access to the local file system is not prohibited in any way. Therefore, an attacker may include source code which reads or writes local directories and files. It is also possible for the attacker to prepare a report which has a variable that holds the gathered data and render it in the report.



- [https://github.com/trustcves/CVE-2023-25261](https://github.com/trustcves/CVE-2023-25261) :  ![starts](https://img.shields.io/github/stars/trustcves/CVE-2023-25261.svg) ![forks](https://img.shields.io/github/forks/trustcves/CVE-2023-25261.svg)

## CVE-2023-25260
 Stimulsoft Designer (Web) 2023.1.3 is vulnerable to Local File Inclusion.



- [https://github.com/trustcves/CVE-2023-25260](https://github.com/trustcves/CVE-2023-25260) :  ![starts](https://img.shields.io/github/stars/trustcves/CVE-2023-25260.svg) ![forks](https://img.shields.io/github/forks/trustcves/CVE-2023-25260.svg)

## CVE-2023-25234
 Tenda AC500 V2.0.1.9(1307) is vulnerable to Buffer Overflow in function fromAddressNat via parameters entrys and mitInterface.



- [https://github.com/FzBacon/CVE-2023-25234_Tenda_AC6_stack_overflow](https://github.com/FzBacon/CVE-2023-25234_Tenda_AC6_stack_overflow) :  ![starts](https://img.shields.io/github/stars/FzBacon/CVE-2023-25234_Tenda_AC6_stack_overflow.svg) ![forks](https://img.shields.io/github/forks/FzBacon/CVE-2023-25234_Tenda_AC6_stack_overflow.svg)

## CVE-2023-25203
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Trackflaw/CVE-2023-25203](https://github.com/Trackflaw/CVE-2023-25203) :  ![starts](https://img.shields.io/github/stars/Trackflaw/CVE-2023-25203.svg) ![forks](https://img.shields.io/github/forks/Trackflaw/CVE-2023-25203.svg)

## CVE-2023-25202
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Trackflaw/CVE-2023-25202](https://github.com/Trackflaw/CVE-2023-25202) :  ![starts](https://img.shields.io/github/stars/Trackflaw/CVE-2023-25202.svg) ![forks](https://img.shields.io/github/forks/Trackflaw/CVE-2023-25202.svg)

## CVE-2023-25194
 A possible security vulnerability has been identified in Apache Kafka Connect API.
This requires access to a Kafka Connect worker, and the ability to create/modify connectors on it with an arbitrary Kafka client SASL JAAS config
and a SASL-based security protocol, which has been possible on Kafka Connect clusters since Apache Kafka Connect 2.3.0.
When configuring the connector via the Kafka Connect REST API, an authenticated operator can set the `sasl.jaas.config`
property for any of the connector's Kafka clients to "com.sun.security.auth.module.JndiLoginModule", which can be done via the
`producer.override.sasl.jaas.config`, `consumer.override.sasl.jaas.config`, or `admin.override.sasl.jaas.config` properties.
This will allow the server to connect to the attacker's LDAP server
and deserialize the LDAP response, which the attacker can use to execute java deserialization gadget chains on the Kafka connect server.
Attacker can cause unrestricted deserialization of untrusted data (or) RCE vulnerability when there are gadgets in the classpath.

Since Apache Kafka 3.0.0, users are allowed to specify these properties in connector configurations for Kafka Connect clusters running with out-of-the-box
configurations. Before Apache Kafka 3.0.0, users may not specify these properties unless the Kafka Connect cluster has been reconfigured with a connector
client override policy that permits them.

Since Apache Kafka 3.4.0, we have added a system property ("-Dorg.apache.kafka.disallowed.login.modules") to disable the problematic login modules usage
in SASL JAAS configuration. Also by default "com.sun.security.auth.module.JndiLoginModule" is disabled in Apache Kafka Connect 3.4.0. 

We advise the Kafka Connect users to validate connector configurations and only allow trusted JNDI configurations. Also examine connector dependencies for 
vulnerable versions and either upgrade their connectors, upgrading that specific dependency, or removing the connectors as options for remediation. Finally,
in addition to leveraging the "org.apache.kafka.disallowed.login.modules" system property, Kafka Connect users can also implement their own connector
client config override policy, which can be used to control which Kafka client properties can be overridden directly in a connector config and which cannot.




- [https://github.com/ohnonoyesyes/CVE-2023-25194](https://github.com/ohnonoyesyes/CVE-2023-25194) :  ![starts](https://img.shields.io/github/stars/ohnonoyesyes/CVE-2023-25194.svg) ![forks](https://img.shields.io/github/forks/ohnonoyesyes/CVE-2023-25194.svg)

- [https://github.com/vulncheck-oss/cve-2023-25194](https://github.com/vulncheck-oss/cve-2023-25194) :  ![starts](https://img.shields.io/github/stars/vulncheck-oss/cve-2023-25194.svg) ![forks](https://img.shields.io/github/forks/vulncheck-oss/cve-2023-25194.svg)

- [https://github.com/Avento/Apache_Druid_JNDI_Vuln](https://github.com/Avento/Apache_Druid_JNDI_Vuln) :  ![starts](https://img.shields.io/github/stars/Avento/Apache_Druid_JNDI_Vuln.svg) ![forks](https://img.shields.io/github/forks/Avento/Apache_Druid_JNDI_Vuln.svg)

- [https://github.com/YongYe-Security/CVE-2023-25194](https://github.com/YongYe-Security/CVE-2023-25194) :  ![starts](https://img.shields.io/github/stars/YongYe-Security/CVE-2023-25194.svg) ![forks](https://img.shields.io/github/forks/YongYe-Security/CVE-2023-25194.svg)

## CVE-2023-25158
 GeoTools is an open source Java library that provides tools for geospatial data. GeoTools includes support for OGC Filter expression language parsing, encoding and execution against a range of datastore. SQL Injection Vulnerabilities have been found when executing OGC Filters with JDBCDataStore implementations. Users are advised to upgrade to either version 27.4 or to 28.2 to resolve this issue. Users unable to upgrade may disable `encode functions` for PostGIS DataStores or enable `prepared statements` for JDBCDataStores as a partial mitigation.



- [https://github.com/murataydemir/CVE-2023-25157-and-CVE-2023-25158](https://github.com/murataydemir/CVE-2023-25157-and-CVE-2023-25158) :  ![starts](https://img.shields.io/github/stars/murataydemir/CVE-2023-25157-and-CVE-2023-25158.svg) ![forks](https://img.shields.io/github/forks/murataydemir/CVE-2023-25157-and-CVE-2023-25158.svg)

## CVE-2023-25157
 GeoServer is an open source software server written in Java that allows users to share and edit geospatial data. GeoServer includes support for the OGC Filter expression language and the OGC Common Query Language (CQL) as part of the Web Feature Service (WFS) and Web Map Service (WMS) protocols.  CQL is also supported through the Web Coverage Service (WCS) protocol for ImageMosaic coverages. Users are advised to upgrade to either version 2.21.4, or version 2.22.2 to resolve this issue. Users unable to upgrade should disable the PostGIS Datastore *encode functions* setting to mitigate ``strEndsWith``, ``strStartsWith`` and ``PropertyIsLike `` misuse and enable the PostGIS DataStore *preparedStatements* setting to mitigate the ``FeatureId`` misuse.



- [https://github.com/win3zz/CVE-2023-25157](https://github.com/win3zz/CVE-2023-25157) :  ![starts](https://img.shields.io/github/stars/win3zz/CVE-2023-25157.svg) ![forks](https://img.shields.io/github/forks/win3zz/CVE-2023-25157.svg)

- [https://github.com/murataydemir/CVE-2023-25157-and-CVE-2023-25158](https://github.com/murataydemir/CVE-2023-25157-and-CVE-2023-25158) :  ![starts](https://img.shields.io/github/stars/murataydemir/CVE-2023-25157-and-CVE-2023-25158.svg) ![forks](https://img.shields.io/github/forks/murataydemir/CVE-2023-25157-and-CVE-2023-25158.svg)

- [https://github.com/0x2458bughunt/CVE-2023-25157](https://github.com/0x2458bughunt/CVE-2023-25157) :  ![starts](https://img.shields.io/github/stars/0x2458bughunt/CVE-2023-25157.svg) ![forks](https://img.shields.io/github/forks/0x2458bughunt/CVE-2023-25157.svg)

- [https://github.com/charis3306/CVE-2023-25157](https://github.com/charis3306/CVE-2023-25157) :  ![starts](https://img.shields.io/github/stars/charis3306/CVE-2023-25157.svg) ![forks](https://img.shields.io/github/forks/charis3306/CVE-2023-25157.svg)

- [https://github.com/7imbitz/CVE-2023-25157-checker](https://github.com/7imbitz/CVE-2023-25157-checker) :  ![starts](https://img.shields.io/github/stars/7imbitz/CVE-2023-25157-checker.svg) ![forks](https://img.shields.io/github/forks/7imbitz/CVE-2023-25157-checker.svg)

- [https://github.com/dr-cable-tv/Geoserver-CVE-2023-25157](https://github.com/dr-cable-tv/Geoserver-CVE-2023-25157) :  ![starts](https://img.shields.io/github/stars/dr-cable-tv/Geoserver-CVE-2023-25157.svg) ![forks](https://img.shields.io/github/forks/dr-cable-tv/Geoserver-CVE-2023-25157.svg)

- [https://github.com/custiya/geoserver-CVE-2023-25157](https://github.com/custiya/geoserver-CVE-2023-25157) :  ![starts](https://img.shields.io/github/stars/custiya/geoserver-CVE-2023-25157.svg) ![forks](https://img.shields.io/github/forks/custiya/geoserver-CVE-2023-25157.svg)

- [https://github.com/Rubikcuv5/CVE-2023-25157](https://github.com/Rubikcuv5/CVE-2023-25157) :  ![starts](https://img.shields.io/github/stars/Rubikcuv5/CVE-2023-25157.svg) ![forks](https://img.shields.io/github/forks/Rubikcuv5/CVE-2023-25157.svg)

## CVE-2023-25136
 OpenSSH server (sshd) 9.1 introduced a double-free vulnerability during options.kex_algorithms handling. This is fixed in OpenSSH 9.2. The double free can be leveraged, by an unauthenticated remote attacker in the default configuration, to jump to any location in the sshd address space. One third-party report states "remote code execution is theoretically possible."



- [https://github.com/Christbowel/CVE-2023-25136](https://github.com/Christbowel/CVE-2023-25136) :  ![starts](https://img.shields.io/github/stars/Christbowel/CVE-2023-25136.svg) ![forks](https://img.shields.io/github/forks/Christbowel/CVE-2023-25136.svg)

- [https://github.com/adhikara13/CVE-2023-25136](https://github.com/adhikara13/CVE-2023-25136) :  ![starts](https://img.shields.io/github/stars/adhikara13/CVE-2023-25136.svg) ![forks](https://img.shields.io/github/forks/adhikara13/CVE-2023-25136.svg)

- [https://github.com/jfrog/jfrog-CVE-2023-25136-OpenSSH_Double-Free](https://github.com/jfrog/jfrog-CVE-2023-25136-OpenSSH_Double-Free) :  ![starts](https://img.shields.io/github/stars/jfrog/jfrog-CVE-2023-25136-OpenSSH_Double-Free.svg) ![forks](https://img.shields.io/github/forks/jfrog/jfrog-CVE-2023-25136-OpenSSH_Double-Free.svg)

- [https://github.com/nhakobyan685/CVE-2023-25136](https://github.com/nhakobyan685/CVE-2023-25136) :  ![starts](https://img.shields.io/github/stars/nhakobyan685/CVE-2023-25136.svg) ![forks](https://img.shields.io/github/forks/nhakobyan685/CVE-2023-25136.svg)

- [https://github.com/H4K6/CVE-2023-25136](https://github.com/H4K6/CVE-2023-25136) :  ![starts](https://img.shields.io/github/stars/H4K6/CVE-2023-25136.svg) ![forks](https://img.shields.io/github/forks/H4K6/CVE-2023-25136.svg)

- [https://github.com/malvika-thakur/CVE-2023-25136](https://github.com/malvika-thakur/CVE-2023-25136) :  ![starts](https://img.shields.io/github/stars/malvika-thakur/CVE-2023-25136.svg) ![forks](https://img.shields.io/github/forks/malvika-thakur/CVE-2023-25136.svg)

- [https://github.com/ticofookfook/CVE-2023-25136](https://github.com/ticofookfook/CVE-2023-25136) :  ![starts](https://img.shields.io/github/stars/ticofookfook/CVE-2023-25136.svg) ![forks](https://img.shields.io/github/forks/ticofookfook/CVE-2023-25136.svg)

- [https://github.com/axylisdead/CVE-2023-25136_POC](https://github.com/axylisdead/CVE-2023-25136_POC) :  ![starts](https://img.shields.io/github/stars/axylisdead/CVE-2023-25136_POC.svg) ![forks](https://img.shields.io/github/forks/axylisdead/CVE-2023-25136_POC.svg)

- [https://github.com/Business1sg00d/CVE-2023-25136](https://github.com/Business1sg00d/CVE-2023-25136) :  ![starts](https://img.shields.io/github/stars/Business1sg00d/CVE-2023-25136.svg) ![forks](https://img.shields.io/github/forks/Business1sg00d/CVE-2023-25136.svg)

## CVE-2023-24998
 Apache Commons FileUpload before 1.5 does not limit the number of request parts to be processed resulting in the possibility of an attacker triggering a DoS with a malicious upload or series of uploads.




Note that, like all of the file upload limits, the
          new configuration option (FileUploadBase#setFileCountMax) is not
          enabled by default and must be explicitly configured.



- [https://github.com/nice1st/CVE-2023-24998](https://github.com/nice1st/CVE-2023-24998) :  ![starts](https://img.shields.io/github/stars/nice1st/CVE-2023-24998.svg) ![forks](https://img.shields.io/github/forks/nice1st/CVE-2023-24998.svg)

## CVE-2023-24955
 Microsoft SharePoint Server Remote Code Execution Vulnerability



- [https://github.com/Chocapikk/CVE-2023-29357](https://github.com/Chocapikk/CVE-2023-29357) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-29357.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-29357.svg)

- [https://github.com/former-farmer/CVE-2023-24955-PoC](https://github.com/former-farmer/CVE-2023-24955-PoC) :  ![starts](https://img.shields.io/github/stars/former-farmer/CVE-2023-24955-PoC.svg) ![forks](https://img.shields.io/github/forks/former-farmer/CVE-2023-24955-PoC.svg)

## CVE-2023-24932
 Secure Boot Security Feature Bypass Vulnerability



- [https://github.com/Wack0/CVE-2022-21894](https://github.com/Wack0/CVE-2022-21894) :  ![starts](https://img.shields.io/github/stars/Wack0/CVE-2022-21894.svg) ![forks](https://img.shields.io/github/forks/Wack0/CVE-2022-21894.svg)

- [https://github.com/ajf8729/BlackLotus](https://github.com/ajf8729/BlackLotus) :  ![starts](https://img.shields.io/github/stars/ajf8729/BlackLotus.svg) ![forks](https://img.shields.io/github/forks/ajf8729/BlackLotus.svg)

## CVE-2023-24871
 Windows Bluetooth Service Remote Code Execution Vulnerability



- [https://github.com/ynwarcs/CVE-2023-24871](https://github.com/ynwarcs/CVE-2023-24871) :  ![starts](https://img.shields.io/github/stars/ynwarcs/CVE-2023-24871.svg) ![forks](https://img.shields.io/github/forks/ynwarcs/CVE-2023-24871.svg)

## CVE-2023-24780
 Funadmin v3.2.0 was discovered to contain a SQL injection vulnerability via the id parameter at /databases/table/columns.



- [https://github.com/csffs/CVE-2023-24775-and-CVE-2023-24780](https://github.com/csffs/CVE-2023-24775-and-CVE-2023-24780) :  ![starts](https://img.shields.io/github/stars/csffs/CVE-2023-24775-and-CVE-2023-24780.svg) ![forks](https://img.shields.io/github/forks/csffs/CVE-2023-24775-and-CVE-2023-24780.svg)

## CVE-2023-24775
 Funadmin v3.2.0 was discovered to contain a SQL injection vulnerability via the selectFields parameter at \member\Member.php.



- [https://github.com/csffs/CVE-2023-24775-and-CVE-2023-24780](https://github.com/csffs/CVE-2023-24775-and-CVE-2023-24780) :  ![starts](https://img.shields.io/github/stars/csffs/CVE-2023-24775-and-CVE-2023-24780.svg) ![forks](https://img.shields.io/github/forks/csffs/CVE-2023-24775-and-CVE-2023-24780.svg)

## CVE-2023-24774
 Funadmin v3.2.0 was discovered to contain a SQL injection vulnerability via the selectFields parameter at \controller\auth\Auth.php.



- [https://github.com/csffs/CVE-2023-24775-and-CVE-2023-24780](https://github.com/csffs/CVE-2023-24775-and-CVE-2023-24780) :  ![starts](https://img.shields.io/github/stars/csffs/CVE-2023-24775-and-CVE-2023-24780.svg) ![forks](https://img.shields.io/github/forks/csffs/CVE-2023-24775-and-CVE-2023-24780.svg)

## CVE-2023-24749
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/mahaloz/netgear-pwnagent](https://github.com/mahaloz/netgear-pwnagent) :  ![starts](https://img.shields.io/github/stars/mahaloz/netgear-pwnagent.svg) ![forks](https://img.shields.io/github/forks/mahaloz/netgear-pwnagent.svg)

## CVE-2023-24709
 An issue found in Paradox Security Systems IPR512 allows attackers to cause a denial of service via the login.html and login.xml parameters.



- [https://github.com/DRAGOWN/CVE-2023-24709-PoC](https://github.com/DRAGOWN/CVE-2023-24709-PoC) :  ![starts](https://img.shields.io/github/stars/DRAGOWN/CVE-2023-24709-PoC.svg) ![forks](https://img.shields.io/github/forks/DRAGOWN/CVE-2023-24709-PoC.svg)

## CVE-2023-24706
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/hatjwe/CVE-2023-24706](https://github.com/hatjwe/CVE-2023-24706) :  ![starts](https://img.shields.io/github/stars/hatjwe/CVE-2023-24706.svg) ![forks](https://img.shields.io/github/forks/hatjwe/CVE-2023-24706.svg)

## CVE-2023-24610
 NOSH 4a5cfdb allows remote authenticated users to execute PHP arbitrary code via the "practice logo" upload feature. The client-side checks can be bypassed. This may allow attackers to steal Protected Health Information because the product is for health charting.



- [https://github.com/abbisQQ/CVE-2023-24610](https://github.com/abbisQQ/CVE-2023-24610) :  ![starts](https://img.shields.io/github/stars/abbisQQ/CVE-2023-24610.svg) ![forks](https://img.shields.io/github/forks/abbisQQ/CVE-2023-24610.svg)

## CVE-2023-24538
 Templates do not properly consider backticks (`) as Javascript string delimiters, and do not escape them as expected. Backticks are used, since ES6, for JS template literals. If a template contains a Go template action within a Javascript template literal, the contents of the action can be used to terminate the literal, injecting arbitrary Javascript code into the Go template. As ES6 template literals are rather complex, and themselves can do string interpolation, the decision was made to simply disallow Go template actions from being used inside of them (e.g. "var a = {{.}}"), since there is no obviously safe way to allow this behavior. This takes the same approach as github.com/google/safehtml. With fix, Template.Parse returns an Error when it encounters templates like this, with an ErrorCode of value 12. This ErrorCode is currently unexported, but will be exported in the release of Go 1.21. Users who rely on the previous behavior can re-enable it using the GODEBUG flag jstmpllitinterp=1, with the caveat that backticks will now be escaped. This should be used with caution.



- [https://github.com/skulkarni-mv/goIssue_dunfell](https://github.com/skulkarni-mv/goIssue_dunfell) :  ![starts](https://img.shields.io/github/stars/skulkarni-mv/goIssue_dunfell.svg) ![forks](https://img.shields.io/github/forks/skulkarni-mv/goIssue_dunfell.svg)

- [https://github.com/skulkarni-mv/goIssue_kirkstone](https://github.com/skulkarni-mv/goIssue_kirkstone) :  ![starts](https://img.shields.io/github/stars/skulkarni-mv/goIssue_kirkstone.svg) ![forks](https://img.shields.io/github/forks/skulkarni-mv/goIssue_kirkstone.svg)

## CVE-2023-24517
 Unrestricted Upload of File with Dangerous Type vulnerability in the Pandora FMS File Manager component, allows an attacker to make make use of this issue ( unrestricted file upload ) to execute arbitrary system commands. This issue affects Pandora FMS v767 version and prior versions on all platforms.



- [https://github.com/Argonx21/CVE-2023-24517](https://github.com/Argonx21/CVE-2023-24517) :  ![starts](https://img.shields.io/github/stars/Argonx21/CVE-2023-24517.svg) ![forks](https://img.shields.io/github/forks/Argonx21/CVE-2023-24517.svg)

## CVE-2023-24489
 
A vulnerability has been discovered in the customer-managed ShareFile storage zones controller which, if exploited, could allow an unauthenticated attacker to remotely compromise the customer-managed ShareFile storage zones controller.



- [https://github.com/adhikara13/CVE-2023-24489-ShareFile](https://github.com/adhikara13/CVE-2023-24489-ShareFile) :  ![starts](https://img.shields.io/github/stars/adhikara13/CVE-2023-24489-ShareFile.svg) ![forks](https://img.shields.io/github/forks/adhikara13/CVE-2023-24489-ShareFile.svg)

- [https://github.com/whalebone7/CVE-2023-24489-poc](https://github.com/whalebone7/CVE-2023-24489-poc) :  ![starts](https://img.shields.io/github/stars/whalebone7/CVE-2023-24489-poc.svg) ![forks](https://img.shields.io/github/forks/whalebone7/CVE-2023-24489-poc.svg)

## CVE-2023-24488
 Cross site scripting vulnerability in Citrix ADC and Citrix Gateway  in allows and attacker to perform cross site scripting



- [https://github.com/securitycipher/CVE-2023-24488](https://github.com/securitycipher/CVE-2023-24488) :  ![starts](https://img.shields.io/github/stars/securitycipher/CVE-2023-24488.svg) ![forks](https://img.shields.io/github/forks/securitycipher/CVE-2023-24488.svg)

- [https://github.com/SirBugs/CVE-2023-24488-PoC](https://github.com/SirBugs/CVE-2023-24488-PoC) :  ![starts](https://img.shields.io/github/stars/SirBugs/CVE-2023-24488-PoC.svg) ![forks](https://img.shields.io/github/forks/SirBugs/CVE-2023-24488-PoC.svg)

- [https://github.com/NSTCyber/CVE-2023-24488-SIEM-Sigma-Rule](https://github.com/NSTCyber/CVE-2023-24488-SIEM-Sigma-Rule) :  ![starts](https://img.shields.io/github/stars/NSTCyber/CVE-2023-24488-SIEM-Sigma-Rule.svg) ![forks](https://img.shields.io/github/forks/NSTCyber/CVE-2023-24488-SIEM-Sigma-Rule.svg)

- [https://github.com/raytheon0x21/CVE-2023-24488](https://github.com/raytheon0x21/CVE-2023-24488) :  ![starts](https://img.shields.io/github/stars/raytheon0x21/CVE-2023-24488.svg) ![forks](https://img.shields.io/github/forks/raytheon0x21/CVE-2023-24488.svg)

## CVE-2023-24329
 An issue in the urllib.parse component of Python before 3.11.4 allows attackers to bypass blocklisting methods by supplying a URL that starts with blank characters.



- [https://github.com/PenTestMano/CVE-2023-24329-Exploit](https://github.com/PenTestMano/CVE-2023-24329-Exploit) :  ![starts](https://img.shields.io/github/stars/PenTestMano/CVE-2023-24329-Exploit.svg) ![forks](https://img.shields.io/github/forks/PenTestMano/CVE-2023-24329-Exploit.svg)

- [https://github.com/Pandante-Central/CVE-2023-24329-codeql-test](https://github.com/Pandante-Central/CVE-2023-24329-codeql-test) :  ![starts](https://img.shields.io/github/stars/Pandante-Central/CVE-2023-24329-codeql-test.svg) ![forks](https://img.shields.io/github/forks/Pandante-Central/CVE-2023-24329-codeql-test.svg)

- [https://github.com/H4R335HR/CVE-2023-24329-PoC](https://github.com/H4R335HR/CVE-2023-24329-PoC) :  ![starts](https://img.shields.io/github/stars/H4R335HR/CVE-2023-24329-PoC.svg) ![forks](https://img.shields.io/github/forks/H4R335HR/CVE-2023-24329-PoC.svg)

## CVE-2023-24317
 Judging Management System 1.0 was discovered to contain an arbitrary file upload vulnerability via the component edit_organizer.php.



- [https://github.com/angelopioamirante/CVE-2023-24317](https://github.com/angelopioamirante/CVE-2023-24317) :  ![starts](https://img.shields.io/github/stars/angelopioamirante/CVE-2023-24317.svg) ![forks](https://img.shields.io/github/forks/angelopioamirante/CVE-2023-24317.svg)

## CVE-2023-24278
 Squidex before 7.4.0 was discovered to contain a squid.svg cross-site scripting (XSS) vulnerability.



- [https://github.com/NeCr00/CVE-2023-24278](https://github.com/NeCr00/CVE-2023-24278) :  ![starts](https://img.shields.io/github/stars/NeCr00/CVE-2023-24278.svg) ![forks](https://img.shields.io/github/forks/NeCr00/CVE-2023-24278.svg)

## CVE-2023-24249
 An arbitrary file upload vulnerability in laravel-admin v1.8.19 allows attackers to execute arbitrary code via a crafted PHP file.



- [https://github.com/IDUZZEL/CVE-2023-24249-Exploit](https://github.com/IDUZZEL/CVE-2023-24249-Exploit) :  ![starts](https://img.shields.io/github/stars/IDUZZEL/CVE-2023-24249-Exploit.svg) ![forks](https://img.shields.io/github/forks/IDUZZEL/CVE-2023-24249-Exploit.svg)

## CVE-2023-24204
 SQL injection vulnerability in SourceCodester Simple Customer Relationship Management System v1.0 allows attacker to execute arbitrary code via the name parameter in get-quote.php.



- [https://github.com/momo1239/CVE-2023-24203-and-CVE-2023-24204](https://github.com/momo1239/CVE-2023-24203-and-CVE-2023-24204) :  ![starts](https://img.shields.io/github/stars/momo1239/CVE-2023-24203-and-CVE-2023-24204.svg) ![forks](https://img.shields.io/github/forks/momo1239/CVE-2023-24203-and-CVE-2023-24204.svg)

## CVE-2023-24203
 Cross Site Scripting vulnerability in SourceCodester Simple Customer Relationship Management System v1.0 allows attacker to execute arbitary code via the company or query parameter(s).



- [https://github.com/momo1239/CVE-2023-24203-and-CVE-2023-24204](https://github.com/momo1239/CVE-2023-24203-and-CVE-2023-24204) :  ![starts](https://img.shields.io/github/stars/momo1239/CVE-2023-24203-and-CVE-2023-24204.svg) ![forks](https://img.shields.io/github/forks/momo1239/CVE-2023-24203-and-CVE-2023-24204.svg)

## CVE-2023-24100
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/badboycxcc/CVE-2023-24100](https://github.com/badboycxcc/CVE-2023-24100) :  ![starts](https://img.shields.io/github/stars/badboycxcc/CVE-2023-24100.svg) ![forks](https://img.shields.io/github/forks/badboycxcc/CVE-2023-24100.svg)

## CVE-2023-24078
 Real Time Logic FuguHub v8.1 and earlier was discovered to contain a remote code execution (RCE) vulnerability via the component /FuguHub/cmsdocs/.



- [https://github.com/overgrowncarrot1/CVE-2023-24078](https://github.com/overgrowncarrot1/CVE-2023-24078) :  ![starts](https://img.shields.io/github/stars/overgrowncarrot1/CVE-2023-24078.svg) ![forks](https://img.shields.io/github/forks/overgrowncarrot1/CVE-2023-24078.svg)

- [https://github.com/rio128128/CVE-2023-24078](https://github.com/rio128128/CVE-2023-24078) :  ![starts](https://img.shields.io/github/stars/rio128128/CVE-2023-24078.svg) ![forks](https://img.shields.io/github/forks/rio128128/CVE-2023-24078.svg)

- [https://github.com/d2cy/CVEs](https://github.com/d2cy/CVEs) :  ![starts](https://img.shields.io/github/stars/d2cy/CVEs.svg) ![forks](https://img.shields.io/github/forks/d2cy/CVEs.svg)

- [https://github.com/ag-rodriguez/CVE-2023-24078](https://github.com/ag-rodriguez/CVE-2023-24078) :  ![starts](https://img.shields.io/github/stars/ag-rodriguez/CVE-2023-24078.svg) ![forks](https://img.shields.io/github/forks/ag-rodriguez/CVE-2023-24078.svg)

## CVE-2023-24059
 Grand Theft Auto V for PC allows attackers to achieve partial remote code execution or modify files on a PC, as exploited in the wild in January 2023.



- [https://github.com/gmh5225/CVE-2023-24059](https://github.com/gmh5225/CVE-2023-24059) :  ![starts](https://img.shields.io/github/stars/gmh5225/CVE-2023-24059.svg) ![forks](https://img.shields.io/github/forks/gmh5225/CVE-2023-24059.svg)

## CVE-2023-24055
 KeePass through 2.53 (in a default installation) allows an attacker, who has write access to the XML configuration file, to obtain the cleartext passwords by adding an export trigger. NOTE: the vendor's position is that the password database is not intended to be secure against an attacker who has that level of access to the local PC.



- [https://github.com/alt3kx/CVE-2023-24055_PoC](https://github.com/alt3kx/CVE-2023-24055_PoC) :  ![starts](https://img.shields.io/github/stars/alt3kx/CVE-2023-24055_PoC.svg) ![forks](https://img.shields.io/github/forks/alt3kx/CVE-2023-24055_PoC.svg)

- [https://github.com/deetl/CVE-2023-24055](https://github.com/deetl/CVE-2023-24055) :  ![starts](https://img.shields.io/github/stars/deetl/CVE-2023-24055.svg) ![forks](https://img.shields.io/github/forks/deetl/CVE-2023-24055.svg)

- [https://github.com/n3rada/Invoke-KeePassBackup](https://github.com/n3rada/Invoke-KeePassBackup) :  ![starts](https://img.shields.io/github/stars/n3rada/Invoke-KeePassBackup.svg) ![forks](https://img.shields.io/github/forks/n3rada/Invoke-KeePassBackup.svg)

- [https://github.com/zwlsix/KeePass-CVE-2023-24055](https://github.com/zwlsix/KeePass-CVE-2023-24055) :  ![starts](https://img.shields.io/github/stars/zwlsix/KeePass-CVE-2023-24055.svg) ![forks](https://img.shields.io/github/forks/zwlsix/KeePass-CVE-2023-24055.svg)

- [https://github.com/julesbozouklian/PoC_CVE-2023-24055](https://github.com/julesbozouklian/PoC_CVE-2023-24055) :  ![starts](https://img.shields.io/github/stars/julesbozouklian/PoC_CVE-2023-24055.svg) ![forks](https://img.shields.io/github/forks/julesbozouklian/PoC_CVE-2023-24055.svg)

- [https://github.com/Cyb3rtus/keepass_CVE-2023-24055_yara_rule](https://github.com/Cyb3rtus/keepass_CVE-2023-24055_yara_rule) :  ![starts](https://img.shields.io/github/stars/Cyb3rtus/keepass_CVE-2023-24055_yara_rule.svg) ![forks](https://img.shields.io/github/forks/Cyb3rtus/keepass_CVE-2023-24055_yara_rule.svg)

- [https://github.com/yosef0x01/CVE-2023-24055](https://github.com/yosef0x01/CVE-2023-24055) :  ![starts](https://img.shields.io/github/stars/yosef0x01/CVE-2023-24055.svg) ![forks](https://img.shields.io/github/forks/yosef0x01/CVE-2023-24055.svg)

- [https://github.com/digital-dev/KeePass-TriggerLess](https://github.com/digital-dev/KeePass-TriggerLess) :  ![starts](https://img.shields.io/github/stars/digital-dev/KeePass-TriggerLess.svg) ![forks](https://img.shields.io/github/forks/digital-dev/KeePass-TriggerLess.svg)

## CVE-2023-24044
 A Host Header Injection issue on the Login page of Plesk Obsidian through 18.0.49 allows attackers to redirect users to malicious websites via a Host request header. NOTE: the vendor's position is "the ability to use arbitrary domain names to access the panel is an intended feature."



- [https://github.com/Cappricio-Securities/CVE-2023-24044](https://github.com/Cappricio-Securities/CVE-2023-24044) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2023-24044.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2023-24044.svg)

## CVE-2023-24034
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/hotblac/cve-2023-34034](https://github.com/hotblac/cve-2023-34034) :  ![starts](https://img.shields.io/github/stars/hotblac/cve-2023-34034.svg) ![forks](https://img.shields.io/github/forks/hotblac/cve-2023-34034.svg)

## CVE-2023-24023
 Bluetooth BR/EDR devices with Secure Simple Pairing and Secure Connections pairing in Bluetooth Core Specification 4.2 through 5.4 allow certain man-in-the-middle attacks that force a short key length, and might lead to discovery of the encryption key and live injection, aka BLUFFS.



- [https://github.com/francozappa/bluffs](https://github.com/francozappa/bluffs) :  ![starts](https://img.shields.io/github/stars/francozappa/bluffs.svg) ![forks](https://img.shields.io/github/forks/francozappa/bluffs.svg)

## CVE-2023-23946
 Git, a revision control system, is vulnerable to path traversal prior to versions 2.39.2, 2.38.4, 2.37.6, 2.36.5, 2.35.7, 2.34.7, 2.33.7, 2.32.6, 2.31.7, and 2.30.8. By feeding a crafted input to `git apply`, a path outside the working tree can be overwritten as the user who is running `git apply`. A fix has been prepared and will appear in v2.39.2, v2.38.4, v2.37.6, v2.36.5, v2.35.7, v2.34.7, v2.33.7, v2.32.6, v2.31.7, and v2.30.8. As a workaround, use `git apply --stat` to inspect a patch before applying; avoid applying one that creates a symbolic link and then creates a file beyond the symbolic link.



- [https://github.com/bruno-1337/CVE-2023-23946-POC](https://github.com/bruno-1337/CVE-2023-23946-POC) :  ![starts](https://img.shields.io/github/stars/bruno-1337/CVE-2023-23946-POC.svg) ![forks](https://img.shields.io/github/forks/bruno-1337/CVE-2023-23946-POC.svg)

## CVE-2023-23924
 Dompdf is an HTML to PDF converter. The URI validation on dompdf 2.0.1 can be bypassed on SVG parsing by passing `image` tags with uppercase letters. This may lead to arbitrary object unserialize on PHP  8, through the `phar` URL wrapper. An attacker can exploit the vulnerability to call arbitrary URL with arbitrary protocols, if they can provide a SVG file to dompdf. In PHP versions before 8.0.0, it leads to arbitrary unserialize, that will lead to the very least to an arbitrary file deletion and even remote code execution, depending on classes that are available.




- [https://github.com/motikan2010/CVE-2023-23924](https://github.com/motikan2010/CVE-2023-23924) :  ![starts](https://img.shields.io/github/stars/motikan2010/CVE-2023-23924.svg) ![forks](https://img.shields.io/github/forks/motikan2010/CVE-2023-23924.svg)

## CVE-2023-23752
 An issue was discovered in Joomla! 4.0.0 through 4.2.7. An improper access check allows unauthorized access to webservice endpoints.



- [https://github.com/Acceis/exploit-CVE-2023-23752](https://github.com/Acceis/exploit-CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/Acceis/exploit-CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/Acceis/exploit-CVE-2023-23752.svg)

- [https://github.com/ThatNotEasy/CVE-2023-23752](https://github.com/ThatNotEasy/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2023-23752.svg)

- [https://github.com/z3n70/CVE-2023-23752](https://github.com/z3n70/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/z3n70/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/z3n70/CVE-2023-23752.svg)

- [https://github.com/keyuan15/CVE-2023-23752](https://github.com/keyuan15/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/keyuan15/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/keyuan15/CVE-2023-23752.svg)

- [https://github.com/K3ysTr0K3R/CVE-2023-23752-EXPLOIT](https://github.com/K3ysTr0K3R/CVE-2023-23752-EXPLOIT) :  ![starts](https://img.shields.io/github/stars/K3ysTr0K3R/CVE-2023-23752-EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/K3ysTr0K3R/CVE-2023-23752-EXPLOIT.svg)

- [https://github.com/gibran-abdillah/CVE-2023-23752](https://github.com/gibran-abdillah/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/gibran-abdillah/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/gibran-abdillah/CVE-2023-23752.svg)

- [https://github.com/0xNahim/CVE-2023-23752](https://github.com/0xNahim/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/0xNahim/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/0xNahim/CVE-2023-23752.svg)

- [https://github.com/Sweelg/CVE-2023-23752](https://github.com/Sweelg/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/Sweelg/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/Sweelg/CVE-2023-23752.svg)

- [https://github.com/Youns92/Joomla-v4.2.8---CVE-2023-23752](https://github.com/Youns92/Joomla-v4.2.8---CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/Youns92/Joomla-v4.2.8---CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/Youns92/Joomla-v4.2.8---CVE-2023-23752.svg)

- [https://github.com/adhikara13/CVE-2023-23752](https://github.com/adhikara13/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/adhikara13/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/adhikara13/CVE-2023-23752.svg)

- [https://github.com/karthikuj/CVE-2023-23752-Docker](https://github.com/karthikuj/CVE-2023-23752-Docker) :  ![starts](https://img.shields.io/github/stars/karthikuj/CVE-2023-23752-Docker.svg) ![forks](https://img.shields.io/github/forks/karthikuj/CVE-2023-23752-Docker.svg)

- [https://github.com/Fernando-olv/Joomla-CVE-2023-23752](https://github.com/Fernando-olv/Joomla-CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/Fernando-olv/Joomla-CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/Fernando-olv/Joomla-CVE-2023-23752.svg)

- [https://github.com/revkami/CVE-2023-23752-Joomla-v4.2.8](https://github.com/revkami/CVE-2023-23752-Joomla-v4.2.8) :  ![starts](https://img.shields.io/github/stars/revkami/CVE-2023-23752-Joomla-v4.2.8.svg) ![forks](https://img.shields.io/github/forks/revkami/CVE-2023-23752-Joomla-v4.2.8.svg)

- [https://github.com/ifacker/CVE-2023-23752-Joomla](https://github.com/ifacker/CVE-2023-23752-Joomla) :  ![starts](https://img.shields.io/github/stars/ifacker/CVE-2023-23752-Joomla.svg) ![forks](https://img.shields.io/github/forks/ifacker/CVE-2023-23752-Joomla.svg)

- [https://github.com/JohnDoeAnonITA/CVE-2023-23752](https://github.com/JohnDoeAnonITA/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/JohnDoeAnonITA/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/JohnDoeAnonITA/CVE-2023-23752.svg)

- [https://github.com/Vulnmachines/joomla_CVE-2023-23752](https://github.com/Vulnmachines/joomla_CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/Vulnmachines/joomla_CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/Vulnmachines/joomla_CVE-2023-23752.svg)

- [https://github.com/Saboor-Hakimi/CVE-2023-23752](https://github.com/Saboor-Hakimi/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/Saboor-Hakimi/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/Saboor-Hakimi/CVE-2023-23752.svg)

- [https://github.com/blacks1ph0n/CVE-2023-23752](https://github.com/blacks1ph0n/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/blacks1ph0n/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/blacks1ph0n/CVE-2023-23752.svg)

- [https://github.com/0xWhoami35/CVE-2023-23752](https://github.com/0xWhoami35/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/0xWhoami35/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/0xWhoami35/CVE-2023-23752.svg)

- [https://github.com/yusinomy/CVE-2023-23752](https://github.com/yusinomy/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/yusinomy/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/yusinomy/CVE-2023-23752.svg)

- [https://github.com/GhostToKnow/CVE-2023-23752](https://github.com/GhostToKnow/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/GhostToKnow/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/GhostToKnow/CVE-2023-23752.svg)

- [https://github.com/ibaiw/joomla_CVE-2023-23752](https://github.com/ibaiw/joomla_CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/ibaiw/joomla_CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/ibaiw/joomla_CVE-2023-23752.svg)

- [https://github.com/wangking1/CVE-2023-23752-poc](https://github.com/wangking1/CVE-2023-23752-poc) :  ![starts](https://img.shields.io/github/stars/wangking1/CVE-2023-23752-poc.svg) ![forks](https://img.shields.io/github/forks/wangking1/CVE-2023-23752-poc.svg)

- [https://github.com/TindalyTn/CVE-2023-23752](https://github.com/TindalyTn/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/TindalyTn/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/TindalyTn/CVE-2023-23752.svg)

- [https://github.com/h3x0v3rl0rd/CVE-2023-23752](https://github.com/h3x0v3rl0rd/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/h3x0v3rl0rd/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/h3x0v3rl0rd/CVE-2023-23752.svg)

- [https://github.com/AlissonFaoli/CVE-2023-23752](https://github.com/AlissonFaoli/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/AlissonFaoli/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/AlissonFaoli/CVE-2023-23752.svg)

- [https://github.com/r3dston3/CVE-2023-23752](https://github.com/r3dston3/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/r3dston3/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/r3dston3/CVE-2023-23752.svg)

- [https://github.com/Pushkarup/CVE-2023-23752](https://github.com/Pushkarup/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/Pushkarup/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/Pushkarup/CVE-2023-23752.svg)

- [https://github.com/Jenderal92/Joomla-CVE-2023-23752](https://github.com/Jenderal92/Joomla-CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/Jenderal92/Joomla-CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/Jenderal92/Joomla-CVE-2023-23752.svg)

- [https://github.com/adriyansyah-mf/CVE-2023-23752](https://github.com/adriyansyah-mf/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/adriyansyah-mf/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/adriyansyah-mf/CVE-2023-23752.svg)

- [https://github.com/raystr-atearedteam/CVE2023-23752](https://github.com/raystr-atearedteam/CVE2023-23752) :  ![starts](https://img.shields.io/github/stars/raystr-atearedteam/CVE2023-23752.svg) ![forks](https://img.shields.io/github/forks/raystr-atearedteam/CVE2023-23752.svg)

- [https://github.com/AkbarWiraN/Joomla-Scanner](https://github.com/AkbarWiraN/Joomla-Scanner) :  ![starts](https://img.shields.io/github/stars/AkbarWiraN/Joomla-Scanner.svg) ![forks](https://img.shields.io/github/forks/AkbarWiraN/Joomla-Scanner.svg)

- [https://github.com/gunzf0x/CVE-2023-23752](https://github.com/gunzf0x/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/gunzf0x/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/gunzf0x/CVE-2023-23752.svg)

- [https://github.com/lainonz/CVE-2023-23752](https://github.com/lainonz/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/lainonz/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/lainonz/CVE-2023-23752.svg)

- [https://github.com/Ly0kha/Joomla-CVE-2023-23752-Exploit-Script](https://github.com/Ly0kha/Joomla-CVE-2023-23752-Exploit-Script) :  ![starts](https://img.shields.io/github/stars/Ly0kha/Joomla-CVE-2023-23752-Exploit-Script.svg) ![forks](https://img.shields.io/github/forks/Ly0kha/Joomla-CVE-2023-23752-Exploit-Script.svg)

- [https://github.com/Aureum01/CVE-2023-23752](https://github.com/Aureum01/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/Aureum01/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/Aureum01/CVE-2023-23752.svg)

- [https://github.com/JeneralMotors/CVE-2023-23752](https://github.com/JeneralMotors/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/JeneralMotors/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/JeneralMotors/CVE-2023-23752.svg)

- [https://github.com/svaltheim/CVE-2023-23752](https://github.com/svaltheim/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/svaltheim/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/svaltheim/CVE-2023-23752.svg)

- [https://github.com/Rival420/CVE-2023-23752](https://github.com/Rival420/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/Rival420/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/Rival420/CVE-2023-23752.svg)

- [https://github.com/C1ph3rX13/CVE-2023-23752](https://github.com/C1ph3rX13/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/C1ph3rX13/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/C1ph3rX13/CVE-2023-23752.svg)

- [https://github.com/sw0rd1ight/CVE-2023-23752](https://github.com/sw0rd1ight/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/sw0rd1ight/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/sw0rd1ight/CVE-2023-23752.svg)

- [https://github.com/0xx01/CVE-2023-23752](https://github.com/0xx01/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/0xx01/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/0xx01/CVE-2023-23752.svg)

- [https://github.com/yTxZx/CVE-2023-23752](https://github.com/yTxZx/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/yTxZx/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/yTxZx/CVE-2023-23752.svg)

- [https://github.com/shellvik/CVE-2023-23752](https://github.com/shellvik/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/shellvik/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/shellvik/CVE-2023-23752.svg)

- [https://github.com/MrP4nda1337/CVE-2023-23752](https://github.com/MrP4nda1337/CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/MrP4nda1337/CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/MrP4nda1337/CVE-2023-23752.svg)

- [https://github.com/hadrian3689/CVE-2023-23752_Joomla](https://github.com/hadrian3689/CVE-2023-23752_Joomla) :  ![starts](https://img.shields.io/github/stars/hadrian3689/CVE-2023-23752_Joomla.svg) ![forks](https://img.shields.io/github/forks/hadrian3689/CVE-2023-23752_Joomla.svg)

- [https://github.com/mariovata/CVE-2023-23752-Python](https://github.com/mariovata/CVE-2023-23752-Python) :  ![starts](https://img.shields.io/github/stars/mariovata/CVE-2023-23752-Python.svg) ![forks](https://img.shields.io/github/forks/mariovata/CVE-2023-23752-Python.svg)

- [https://github.com/Ge-Per/Scanner-CVE-2023-23752](https://github.com/Ge-Per/Scanner-CVE-2023-23752) :  ![starts](https://img.shields.io/github/stars/Ge-Per/Scanner-CVE-2023-23752.svg) ![forks](https://img.shields.io/github/forks/Ge-Per/Scanner-CVE-2023-23752.svg)

- [https://github.com/m4nInTh3mIdDle/joomla-CVE-2023](https://github.com/m4nInTh3mIdDle/joomla-CVE-2023) :  ![starts](https://img.shields.io/github/stars/m4nInTh3mIdDle/joomla-CVE-2023.svg) ![forks](https://img.shields.io/github/forks/m4nInTh3mIdDle/joomla-CVE-2023.svg)

- [https://github.com/0x0jr/HTB-Devvortex-CVE-2023-2375-PoC](https://github.com/0x0jr/HTB-Devvortex-CVE-2023-2375-PoC) :  ![starts](https://img.shields.io/github/stars/0x0jr/HTB-Devvortex-CVE-2023-2375-PoC.svg) ![forks](https://img.shields.io/github/forks/0x0jr/HTB-Devvortex-CVE-2023-2375-PoC.svg)

## CVE-2023-23638
 A deserialization vulnerability existed when dubbo generic invoke, which could lead to malicious code execution. 

This issue affects Apache Dubbo 2.7.x version 2.7.21 and prior versions; Apache Dubbo 3.0.x version 3.0.13 and prior versions; Apache Dubbo 3.1.x version 3.1.5 and prior versions. 



- [https://github.com/YYHYlh/Apache-Dubbo-CVE-2023-23638-exp](https://github.com/YYHYlh/Apache-Dubbo-CVE-2023-23638-exp) :  ![starts](https://img.shields.io/github/stars/YYHYlh/Apache-Dubbo-CVE-2023-23638-exp.svg) ![forks](https://img.shields.io/github/forks/YYHYlh/Apache-Dubbo-CVE-2023-23638-exp.svg)

- [https://github.com/X1r0z/Dubbo-RCE](https://github.com/X1r0z/Dubbo-RCE) :  ![starts](https://img.shields.io/github/stars/X1r0z/Dubbo-RCE.svg) ![forks](https://img.shields.io/github/forks/X1r0z/Dubbo-RCE.svg)

- [https://github.com/cuijiung/dubbo-CVE-2023-23638](https://github.com/cuijiung/dubbo-CVE-2023-23638) :  ![starts](https://img.shields.io/github/stars/cuijiung/dubbo-CVE-2023-23638.svg) ![forks](https://img.shields.io/github/forks/cuijiung/dubbo-CVE-2023-23638.svg)

- [https://github.com/P4x1s/CVE-2023-23638-Tools](https://github.com/P4x1s/CVE-2023-23638-Tools) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2023-23638-Tools.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2023-23638-Tools.svg)

## CVE-2023-23583
 Sequence of processor instructions leads to unexpected behavior for some Intel(R) Processors may allow an authenticated user to potentially enable escalation of privilege and/or information disclosure and/or denial of service via local access.



- [https://github.com/Mav3r1ck0x1/CVE-2023-23583-Reptar-](https://github.com/Mav3r1ck0x1/CVE-2023-23583-Reptar-) :  ![starts](https://img.shields.io/github/stars/Mav3r1ck0x1/CVE-2023-23583-Reptar-.svg) ![forks](https://img.shields.io/github/forks/Mav3r1ck0x1/CVE-2023-23583-Reptar-.svg)

## CVE-2023-23531
 The issue was addressed with improved memory handling. This issue is fixed in macOS Ventura 13.2, iOS 16.3 and iPadOS 16.3. An app may be able to execute arbitrary code out of its sandbox or with certain elevated privileges.



- [https://github.com/DarthOCE/MonkeyJB](https://github.com/DarthOCE/MonkeyJB) :  ![starts](https://img.shields.io/github/stars/DarthOCE/MonkeyJB.svg) ![forks](https://img.shields.io/github/forks/DarthOCE/MonkeyJB.svg)

## CVE-2023-23504
 The issue was addressed with improved memory handling. This issue is fixed in macOS Monterey 12.6.3, macOS Ventura 13.2, watchOS 9.3, iOS 15.7.3 and iPadOS 15.7.3, tvOS 16.3, iOS 16.3 and iPadOS 16.3. An app may be able to execute arbitrary code with kernel privileges.



- [https://github.com/zeroc00I/CVE-2023-23504](https://github.com/zeroc00I/CVE-2023-23504) :  ![starts](https://img.shields.io/github/stars/zeroc00I/CVE-2023-23504.svg) ![forks](https://img.shields.io/github/forks/zeroc00I/CVE-2023-23504.svg)

## CVE-2023-23488
 The Paid Memberships Pro WordPress Plugin, version  2.9.8, is affected by an unauthenticated SQL injection vulnerability in the 'code' parameter of the '/pmpro/v1/order' REST route.



- [https://github.com/cybfar/CVE-2023-23488-pmpro-2.8](https://github.com/cybfar/CVE-2023-23488-pmpro-2.8) :  ![starts](https://img.shields.io/github/stars/cybfar/CVE-2023-23488-pmpro-2.8.svg) ![forks](https://img.shields.io/github/forks/cybfar/CVE-2023-23488-pmpro-2.8.svg)

- [https://github.com/long-rookie/CVE-2023-23488-PoC](https://github.com/long-rookie/CVE-2023-23488-PoC) :  ![starts](https://img.shields.io/github/stars/long-rookie/CVE-2023-23488-PoC.svg) ![forks](https://img.shields.io/github/forks/long-rookie/CVE-2023-23488-PoC.svg)

## CVE-2023-23397
 Microsoft Outlook Elevation of Privilege Vulnerability



- [https://github.com/api0cradle/CVE-2023-23397-POC-Powershell](https://github.com/api0cradle/CVE-2023-23397-POC-Powershell) :  ![starts](https://img.shields.io/github/stars/api0cradle/CVE-2023-23397-POC-Powershell.svg) ![forks](https://img.shields.io/github/forks/api0cradle/CVE-2023-23397-POC-Powershell.svg)

- [https://github.com/sqrtZeroKnowledge/CVE-2023-23397_EXPLOIT_0DAY](https://github.com/sqrtZeroKnowledge/CVE-2023-23397_EXPLOIT_0DAY) :  ![starts](https://img.shields.io/github/stars/sqrtZeroKnowledge/CVE-2023-23397_EXPLOIT_0DAY.svg) ![forks](https://img.shields.io/github/forks/sqrtZeroKnowledge/CVE-2023-23397_EXPLOIT_0DAY.svg)

- [https://github.com/Trackflaw/CVE-2023-23397](https://github.com/Trackflaw/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/Trackflaw/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/Trackflaw/CVE-2023-23397.svg)

- [https://github.com/ka7ana/CVE-2023-23397](https://github.com/ka7ana/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/ka7ana/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/ka7ana/CVE-2023-23397.svg)

- [https://github.com/tiepologian/CVE-2023-23397](https://github.com/tiepologian/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/tiepologian/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/tiepologian/CVE-2023-23397.svg)

- [https://github.com/Muhammad-Ali007/OutlookNTLM_CVE-2023-23397](https://github.com/Muhammad-Ali007/OutlookNTLM_CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/Muhammad-Ali007/OutlookNTLM_CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/Muhammad-Ali007/OutlookNTLM_CVE-2023-23397.svg)

- [https://github.com/BronzeBee/cve-2023-23397](https://github.com/BronzeBee/cve-2023-23397) :  ![starts](https://img.shields.io/github/stars/BronzeBee/cve-2023-23397.svg) ![forks](https://img.shields.io/github/forks/BronzeBee/cve-2023-23397.svg)

- [https://github.com/djackreuter/CVE-2023-23397-PoC](https://github.com/djackreuter/CVE-2023-23397-PoC) :  ![starts](https://img.shields.io/github/stars/djackreuter/CVE-2023-23397-PoC.svg) ![forks](https://img.shields.io/github/forks/djackreuter/CVE-2023-23397-PoC.svg)

- [https://github.com/BillSkiCO/CVE-2023-23397_EXPLOIT](https://github.com/BillSkiCO/CVE-2023-23397_EXPLOIT) :  ![starts](https://img.shields.io/github/stars/BillSkiCO/CVE-2023-23397_EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/BillSkiCO/CVE-2023-23397_EXPLOIT.svg)

- [https://github.com/ahmedkhlief/CVE-2023-23397-POC](https://github.com/ahmedkhlief/CVE-2023-23397-POC) :  ![starts](https://img.shields.io/github/stars/ahmedkhlief/CVE-2023-23397-POC.svg) ![forks](https://img.shields.io/github/forks/ahmedkhlief/CVE-2023-23397-POC.svg)

- [https://github.com/vlad-a-man/CVE-2023-23397](https://github.com/vlad-a-man/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/vlad-a-man/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/vlad-a-man/CVE-2023-23397.svg)

- [https://github.com/grn-bogo/CVE-2023-23397](https://github.com/grn-bogo/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/grn-bogo/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/grn-bogo/CVE-2023-23397.svg)

- [https://github.com/Pushkarup/CVE-2023-23397](https://github.com/Pushkarup/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/Pushkarup/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/Pushkarup/CVE-2023-23397.svg)

- [https://github.com/alicangnll/CVE-2023-23397](https://github.com/alicangnll/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/alicangnll/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/alicangnll/CVE-2023-23397.svg)

- [https://github.com/P4x1s/CVE-2023-23397-POC](https://github.com/P4x1s/CVE-2023-23397-POC) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2023-23397-POC.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2023-23397-POC.svg)

- [https://github.com/ahmedkhlief/CVE-2023-23397-POC-Using-Interop-Outlook](https://github.com/ahmedkhlief/CVE-2023-23397-POC-Using-Interop-Outlook) :  ![starts](https://img.shields.io/github/stars/ahmedkhlief/CVE-2023-23397-POC-Using-Interop-Outlook.svg) ![forks](https://img.shields.io/github/forks/ahmedkhlief/CVE-2023-23397-POC-Using-Interop-Outlook.svg)

- [https://github.com/cleverg0d/CVE-2023-23397-PoC-PowerShell](https://github.com/cleverg0d/CVE-2023-23397-PoC-PowerShell) :  ![starts](https://img.shields.io/github/stars/cleverg0d/CVE-2023-23397-PoC-PowerShell.svg) ![forks](https://img.shields.io/github/forks/cleverg0d/CVE-2023-23397-PoC-PowerShell.svg)

- [https://github.com/moneertv/CVE-2023-23397](https://github.com/moneertv/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/moneertv/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/moneertv/CVE-2023-23397.svg)

- [https://github.com/SecCTechs/CVE-2023-23397](https://github.com/SecCTechs/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/SecCTechs/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/SecCTechs/CVE-2023-23397.svg)

- [https://github.com/j0eyv/CVE-2023-23397](https://github.com/j0eyv/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/j0eyv/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/j0eyv/CVE-2023-23397.svg)

- [https://github.com/TheUnknownSoul/CVE-2023-23397-PoW](https://github.com/TheUnknownSoul/CVE-2023-23397-PoW) :  ![starts](https://img.shields.io/github/stars/TheUnknownSoul/CVE-2023-23397-PoW.svg) ![forks](https://img.shields.io/github/forks/TheUnknownSoul/CVE-2023-23397-PoW.svg)

- [https://github.com/securiteinfo/expl_outlook_cve_2023_23397_securiteinfo.yar](https://github.com/securiteinfo/expl_outlook_cve_2023_23397_securiteinfo.yar) :  ![starts](https://img.shields.io/github/stars/securiteinfo/expl_outlook_cve_2023_23397_securiteinfo.yar.svg) ![forks](https://img.shields.io/github/forks/securiteinfo/expl_outlook_cve_2023_23397_securiteinfo.yar.svg)

- [https://github.com/Symbolexe/CVE-2023-23397](https://github.com/Symbolexe/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/Symbolexe/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/Symbolexe/CVE-2023-23397.svg)

- [https://github.com/stevesec/CVE-2023-23397](https://github.com/stevesec/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/stevesec/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/stevesec/CVE-2023-23397.svg)

- [https://github.com/ducnorth2712/CVE-2023-23397](https://github.com/ducnorth2712/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/ducnorth2712/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/ducnorth2712/CVE-2023-23397.svg)

- [https://github.com/Gilospy/CVE-2023-23397](https://github.com/Gilospy/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/Gilospy/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/Gilospy/CVE-2023-23397.svg)

- [https://github.com/jacquesquail/CVE-2023-23397](https://github.com/jacquesquail/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/jacquesquail/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/jacquesquail/CVE-2023-23397.svg)

- [https://github.com/im007/CVE-2023-23397](https://github.com/im007/CVE-2023-23397) :  ![starts](https://img.shields.io/github/stars/im007/CVE-2023-23397.svg) ![forks](https://img.shields.io/github/forks/im007/CVE-2023-23397.svg)

- [https://github.com/Cyb3rMaddy/CVE-2023-23397-Report](https://github.com/Cyb3rMaddy/CVE-2023-23397-Report) :  ![starts](https://img.shields.io/github/stars/Cyb3rMaddy/CVE-2023-23397-Report.svg) ![forks](https://img.shields.io/github/forks/Cyb3rMaddy/CVE-2023-23397-Report.svg)

- [https://github.com/sarsaeroth/CVE-2023-23397-POC](https://github.com/sarsaeroth/CVE-2023-23397-POC) :  ![starts](https://img.shields.io/github/stars/sarsaeroth/CVE-2023-23397-POC.svg) ![forks](https://img.shields.io/github/forks/sarsaeroth/CVE-2023-23397-POC.svg)

- [https://github.com/Zeppperoni/CVE-2023-23397-Patch](https://github.com/Zeppperoni/CVE-2023-23397-Patch) :  ![starts](https://img.shields.io/github/stars/Zeppperoni/CVE-2023-23397-Patch.svg) ![forks](https://img.shields.io/github/forks/Zeppperoni/CVE-2023-23397-Patch.svg)

## CVE-2023-23396
 Microsoft Excel Denial of Service Vulnerability



- [https://github.com/LucaBarile/CVE-2023-23396](https://github.com/LucaBarile/CVE-2023-23396) :  ![starts](https://img.shields.io/github/stars/LucaBarile/CVE-2023-23396.svg) ![forks](https://img.shields.io/github/forks/LucaBarile/CVE-2023-23396.svg)

## CVE-2023-23388
 Windows Bluetooth Driver Elevation of Privilege Vulnerability



- [https://github.com/ynwarcs/CVE-2023-23388](https://github.com/ynwarcs/CVE-2023-23388) :  ![starts](https://img.shields.io/github/stars/ynwarcs/CVE-2023-23388.svg) ![forks](https://img.shields.io/github/forks/ynwarcs/CVE-2023-23388.svg)

## CVE-2023-23333
 There is a command injection vulnerability in SolarView Compact through 6.00, attackers can execute commands by bypassing internal restrictions through downloader.php.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/Mr-xn/CVE-2023-23333](https://github.com/Mr-xn/CVE-2023-23333) :  ![starts](https://img.shields.io/github/stars/Mr-xn/CVE-2023-23333.svg) ![forks](https://img.shields.io/github/forks/Mr-xn/CVE-2023-23333.svg)

- [https://github.com/Timorlover/CVE-2023-23333](https://github.com/Timorlover/CVE-2023-23333) :  ![starts](https://img.shields.io/github/stars/Timorlover/CVE-2023-23333.svg) ![forks](https://img.shields.io/github/forks/Timorlover/CVE-2023-23333.svg)

- [https://github.com/emanueldosreis/nmap-CVE-2023-23333-exploit](https://github.com/emanueldosreis/nmap-CVE-2023-23333-exploit) :  ![starts](https://img.shields.io/github/stars/emanueldosreis/nmap-CVE-2023-23333-exploit.svg) ![forks](https://img.shields.io/github/forks/emanueldosreis/nmap-CVE-2023-23333-exploit.svg)

## CVE-2023-23279
 Canteen Management System 1.0 is vulnerable to SQL Injection via /php_action/getOrderReport.php.



- [https://github.com/tuannq2299/CVE-2023-23279](https://github.com/tuannq2299/CVE-2023-23279) :  ![starts](https://img.shields.io/github/stars/tuannq2299/CVE-2023-23279.svg) ![forks](https://img.shields.io/github/forks/tuannq2299/CVE-2023-23279.svg)

## CVE-2023-23192
 IS Decisions UserLock MFA 11.01 is vulnerable to authentication bypass using scheduled task.



- [https://github.com/pinarsadioglu/CVE-2023-23192](https://github.com/pinarsadioglu/CVE-2023-23192) :  ![starts](https://img.shields.io/github/stars/pinarsadioglu/CVE-2023-23192.svg) ![forks](https://img.shields.io/github/forks/pinarsadioglu/CVE-2023-23192.svg)

- [https://github.com/Penkyzduyi/CVE-2023-23192](https://github.com/Penkyzduyi/CVE-2023-23192) :  ![starts](https://img.shields.io/github/stars/Penkyzduyi/CVE-2023-23192.svg) ![forks](https://img.shields.io/github/forks/Penkyzduyi/CVE-2023-23192.svg)

## CVE-2023-23169
 Synapsoft pdfocus 1.17 is vulnerable to local file inclusion and server-side request forgery Directory Traversal.



- [https://github.com/S4nshine/CVE-2023-23169](https://github.com/S4nshine/CVE-2023-23169) :  ![starts](https://img.shields.io/github/stars/S4nshine/CVE-2023-23169.svg) ![forks](https://img.shields.io/github/forks/S4nshine/CVE-2023-23169.svg)

## CVE-2023-23138
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/OmarAtallahh/CVE-2023-23138](https://github.com/OmarAtallahh/CVE-2023-23138) :  ![starts](https://img.shields.io/github/stars/OmarAtallahh/CVE-2023-23138.svg) ![forks](https://img.shields.io/github/forks/OmarAtallahh/CVE-2023-23138.svg)

## CVE-2023-23132
 Selfwealth iOS mobile App 3.3.1 is vulnerable to Sensitive key disclosure. The application reveals hardcoded API keys.



- [https://github.com/l00neyhacker/CVE-2023-23132](https://github.com/l00neyhacker/CVE-2023-23132) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2023-23132.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2023-23132.svg)

## CVE-2023-23131
 Selfwealth iOS mobile App 3.3.1 is vulnerable to Insecure App Transport Security (ATS) Settings.



- [https://github.com/l00neyhacker/CVE-2023-23131](https://github.com/l00neyhacker/CVE-2023-23131) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2023-23131.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2023-23131.svg)

## CVE-2023-23130
 Connectwise Automate 2022.11 is vulnerable to Cleartext authentication. Authentication is being done via HTTP (cleartext) with SSL disabled. OTE: the vendor's position is that, by design, this is controlled by a configuration option in which a customer can choose to use HTTP (rather than HTTPS) during troubleshooting.



- [https://github.com/l00neyhacker/CVE-2023-23130](https://github.com/l00neyhacker/CVE-2023-23130) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2023-23130.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2023-23130.svg)

## CVE-2023-23128
 Connectwise Control 22.8.10013.8329 is vulnerable to Cross Origin Resource Sharing (CORS). The vendor's position is that two endpoints have Access-Control-Allow-Origin wildcarding to support product functionality, and that there is no risk from this behavior. The vulnerability report is thus not valid.



- [https://github.com/l00neyhacker/CVE-2023-23128](https://github.com/l00neyhacker/CVE-2023-23128) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2023-23128.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2023-23128.svg)

## CVE-2023-23127
 In Connectwise Control 22.8.10013.8329, the login page does not implement HSTS headers therefore not enforcing HTTPS. NOTE: the vendor's position is that, by design, this is controlled by a configuration option in which a customer can choose to use HTTP (rather than HTTPS) during troubleshooting.



- [https://github.com/l00neyhacker/CVE-2023-23127](https://github.com/l00neyhacker/CVE-2023-23127) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2023-23127.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2023-23127.svg)

## CVE-2023-23126
 Connectwise Automate 2022.11 is vulnerable to Clickjacking. The login screen can be iframed and used to manipulate users to perform unintended actions. NOTE: the vendor's position is that a Content-Security-Policy HTTP response header is present to block this attack.



- [https://github.com/l00neyhacker/CVE-2023-23126](https://github.com/l00neyhacker/CVE-2023-23126) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2023-23126.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2023-23126.svg)

## CVE-2023-22974
 A Path Traversal in setup.php in OpenEMR  7.0.0 allows remote unauthenticated users to read arbitrary files by controlling a connection to an attacker-controlled MySQL server.



- [https://github.com/gbrsh/CVE-2023-22974](https://github.com/gbrsh/CVE-2023-22974) :  ![starts](https://img.shields.io/github/stars/gbrsh/CVE-2023-22974.svg) ![forks](https://img.shields.io/github/forks/gbrsh/CVE-2023-22974.svg)

## CVE-2023-22960
 Lexmark products through 2023-01-10 have Improper Control of Interaction Frequency.



- [https://github.com/t3l3machus/CVE-2023-22960](https://github.com/t3l3machus/CVE-2023-22960) :  ![starts](https://img.shields.io/github/stars/t3l3machus/CVE-2023-22960.svg) ![forks](https://img.shields.io/github/forks/t3l3machus/CVE-2023-22960.svg)

## CVE-2023-22941
 In Splunk Enterprise versions below 8.1.13, 8.2.10, and 9.0.4, an improperly-formatted ‘INGEST_EVAL’ parameter in a Field Transformation crashes the Splunk daemon (splunkd).



- [https://github.com/eduardosantos1989/CVE-2023-22941](https://github.com/eduardosantos1989/CVE-2023-22941) :  ![starts](https://img.shields.io/github/stars/eduardosantos1989/CVE-2023-22941.svg) ![forks](https://img.shields.io/github/forks/eduardosantos1989/CVE-2023-22941.svg)

## CVE-2023-22906
 Hero Qubo HCD01_02_V1.38_20220125 devices allow TELNET access with root privileges by default, without a password.



- [https://github.com/nonamecoder/CVE-2023-22906](https://github.com/nonamecoder/CVE-2023-22906) :  ![starts](https://img.shields.io/github/stars/nonamecoder/CVE-2023-22906.svg) ![forks](https://img.shields.io/github/forks/nonamecoder/CVE-2023-22906.svg)

## CVE-2023-22894
 Strapi through 4.5.5 allows attackers (with access to the admin panel) to discover sensitive user details by exploiting the query filter. The attacker can filter users by columns that contain sensitive information and infer a value from API responses. If the attacker has super admin access, then this can be exploited to discover the password hash and password reset token of all users. If the attacker has admin panel access to an account with permission to access the username and email of API users with a lower privileged role (e.g., Editor or Author), then this can be exploited to discover sensitive information for all API users but not other admin accounts.



- [https://github.com/Saboor-Hakimi/CVE-2023-22894](https://github.com/Saboor-Hakimi/CVE-2023-22894) :  ![starts](https://img.shields.io/github/stars/Saboor-Hakimi/CVE-2023-22894.svg) ![forks](https://img.shields.io/github/forks/Saboor-Hakimi/CVE-2023-22894.svg)

- [https://github.com/maxntv24/CVE-2023-22894-PoC](https://github.com/maxntv24/CVE-2023-22894-PoC) :  ![starts](https://img.shields.io/github/stars/maxntv24/CVE-2023-22894-PoC.svg) ![forks](https://img.shields.io/github/forks/maxntv24/CVE-2023-22894-PoC.svg)

## CVE-2023-22884
 Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Apache Software Foundation Apache Airflow, Apache Software Foundation Apache Airflow MySQL Provider.This issue affects Apache Airflow: before 2.5.1; Apache Airflow MySQL Provider: before 4.0.0.





- [https://github.com/jakabakos/CVE-2023-22884-Airflow-SQLi](https://github.com/jakabakos/CVE-2023-22884-Airflow-SQLi) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2023-22884-Airflow-SQLi.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2023-22884-Airflow-SQLi.svg)

## CVE-2023-22855
 Kardex Mlog MCC 5.7.12+0-a203c2a213-master allows remote code execution. It spawns a web interface listening on port 8088. A user-controllable path is handed to a path-concatenation method (Path.Combine from .NET) without proper sanitisation. This yields the possibility of including local files, as well as remote files on SMB shares. If one provides a file with the extension .t4, it is rendered with the .NET templating engine mono/t4, which can execute code.



- [https://github.com/vianic/CVE-2023-22855](https://github.com/vianic/CVE-2023-22855) :  ![starts](https://img.shields.io/github/stars/vianic/CVE-2023-22855.svg) ![forks](https://img.shields.io/github/forks/vianic/CVE-2023-22855.svg)

- [https://github.com/patrickhener/CVE-2023-22855](https://github.com/patrickhener/CVE-2023-22855) :  ![starts](https://img.shields.io/github/stars/patrickhener/CVE-2023-22855.svg) ![forks](https://img.shields.io/github/forks/patrickhener/CVE-2023-22855.svg)

## CVE-2023-22809
 In Sudo before 1.9.12p2, the sudoedit (aka -e) feature mishandles extra arguments passed in the user-provided environment variables (SUDO_EDITOR, VISUAL, and EDITOR), allowing a local attacker to append arbitrary entries to the list of files to process. This can lead to privilege escalation. Affected versions are 1.8.0 through 1.9.12.p1. The problem exists because a user-specified editor may contain a "--" argument that defeats a protection mechanism, e.g., an EDITOR='vim -- /path/to/extra/file' value.



- [https://github.com/n3m1sys/CVE-2023-22809-sudoedit-privesc](https://github.com/n3m1sys/CVE-2023-22809-sudoedit-privesc) :  ![starts](https://img.shields.io/github/stars/n3m1sys/CVE-2023-22809-sudoedit-privesc.svg) ![forks](https://img.shields.io/github/forks/n3m1sys/CVE-2023-22809-sudoedit-privesc.svg)

- [https://github.com/P4x1s/CVE-2023-22809-sudo-POC](https://github.com/P4x1s/CVE-2023-22809-sudo-POC) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2023-22809-sudo-POC.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2023-22809-sudo-POC.svg)

- [https://github.com/M4fiaB0y/CVE-2023-22809](https://github.com/M4fiaB0y/CVE-2023-22809) :  ![starts](https://img.shields.io/github/stars/M4fiaB0y/CVE-2023-22809.svg) ![forks](https://img.shields.io/github/forks/M4fiaB0y/CVE-2023-22809.svg)

- [https://github.com/asepsaepdin/CVE-2023-22809](https://github.com/asepsaepdin/CVE-2023-22809) :  ![starts](https://img.shields.io/github/stars/asepsaepdin/CVE-2023-22809.svg) ![forks](https://img.shields.io/github/forks/asepsaepdin/CVE-2023-22809.svg)

- [https://github.com/Toothless5143/CVE-2023-22809](https://github.com/Toothless5143/CVE-2023-22809) :  ![starts](https://img.shields.io/github/stars/Toothless5143/CVE-2023-22809.svg) ![forks](https://img.shields.io/github/forks/Toothless5143/CVE-2023-22809.svg)

- [https://github.com/Chan9Yan9/CVE-2023-22809](https://github.com/Chan9Yan9/CVE-2023-22809) :  ![starts](https://img.shields.io/github/stars/Chan9Yan9/CVE-2023-22809.svg) ![forks](https://img.shields.io/github/forks/Chan9Yan9/CVE-2023-22809.svg)

- [https://github.com/pashayogi/CVE-2023-22809](https://github.com/pashayogi/CVE-2023-22809) :  ![starts](https://img.shields.io/github/stars/pashayogi/CVE-2023-22809.svg) ![forks](https://img.shields.io/github/forks/pashayogi/CVE-2023-22809.svg)

- [https://github.com/hello4r1end/patch_CVE-2023-22809](https://github.com/hello4r1end/patch_CVE-2023-22809) :  ![starts](https://img.shields.io/github/stars/hello4r1end/patch_CVE-2023-22809.svg) ![forks](https://img.shields.io/github/forks/hello4r1end/patch_CVE-2023-22809.svg)

- [https://github.com/Spydomain/CVE-2023-22809-automated-python-exploits](https://github.com/Spydomain/CVE-2023-22809-automated-python-exploits) :  ![starts](https://img.shields.io/github/stars/Spydomain/CVE-2023-22809-automated-python-exploits.svg) ![forks](https://img.shields.io/github/forks/Spydomain/CVE-2023-22809-automated-python-exploits.svg)

## CVE-2023-22726
 act is a project which allows for local running of github actions. The artifact server that stores artifacts from Github Action runs does not sanitize path inputs. This allows an attacker to download and overwrite arbitrary files on the host from a Github Action. This issue may lead to privilege escalation. The /upload endpoint is vulnerable to path traversal as filepath is user controlled, and ultimately flows into os.Mkdir and os.Open. The /artifact endpoint is vulnerable to path traversal as the path is variable is user controlled, and the specified file is ultimately returned by the server. This has been addressed in version 0.2.40. Users are advised to upgrade. Users unable to upgrade may, during implementation of Open and OpenAtEnd for FS, ensure to use ValidPath() to check against path traversal or clean the user-provided paths manually.



- [https://github.com/ProxyPog/POC-CVE-2023-22726](https://github.com/ProxyPog/POC-CVE-2023-22726) :  ![starts](https://img.shields.io/github/stars/ProxyPog/POC-CVE-2023-22726.svg) ![forks](https://img.shields.io/github/forks/ProxyPog/POC-CVE-2023-22726.svg)

## CVE-2023-22622
 WordPress through 6.1.1 depends on unpredictable client visits to cause wp-cron.php execution and the resulting security updates, and the source code describes "the scenario where a site may not receive enough visits to execute scheduled tasks in a timely manner," but neither the installation guide nor the security guide mentions this default behavior, or alerts the user about security risks on installations with very few visits.



- [https://github.com/michael-david-fry/CVE-2023-22622](https://github.com/michael-david-fry/CVE-2023-22622) :  ![starts](https://img.shields.io/github/stars/michael-david-fry/CVE-2023-22622.svg) ![forks](https://img.shields.io/github/forks/michael-david-fry/CVE-2023-22622.svg)

## CVE-2023-22621
 Strapi through 4.5.5 allows authenticated Server-Side Template Injection (SSTI) that can be exploited to execute arbitrary code on the server. A remote attacker with access to the Strapi admin panel can inject a crafted payload that executes code on the server into an email template that bypasses the validation checks that should prevent code execution.



- [https://github.com/sofianeelhor/CVE-2023-22621-POC](https://github.com/sofianeelhor/CVE-2023-22621-POC) :  ![starts](https://img.shields.io/github/stars/sofianeelhor/CVE-2023-22621-POC.svg) ![forks](https://img.shields.io/github/forks/sofianeelhor/CVE-2023-22621-POC.svg)

## CVE-2023-22551
 The FTP (aka "Implementation of a simple FTP client and server") project through 96c1a35 allows remote attackers to cause a denial of service (memory consumption) by engaging in client activity, such as establishing and then terminating a connection. This occurs because malloc is used but free is not.



- [https://github.com/viswagb/CVE-2023-22551](https://github.com/viswagb/CVE-2023-22551) :  ![starts](https://img.shields.io/github/stars/viswagb/CVE-2023-22551.svg) ![forks](https://img.shields.io/github/forks/viswagb/CVE-2023-22551.svg)

## CVE-2023-22527
 A template injection vulnerability on older versions of Confluence Data Center and Server allows an unauthenticated attacker to achieve RCE on an affected instance. Customers using an affected version must take immediate action.

Most recent supported versions of Confluence Data Center and Server are not affected by this vulnerability as it was ultimately mitigated during regular version updates. However, Atlassian recommends that customers take care to install the latest version to protect their instances from non-critical vulnerabilities outlined in Atlassian’s January Security Bulletin.



- [https://github.com/gobysec/Goby](https://github.com/gobysec/Goby) :  ![starts](https://img.shields.io/github/stars/gobysec/Goby.svg) ![forks](https://img.shields.io/github/forks/gobysec/Goby.svg)

- [https://github.com/gobysec/GobyVuls](https://github.com/gobysec/GobyVuls) :  ![starts](https://img.shields.io/github/stars/gobysec/GobyVuls.svg) ![forks](https://img.shields.io/github/forks/gobysec/GobyVuls.svg)

- [https://github.com/Boogipop/CVE-2023-22527-Godzilla-MEMSHELL](https://github.com/Boogipop/CVE-2023-22527-Godzilla-MEMSHELL) :  ![starts](https://img.shields.io/github/stars/Boogipop/CVE-2023-22527-Godzilla-MEMSHELL.svg) ![forks](https://img.shields.io/github/forks/Boogipop/CVE-2023-22527-Godzilla-MEMSHELL.svg)

- [https://github.com/M0untainShley/CVE-2023-22527-MEMSHELL](https://github.com/M0untainShley/CVE-2023-22527-MEMSHELL) :  ![starts](https://img.shields.io/github/stars/M0untainShley/CVE-2023-22527-MEMSHELL.svg) ![forks](https://img.shields.io/github/forks/M0untainShley/CVE-2023-22527-MEMSHELL.svg)

- [https://github.com/Avento/CVE-2023-22527_Confluence_RCE](https://github.com/Avento/CVE-2023-22527_Confluence_RCE) :  ![starts](https://img.shields.io/github/stars/Avento/CVE-2023-22527_Confluence_RCE.svg) ![forks](https://img.shields.io/github/forks/Avento/CVE-2023-22527_Confluence_RCE.svg)

- [https://github.com/Manh130902/CVE-2023-22527-POC](https://github.com/Manh130902/CVE-2023-22527-POC) :  ![starts](https://img.shields.io/github/stars/Manh130902/CVE-2023-22527-POC.svg) ![forks](https://img.shields.io/github/forks/Manh130902/CVE-2023-22527-POC.svg)

- [https://github.com/VNCERT-CC/CVE-2023-22527-confluence](https://github.com/VNCERT-CC/CVE-2023-22527-confluence) :  ![starts](https://img.shields.io/github/stars/VNCERT-CC/CVE-2023-22527-confluence.svg) ![forks](https://img.shields.io/github/forks/VNCERT-CC/CVE-2023-22527-confluence.svg)

- [https://github.com/Vozec/CVE-2023-22527](https://github.com/Vozec/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/Vozec/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/Vozec/CVE-2023-22527.svg)

- [https://github.com/RevoltSecurities/CVE-2023-22527](https://github.com/RevoltSecurities/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/RevoltSecurities/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/RevoltSecurities/CVE-2023-22527.svg)

- [https://github.com/Chocapikk/CVE-2023-22527](https://github.com/Chocapikk/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-22527.svg)

- [https://github.com/vulncheck-oss/cve-2023-22527](https://github.com/vulncheck-oss/cve-2023-22527) :  ![starts](https://img.shields.io/github/stars/vulncheck-oss/cve-2023-22527.svg) ![forks](https://img.shields.io/github/forks/vulncheck-oss/cve-2023-22527.svg)

- [https://github.com/Privia-Security/CVE-2023-22527](https://github.com/Privia-Security/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/Privia-Security/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/Privia-Security/CVE-2023-22527.svg)

- [https://github.com/thanhlam-attt/CVE-2023-22527](https://github.com/thanhlam-attt/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/thanhlam-attt/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/thanhlam-attt/CVE-2023-22527.svg)

- [https://github.com/adminlove520/CVE-2023-22527](https://github.com/adminlove520/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/adminlove520/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/adminlove520/CVE-2023-22527.svg)

- [https://github.com/C1ph3rX13/CVE-2023-22527](https://github.com/C1ph3rX13/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/C1ph3rX13/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/C1ph3rX13/CVE-2023-22527.svg)

- [https://github.com/yoryio/CVE-2023-22527](https://github.com/yoryio/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/yoryio/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/yoryio/CVE-2023-22527.svg)

- [https://github.com/BBD-YZZ/Confluence-RCE](https://github.com/BBD-YZZ/Confluence-RCE) :  ![starts](https://img.shields.io/github/stars/BBD-YZZ/Confluence-RCE.svg) ![forks](https://img.shields.io/github/forks/BBD-YZZ/Confluence-RCE.svg)

- [https://github.com/Sudistark/patch-diff-CVE-2023-22527](https://github.com/Sudistark/patch-diff-CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/Sudistark/patch-diff-CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/Sudistark/patch-diff-CVE-2023-22527.svg)

- [https://github.com/Niuwoo/CVE-2023-22527](https://github.com/Niuwoo/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/Niuwoo/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/Niuwoo/CVE-2023-22527.svg)

- [https://github.com/Drun1baby/CVE-2023-22527](https://github.com/Drun1baby/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/Drun1baby/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/Drun1baby/CVE-2023-22527.svg)

- [https://github.com/ga0we1/CVE-2023-22527_Confluence_RCE](https://github.com/ga0we1/CVE-2023-22527_Confluence_RCE) :  ![starts](https://img.shields.io/github/stars/ga0we1/CVE-2023-22527_Confluence_RCE.svg) ![forks](https://img.shields.io/github/forks/ga0we1/CVE-2023-22527_Confluence_RCE.svg)

- [https://github.com/cleverg0d/CVE-2023-22527](https://github.com/cleverg0d/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/cleverg0d/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/cleverg0d/CVE-2023-22527.svg)

- [https://github.com/MaanVader/CVE-2023-22527-POC](https://github.com/MaanVader/CVE-2023-22527-POC) :  ![starts](https://img.shields.io/github/stars/MaanVader/CVE-2023-22527-POC.svg) ![forks](https://img.shields.io/github/forks/MaanVader/CVE-2023-22527-POC.svg)

- [https://github.com/YongYe-Security/CVE-2023-22527](https://github.com/YongYe-Security/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/YongYe-Security/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/YongYe-Security/CVE-2023-22527.svg)

- [https://github.com/thompson005/CVE-2023-22527](https://github.com/thompson005/CVE-2023-22527) :  ![starts](https://img.shields.io/github/stars/thompson005/CVE-2023-22527.svg) ![forks](https://img.shields.io/github/forks/thompson005/CVE-2023-22527.svg)

## CVE-2023-22524
 Certain versions of the Atlassian Companion App for MacOS were affected by a remote code execution vulnerability. An attacker could utilize WebSockets to bypass Atlassian Companion’s blocklist and MacOS Gatekeeper to allow execution of code.



- [https://github.com/ron-imperva/CVE-2023-22524](https://github.com/ron-imperva/CVE-2023-22524) :  ![starts](https://img.shields.io/github/stars/ron-imperva/CVE-2023-22524.svg) ![forks](https://img.shields.io/github/forks/ron-imperva/CVE-2023-22524.svg)

- [https://github.com/imperva/CVE-2023-22524](https://github.com/imperva/CVE-2023-22524) :  ![starts](https://img.shields.io/github/stars/imperva/CVE-2023-22524.svg) ![forks](https://img.shields.io/github/forks/imperva/CVE-2023-22524.svg)

## CVE-2023-22518
 All versions of Confluence Data Center and Server are affected by this unexploited vulnerability. This Improper Authorization vulnerability allows an unauthenticated attacker to reset Confluence and create a Confluence instance administrator account. Using this account, an attacker can then perform all administrative actions that are available to Confluence instance administrator leading to - but not limited to - full loss of confidentiality, integrity and availability. 

Atlassian Cloud sites are not affected by this vulnerability. If your Confluence site is accessed via an atlassian.net domain, it is hosted by Atlassian and is not vulnerable to this issue.



- [https://github.com/ForceFledgling/CVE-2023-22518](https://github.com/ForceFledgling/CVE-2023-22518) :  ![starts](https://img.shields.io/github/stars/ForceFledgling/CVE-2023-22518.svg) ![forks](https://img.shields.io/github/forks/ForceFledgling/CVE-2023-22518.svg)

- [https://github.com/RevoltSecurities/CVE-2023-22518](https://github.com/RevoltSecurities/CVE-2023-22518) :  ![starts](https://img.shields.io/github/stars/RevoltSecurities/CVE-2023-22518.svg) ![forks](https://img.shields.io/github/forks/RevoltSecurities/CVE-2023-22518.svg)

- [https://github.com/davidfortytwo/CVE-2023-22518](https://github.com/davidfortytwo/CVE-2023-22518) :  ![starts](https://img.shields.io/github/stars/davidfortytwo/CVE-2023-22518.svg) ![forks](https://img.shields.io/github/forks/davidfortytwo/CVE-2023-22518.svg)

- [https://github.com/0x0d3ad/CVE-2023-22518](https://github.com/0x0d3ad/CVE-2023-22518) :  ![starts](https://img.shields.io/github/stars/0x0d3ad/CVE-2023-22518.svg) ![forks](https://img.shields.io/github/forks/0x0d3ad/CVE-2023-22518.svg)

- [https://github.com/0x00sector/CVE_2023_22518_Checker](https://github.com/0x00sector/CVE_2023_22518_Checker) :  ![starts](https://img.shields.io/github/stars/0x00sector/CVE_2023_22518_Checker.svg) ![forks](https://img.shields.io/github/forks/0x00sector/CVE_2023_22518_Checker.svg)

- [https://github.com/bibo318/CVE-2023-22518](https://github.com/bibo318/CVE-2023-22518) :  ![starts](https://img.shields.io/github/stars/bibo318/CVE-2023-22518.svg) ![forks](https://img.shields.io/github/forks/bibo318/CVE-2023-22518.svg)

- [https://github.com/Lilly-dox/Exploit-CVE-2023-22518](https://github.com/Lilly-dox/Exploit-CVE-2023-22518) :  ![starts](https://img.shields.io/github/stars/Lilly-dox/Exploit-CVE-2023-22518.svg) ![forks](https://img.shields.io/github/forks/Lilly-dox/Exploit-CVE-2023-22518.svg)

- [https://github.com/ductink98lhp/analyze-Exploit-CVE-2023-22518-Confluence](https://github.com/ductink98lhp/analyze-Exploit-CVE-2023-22518-Confluence) :  ![starts](https://img.shields.io/github/stars/ductink98lhp/analyze-Exploit-CVE-2023-22518-Confluence.svg) ![forks](https://img.shields.io/github/forks/ductink98lhp/analyze-Exploit-CVE-2023-22518-Confluence.svg)

- [https://github.com/C1ph3rX13/CVE-2023-22518](https://github.com/C1ph3rX13/CVE-2023-22518) :  ![starts](https://img.shields.io/github/stars/C1ph3rX13/CVE-2023-22518.svg) ![forks](https://img.shields.io/github/forks/C1ph3rX13/CVE-2023-22518.svg)

## CVE-2023-22515
 Atlassian has been made aware of an issue reported by a handful of customers where external attackers may have exploited a previously unknown vulnerability in publicly accessible Confluence Data Center and Server instances to create unauthorized Confluence administrator accounts and access Confluence instances. 

Atlassian Cloud sites are not affected by this vulnerability. If your Confluence site is accessed via an atlassian.net domain, it is hosted by Atlassian and is not vulnerable to this issue. 



- [https://github.com/Chocapikk/CVE-2023-22515](https://github.com/Chocapikk/CVE-2023-22515) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-22515.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-22515.svg)

- [https://github.com/ad-calcium/CVE-2023-22515](https://github.com/ad-calcium/CVE-2023-22515) :  ![starts](https://img.shields.io/github/stars/ad-calcium/CVE-2023-22515.svg) ![forks](https://img.shields.io/github/forks/ad-calcium/CVE-2023-22515.svg)

- [https://github.com/ErikWynter/CVE-2023-22515-Scan](https://github.com/ErikWynter/CVE-2023-22515-Scan) :  ![starts](https://img.shields.io/github/stars/ErikWynter/CVE-2023-22515-Scan.svg) ![forks](https://img.shields.io/github/forks/ErikWynter/CVE-2023-22515-Scan.svg)

- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/spark1security/n0s1](https://github.com/spark1security/n0s1) :  ![starts](https://img.shields.io/github/stars/spark1security/n0s1.svg) ![forks](https://img.shields.io/github/forks/spark1security/n0s1.svg)

- [https://github.com/AIex-3/confluence-hack](https://github.com/AIex-3/confluence-hack) :  ![starts](https://img.shields.io/github/stars/AIex-3/confluence-hack.svg) ![forks](https://img.shields.io/github/forks/AIex-3/confluence-hack.svg)

- [https://github.com/sincere9/CVE-2023-22515](https://github.com/sincere9/CVE-2023-22515) :  ![starts](https://img.shields.io/github/stars/sincere9/CVE-2023-22515.svg) ![forks](https://img.shields.io/github/forks/sincere9/CVE-2023-22515.svg)

- [https://github.com/aaaademo/Confluence-EvilJar](https://github.com/aaaademo/Confluence-EvilJar) :  ![starts](https://img.shields.io/github/stars/aaaademo/Confluence-EvilJar.svg) ![forks](https://img.shields.io/github/forks/aaaademo/Confluence-EvilJar.svg)

- [https://github.com/youcannotseemeagain/CVE-2023-22515_RCE](https://github.com/youcannotseemeagain/CVE-2023-22515_RCE) :  ![starts](https://img.shields.io/github/stars/youcannotseemeagain/CVE-2023-22515_RCE.svg) ![forks](https://img.shields.io/github/forks/youcannotseemeagain/CVE-2023-22515_RCE.svg)

- [https://github.com/j3seer/CVE-2023-22515-POC](https://github.com/j3seer/CVE-2023-22515-POC) :  ![starts](https://img.shields.io/github/stars/j3seer/CVE-2023-22515-POC.svg) ![forks](https://img.shields.io/github/forks/j3seer/CVE-2023-22515-POC.svg)

- [https://github.com/Le1a/CVE-2023-22515](https://github.com/Le1a/CVE-2023-22515) :  ![starts](https://img.shields.io/github/stars/Le1a/CVE-2023-22515.svg) ![forks](https://img.shields.io/github/forks/Le1a/CVE-2023-22515.svg)

- [https://github.com/kh4sh3i/CVE-2023-22515](https://github.com/kh4sh3i/CVE-2023-22515) :  ![starts](https://img.shields.io/github/stars/kh4sh3i/CVE-2023-22515.svg) ![forks](https://img.shields.io/github/forks/kh4sh3i/CVE-2023-22515.svg)

- [https://github.com/spareack/CVE-2023-22515-NSE](https://github.com/spareack/CVE-2023-22515-NSE) :  ![starts](https://img.shields.io/github/stars/spareack/CVE-2023-22515-NSE.svg) ![forks](https://img.shields.io/github/forks/spareack/CVE-2023-22515-NSE.svg)

- [https://github.com/Vulnmachines/confluence-cve-2023-22515](https://github.com/Vulnmachines/confluence-cve-2023-22515) :  ![starts](https://img.shields.io/github/stars/Vulnmachines/confluence-cve-2023-22515.svg) ![forks](https://img.shields.io/github/forks/Vulnmachines/confluence-cve-2023-22515.svg)

- [https://github.com/LucasPDiniz/CVE-2023-22515](https://github.com/LucasPDiniz/CVE-2023-22515) :  ![starts](https://img.shields.io/github/stars/LucasPDiniz/CVE-2023-22515.svg) ![forks](https://img.shields.io/github/forks/LucasPDiniz/CVE-2023-22515.svg)

- [https://github.com/fyx1t/NSE--CVE-2023-22515](https://github.com/fyx1t/NSE--CVE-2023-22515) :  ![starts](https://img.shields.io/github/stars/fyx1t/NSE--CVE-2023-22515.svg) ![forks](https://img.shields.io/github/forks/fyx1t/NSE--CVE-2023-22515.svg)

- [https://github.com/C1ph3rX13/CVE-2023-22515](https://github.com/C1ph3rX13/CVE-2023-22515) :  ![starts](https://img.shields.io/github/stars/C1ph3rX13/CVE-2023-22515.svg) ![forks](https://img.shields.io/github/forks/C1ph3rX13/CVE-2023-22515.svg)

- [https://github.com/iveresk/CVE-2023-22515](https://github.com/iveresk/CVE-2023-22515) :  ![starts](https://img.shields.io/github/stars/iveresk/CVE-2023-22515.svg) ![forks](https://img.shields.io/github/forks/iveresk/CVE-2023-22515.svg)

- [https://github.com/rxerium/CVE-2023-22515](https://github.com/rxerium/CVE-2023-22515) :  ![starts](https://img.shields.io/github/stars/rxerium/CVE-2023-22515.svg) ![forks](https://img.shields.io/github/forks/rxerium/CVE-2023-22515.svg)

- [https://github.com/Onedy1703/CVE-2023-22515-Confluence](https://github.com/Onedy1703/CVE-2023-22515-Confluence) :  ![starts](https://img.shields.io/github/stars/Onedy1703/CVE-2023-22515-Confluence.svg) ![forks](https://img.shields.io/github/forks/Onedy1703/CVE-2023-22515-Confluence.svg)

- [https://github.com/xorbbo/cve-2023-22515](https://github.com/xorbbo/cve-2023-22515) :  ![starts](https://img.shields.io/github/stars/xorbbo/cve-2023-22515.svg) ![forks](https://img.shields.io/github/forks/xorbbo/cve-2023-22515.svg)

- [https://github.com/INTfinityConsulting/cve-2023-22515](https://github.com/INTfinityConsulting/cve-2023-22515) :  ![starts](https://img.shields.io/github/stars/INTfinityConsulting/cve-2023-22515.svg) ![forks](https://img.shields.io/github/forks/INTfinityConsulting/cve-2023-22515.svg)

- [https://github.com/killvxk/CVE-2023-22515-joaoviictorti](https://github.com/killvxk/CVE-2023-22515-joaoviictorti) :  ![starts](https://img.shields.io/github/stars/killvxk/CVE-2023-22515-joaoviictorti.svg) ![forks](https://img.shields.io/github/forks/killvxk/CVE-2023-22515-joaoviictorti.svg)

- [https://github.com/CalegariMindSec/Exploit-CVE-2023-22515](https://github.com/CalegariMindSec/Exploit-CVE-2023-22515) :  ![starts](https://img.shields.io/github/stars/CalegariMindSec/Exploit-CVE-2023-22515.svg) ![forks](https://img.shields.io/github/forks/CalegariMindSec/Exploit-CVE-2023-22515.svg)

- [https://github.com/s1d6point7bugcrowd/CVE-2023-22515-check](https://github.com/s1d6point7bugcrowd/CVE-2023-22515-check) :  ![starts](https://img.shields.io/github/stars/s1d6point7bugcrowd/CVE-2023-22515-check.svg) ![forks](https://img.shields.io/github/forks/s1d6point7bugcrowd/CVE-2023-22515-check.svg)

- [https://github.com/edsonjt81/CVE-2023-22515-Scan.](https://github.com/edsonjt81/CVE-2023-22515-Scan.) :  ![starts](https://img.shields.io/github/stars/edsonjt81/CVE-2023-22515-Scan..svg) ![forks](https://img.shields.io/github/forks/edsonjt81/CVE-2023-22515-Scan..svg)

- [https://github.com/DsaHen/cve-2023-22515-exp](https://github.com/DsaHen/cve-2023-22515-exp) :  ![starts](https://img.shields.io/github/stars/DsaHen/cve-2023-22515-exp.svg) ![forks](https://img.shields.io/github/forks/DsaHen/cve-2023-22515-exp.svg)

## CVE-2023-22493
 RSSHub is an open source RSS feed generator. RSSHub is vulnerable to Server-Side Request Forgery (SSRF) attacks. This vulnerability allows an attacker to send arbitrary HTTP requests from the server to other servers or resources on the network. An attacker can exploit this vulnerability by sending a request to the affected routes with a malicious URL. An attacker could also use this vulnerability to send requests to internal or any other servers or resources on the network, potentially gain access to sensitive information that would not normally be accessible and amplifying the impact of the attack. The patch for this issue can be found in commit a66cbcf. 



- [https://github.com/buitanhung144/SSRF-CVE-2023-22493](https://github.com/buitanhung144/SSRF-CVE-2023-22493) :  ![starts](https://img.shields.io/github/stars/buitanhung144/SSRF-CVE-2023-22493.svg) ![forks](https://img.shields.io/github/forks/buitanhung144/SSRF-CVE-2023-22493.svg)

## CVE-2023-22490
 Git is a revision control system. Using a specially-crafted repository, Git prior to versions 2.39.2, 2.38.4, 2.37.6, 2.36.5, 2.35.7, 2.34.7, 2.33.7, 2.32.6, 2.31.7, and 2.30.8 can be tricked into using its local clone optimization even when using a non-local transport. Though Git will abort local clones whose source `$GIT_DIR/objects` directory contains symbolic links, the `objects` directory itself may still be a symbolic link. These two may be combined to include arbitrary files based on known paths on the victim's filesystem within the malicious repository's working copy, allowing for data exfiltration in a similar manner as CVE-2022-39253.

A fix has been prepared and will appear in v2.39.2 v2.38.4 v2.37.6 v2.36.5 v2.35.7 v2.34.7 v2.33.7 v2.32.6, v2.31.7 and v2.30.8. If upgrading is impractical, two short-term workarounds are available. Avoid cloning repositories from untrusted sources with `--recurse-submodules`. Instead, consider cloning repositories without recursively cloning their submodules, and instead run `git submodule update` at each layer. Before doing so, inspect each new `.gitmodules` file to ensure that it does not contain suspicious module URLs.



- [https://github.com/smash8tap/CVE-2023-22490_PoC](https://github.com/smash8tap/CVE-2023-22490_PoC) :  ![starts](https://img.shields.io/github/stars/smash8tap/CVE-2023-22490_PoC.svg) ![forks](https://img.shields.io/github/forks/smash8tap/CVE-2023-22490_PoC.svg)

## CVE-2023-22432
 Open redirect vulnerability exists in web2py versions prior to 2.23.1. When using the tool, a web2py user may be redirected to an arbitrary website by accessing a specially crafted URL. As a result, the user may become a victim of a phishing attack.



- [https://github.com/aeyesec/CVE-2023-22432](https://github.com/aeyesec/CVE-2023-22432) :  ![starts](https://img.shields.io/github/stars/aeyesec/CVE-2023-22432.svg) ![forks](https://img.shields.io/github/forks/aeyesec/CVE-2023-22432.svg)

## CVE-2023-22077
 Vulnerability in the Oracle Database Recovery Manager component of Oracle Database Server.  Supported versions that are affected are 19.3-19.20 and  21.3-21.11. Easily exploitable vulnerability allows high privileged attacker having DBA account privilege with network access via Oracle Net to compromise Oracle Database Recovery Manager.  Successful attacks of this vulnerability can result in unauthorized ability to cause a hang or frequently repeatable crash (complete DOS) of Oracle Database Recovery Manager. CVSS 3.1 Base Score 4.9 (Availability impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:H).



- [https://github.com/emad-almousa/CVE-2023-22077](https://github.com/emad-almousa/CVE-2023-22077) :  ![starts](https://img.shields.io/github/stars/emad-almousa/CVE-2023-22077.svg) ![forks](https://img.shields.io/github/forks/emad-almousa/CVE-2023-22077.svg)

## CVE-2023-22074
 Vulnerability in the Oracle Database Sharding component of Oracle Database Server.  Supported versions that are affected are 19.3-19.20 and  21.3-21.11. Easily exploitable vulnerability allows high privileged attacker having Create Session, Select Any Dictionary privilege with network access via Oracle Net to compromise Oracle Database Sharding.  Successful attacks require human interaction from a person other than the attacker. Successful attacks of this vulnerability can result in unauthorized ability to cause a partial denial of service (partial DOS) of Oracle Database Sharding. CVSS 3.1 Base Score 2.4 (Availability impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:U/C:N/I:N/A:L).



- [https://github.com/emad-almousa/CVE-2023-22074](https://github.com/emad-almousa/CVE-2023-22074) :  ![starts](https://img.shields.io/github/stars/emad-almousa/CVE-2023-22074.svg) ![forks](https://img.shields.io/github/forks/emad-almousa/CVE-2023-22074.svg)

## CVE-2023-22047
 Vulnerability in the PeopleSoft Enterprise PeopleTools product of Oracle PeopleSoft (component: Portal).  Supported versions that are affected are 8.59 and  8.60. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise PeopleSoft Enterprise PeopleTools.  Successful attacks of this vulnerability can result in  unauthorized access to critical data or complete access to all PeopleSoft Enterprise PeopleTools accessible data. CVSS 3.1 Base Score 7.5 (Confidentiality impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N).



- [https://github.com/tuo4n8/CVE-2023-22047](https://github.com/tuo4n8/CVE-2023-22047) :  ![starts](https://img.shields.io/github/stars/tuo4n8/CVE-2023-22047.svg) ![forks](https://img.shields.io/github/forks/tuo4n8/CVE-2023-22047.svg)

## CVE-2023-21971
 Vulnerability in the MySQL Connectors product of Oracle MySQL (component: Connector/J).  Supported versions that are affected are 8.0.32 and prior. Difficult to exploit vulnerability allows high privileged attacker with network access via multiple protocols to compromise MySQL Connectors.  Successful attacks require human interaction from a person other than the attacker. Successful attacks of this vulnerability can result in unauthorized ability to cause a hang or frequently repeatable crash (complete DOS) of MySQL Connectors as well as  unauthorized update, insert or delete access to some of MySQL Connectors accessible data and  unauthorized read access to a subset of MySQL Connectors accessible data. CVSS 3.1 Base Score 5.3 (Confidentiality, Integrity and Availability impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:H/PR:H/UI:R/S:U/C:L/I:L/A:H).



- [https://github.com/Avento/CVE-2023-21971_Analysis](https://github.com/Avento/CVE-2023-21971_Analysis) :  ![starts](https://img.shields.io/github/stars/Avento/CVE-2023-21971_Analysis.svg) ![forks](https://img.shields.io/github/forks/Avento/CVE-2023-21971_Analysis.svg)

## CVE-2023-21939
 Vulnerability in the Oracle Java SE, Oracle GraalVM Enterprise Edition product of Oracle Java SE (component: Swing).  Supported versions that are affected are Oracle Java SE: 8u361, 8u361-perf, 11.0.18, 17.0.6, 20; Oracle GraalVM Enterprise Edition: 20.3.9, 21.3.5 and  22.3.1. Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Java SE, Oracle GraalVM Enterprise Edition.  Successful attacks of this vulnerability can result in  unauthorized update, insert or delete access to some of Oracle Java SE, Oracle GraalVM Enterprise Edition accessible data. Note: This vulnerability applies to Java deployments, typically in clients running sandboxed Java Web Start applications or sandboxed Java applets, that load and run untrusted code (e.g., code that comes from the internet) and rely on the Java sandbox for security. This vulnerability can also be exploited by using APIs in the specified Component, e.g., through a web service which supplies data to the APIs. CVSS 3.1 Base Score 5.3 (Integrity impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N).



- [https://github.com/Y4Sec-Team/CVE-2023-21939](https://github.com/Y4Sec-Team/CVE-2023-21939) :  ![starts](https://img.shields.io/github/stars/Y4Sec-Team/CVE-2023-21939.svg) ![forks](https://img.shields.io/github/forks/Y4Sec-Team/CVE-2023-21939.svg)

## CVE-2023-21931
 Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions that are affected are 12.2.1.3.0, 12.2.1.4.0 and  14.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via T3 to compromise Oracle WebLogic Server.  Successful attacks of this vulnerability can result in  unauthorized access to critical data or complete access to all Oracle WebLogic Server accessible data. CVSS 3.1 Base Score 7.5 (Confidentiality impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N).



- [https://github.com/gobysec/Weblogic](https://github.com/gobysec/Weblogic) :  ![starts](https://img.shields.io/github/stars/gobysec/Weblogic.svg) ![forks](https://img.shields.io/github/forks/gobysec/Weblogic.svg)

- [https://github.com/TimeSHU/weblogic_CVE-2023-21931_POC-EXP](https://github.com/TimeSHU/weblogic_CVE-2023-21931_POC-EXP) :  ![starts](https://img.shields.io/github/stars/TimeSHU/weblogic_CVE-2023-21931_POC-EXP.svg) ![forks](https://img.shields.io/github/forks/TimeSHU/weblogic_CVE-2023-21931_POC-EXP.svg)

## CVE-2023-21887
 Vulnerability in the MySQL Server product of Oracle MySQL (component: Server: GIS).  Supported versions that are affected are 8.0.31 and prior. Easily exploitable vulnerability allows high privileged attacker with network access via multiple protocols to compromise MySQL Server.  Successful attacks of this vulnerability can result in unauthorized ability to cause a hang or frequently repeatable crash (complete DOS) of MySQL Server. CVSS 3.1 Base Score 4.9 (Availability impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:H).



- [https://github.com/zwxxb/CVE-2023-21887](https://github.com/zwxxb/CVE-2023-21887) :  ![starts](https://img.shields.io/github/stars/zwxxb/CVE-2023-21887.svg) ![forks](https://img.shields.io/github/forks/zwxxb/CVE-2023-21887.svg)

## CVE-2023-21839
 Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions that are affected are 12.2.1.3.0, 12.2.1.4.0 and  14.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server.  Successful attacks of this vulnerability can result in  unauthorized access to critical data or complete access to all Oracle WebLogic Server accessible data. CVSS 3.1 Base Score 7.5 (Confidentiality impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N).



- [https://github.com/DXask88MA/Weblogic-CVE-2023-21839](https://github.com/DXask88MA/Weblogic-CVE-2023-21839) :  ![starts](https://img.shields.io/github/stars/DXask88MA/Weblogic-CVE-2023-21839.svg) ![forks](https://img.shields.io/github/forks/DXask88MA/Weblogic-CVE-2023-21839.svg)

- [https://github.com/gobysec/Weblogic](https://github.com/gobysec/Weblogic) :  ![starts](https://img.shields.io/github/stars/gobysec/Weblogic.svg) ![forks](https://img.shields.io/github/forks/gobysec/Weblogic.svg)

- [https://github.com/ASkyeye/CVE-2023-21839](https://github.com/ASkyeye/CVE-2023-21839) :  ![starts](https://img.shields.io/github/stars/ASkyeye/CVE-2023-21839.svg) ![forks](https://img.shields.io/github/forks/ASkyeye/CVE-2023-21839.svg)

- [https://github.com/dinosn/CVE-2024-20931](https://github.com/dinosn/CVE-2024-20931) :  ![starts](https://img.shields.io/github/stars/dinosn/CVE-2024-20931.svg) ![forks](https://img.shields.io/github/forks/dinosn/CVE-2024-20931.svg)

- [https://github.com/Firebasky/CVE-2023-21839](https://github.com/Firebasky/CVE-2023-21839) :  ![starts](https://img.shields.io/github/stars/Firebasky/CVE-2023-21839.svg) ![forks](https://img.shields.io/github/forks/Firebasky/CVE-2023-21839.svg)

- [https://github.com/houqe/POC_CVE-2023-21839](https://github.com/houqe/POC_CVE-2023-21839) :  ![starts](https://img.shields.io/github/stars/houqe/POC_CVE-2023-21839.svg) ![forks](https://img.shields.io/github/forks/houqe/POC_CVE-2023-21839.svg)

- [https://github.com/Romanc9/Gui-poc-test](https://github.com/Romanc9/Gui-poc-test) :  ![starts](https://img.shields.io/github/stars/Romanc9/Gui-poc-test.svg) ![forks](https://img.shields.io/github/forks/Romanc9/Gui-poc-test.svg)

- [https://github.com/0xn0ne/simple-scanner](https://github.com/0xn0ne/simple-scanner) :  ![starts](https://img.shields.io/github/stars/0xn0ne/simple-scanner.svg) ![forks](https://img.shields.io/github/forks/0xn0ne/simple-scanner.svg)

- [https://github.com/fakenews2025/CVE-2023-21839](https://github.com/fakenews2025/CVE-2023-21839) :  ![starts](https://img.shields.io/github/stars/fakenews2025/CVE-2023-21839.svg) ![forks](https://img.shields.io/github/forks/fakenews2025/CVE-2023-21839.svg)

- [https://github.com/kw3h4/CVE-2023-21839-metasploit-scanner](https://github.com/kw3h4/CVE-2023-21839-metasploit-scanner) :  ![starts](https://img.shields.io/github/stars/kw3h4/CVE-2023-21839-metasploit-scanner.svg) ![forks](https://img.shields.io/github/forks/kw3h4/CVE-2023-21839-metasploit-scanner.svg)

## CVE-2023-21837
 Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions that are affected are 12.2.1.3.0, 12.2.1.4.0 and  14.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via IIOP to compromise Oracle WebLogic Server.  Successful attacks of this vulnerability can result in  unauthorized access to critical data or complete access to all Oracle WebLogic Server accessible data. CVSS 3.1 Base Score 7.5 (Confidentiality impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N).



- [https://github.com/hktalent/CVE-2023-21837](https://github.com/hktalent/CVE-2023-21837) :  ![starts](https://img.shields.io/github/stars/hktalent/CVE-2023-21837.svg) ![forks](https://img.shields.io/github/forks/hktalent/CVE-2023-21837.svg)

## CVE-2023-21823
 Windows Graphics Component Remote Code Execution Vulnerability



- [https://github.com/Elizarfish/CVE-2023-21823](https://github.com/Elizarfish/CVE-2023-21823) :  ![starts](https://img.shields.io/github/stars/Elizarfish/CVE-2023-21823.svg) ![forks](https://img.shields.io/github/forks/Elizarfish/CVE-2023-21823.svg)

## CVE-2023-21822
 Windows Graphics Component Elevation of Privilege Vulnerability



- [https://github.com/DashaMilitskaya/cve_2023_21822](https://github.com/DashaMilitskaya/cve_2023_21822) :  ![starts](https://img.shields.io/github/stars/DashaMilitskaya/cve_2023_21822.svg) ![forks](https://img.shields.io/github/forks/DashaMilitskaya/cve_2023_21822.svg)

## CVE-2023-21768
 Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability



- [https://github.com/chompie1337/Windows_LPE_AFD_CVE-2023-21768](https://github.com/chompie1337/Windows_LPE_AFD_CVE-2023-21768) :  ![starts](https://img.shields.io/github/stars/chompie1337/Windows_LPE_AFD_CVE-2023-21768.svg) ![forks](https://img.shields.io/github/forks/chompie1337/Windows_LPE_AFD_CVE-2023-21768.svg)

- [https://github.com/SamuelTulach/nullmap](https://github.com/SamuelTulach/nullmap) :  ![starts](https://img.shields.io/github/stars/SamuelTulach/nullmap.svg) ![forks](https://img.shields.io/github/forks/SamuelTulach/nullmap.svg)

- [https://github.com/Malwareman007/CVE-2023-21768](https://github.com/Malwareman007/CVE-2023-21768) :  ![starts](https://img.shields.io/github/stars/Malwareman007/CVE-2023-21768.svg) ![forks](https://img.shields.io/github/forks/Malwareman007/CVE-2023-21768.svg)

- [https://github.com/cl4ym0re/cve-2023-21768-compiled](https://github.com/cl4ym0re/cve-2023-21768-compiled) :  ![starts](https://img.shields.io/github/stars/cl4ym0re/cve-2023-21768-compiled.svg) ![forks](https://img.shields.io/github/forks/cl4ym0re/cve-2023-21768-compiled.svg)

- [https://github.com/P4x1s/CVE-2023-21768-POC](https://github.com/P4x1s/CVE-2023-21768-POC) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2023-21768-POC.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2023-21768-POC.svg)

- [https://github.com/zoemurmure/CVE-2023-21768-AFD-for-WinSock-EoP-exploit](https://github.com/zoemurmure/CVE-2023-21768-AFD-for-WinSock-EoP-exploit) :  ![starts](https://img.shields.io/github/stars/zoemurmure/CVE-2023-21768-AFD-for-WinSock-EoP-exploit.svg) ![forks](https://img.shields.io/github/forks/zoemurmure/CVE-2023-21768-AFD-for-WinSock-EoP-exploit.svg)

- [https://github.com/xboxoneresearch/CVE-2023-21768-dotnet](https://github.com/xboxoneresearch/CVE-2023-21768-dotnet) :  ![starts](https://img.shields.io/github/stars/xboxoneresearch/CVE-2023-21768-dotnet.svg) ![forks](https://img.shields.io/github/forks/xboxoneresearch/CVE-2023-21768-dotnet.svg)

- [https://github.com/HKxiaoli/Windows_AFD_LPE_CVE-2023-21768](https://github.com/HKxiaoli/Windows_AFD_LPE_CVE-2023-21768) :  ![starts](https://img.shields.io/github/stars/HKxiaoli/Windows_AFD_LPE_CVE-2023-21768.svg) ![forks](https://img.shields.io/github/forks/HKxiaoli/Windows_AFD_LPE_CVE-2023-21768.svg)

- [https://github.com/h1bAna/CVE-2023-21768](https://github.com/h1bAna/CVE-2023-21768) :  ![starts](https://img.shields.io/github/stars/h1bAna/CVE-2023-21768.svg) ![forks](https://img.shields.io/github/forks/h1bAna/CVE-2023-21768.svg)

- [https://github.com/IlanDudnik/CVE-2023-21768](https://github.com/IlanDudnik/CVE-2023-21768) :  ![starts](https://img.shields.io/github/stars/IlanDudnik/CVE-2023-21768.svg) ![forks](https://img.shields.io/github/forks/IlanDudnik/CVE-2023-21768.svg)

- [https://github.com/Rosayxy/Recreate-cve-2023-21768](https://github.com/Rosayxy/Recreate-cve-2023-21768) :  ![starts](https://img.shields.io/github/stars/Rosayxy/Recreate-cve-2023-21768.svg) ![forks](https://img.shields.io/github/forks/Rosayxy/Recreate-cve-2023-21768.svg)

- [https://github.com/ldrx30/CVE-2023-21768](https://github.com/ldrx30/CVE-2023-21768) :  ![starts](https://img.shields.io/github/stars/ldrx30/CVE-2023-21768.svg) ![forks](https://img.shields.io/github/forks/ldrx30/CVE-2023-21768.svg)

## CVE-2023-21766
 Windows Overlay Filter Information Disclosure Vulnerability



- [https://github.com/Y3A/cve-2023-21766](https://github.com/Y3A/cve-2023-21766) :  ![starts](https://img.shields.io/github/stars/Y3A/cve-2023-21766.svg) ![forks](https://img.shields.io/github/forks/Y3A/cve-2023-21766.svg)

## CVE-2023-21752
 Windows Backup Service Elevation of Privilege Vulnerability



- [https://github.com/Wh04m1001/CVE-2023-21752](https://github.com/Wh04m1001/CVE-2023-21752) :  ![starts](https://img.shields.io/github/stars/Wh04m1001/CVE-2023-21752.svg) ![forks](https://img.shields.io/github/forks/Wh04m1001/CVE-2023-21752.svg)

- [https://github.com/yosef0x01/CVE-2023-21752](https://github.com/yosef0x01/CVE-2023-21752) :  ![starts](https://img.shields.io/github/stars/yosef0x01/CVE-2023-21752.svg) ![forks](https://img.shields.io/github/forks/yosef0x01/CVE-2023-21752.svg)

## CVE-2023-21746
 Windows NTLM Elevation of Privilege Vulnerability



- [https://github.com/Muhammad-Ali007/LocalPotato_CVE-2023-21746](https://github.com/Muhammad-Ali007/LocalPotato_CVE-2023-21746) :  ![starts](https://img.shields.io/github/stars/Muhammad-Ali007/LocalPotato_CVE-2023-21746.svg) ![forks](https://img.shields.io/github/forks/Muhammad-Ali007/LocalPotato_CVE-2023-21746.svg)

## CVE-2023-21742
 Microsoft SharePoint Server Remote Code Execution Vulnerability



- [https://github.com/ohnonoyesyes/CVE-2023-21742](https://github.com/ohnonoyesyes/CVE-2023-21742) :  ![starts](https://img.shields.io/github/stars/ohnonoyesyes/CVE-2023-21742.svg) ![forks](https://img.shields.io/github/forks/ohnonoyesyes/CVE-2023-21742.svg)

## CVE-2023-21739
 Windows Bluetooth Driver Elevation of Privilege Vulnerability



- [https://github.com/gmh5225/CVE-2023-21739](https://github.com/gmh5225/CVE-2023-21739) :  ![starts](https://img.shields.io/github/stars/gmh5225/CVE-2023-21739.svg) ![forks](https://img.shields.io/github/forks/gmh5225/CVE-2023-21739.svg)

## CVE-2023-21716
 Microsoft Word Remote Code Execution Vulnerability



- [https://github.com/gyaansastra/CVE-2023-21716](https://github.com/gyaansastra/CVE-2023-21716) :  ![starts](https://img.shields.io/github/stars/gyaansastra/CVE-2023-21716.svg) ![forks](https://img.shields.io/github/forks/gyaansastra/CVE-2023-21716.svg)

- [https://github.com/Xnuvers007/CVE-2023-21716](https://github.com/Xnuvers007/CVE-2023-21716) :  ![starts](https://img.shields.io/github/stars/Xnuvers007/CVE-2023-21716.svg) ![forks](https://img.shields.io/github/forks/Xnuvers007/CVE-2023-21716.svg)

- [https://github.com/JMousqueton/CVE-2023-21716](https://github.com/JMousqueton/CVE-2023-21716) :  ![starts](https://img.shields.io/github/stars/JMousqueton/CVE-2023-21716.svg) ![forks](https://img.shields.io/github/forks/JMousqueton/CVE-2023-21716.svg)

- [https://github.com/hv0l/CVE-2023-21716_exploit](https://github.com/hv0l/CVE-2023-21716_exploit) :  ![starts](https://img.shields.io/github/stars/hv0l/CVE-2023-21716_exploit.svg) ![forks](https://img.shields.io/github/forks/hv0l/CVE-2023-21716_exploit.svg)

- [https://github.com/FeatherStark/CVE-2023-21716](https://github.com/FeatherStark/CVE-2023-21716) :  ![starts](https://img.shields.io/github/stars/FeatherStark/CVE-2023-21716.svg) ![forks](https://img.shields.io/github/forks/FeatherStark/CVE-2023-21716.svg)

- [https://github.com/maldev866/WordExp_CVE_2023_21716](https://github.com/maldev866/WordExp_CVE_2023_21716) :  ![starts](https://img.shields.io/github/stars/maldev866/WordExp_CVE_2023_21716.svg) ![forks](https://img.shields.io/github/forks/maldev866/WordExp_CVE_2023_21716.svg)

- [https://github.com/MojithaR/CVE-2023-21716-EXPLOIT.py](https://github.com/MojithaR/CVE-2023-21716-EXPLOIT.py) :  ![starts](https://img.shields.io/github/stars/MojithaR/CVE-2023-21716-EXPLOIT.py.svg) ![forks](https://img.shields.io/github/forks/MojithaR/CVE-2023-21716-EXPLOIT.py.svg)

- [https://github.com/Lord-of-the-IoT/CVE-2023-21716](https://github.com/Lord-of-the-IoT/CVE-2023-21716) :  ![starts](https://img.shields.io/github/stars/Lord-of-the-IoT/CVE-2023-21716.svg) ![forks](https://img.shields.io/github/forks/Lord-of-the-IoT/CVE-2023-21716.svg)

- [https://github.com/P4x1s/CVE-2023-21716-POC](https://github.com/P4x1s/CVE-2023-21716-POC) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2023-21716-POC.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2023-21716-POC.svg)

- [https://github.com/mikesxrs/CVE-2023-21716_YARA_Results](https://github.com/mikesxrs/CVE-2023-21716_YARA_Results) :  ![starts](https://img.shields.io/github/stars/mikesxrs/CVE-2023-21716_YARA_Results.svg) ![forks](https://img.shields.io/github/forks/mikesxrs/CVE-2023-21716_YARA_Results.svg)

## CVE-2023-21707
 Microsoft Exchange Server Remote Code Execution Vulnerability



- [https://github.com/N1k0la-T/CVE-2023-21707](https://github.com/N1k0la-T/CVE-2023-21707) :  ![starts](https://img.shields.io/github/stars/N1k0la-T/CVE-2023-21707.svg) ![forks](https://img.shields.io/github/forks/N1k0la-T/CVE-2023-21707.svg)

## CVE-2023-21674
 Windows Advanced Local Procedure Call (ALPC) Elevation of Privilege Vulnerability



- [https://github.com/hd3s5aa/CVE-2023-21674](https://github.com/hd3s5aa/CVE-2023-21674) :  ![starts](https://img.shields.io/github/stars/hd3s5aa/CVE-2023-21674.svg) ![forks](https://img.shields.io/github/forks/hd3s5aa/CVE-2023-21674.svg)

## CVE-2023-21608
 Adobe Acrobat Reader versions 22.003.20282 (and earlier), 22.003.20281 (and earlier) and 20.005.30418 (and earlier) are affected by a Use After Free vulnerability that could result in arbitrary code execution in the context of the current user. Exploitation of this issue requires user interaction in that a victim must open a malicious file.



- [https://github.com/hacksysteam/CVE-2023-21608](https://github.com/hacksysteam/CVE-2023-21608) :  ![starts](https://img.shields.io/github/stars/hacksysteam/CVE-2023-21608.svg) ![forks](https://img.shields.io/github/forks/hacksysteam/CVE-2023-21608.svg)

- [https://github.com/Malwareman007/CVE-2023-21608](https://github.com/Malwareman007/CVE-2023-21608) :  ![starts](https://img.shields.io/github/stars/Malwareman007/CVE-2023-21608.svg) ![forks](https://img.shields.io/github/forks/Malwareman007/CVE-2023-21608.svg)

## CVE-2023-21563
 BitLocker Security Feature Bypass Vulnerability



- [https://github.com/Wack0/bitlocker-attacks](https://github.com/Wack0/bitlocker-attacks) :  ![starts](https://img.shields.io/github/stars/Wack0/bitlocker-attacks.svg) ![forks](https://img.shields.io/github/forks/Wack0/bitlocker-attacks.svg)

- [https://github.com/andigandhi/bitpixie](https://github.com/andigandhi/bitpixie) :  ![starts](https://img.shields.io/github/stars/andigandhi/bitpixie.svg) ![forks](https://img.shields.io/github/forks/andigandhi/bitpixie.svg)

## CVE-2023-21560
 Windows Boot Manager Security Feature Bypass Vulnerability



- [https://github.com/Wack0/dubiousdisk](https://github.com/Wack0/dubiousdisk) :  ![starts](https://img.shields.io/github/stars/Wack0/dubiousdisk.svg) ![forks](https://img.shields.io/github/forks/Wack0/dubiousdisk.svg)

## CVE-2023-21554
 Microsoft Message Queuing (MSMQ) Remote Code Execution Vulnerability



- [https://github.com/zoemurmure/CVE-2023-21554-PoC](https://github.com/zoemurmure/CVE-2023-21554-PoC) :  ![starts](https://img.shields.io/github/stars/zoemurmure/CVE-2023-21554-PoC.svg) ![forks](https://img.shields.io/github/forks/zoemurmure/CVE-2023-21554-PoC.svg)

- [https://github.com/3tternp/CVE-2023-21554](https://github.com/3tternp/CVE-2023-21554) :  ![starts](https://img.shields.io/github/stars/3tternp/CVE-2023-21554.svg) ![forks](https://img.shields.io/github/forks/3tternp/CVE-2023-21554.svg)

- [https://github.com/Rahul-Thakur7/CVE-2023-21554](https://github.com/Rahul-Thakur7/CVE-2023-21554) :  ![starts](https://img.shields.io/github/stars/Rahul-Thakur7/CVE-2023-21554.svg) ![forks](https://img.shields.io/github/forks/Rahul-Thakur7/CVE-2023-21554.svg)

## CVE-2023-21537
 Microsoft Message Queuing (MSMQ) Elevation of Privilege Vulnerability



- [https://github.com/stevenjoezhang/CVE-2023-21537](https://github.com/stevenjoezhang/CVE-2023-21537) :  ![starts](https://img.shields.io/github/stars/stevenjoezhang/CVE-2023-21537.svg) ![forks](https://img.shields.io/github/forks/stevenjoezhang/CVE-2023-21537.svg)

## CVE-2023-21288
 In visitUris of Notification.java, there is a possible way to reveal images across users due to a missing permission check. This could lead to local information disclosure with User execution privileges needed. User interaction is not needed for exploitation.





- [https://github.com/Trinadh465/platform_frameworks_base_CVE-2023-21288](https://github.com/Trinadh465/platform_frameworks_base_CVE-2023-21288) :  ![starts](https://img.shields.io/github/stars/Trinadh465/platform_frameworks_base_CVE-2023-21288.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/platform_frameworks_base_CVE-2023-21288.svg)

## CVE-2023-21286
 In visitUris of RemoteViews.java, there is a possible way to reveal images across users due to a missing permission check. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.





- [https://github.com/Trinadh465/platform_frameworks_base_CVE-2023-21286](https://github.com/Trinadh465/platform_frameworks_base_CVE-2023-21286) :  ![starts](https://img.shields.io/github/stars/Trinadh465/platform_frameworks_base_CVE-2023-21286.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/platform_frameworks_base_CVE-2023-21286.svg)

## CVE-2023-21285
 In setMetadata of MediaSessionRecord.java, there is a possible way to view another user's images due to a confused deputy. This could lead to local information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.





- [https://github.com/uthrasri/framework_base_CVE-2023-21285_NoPatch](https://github.com/uthrasri/framework_base_CVE-2023-21285_NoPatch) :  ![starts](https://img.shields.io/github/stars/uthrasri/framework_base_CVE-2023-21285_NoPatch.svg) ![forks](https://img.shields.io/github/forks/uthrasri/framework_base_CVE-2023-21285_NoPatch.svg)

## CVE-2023-21284
 In multiple functions of DevicePolicyManager.java, there is a possible way to prevent enabling the Find my Device feature due to improper input validation. This could lead to local denial of service with User execution privileges needed. User interaction is not needed for exploitation.





- [https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21284](https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21284) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21284.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21284.svg)

## CVE-2023-21282
 In TRANSPOSER_SETTINGS of lpp_tran.h, there is a possible out of bounds write due to an incorrect bounds check. This could lead to remote code execution with no additional execution privileges needed. User interaction is needed for exploitation.





- [https://github.com/Trinadh465/external_aac_AOSP10_r33_CVE-2023-21282](https://github.com/Trinadh465/external_aac_AOSP10_r33_CVE-2023-21282) :  ![starts](https://img.shields.io/github/stars/Trinadh465/external_aac_AOSP10_r33_CVE-2023-21282.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/external_aac_AOSP10_r33_CVE-2023-21282.svg)

- [https://github.com/Trinadh465/external_aac_android-4.2.2_r1_CVE-2023-21282](https://github.com/Trinadh465/external_aac_android-4.2.2_r1_CVE-2023-21282) :  ![starts](https://img.shields.io/github/stars/Trinadh465/external_aac_android-4.2.2_r1_CVE-2023-21282.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/external_aac_android-4.2.2_r1_CVE-2023-21282.svg)

## CVE-2023-21281
 In multiple functions of KeyguardViewMediator.java, there is a possible failure to lock after screen timeout due to a logic error in the code. This could lead to local escalation of privilege across users with no additional execution privileges needed. User interaction is not needed for exploitation.





- [https://github.com/Trinadh465/platform_frameworks_base_CVE-2023-21281](https://github.com/Trinadh465/platform_frameworks_base_CVE-2023-21281) :  ![starts](https://img.shields.io/github/stars/Trinadh465/platform_frameworks_base_CVE-2023-21281.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/platform_frameworks_base_CVE-2023-21281.svg)

## CVE-2023-21275
 In decideCancelProvisioningDialog of AdminIntegratedFlowPrepareActivity.java, there is a possible way to bypass factory reset protections due to a logic error in the code. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.





- [https://github.com/Trinadh465/packages_apps_ManagedProvisioning_AOSP10_r33_CVE-2023-21275](https://github.com/Trinadh465/packages_apps_ManagedProvisioning_AOSP10_r33_CVE-2023-21275) :  ![starts](https://img.shields.io/github/stars/Trinadh465/packages_apps_ManagedProvisioning_AOSP10_r33_CVE-2023-21275.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/packages_apps_ManagedProvisioning_AOSP10_r33_CVE-2023-21275.svg)

## CVE-2023-21272
 In readFrom of Uri.java, there is a possible bad URI permission grant due to improper input validation. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.





- [https://github.com/pazhanivel07/platform_frameworks_base_AOSP_10_r33_CVE-2023-21272](https://github.com/pazhanivel07/platform_frameworks_base_AOSP_10_r33_CVE-2023-21272) :  ![starts](https://img.shields.io/github/stars/pazhanivel07/platform_frameworks_base_AOSP_10_r33_CVE-2023-21272.svg) ![forks](https://img.shields.io/github/forks/pazhanivel07/platform_frameworks_base_AOSP_10_r33_CVE-2023-21272.svg)

- [https://github.com/Trinadh465/frameworks_base_AOSP-4.2.2_r1_CVE-2023-21272](https://github.com/Trinadh465/frameworks_base_AOSP-4.2.2_r1_CVE-2023-21272) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_AOSP-4.2.2_r1_CVE-2023-21272.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_AOSP-4.2.2_r1_CVE-2023-21272.svg)

## CVE-2023-21251
 In onCreate of ConfirmDialog.java, there is a possible way to connect to VNP bypassing user's consent due to improper input validation. This could lead to local escalation of privilege with User execution privileges needed. User interaction is needed for exploitation.





- [https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21251](https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21251) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21251.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21251.svg)

## CVE-2023-21246
 In ShortcutInfo of ShortcutInfo.java, there is a possible way for an app to retain notification listening access due to an uncaught exception. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.





- [https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21246](https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21246) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21246.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21246.svg)

## CVE-2023-21238
 In visitUris of RemoteViews.java, there is a possible leak of images between users due to a confused deputy. This could lead to local information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.





- [https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21238](https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21238) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21238.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21238.svg)

## CVE-2023-21118
 In unflattenString8 of Sensor.cpp, there is a possible out of bounds read due to a heap buffer overflow. This could lead to local information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-11 Android-12 Android-12L Android-13Android ID: A-269014004



- [https://github.com/Satheesh575555/frameworks_native_AOSP10_r33_CVE-2023-21118](https://github.com/Satheesh575555/frameworks_native_AOSP10_r33_CVE-2023-21118) :  ![starts](https://img.shields.io/github/stars/Satheesh575555/frameworks_native_AOSP10_r33_CVE-2023-21118.svg) ![forks](https://img.shields.io/github/forks/Satheesh575555/frameworks_native_AOSP10_r33_CVE-2023-21118.svg)

- [https://github.com/Trinadh465/frameworks_native_AOSP-10_r33_CVE-2023-21118](https://github.com/Trinadh465/frameworks_native_AOSP-10_r33_CVE-2023-21118) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_native_AOSP-10_r33_CVE-2023-21118.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_native_AOSP-10_r33_CVE-2023-21118.svg)

## CVE-2023-21109
 In multiple places of AccessibilityService, there is a possible way to hide the app from the user due to a logic error in the code. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-11 Android-12 Android-12L Android-13Android ID: A-261589597



- [https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21109](https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21109) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21109.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21109.svg)

- [https://github.com/Trinadh465/frameworks_base_AOSP10_CVE-2023-21109r33_](https://github.com/Trinadh465/frameworks_base_AOSP10_CVE-2023-21109r33_) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_AOSP10_CVE-2023-21109r33_.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_AOSP10_CVE-2023-21109r33_.svg)

## CVE-2023-21097
 In toUriInner of Intent.java, there is a possible way to launch an arbitrary activity due to a confused deputy. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-11 Android-12 Android-12L Android-13Android ID: A-261858325



- [https://github.com/uthrasri/frameworks_base_AOSP10_r33_CVE-2023-21097](https://github.com/uthrasri/frameworks_base_AOSP10_r33_CVE-2023-21097) :  ![starts](https://img.shields.io/github/stars/uthrasri/frameworks_base_AOSP10_r33_CVE-2023-21097.svg) ![forks](https://img.shields.io/github/forks/uthrasri/frameworks_base_AOSP10_r33_CVE-2023-21097.svg)

- [https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21097](https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21097) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21097.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-21097.svg)

## CVE-2023-21094
 In sanitize of LayerState.cpp, there is a possible way to take over the screen display and swap the display content due to a missing permission check. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-11 Android-12 Android-12L Android-13Android ID: A-248031255



- [https://github.com/Trinadh465/frameworks_native_AOSP-10_r33_CVE-2023-21094](https://github.com/Trinadh465/frameworks_native_AOSP-10_r33_CVE-2023-21094) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_native_AOSP-10_r33_CVE-2023-21094.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_native_AOSP-10_r33_CVE-2023-21094.svg)

## CVE-2023-21086
 In isToggleable of SecureNfcEnabler.java and SecureNfcPreferenceController.java, there is a possible way to enable NFC from a secondary account due to a permissions bypass. This could lead to local escalation of privilege from the Guest account with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-11 Android-12 Android-12L Android-13Android ID: A-238298970



- [https://github.com/Trinadh465/packages_apps_Settings_CVE-2023-21086](https://github.com/Trinadh465/packages_apps_Settings_CVE-2023-21086) :  ![starts](https://img.shields.io/github/stars/Trinadh465/packages_apps_Settings_CVE-2023-21086.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/packages_apps_Settings_CVE-2023-21086.svg)

## CVE-2023-21036
 In BitmapExport.java, there is a possible failure to truncate images due to a logic error in the code.Product: AndroidVersions: Android kernelAndroid ID: A-264261868References: N/A



- [https://github.com/frankthetank-music/Acropalypse-Multi-Tool](https://github.com/frankthetank-music/Acropalypse-Multi-Tool) :  ![starts](https://img.shields.io/github/stars/frankthetank-music/Acropalypse-Multi-Tool.svg) ![forks](https://img.shields.io/github/forks/frankthetank-music/Acropalypse-Multi-Tool.svg)

- [https://github.com/infobyte/CVE-2023-21036](https://github.com/infobyte/CVE-2023-21036) :  ![starts](https://img.shields.io/github/stars/infobyte/CVE-2023-21036.svg) ![forks](https://img.shields.io/github/forks/infobyte/CVE-2023-21036.svg)

- [https://github.com/qixils/AntiCropalypse](https://github.com/qixils/AntiCropalypse) :  ![starts](https://img.shields.io/github/stars/qixils/AntiCropalypse.svg) ![forks](https://img.shields.io/github/forks/qixils/AntiCropalypse.svg)

- [https://github.com/lordofpipes/acropadetect](https://github.com/lordofpipes/acropadetect) :  ![starts](https://img.shields.io/github/stars/lordofpipes/acropadetect.svg) ![forks](https://img.shields.io/github/forks/lordofpipes/acropadetect.svg)

- [https://github.com/notaSWE/gocropalypse](https://github.com/notaSWE/gocropalypse) :  ![starts](https://img.shields.io/github/stars/notaSWE/gocropalypse.svg) ![forks](https://img.shields.io/github/forks/notaSWE/gocropalypse.svg)

- [https://github.com/L1-0/codestuff](https://github.com/L1-0/codestuff) :  ![starts](https://img.shields.io/github/stars/L1-0/codestuff.svg) ![forks](https://img.shields.io/github/forks/L1-0/codestuff.svg)

## CVE-2023-20963
 In WorkSource, there is a possible parcel mismatch. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-11 Android-12 Android-12L Android-13Android ID: A-220302519



- [https://github.com/pwnipc/BadParcel](https://github.com/pwnipc/BadParcel) :  ![starts](https://img.shields.io/github/stars/pwnipc/BadParcel.svg) ![forks](https://img.shields.io/github/forks/pwnipc/BadParcel.svg)

- [https://github.com/Ailenchick/CVE-2023-20963](https://github.com/Ailenchick/CVE-2023-20963) :  ![starts](https://img.shields.io/github/stars/Ailenchick/CVE-2023-20963.svg) ![forks](https://img.shields.io/github/forks/Ailenchick/CVE-2023-20963.svg)

- [https://github.com/black7024/BadParcel](https://github.com/black7024/BadParcel) :  ![starts](https://img.shields.io/github/stars/black7024/BadParcel.svg) ![forks](https://img.shields.io/github/forks/black7024/BadParcel.svg)

- [https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20963](https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20963) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20963.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20963.svg)

## CVE-2023-20955
 In onPrepareOptionsMenu of AppInfoDashboardFragment.java, there is a possible way to bypass admin restrictions and uninstall applications for all users due to a missing permission check. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-11 Android-12 Android-12L Android-13Android ID: A-258653813



- [https://github.com/Trinadh465/packages_apps_Settings_AOSP10_r33_CVE-2023-20955](https://github.com/Trinadh465/packages_apps_Settings_AOSP10_r33_CVE-2023-20955) :  ![starts](https://img.shields.io/github/stars/Trinadh465/packages_apps_Settings_AOSP10_r33_CVE-2023-20955.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/packages_apps_Settings_AOSP10_r33_CVE-2023-20955.svg)

## CVE-2023-20945
 In phNciNfc_MfCreateXchgDataHdr of phNxpExtns_MifareStd.cpp, there is a possible out of bounds write due to a missing bounds check. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-10Android ID: A-246932269



- [https://github.com/Ailenchick/CVE-2023-20945](https://github.com/Ailenchick/CVE-2023-20945) :  ![starts](https://img.shields.io/github/stars/Ailenchick/CVE-2023-20945.svg) ![forks](https://img.shields.io/github/forks/Ailenchick/CVE-2023-20945.svg)

## CVE-2023-20944
 In run of ChooseTypeAndAccountActivity.java, there is a possible escalation of privilege due to unsafe deserialization. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-10 Android-11 Android-12 Android-12L Android-13Android ID: A-244154558



- [https://github.com/Trinadh465/frameworks_base_CVE-2023-20944](https://github.com/Trinadh465/frameworks_base_CVE-2023-20944) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_CVE-2023-20944.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_CVE-2023-20944.svg)

## CVE-2023-20943
 In clearApplicationUserData of ActivityManagerService.java, there is a possible way to remove system files due to a path traversal error. This could lead to local escalation of privilege with User execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-10 Android-11 Android-12 Android-12L Android-13Android ID: A-240267890



- [https://github.com/Trinadh465/frameworks_base_CVE-2023-20943](https://github.com/Trinadh465/frameworks_base_CVE-2023-20943) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_CVE-2023-20943.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_CVE-2023-20943.svg)

## CVE-2023-20933
 In several functions of MediaCodec.cpp, there is a possible way to corrupt memory due to a use after free. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-10 Android-11 Android-12 Android-12L Android-13Android ID: A-245860753



- [https://github.com/Trinadh465/frameworks_av_CVE-2023-20933](https://github.com/Trinadh465/frameworks_av_CVE-2023-20933) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_av_CVE-2023-20933.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_av_CVE-2023-20933.svg)

## CVE-2023-20921
 In onPackageRemoved of AccessibilityManagerService.java, there is a possibility to automatically grant accessibility services due to a logic error in the code. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is needed for exploitation.Product: AndroidVersions: Android-10 Android-11 Android-12 Android-12L Android-13Android ID: A-243378132



- [https://github.com/Trinadh465/frameworks_base_android-6.0.1_r22_CVE-2023-20921](https://github.com/Trinadh465/frameworks_base_android-6.0.1_r22_CVE-2023-20921) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_android-6.0.1_r22_CVE-2023-20921.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_android-6.0.1_r22_CVE-2023-20921.svg)

## CVE-2023-20918
 In getPendingIntentLaunchFlags of ActivityOptions.java, there is a possible elevation of privilege due to a confused deputy with no additional execution privileges needed. User interaction is not needed for exploitation.





- [https://github.com/Trinadh465/platform_frameworks_base_CVE-2023-20918](https://github.com/Trinadh465/platform_frameworks_base_CVE-2023-20918) :  ![starts](https://img.shields.io/github/stars/Trinadh465/platform_frameworks_base_CVE-2023-20918.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/platform_frameworks_base_CVE-2023-20918.svg)

- [https://github.com/pazhanivel07/platform_frameworks_base_AOSP_10_r33_CVE-2023-20918](https://github.com/pazhanivel07/platform_frameworks_base_AOSP_10_r33_CVE-2023-20918) :  ![starts](https://img.shields.io/github/stars/pazhanivel07/platform_frameworks_base_AOSP_10_r33_CVE-2023-20918.svg) ![forks](https://img.shields.io/github/forks/pazhanivel07/platform_frameworks_base_AOSP_10_r33_CVE-2023-20918.svg)

## CVE-2023-20911
 In addPermission of PermissionManagerServiceImpl.java , there is a possible failure to persist permission settings due to resource exhaustion. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-11 Android-12 Android-12L Android-13Android ID: A-242537498



- [https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20911](https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20911) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20911.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20911.svg)

## CVE-2023-20909
 In multiple functions of RunningTasks.java, there is a possible privilege escalation due to a missing privilege check. This could lead to local information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-11 Android-12 Android-12L Android-13Android ID: A-243130512



- [https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20909](https://github.com/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20909) :  ![starts](https://img.shields.io/github/stars/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20909.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/frameworks_base_AOSP10_r33_CVE-2023-20909.svg)

- [https://github.com/Trinadh465/platform_frameworks_base_AOSP10_r33_CVE-2023-20909](https://github.com/Trinadh465/platform_frameworks_base_AOSP10_r33_CVE-2023-20909) :  ![starts](https://img.shields.io/github/stars/Trinadh465/platform_frameworks_base_AOSP10_r33_CVE-2023-20909.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/platform_frameworks_base_AOSP10_r33_CVE-2023-20909.svg)

## CVE-2023-20904
 In getTrampolineIntent of SettingsActivity.java, there is a possible launch of arbitrary activity due to an Intent mismatch in the code. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.Product: AndroidVersions: Android-12L Android-13Android ID: A-246300272



- [https://github.com/FishMan132/CVE-2023-20904](https://github.com/FishMan132/CVE-2023-20904) :  ![starts](https://img.shields.io/github/stars/FishMan132/CVE-2023-20904.svg) ![forks](https://img.shields.io/github/forks/FishMan132/CVE-2023-20904.svg)

## CVE-2023-20887
 Aria Operations for Networks contains a command injection vulnerability. A malicious actor with network access to VMware Aria Operations for Networks may be able to perform a command injection attack resulting in remote code execution.



- [https://github.com/sinsinology/CVE-2023-20887](https://github.com/sinsinology/CVE-2023-20887) :  ![starts](https://img.shields.io/github/stars/sinsinology/CVE-2023-20887.svg) ![forks](https://img.shields.io/github/forks/sinsinology/CVE-2023-20887.svg)

- [https://github.com/Malwareman007/CVE-2023-20887](https://github.com/Malwareman007/CVE-2023-20887) :  ![starts](https://img.shields.io/github/stars/Malwareman007/CVE-2023-20887.svg) ![forks](https://img.shields.io/github/forks/Malwareman007/CVE-2023-20887.svg)

- [https://github.com/miko550/CVE-2023-20887](https://github.com/miko550/CVE-2023-20887) :  ![starts](https://img.shields.io/github/stars/miko550/CVE-2023-20887.svg) ![forks](https://img.shields.io/github/forks/miko550/CVE-2023-20887.svg)

## CVE-2023-20872
 VMware Workstation and Fusion contain an out-of-bounds read/write vulnerability in SCSI CD/DVD device emulation.



- [https://github.com/ze0r/vmware-escape-CVE-2023-20872-poc](https://github.com/ze0r/vmware-escape-CVE-2023-20872-poc) :  ![starts](https://img.shields.io/github/stars/ze0r/vmware-escape-CVE-2023-20872-poc.svg) ![forks](https://img.shields.io/github/forks/ze0r/vmware-escape-CVE-2023-20872-poc.svg)

## CVE-2023-20860
 Spring Framework running version 6.0.0 - 6.0.6 or 5.3.0 - 5.3.25 using "**" as a pattern in Spring Security configuration with the mvcRequestMatcher creates a mismatch in pattern matching between Spring Security and Spring MVC, and the potential for a security bypass.



- [https://github.com/limo520/CVE-2023-20860](https://github.com/limo520/CVE-2023-20860) :  ![starts](https://img.shields.io/github/stars/limo520/CVE-2023-20860.svg) ![forks](https://img.shields.io/github/forks/limo520/CVE-2023-20860.svg)

## CVE-2023-20598
 


An improper privilege management in the AMD Radeon™ Graphics driver may allow an authenticated attacker to craft an IOCTL request to gain I/O control over arbitrary hardware ports or physical addresses resulting in a potential arbitrary code execution.







- [https://github.com/H4rk3nz0/CVE-2023-20598-PDFWKRNL](https://github.com/H4rk3nz0/CVE-2023-20598-PDFWKRNL) :  ![starts](https://img.shields.io/github/stars/H4rk3nz0/CVE-2023-20598-PDFWKRNL.svg) ![forks](https://img.shields.io/github/forks/H4rk3nz0/CVE-2023-20598-PDFWKRNL.svg)

## CVE-2023-20593
 An issue in “Zen 2” CPUs, under specific microarchitectural circumstances, may allow an attacker to potentially access sensitive information.



- [https://github.com/sbaresearch/stop-zenbleed-win](https://github.com/sbaresearch/stop-zenbleed-win) :  ![starts](https://img.shields.io/github/stars/sbaresearch/stop-zenbleed-win.svg) ![forks](https://img.shields.io/github/forks/sbaresearch/stop-zenbleed-win.svg)

## CVE-2023-20573
 A privileged attacker
can prevent delivery of debug exceptions to SEV-SNP guests potentially
resulting in guests not receiving expected debug information.







- [https://github.com/Freax13/cve-2023-20573-poc](https://github.com/Freax13/cve-2023-20573-poc) :  ![starts](https://img.shields.io/github/stars/Freax13/cve-2023-20573-poc.svg) ![forks](https://img.shields.io/github/forks/Freax13/cve-2023-20573-poc.svg)

## CVE-2023-20562
 


Insufficient validation in the IOCTL (Input Output Control) input buffer in AMD uProf may allow an authenticated user to load an unsigned driver potentially leading to arbitrary kernel execution.





















- [https://github.com/zeze-zeze/HITCON-2023-Demo-CVE-2023-20562](https://github.com/zeze-zeze/HITCON-2023-Demo-CVE-2023-20562) :  ![starts](https://img.shields.io/github/stars/zeze-zeze/HITCON-2023-Demo-CVE-2023-20562.svg) ![forks](https://img.shields.io/github/forks/zeze-zeze/HITCON-2023-Demo-CVE-2023-20562.svg)

- [https://github.com/passwa11/HITCON-2023-Demo-CVE-2023-20562](https://github.com/passwa11/HITCON-2023-Demo-CVE-2023-20562) :  ![starts](https://img.shields.io/github/stars/passwa11/HITCON-2023-Demo-CVE-2023-20562.svg) ![forks](https://img.shields.io/github/forks/passwa11/HITCON-2023-Demo-CVE-2023-20562.svg)

## CVE-2023-20273
 A vulnerability in the web UI feature of Cisco IOS XE Software could allow an authenticated, remote attacker to inject commands with the privileges of root. This vulnerability is due to insufficient input validation. An attacker could exploit this vulnerability by sending crafted input to the web UI. A successful exploit could allow the attacker to inject commands to the underlying operating system with root privileges.



- [https://github.com/fox-it/cisco-ios-xe-implant-detection](https://github.com/fox-it/cisco-ios-xe-implant-detection) :  ![starts](https://img.shields.io/github/stars/fox-it/cisco-ios-xe-implant-detection.svg) ![forks](https://img.shields.io/github/forks/fox-it/cisco-ios-xe-implant-detection.svg)

- [https://github.com/Shadow0ps/CVE-2023-20198-Scanner](https://github.com/Shadow0ps/CVE-2023-20198-Scanner) :  ![starts](https://img.shields.io/github/stars/Shadow0ps/CVE-2023-20198-Scanner.svg) ![forks](https://img.shields.io/github/forks/Shadow0ps/CVE-2023-20198-Scanner.svg)

- [https://github.com/smokeintheshell/CVE-2023-20273](https://github.com/smokeintheshell/CVE-2023-20273) :  ![starts](https://img.shields.io/github/stars/smokeintheshell/CVE-2023-20273.svg) ![forks](https://img.shields.io/github/forks/smokeintheshell/CVE-2023-20273.svg)

## CVE-2023-20209
 A vulnerability in the web-based management interface of Cisco Expressway Series and Cisco TelePresence Video Communication Server (VCS) could allow an authenticated, remote attacker with read-write privileges on the application to perform a command injection attack that could result in remote code execution on an affected device.
 This vulnerability is due to insufficient validation of user-supplied input. An attacker could exploit this vulnerability by sending a crafted request to the web-based management interface of an affected device. A successful exploit could allow the attacker to establish a remote shell with root privileges.



- [https://github.com/peter5he1by/CVE-2023-20209](https://github.com/peter5he1by/CVE-2023-20209) :  ![starts](https://img.shields.io/github/stars/peter5he1by/CVE-2023-20209.svg) ![forks](https://img.shields.io/github/forks/peter5he1by/CVE-2023-20209.svg)

## CVE-2023-20198
 Cisco is providing an update for the ongoing investigation into observed exploitation of the web UI feature in Cisco IOS XE Software. We are updating the list of fixed releases and adding the Software Checker. Our investigation has determined that the actors exploited two previously unknown issues. The attacker first exploited CVE-2023-20198 to gain initial access and issued a privilege 15 command to create a local user and password combination. This allowed the user to log in with normal user access. The attacker then exploited another component of the web UI feature, leveraging the new local user to elevate privilege to root and write the implant to the file system. Cisco has assigned CVE-2023-20273 to this issue. CVE-2023-20198 has been assigned a CVSS Score of 10.0. CVE-2023-20273 has been assigned a CVSS Score of 7.2. Both of these CVEs are being tracked by CSCwh87343.



- [https://github.com/smokeintheshell/CVE-2023-20198](https://github.com/smokeintheshell/CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/smokeintheshell/CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/smokeintheshell/CVE-2023-20198.svg)

- [https://github.com/vulncheck-oss/cisco-ios-xe-implant-scanner](https://github.com/vulncheck-oss/cisco-ios-xe-implant-scanner) :  ![starts](https://img.shields.io/github/stars/vulncheck-oss/cisco-ios-xe-implant-scanner.svg) ![forks](https://img.shields.io/github/forks/vulncheck-oss/cisco-ios-xe-implant-scanner.svg)

- [https://github.com/W01fh4cker/CVE-2023-20198-RCE](https://github.com/W01fh4cker/CVE-2023-20198-RCE) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/CVE-2023-20198-RCE.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/CVE-2023-20198-RCE.svg)

- [https://github.com/fox-it/cisco-ios-xe-implant-detection](https://github.com/fox-it/cisco-ios-xe-implant-detection) :  ![starts](https://img.shields.io/github/stars/fox-it/cisco-ios-xe-implant-detection.svg) ![forks](https://img.shields.io/github/forks/fox-it/cisco-ios-xe-implant-detection.svg)

- [https://github.com/ZephrFish/CVE-2023-20198-Checker](https://github.com/ZephrFish/CVE-2023-20198-Checker) :  ![starts](https://img.shields.io/github/stars/ZephrFish/CVE-2023-20198-Checker.svg) ![forks](https://img.shields.io/github/forks/ZephrFish/CVE-2023-20198-Checker.svg)

- [https://github.com/Shadow0ps/CVE-2023-20198-Scanner](https://github.com/Shadow0ps/CVE-2023-20198-Scanner) :  ![starts](https://img.shields.io/github/stars/Shadow0ps/CVE-2023-20198-Scanner.svg) ![forks](https://img.shields.io/github/forks/Shadow0ps/CVE-2023-20198-Scanner.svg)

- [https://github.com/Atea-Redteam/CVE-2023-20198](https://github.com/Atea-Redteam/CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/Atea-Redteam/CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/Atea-Redteam/CVE-2023-20198.svg)

- [https://github.com/Tounsi007/CVE-2023-20198](https://github.com/Tounsi007/CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/Tounsi007/CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/Tounsi007/CVE-2023-20198.svg)

- [https://github.com/Pushkarup/CVE-2023-20198](https://github.com/Pushkarup/CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/Pushkarup/CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/Pushkarup/CVE-2023-20198.svg)

- [https://github.com/XiaomingX/cve-2023-20198-poc](https://github.com/XiaomingX/cve-2023-20198-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2023-20198-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2023-20198-poc.svg)

- [https://github.com/RevoltSecurities/CVE-2023-20198](https://github.com/RevoltSecurities/CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/RevoltSecurities/CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/RevoltSecurities/CVE-2023-20198.svg)

- [https://github.com/iveresk/cve-2023-20198](https://github.com/iveresk/cve-2023-20198) :  ![starts](https://img.shields.io/github/stars/iveresk/cve-2023-20198.svg) ![forks](https://img.shields.io/github/forks/iveresk/cve-2023-20198.svg)

- [https://github.com/sohaibeb/CVE-2023-20198](https://github.com/sohaibeb/CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/sohaibeb/CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/sohaibeb/CVE-2023-20198.svg)

- [https://github.com/Vulnmachines/Cisco_CVE-2023-20198](https://github.com/Vulnmachines/Cisco_CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/Vulnmachines/Cisco_CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/Vulnmachines/Cisco_CVE-2023-20198.svg)

- [https://github.com/G4sul1n/Cisco-IOS-XE-CVE-2023-20198](https://github.com/G4sul1n/Cisco-IOS-XE-CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/G4sul1n/Cisco-IOS-XE-CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/G4sul1n/Cisco-IOS-XE-CVE-2023-20198.svg)

- [https://github.com/alekos3/CVE_2023_20198_Detector](https://github.com/alekos3/CVE_2023_20198_Detector) :  ![starts](https://img.shields.io/github/stars/alekos3/CVE_2023_20198_Detector.svg) ![forks](https://img.shields.io/github/forks/alekos3/CVE_2023_20198_Detector.svg)

- [https://github.com/mr-r3b00t/CVE-2023-20198-IOS-XE-Scanner](https://github.com/mr-r3b00t/CVE-2023-20198-IOS-XE-Scanner) :  ![starts](https://img.shields.io/github/stars/mr-r3b00t/CVE-2023-20198-IOS-XE-Scanner.svg) ![forks](https://img.shields.io/github/forks/mr-r3b00t/CVE-2023-20198-IOS-XE-Scanner.svg)

- [https://github.com/securityphoenix/cisco-CVE-2023-20198-tester](https://github.com/securityphoenix/cisco-CVE-2023-20198-tester) :  ![starts](https://img.shields.io/github/stars/securityphoenix/cisco-CVE-2023-20198-tester.svg) ![forks](https://img.shields.io/github/forks/securityphoenix/cisco-CVE-2023-20198-tester.svg)

- [https://github.com/IceBreakerCode/CVE-2023-20198](https://github.com/IceBreakerCode/CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/IceBreakerCode/CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/IceBreakerCode/CVE-2023-20198.svg)

- [https://github.com/kacem-expereo/CVE-2023-20198](https://github.com/kacem-expereo/CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/kacem-expereo/CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/kacem-expereo/CVE-2023-20198.svg)

- [https://github.com/alekos3/CVE_2023_20198_Remediator](https://github.com/alekos3/CVE_2023_20198_Remediator) :  ![starts](https://img.shields.io/github/stars/alekos3/CVE_2023_20198_Remediator.svg) ![forks](https://img.shields.io/github/forks/alekos3/CVE_2023_20198_Remediator.svg)

- [https://github.com/emomeni/Simple-Ansible-for-CVE-2023-20198](https://github.com/emomeni/Simple-Ansible-for-CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/emomeni/Simple-Ansible-for-CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/emomeni/Simple-Ansible-for-CVE-2023-20198.svg)

- [https://github.com/ohlawd/CVE-2023-20198](https://github.com/ohlawd/CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/ohlawd/CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/ohlawd/CVE-2023-20198.svg)

- [https://github.com/JoyGhoshs/CVE-2023-20198](https://github.com/JoyGhoshs/CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/JoyGhoshs/CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/JoyGhoshs/CVE-2023-20198.svg)

- [https://github.com/reket99/Cisco_CVE-2023-20198](https://github.com/reket99/Cisco_CVE-2023-20198) :  ![starts](https://img.shields.io/github/stars/reket99/Cisco_CVE-2023-20198.svg) ![forks](https://img.shields.io/github/forks/reket99/Cisco_CVE-2023-20198.svg)

- [https://github.com/netbell/CVE-2023-20198-Fix](https://github.com/netbell/CVE-2023-20198-Fix) :  ![starts](https://img.shields.io/github/stars/netbell/CVE-2023-20198-Fix.svg) ![forks](https://img.shields.io/github/forks/netbell/CVE-2023-20198-Fix.svg)

- [https://github.com/raystr-atearedteam/CVE-2023-20198-checker](https://github.com/raystr-atearedteam/CVE-2023-20198-checker) :  ![starts](https://img.shields.io/github/stars/raystr-atearedteam/CVE-2023-20198-checker.svg) ![forks](https://img.shields.io/github/forks/raystr-atearedteam/CVE-2023-20198-checker.svg)

## CVE-2023-20178
 A vulnerability in the client update process of Cisco AnyConnect Secure Mobility Client Software for Windows and Cisco Secure Client Software for Windows could allow a low-privileged, authenticated, local attacker to elevate privileges to those of SYSTEM. The client update process is executed after a successful VPN connection is established.
 This vulnerability exists because improper permissions are assigned to a temporary directory that is created during the update process. An attacker could exploit this vulnerability by abusing a specific function of the Windows installer process. A successful exploit could allow the attacker to execute code with SYSTEM privileges.



- [https://github.com/Wh04m1001/CVE-2023-20178](https://github.com/Wh04m1001/CVE-2023-20178) :  ![starts](https://img.shields.io/github/stars/Wh04m1001/CVE-2023-20178.svg) ![forks](https://img.shields.io/github/forks/Wh04m1001/CVE-2023-20178.svg)

## CVE-2023-20126
 A vulnerability in the web-based management interface of Cisco SPA112 2-Port Phone Adapters could allow an unauthenticated, remote attacker to execute arbitrary code on an affected device. This vulnerability is due to a missing authentication process within the firmware upgrade function. An attacker could exploit this vulnerability by upgrading an affected device to a crafted version of firmware. A successful exploit could allow the attacker to execute arbitrary code on the affected device with full privileges. Cisco has not released firmware updates to address this vulnerability.



- [https://github.com/fullspectrumdev/RancidCrisco](https://github.com/fullspectrumdev/RancidCrisco) :  ![starts](https://img.shields.io/github/stars/fullspectrumdev/RancidCrisco.svg) ![forks](https://img.shields.io/github/forks/fullspectrumdev/RancidCrisco.svg)

## CVE-2023-20110
 A vulnerability in the web-based management interface of Cisco Smart Software Manager On-Prem (SSM On-Prem) could allow an authenticated, remote attacker to conduct SQL injection attacks on an affected system. This vulnerability exists because the web-based management interface inadequately validates user input. An attacker could exploit this vulnerability by authenticating to the application as a low-privileged user and sending crafted SQL queries to an affected system. A successful exploit could allow the attacker to read sensitive data on the underlying database.



- [https://github.com/redfr0g/CVE-2023-20110](https://github.com/redfr0g/CVE-2023-20110) :  ![starts](https://img.shields.io/github/stars/redfr0g/CVE-2023-20110.svg) ![forks](https://img.shields.io/github/forks/redfr0g/CVE-2023-20110.svg)

## CVE-2023-20073
 A vulnerability in the web-based management interface of Cisco RV340, RV340W, RV345, and RV345P Dual WAN Gigabit VPN Routers could allow an unauthenticated, remote attacker to upload arbitrary files to an affected device. This vulnerability is due to insufficient authorization enforcement mechanisms in the context of file uploads. An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected device. A successful exploit could allow the attacker to upload arbitrary files to the affected device.



- [https://github.com/RegularITCat/CVE-2023-20073](https://github.com/RegularITCat/CVE-2023-20073) :  ![starts](https://img.shields.io/github/stars/RegularITCat/CVE-2023-20073.svg) ![forks](https://img.shields.io/github/forks/RegularITCat/CVE-2023-20073.svg)

## CVE-2023-20052
 On Feb 15, 2023, the following vulnerability in the ClamAV scanning library was disclosed:
  A vulnerability in the DMG file parser of ClamAV versions 1.0.0 and earlier, 0.105.1 and earlier, and 0.103.7 and earlier could allow an unauthenticated, remote attacker to access sensitive information on an affected device.
  This vulnerability is due to enabling XML entity substitution that may result in XML external entity injection. An attacker could exploit this vulnerability by submitting a crafted DMG file to be scanned by ClamAV on an affected device. A successful exploit could allow the attacker to leak bytes from any file that may be read by the ClamAV scanning process.



- [https://github.com/nokn0wthing/CVE-2023-20052](https://github.com/nokn0wthing/CVE-2023-20052) :  ![starts](https://img.shields.io/github/stars/nokn0wthing/CVE-2023-20052.svg) ![forks](https://img.shields.io/github/forks/nokn0wthing/CVE-2023-20052.svg)

- [https://github.com/cY83rR0H1t/CVE-2023-20052](https://github.com/cY83rR0H1t/CVE-2023-20052) :  ![starts](https://img.shields.io/github/stars/cY83rR0H1t/CVE-2023-20052.svg) ![forks](https://img.shields.io/github/forks/cY83rR0H1t/CVE-2023-20052.svg)

## CVE-2023-20048
 A vulnerability in the web services interface of Cisco Firepower Management Center (FMC) Software could allow an authenticated, remote attacker to execute certain unauthorized configuration commands on a Firepower Threat Defense (FTD) device that is managed by the FMC Software. This vulnerability is due to insufficient authorization of configuration commands that are sent through the web service interface. An attacker could exploit this vulnerability by authenticating to the FMC web services interface and sending a crafted HTTP request to an affected device. A successful exploit could allow the attacker to execute certain configuration commands on the targeted FTD device. To successfully exploit this vulnerability, an attacker would need valid credentials on the FMC Software.



- [https://github.com/0zer0d4y/FuegoTest](https://github.com/0zer0d4y/FuegoTest) :  ![starts](https://img.shields.io/github/stars/0zer0d4y/FuegoTest.svg) ![forks](https://img.shields.io/github/forks/0zer0d4y/FuegoTest.svg)

## CVE-2023-20025
 A vulnerability in the web-based management interface of Cisco Small Business RV016, RV042, RV042G, and RV082 Routers could allow an unauthenticated, remote attacker to bypass authentication on an affected device.
 This vulnerability is due to improper validation of user input within incoming HTTP packets. An attacker could exploit this vulnerability by sending a crafted HTTP request to the web-based management interface. A successful exploit could allow the attacker to bypass authentication and gain root access on the underlying operating system.



- [https://github.com/lnversed/CVE-2023-20025](https://github.com/lnversed/CVE-2023-20025) :  ![starts](https://img.shields.io/github/stars/lnversed/CVE-2023-20025.svg) ![forks](https://img.shields.io/github/forks/lnversed/CVE-2023-20025.svg)

## CVE-2023-7261
 Inappropriate implementation in Google Updator prior to 1.3.36.351 in Google Chrome allowed a local attacker to perform privilege escalation via a malicious file. (Chromium security severity: High)



- [https://github.com/zerozenxlabs/CVE-2023-7261](https://github.com/zerozenxlabs/CVE-2023-7261) :  ![starts](https://img.shields.io/github/stars/zerozenxlabs/CVE-2023-7261.svg) ![forks](https://img.shields.io/github/forks/zerozenxlabs/CVE-2023-7261.svg)

## CVE-2023-7231
 The illi Link Party! WordPress plugin through 1.0 lacks proper access controls, allowing unauthenticated visitors to delete links.



- [https://github.com/BBO513/CVE-2023-7231](https://github.com/BBO513/CVE-2023-7231) :  ![starts](https://img.shields.io/github/stars/BBO513/CVE-2023-7231.svg) ![forks](https://img.shields.io/github/forks/BBO513/CVE-2023-7231.svg)

## CVE-2023-7173
 A vulnerability, which was classified as problematic, was found in PHPGurukul Hospital Management System 1.0. This affects an unknown part of the file registration.php. The manipulation of the argument First Name leads to cross site scripting. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The identifier VDB-249357 was assigned to this vulnerability.



- [https://github.com/sharathc213/CVE-2023-7173](https://github.com/sharathc213/CVE-2023-7173) :  ![starts](https://img.shields.io/github/stars/sharathc213/CVE-2023-7173.svg) ![forks](https://img.shields.io/github/forks/sharathc213/CVE-2023-7173.svg)

## CVE-2023-7172
 A vulnerability, which was classified as critical, has been found in PHPGurukul Hospital Management System 1.0. Affected by this issue is some unknown functionality of the component Admin Dashboard. The manipulation leads to sql injection. The attack may be launched remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-249356.



- [https://github.com/sharathc213/CVE-2023-7172](https://github.com/sharathc213/CVE-2023-7172) :  ![starts](https://img.shields.io/github/stars/sharathc213/CVE-2023-7172.svg) ![forks](https://img.shields.io/github/forks/sharathc213/CVE-2023-7172.svg)

## CVE-2023-7028
 An issue has been discovered in GitLab CE/EE affecting all versions from 16.1 prior to 16.1.6, 16.2 prior to 16.2.9, 16.3 prior to 16.3.7, 16.4 prior to 16.4.5, 16.5 prior to 16.5.6, 16.6 prior to 16.6.4, and 16.7 prior to 16.7.2 in which user account password reset emails could be delivered to an unverified email address.



- [https://github.com/Vozec/CVE-2023-7028](https://github.com/Vozec/CVE-2023-7028) :  ![starts](https://img.shields.io/github/stars/Vozec/CVE-2023-7028.svg) ![forks](https://img.shields.io/github/forks/Vozec/CVE-2023-7028.svg)

- [https://github.com/RandomRobbieBF/CVE-2023-7028](https://github.com/RandomRobbieBF/CVE-2023-7028) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-7028.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-7028.svg)

- [https://github.com/Esonhugh/gitlab_honeypot](https://github.com/Esonhugh/gitlab_honeypot) :  ![starts](https://img.shields.io/github/stars/Esonhugh/gitlab_honeypot.svg) ![forks](https://img.shields.io/github/forks/Esonhugh/gitlab_honeypot.svg)

- [https://github.com/duy-31/CVE-2023-7028](https://github.com/duy-31/CVE-2023-7028) :  ![starts](https://img.shields.io/github/stars/duy-31/CVE-2023-7028.svg) ![forks](https://img.shields.io/github/forks/duy-31/CVE-2023-7028.svg)

- [https://github.com/thanhlam-attt/CVE-2023-7028](https://github.com/thanhlam-attt/CVE-2023-7028) :  ![starts](https://img.shields.io/github/stars/thanhlam-attt/CVE-2023-7028.svg) ![forks](https://img.shields.io/github/forks/thanhlam-attt/CVE-2023-7028.svg)

- [https://github.com/hackeremmen/gitlab-exploit](https://github.com/hackeremmen/gitlab-exploit) :  ![starts](https://img.shields.io/github/stars/hackeremmen/gitlab-exploit.svg) ![forks](https://img.shields.io/github/forks/hackeremmen/gitlab-exploit.svg)

- [https://github.com/Trackflaw/CVE-2023-7028-Docker](https://github.com/Trackflaw/CVE-2023-7028-Docker) :  ![starts](https://img.shields.io/github/stars/Trackflaw/CVE-2023-7028-Docker.svg) ![forks](https://img.shields.io/github/forks/Trackflaw/CVE-2023-7028-Docker.svg)

- [https://github.com/olebris/Exploit_CVE_2023_7028-](https://github.com/olebris/Exploit_CVE_2023_7028-) :  ![starts](https://img.shields.io/github/stars/olebris/Exploit_CVE_2023_7028-.svg) ![forks](https://img.shields.io/github/forks/olebris/Exploit_CVE_2023_7028-.svg)

- [https://github.com/googlei1996/CVE-2023-7028](https://github.com/googlei1996/CVE-2023-7028) :  ![starts](https://img.shields.io/github/stars/googlei1996/CVE-2023-7028.svg) ![forks](https://img.shields.io/github/forks/googlei1996/CVE-2023-7028.svg)

- [https://github.com/soltanali0/CVE-2023-7028](https://github.com/soltanali0/CVE-2023-7028) :  ![starts](https://img.shields.io/github/stars/soltanali0/CVE-2023-7028.svg) ![forks](https://img.shields.io/github/forks/soltanali0/CVE-2023-7028.svg)

- [https://github.com/mochammadrafi/CVE-2023-7028](https://github.com/mochammadrafi/CVE-2023-7028) :  ![starts](https://img.shields.io/github/stars/mochammadrafi/CVE-2023-7028.svg) ![forks](https://img.shields.io/github/forks/mochammadrafi/CVE-2023-7028.svg)

- [https://github.com/szybnev/CVE-2023-7028](https://github.com/szybnev/CVE-2023-7028) :  ![starts](https://img.shields.io/github/stars/szybnev/CVE-2023-7028.svg) ![forks](https://img.shields.io/github/forks/szybnev/CVE-2023-7028.svg)

- [https://github.com/yoryio/CVE-2023-7028](https://github.com/yoryio/CVE-2023-7028) :  ![starts](https://img.shields.io/github/stars/yoryio/CVE-2023-7028.svg) ![forks](https://img.shields.io/github/forks/yoryio/CVE-2023-7028.svg)

- [https://github.com/Shimon03/CVE-2023-7028-Account-Take-Over-Gitlab](https://github.com/Shimon03/CVE-2023-7028-Account-Take-Over-Gitlab) :  ![starts](https://img.shields.io/github/stars/Shimon03/CVE-2023-7028-Account-Take-Over-Gitlab.svg) ![forks](https://img.shields.io/github/forks/Shimon03/CVE-2023-7028-Account-Take-Over-Gitlab.svg)

## CVE-2023-7016
 A flaw in Thales SafeNet Authentication Client prior to 10.8 R10 on Windows allows an attacker to execute code at a SYSTEM level via local access.



- [https://github.com/ewilded/CVE-2023-7016-POC](https://github.com/ewilded/CVE-2023-7016-POC) :  ![starts](https://img.shields.io/github/stars/ewilded/CVE-2023-7016-POC.svg) ![forks](https://img.shields.io/github/forks/ewilded/CVE-2023-7016-POC.svg)

## CVE-2023-6985
 The 10Web AI Assistant – AI content writing assistant plugin for WordPress is vulnerable to unauthorized modification of data due to a missing capability check on the install_plugin AJAX action in all versions up to, and including, 1.0.18. This makes it possible for authenticated attackers, with subscriber-level access and above, to install arbitrary plugins that can be used to gain further access to a compromised site.



- [https://github.com/RandomRobbieBF/CVE-2023-6985](https://github.com/RandomRobbieBF/CVE-2023-6985) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-6985.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-6985.svg)

## CVE-2023-6933
 The Better Search Replace plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and including, 1.4.4 via deserialization of untrusted input. This makes it possible for unauthenticated attackers to inject a PHP Object. No POP chain is present in the vulnerable plugin. If a POP chain is present via an additional plugin or theme installed on the target system, it could allow the attacker to delete arbitrary files, retrieve sensitive data, or execute code.



- [https://github.com/w2xim3/CVE-2023-6933](https://github.com/w2xim3/CVE-2023-6933) :  ![starts](https://img.shields.io/github/stars/w2xim3/CVE-2023-6933.svg) ![forks](https://img.shields.io/github/forks/w2xim3/CVE-2023-6933.svg)

## CVE-2023-6931
 A heap out-of-bounds write vulnerability in the Linux kernel's Performance Events system component can be exploited to achieve local privilege escalation.

A perf_event's read_size can overflow, leading to an heap out-of-bounds increment or write in perf_read_group().

We recommend upgrading past commit 382c27f4ed28f803b1f1473ac2d8db0afc795a1b.



- [https://github.com/K0n9-log/CVE-2023-6931](https://github.com/K0n9-log/CVE-2023-6931) :  ![starts](https://img.shields.io/github/stars/K0n9-log/CVE-2023-6931.svg) ![forks](https://img.shields.io/github/forks/K0n9-log/CVE-2023-6931.svg)

## CVE-2023-6895
 A vulnerability was found in Hikvision Intercom Broadcasting System 3.0.3_20201113_RELEASE(HIK). It has been declared as critical. This vulnerability affects unknown code of the file /php/ping.php. The manipulation of the argument jsondata[ip] with the input netstat -ano leads to os command injection. The exploit has been disclosed to the public and may be used. Upgrading to version 4.1.0 is able to address this issue. It is recommended to upgrade the affected component. VDB-248254 is the identifier assigned to this vulnerability.



- [https://github.com/FuBoLuSec/CVE-2023-6895](https://github.com/FuBoLuSec/CVE-2023-6895) :  ![starts](https://img.shields.io/github/stars/FuBoLuSec/CVE-2023-6895.svg) ![forks](https://img.shields.io/github/forks/FuBoLuSec/CVE-2023-6895.svg)

- [https://github.com/nles-crt/CVE-2023-6895](https://github.com/nles-crt/CVE-2023-6895) :  ![starts](https://img.shields.io/github/stars/nles-crt/CVE-2023-6895.svg) ![forks](https://img.shields.io/github/forks/nles-crt/CVE-2023-6895.svg)

## CVE-2023-6875
 The POST SMTP Mailer – Email log, Delivery Failure Notifications and Best Mail SMTP for WordPress plugin for WordPress is vulnerable to unauthorized access of data and modification of data due to a type juggling issue on the connect-app REST endpoint in all versions up to, and including, 2.8.7. This makes it possible for unauthenticated attackers to reset the API key used to authenticate to the mailer and view logs, including password reset emails, allowing site takeover.



- [https://github.com/UlyssesSaicha/CVE-2023-6875](https://github.com/UlyssesSaicha/CVE-2023-6875) :  ![starts](https://img.shields.io/github/stars/UlyssesSaicha/CVE-2023-6875.svg) ![forks](https://img.shields.io/github/forks/UlyssesSaicha/CVE-2023-6875.svg)

- [https://github.com/gbrsh/CVE-2023-6875](https://github.com/gbrsh/CVE-2023-6875) :  ![starts](https://img.shields.io/github/stars/gbrsh/CVE-2023-6875.svg) ![forks](https://img.shields.io/github/forks/gbrsh/CVE-2023-6875.svg)

- [https://github.com/hatlesswizard/CVE-2023-6875](https://github.com/hatlesswizard/CVE-2023-6875) :  ![starts](https://img.shields.io/github/stars/hatlesswizard/CVE-2023-6875.svg) ![forks](https://img.shields.io/github/forks/hatlesswizard/CVE-2023-6875.svg)

## CVE-2023-6710
 A flaw was found in the mod_proxy_cluster in the Apache server. This issue may allow a malicious user to add a script in the 'alias' parameter in the URL to trigger the stored cross-site scripting (XSS) vulnerability. By adding a script on the alias parameter on the URL, it adds a new virtual host and adds the script to the cluster-manager page.



- [https://github.com/DedSec-47/CVE-2023-6710](https://github.com/DedSec-47/CVE-2023-6710) :  ![starts](https://img.shields.io/github/stars/DedSec-47/CVE-2023-6710.svg) ![forks](https://img.shields.io/github/forks/DedSec-47/CVE-2023-6710.svg)

- [https://github.com/DedSec-47/Metasploit-Exploits-CVE-2023-6710](https://github.com/DedSec-47/Metasploit-Exploits-CVE-2023-6710) :  ![starts](https://img.shields.io/github/stars/DedSec-47/Metasploit-Exploits-CVE-2023-6710.svg) ![forks](https://img.shields.io/github/forks/DedSec-47/Metasploit-Exploits-CVE-2023-6710.svg)

## CVE-2023-6702
 Type confusion in V8 in Google Chrome prior to 120.0.6099.109 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/kaist-hacking/CVE-2023-6702](https://github.com/kaist-hacking/CVE-2023-6702) :  ![starts](https://img.shields.io/github/stars/kaist-hacking/CVE-2023-6702.svg) ![forks](https://img.shields.io/github/forks/kaist-hacking/CVE-2023-6702.svg)

## CVE-2023-6700
 The Cookie Information | Free GDPR Consent Solution plugin for WordPress is vulnerable to arbitrary option updates due to a missing capability check on its AJAX request handler in versions up to, and including, 2.0.22. This makes it possible for authenticated attackers, with subscriber-level access or higher, to edit arbitrary site options which can be used to create administrator accounts.



- [https://github.com/RandomRobbieBF/CVE-2023-6700](https://github.com/RandomRobbieBF/CVE-2023-6700) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-6700.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-6700.svg)

## CVE-2023-6663
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/cli-ish/CVE-2023-6663](https://github.com/cli-ish/CVE-2023-6663) :  ![starts](https://img.shields.io/github/stars/cli-ish/CVE-2023-6663.svg) ![forks](https://img.shields.io/github/forks/cli-ish/CVE-2023-6663.svg)

## CVE-2023-6661
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/cli-ish/CVE-2023-6661](https://github.com/cli-ish/CVE-2023-6661) :  ![starts](https://img.shields.io/github/stars/cli-ish/CVE-2023-6661.svg) ![forks](https://img.shields.io/github/forks/cli-ish/CVE-2023-6661.svg)

## CVE-2023-6654
 A vulnerability classified as critical was found in PHPEMS 6.x/7.x/8.x/9.0. Affected by this vulnerability is an unknown functionality in the library lib/session.cls.php of the component Session Data Handler. The manipulation leads to deserialization. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The identifier VDB-247357 was assigned to this vulnerability.



- [https://github.com/qfmy1024/CVE-2023-6654](https://github.com/qfmy1024/CVE-2023-6654) :  ![starts](https://img.shields.io/github/stars/qfmy1024/CVE-2023-6654.svg) ![forks](https://img.shields.io/github/forks/qfmy1024/CVE-2023-6654.svg)

## CVE-2023-6634
 The LearnPress plugin for WordPress is vulnerable to Command Injection in all versions up to, and including, 4.2.5.7 via the get_content function. This is due to the plugin making use of the call_user_func function with user input. This makes it possible for unauthenticated attackers to execute any public function with one parameter, which could result in remote code execution.



- [https://github.com/krn966/CVE-2023-6634](https://github.com/krn966/CVE-2023-6634) :  ![starts](https://img.shields.io/github/stars/krn966/CVE-2023-6634.svg) ![forks](https://img.shields.io/github/forks/krn966/CVE-2023-6634.svg)

## CVE-2023-6595
 In WhatsUp Gold versions released before 2023.1, an API endpoint was found to be missing an authentication mechanism. It is possible for an unauthenticated attacker to enumerate ancillary credential information stored within WhatsUp Gold.



- [https://github.com/sharmashreejaa/CVE-2023-6595](https://github.com/sharmashreejaa/CVE-2023-6595) :  ![starts](https://img.shields.io/github/stars/sharmashreejaa/CVE-2023-6595.svg) ![forks](https://img.shields.io/github/forks/sharmashreejaa/CVE-2023-6595.svg)

## CVE-2023-6567
 The LearnPress plugin for WordPress is vulnerable to time-based SQL Injection via the ‘order_by’ parameter in all versions up to, and including, 4.2.5.7 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/mimiloveexe/CVE-2023-6567-poc](https://github.com/mimiloveexe/CVE-2023-6567-poc) :  ![starts](https://img.shields.io/github/stars/mimiloveexe/CVE-2023-6567-poc.svg) ![forks](https://img.shields.io/github/forks/mimiloveexe/CVE-2023-6567-poc.svg)

## CVE-2023-6553
 The Backup Migration plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, 1.3.7 via the /includes/backup-heart.php file. This is due to an attacker being able to control the values passed to an include, and subsequently leverage that to achieve remote code execution. This makes it possible for unauthenticated attackers to easily execute code on the server.



- [https://github.com/Chocapikk/CVE-2023-6553](https://github.com/Chocapikk/CVE-2023-6553) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-6553.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-6553.svg)

- [https://github.com/motikan2010/CVE-2023-6553-PoC](https://github.com/motikan2010/CVE-2023-6553-PoC) :  ![starts](https://img.shields.io/github/stars/motikan2010/CVE-2023-6553-PoC.svg) ![forks](https://img.shields.io/github/forks/motikan2010/CVE-2023-6553-PoC.svg)

- [https://github.com/cc3305/CVE-2023-6553](https://github.com/cc3305/CVE-2023-6553) :  ![starts](https://img.shields.io/github/stars/cc3305/CVE-2023-6553.svg) ![forks](https://img.shields.io/github/forks/cc3305/CVE-2023-6553.svg)

- [https://github.com/kiddenta/CVE-2023-6553](https://github.com/kiddenta/CVE-2023-6553) :  ![starts](https://img.shields.io/github/stars/kiddenta/CVE-2023-6553.svg) ![forks](https://img.shields.io/github/forks/kiddenta/CVE-2023-6553.svg)

- [https://github.com/Harshit-Mashru/CVE-2023-6553](https://github.com/Harshit-Mashru/CVE-2023-6553) :  ![starts](https://img.shields.io/github/stars/Harshit-Mashru/CVE-2023-6553.svg) ![forks](https://img.shields.io/github/forks/Harshit-Mashru/CVE-2023-6553.svg)

## CVE-2023-6538
 SMU versions prior to 14.8.7825.01 are susceptible to unintended information disclosure, through URL manipulation. Authenticated users in Storage, Server or combined Server+Storage administrative roles are able to access SMU configuration backup, that would normally be barred to those specific administrative roles. 



- [https://github.com/Arszilla/CVE-2023-6538](https://github.com/Arszilla/CVE-2023-6538) :  ![starts](https://img.shields.io/github/stars/Arszilla/CVE-2023-6538.svg) ![forks](https://img.shields.io/github/forks/Arszilla/CVE-2023-6538.svg)

## CVE-2023-6444
 The Seriously Simple Podcasting WordPress plugin before 3.0.0 discloses the Podcast owner's email address (which by default is the admin email address) via an unauthenticated crafted request.



- [https://github.com/Wayne-Ker/CVE-2023-6444-POC](https://github.com/Wayne-Ker/CVE-2023-6444-POC) :  ![starts](https://img.shields.io/github/stars/Wayne-Ker/CVE-2023-6444-POC.svg) ![forks](https://img.shields.io/github/forks/Wayne-Ker/CVE-2023-6444-POC.svg)

## CVE-2023-6387
 A potential buffer overflow exists in the Bluetooth LE HCI CPC sample application in the Gecko SDK which may result in a denial of service or remote code execution



- [https://github.com/A3ST1CODE/CVE_6387](https://github.com/A3ST1CODE/CVE_6387) :  ![starts](https://img.shields.io/github/stars/A3ST1CODE/CVE_6387.svg) ![forks](https://img.shields.io/github/forks/A3ST1CODE/CVE_6387.svg)

## CVE-2023-6319
 A command injection vulnerability exists in the getAudioMetadata method from the com.webos.service.attachedstoragemanager service on webOS version 4 through 7. A series of specially crafted requests can lead to command execution as the root user. An attacker can make authenticated requests to trigger this vulnerability.

  *  webOS 4.9.7 - 5.30.40 running on LG43UM7000PLA 

  *  webOS 5.5.0 - 04.50.51 running on OLED55CXPUA 

  *  webOS 6.3.3-442 (kisscurl-kinglake) - 03.36.50 running on OLED48C1PUB 

  *  webOS 7.3.1-43 (mullet-mebin) - 03.33.85 running on OLED55A23LA





- [https://github.com/illixion/root-my-webos-tv](https://github.com/illixion/root-my-webos-tv) :  ![starts](https://img.shields.io/github/stars/illixion/root-my-webos-tv.svg) ![forks](https://img.shields.io/github/forks/illixion/root-my-webos-tv.svg)

## CVE-2023-6289
 The Swift Performance Lite WordPress plugin before 2.3.6.15 does not prevent users from exporting the plugin's settings, which may include sensitive information such as Cloudflare API tokens.



- [https://github.com/RandomRobbieBF/CVE-2023-6289](https://github.com/RandomRobbieBF/CVE-2023-6289) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-6289.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-6289.svg)

## CVE-2023-6246
 A heap-based buffer overflow was found in the __vsyslog_internal function of the glibc library. This function is called by the syslog and vsyslog functions. This issue occurs when the openlog function was not called, or called with the ident argument set to NULL, and the program name (the basename of argv[0]) is bigger than 1024 bytes, resulting in an application crash or local privilege escalation. This issue affects glibc 2.36 and newer.



- [https://github.com/elpe-pinillo/CVE-2023-6246](https://github.com/elpe-pinillo/CVE-2023-6246) :  ![starts](https://img.shields.io/github/stars/elpe-pinillo/CVE-2023-6246.svg) ![forks](https://img.shields.io/github/forks/elpe-pinillo/CVE-2023-6246.svg)

## CVE-2023-6241
 Use After Free vulnerability in Arm Ltd Midgard GPU Kernel Driver, Arm Ltd Bifrost GPU Kernel Driver, Arm Ltd Valhall GPU Kernel Driver, Arm Ltd Arm 5th Gen GPU Architecture Kernel Driver allows a local non-privileged user to exploit a software race condition to perform improper memory processing operations. If the system’s memory is carefully prepared by the user, then this in turn cause a use-after-free.This issue affects Midgard GPU Kernel Driver: from r13p0 through r32p0; Bifrost GPU Kernel Driver: from r11p0 through r25p0; Valhall GPU Kernel Driver: from r19p0 through r25p0, from r29p0 through r46p0; Arm 5th Gen GPU Architecture Kernel Driver: from r41p0 through r46p0.





- [https://github.com/SmileTabLabo/CVE-2023-6241](https://github.com/SmileTabLabo/CVE-2023-6241) :  ![starts](https://img.shields.io/github/stars/SmileTabLabo/CVE-2023-6241.svg) ![forks](https://img.shields.io/github/forks/SmileTabLabo/CVE-2023-6241.svg)

## CVE-2023-6063
 The WP Fastest Cache WordPress plugin before 1.2.2 does not properly sanitise and escape a parameter before using it in a SQL statement, leading to a SQL injection exploitable by unauthenticated users.



- [https://github.com/motikan2010/CVE-2023-6063-PoC](https://github.com/motikan2010/CVE-2023-6063-PoC) :  ![starts](https://img.shields.io/github/stars/motikan2010/CVE-2023-6063-PoC.svg) ![forks](https://img.shields.io/github/forks/motikan2010/CVE-2023-6063-PoC.svg)

- [https://github.com/Eulex0x/CVE-2023-6063](https://github.com/Eulex0x/CVE-2023-6063) :  ![starts](https://img.shields.io/github/stars/Eulex0x/CVE-2023-6063.svg) ![forks](https://img.shields.io/github/forks/Eulex0x/CVE-2023-6063.svg)

- [https://github.com/hackersroot/CVE-2023-6063-PoC](https://github.com/hackersroot/CVE-2023-6063-PoC) :  ![starts](https://img.shields.io/github/stars/hackersroot/CVE-2023-6063-PoC.svg) ![forks](https://img.shields.io/github/forks/hackersroot/CVE-2023-6063-PoC.svg)

- [https://github.com/incommatose/CVE-2023-6063-PoC](https://github.com/incommatose/CVE-2023-6063-PoC) :  ![starts](https://img.shields.io/github/stars/incommatose/CVE-2023-6063-PoC.svg) ![forks](https://img.shields.io/github/forks/incommatose/CVE-2023-6063-PoC.svg)

## CVE-2023-6036
 The Web3 WordPress plugin before 3.0.0 is vulnerable to an authentication bypass due to incorrect authentication checking in the login flow in functions 'handle_auth_request' and 'hadle_login_request'. This makes it possible for non authenticated attackers to log in as any existing user on the site, such as an administrator, if they have access to the username.



- [https://github.com/pctripsesp/CVE-2023-6036](https://github.com/pctripsesp/CVE-2023-6036) :  ![starts](https://img.shields.io/github/stars/pctripsesp/CVE-2023-6036.svg) ![forks](https://img.shields.io/github/forks/pctripsesp/CVE-2023-6036.svg)

## CVE-2023-6019
 A command injection existed in Ray's cpu_profile URL parameter allowing attackers to execute os commands on the system running the ray dashboard remotely without authentication. The issue is fixed in version 2.8.1+. Ray maintainers' response can be found here: https://www.anyscale.com/blog/update-on-ray-cves-cve-2023-6019-cve-2023-6020-cve-2023-6021-cve-2023-48022-cve-2023-48023



- [https://github.com/Clydeston/CVE-2023-6019](https://github.com/Clydeston/CVE-2023-6019) :  ![starts](https://img.shields.io/github/stars/Clydeston/CVE-2023-6019.svg) ![forks](https://img.shields.io/github/forks/Clydeston/CVE-2023-6019.svg)

- [https://github.com/FireWolfWang/CVE-2023-6019](https://github.com/FireWolfWang/CVE-2023-6019) :  ![starts](https://img.shields.io/github/stars/FireWolfWang/CVE-2023-6019.svg) ![forks](https://img.shields.io/github/forks/FireWolfWang/CVE-2023-6019.svg)

## CVE-2023-6000
 The Popup Builder WordPress plugin before 4.2.3 does not prevent simple visitors from updating existing popups, and injecting raw JavaScript in them, which could lead to Stored XSS attacks.



- [https://github.com/rxerium/CVE-2023-6000](https://github.com/rxerium/CVE-2023-6000) :  ![starts](https://img.shields.io/github/stars/rxerium/CVE-2023-6000.svg) ![forks](https://img.shields.io/github/forks/rxerium/CVE-2023-6000.svg)

## CVE-2023-5966
 An authenticated privileged attacker could upload a specially crafted zip to the EspoCRM server in version 7.2.5, via the extension deployment form, which could lead to arbitrary PHP code execution.



- [https://github.com/pedrojosenavasperez/cve-2023-5966](https://github.com/pedrojosenavasperez/cve-2023-5966) :  ![starts](https://img.shields.io/github/stars/pedrojosenavasperez/cve-2023-5966.svg) ![forks](https://img.shields.io/github/forks/pedrojosenavasperez/cve-2023-5966.svg)

## CVE-2023-5965
 An authenticated privileged attacker could upload a specially crafted zip to the EspoCRM server in version 7.2.5, via the update form, which could lead to arbitrary PHP code execution.



- [https://github.com/pedrojosenavasperez/cve-2023-5965](https://github.com/pedrojosenavasperez/cve-2023-5965) :  ![starts](https://img.shields.io/github/stars/pedrojosenavasperez/cve-2023-5965.svg) ![forks](https://img.shields.io/github/forks/pedrojosenavasperez/cve-2023-5965.svg)

## CVE-2023-5961
 A Cross-Site Request Forgery (CSRF) vulnerability has been identified in ioLogik E1200 Series firmware versions v3.3 and prior. An attacker can exploit this vulnerability to trick a client into making an unintentional request to the web server, which will be treated as an authentic request. This vulnerability may lead an attacker to perform operations on behalf of the victimized user.





- [https://github.com/HadessCS/CVE-2023-5961](https://github.com/HadessCS/CVE-2023-5961) :  ![starts](https://img.shields.io/github/stars/HadessCS/CVE-2023-5961.svg) ![forks](https://img.shields.io/github/forks/HadessCS/CVE-2023-5961.svg)

## CVE-2023-5808
 SMU versions prior to 14.8.7825.01 are susceptible to unintended information disclosure, through URL manipulation. Authenticated users in a Storage administrative role are able to access HNAS configuration backup and diagnostic data, that would normally be barred to that specific administrative role.



- [https://github.com/Arszilla/CVE-2023-5808](https://github.com/Arszilla/CVE-2023-5808) :  ![starts](https://img.shields.io/github/stars/Arszilla/CVE-2023-5808.svg) ![forks](https://img.shields.io/github/forks/Arszilla/CVE-2023-5808.svg)

## CVE-2023-5717
 A heap out-of-bounds write vulnerability in the Linux kernel's Linux Kernel Performance Events (perf) component can be exploited to achieve local privilege escalation.

If perf_read_group() is called while an event's sibling_list is smaller than its child's sibling_list, it can increment or write to memory locations outside of the allocated buffer.

We recommend upgrading past commit 32671e3799ca2e4590773fd0e63aaa4229e50c06.



- [https://github.com/uthrasri/CVE-2023-5717](https://github.com/uthrasri/CVE-2023-5717) :  ![starts](https://img.shields.io/github/stars/uthrasri/CVE-2023-5717.svg) ![forks](https://img.shields.io/github/forks/uthrasri/CVE-2023-5717.svg)

## CVE-2023-5612
 An issue has been discovered in GitLab affecting all versions before 16.6.6, 16.7 prior to 16.7.4, and 16.8 prior to 16.8.1. It was possible to read the user email address via tags feed although the visibility in the user profile has been disabled.



- [https://github.com/TopskiyPavelQwertyGang/Review.CVE-2023-5612](https://github.com/TopskiyPavelQwertyGang/Review.CVE-2023-5612) :  ![starts](https://img.shields.io/github/stars/TopskiyPavelQwertyGang/Review.CVE-2023-5612.svg) ![forks](https://img.shields.io/github/forks/TopskiyPavelQwertyGang/Review.CVE-2023-5612.svg)

## CVE-2023-5561
 WordPress does not properly restrict which user fields are searchable via the REST API, allowing unauthenticated attackers to discern the email addresses of users who have published public posts on an affected website via an Oracle style attack



- [https://github.com/pog007/CVE-2023-5561-PoC](https://github.com/pog007/CVE-2023-5561-PoC) :  ![starts](https://img.shields.io/github/stars/pog007/CVE-2023-5561-PoC.svg) ![forks](https://img.shields.io/github/forks/pog007/CVE-2023-5561-PoC.svg)

- [https://github.com/dthkhang/CVE-2023-5561-PoC](https://github.com/dthkhang/CVE-2023-5561-PoC) :  ![starts](https://img.shields.io/github/stars/dthkhang/CVE-2023-5561-PoC.svg) ![forks](https://img.shields.io/github/forks/dthkhang/CVE-2023-5561-PoC.svg)

## CVE-2023-5546
 ID numbers displayed in the quiz grading report required additional sanitizing to prevent a stored XSS risk.



- [https://github.com/obelia01/CVE-2023-5546](https://github.com/obelia01/CVE-2023-5546) :  ![starts](https://img.shields.io/github/stars/obelia01/CVE-2023-5546.svg) ![forks](https://img.shields.io/github/forks/obelia01/CVE-2023-5546.svg)

## CVE-2023-5540
 A remote code execution risk was identified in the IMSCP activity. By default this was only available to teachers and managers.



- [https://github.com/cli-ish/CVE-2023-5540](https://github.com/cli-ish/CVE-2023-5540) :  ![starts](https://img.shields.io/github/stars/cli-ish/CVE-2023-5540.svg) ![forks](https://img.shields.io/github/forks/cli-ish/CVE-2023-5540.svg)

## CVE-2023-5539
 A remote code execution risk was identified in the Lesson activity. By default this was only available to teachers and managers.



- [https://github.com/cli-ish/CVE-2023-5539](https://github.com/cli-ish/CVE-2023-5539) :  ![starts](https://img.shields.io/github/stars/cli-ish/CVE-2023-5539.svg) ![forks](https://img.shields.io/github/forks/cli-ish/CVE-2023-5539.svg)

## CVE-2023-5538
 The MpOperationLogs plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the IP Request Headers in versions up to, and including, 1.0.1 due to insufficient input sanitization and output escaping. This makes it possible for unauthenticated attackers to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page.



- [https://github.com/juweihuitao/MpOperationLogs](https://github.com/juweihuitao/MpOperationLogs) :  ![starts](https://img.shields.io/github/stars/juweihuitao/MpOperationLogs.svg) ![forks](https://img.shields.io/github/forks/juweihuitao/MpOperationLogs.svg)

## CVE-2023-5521
 Incorrect Authorization in GitHub repository tiann/kernelsu prior to v0.6.9.



- [https://github.com/Ylarod/CVE-2023-5521](https://github.com/Ylarod/CVE-2023-5521) :  ![starts](https://img.shields.io/github/stars/Ylarod/CVE-2023-5521.svg) ![forks](https://img.shields.io/github/forks/Ylarod/CVE-2023-5521.svg)

## CVE-2023-5412
 The Image horizontal reel scroll slideshow plugin for WordPress is vulnerable to SQL Injection via the plugin's shortcode in versions up to, and including, 13.2 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query. This makes it possible for authenticated attackers with subscriber-level and above permissions to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/RandomRobbieBF/CVE-2023-5412](https://github.com/RandomRobbieBF/CVE-2023-5412) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-5412.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-5412.svg)

## CVE-2023-5360
 The Royal Elementor Addons and Templates WordPress plugin before 1.3.79 does not properly validate uploaded files, which could allow unauthenticated users to upload arbitrary files, such as PHP and achieve RCE.



- [https://github.com/phankz/Worpress-CVE-2023-5360](https://github.com/phankz/Worpress-CVE-2023-5360) :  ![starts](https://img.shields.io/github/stars/phankz/Worpress-CVE-2023-5360.svg) ![forks](https://img.shields.io/github/forks/phankz/Worpress-CVE-2023-5360.svg)

- [https://github.com/Chocapikk/CVE-2023-5360](https://github.com/Chocapikk/CVE-2023-5360) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-5360.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-5360.svg)

- [https://github.com/Pushkarup/CVE-2023-5360](https://github.com/Pushkarup/CVE-2023-5360) :  ![starts](https://img.shields.io/github/stars/Pushkarup/CVE-2023-5360.svg) ![forks](https://img.shields.io/github/forks/Pushkarup/CVE-2023-5360.svg)

- [https://github.com/sagsooz/CVE-2023-5360](https://github.com/sagsooz/CVE-2023-5360) :  ![starts](https://img.shields.io/github/stars/sagsooz/CVE-2023-5360.svg) ![forks](https://img.shields.io/github/forks/sagsooz/CVE-2023-5360.svg)

- [https://github.com/tucommenceapousser/CVE-2023-5360](https://github.com/tucommenceapousser/CVE-2023-5360) :  ![starts](https://img.shields.io/github/stars/tucommenceapousser/CVE-2023-5360.svg) ![forks](https://img.shields.io/github/forks/tucommenceapousser/CVE-2023-5360.svg)

- [https://github.com/X3RX3SSec/CVE-2023-5360](https://github.com/X3RX3SSec/CVE-2023-5360) :  ![starts](https://img.shields.io/github/stars/X3RX3SSec/CVE-2023-5360.svg) ![forks](https://img.shields.io/github/forks/X3RX3SSec/CVE-2023-5360.svg)

- [https://github.com/nastar-id/CVE-2023-5360](https://github.com/nastar-id/CVE-2023-5360) :  ![starts](https://img.shields.io/github/stars/nastar-id/CVE-2023-5360.svg) ![forks](https://img.shields.io/github/forks/nastar-id/CVE-2023-5360.svg)

- [https://github.com/Jenderal92/WP-CVE-2023-5360](https://github.com/Jenderal92/WP-CVE-2023-5360) :  ![starts](https://img.shields.io/github/stars/Jenderal92/WP-CVE-2023-5360.svg) ![forks](https://img.shields.io/github/forks/Jenderal92/WP-CVE-2023-5360.svg)

## CVE-2023-5324
 A vulnerability has been found in eeroOS up to 6.16.4-11 and classified as critical. This vulnerability affects unknown code of the component Ethernet Interface. The manipulation leads to denial of service. The attack needs to be approached within the local network. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-241024.



- [https://github.com/nomis/eero-zero-length-ipv6-options-header-dos](https://github.com/nomis/eero-zero-length-ipv6-options-header-dos) :  ![starts](https://img.shields.io/github/stars/nomis/eero-zero-length-ipv6-options-header-dos.svg) ![forks](https://img.shields.io/github/forks/nomis/eero-zero-length-ipv6-options-header-dos.svg)

## CVE-2023-5270
 A vulnerability was found in SourceCodester Best Courier Management System 1.0. It has been declared as critical. Affected by this vulnerability is an unknown functionality of the file view_parcel.php. The manipulation of the argument id leads to sql injection. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-240883.



- [https://github.com/KevinMitchell-OSWP-CISSP/CVE-2023-52709-PoC](https://github.com/KevinMitchell-OSWP-CISSP/CVE-2023-52709-PoC) :  ![starts](https://img.shields.io/github/stars/KevinMitchell-OSWP-CISSP/CVE-2023-52709-PoC.svg) ![forks](https://img.shields.io/github/forks/KevinMitchell-OSWP-CISSP/CVE-2023-52709-PoC.svg)

## CVE-2023-5217
 Heap buffer overflow in vp8 encoding in libvpx in Google Chrome prior to 117.0.5938.132 and libvpx 1.13.1 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/UT-Security/cve-2023-5217-poc](https://github.com/UT-Security/cve-2023-5217-poc) :  ![starts](https://img.shields.io/github/stars/UT-Security/cve-2023-5217-poc.svg) ![forks](https://img.shields.io/github/forks/UT-Security/cve-2023-5217-poc.svg)

- [https://github.com/Trinadh465/platform_external_libvpx_v1.8.0_CVE-2023-5217](https://github.com/Trinadh465/platform_external_libvpx_v1.8.0_CVE-2023-5217) :  ![starts](https://img.shields.io/github/stars/Trinadh465/platform_external_libvpx_v1.8.0_CVE-2023-5217.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/platform_external_libvpx_v1.8.0_CVE-2023-5217.svg)

- [https://github.com/Trinadh465/platform_external_libvpx_v1.4.0_CVE-2023-5217](https://github.com/Trinadh465/platform_external_libvpx_v1.4.0_CVE-2023-5217) :  ![starts](https://img.shields.io/github/stars/Trinadh465/platform_external_libvpx_v1.4.0_CVE-2023-5217.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/platform_external_libvpx_v1.4.0_CVE-2023-5217.svg)

## CVE-2023-5204
 The ChatBot plugin for WordPress is vulnerable to SQL Injection via the $strid parameter in versions up to, and including, 4.8.9 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/RandomRobbieBF/CVE-2023-5204](https://github.com/RandomRobbieBF/CVE-2023-5204) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-5204.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-5204.svg)

## CVE-2023-5178
 A use-after-free vulnerability was found in drivers/nvme/target/tcp.c` in `nvmet_tcp_free_crypto` due to a logical bug in the NVMe/TCP subsystem in the Linux kernel. This issue may allow a malicious user to cause a use-after-free and double-free problem, which may permit remote code execution or lead to local privilege escalation.



- [https://github.com/rockrid3r/CVE-2023-5178](https://github.com/rockrid3r/CVE-2023-5178) :  ![starts](https://img.shields.io/github/stars/rockrid3r/CVE-2023-5178.svg) ![forks](https://img.shields.io/github/forks/rockrid3r/CVE-2023-5178.svg)

## CVE-2023-5142
 A vulnerability classified as problematic was found in H3C GR-1100-P, GR-1108-P, GR-1200W, GR-1800AX, GR-2200, GR-3200, GR-5200, GR-8300, ER2100n, ER2200G2, ER3200G2, ER3260G2, ER5100G2, ER5200G2 and ER6300G2 up to 20230908. This vulnerability affects unknown code of the file /userLogin.asp of the component Config File Handler. The manipulation leads to path traversal. The attack can be initiated remotely. The complexity of an attack is rather high. The exploitation appears to be difficult. The exploit has been disclosed to the public and may be used. VDB-240238 is the identifier assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/kuangxiaotu/CVE-H3C-Report](https://github.com/kuangxiaotu/CVE-H3C-Report) :  ![starts](https://img.shields.io/github/stars/kuangxiaotu/CVE-H3C-Report.svg) ![forks](https://img.shields.io/github/forks/kuangxiaotu/CVE-H3C-Report.svg)

## CVE-2023-5129
 This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. Duplicate of CVE-2023-4863.



- [https://github.com/GTGalaxi/ElectronVulnerableVersion](https://github.com/GTGalaxi/ElectronVulnerableVersion) :  ![starts](https://img.shields.io/github/stars/GTGalaxi/ElectronVulnerableVersion.svg) ![forks](https://img.shields.io/github/forks/GTGalaxi/ElectronVulnerableVersion.svg)

- [https://github.com/OITApps/Find-VulnerableElectronVersion](https://github.com/OITApps/Find-VulnerableElectronVersion) :  ![starts](https://img.shields.io/github/stars/OITApps/Find-VulnerableElectronVersion.svg) ![forks](https://img.shields.io/github/forks/OITApps/Find-VulnerableElectronVersion.svg)

## CVE-2023-5121
 The Migration, Backup, Staging – WPvivid plugin for WordPress is vulnerable to Stored Cross-Site Scripting via admin settings (the backup path parameter) in versions up to, and including, 0.9.89 due to insufficient input sanitization and output escaping. This makes it possible for authenticated attackers, with administrator-level permissions and above, to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page. This only affects multi-site installations and installations where unfiltered_html has been disabled.



- [https://github.com/chandraprarikraj/CVE-2023-51214](https://github.com/chandraprarikraj/CVE-2023-51214) :  ![starts](https://img.shields.io/github/stars/chandraprarikraj/CVE-2023-51214.svg) ![forks](https://img.shields.io/github/forks/chandraprarikraj/CVE-2023-51214.svg)

## CVE-2023-5111
 Os Commerce is currently susceptible to a Cross-Site Scripting (XSS) vulnerability.
This vulnerability allows attackers to inject JS through the "featured_type_name[1]" parameter,
potentially leading to unauthorized execution of scripts within a user's web browser.



- [https://github.com/OscarAkaElvis/CVE-2023-51119](https://github.com/OscarAkaElvis/CVE-2023-51119) :  ![starts](https://img.shields.io/github/stars/OscarAkaElvis/CVE-2023-51119.svg) ![forks](https://img.shields.io/github/forks/OscarAkaElvis/CVE-2023-51119.svg)

## CVE-2023-5089
 The Defender Security WordPress plugin before 4.1.0 does not prevent redirects to the login page via the auth_redirect WordPress function, allowing an unauthenticated visitor to access the login page, even when the hide login page functionality of the plugin is enabled.



- [https://github.com/Cappricio-Securities/CVE-2023-5089](https://github.com/Cappricio-Securities/CVE-2023-5089) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2023-5089.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2023-5089.svg)

## CVE-2023-5070
 The Social Media Share Buttons & Social Sharing Icons plugin for WordPress is vulnerable to Sensitive Information Exposure in versions up to, and including, 2.8.5 via the sfsi_save_export function. This can allow subscribers to export plugin settings that include social media authentication tokens and secrets as well as app passwords.



- [https://github.com/RandomRobbieBF/CVE-2023-5070](https://github.com/RandomRobbieBF/CVE-2023-5070) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-5070.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-5070.svg)

## CVE-2023-5059
 




Santesoft Sante FFT Imaging lacks proper validation of user-supplied data when parsing DICOM files. This could lead to an out-of-bounds read. An attacker could leverage this vulnerability to execute arbitrary code in the context of the current process.



- [https://github.com/chandraprarikraj/CVE-2023-50596](https://github.com/chandraprarikraj/CVE-2023-50596) :  ![starts](https://img.shields.io/github/stars/chandraprarikraj/CVE-2023-50596.svg) ![forks](https://img.shields.io/github/forks/chandraprarikraj/CVE-2023-50596.svg)

## CVE-2023-5044
 Code injection via nginx.ingress.kubernetes.io/permanent-redirect annotation.



- [https://github.com/r0binak/CVE-2023-5044](https://github.com/r0binak/CVE-2023-5044) :  ![starts](https://img.shields.io/github/stars/r0binak/CVE-2023-5044.svg) ![forks](https://img.shields.io/github/forks/r0binak/CVE-2023-5044.svg)

- [https://github.com/4ARMED/cve-2023-5044](https://github.com/4ARMED/cve-2023-5044) :  ![starts](https://img.shields.io/github/stars/4ARMED/cve-2023-5044.svg) ![forks](https://img.shields.io/github/forks/4ARMED/cve-2023-5044.svg)

- [https://github.com/KubernetesBachelor/CVE-2023-5044](https://github.com/KubernetesBachelor/CVE-2023-5044) :  ![starts](https://img.shields.io/github/stars/KubernetesBachelor/CVE-2023-5044.svg) ![forks](https://img.shields.io/github/forks/KubernetesBachelor/CVE-2023-5044.svg)

## CVE-2023-5043
 Ingress nginx annotation injection causes arbitrary command execution.



- [https://github.com/r0binak/CVE-2023-5043](https://github.com/r0binak/CVE-2023-5043) :  ![starts](https://img.shields.io/github/stars/r0binak/CVE-2023-5043.svg) ![forks](https://img.shields.io/github/forks/r0binak/CVE-2023-5043.svg)

## CVE-2023-5024
 A vulnerability was found in Planno 23.04.04. It has been classified as problematic. This affects an unknown part of the component Comment Handler. The manipulation leads to cross site scripting. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The identifier VDB-239865 was assigned to this vulnerability.



- [https://github.com/PH03N1XSP/CVE-2023-5024](https://github.com/PH03N1XSP/CVE-2023-5024) :  ![starts](https://img.shields.io/github/stars/PH03N1XSP/CVE-2023-5024.svg) ![forks](https://img.shields.io/github/forks/PH03N1XSP/CVE-2023-5024.svg)

## CVE-2023-5013
 A vulnerability has been found in Pluck CMS 4.7.18 and classified as problematic. This vulnerability affects unknown code of the file install.php of the component Installation Handler. The manipulation of the argument contents with the input scriptalert('xss')/script leads to cross site scripting. The attack can be initiated remotely. The complexity of an attack is rather high. The exploitation appears to be difficult. The exploit has been disclosed to the public and may be used. VDB-239854 is the identifier assigned to this vulnerability.



- [https://github.com/sajaljat/CVE-2023-50131](https://github.com/sajaljat/CVE-2023-50131) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2023-50131.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2023-50131.svg)

- [https://github.com/sajaljat/CVE-2023-50132](https://github.com/sajaljat/CVE-2023-50132) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2023-50132.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2023-50132.svg)

## CVE-2023-4966
 Sensitive information disclosure in NetScaler ADC and NetScaler Gateway when configured as a Gateway (VPN virtual server, ICA Proxy, CVPN, RDP Proxy) or AAA  virtual server.



- [https://github.com/Chocapikk/CVE-2023-4966](https://github.com/Chocapikk/CVE-2023-4966) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-4966.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-4966.svg)

- [https://github.com/dinosn/citrix_cve-2023-4966](https://github.com/dinosn/citrix_cve-2023-4966) :  ![starts](https://img.shields.io/github/stars/dinosn/citrix_cve-2023-4966.svg) ![forks](https://img.shields.io/github/forks/dinosn/citrix_cve-2023-4966.svg)

- [https://github.com/RevoltSecurities/CVE-2023-4966](https://github.com/RevoltSecurities/CVE-2023-4966) :  ![starts](https://img.shields.io/github/stars/RevoltSecurities/CVE-2023-4966.svg) ![forks](https://img.shields.io/github/forks/RevoltSecurities/CVE-2023-4966.svg)

- [https://github.com/mlynchcogent/CVE-2023-4966-POC](https://github.com/mlynchcogent/CVE-2023-4966-POC) :  ![starts](https://img.shields.io/github/stars/mlynchcogent/CVE-2023-4966-POC.svg) ![forks](https://img.shields.io/github/forks/mlynchcogent/CVE-2023-4966-POC.svg)

- [https://github.com/certat/citrix-logchecker](https://github.com/certat/citrix-logchecker) :  ![starts](https://img.shields.io/github/stars/certat/citrix-logchecker.svg) ![forks](https://img.shields.io/github/forks/certat/citrix-logchecker.svg)

- [https://github.com/morganwdavis/overread](https://github.com/morganwdavis/overread) :  ![starts](https://img.shields.io/github/stars/morganwdavis/overread.svg) ![forks](https://img.shields.io/github/forks/morganwdavis/overread.svg)

- [https://github.com/IceBreakerCode/CVE-2023-4966](https://github.com/IceBreakerCode/CVE-2023-4966) :  ![starts](https://img.shields.io/github/stars/IceBreakerCode/CVE-2023-4966.svg) ![forks](https://img.shields.io/github/forks/IceBreakerCode/CVE-2023-4966.svg)

- [https://github.com/akshthejo/CVE-2023-4966-exploit](https://github.com/akshthejo/CVE-2023-4966-exploit) :  ![starts](https://img.shields.io/github/stars/akshthejo/CVE-2023-4966-exploit.svg) ![forks](https://img.shields.io/github/forks/akshthejo/CVE-2023-4966-exploit.svg)

- [https://github.com/byte4RR4Y/CVE-2023-4966](https://github.com/byte4RR4Y/CVE-2023-4966) :  ![starts](https://img.shields.io/github/stars/byte4RR4Y/CVE-2023-4966.svg) ![forks](https://img.shields.io/github/forks/byte4RR4Y/CVE-2023-4966.svg)

- [https://github.com/s-bt/CVE-2023-4966](https://github.com/s-bt/CVE-2023-4966) :  ![starts](https://img.shields.io/github/stars/s-bt/CVE-2023-4966.svg) ![forks](https://img.shields.io/github/forks/s-bt/CVE-2023-4966.svg)

- [https://github.com/0xKayala/CVE-2023-4966](https://github.com/0xKayala/CVE-2023-4966) :  ![starts](https://img.shields.io/github/stars/0xKayala/CVE-2023-4966.svg) ![forks](https://img.shields.io/github/forks/0xKayala/CVE-2023-4966.svg)

- [https://github.com/jmussmann/cve-2023-4966-iocs](https://github.com/jmussmann/cve-2023-4966-iocs) :  ![starts](https://img.shields.io/github/stars/jmussmann/cve-2023-4966-iocs.svg) ![forks](https://img.shields.io/github/forks/jmussmann/cve-2023-4966-iocs.svg)

- [https://github.com/senpaisamp/Netscaler-CVE-2023-4966-POC](https://github.com/senpaisamp/Netscaler-CVE-2023-4966-POC) :  ![starts](https://img.shields.io/github/stars/senpaisamp/Netscaler-CVE-2023-4966-POC.svg) ![forks](https://img.shields.io/github/forks/senpaisamp/Netscaler-CVE-2023-4966-POC.svg)

## CVE-2023-4949
 An attacker with local access to a system (either through a disk or external drive) can present a modified XFS partition to grub-legacy in such a way to exploit a memory corruption in grub’s XFS file system implementation.




- [https://github.com/HuangYanQwQ/CVE-2023-49496_PoC](https://github.com/HuangYanQwQ/CVE-2023-49496_PoC) :  ![starts](https://img.shields.io/github/stars/HuangYanQwQ/CVE-2023-49496_PoC.svg) ![forks](https://img.shields.io/github/forks/HuangYanQwQ/CVE-2023-49496_PoC.svg)

## CVE-2023-4911
 A buffer overflow was discovered in the GNU C Library's dynamic loader ld.so while processing the GLIBC_TUNABLES environment variable. This issue could allow a local attacker to use maliciously crafted GLIBC_TUNABLES environment variables when launching binaries with SUID permission to execute code with elevated privileges.



- [https://github.com/leesh3288/CVE-2023-4911](https://github.com/leesh3288/CVE-2023-4911) :  ![starts](https://img.shields.io/github/stars/leesh3288/CVE-2023-4911.svg) ![forks](https://img.shields.io/github/forks/leesh3288/CVE-2023-4911.svg)

- [https://github.com/RickdeJager/CVE-2023-4911](https://github.com/RickdeJager/CVE-2023-4911) :  ![starts](https://img.shields.io/github/stars/RickdeJager/CVE-2023-4911.svg) ![forks](https://img.shields.io/github/forks/RickdeJager/CVE-2023-4911.svg)

- [https://github.com/chaudharyarjun/LooneyPwner](https://github.com/chaudharyarjun/LooneyPwner) :  ![starts](https://img.shields.io/github/stars/chaudharyarjun/LooneyPwner.svg) ![forks](https://img.shields.io/github/forks/chaudharyarjun/LooneyPwner.svg)

- [https://github.com/hadrian3689/looney-tunables-CVE-2023-4911](https://github.com/hadrian3689/looney-tunables-CVE-2023-4911) :  ![starts](https://img.shields.io/github/stars/hadrian3689/looney-tunables-CVE-2023-4911.svg) ![forks](https://img.shields.io/github/forks/hadrian3689/looney-tunables-CVE-2023-4911.svg)

- [https://github.com/ruycr4ft/CVE-2023-4911](https://github.com/ruycr4ft/CVE-2023-4911) :  ![starts](https://img.shields.io/github/stars/ruycr4ft/CVE-2023-4911.svg) ![forks](https://img.shields.io/github/forks/ruycr4ft/CVE-2023-4911.svg)

- [https://github.com/Green-Avocado/CVE-2023-4911](https://github.com/Green-Avocado/CVE-2023-4911) :  ![starts](https://img.shields.io/github/stars/Green-Avocado/CVE-2023-4911.svg) ![forks](https://img.shields.io/github/forks/Green-Avocado/CVE-2023-4911.svg)

- [https://github.com/KernelKrise/CVE-2023-4911](https://github.com/KernelKrise/CVE-2023-4911) :  ![starts](https://img.shields.io/github/stars/KernelKrise/CVE-2023-4911.svg) ![forks](https://img.shields.io/github/forks/KernelKrise/CVE-2023-4911.svg)

- [https://github.com/Diego-AltF4/CVE-2023-4911](https://github.com/Diego-AltF4/CVE-2023-4911) :  ![starts](https://img.shields.io/github/stars/Diego-AltF4/CVE-2023-4911.svg) ![forks](https://img.shields.io/github/forks/Diego-AltF4/CVE-2023-4911.svg)

- [https://github.com/NishanthAnand21/CVE-2023-4911-PoC](https://github.com/NishanthAnand21/CVE-2023-4911-PoC) :  ![starts](https://img.shields.io/github/stars/NishanthAnand21/CVE-2023-4911-PoC.svg) ![forks](https://img.shields.io/github/forks/NishanthAnand21/CVE-2023-4911-PoC.svg)

- [https://github.com/RRespxwnss/Looney-Tunables-CVE-2023-4911](https://github.com/RRespxwnss/Looney-Tunables-CVE-2023-4911) :  ![starts](https://img.shields.io/github/stars/RRespxwnss/Looney-Tunables-CVE-2023-4911.svg) ![forks](https://img.shields.io/github/forks/RRespxwnss/Looney-Tunables-CVE-2023-4911.svg)

- [https://github.com/xiaoQ1z/CVE-2023-4911](https://github.com/xiaoQ1z/CVE-2023-4911) :  ![starts](https://img.shields.io/github/stars/xiaoQ1z/CVE-2023-4911.svg) ![forks](https://img.shields.io/github/forks/xiaoQ1z/CVE-2023-4911.svg)

- [https://github.com/teraGL/looneyCVE](https://github.com/teraGL/looneyCVE) :  ![starts](https://img.shields.io/github/stars/teraGL/looneyCVE.svg) ![forks](https://img.shields.io/github/forks/teraGL/looneyCVE.svg)

- [https://github.com/silent6trinity/looney-tuneables](https://github.com/silent6trinity/looney-tuneables) :  ![starts](https://img.shields.io/github/stars/silent6trinity/looney-tuneables.svg) ![forks](https://img.shields.io/github/forks/silent6trinity/looney-tuneables.svg)

- [https://github.com/snurkeburk/Looney-Tunables](https://github.com/snurkeburk/Looney-Tunables) :  ![starts](https://img.shields.io/github/stars/snurkeburk/Looney-Tunables.svg) ![forks](https://img.shields.io/github/forks/snurkeburk/Looney-Tunables.svg)

- [https://github.com/guffre/CVE-2023-4911](https://github.com/guffre/CVE-2023-4911) :  ![starts](https://img.shields.io/github/stars/guffre/CVE-2023-4911.svg) ![forks](https://img.shields.io/github/forks/guffre/CVE-2023-4911.svg)

- [https://github.com/puckiestyle/CVE-2023-4911](https://github.com/puckiestyle/CVE-2023-4911) :  ![starts](https://img.shields.io/github/stars/puckiestyle/CVE-2023-4911.svg) ![forks](https://img.shields.io/github/forks/puckiestyle/CVE-2023-4911.svg)

## CVE-2023-4898
 Authentication Bypass by Primary Weakness in GitHub repository mintplex-labs/anything-llm prior to 0.0.1.



- [https://github.com/tristao-io/CVE-2023-48983](https://github.com/tristao-io/CVE-2023-48983) :  ![starts](https://img.shields.io/github/stars/tristao-io/CVE-2023-48983.svg) ![forks](https://img.shields.io/github/forks/tristao-io/CVE-2023-48983.svg)

- [https://github.com/tristao-io/CVE-2023-48982](https://github.com/tristao-io/CVE-2023-48982) :  ![starts](https://img.shields.io/github/stars/tristao-io/CVE-2023-48982.svg) ![forks](https://img.shields.io/github/forks/tristao-io/CVE-2023-48982.svg)

- [https://github.com/tristao-io/CVE-2023-48981](https://github.com/tristao-io/CVE-2023-48981) :  ![starts](https://img.shields.io/github/stars/tristao-io/CVE-2023-48981.svg) ![forks](https://img.shields.io/github/forks/tristao-io/CVE-2023-48981.svg)

- [https://github.com/l00neyhacker/CVE-2023-48984](https://github.com/l00neyhacker/CVE-2023-48984) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2023-48984.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2023-48984.svg)

## CVE-2023-4863
 Heap buffer overflow in libwebp in Google Chrome prior to 116.0.5845.187 and libwebp 1.3.2 allowed a remote attacker to perform an out of bounds memory write via a crafted HTML page. (Chromium security severity: Critical)



- [https://github.com/mistymntncop/CVE-2023-4863](https://github.com/mistymntncop/CVE-2023-4863) :  ![starts](https://img.shields.io/github/stars/mistymntncop/CVE-2023-4863.svg) ![forks](https://img.shields.io/github/forks/mistymntncop/CVE-2023-4863.svg)

- [https://github.com/LiveOverflow/webp-CVE-2023-4863](https://github.com/LiveOverflow/webp-CVE-2023-4863) :  ![starts](https://img.shields.io/github/stars/LiveOverflow/webp-CVE-2023-4863.svg) ![forks](https://img.shields.io/github/forks/LiveOverflow/webp-CVE-2023-4863.svg)

- [https://github.com/caoweiquan322/NotEnough](https://github.com/caoweiquan322/NotEnough) :  ![starts](https://img.shields.io/github/stars/caoweiquan322/NotEnough.svg) ![forks](https://img.shields.io/github/forks/caoweiquan322/NotEnough.svg)

- [https://github.com/murphysecurity/libwebp-checker](https://github.com/murphysecurity/libwebp-checker) :  ![starts](https://img.shields.io/github/stars/murphysecurity/libwebp-checker.svg) ![forks](https://img.shields.io/github/forks/murphysecurity/libwebp-checker.svg)

- [https://github.com/bbaranoff/CVE-2023-4863](https://github.com/bbaranoff/CVE-2023-4863) :  ![starts](https://img.shields.io/github/stars/bbaranoff/CVE-2023-4863.svg) ![forks](https://img.shields.io/github/forks/bbaranoff/CVE-2023-4863.svg)

- [https://github.com/GTGalaxi/ElectronVulnerableVersion](https://github.com/GTGalaxi/ElectronVulnerableVersion) :  ![starts](https://img.shields.io/github/stars/GTGalaxi/ElectronVulnerableVersion.svg) ![forks](https://img.shields.io/github/forks/GTGalaxi/ElectronVulnerableVersion.svg)

- [https://github.com/OITApps/Find-VulnerableElectronVersion](https://github.com/OITApps/Find-VulnerableElectronVersion) :  ![starts](https://img.shields.io/github/stars/OITApps/Find-VulnerableElectronVersion.svg) ![forks](https://img.shields.io/github/forks/OITApps/Find-VulnerableElectronVersion.svg)

- [https://github.com/talbeerysec/BAD-WEBP-CVE-2023-4863](https://github.com/talbeerysec/BAD-WEBP-CVE-2023-4863) :  ![starts](https://img.shields.io/github/stars/talbeerysec/BAD-WEBP-CVE-2023-4863.svg) ![forks](https://img.shields.io/github/forks/talbeerysec/BAD-WEBP-CVE-2023-4863.svg)

- [https://github.com/huiwen-yayaya/CVE-2023-4863](https://github.com/huiwen-yayaya/CVE-2023-4863) :  ![starts](https://img.shields.io/github/stars/huiwen-yayaya/CVE-2023-4863.svg) ![forks](https://img.shields.io/github/forks/huiwen-yayaya/CVE-2023-4863.svg)

- [https://github.com/CrackerCat/CVE-2023-4863-](https://github.com/CrackerCat/CVE-2023-4863-) :  ![starts](https://img.shields.io/github/stars/CrackerCat/CVE-2023-4863-.svg) ![forks](https://img.shields.io/github/forks/CrackerCat/CVE-2023-4863-.svg)

- [https://github.com/sarsaeroth/CVE-2023-4863-POC](https://github.com/sarsaeroth/CVE-2023-4863-POC) :  ![starts](https://img.shields.io/github/stars/sarsaeroth/CVE-2023-4863-POC.svg) ![forks](https://img.shields.io/github/forks/sarsaeroth/CVE-2023-4863-POC.svg)

## CVE-2023-4813
 A flaw was found in glibc. In an uncommon situation, the gaih_inet function may use memory that has been freed, resulting in an application crash. This issue is only exploitable when the getaddrinfo function is called and the hosts database in /etc/nsswitch.conf is configured with SUCCESS=continue or SUCCESS=merge.



- [https://github.com/tnishiox/cve-2023-4813](https://github.com/tnishiox/cve-2023-4813) :  ![starts](https://img.shields.io/github/stars/tnishiox/cve-2023-4813.svg) ![forks](https://img.shields.io/github/forks/tnishiox/cve-2023-4813.svg)

## CVE-2023-4800
 The DoLogin Security WordPress plugin before 3.7.1 does not restrict the access of a widget that shows the IPs of failed logins to low privileged users.



- [https://github.com/b0marek/CVE-2023-4800](https://github.com/b0marek/CVE-2023-4800) :  ![starts](https://img.shields.io/github/stars/b0marek/CVE-2023-4800.svg) ![forks](https://img.shields.io/github/forks/b0marek/CVE-2023-4800.svg)

## CVE-2023-4771
 A Cross-Site scripting vulnerability has been found in CKSource CKEditor affecting versions 4.15.1 and earlier. An attacker could send malicious javascript code through the /ckeditor/samples/old/ajax.html file and retrieve an authorized user's information.



- [https://github.com/sahar042/CVE-2023-4771](https://github.com/sahar042/CVE-2023-4771) :  ![starts](https://img.shields.io/github/stars/sahar042/CVE-2023-4771.svg) ![forks](https://img.shields.io/github/forks/sahar042/CVE-2023-4771.svg)

## CVE-2023-4762
 Type Confusion in V8 in Google Chrome prior to 116.0.5845.179 allowed a remote attacker to execute arbitrary code via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/buptsb/CVE-2023-4762](https://github.com/buptsb/CVE-2023-4762) :  ![starts](https://img.shields.io/github/stars/buptsb/CVE-2023-4762.svg) ![forks](https://img.shields.io/github/forks/buptsb/CVE-2023-4762.svg)

- [https://github.com/sherlocksecurity/CVE-2023-4762-Code-Review](https://github.com/sherlocksecurity/CVE-2023-4762-Code-Review) :  ![starts](https://img.shields.io/github/stars/sherlocksecurity/CVE-2023-4762-Code-Review.svg) ![forks](https://img.shields.io/github/forks/sherlocksecurity/CVE-2023-4762-Code-Review.svg)

## CVE-2023-4741
 A vulnerability has been found in IBOS OA 4.5.5 and classified as critical. This vulnerability affects unknown code of the file ?r=diary/default/del of the component Delete Logs Handler. The manipulation leads to sql injection. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. VDB-238630 is the identifier assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/wudidike/CVE-2023-4741](https://github.com/wudidike/CVE-2023-4741) :  ![starts](https://img.shields.io/github/stars/wudidike/CVE-2023-4741.svg) ![forks](https://img.shields.io/github/forks/wudidike/CVE-2023-4741.svg)

## CVE-2023-4740
 A vulnerability, which was classified as critical, was found in IBOS OA 4.5.5. This affects an unknown part of the file ?r=email/api/delDraft&archiveId=0 of the component Delete Draft Handler. The manipulation leads to sql injection. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The identifier VDB-238629 was assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/LucasVanHaaren/CVE-2023-47400](https://github.com/LucasVanHaaren/CVE-2023-47400) :  ![starts](https://img.shields.io/github/stars/LucasVanHaaren/CVE-2023-47400.svg) ![forks](https://img.shields.io/github/forks/LucasVanHaaren/CVE-2023-47400.svg)

## CVE-2023-4699
 Missing Authentication for Critical Function vulnerability in Mitsubishi Electric Corporation MELSEC-F Series CPU modules, MELSEC iQ-F Series, MELSEC iQ-R series CPU modules, MELSEC iQ-R series, MELSEC iQ-L series, MELSEC Q series, MELSEC-L series, Mitsubishi Electric CNC M800V/M80V series, Mitsubishi Electric CNC M800/M80/E80 series and Mitsubishi Electric CNC M700V/M70V/E70 series allows a remote unauthenticated attacker to execute arbitrary commands by sending specific packets to the affected products. This could lead to disclose or tamper with information by reading or writing control programs, or cause a denial-of-service (DoS) condition on the products by resetting the memory contents of the products to factory settings or resetting the products remotely.



- [https://github.com/Scottzxor/Citrix-Bleed-Buffer-Overread-Demo](https://github.com/Scottzxor/Citrix-Bleed-Buffer-Overread-Demo) :  ![starts](https://img.shields.io/github/stars/Scottzxor/Citrix-Bleed-Buffer-Overread-Demo.svg) ![forks](https://img.shields.io/github/forks/Scottzxor/Citrix-Bleed-Buffer-Overread-Demo.svg)

## CVE-2023-4698
 Improper Input Validation in GitHub repository usememos/memos prior to 0.13.2.



- [https://github.com/mnqazi/CVE-2023-4698](https://github.com/mnqazi/CVE-2023-4698) :  ![starts](https://img.shields.io/github/stars/mnqazi/CVE-2023-4698.svg) ![forks](https://img.shields.io/github/forks/mnqazi/CVE-2023-4698.svg)

## CVE-2023-4696
 Improper Access Control in GitHub repository usememos/memos prior to 0.13.2.



- [https://github.com/mnqazi/CVE-2023-4696](https://github.com/mnqazi/CVE-2023-4696) :  ![starts](https://img.shields.io/github/stars/mnqazi/CVE-2023-4696.svg) ![forks](https://img.shields.io/github/forks/mnqazi/CVE-2023-4696.svg)

## CVE-2023-4683
 NULL Pointer Dereference in GitHub repository gpac/gpac prior to 2.3-DEV.



- [https://github.com/Songg45/CVE-2023-4683-Test](https://github.com/Songg45/CVE-2023-4683-Test) :  ![starts](https://img.shields.io/github/stars/Songg45/CVE-2023-4683-Test.svg) ![forks](https://img.shields.io/github/forks/Songg45/CVE-2023-4683-Test.svg)

## CVE-2023-4636
 The WordPress File Sharing Plugin plugin for WordPress is vulnerable to Stored Cross-Site Scripting via admin settings in versions up to, and including, 2.0.3 due to insufficient input sanitization and output escaping. This makes it possible for authenticated attackers, with administrator-level permissions and above, to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page. This only affects multi-site installations and installations where unfiltered_html has been disabled.



- [https://github.com/ThatNotEasy/CVE-2023-4636](https://github.com/ThatNotEasy/CVE-2023-4636) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2023-4636.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2023-4636.svg)

## CVE-2023-4634
 The Media Library Assistant plugin for WordPress is vulnerable to Local File Inclusion and Remote Code Execution in versions up to, and including, 3.09. This is due to insufficient controls on file paths being supplied to the 'mla_stream_file' parameter from the ~/includes/mla-stream-image.php file, where images are processed via Imagick(). This makes it possible for unauthenticated attackers to supply files via FTP that will make directory lists, local file inclusion, and remote code execution possible.



- [https://github.com/Patrowl/CVE-2023-4634](https://github.com/Patrowl/CVE-2023-4634) :  ![starts](https://img.shields.io/github/stars/Patrowl/CVE-2023-4634.svg) ![forks](https://img.shields.io/github/forks/Patrowl/CVE-2023-4634.svg)

## CVE-2023-4631
 The DoLogin Security WordPress plugin before 3.7 uses headers such as the X-Forwarded-For to retrieve the IP address of the request, which could lead to IP spoofing.



- [https://github.com/b0marek/CVE-2023-4631](https://github.com/b0marek/CVE-2023-4631) :  ![starts](https://img.shields.io/github/stars/b0marek/CVE-2023-4631.svg) ![forks](https://img.shields.io/github/forks/b0marek/CVE-2023-4631.svg)

## CVE-2023-4622
 A use-after-free vulnerability in the Linux kernel's af_unix component can be exploited to achieve local privilege escalation.

The unix_stream_sendpage() function tries to add data to the last skb in the peer's recv queue without locking the queue. Thus there is a race where unix_stream_sendpage() could access an skb locklessly that is being released by garbage collection, resulting in use-after-free.

We recommend upgrading past commit 790c2f9d15b594350ae9bca7b236f2b1859de02c.



- [https://github.com/0range1337/CVE-CVE-2023-4622](https://github.com/0range1337/CVE-CVE-2023-4622) :  ![starts](https://img.shields.io/github/stars/0range1337/CVE-CVE-2023-4622.svg) ![forks](https://img.shields.io/github/forks/0range1337/CVE-CVE-2023-4622.svg)

## CVE-2023-4596
 The Forminator plugin for WordPress is vulnerable to arbitrary file uploads due to file type validation occurring after a file has been uploaded to the server in the upload_post_image() function in versions up to, and including, 1.24.6. This makes it possible for unauthenticated attackers to upload arbitrary files on the affected site's server which may make remote code execution possible.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/E1A/CVE-2023-4596](https://github.com/E1A/CVE-2023-4596) :  ![starts](https://img.shields.io/github/stars/E1A/CVE-2023-4596.svg) ![forks](https://img.shields.io/github/forks/E1A/CVE-2023-4596.svg)

- [https://github.com/X-Projetion/CVE-2023-4596-OpenSSH-Multi-Checker](https://github.com/X-Projetion/CVE-2023-4596-OpenSSH-Multi-Checker) :  ![starts](https://img.shields.io/github/stars/X-Projetion/CVE-2023-4596-OpenSSH-Multi-Checker.svg) ![forks](https://img.shields.io/github/forks/X-Projetion/CVE-2023-4596-OpenSSH-Multi-Checker.svg)

- [https://github.com/X-Projetion/CVE-2023-4596-Vulnerable-Exploit-and-Checker-Version](https://github.com/X-Projetion/CVE-2023-4596-Vulnerable-Exploit-and-Checker-Version) :  ![starts](https://img.shields.io/github/stars/X-Projetion/CVE-2023-4596-Vulnerable-Exploit-and-Checker-Version.svg) ![forks](https://img.shields.io/github/forks/X-Projetion/CVE-2023-4596-Vulnerable-Exploit-and-Checker-Version.svg)

## CVE-2023-4568
 PaperCut NG allows for unauthenticated XMLRPC commands to be run by default. Versions 22.0.12 and below are confirmed to be affected, but later versions may also be affected due to lack of a vendor supplied patch.



- [https://github.com/Cappricio-Securities/CVE-2023-4568](https://github.com/Cappricio-Securities/CVE-2023-4568) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2023-4568.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2023-4568.svg)

## CVE-2023-4549
 The DoLogin Security WordPress plugin before 3.7 does not properly sanitize IP addresses coming from the X-Forwarded-For header, which can be used by attackers to conduct Stored XSS attacks via WordPress' login form.



- [https://github.com/b0marek/CVE-2023-4549](https://github.com/b0marek/CVE-2023-4549) :  ![starts](https://img.shields.io/github/stars/b0marek/CVE-2023-4549.svg) ![forks](https://img.shields.io/github/forks/b0marek/CVE-2023-4549.svg)

## CVE-2023-4542
 A vulnerability was found in D-Link DAR-8000-10 up to 20230809. It has been classified as critical. This affects an unknown part of the file /app/sys1.php. The manipulation of the argument cmd with the input id leads to os command injection. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-238047. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/PumpkinBridge/CVE-2023-4542](https://github.com/PumpkinBridge/CVE-2023-4542) :  ![starts](https://img.shields.io/github/stars/PumpkinBridge/CVE-2023-4542.svg) ![forks](https://img.shields.io/github/forks/PumpkinBridge/CVE-2023-4542.svg)

## CVE-2023-4504
 Due to failure in validating the length provided by an attacker-crafted PPD PostScript document, CUPS and libppd are susceptible to a heap-based buffer overflow and possibly code execution. This issue has been fixed in CUPS version 2.4.7, released in September of 2023.



- [https://github.com/djjohnson565/CUPS-Exploit](https://github.com/djjohnson565/CUPS-Exploit) :  ![starts](https://img.shields.io/github/stars/djjohnson565/CUPS-Exploit.svg) ![forks](https://img.shields.io/github/forks/djjohnson565/CUPS-Exploit.svg)

## CVE-2023-4460
 The Uploading SVG, WEBP and ICO files WordPress plugin through 1.2.1 does not sanitise uploaded SVG files, which could allow users with a role as low as Author to upload a malicious SVG containing XSS payloads.



- [https://github.com/0xn4d/poc-cve-xss-uploading-svg](https://github.com/0xn4d/poc-cve-xss-uploading-svg) :  ![starts](https://img.shields.io/github/stars/0xn4d/poc-cve-xss-uploading-svg.svg) ![forks](https://img.shields.io/github/forks/0xn4d/poc-cve-xss-uploading-svg.svg)

## CVE-2023-4450
 A vulnerability was found in jeecgboot JimuReport up to 1.6.0. It has been declared as critical. Affected by this vulnerability is an unknown functionality of the component Template Handler. The manipulation leads to injection. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. Upgrading to version 1.6.1 is able to address this issue. It is recommended to upgrade the affected component. The associated identifier of this vulnerability is VDB-237571.



- [https://github.com/ilikeoyt/CVE-2023-4450-Attack](https://github.com/ilikeoyt/CVE-2023-4450-Attack) :  ![starts](https://img.shields.io/github/stars/ilikeoyt/CVE-2023-4450-Attack.svg) ![forks](https://img.shields.io/github/forks/ilikeoyt/CVE-2023-4450-Attack.svg)

## CVE-2023-4427
 Out of bounds memory access in V8 in Google Chrome prior to 116.0.5845.110 allowed a remote attacker to perform an out of bounds memory read via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/tianstcht/CVE-2023-4427](https://github.com/tianstcht/CVE-2023-4427) :  ![starts](https://img.shields.io/github/stars/tianstcht/CVE-2023-4427.svg) ![forks](https://img.shields.io/github/forks/tianstcht/CVE-2023-4427.svg)

## CVE-2023-4415
 A vulnerability was found in Ruijie RG-EW1200G 07161417 r483. It has been rated as critical. Affected by this issue is some unknown functionality of the file /api/sys/login. The manipulation leads to improper authentication. The attack may be launched remotely. The exploit has been disclosed to the public and may be used. VDB-237518 is the identifier assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415](https://github.com/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415) :  ![starts](https://img.shields.io/github/stars/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415.svg) ![forks](https://img.shields.io/github/forks/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415.svg)

## CVE-2023-4357
 Insufficient validation of untrusted input in XML in Google Chrome prior to 116.0.5845.96 allowed a remote attacker to bypass file access restrictions via a crafted HTML page. (Chromium security severity: Medium)



- [https://github.com/xcanwin/CVE-2023-4357-Chrome-XXE](https://github.com/xcanwin/CVE-2023-4357-Chrome-XXE) :  ![starts](https://img.shields.io/github/stars/xcanwin/CVE-2023-4357-Chrome-XXE.svg) ![forks](https://img.shields.io/github/forks/xcanwin/CVE-2023-4357-Chrome-XXE.svg)

- [https://github.com/lon5948/CVE-2023-4357-Exploitation](https://github.com/lon5948/CVE-2023-4357-Exploitation) :  ![starts](https://img.shields.io/github/stars/lon5948/CVE-2023-4357-Exploitation.svg) ![forks](https://img.shields.io/github/forks/lon5948/CVE-2023-4357-Exploitation.svg)

- [https://github.com/sunu11/chrome-CVE-2023-4357](https://github.com/sunu11/chrome-CVE-2023-4357) :  ![starts](https://img.shields.io/github/stars/sunu11/chrome-CVE-2023-4357.svg) ![forks](https://img.shields.io/github/forks/sunu11/chrome-CVE-2023-4357.svg)

- [https://github.com/WinnieZy/CVE-2023-4357](https://github.com/WinnieZy/CVE-2023-4357) :  ![starts](https://img.shields.io/github/stars/WinnieZy/CVE-2023-4357.svg) ![forks](https://img.shields.io/github/forks/WinnieZy/CVE-2023-4357.svg)

- [https://github.com/CamillaFranceschini/CVE-2023-4357](https://github.com/CamillaFranceschini/CVE-2023-4357) :  ![starts](https://img.shields.io/github/stars/CamillaFranceschini/CVE-2023-4357.svg) ![forks](https://img.shields.io/github/forks/CamillaFranceschini/CVE-2023-4357.svg)

- [https://github.com/passwa11/CVE-2023-4357-APT-Style-exploitation](https://github.com/passwa11/CVE-2023-4357-APT-Style-exploitation) :  ![starts](https://img.shields.io/github/stars/passwa11/CVE-2023-4357-APT-Style-exploitation.svg) ![forks](https://img.shields.io/github/forks/passwa11/CVE-2023-4357-APT-Style-exploitation.svg)

## CVE-2023-4350
 Inappropriate implementation in Fullscreen in Google Chrome on Android prior to 116.0.5845.96 allowed a remote attacker to potentially spoof the contents of the Omnibox (URL bar) via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/0nyx-hkr/cve-2023-4350](https://github.com/0nyx-hkr/cve-2023-4350) :  ![starts](https://img.shields.io/github/stars/0nyx-hkr/cve-2023-4350.svg) ![forks](https://img.shields.io/github/forks/0nyx-hkr/cve-2023-4350.svg)

## CVE-2023-4300
 The Import XML and RSS Feeds WordPress plugin before 2.1.4 does not filter file extensions for uploaded files, allowing an attacker to upload a malicious PHP file, leading to Remote Code Execution.



- [https://github.com/bde574786/CVE-2023-4300](https://github.com/bde574786/CVE-2023-4300) :  ![starts](https://img.shields.io/github/stars/bde574786/CVE-2023-4300.svg) ![forks](https://img.shields.io/github/forks/bde574786/CVE-2023-4300.svg)

## CVE-2023-4294
 The URL Shortify WordPress plugin before 1.7.6 does not properly escape the value of the referer header, thus allowing an unauthenticated attacker to inject malicious javascript that will trigger in the plugins admin panel with statistics of the created short link.



- [https://github.com/b0marek/CVE-2023-4294](https://github.com/b0marek/CVE-2023-4294) :  ![starts](https://img.shields.io/github/stars/b0marek/CVE-2023-4294.svg) ![forks](https://img.shields.io/github/forks/b0marek/CVE-2023-4294.svg)

## CVE-2023-4281
 This Activity Log WordPress plugin before 2.8.8 retrieves client IP addresses from potentially untrusted headers, allowing an attacker to manipulate its value. This may be used to hide the source of malicious traffic.



- [https://github.com/b0marek/CVE-2023-4281](https://github.com/b0marek/CVE-2023-4281) :  ![starts](https://img.shields.io/github/stars/b0marek/CVE-2023-4281.svg) ![forks](https://img.shields.io/github/forks/b0marek/CVE-2023-4281.svg)

## CVE-2023-4279
 This User Activity Log WordPress plugin before 1.6.7 retrieves client IP addresses from potentially untrusted headers, allowing an attacker to manipulate its value. This may be used to hide the source of malicious traffic.



- [https://github.com/b0marek/CVE-2023-4279](https://github.com/b0marek/CVE-2023-4279) :  ![starts](https://img.shields.io/github/stars/b0marek/CVE-2023-4279.svg) ![forks](https://img.shields.io/github/forks/b0marek/CVE-2023-4279.svg)

## CVE-2023-4278
 The MasterStudy LMS WordPress Plugin WordPress plugin before 3.0.18 does not have proper checks in place during registration allowing anyone to register on the site as an instructor. They can then add courses and/or posts.



- [https://github.com/revan-ar/CVE-2023-4278](https://github.com/revan-ar/CVE-2023-4278) :  ![starts](https://img.shields.io/github/stars/revan-ar/CVE-2023-4278.svg) ![forks](https://img.shields.io/github/forks/revan-ar/CVE-2023-4278.svg)

## CVE-2023-4241
 lol-html can cause panics on certain HTML inputs. Anyone processing arbitrary 3rd party HTML with the library is affected.





- [https://github.com/chenghao-hao/cve-2023-42413](https://github.com/chenghao-hao/cve-2023-42413) :  ![starts](https://img.shields.io/github/stars/chenghao-hao/cve-2023-42413.svg) ![forks](https://img.shields.io/github/forks/chenghao-hao/cve-2023-42413.svg)

## CVE-2023-4226
 Unrestricted file upload in `/main/inc/ajax/work.ajax.php` in Chamilo LMS = v1.11.24 allows authenticated attackers with learner role to obtain remote code execution via uploading of PHP files.



- [https://github.com/SkyW4r33x/CVE-2023-4226](https://github.com/SkyW4r33x/CVE-2023-4226) :  ![starts](https://img.shields.io/github/stars/SkyW4r33x/CVE-2023-4226.svg) ![forks](https://img.shields.io/github/forks/SkyW4r33x/CVE-2023-4226.svg)

- [https://github.com/krishnan-tech/CVE-2023-4226-POC](https://github.com/krishnan-tech/CVE-2023-4226-POC) :  ![starts](https://img.shields.io/github/stars/krishnan-tech/CVE-2023-4226-POC.svg) ![forks](https://img.shields.io/github/forks/krishnan-tech/CVE-2023-4226-POC.svg)

## CVE-2023-4220
 Unrestricted file upload in big file upload functionality in `/main/inc/lib/javascript/bigupload/inc/bigUpload.php` in Chamilo LMS = v1.11.24 allows unauthenticated attackers to perform stored cross-site scripting attacks and obtain remote code execution via uploading of web shell.



- [https://github.com/Ziad-Sakr/Chamilo-CVE-2023-4220-Exploit](https://github.com/Ziad-Sakr/Chamilo-CVE-2023-4220-Exploit) :  ![starts](https://img.shields.io/github/stars/Ziad-Sakr/Chamilo-CVE-2023-4220-Exploit.svg) ![forks](https://img.shields.io/github/forks/Ziad-Sakr/Chamilo-CVE-2023-4220-Exploit.svg)

- [https://github.com/Rai2en/CVE-2023-4220-Chamilo-LMS](https://github.com/Rai2en/CVE-2023-4220-Chamilo-LMS) :  ![starts](https://img.shields.io/github/stars/Rai2en/CVE-2023-4220-Chamilo-LMS.svg) ![forks](https://img.shields.io/github/forks/Rai2en/CVE-2023-4220-Chamilo-LMS.svg)

- [https://github.com/N1ghtfallXxX/CVE-2023-4220](https://github.com/N1ghtfallXxX/CVE-2023-4220) :  ![starts](https://img.shields.io/github/stars/N1ghtfallXxX/CVE-2023-4220.svg) ![forks](https://img.shields.io/github/forks/N1ghtfallXxX/CVE-2023-4220.svg)

- [https://github.com/charlesgargasson/CVE-2023-4220](https://github.com/charlesgargasson/CVE-2023-4220) :  ![starts](https://img.shields.io/github/stars/charlesgargasson/CVE-2023-4220.svg) ![forks](https://img.shields.io/github/forks/charlesgargasson/CVE-2023-4220.svg)

- [https://github.com/Pr1or95/CVE-2023-4220-exploit](https://github.com/Pr1or95/CVE-2023-4220-exploit) :  ![starts](https://img.shields.io/github/stars/Pr1or95/CVE-2023-4220-exploit.svg) ![forks](https://img.shields.io/github/forks/Pr1or95/CVE-2023-4220-exploit.svg)

- [https://github.com/oxapavan/CVE-2023-4220-HTB-PermX](https://github.com/oxapavan/CVE-2023-4220-HTB-PermX) :  ![starts](https://img.shields.io/github/stars/oxapavan/CVE-2023-4220-HTB-PermX.svg) ![forks](https://img.shields.io/github/forks/oxapavan/CVE-2023-4220-HTB-PermX.svg)

- [https://github.com/dollarboysushil/Chamilo-LMS-Unauthenticated-File-Upload-CVE-2023-4220](https://github.com/dollarboysushil/Chamilo-LMS-Unauthenticated-File-Upload-CVE-2023-4220) :  ![starts](https://img.shields.io/github/stars/dollarboysushil/Chamilo-LMS-Unauthenticated-File-Upload-CVE-2023-4220.svg) ![forks](https://img.shields.io/github/forks/dollarboysushil/Chamilo-LMS-Unauthenticated-File-Upload-CVE-2023-4220.svg)

- [https://github.com/krishnan-tech/CVE-2023-4226-POC](https://github.com/krishnan-tech/CVE-2023-4226-POC) :  ![starts](https://img.shields.io/github/stars/krishnan-tech/CVE-2023-4226-POC.svg) ![forks](https://img.shields.io/github/forks/krishnan-tech/CVE-2023-4226-POC.svg)

- [https://github.com/nr4x4/CVE-2023-4220](https://github.com/nr4x4/CVE-2023-4220) :  ![starts](https://img.shields.io/github/stars/nr4x4/CVE-2023-4220.svg) ![forks](https://img.shields.io/github/forks/nr4x4/CVE-2023-4220.svg)

- [https://github.com/gmh5225/CVE-2023-4220](https://github.com/gmh5225/CVE-2023-4220) :  ![starts](https://img.shields.io/github/stars/gmh5225/CVE-2023-4220.svg) ![forks](https://img.shields.io/github/forks/gmh5225/CVE-2023-4220.svg)

- [https://github.com/numaan911098/CVE-2023-4220](https://github.com/numaan911098/CVE-2023-4220) :  ![starts](https://img.shields.io/github/stars/numaan911098/CVE-2023-4220.svg) ![forks](https://img.shields.io/github/forks/numaan911098/CVE-2023-4220.svg)

- [https://github.com/HO4XXX/cve-2023-4220-poc](https://github.com/HO4XXX/cve-2023-4220-poc) :  ![starts](https://img.shields.io/github/stars/HO4XXX/cve-2023-4220-poc.svg) ![forks](https://img.shields.io/github/forks/HO4XXX/cve-2023-4220-poc.svg)

- [https://github.com/Al3xGD/CVE-2023-4220-Exploit](https://github.com/Al3xGD/CVE-2023-4220-Exploit) :  ![starts](https://img.shields.io/github/stars/Al3xGD/CVE-2023-4220-Exploit.svg) ![forks](https://img.shields.io/github/forks/Al3xGD/CVE-2023-4220-Exploit.svg)

- [https://github.com/B1TC0R3/CVE-2023-4220-PoC](https://github.com/B1TC0R3/CVE-2023-4220-PoC) :  ![starts](https://img.shields.io/github/stars/B1TC0R3/CVE-2023-4220-PoC.svg) ![forks](https://img.shields.io/github/forks/B1TC0R3/CVE-2023-4220-PoC.svg)

- [https://github.com/charchit-subedi/chamilo-lms-unauthenticated-rce-poc](https://github.com/charchit-subedi/chamilo-lms-unauthenticated-rce-poc) :  ![starts](https://img.shields.io/github/stars/charchit-subedi/chamilo-lms-unauthenticated-rce-poc.svg) ![forks](https://img.shields.io/github/forks/charchit-subedi/chamilo-lms-unauthenticated-rce-poc.svg)

- [https://github.com/m3m0o/chamilo-lms-unauthenticated-big-upload-rce-poc](https://github.com/m3m0o/chamilo-lms-unauthenticated-big-upload-rce-poc) :  ![starts](https://img.shields.io/github/stars/m3m0o/chamilo-lms-unauthenticated-big-upload-rce-poc.svg) ![forks](https://img.shields.io/github/forks/m3m0o/chamilo-lms-unauthenticated-big-upload-rce-poc.svg)

## CVE-2023-4197
 Improper input validation in Dolibarr ERP CRM = v18.0.1 fails to strip certain PHP code from user-supplied input when creating a Website, allowing an attacker to inject and evaluate arbitrary PHP code.



- [https://github.com/alien-keric/CVE-2023-4197](https://github.com/alien-keric/CVE-2023-4197) :  ![starts](https://img.shields.io/github/stars/alien-keric/CVE-2023-4197.svg) ![forks](https://img.shields.io/github/forks/alien-keric/CVE-2023-4197.svg)

## CVE-2023-4174
 A vulnerability has been found in mooSocial mooStore 3.1.6 and classified as problematic. Affected by this vulnerability is an unknown functionality. The manipulation leads to cross site scripting. The attack can be launched remotely. The identifier VDB-236209 was assigned to this vulnerability.



- [https://github.com/d0rb/CVE-2023-4174](https://github.com/d0rb/CVE-2023-4174) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-4174.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-4174.svg)

## CVE-2023-4169
 A vulnerability was found in Ruijie RG-EW1200G 1.0(1)B1P5. It has been declared as critical. Affected by this vulnerability is an unknown functionality of the file /api/sys/set_passwd of the component Administrator Password Handler. The manipulation leads to improper access controls. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The identifier VDB-236185 was assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415](https://github.com/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415) :  ![starts](https://img.shields.io/github/stars/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415.svg) ![forks](https://img.shields.io/github/forks/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415.svg)

## CVE-2023-4166
 A vulnerability has been found in Tongda OA and classified as critical. This vulnerability affects unknown code of the file general/system/seal_manage/dianju/delete_log.php. The manipulation of the argument DELETE_STR leads to sql injection. The exploit has been disclosed to the public and may be used. Upgrading to version 11.10 is able to address this issue. It is recommended to upgrade the affected component. VDB-236182 is the identifier assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/mvpyyds/CVE-2023-4166](https://github.com/mvpyyds/CVE-2023-4166) :  ![starts](https://img.shields.io/github/stars/mvpyyds/CVE-2023-4166.svg) ![forks](https://img.shields.io/github/forks/mvpyyds/CVE-2023-4166.svg)

## CVE-2023-4165
 A vulnerability, which was classified as critical, was found in Tongda OA. This affects an unknown part of the file general/system/seal_manage/iweboffice/delete_seal.php. The manipulation of the argument DELETE_STR leads to sql injection. The exploit has been disclosed to the public and may be used. Upgrading to version 11.10 is able to address this issue. It is recommended to upgrade the affected component. The identifier VDB-236181 was assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/mvpyyds/CVE-2023-4165](https://github.com/mvpyyds/CVE-2023-4165) :  ![starts](https://img.shields.io/github/stars/mvpyyds/CVE-2023-4165.svg) ![forks](https://img.shields.io/github/forks/mvpyyds/CVE-2023-4165.svg)

## CVE-2023-4153
 The BAN Users plugin for WordPress is vulnerable to privilege escalation in versions up to, and including, 1.5.3 due to a missing capability check on the 'w3dev_save_ban_user_settings_callback' function. This makes it possible for authenticated attackers, with minimal permissions such as a subscriber, to modify the plugin settings to access the ban and unban functionality and set the role of the unbanned user.



- [https://github.com/Sh33talUmath/CVE-2023-41534](https://github.com/Sh33talUmath/CVE-2023-41534) :  ![starts](https://img.shields.io/github/stars/Sh33talUmath/CVE-2023-41534.svg) ![forks](https://img.shields.io/github/forks/Sh33talUmath/CVE-2023-41534.svg)

- [https://github.com/Sh33talUmath/CVE-2023-41533](https://github.com/Sh33talUmath/CVE-2023-41533) :  ![starts](https://img.shields.io/github/stars/Sh33talUmath/CVE-2023-41533.svg) ![forks](https://img.shields.io/github/forks/Sh33talUmath/CVE-2023-41533.svg)

- [https://github.com/Sh33talUmath/CVE-2023-41535](https://github.com/Sh33talUmath/CVE-2023-41535) :  ![starts](https://img.shields.io/github/stars/Sh33talUmath/CVE-2023-41535.svg) ![forks](https://img.shields.io/github/forks/Sh33talUmath/CVE-2023-41535.svg)

## CVE-2023-4150
 The User Activity Tracking and Log WordPress plugin before 4.0.9 does not have proper CSRF checks when managing its license, which could allow attackers to make logged in admins update and deactivate the plugin's license via CSRF attacks



- [https://github.com/ASR511-OO7/CVE-2023-41501](https://github.com/ASR511-OO7/CVE-2023-41501) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41501.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41501.svg)

- [https://github.com/ASR511-OO7/CVE-2023-41500](https://github.com/ASR511-OO7/CVE-2023-41500) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41500.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41500.svg)

## CVE-2023-4149
 A vulnerability in the web-based management allows an unauthenticated remote attacker to inject arbitrary system commands and gain full system control. Those commands are executed with root privileges. The vulnerability is located in the user request handling of the web-based management.



- [https://github.com/ASR511-OO7/CVE-2023-41498](https://github.com/ASR511-OO7/CVE-2023-41498) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41498.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41498.svg)

- [https://github.com/ASR511-OO7/CVE-2023-41497](https://github.com/ASR511-OO7/CVE-2023-41497) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41497.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41497.svg)

- [https://github.com/ASR511-OO7/CVE-2023-41499](https://github.com/ASR511-OO7/CVE-2023-41499) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2023-41499.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2023-41499.svg)

## CVE-2023-4147
 A use-after-free flaw was found in the Linux kernel’s Netfilter functionality when adding a rule with NFTA_RULE_CHAIN_ID. This flaw allows a local user to crash or escalate their privileges on the system.



- [https://github.com/murdok1982/Exploit-en-Python-para-CVE-2023-4147](https://github.com/murdok1982/Exploit-en-Python-para-CVE-2023-4147) :  ![starts](https://img.shields.io/github/stars/murdok1982/Exploit-en-Python-para-CVE-2023-4147.svg) ![forks](https://img.shields.io/github/forks/murdok1982/Exploit-en-Python-para-CVE-2023-4147.svg)

## CVE-2023-4128
 ** REJECT ** DO NOT USE THIS CVE RECORD. ConsultIDs: CVE-2023-4206, CVE-2023-4207, CVE-2023-4208.  Reason: This record is a duplicate of CVE-2023-4206, CVE-2023-4207, CVE-2023-4208. Notes: All CVE users should reference CVE-2023-4206, CVE-2023-4207, CVE-2023-4208 instead of this record. All references and descriptions in this record have been removed to prevent accidental usage.



- [https://github.com/Trinadh465/linux-4.1.15_CVE-2023-4128](https://github.com/Trinadh465/linux-4.1.15_CVE-2023-4128) :  ![starts](https://img.shields.io/github/stars/Trinadh465/linux-4.1.15_CVE-2023-4128.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/linux-4.1.15_CVE-2023-4128.svg)

## CVE-2023-3972
 A vulnerability was found in insights-client. This security issue occurs because of insecure file operations or unsafe handling of temporary files and directories that lead to local privilege escalation. Before the insights-client has been registered on the system by root, an unprivileged local user or attacker could create the /var/tmp/insights-client directory (owning the directory with read, write, and execute permissions) on the system. After the insights-client is registered by root, an attacker could then control the directory content that insights are using by putting malicious scripts into it and executing arbitrary code as root (trivially bypassing SELinux protections because insights processes are allowed to disable SELinux system-wide).



- [https://github.com/anky-123/CVE-2023-39725](https://github.com/anky-123/CVE-2023-39725) :  ![starts](https://img.shields.io/github/stars/anky-123/CVE-2023-39725.svg) ![forks](https://img.shields.io/github/forks/anky-123/CVE-2023-39725.svg)

## CVE-2023-3971
 An HTML injection flaw was found in Controller in the user interface settings. This flaw allows an attacker to capture credentials by creating a custom login page by injecting HTML, resulting in a complete compromise.



- [https://github.com/ashangp923/CVE-2023-3971](https://github.com/ashangp923/CVE-2023-3971) :  ![starts](https://img.shields.io/github/stars/ashangp923/CVE-2023-3971.svg) ![forks](https://img.shields.io/github/forks/ashangp923/CVE-2023-3971.svg)

## CVE-2023-3897
 Username enumeration is possible through Bypassing CAPTCHA in On-premise SureMDM Solution on Windows deployment allows attacker to enumerate local user information via error message.

This issue affects SureMDM On-premise: 6.31 and below version



- [https://github.com/jFriedli/CVE-2023-3897](https://github.com/jFriedli/CVE-2023-3897) :  ![starts](https://img.shields.io/github/stars/jFriedli/CVE-2023-3897.svg) ![forks](https://img.shields.io/github/forks/jFriedli/CVE-2023-3897.svg)

## CVE-2023-3882
 A vulnerability, which was classified as critical, has been found in Campcodes Beauty Salon Management System 1.0. Affected by this issue is some unknown functionality of the file /admin/edit-accepted-appointment.php. The manipulation of the argument contactno leads to sql injection. The attack may be launched remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-235244.



- [https://github.com/TraiLeR2/Corsair---DLL-Planting-CVE-2023-38822](https://github.com/TraiLeR2/Corsair---DLL-Planting-CVE-2023-38822) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/Corsair---DLL-Planting-CVE-2023-38822.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/Corsair---DLL-Planting-CVE-2023-38822.svg)

- [https://github.com/TraiLeR2/CoD-MW-Warzone-2---CVE-2023-38821](https://github.com/TraiLeR2/CoD-MW-Warzone-2---CVE-2023-38821) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/CoD-MW-Warzone-2---CVE-2023-38821.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/CoD-MW-Warzone-2---CVE-2023-38821.svg)

- [https://github.com/TraiLeR2/DLL-Planting-Slack-4.33.73-CVE-2023-38820](https://github.com/TraiLeR2/DLL-Planting-Slack-4.33.73-CVE-2023-38820) :  ![starts](https://img.shields.io/github/stars/TraiLeR2/DLL-Planting-Slack-4.33.73-CVE-2023-38820.svg) ![forks](https://img.shields.io/github/forks/TraiLeR2/DLL-Planting-Slack-4.33.73-CVE-2023-38820.svg)

## CVE-2023-3881
 A vulnerability classified as critical was found in Campcodes Beauty Salon Management System 1.0. Affected by this vulnerability is an unknown functionality of the file /admin/forgot-password.php. The manipulation of the argument contactno leads to sql injection. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-235243.



- [https://github.com/AnugiArrawwala/CVE-Research](https://github.com/AnugiArrawwala/CVE-Research) :  ![starts](https://img.shields.io/github/stars/AnugiArrawwala/CVE-Research.svg) ![forks](https://img.shields.io/github/forks/AnugiArrawwala/CVE-Research.svg)

## CVE-2023-3836
 A vulnerability classified as critical was found in Dahua Smart Park Management up to 20230713. This vulnerability affects unknown code of the file /emap/devicePoint_addImgIco?hasSubsystem=true. The manipulation of the argument upload leads to unrestricted upload. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. VDB-235162 is the identifier assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/zh-byte/CVE-2023-3836](https://github.com/zh-byte/CVE-2023-3836) :  ![starts](https://img.shields.io/github/stars/zh-byte/CVE-2023-3836.svg) ![forks](https://img.shields.io/github/forks/zh-byte/CVE-2023-3836.svg)

## CVE-2023-3824
 In PHP version 8.0.* before 8.0.30,  8.1.* before 8.1.22, and 8.2.* before 8.2.8, when loading phar file, while reading PHAR directory entries, insufficient length checking may lead to a stack buffer overflow, leading potentially to memory corruption or RCE.



- [https://github.com/jhonnybonny/CVE-2023-3824](https://github.com/jhonnybonny/CVE-2023-3824) :  ![starts](https://img.shields.io/github/stars/jhonnybonny/CVE-2023-3824.svg) ![forks](https://img.shields.io/github/forks/jhonnybonny/CVE-2023-3824.svg)

- [https://github.com/bluefish3r/poc-cve](https://github.com/bluefish3r/poc-cve) :  ![starts](https://img.shields.io/github/stars/bluefish3r/poc-cve.svg) ![forks](https://img.shields.io/github/forks/bluefish3r/poc-cve.svg)

## CVE-2023-3777
 A use-after-free vulnerability in the Linux kernel's netfilter: nf_tables component can be exploited to achieve local privilege escalation.

When nf_tables_delrule() is flushing table rules, it is not checked whether the chain is bound and the chain's owner rule can also release the objects in certain circumstances.

We recommend upgrading past commit 6eaf41e87a223ae6f8e7a28d6e78384ad7e407f8.



- [https://github.com/jyoti818680/CVE-2023-37779](https://github.com/jyoti818680/CVE-2023-37779) :  ![starts](https://img.shields.io/github/stars/jyoti818680/CVE-2023-37779.svg) ![forks](https://img.shields.io/github/forks/jyoti818680/CVE-2023-37779.svg)

- [https://github.com/jyoti818680/CVE-2023-37778](https://github.com/jyoti818680/CVE-2023-37778) :  ![starts](https://img.shields.io/github/stars/jyoti818680/CVE-2023-37778.svg) ![forks](https://img.shields.io/github/forks/jyoti818680/CVE-2023-37778.svg)

## CVE-2023-3722
 An OS command injection vulnerability was found in the Avaya Aura Device Services Web application which could allow remote code execution as the Web server user via a malicious uploaded file. This issue affects Avaya Aura Device Services version 8.1.4.0 and earlier.



- [https://github.com/pizza-power/CVE-2023-3722](https://github.com/pizza-power/CVE-2023-3722) :  ![starts](https://img.shields.io/github/stars/pizza-power/CVE-2023-3722.svg) ![forks](https://img.shields.io/github/forks/pizza-power/CVE-2023-3722.svg)

## CVE-2023-3712
 Files or Directories Accessible to External Parties vulnerability in Honeywell PM43 on 32 bit, ARM (Printer web page modules) allows Privilege Escalation.This issue affects PM43 versions prior to P10.19.050004. 

Update to the latest available firmware version of the respective printers to version MR19.5 (e.g. P10.19.050006).



- [https://github.com/vpxuser/CVE-2023-3712-POC](https://github.com/vpxuser/CVE-2023-3712-POC) :  ![starts](https://img.shields.io/github/stars/vpxuser/CVE-2023-3712-POC.svg) ![forks](https://img.shields.io/github/forks/vpxuser/CVE-2023-3712-POC.svg)

## CVE-2023-3711
 Session Fixation vulnerability in Honeywell PM43 on 32 bit, ARM (Printer web page modules) allows Session Credential Falsification through Prediction.This issue affects PM43 versions prior to P10.19.050004. Update to the latest available firmware version of the respective printers to version MR19.5 (e.g. P10.19.050006).



- [https://github.com/vpxuser/CVE-2023-3711-POC](https://github.com/vpxuser/CVE-2023-3711-POC) :  ![starts](https://img.shields.io/github/stars/vpxuser/CVE-2023-3711-POC.svg) ![forks](https://img.shields.io/github/forks/vpxuser/CVE-2023-3711-POC.svg)

## CVE-2023-3710
 Improper Input Validation vulnerability in Honeywell PM43 on 32 bit, ARM (Printer web page modules) allows Command Injection.This issue affects PM43 versions prior to P10.19.050004. Update to the latest available firmware version of the respective printers to version MR19.5 (e.g. P10.19.050006).



- [https://github.com/vpxuser/CVE-2023-3710-POC](https://github.com/vpxuser/CVE-2023-3710-POC) :  ![starts](https://img.shields.io/github/stars/vpxuser/CVE-2023-3710-POC.svg) ![forks](https://img.shields.io/github/forks/vpxuser/CVE-2023-3710-POC.svg)

## CVE-2023-3707
 The ActivityPub WordPress plugin before 1.0.0 does not ensure that post contents to be displayed are public and belong to the plugin, allowing any authenticated user, such as subscriber to retrieve the content of arbitrary post (such as draft and private) via an IDOR vector. Password protected posts are not affected by this issue.



- [https://github.com/Hamza0X/CVE-2023-37073](https://github.com/Hamza0X/CVE-2023-37073) :  ![starts](https://img.shields.io/github/stars/Hamza0X/CVE-2023-37073.svg) ![forks](https://img.shields.io/github/forks/Hamza0X/CVE-2023-37073.svg)

## CVE-2023-3640
 A possible unauthorized memory access flaw was found in the Linux kernel's cpu_entry_area mapping of X86 CPU data to memory, where a user may guess the location of exception stacks or other important data. Based on the previous CVE-2023-0597, the 'Randomize per-cpu entry area' feature was implemented in /arch/x86/mm/cpu_entry_area.c, which works through the init_cea_offsets() function when KASLR is enabled. However, despite this feature, there is still a risk of per-cpu entry area leaks. This issue could allow a local user to gain access to some important data with memory in an expected location and potentially escalate their privileges on the system.



- [https://github.com/pray77/CVE-2023-3640](https://github.com/pray77/CVE-2023-3640) :  ![starts](https://img.shields.io/github/stars/pray77/CVE-2023-3640.svg) ![forks](https://img.shields.io/github/forks/pray77/CVE-2023-3640.svg)

## CVE-2023-3519
 Unauthenticated remote code execution



- [https://github.com/BishopFox/CVE-2023-3519](https://github.com/BishopFox/CVE-2023-3519) :  ![starts](https://img.shields.io/github/stars/BishopFox/CVE-2023-3519.svg) ![forks](https://img.shields.io/github/forks/BishopFox/CVE-2023-3519.svg)

- [https://github.com/securekomodo/citrixInspector](https://github.com/securekomodo/citrixInspector) :  ![starts](https://img.shields.io/github/stars/securekomodo/citrixInspector.svg) ![forks](https://img.shields.io/github/forks/securekomodo/citrixInspector.svg)

- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/mandiant/citrix-ioc-scanner-cve-2023-3519](https://github.com/mandiant/citrix-ioc-scanner-cve-2023-3519) :  ![starts](https://img.shields.io/github/stars/mandiant/citrix-ioc-scanner-cve-2023-3519.svg) ![forks](https://img.shields.io/github/forks/mandiant/citrix-ioc-scanner-cve-2023-3519.svg)

- [https://github.com/fox-it/citrix-netscaler-triage](https://github.com/fox-it/citrix-netscaler-triage) :  ![starts](https://img.shields.io/github/stars/fox-it/citrix-netscaler-triage.svg) ![forks](https://img.shields.io/github/forks/fox-it/citrix-netscaler-triage.svg)

- [https://github.com/telekom-security/cve-2023-3519-citrix-scanner](https://github.com/telekom-security/cve-2023-3519-citrix-scanner) :  ![starts](https://img.shields.io/github/stars/telekom-security/cve-2023-3519-citrix-scanner.svg) ![forks](https://img.shields.io/github/forks/telekom-security/cve-2023-3519-citrix-scanner.svg)

- [https://github.com/mr-r3b00t/CVE-2023-3519](https://github.com/mr-r3b00t/CVE-2023-3519) :  ![starts](https://img.shields.io/github/stars/mr-r3b00t/CVE-2023-3519.svg) ![forks](https://img.shields.io/github/forks/mr-r3b00t/CVE-2023-3519.svg)

- [https://github.com/SalehLardhi/CVE-2023-3519](https://github.com/SalehLardhi/CVE-2023-3519) :  ![starts](https://img.shields.io/github/stars/SalehLardhi/CVE-2023-3519.svg) ![forks](https://img.shields.io/github/forks/SalehLardhi/CVE-2023-3519.svg)

- [https://github.com/Chocapikk/CVE-2023-3519](https://github.com/Chocapikk/CVE-2023-3519) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-3519.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-3519.svg)

- [https://github.com/Mohammaddvd/CVE-2023-3519](https://github.com/Mohammaddvd/CVE-2023-3519) :  ![starts](https://img.shields.io/github/stars/Mohammaddvd/CVE-2023-3519.svg) ![forks](https://img.shields.io/github/forks/Mohammaddvd/CVE-2023-3519.svg)

- [https://github.com/rwincey/cve-2023-3519](https://github.com/rwincey/cve-2023-3519) :  ![starts](https://img.shields.io/github/stars/rwincey/cve-2023-3519.svg) ![forks](https://img.shields.io/github/forks/rwincey/cve-2023-3519.svg)

- [https://github.com/KR0N-SECURITY/CVE-2023-3519](https://github.com/KR0N-SECURITY/CVE-2023-3519) :  ![starts](https://img.shields.io/github/stars/KR0N-SECURITY/CVE-2023-3519.svg) ![forks](https://img.shields.io/github/forks/KR0N-SECURITY/CVE-2023-3519.svg)

- [https://github.com/passwa11/CVE-2023-3519](https://github.com/passwa11/CVE-2023-3519) :  ![starts](https://img.shields.io/github/stars/passwa11/CVE-2023-3519.svg) ![forks](https://img.shields.io/github/forks/passwa11/CVE-2023-3519.svg)

- [https://github.com/d0rb/CVE-2023-3519](https://github.com/d0rb/CVE-2023-3519) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-3519.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-3519.svg)

- [https://github.com/JonaNeidhart/CVE-2023-3519-BackdoorCheck](https://github.com/JonaNeidhart/CVE-2023-3519-BackdoorCheck) :  ![starts](https://img.shields.io/github/stars/JonaNeidhart/CVE-2023-3519-BackdoorCheck.svg) ![forks](https://img.shields.io/github/forks/JonaNeidhart/CVE-2023-3519-BackdoorCheck.svg)

## CVE-2023-3462
 HashiCorp's Vault and Vault Enterprise are vulnerable to user enumeration when using the LDAP auth method. An attacker may submit requests of existent and non-existent LDAP users and observe the response from Vault to check if the account is valid on the LDAP server. This vulnerability is fixed in Vault 1.14.1 and 1.13.5.



- [https://github.com/Chinyemba-ck/MOVEit-CVE-2023-34362](https://github.com/Chinyemba-ck/MOVEit-CVE-2023-34362) :  ![starts](https://img.shields.io/github/stars/Chinyemba-ck/MOVEit-CVE-2023-34362.svg) ![forks](https://img.shields.io/github/forks/Chinyemba-ck/MOVEit-CVE-2023-34362.svg)

## CVE-2023-3460
 The Ultimate Member WordPress plugin before 2.6.7 does not prevent visitors from creating user accounts with arbitrary capabilities, effectively allowing attackers to create administrator accounts at will. This is actively being exploited in the wild.



- [https://github.com/gbrsh/CVE-2023-3460](https://github.com/gbrsh/CVE-2023-3460) :  ![starts](https://img.shields.io/github/stars/gbrsh/CVE-2023-3460.svg) ![forks](https://img.shields.io/github/forks/gbrsh/CVE-2023-3460.svg)

- [https://github.com/diego-tella/CVE-2023-3460](https://github.com/diego-tella/CVE-2023-3460) :  ![starts](https://img.shields.io/github/stars/diego-tella/CVE-2023-3460.svg) ![forks](https://img.shields.io/github/forks/diego-tella/CVE-2023-3460.svg)

- [https://github.com/Rajneeshkarya/CVE-2023-3460](https://github.com/Rajneeshkarya/CVE-2023-3460) :  ![starts](https://img.shields.io/github/stars/Rajneeshkarya/CVE-2023-3460.svg) ![forks](https://img.shields.io/github/forks/Rajneeshkarya/CVE-2023-3460.svg)

- [https://github.com/yon3zu/Mass-CVE-2023-3460](https://github.com/yon3zu/Mass-CVE-2023-3460) :  ![starts](https://img.shields.io/github/stars/yon3zu/Mass-CVE-2023-3460.svg) ![forks](https://img.shields.io/github/forks/yon3zu/Mass-CVE-2023-3460.svg)

- [https://github.com/EmadYaY/CVE-2023-3460](https://github.com/EmadYaY/CVE-2023-3460) :  ![starts](https://img.shields.io/github/stars/EmadYaY/CVE-2023-3460.svg) ![forks](https://img.shields.io/github/forks/EmadYaY/CVE-2023-3460.svg)

- [https://github.com/ollie-blue/CVE_2023_3460](https://github.com/ollie-blue/CVE_2023_3460) :  ![starts](https://img.shields.io/github/stars/ollie-blue/CVE_2023_3460.svg) ![forks](https://img.shields.io/github/forks/ollie-blue/CVE_2023_3460.svg)

- [https://github.com/GURJOTEXPERT/CVE-2023-3460](https://github.com/GURJOTEXPERT/CVE-2023-3460) :  ![starts](https://img.shields.io/github/stars/GURJOTEXPERT/CVE-2023-3460.svg) ![forks](https://img.shields.io/github/forks/GURJOTEXPERT/CVE-2023-3460.svg)

- [https://github.com/DiMarcoSK/CVE-2023-3460_POC](https://github.com/DiMarcoSK/CVE-2023-3460_POC) :  ![starts](https://img.shields.io/github/stars/DiMarcoSK/CVE-2023-3460_POC.svg) ![forks](https://img.shields.io/github/forks/DiMarcoSK/CVE-2023-3460_POC.svg)

- [https://github.com/rizqimaulanaa/CVE-2023-3460](https://github.com/rizqimaulanaa/CVE-2023-3460) :  ![starts](https://img.shields.io/github/stars/rizqimaulanaa/CVE-2023-3460.svg) ![forks](https://img.shields.io/github/forks/rizqimaulanaa/CVE-2023-3460.svg)

- [https://github.com/julienbrs/exploit-CVE-2023-3460](https://github.com/julienbrs/exploit-CVE-2023-3460) :  ![starts](https://img.shields.io/github/stars/julienbrs/exploit-CVE-2023-3460.svg) ![forks](https://img.shields.io/github/forks/julienbrs/exploit-CVE-2023-3460.svg)

- [https://github.com/TranKuBao/CVE-2023-3460_FIX](https://github.com/TranKuBao/CVE-2023-3460_FIX) :  ![starts](https://img.shields.io/github/stars/TranKuBao/CVE-2023-3460_FIX.svg) ![forks](https://img.shields.io/github/forks/TranKuBao/CVE-2023-3460_FIX.svg)

## CVE-2023-3458
 A vulnerability was found in SourceCodester Shopping Website 1.0. It has been declared as critical. Affected by this vulnerability is an unknown functionality of the file forgot-password.php. The manipulation of the argument contact leads to sql injection. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-232675.



- [https://github.com/fu2x2000/-CVE-2023-34584](https://github.com/fu2x2000/-CVE-2023-34584) :  ![starts](https://img.shields.io/github/stars/fu2x2000/-CVE-2023-34584.svg) ![forks](https://img.shields.io/github/forks/fu2x2000/-CVE-2023-34584.svg)

## CVE-2023-3452
 The Canto plugin for WordPress is vulnerable to Remote File Inclusion in versions up to, and including, 3.0.4 via the 'wp_abspath' parameter. This allows unauthenticated attackers to include and execute arbitrary remote code on the server, provided that allow_url_include is enabled. Local File Inclusion is also possible, albeit less useful because it requires that the attacker be able to upload a malicious php file via FTP or some other means into a directory readable by the web server.



- [https://github.com/leoanggal1/CVE-2023-3452-PoC](https://github.com/leoanggal1/CVE-2023-3452-PoC) :  ![starts](https://img.shields.io/github/stars/leoanggal1/CVE-2023-3452-PoC.svg) ![forks](https://img.shields.io/github/forks/leoanggal1/CVE-2023-3452-PoC.svg)

## CVE-2023-3450
 A vulnerability was found in Ruijie RG-BCR860 2.5.13 and classified as critical. This issue affects some unknown processing of the component Network Diagnostic Page. The manipulation leads to os command injection. The attack may be initiated remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-232547. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/yuanjinyuyuyu/CVE-2023-3450](https://github.com/yuanjinyuyuyu/CVE-2023-3450) :  ![starts](https://img.shields.io/github/stars/yuanjinyuyuyu/CVE-2023-3450.svg) ![forks](https://img.shields.io/github/forks/yuanjinyuyuyu/CVE-2023-3450.svg)

- [https://github.com/caopengyan/CVE-2023-3450](https://github.com/caopengyan/CVE-2023-3450) :  ![starts](https://img.shields.io/github/stars/caopengyan/CVE-2023-3450.svg) ![forks](https://img.shields.io/github/forks/caopengyan/CVE-2023-3450.svg)

## CVE-2023-3420
 Type Confusion in V8 in Google Chrome prior to 114.0.5735.198 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/paulsery/CVE_2023_3420](https://github.com/paulsery/CVE_2023_3420) :  ![starts](https://img.shields.io/github/stars/paulsery/CVE_2023_3420.svg) ![forks](https://img.shields.io/github/forks/paulsery/CVE_2023_3420.svg)

## CVE-2023-3338
 A null pointer dereference flaw was found in the Linux kernel's DECnet networking protocol. This issue could allow a remote user to crash the system.



- [https://github.com/TurtleARM/CVE-2023-3338-DECPwn](https://github.com/TurtleARM/CVE-2023-3338-DECPwn) :  ![starts](https://img.shields.io/github/stars/TurtleARM/CVE-2023-3338-DECPwn.svg) ![forks](https://img.shields.io/github/forks/TurtleARM/CVE-2023-3338-DECPwn.svg)

## CVE-2023-3306
 A vulnerability was found in Ruijie RG-EW1200G EW_3.0(1)B11P204. It has been declared as critical. This vulnerability affects unknown code of the file app.09df2a9e44ab48766f5f.js of the component Admin Password Handler. The manipulation leads to improper access controls. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. VDB-231802 is the identifier assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415](https://github.com/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415) :  ![starts](https://img.shields.io/github/stars/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415.svg) ![forks](https://img.shields.io/github/forks/thedarknessdied/CVE-2023-4169_CVE-2023-3306_CVE-2023-4415.svg)

## CVE-2023-3269
 A vulnerability exists in the memory management subsystem of the Linux kernel. The lock handling for accessing and updating virtual memory areas (VMAs) is incorrect, leading to use-after-free problems. This issue can be successfully exploited to execute arbitrary kernel code, escalate containers, and gain root privileges.



- [https://github.com/lrh2000/StackRot](https://github.com/lrh2000/StackRot) :  ![starts](https://img.shields.io/github/stars/lrh2000/StackRot.svg) ![forks](https://img.shields.io/github/forks/lrh2000/StackRot.svg)

## CVE-2023-3262
 The Dataprobe iBoot PDU running firmware version 1.43.03312023 or earlier uses hard-coded credentials for all interactions with the internal Postgres database.A malicious agent with the ability to execute operating system commands on the device can leverage this vulnerability to read, modify, or delete arbitrary database records.



- [https://github.com/SanjayRagavendar/Ubuntu-GameOver-Lay](https://github.com/SanjayRagavendar/Ubuntu-GameOver-Lay) :  ![starts](https://img.shields.io/github/stars/SanjayRagavendar/Ubuntu-GameOver-Lay.svg) ![forks](https://img.shields.io/github/forks/SanjayRagavendar/Ubuntu-GameOver-Lay.svg)

## CVE-2023-3244
 The Comments Like Dislike plugin for WordPress is vulnerable to unauthorized modification of data due to a missing capability check on the restore_settings function called via an AJAX action in versions up to, and including, 1.1.9. This makes it possible for authenticated attackers with minimal permissions, such as a subscriber, to reset the plugin's settings. NOTE: After attempting to contact the developer with no response, and reporting this to the WordPress plugin's team 30 days ago we are disclosing this issue as it still is not updated.



- [https://github.com/drnull03/POC-CVE-2023-3244](https://github.com/drnull03/POC-CVE-2023-3244) :  ![starts](https://img.shields.io/github/stars/drnull03/POC-CVE-2023-3244.svg) ![forks](https://img.shields.io/github/forks/drnull03/POC-CVE-2023-3244.svg)

## CVE-2023-3171
 A flaw was found in EAP-7 during deserialization of certain classes, which permits instantiation of HashMap and HashTable with no checks on resources consumed. This issue could allow an attacker to submit malicious requests using these classes, which could eventually exhaust the heap and result in a Denial of Service.



- [https://github.com/HritikThapa7/CVE-2023-31711](https://github.com/HritikThapa7/CVE-2023-31711) :  ![starts](https://img.shields.io/github/stars/HritikThapa7/CVE-2023-31711.svg) ![forks](https://img.shields.io/github/forks/HritikThapa7/CVE-2023-31711.svg)

## CVE-2023-3163
 A vulnerability was found in y_project RuoYi up to 4.7.7. It has been classified as problematic. Affected is the function filterKeyword. The manipulation of the argument value leads to resource consumption. VDB-231090 is the identifier assigned to this vulnerability.



- [https://github.com/George0Papasotiriou/CVE-2023-3163-SQL-Injection-Prevention](https://github.com/George0Papasotiriou/CVE-2023-3163-SQL-Injection-Prevention) :  ![starts](https://img.shields.io/github/stars/George0Papasotiriou/CVE-2023-3163-SQL-Injection-Prevention.svg) ![forks](https://img.shields.io/github/forks/George0Papasotiriou/CVE-2023-3163-SQL-Injection-Prevention.svg)

## CVE-2023-3144
 A vulnerability classified as problematic was found in SourceCodester Online Discussion Forum Site 1.0. Affected by this vulnerability is an unknown functionality of the file admin\posts\manage_post.php. The manipulation of the argument title leads to cross site scripting. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The identifier VDB-231013 was assigned to this vulnerability.



- [https://github.com/MaherAzzouzi/CVE-2023-31443](https://github.com/MaherAzzouzi/CVE-2023-31443) :  ![starts](https://img.shields.io/github/stars/MaherAzzouzi/CVE-2023-31443.svg) ![forks](https://img.shields.io/github/forks/MaherAzzouzi/CVE-2023-31443.svg)

## CVE-2023-3128
 Grafana is validating Azure AD accounts based on the email claim. 

On Azure AD, the profile email field is not unique and can be easily modified. 

This leads to account takeover and authentication bypass when Azure AD OAuth is configured with a multi-tenant app.



- [https://github.com/spyata123/CVE-2023-3128](https://github.com/spyata123/CVE-2023-3128) :  ![starts](https://img.shields.io/github/stars/spyata123/CVE-2023-3128.svg) ![forks](https://img.shields.io/github/forks/spyata123/CVE-2023-3128.svg)

## CVE-2023-3124
 The Elementor Pro plugin for WordPress is vulnerable to unauthorized data modification due to a missing capability check on the update_page_option function in versions up to, and including, 3.11.6. This makes it possible for authenticated attackers with subscriber-level capabilities to update arbitrary site options, which can lead to privilege escalation.



- [https://github.com/AmirWhiteHat/CVE-2023-3124](https://github.com/AmirWhiteHat/CVE-2023-3124) :  ![starts](https://img.shields.io/github/stars/AmirWhiteHat/CVE-2023-3124.svg) ![forks](https://img.shields.io/github/forks/AmirWhiteHat/CVE-2023-3124.svg)

## CVE-2023-3107
 A set of carefully crafted ipv6 packets can trigger an integer overflow in the calculation of a fragment reassembled packet's payload length field. This allows an attacker to trigger a kernel panic, resulting in a denial of service.



- [https://github.com/bugprove/cve-2023-31070](https://github.com/bugprove/cve-2023-31070) :  ![starts](https://img.shields.io/github/stars/bugprove/cve-2023-31070.svg) ![forks](https://img.shields.io/github/forks/bugprove/cve-2023-31070.svg)

## CVE-2023-3079
 Type confusion in V8 in Google Chrome prior to 114.0.5735.110 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/mistymntncop/CVE-2023-3079](https://github.com/mistymntncop/CVE-2023-3079) :  ![starts](https://img.shields.io/github/stars/mistymntncop/CVE-2023-3079.svg) ![forks](https://img.shields.io/github/forks/mistymntncop/CVE-2023-3079.svg)

## CVE-2023-3076
 The MStore API WordPress plugin before 3.9.9 does not prevent visitors from creating user accounts with the role of their choice via their wholesale REST API endpoint. This is only exploitable if the site owner paid to access the plugin's pro features.



- [https://github.com/im-hanzou/MSAPer](https://github.com/im-hanzou/MSAPer) :  ![starts](https://img.shields.io/github/stars/im-hanzou/MSAPer.svg) ![forks](https://img.shields.io/github/forks/im-hanzou/MSAPer.svg)

## CVE-2023-3047
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in TMT Lockcell allows SQL Injection.This issue affects Lockcell: before 15.





- [https://github.com/Phamchie/CVE-2023-3047](https://github.com/Phamchie/CVE-2023-3047) :  ![starts](https://img.shields.io/github/stars/Phamchie/CVE-2023-3047.svg) ![forks](https://img.shields.io/github/forks/Phamchie/CVE-2023-3047.svg)

- [https://github.com/Kimsovannareth/Phamchie](https://github.com/Kimsovannareth/Phamchie) :  ![starts](https://img.shields.io/github/stars/Kimsovannareth/Phamchie.svg) ![forks](https://img.shields.io/github/forks/Kimsovannareth/Phamchie.svg)

## CVE-2023-3019
 A DMA reentrancy issue leading to a use-after-free error was found in the e1000e NIC emulation code in QEMU. This issue could allow a privileged guest user to crash the QEMU process on the host, resulting in a denial of service.



- [https://github.com/MojithaR/CVE-2023-30190-FOLLINA](https://github.com/MojithaR/CVE-2023-30190-FOLLINA) :  ![starts](https://img.shields.io/github/stars/MojithaR/CVE-2023-30190-FOLLINA.svg) ![forks](https://img.shields.io/github/forks/MojithaR/CVE-2023-30190-FOLLINA.svg)

## CVE-2023-3009
 Cross-site Scripting (XSS) - Stored in GitHub repository nilsteampassnet/teampass prior to 3.0.9.



- [https://github.com/mnqazi/CVE-2023-3009](https://github.com/mnqazi/CVE-2023-3009) :  ![starts](https://img.shields.io/github/stars/mnqazi/CVE-2023-3009.svg) ![forks](https://img.shields.io/github/forks/mnqazi/CVE-2023-3009.svg)

## CVE-2023-3003
 A vulnerability classified as critical was found in SourceCodester Train Station Ticketing System 1.0. Affected by this vulnerability is an unknown functionality of the file manage_prices.php of the component GET Parameter Handler. The manipulation of the argument id leads to sql injection. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-230347.



- [https://github.com/phucodeexp/CVE-2023-30033](https://github.com/phucodeexp/CVE-2023-30033) :  ![starts](https://img.shields.io/github/stars/phucodeexp/CVE-2023-30033.svg) ![forks](https://img.shields.io/github/forks/phucodeexp/CVE-2023-30033.svg)

## CVE-2023-2986
 The Abandoned Cart Lite for WooCommerce plugin for WordPress is vulnerable to authentication bypass in versions up to, and including, 5.14.2. This is due to insufficient encryption on the user being supplied during the abandoned cart link decode through the plugin. This allows unauthenticated attackers to log in as users who have abandoned the cart, who are typically customers. Further security hardening was introduced in version 5.15.1 that ensures sites are no longer vulnerable through historical check-out links, and additional hardening was introduced in version 5.15.2 that ensured null key values wouldn't permit the authentication bypass.



- [https://github.com/Ayantaker/CVE-2023-2986](https://github.com/Ayantaker/CVE-2023-2986) :  ![starts](https://img.shields.io/github/stars/Ayantaker/CVE-2023-2986.svg) ![forks](https://img.shields.io/github/forks/Ayantaker/CVE-2023-2986.svg)

- [https://github.com/Alucard0x1/CVE-2023-2986](https://github.com/Alucard0x1/CVE-2023-2986) :  ![starts](https://img.shields.io/github/stars/Alucard0x1/CVE-2023-2986.svg) ![forks](https://img.shields.io/github/forks/Alucard0x1/CVE-2023-2986.svg)

## CVE-2023-2982
 The WordPress Social Login and Register (Discord, Google, Twitter, LinkedIn) plugin for WordPress is vulnerable to authentication bypass in versions up to, and including, 7.6.4. This is due to insufficient encryption on the user being supplied during a login validated through the plugin. This makes it possible for unauthenticated attackers to log in as any existing user on the site, such as an administrator, if they know the email address associated with that user. This was partially patched in version 7.6.4 and fully patched in version 7.6.5.



- [https://github.com/RandomRobbieBF/CVE-2023-2982](https://github.com/RandomRobbieBF/CVE-2023-2982) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-2982.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-2982.svg)

- [https://github.com/H4K6/CVE-2023-2982-POC](https://github.com/H4K6/CVE-2023-2982-POC) :  ![starts](https://img.shields.io/github/stars/H4K6/CVE-2023-2982-POC.svg) ![forks](https://img.shields.io/github/forks/H4K6/CVE-2023-2982-POC.svg)

- [https://github.com/wshinkle/CVE-2023-2982](https://github.com/wshinkle/CVE-2023-2982) :  ![starts](https://img.shields.io/github/stars/wshinkle/CVE-2023-2982.svg) ![forks](https://img.shields.io/github/forks/wshinkle/CVE-2023-2982.svg)

- [https://github.com/LoaiEsam37/CVE-2023-2982](https://github.com/LoaiEsam37/CVE-2023-2982) :  ![starts](https://img.shields.io/github/stars/LoaiEsam37/CVE-2023-2982.svg) ![forks](https://img.shields.io/github/forks/LoaiEsam37/CVE-2023-2982.svg)

## CVE-2023-2951
 A vulnerability classified as critical has been found in code-projects Bus Dispatch and Information System 1.0. Affected is an unknown function of the file delete_bus.php. The manipulation of the argument busid leads to sql injection. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-230112.



- [https://github.com/Spr1te76/CVE-2023-2951](https://github.com/Spr1te76/CVE-2023-2951) :  ![starts](https://img.shields.io/github/stars/Spr1te76/CVE-2023-2951.svg) ![forks](https://img.shields.io/github/forks/Spr1te76/CVE-2023-2951.svg)

## CVE-2023-2928
 A vulnerability was found in DedeCMS up to 5.7.106. It has been declared as critical. Affected by this vulnerability is an unknown functionality of the file uploads/dede/article_allowurl_edit.php. The manipulation of the argument allurls leads to code injection. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-230083.



- [https://github.com/CN016/DedeCMS-getshell-CVE-2023-2928-](https://github.com/CN016/DedeCMS-getshell-CVE-2023-2928-) :  ![starts](https://img.shields.io/github/stars/CN016/DedeCMS-getshell-CVE-2023-2928-.svg) ![forks](https://img.shields.io/github/forks/CN016/DedeCMS-getshell-CVE-2023-2928-.svg)

## CVE-2023-2916
 The InfiniteWP Client plugin for WordPress is vulnerable to Sensitive Information Exposure in versions up to, and including, 1.11.1 via the 'admin_notice' function. This can allow authenticated attackers with subscriber-level permissions or above to extract sensitive data including configuration. It can only be exploited if the plugin has not been configured yet. If combined with another arbitrary plugin installation and activation vulnerability, it may be possible to connect a site to InfiniteWP which would make remote management possible and allow for elevation of privileges.



- [https://github.com/d0rb/CVE-2023-2916](https://github.com/d0rb/CVE-2023-2916) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2023-2916.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2023-2916.svg)

## CVE-2023-2877
 The Formidable Forms WordPress plugin before 6.3.1 does not adequately authorize the user or validate the plugin URL in its functionality for installing add-ons. This allows a user with a role as low as Subscriber to install and activate arbitrary plugins of arbitrary versions from the WordPress.org plugin repository onto the site, leading to Remote Code Execution.



- [https://github.com/RandomRobbieBF/CVE-2023-2877](https://github.com/RandomRobbieBF/CVE-2023-2877) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-2877.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-2877.svg)

## CVE-2023-2868
 A remote command injection vulnerability exists in the Barracuda Email Security Gateway (appliance form factor only) product effecting versions 5.1.3.001-9.2.0.006. The vulnerability arises out of a failure to comprehensively sanitize the processing of .tar file (tape archives). The vulnerability stems from incomplete input validation of a user-supplied .tar file as it pertains to the names of the files contained within the archive. As a consequence, a remote attacker can specifically format these file names in a particular manner that will result in remotely executing a system command through Perl's qx operator with the privileges of the Email Security Gateway product. This issue was fixed as part of BNSF-36456 patch. This patch was automatically applied to all customer appliances.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/cfielding-r7/poc-cve-2023-2868](https://github.com/cfielding-r7/poc-cve-2023-2868) :  ![starts](https://img.shields.io/github/stars/cfielding-r7/poc-cve-2023-2868.svg) ![forks](https://img.shields.io/github/forks/cfielding-r7/poc-cve-2023-2868.svg)

- [https://github.com/cashapp323232/CVE-2023-2868CVE-2023-2868](https://github.com/cashapp323232/CVE-2023-2868CVE-2023-2868) :  ![starts](https://img.shields.io/github/stars/cashapp323232/CVE-2023-2868CVE-2023-2868.svg) ![forks](https://img.shields.io/github/forks/cashapp323232/CVE-2023-2868CVE-2023-2868.svg)

- [https://github.com/krmxd/CVE-2023-2868](https://github.com/krmxd/CVE-2023-2868) :  ![starts](https://img.shields.io/github/stars/krmxd/CVE-2023-2868.svg) ![forks](https://img.shields.io/github/forks/krmxd/CVE-2023-2868.svg)

## CVE-2023-2859
 Code Injection in GitHub repository nilsteampassnet/teampass prior to 3.0.9.



- [https://github.com/mnqazi/CVE-2023-2859](https://github.com/mnqazi/CVE-2023-2859) :  ![starts](https://img.shields.io/github/stars/mnqazi/CVE-2023-2859.svg) ![forks](https://img.shields.io/github/forks/mnqazi/CVE-2023-2859.svg)

## CVE-2023-2833
 The ReviewX plugin for WordPress is vulnerable to privilege escalation in versions up to, and including, 1.6.13 due to insufficient restriction on the 'rx_set_screen_options' function. This makes it possible for authenticated attackers, with minimal permissions such as a subscriber, to modify their user role by supplying the 'wp_screen_options[option]' and 'wp_screen_options[value]' parameters during a screen option update.



- [https://github.com/Alucard0x1/CVE-2023-2833](https://github.com/Alucard0x1/CVE-2023-2833) :  ![starts](https://img.shields.io/github/stars/Alucard0x1/CVE-2023-2833.svg) ![forks](https://img.shields.io/github/forks/Alucard0x1/CVE-2023-2833.svg)

## CVE-2023-2825
 An issue has been discovered in GitLab CE/EE affecting only version 16.0.0. An unauthenticated malicious user can use a path traversal vulnerability to read arbitrary files on the server when an attachment exists in a public project nested within at least five groups.



- [https://github.com/Occamsec/CVE-2023-2825](https://github.com/Occamsec/CVE-2023-2825) :  ![starts](https://img.shields.io/github/stars/Occamsec/CVE-2023-2825.svg) ![forks](https://img.shields.io/github/forks/Occamsec/CVE-2023-2825.svg)

- [https://github.com/yuimarudev/CVE-2023-2825](https://github.com/yuimarudev/CVE-2023-2825) :  ![starts](https://img.shields.io/github/stars/yuimarudev/CVE-2023-2825.svg) ![forks](https://img.shields.io/github/forks/yuimarudev/CVE-2023-2825.svg)

- [https://github.com/cc3305/CVE-2023-2825](https://github.com/cc3305/CVE-2023-2825) :  ![starts](https://img.shields.io/github/stars/cc3305/CVE-2023-2825.svg) ![forks](https://img.shields.io/github/forks/cc3305/CVE-2023-2825.svg)

- [https://github.com/alej6/MassCyberCenter-Mentorship-Project-](https://github.com/alej6/MassCyberCenter-Mentorship-Project-) :  ![starts](https://img.shields.io/github/stars/alej6/MassCyberCenter-Mentorship-Project-.svg) ![forks](https://img.shields.io/github/forks/alej6/MassCyberCenter-Mentorship-Project-.svg)

- [https://github.com/Rubikcuv5/CVE-2023-2825](https://github.com/Rubikcuv5/CVE-2023-2825) :  ![starts](https://img.shields.io/github/stars/Rubikcuv5/CVE-2023-2825.svg) ![forks](https://img.shields.io/github/forks/Rubikcuv5/CVE-2023-2825.svg)

- [https://github.com/caopengyan/CVE-2023-2825](https://github.com/caopengyan/CVE-2023-2825) :  ![starts](https://img.shields.io/github/stars/caopengyan/CVE-2023-2825.svg) ![forks](https://img.shields.io/github/forks/caopengyan/CVE-2023-2825.svg)

- [https://github.com/Tornad0007/CVE-2023-2825-Gitlab](https://github.com/Tornad0007/CVE-2023-2825-Gitlab) :  ![starts](https://img.shields.io/github/stars/Tornad0007/CVE-2023-2825-Gitlab.svg) ![forks](https://img.shields.io/github/forks/Tornad0007/CVE-2023-2825-Gitlab.svg)

## CVE-2023-2822
 A vulnerability was found in Ellucian Ethos Identity up to 5.10.5. It has been classified as problematic. Affected is an unknown function of the file /cas/logout. The manipulation of the argument url leads to cross site scripting. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. Upgrading to version 5.10.6 is able to address this issue. It is recommended to upgrade the affected component. The identifier of this vulnerability is VDB-229596.



- [https://github.com/cberman/CVE-2023-2822-demo](https://github.com/cberman/CVE-2023-2822-demo) :  ![starts](https://img.shields.io/github/stars/cberman/CVE-2023-2822-demo.svg) ![forks](https://img.shields.io/github/forks/cberman/CVE-2023-2822-demo.svg)

## CVE-2023-2744
 The ERP WordPress plugin before 1.12.4 does not properly sanitise and escape the `type` parameter in the `erp/v1/accounting/v1/people` REST API endpoint before using it in a SQL statement, leading to a SQL injection exploitable by high privilege users such as admin.



- [https://github.com/pashayogi/CVE-2023-2744](https://github.com/pashayogi/CVE-2023-2744) :  ![starts](https://img.shields.io/github/stars/pashayogi/CVE-2023-2744.svg) ![forks](https://img.shields.io/github/forks/pashayogi/CVE-2023-2744.svg)

## CVE-2023-2732
 The MStore API plugin for WordPress is vulnerable to authentication bypass in versions up to, and including, 3.9.2. This is due to insufficient verification on the user being supplied during the add listing REST API request through the plugin. This makes it possible for unauthenticated attackers to log in as any existing user on the site, such as an administrator, if they have access to the user id.



- [https://github.com/RandomRobbieBF/CVE-2023-2732](https://github.com/RandomRobbieBF/CVE-2023-2732) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-2732.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-2732.svg)

- [https://github.com/ThatNotEasy/CVE-2023-2732](https://github.com/ThatNotEasy/CVE-2023-2732) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2023-2732.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2023-2732.svg)

- [https://github.com/Jenderal92/WP-CVE-2023-2732](https://github.com/Jenderal92/WP-CVE-2023-2732) :  ![starts](https://img.shields.io/github/stars/Jenderal92/WP-CVE-2023-2732.svg) ![forks](https://img.shields.io/github/forks/Jenderal92/WP-CVE-2023-2732.svg)

## CVE-2023-2648
 A vulnerability was found in Weaver E-Office 9.5. It has been classified as critical. This affects an unknown part of the file /inc/jquery/uploadify/uploadify.php. The manipulation of the argument Filedata leads to unrestricted upload. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The identifier VDB-228777 was assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/werwolfz/cve-2023-2523-and-cve-2023-2648](https://github.com/werwolfz/cve-2023-2523-and-cve-2023-2648) :  ![starts](https://img.shields.io/github/stars/werwolfz/cve-2023-2523-and-cve-2023-2648.svg) ![forks](https://img.shields.io/github/forks/werwolfz/cve-2023-2523-and-cve-2023-2648.svg)

## CVE-2023-2645
 A vulnerability, which was classified as critical, was found in USR USR-G806 1.0.41. Affected is an unknown function of the component Web Management Page. The manipulation of the argument username/password with the input root leads to use of hard-coded password. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. It is recommended to change the configuration settings. VDB-228774 is the identifier assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/xymbiot-solution/CVE-2023-2645](https://github.com/xymbiot-solution/CVE-2023-2645) :  ![starts](https://img.shields.io/github/stars/xymbiot-solution/CVE-2023-2645.svg) ![forks](https://img.shields.io/github/forks/xymbiot-solution/CVE-2023-2645.svg)

## CVE-2023-2640
 On Ubuntu kernels carrying both c914c0e27eb0 and "UBUNTU: SAUCE: overlayfs: Skip permission checking for trusted.overlayfs.* xattrs", an unprivileged user may set privileged extended attributes on the mounted files, leading them to be set on the upper files without the appropriate security checks.



- [https://github.com/g1vi/CVE-2023-2640-CVE-2023-32629](https://github.com/g1vi/CVE-2023-2640-CVE-2023-32629) :  ![starts](https://img.shields.io/github/stars/g1vi/CVE-2023-2640-CVE-2023-32629.svg) ![forks](https://img.shields.io/github/forks/g1vi/CVE-2023-2640-CVE-2023-32629.svg)

- [https://github.com/ThrynSec/CVE-2023-32629-CVE-2023-2640---POC-Escalation](https://github.com/ThrynSec/CVE-2023-32629-CVE-2023-2640---POC-Escalation) :  ![starts](https://img.shields.io/github/stars/ThrynSec/CVE-2023-32629-CVE-2023-2640---POC-Escalation.svg) ![forks](https://img.shields.io/github/forks/ThrynSec/CVE-2023-32629-CVE-2023-2640---POC-Escalation.svg)

- [https://github.com/luanoliveira350/GameOverlayFS](https://github.com/luanoliveira350/GameOverlayFS) :  ![starts](https://img.shields.io/github/stars/luanoliveira350/GameOverlayFS.svg) ![forks](https://img.shields.io/github/forks/luanoliveira350/GameOverlayFS.svg)

- [https://github.com/OllaPapito/gameoverlay](https://github.com/OllaPapito/gameoverlay) :  ![starts](https://img.shields.io/github/stars/OllaPapito/gameoverlay.svg) ![forks](https://img.shields.io/github/forks/OllaPapito/gameoverlay.svg)

- [https://github.com/k4but0/Ubuntu-LPE](https://github.com/k4but0/Ubuntu-LPE) :  ![starts](https://img.shields.io/github/stars/k4but0/Ubuntu-LPE.svg) ![forks](https://img.shields.io/github/forks/k4but0/Ubuntu-LPE.svg)

- [https://github.com/musorblyat/CVE-2023-2640-CVE-2023-32629](https://github.com/musorblyat/CVE-2023-2640-CVE-2023-32629) :  ![starts](https://img.shields.io/github/stars/musorblyat/CVE-2023-2640-CVE-2023-32629.svg) ![forks](https://img.shields.io/github/forks/musorblyat/CVE-2023-2640-CVE-2023-32629.svg)

- [https://github.com/johnlettman/juju-scripts](https://github.com/johnlettman/juju-scripts) :  ![starts](https://img.shields.io/github/stars/johnlettman/juju-scripts.svg) ![forks](https://img.shields.io/github/forks/johnlettman/juju-scripts.svg)

- [https://github.com/SanjayRagavendar/Ubuntu-GameOver-Lay](https://github.com/SanjayRagavendar/Ubuntu-GameOver-Lay) :  ![starts](https://img.shields.io/github/stars/SanjayRagavendar/Ubuntu-GameOver-Lay.svg) ![forks](https://img.shields.io/github/forks/SanjayRagavendar/Ubuntu-GameOver-Lay.svg)

- [https://github.com/K5LK/CVE-2023-2640-32629](https://github.com/K5LK/CVE-2023-2640-32629) :  ![starts](https://img.shields.io/github/stars/K5LK/CVE-2023-2640-32629.svg) ![forks](https://img.shields.io/github/forks/K5LK/CVE-2023-2640-32629.svg)

- [https://github.com/Nkipohcs/CVE-2023-2640-CVE-2023-32629](https://github.com/Nkipohcs/CVE-2023-2640-CVE-2023-32629) :  ![starts](https://img.shields.io/github/stars/Nkipohcs/CVE-2023-2640-CVE-2023-32629.svg) ![forks](https://img.shields.io/github/forks/Nkipohcs/CVE-2023-2640-CVE-2023-32629.svg)

- [https://github.com/xS9NTX/CVE-2023-32629-CVE-2023-2640-Ubuntu-Privilege-Escalation-POC](https://github.com/xS9NTX/CVE-2023-32629-CVE-2023-2640-Ubuntu-Privilege-Escalation-POC) :  ![starts](https://img.shields.io/github/stars/xS9NTX/CVE-2023-32629-CVE-2023-2640-Ubuntu-Privilege-Escalation-POC.svg) ![forks](https://img.shields.io/github/forks/xS9NTX/CVE-2023-32629-CVE-2023-2640-Ubuntu-Privilege-Escalation-POC.svg)

- [https://github.com/filippo-zullo98/phpMyAdmin-RCE-Exploit-Lab](https://github.com/filippo-zullo98/phpMyAdmin-RCE-Exploit-Lab) :  ![starts](https://img.shields.io/github/stars/filippo-zullo98/phpMyAdmin-RCE-Exploit-Lab.svg) ![forks](https://img.shields.io/github/forks/filippo-zullo98/phpMyAdmin-RCE-Exploit-Lab.svg)

## CVE-2023-2636
 The AN_GradeBook WordPress plugin through 5.0.1 does not properly sanitise and escape a parameter before using it in a SQL statement, leading to a SQL injection exploitable by users with a role as low as subscriber



- [https://github.com/lukinneberg/CVE-2023-2636](https://github.com/lukinneberg/CVE-2023-2636) :  ![starts](https://img.shields.io/github/stars/lukinneberg/CVE-2023-2636.svg) ![forks](https://img.shields.io/github/forks/lukinneberg/CVE-2023-2636.svg)

## CVE-2023-2603
 A vulnerability was found in libcap. This issue occurs in the _libcap_strdup() function and can lead to an integer overflow if the input string is close to 4GiB.



- [https://github.com/Pazhanivelmani/external_libcap-Android10_r33_CVE-2023-2603](https://github.com/Pazhanivelmani/external_libcap-Android10_r33_CVE-2023-2603) :  ![starts](https://img.shields.io/github/stars/Pazhanivelmani/external_libcap-Android10_r33_CVE-2023-2603.svg) ![forks](https://img.shields.io/github/forks/Pazhanivelmani/external_libcap-Android10_r33_CVE-2023-2603.svg)

## CVE-2023-2598
 A flaw was found in the fixed buffer registration code for io_uring (io_sqe_buffer_register in io_uring/rsrc.c) in the Linux kernel that allows out-of-bounds access to physical memory beyond the end of the buffer. This flaw enables full local privilege escalation.



- [https://github.com/ysanatomic/io_uring_LPE-CVE-2023-2598](https://github.com/ysanatomic/io_uring_LPE-CVE-2023-2598) :  ![starts](https://img.shields.io/github/stars/ysanatomic/io_uring_LPE-CVE-2023-2598.svg) ![forks](https://img.shields.io/github/forks/ysanatomic/io_uring_LPE-CVE-2023-2598.svg)

- [https://github.com/SpongeBob-369/CVE-2023-2598](https://github.com/SpongeBob-369/CVE-2023-2598) :  ![starts](https://img.shields.io/github/stars/SpongeBob-369/CVE-2023-2598.svg) ![forks](https://img.shields.io/github/forks/SpongeBob-369/CVE-2023-2598.svg)

- [https://github.com/LLfam/CVE-2023-2598](https://github.com/LLfam/CVE-2023-2598) :  ![starts](https://img.shields.io/github/stars/LLfam/CVE-2023-2598.svg) ![forks](https://img.shields.io/github/forks/LLfam/CVE-2023-2598.svg)

## CVE-2023-2594
 A vulnerability, which was classified as critical, was found in SourceCodester Food Ordering Management System 1.0. Affected is an unknown function of the component Registration. The manipulation of the argument username leads to sql injection. It is possible to launch the attack remotely. The identifier of this vulnerability is VDB-228396.



- [https://github.com/thehackingverse/CVE-2023-2594](https://github.com/thehackingverse/CVE-2023-2594) :  ![starts](https://img.shields.io/github/stars/thehackingverse/CVE-2023-2594.svg) ![forks](https://img.shields.io/github/forks/thehackingverse/CVE-2023-2594.svg)

## CVE-2023-2591
 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') in GitHub repository nilsteampassnet/teampass prior to 3.0.7.



- [https://github.com/mnqazi/CVE-2023-2591](https://github.com/mnqazi/CVE-2023-2591) :  ![starts](https://img.shields.io/github/stars/mnqazi/CVE-2023-2591.svg) ![forks](https://img.shields.io/github/forks/mnqazi/CVE-2023-2591.svg)

## CVE-2023-2579
 The InventoryPress WordPress plugin through 1.7 does not sanitise and escape some of its settings, which could allow users with the role of author and above to perform Stored Cross-Site Scripting attacks.



- [https://github.com/0xn4d/poc-cve-xss-inventory-press-plugin](https://github.com/0xn4d/poc-cve-xss-inventory-press-plugin) :  ![starts](https://img.shields.io/github/stars/0xn4d/poc-cve-xss-inventory-press-plugin.svg) ![forks](https://img.shields.io/github/forks/0xn4d/poc-cve-xss-inventory-press-plugin.svg)

## CVE-2023-2523
 A vulnerability was found in Weaver E-Office 9.5. It has been rated as critical. Affected by this issue is some unknown functionality of the file App/Ajax/ajax.php?action=mobile_upload_save. The manipulation of the argument upload_quwan leads to unrestricted upload. The attack may be launched remotely. The exploit has been disclosed to the public and may be used. VDB-228014 is the identifier assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/Any3ite/CVE-2023-2523](https://github.com/Any3ite/CVE-2023-2523) :  ![starts](https://img.shields.io/github/stars/Any3ite/CVE-2023-2523.svg) ![forks](https://img.shields.io/github/forks/Any3ite/CVE-2023-2523.svg)

- [https://github.com/werwolfz/cve-2023-2523-and-cve-2023-2648](https://github.com/werwolfz/cve-2023-2523-and-cve-2023-2648) :  ![starts](https://img.shields.io/github/stars/werwolfz/cve-2023-2523-and-cve-2023-2648.svg) ![forks](https://img.shields.io/github/forks/werwolfz/cve-2023-2523-and-cve-2023-2648.svg)

## CVE-2023-2520
 A vulnerability was found in Caton Prime 2.1.2.51.e8d7225049(202303031001) and classified as critical. This issue affects some unknown processing of the file cgi-bin/tools_ping.cgi?action=Command of the component Ping Handler. The manipulation of the argument Destination leads to command injection. The attack may be initiated remotely. The associated identifier of this vulnerability is VDB-228011. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/Trackflaw/CVE-2023-25202](https://github.com/Trackflaw/CVE-2023-25202) :  ![starts](https://img.shields.io/github/stars/Trackflaw/CVE-2023-25202.svg) ![forks](https://img.shields.io/github/forks/Trackflaw/CVE-2023-25202.svg)

- [https://github.com/Trackflaw/CVE-2023-25203](https://github.com/Trackflaw/CVE-2023-25203) :  ![starts](https://img.shields.io/github/stars/Trackflaw/CVE-2023-25203.svg) ![forks](https://img.shields.io/github/forks/Trackflaw/CVE-2023-25203.svg)

## CVE-2023-2516
 Cross-site Scripting (XSS) - Stored in GitHub repository nilsteampassnet/teampass prior to 3.0.7.



- [https://github.com/mnqazi/CVE-2023-3009](https://github.com/mnqazi/CVE-2023-3009) :  ![starts](https://img.shields.io/github/stars/mnqazi/CVE-2023-3009.svg) ![forks](https://img.shields.io/github/forks/mnqazi/CVE-2023-3009.svg)

- [https://github.com/mnqazi/CVE-2023-2516](https://github.com/mnqazi/CVE-2023-2516) :  ![starts](https://img.shields.io/github/stars/mnqazi/CVE-2023-2516.svg) ![forks](https://img.shields.io/github/forks/mnqazi/CVE-2023-2516.svg)

## CVE-2023-2470
 The Add to Feedly WordPress plugin through 1.2.11 does not sanitize and escape its settings, allowing high-privilege users such as admin to perform Cross-Site Scripting attacks even when the unfiltered_html capability is disallowed.



- [https://github.com/hatjwe/CVE-2023-24706](https://github.com/hatjwe/CVE-2023-24706) :  ![starts](https://img.shields.io/github/stars/hatjwe/CVE-2023-24706.svg) ![forks](https://img.shields.io/github/forks/hatjwe/CVE-2023-24706.svg)

## CVE-2023-2437
 The UserPro plugin for WordPress is vulnerable to authentication bypass in versions up to, and including, 5.1.1. This is due to insufficient verification on the user being supplied during a Facebook login through the plugin. This makes it possible for unauthenticated attackers to log in as any existing user on the site, such as an administrator, if they have access to the email. An attacker can leverage CVE-2023-2448 and CVE-2023-2446 to get the user's email address to successfully exploit this vulnerability.



- [https://github.com/RxRCoder/CVE-2023-2437](https://github.com/RxRCoder/CVE-2023-2437) :  ![starts](https://img.shields.io/github/stars/RxRCoder/CVE-2023-2437.svg) ![forks](https://img.shields.io/github/forks/RxRCoder/CVE-2023-2437.svg)

## CVE-2023-2410
 A vulnerability has been found in SourceCodester AC Repair and Services System 1.0 and classified as critical. This vulnerability affects unknown code of the file /admin/bookings/view_booking.php. The manipulation of the argument id leads to sql injection. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-227704.



- [https://github.com/badboycxcc/CVE-2023-24100](https://github.com/badboycxcc/CVE-2023-24100) :  ![starts](https://img.shields.io/github/stars/badboycxcc/CVE-2023-24100.svg) ![forks](https://img.shields.io/github/forks/badboycxcc/CVE-2023-24100.svg)

## CVE-2023-2313
 Inappropriate implementation in Sandbox in Google Chrome on Windows prior to 112.0.5615.49 allowed a remote attacker who had compromised the renderer process to perform arbitrary read/write via a malicious file. (Chromium security severity: High)



- [https://github.com/OmarAtallahh/CVE-2023-23138](https://github.com/OmarAtallahh/CVE-2023-23138) :  ![starts](https://img.shields.io/github/stars/OmarAtallahh/CVE-2023-23138.svg) ![forks](https://img.shields.io/github/forks/OmarAtallahh/CVE-2023-23138.svg)

## CVE-2023-2255
 Improper access control in editor components of The Document Foundation LibreOffice allowed an attacker to craft a document that would cause external links to be loaded without prompt. In the affected versions of LibreOffice documents that used "floating frames" linked to external files, would load the contents of those frames without prompting the user for permission to do so. This was inconsistent with the treatment of other linked content in LibreOffice. This issue affects: The Document Foundation LibreOffice 7.4 versions prior to 7.4.7; 7.5 versions prior to 7.5.3.



- [https://github.com/elweth-sec/CVE-2023-2255](https://github.com/elweth-sec/CVE-2023-2255) :  ![starts](https://img.shields.io/github/stars/elweth-sec/CVE-2023-2255.svg) ![forks](https://img.shields.io/github/forks/elweth-sec/CVE-2023-2255.svg)

- [https://github.com/G4sp4rCS/CVE-2023-2255](https://github.com/G4sp4rCS/CVE-2023-2255) :  ![starts](https://img.shields.io/github/stars/G4sp4rCS/CVE-2023-2255.svg) ![forks](https://img.shields.io/github/forks/G4sp4rCS/CVE-2023-2255.svg)

- [https://github.com/SaintMichae64/CVE-2023-2255](https://github.com/SaintMichae64/CVE-2023-2255) :  ![starts](https://img.shields.io/github/stars/SaintMichae64/CVE-2023-2255.svg) ![forks](https://img.shields.io/github/forks/SaintMichae64/CVE-2023-2255.svg)

## CVE-2023-2249
 The wpForo Forum plugin for WordPress is vulnerable to Local File Include, Server-Side Request Forgery, and PHAR Deserialization in versions up to, and including, 2.1.7. This is due to the insecure use of file_get_contents without appropriate verification of the data being supplied to the function. This makes it possible for authenticated attackers, with minimal permissions such as a subscriber, to retrieve the contents of files like wp-config.php hosted on the system, perform a deserialization attack and possibly achieve remote code execution, and make requests to internal services.



- [https://github.com/ixiacom/CVE-2023-2249](https://github.com/ixiacom/CVE-2023-2249) :  ![starts](https://img.shields.io/github/stars/ixiacom/CVE-2023-2249.svg) ![forks](https://img.shields.io/github/forks/ixiacom/CVE-2023-2249.svg)

## CVE-2023-2215
 A vulnerability classified as critical has been found in Campcodes Coffee Shop POS System 1.0. Affected is an unknown function of the file /admin/user/manage_user.php. The manipulation of the argument id leads to sql injection. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-226980.



- [https://github.com/zwxxb/CVE-2023-2215](https://github.com/zwxxb/CVE-2023-2215) :  ![starts](https://img.shields.io/github/stars/zwxxb/CVE-2023-2215.svg) ![forks](https://img.shields.io/github/forks/zwxxb/CVE-2023-2215.svg)

## CVE-2023-2163
 Incorrect verifier pruning in BPF in Linux Kernel =5.4 leads to unsafe
code paths being incorrectly marked as safe, resulting in arbitrary read/write in
kernel memory, lateral privilege escalation, and container escape.



- [https://github.com/letsr00t/CVE-2023-2163](https://github.com/letsr00t/CVE-2023-2163) :  ![starts](https://img.shields.io/github/stars/letsr00t/CVE-2023-2163.svg) ![forks](https://img.shields.io/github/forks/letsr00t/CVE-2023-2163.svg)

## CVE-2023-2123
 The WP Inventory Manager WordPress plugin before 2.1.0.13 does not sanitise and escape a parameter before outputting it back in the page, leading to a Reflected Cross-Site Scripting.



- [https://github.com/0xn4d/poc-cve-xss-encoded-wp-inventory-manager-plugin](https://github.com/0xn4d/poc-cve-xss-encoded-wp-inventory-manager-plugin) :  ![starts](https://img.shields.io/github/stars/0xn4d/poc-cve-xss-encoded-wp-inventory-manager-plugin.svg) ![forks](https://img.shields.io/github/forks/0xn4d/poc-cve-xss-encoded-wp-inventory-manager-plugin.svg)

## CVE-2023-2114
 The NEX-Forms WordPress plugin before 8.4 does not properly escape the `table` parameter, which is populated with user input, before concatenating it to an SQL query.



- [https://github.com/SchmidAlex/nex-forms_SQL-Injection-CVE-2023-2114](https://github.com/SchmidAlex/nex-forms_SQL-Injection-CVE-2023-2114) :  ![starts](https://img.shields.io/github/stars/SchmidAlex/nex-forms_SQL-Injection-CVE-2023-2114.svg) ![forks](https://img.shields.io/github/forks/SchmidAlex/nex-forms_SQL-Injection-CVE-2023-2114.svg)

## CVE-2023-2033
 Type confusion in V8 in Google Chrome prior to 112.0.5615.121 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/mistymntncop/CVE-2023-2033](https://github.com/mistymntncop/CVE-2023-2033) :  ![starts](https://img.shields.io/github/stars/mistymntncop/CVE-2023-2033.svg) ![forks](https://img.shields.io/github/forks/mistymntncop/CVE-2023-2033.svg)

- [https://github.com/sandumjacob/CVE-2023-2033-Analysis](https://github.com/sandumjacob/CVE-2023-2033-Analysis) :  ![starts](https://img.shields.io/github/stars/sandumjacob/CVE-2023-2033-Analysis.svg) ![forks](https://img.shields.io/github/forks/sandumjacob/CVE-2023-2033-Analysis.svg)

- [https://github.com/insoxin/CVE-2023-2033](https://github.com/insoxin/CVE-2023-2033) :  ![starts](https://img.shields.io/github/stars/insoxin/CVE-2023-2033.svg) ![forks](https://img.shields.io/github/forks/insoxin/CVE-2023-2033.svg)

- [https://github.com/tianstcht/CVE-2023-2033](https://github.com/tianstcht/CVE-2023-2033) :  ![starts](https://img.shields.io/github/stars/tianstcht/CVE-2023-2033.svg) ![forks](https://img.shields.io/github/forks/tianstcht/CVE-2023-2033.svg)

- [https://github.com/gretchenfrage/CVE-2023-2033-analysis](https://github.com/gretchenfrage/CVE-2023-2033-analysis) :  ![starts](https://img.shields.io/github/stars/gretchenfrage/CVE-2023-2033-analysis.svg) ![forks](https://img.shields.io/github/forks/gretchenfrage/CVE-2023-2033-analysis.svg)

## CVE-2023-2024
 Improper authentication in OpenBlue Enterprise Manager Data Collector versions prior to 3.2.5.75 allow access to an unauthorized user under certain circumstances.



- [https://github.com/team890/CVE-2023-2024](https://github.com/team890/CVE-2023-2024) :  ![starts](https://img.shields.io/github/stars/team890/CVE-2023-2024.svg) ![forks](https://img.shields.io/github/forks/team890/CVE-2023-2024.svg)

## CVE-2023-2023
 The Custom 404 Pro WordPress plugin before 3.7.3 does not escape some URLs before outputting them in attributes, leading to Reflected Cross-Site Scripting.



- [https://github.com/thatformat/Hvv2023](https://github.com/thatformat/Hvv2023) :  ![starts](https://img.shields.io/github/stars/thatformat/Hvv2023.svg) ![forks](https://img.shields.io/github/forks/thatformat/Hvv2023.svg)

- [https://github.com/druxter-x/PHP-CVE-2023-2023-2640-POC-Escalation](https://github.com/druxter-x/PHP-CVE-2023-2023-2640-POC-Escalation) :  ![starts](https://img.shields.io/github/stars/druxter-x/PHP-CVE-2023-2023-2640-POC-Escalation.svg) ![forks](https://img.shields.io/github/forks/druxter-x/PHP-CVE-2023-2023-2640-POC-Escalation.svg)

## CVE-2023-2008
 A flaw was found in the Linux kernel's udmabuf device driver. The specific flaw exists within a fault handler. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an array. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.



- [https://github.com/bluefrostsecurity/CVE-2023-2008](https://github.com/bluefrostsecurity/CVE-2023-2008) :  ![starts](https://img.shields.io/github/stars/bluefrostsecurity/CVE-2023-2008.svg) ![forks](https://img.shields.io/github/forks/bluefrostsecurity/CVE-2023-2008.svg)

## CVE-2023-2002
 A vulnerability was found in the HCI sockets implementation due to a missing capability check in net/bluetooth/hci_sock.c in the Linux Kernel. This flaw allows an attacker to unauthorized execution of management commands, compromising the confidentiality, integrity, and availability of Bluetooth communication.



- [https://github.com/lrh2000/CVE-2023-2002](https://github.com/lrh2000/CVE-2023-2002) :  ![starts](https://img.shields.io/github/stars/lrh2000/CVE-2023-2002.svg) ![forks](https://img.shields.io/github/forks/lrh2000/CVE-2023-2002.svg)

## CVE-2023-1999
 There exists a use after free/double free in libwebp. An attacker can use the ApplyFiltersAndEncode() function and loop through to free best.bw and assign best = trial pointer. The second loop will then return 0 because of an Out of memory error in VP8 encoder, the pointer is still assigned to trial and the AddressSanitizer will attempt a double free.



- [https://github.com/Pazhanivelmani/webp_Android10_r33_CVE-2023-1999](https://github.com/Pazhanivelmani/webp_Android10_r33_CVE-2023-1999) :  ![starts](https://img.shields.io/github/stars/Pazhanivelmani/webp_Android10_r33_CVE-2023-1999.svg) ![forks](https://img.shields.io/github/forks/Pazhanivelmani/webp_Android10_r33_CVE-2023-1999.svg)

## CVE-2023-1829
 A use-after-free vulnerability in the Linux Kernel traffic control index filter (tcindex) can be exploited to achieve local privilege escalation. The tcindex_delete function which does not properly deactivate filters in case of a perfect hashes while deleting the underlying structure which can later lead to double freeing the structure. A local attacker user can use this vulnerability to elevate its privileges to root.
We recommend upgrading past commit 8c710f75256bb3cf05ac7b1672c82b92c43f3d28.



- [https://github.com/lanleft/CVE-2023-1829](https://github.com/lanleft/CVE-2023-1829) :  ![starts](https://img.shields.io/github/stars/lanleft/CVE-2023-1829.svg) ![forks](https://img.shields.io/github/forks/lanleft/CVE-2023-1829.svg)

## CVE-2023-1773
 A vulnerability was found in Rockoa 2.3.2. It has been declared as critical. This vulnerability affects unknown code of the file webmainConfig.php of the component Configuration File Handler. The manipulation leads to code injection. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. VDB-224674 is the identifier assigned to this vulnerability.



- [https://github.com/CRONUS-Security/xinhu-v2.3.2](https://github.com/CRONUS-Security/xinhu-v2.3.2) :  ![starts](https://img.shields.io/github/stars/CRONUS-Security/xinhu-v2.3.2.svg) ![forks](https://img.shields.io/github/forks/CRONUS-Security/xinhu-v2.3.2.svg)

## CVE-2023-1767
 The Snyk Advisor website (https://snyk.io/advisor/) was vulnerable to a stored XSS prior to 28th March 2023. A feature of Snyk Advisor is to display the contents of a scanned package's Readme on its package health page. An attacker could create a package in NPM with an associated markdown README file containing XSS-able HTML tags. Upon Snyk Advisor importing the package, the XSS would run each time an end user browsed to the package's page on Snyk Advisor.



- [https://github.com/weizman/CVE-2023-1767](https://github.com/weizman/CVE-2023-1767) :  ![starts](https://img.shields.io/github/stars/weizman/CVE-2023-1767.svg) ![forks](https://img.shields.io/github/forks/weizman/CVE-2023-1767.svg)

## CVE-2023-1718
 
Improper file stream access in /desktop_app/file.ajax.php?action=uploadfile in Bitrix24 22.0.300 allows unauthenticated remote attackers to cause denial-of-service via a crafted "tmp_url".









- [https://github.com/jhonnybonny/Bitrix24DoS](https://github.com/jhonnybonny/Bitrix24DoS) :  ![starts](https://img.shields.io/github/stars/jhonnybonny/Bitrix24DoS.svg) ![forks](https://img.shields.io/github/forks/jhonnybonny/Bitrix24DoS.svg)

## CVE-2023-1698
 In multiple products of WAGO a vulnerability allows an unauthenticated, remote attacker to create new users and change the device configuration which can result in unintended behaviour, Denial of Service and full system compromise.



- [https://github.com/Chocapikk/CVE-2023-1698](https://github.com/Chocapikk/CVE-2023-1698) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2023-1698.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2023-1698.svg)

- [https://github.com/thedarknessdied/WAGO-CVE-2023-1698](https://github.com/thedarknessdied/WAGO-CVE-2023-1698) :  ![starts](https://img.shields.io/github/stars/thedarknessdied/WAGO-CVE-2023-1698.svg) ![forks](https://img.shields.io/github/forks/thedarknessdied/WAGO-CVE-2023-1698.svg)

- [https://github.com/deIndra/CVE-2023-1698](https://github.com/deIndra/CVE-2023-1698) :  ![starts](https://img.shields.io/github/stars/deIndra/CVE-2023-1698.svg) ![forks](https://img.shields.io/github/forks/deIndra/CVE-2023-1698.svg)

## CVE-2023-1671
 A pre-auth command injection vulnerability in the warn-proceed handler of Sophos Web Appliance older than version 4.3.10.4 allows execution of arbitrary code.



- [https://github.com/getdrive/PoC](https://github.com/getdrive/PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/PoC.svg)

- [https://github.com/W01fh4cker/CVE-2023-1671-POC](https://github.com/W01fh4cker/CVE-2023-1671-POC) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/CVE-2023-1671-POC.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/CVE-2023-1671-POC.svg)

- [https://github.com/ohnonoyesyes/CVE-2023-1671](https://github.com/ohnonoyesyes/CVE-2023-1671) :  ![starts](https://img.shields.io/github/stars/ohnonoyesyes/CVE-2023-1671.svg) ![forks](https://img.shields.io/github/forks/ohnonoyesyes/CVE-2023-1671.svg)

- [https://github.com/behnamvanda/CVE-2023-1671](https://github.com/behnamvanda/CVE-2023-1671) :  ![starts](https://img.shields.io/github/stars/behnamvanda/CVE-2023-1671.svg) ![forks](https://img.shields.io/github/forks/behnamvanda/CVE-2023-1671.svg)

- [https://github.com/csffs/cve-2023-1671](https://github.com/csffs/cve-2023-1671) :  ![starts](https://img.shields.io/github/stars/csffs/cve-2023-1671.svg) ![forks](https://img.shields.io/github/forks/csffs/cve-2023-1671.svg)

## CVE-2023-1665
 Improper Restriction of Excessive Authentication Attempts in GitHub repository linagora/twake prior to 0.0.0.



- [https://github.com/0xsu3ks/CVE-2023-1665](https://github.com/0xsu3ks/CVE-2023-1665) :  ![starts](https://img.shields.io/github/stars/0xsu3ks/CVE-2023-1665.svg) ![forks](https://img.shields.io/github/forks/0xsu3ks/CVE-2023-1665.svg)

## CVE-2023-1545
 SQL Injection in GitHub repository nilsteampassnet/teampass prior to 3.0.0.23.



- [https://github.com/gunzf0x/CVE-2023-1545](https://github.com/gunzf0x/CVE-2023-1545) :  ![starts](https://img.shields.io/github/stars/gunzf0x/CVE-2023-1545.svg) ![forks](https://img.shields.io/github/forks/gunzf0x/CVE-2023-1545.svg)

## CVE-2023-1521
 On Linux the sccache client can execute arbitrary code with the privileges of a local sccache server, by preloading the code in a shared library passed to LD_PRELOAD.


If the server is run as root (which is the default when installing the  snap package https://snapcraft.io/sccache ), this means a user running the sccache client can get root privileges.



- [https://github.com/rubbxalc/CVE-2023-1521](https://github.com/rubbxalc/CVE-2023-1521) :  ![starts](https://img.shields.io/github/stars/rubbxalc/CVE-2023-1521.svg) ![forks](https://img.shields.io/github/forks/rubbxalc/CVE-2023-1521.svg)

## CVE-2023-1514
 A vulnerability exists in the component RTU500 Scripting interface. When a client connects to a server using TLS, the server presents a certificate. This certificate links a public key to the identity of the service and is signed by a Certification Authority (CA), allowing the client to validate that the remote service can be trusted and is not malicious. If the client does not validate the parameters of the certificate, then attackers could be able to spoof the identity of the service. An attacker could exploit the vulnerability by using faking the identity of a RTU500 device and intercepting the messages initiated via the RTU500 Scripting interface.



- [https://github.com/wsx-rootdeef/CVE-2023-1514-SQL-Injection-Teampass-](https://github.com/wsx-rootdeef/CVE-2023-1514-SQL-Injection-Teampass-) :  ![starts](https://img.shields.io/github/stars/wsx-rootdeef/CVE-2023-1514-SQL-Injection-Teampass-.svg) ![forks](https://img.shields.io/github/forks/wsx-rootdeef/CVE-2023-1514-SQL-Injection-Teampass-.svg)

## CVE-2023-1500
 A vulnerability, which was classified as problematic, has been found in code-projects Simple Art Gallery 1.0. Affected by this issue is some unknown functionality of the file adminHome.php. The manipulation of the argument about_info leads to cross site scripting. The attack may be launched remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-223400.



- [https://github.com/Decemberus/BugHub](https://github.com/Decemberus/BugHub) :  ![starts](https://img.shields.io/github/stars/Decemberus/BugHub.svg) ![forks](https://img.shields.io/github/forks/Decemberus/BugHub.svg)

## CVE-2023-1498
 A vulnerability classified as critical has been found in code-projects Responsive Hotel Site 1.0. Affected is an unknown function of the file messages.php of the component Newsletter Log Handler. The manipulation of the argument title leads to sql injection. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. VDB-223398 is the identifier assigned to this vulnerability.



- [https://github.com/Decemberus/BugHub](https://github.com/Decemberus/BugHub) :  ![starts](https://img.shields.io/github/stars/Decemberus/BugHub.svg) ![forks](https://img.shields.io/github/forks/Decemberus/BugHub.svg)

## CVE-2023-1454
 A vulnerability classified as critical has been found in jeecg-boot 3.5.0. This affects an unknown part of the file jmreport/qurestSql. The manipulation of the argument apiSelectId leads to sql injection. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-223299.



- [https://github.com/Sweelg/CVE-2023-1454-Jeecg-Boot-qurestSql-SQLvuln](https://github.com/Sweelg/CVE-2023-1454-Jeecg-Boot-qurestSql-SQLvuln) :  ![starts](https://img.shields.io/github/stars/Sweelg/CVE-2023-1454-Jeecg-Boot-qurestSql-SQLvuln.svg) ![forks](https://img.shields.io/github/forks/Sweelg/CVE-2023-1454-Jeecg-Boot-qurestSql-SQLvuln.svg)

- [https://github.com/padbergpete47/CVE-2023-1454](https://github.com/padbergpete47/CVE-2023-1454) :  ![starts](https://img.shields.io/github/stars/padbergpete47/CVE-2023-1454.svg) ![forks](https://img.shields.io/github/forks/padbergpete47/CVE-2023-1454.svg)

- [https://github.com/gobysec/CVE-2023-1454](https://github.com/gobysec/CVE-2023-1454) :  ![starts](https://img.shields.io/github/stars/gobysec/CVE-2023-1454.svg) ![forks](https://img.shields.io/github/forks/gobysec/CVE-2023-1454.svg)

- [https://github.com/shad0w0sec/CVE-2023-1454-EXP](https://github.com/shad0w0sec/CVE-2023-1454-EXP) :  ![starts](https://img.shields.io/github/stars/shad0w0sec/CVE-2023-1454-EXP.svg) ![forks](https://img.shields.io/github/forks/shad0w0sec/CVE-2023-1454-EXP.svg)

- [https://github.com/P4x1s/CVE-2023-1454-EXP](https://github.com/P4x1s/CVE-2023-1454-EXP) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2023-1454-EXP.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2023-1454-EXP.svg)

- [https://github.com/cjybao/CVE-2023-1454](https://github.com/cjybao/CVE-2023-1454) :  ![starts](https://img.shields.io/github/stars/cjybao/CVE-2023-1454.svg) ![forks](https://img.shields.io/github/forks/cjybao/CVE-2023-1454.svg)

- [https://github.com/BugFor-Pings/CVE-2023-1454](https://github.com/BugFor-Pings/CVE-2023-1454) :  ![starts](https://img.shields.io/github/stars/BugFor-Pings/CVE-2023-1454.svg) ![forks](https://img.shields.io/github/forks/BugFor-Pings/CVE-2023-1454.svg)

## CVE-2023-1430
 The FluentCRM - Marketing Automation For WordPress  plugin for WordPress is vulnerable to unauthorized modification of data in versions up to, and including, 2.7.40 due to the use of an MD5 hash without a salt to control subscriptions. This makes it possible for unauthenticated attackers to unsubscribe users from lists and manage subscriptions, granted they gain access to any targeted subscribers email address.



- [https://github.com/karlemilnikka/CVE-2023-1430](https://github.com/karlemilnikka/CVE-2023-1430) :  ![starts](https://img.shields.io/github/stars/karlemilnikka/CVE-2023-1430.svg) ![forks](https://img.shields.io/github/forks/karlemilnikka/CVE-2023-1430.svg)

## CVE-2023-1415
 A vulnerability was found in Simple Art Gallery 1.0. It has been declared as critical. This vulnerability affects the function sliderPicSubmit of the file adminHome.php. The manipulation leads to unrestricted upload. The attack can be initiated remotely. VDB-223126 is the identifier assigned to this vulnerability.



- [https://github.com/0xxtoby/CVE-2023-1415](https://github.com/0xxtoby/CVE-2023-1415) :  ![starts](https://img.shields.io/github/stars/0xxtoby/CVE-2023-1415.svg) ![forks](https://img.shields.io/github/forks/0xxtoby/CVE-2023-1415.svg)

## CVE-2023-1389
 TP-Link Archer AX21 (AX1800) firmware versions before 1.1.4 Build 20230219 contained a command injection vulnerability in the country form of the /cgi-bin/luci;stok=/locale endpoint on the web management interface. Specifically, the country parameter of the write operation was not sanitized before being used in a call to popen(), allowing an unauthenticated attacker to inject commands, which would be run as root, with a simple POST request.



- [https://github.com/Voyag3r-Security/CVE-2023-1389](https://github.com/Voyag3r-Security/CVE-2023-1389) :  ![starts](https://img.shields.io/github/stars/Voyag3r-Security/CVE-2023-1389.svg) ![forks](https://img.shields.io/github/forks/Voyag3r-Security/CVE-2023-1389.svg)

- [https://github.com/werwolfz/CVE-2023-1389](https://github.com/werwolfz/CVE-2023-1389) :  ![starts](https://img.shields.io/github/stars/werwolfz/CVE-2023-1389.svg) ![forks](https://img.shields.io/github/forks/werwolfz/CVE-2023-1389.svg)

- [https://github.com/ohnahee/CVE_2023_1389_poc](https://github.com/ohnahee/CVE_2023_1389_poc) :  ![starts](https://img.shields.io/github/stars/ohnahee/CVE_2023_1389_poc.svg) ![forks](https://img.shields.io/github/forks/ohnahee/CVE_2023_1389_poc.svg)

## CVE-2023-1337
 The RapidLoad Power-Up for Autoptimize plugin for WordPress is vulnerable to unauthorized data loss due to a missing capability check on the clear_uucss_logs function in versions up to, and including, 1.7.1. This makes it possible for authenticated attackers with subscriber-level access to delete plugin log files.



- [https://github.com/Penkyzduyi/CVE-2023-1337](https://github.com/Penkyzduyi/CVE-2023-1337) :  ![starts](https://img.shields.io/github/stars/Penkyzduyi/CVE-2023-1337.svg) ![forks](https://img.shields.io/github/forks/Penkyzduyi/CVE-2023-1337.svg)

## CVE-2023-1326
 A privilege escalation attack was found in apport-cli 2.26.0 and earlier which is similar to CVE-2023-26604. If a system is specially configured to allow unprivileged users to run sudo apport-cli, less is configured as the pager, and the terminal size can be set: a local attacker can escalate privilege. It is extremely unlikely that a system administrator would configure sudo to allow unprivileged users to perform this class of exploit.



- [https://github.com/diego-tella/CVE-2023-1326-PoC](https://github.com/diego-tella/CVE-2023-1326-PoC) :  ![starts](https://img.shields.io/github/stars/diego-tella/CVE-2023-1326-PoC.svg) ![forks](https://img.shields.io/github/forks/diego-tella/CVE-2023-1326-PoC.svg)

- [https://github.com/h3x0v3rl0rd/CVE-2023-1326](https://github.com/h3x0v3rl0rd/CVE-2023-1326) :  ![starts](https://img.shields.io/github/stars/h3x0v3rl0rd/CVE-2023-1326.svg) ![forks](https://img.shields.io/github/forks/h3x0v3rl0rd/CVE-2023-1326.svg)

- [https://github.com/Pol-Ruiz/CVE-2023-1326](https://github.com/Pol-Ruiz/CVE-2023-1326) :  ![starts](https://img.shields.io/github/stars/Pol-Ruiz/CVE-2023-1326.svg) ![forks](https://img.shields.io/github/forks/Pol-Ruiz/CVE-2023-1326.svg)

- [https://github.com/cve-2024/CVE-2023-1326-PoC](https://github.com/cve-2024/CVE-2023-1326-PoC) :  ![starts](https://img.shields.io/github/stars/cve-2024/CVE-2023-1326-PoC.svg) ![forks](https://img.shields.io/github/forks/cve-2024/CVE-2023-1326-PoC.svg)

## CVE-2023-1234
 Inappropriate implementation in Intents in Google Chrome on Android prior to 111.0.5563.64 allowed a remote attacker to perform domain spoofing via a crafted HTML page. (Chromium security severity: Low)



- [https://github.com/emotest1/CVE-2023-123456](https://github.com/emotest1/CVE-2023-123456) :  ![starts](https://img.shields.io/github/stars/emotest1/CVE-2023-123456.svg) ![forks](https://img.shields.io/github/forks/emotest1/CVE-2023-123456.svg)

- [https://github.com/Yuri08loveElaina/CVE-2023-1234](https://github.com/Yuri08loveElaina/CVE-2023-1234) :  ![starts](https://img.shields.io/github/stars/Yuri08loveElaina/CVE-2023-1234.svg) ![forks](https://img.shields.io/github/forks/Yuri08loveElaina/CVE-2023-1234.svg)

## CVE-2023-1177
 Path Traversal: '\..\filename' in GitHub repository mlflow/mlflow prior to 2.2.1.





- [https://github.com/hh-hunter/ml-CVE-2023-1177](https://github.com/hh-hunter/ml-CVE-2023-1177) :  ![starts](https://img.shields.io/github/stars/hh-hunter/ml-CVE-2023-1177.svg) ![forks](https://img.shields.io/github/forks/hh-hunter/ml-CVE-2023-1177.svg)

- [https://github.com/SpycioKon/CVE-2023-1177-rebuild](https://github.com/SpycioKon/CVE-2023-1177-rebuild) :  ![starts](https://img.shields.io/github/stars/SpycioKon/CVE-2023-1177-rebuild.svg) ![forks](https://img.shields.io/github/forks/SpycioKon/CVE-2023-1177-rebuild.svg)

- [https://github.com/alphandbelt1/CVE-2023-1177-MLFlow](https://github.com/alphandbelt1/CVE-2023-1177-MLFlow) :  ![starts](https://img.shields.io/github/stars/alphandbelt1/CVE-2023-1177-MLFlow.svg) ![forks](https://img.shields.io/github/forks/alphandbelt1/CVE-2023-1177-MLFlow.svg)

- [https://github.com/paultheal1en/CVE-2023-1177-PoC-reproduce](https://github.com/paultheal1en/CVE-2023-1177-PoC-reproduce) :  ![starts](https://img.shields.io/github/stars/paultheal1en/CVE-2023-1177-PoC-reproduce.svg) ![forks](https://img.shields.io/github/forks/paultheal1en/CVE-2023-1177-PoC-reproduce.svg)

## CVE-2023-1112
 A vulnerability was found in Drag and Drop Multiple File Upload Contact Form 7 5.0.6.1 on WordPress. It has been classified as critical. Affected is an unknown function of the file admin-ajax.php. The manipulation of the argument upload_name leads to relative path traversal. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-222072.



- [https://github.com/Nickguitar/Drag-and-Drop-Multiple-File-Uploader-PRO-Path-Traversal](https://github.com/Nickguitar/Drag-and-Drop-Multiple-File-Uploader-PRO-Path-Traversal) :  ![starts](https://img.shields.io/github/stars/Nickguitar/Drag-and-Drop-Multiple-File-Uploader-PRO-Path-Traversal.svg) ![forks](https://img.shields.io/github/forks/Nickguitar/Drag-and-Drop-Multiple-File-Uploader-PRO-Path-Traversal.svg)

## CVE-2023-1077
 In the Linux kernel, pick_next_rt_entity() may return a type confused entry, not detected by the BUG_ON condition, as the confused entry will not be NULL, but list_head.The buggy error condition would lead to a type confused entry with the list head,which would then be used as a type confused sched_rt_entity,causing memory corruption.



- [https://github.com/RenukaSelvar/kernel_rt_CVE_2023_1077](https://github.com/RenukaSelvar/kernel_rt_CVE_2023_1077) :  ![starts](https://img.shields.io/github/stars/RenukaSelvar/kernel_rt_CVE_2023_1077.svg) ![forks](https://img.shields.io/github/forks/RenukaSelvar/kernel_rt_CVE_2023_1077.svg)

## CVE-2023-0861
 NetModule NSRW web administration interface executes an OS command constructed with unsanitized user input. A successful exploit could allow an authenticated user to execute arbitrary commands with elevated privileges.
This issue affects NSRW: from 4.3.0.0 before 4.3.0.119, from 4.4.0.0 before 4.4.0.118, from 4.6.0.0 before 4.6.0.105, from 4.7.0.0 before 4.7.0.103.





- [https://github.com/seifallahhomrani1/CVE-2023-0861-POC](https://github.com/seifallahhomrani1/CVE-2023-0861-POC) :  ![starts](https://img.shields.io/github/stars/seifallahhomrani1/CVE-2023-0861-POC.svg) ![forks](https://img.shields.io/github/forks/seifallahhomrani1/CVE-2023-0861-POC.svg)

## CVE-2023-0860
 Improper Restriction of Excessive Authentication Attempts in GitHub repository modoboa/modoboa-installer prior to 2.0.4.



- [https://github.com/0xsu3ks/CVE-2023-0860](https://github.com/0xsu3ks/CVE-2023-0860) :  ![starts](https://img.shields.io/github/stars/0xsu3ks/CVE-2023-0860.svg) ![forks](https://img.shields.io/github/forks/0xsu3ks/CVE-2023-0860.svg)

## CVE-2023-0830
 A vulnerability classified as critical has been found in EasyNAS 1.1.0. Affected is the function system of the file /backup.pl. The manipulation leads to os command injection. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. It is recommended to upgrade the affected component.



- [https://github.com/xbz0n/CVE-2023-0830](https://github.com/xbz0n/CVE-2023-0830) :  ![starts](https://img.shields.io/github/stars/xbz0n/CVE-2023-0830.svg) ![forks](https://img.shields.io/github/forks/xbz0n/CVE-2023-0830.svg)

## CVE-2023-0748
 Open Redirect in GitHub repository btcpayserver/btcpayserver prior to 1.7.6.





- [https://github.com/gonzxph/CVE-2023-0748](https://github.com/gonzxph/CVE-2023-0748) :  ![starts](https://img.shields.io/github/stars/gonzxph/CVE-2023-0748.svg) ![forks](https://img.shields.io/github/forks/gonzxph/CVE-2023-0748.svg)

## CVE-2023-0669
 Fortra (formerly, HelpSystems) GoAnywhere MFT suffers from a pre-authentication command injection vulnerability in the License Response Servlet due to deserializing an arbitrary attacker-controlled object. This issue was patched in version 7.1.2.



- [https://github.com/0xf4n9x/CVE-2023-0669](https://github.com/0xf4n9x/CVE-2023-0669) :  ![starts](https://img.shields.io/github/stars/0xf4n9x/CVE-2023-0669.svg) ![forks](https://img.shields.io/github/forks/0xf4n9x/CVE-2023-0669.svg)

- [https://github.com/Avento/CVE-2023-0669](https://github.com/Avento/CVE-2023-0669) :  ![starts](https://img.shields.io/github/stars/Avento/CVE-2023-0669.svg) ![forks](https://img.shields.io/github/forks/Avento/CVE-2023-0669.svg)

- [https://github.com/yosef0x01/CVE-2023-0669-Analysis](https://github.com/yosef0x01/CVE-2023-0669-Analysis) :  ![starts](https://img.shields.io/github/stars/yosef0x01/CVE-2023-0669-Analysis.svg) ![forks](https://img.shields.io/github/forks/yosef0x01/CVE-2023-0669-Analysis.svg)

- [https://github.com/cataliniovita/CVE-2023-0669](https://github.com/cataliniovita/CVE-2023-0669) :  ![starts](https://img.shields.io/github/stars/cataliniovita/CVE-2023-0669.svg) ![forks](https://img.shields.io/github/forks/cataliniovita/CVE-2023-0669.svg)

- [https://github.com/Griffin-01/CVE-2023-0669](https://github.com/Griffin-01/CVE-2023-0669) :  ![starts](https://img.shields.io/github/stars/Griffin-01/CVE-2023-0669.svg) ![forks](https://img.shields.io/github/forks/Griffin-01/CVE-2023-0669.svg)

## CVE-2023-0656
 A Stack-based buffer overflow vulnerability in the SonicOS allows a remote unauthenticated attacker to cause Denial of Service (DoS), which could cause an impacted firewall to crash.



- [https://github.com/BishopFox/CVE-2022-22274_CVE-2023-0656](https://github.com/BishopFox/CVE-2022-22274_CVE-2023-0656) :  ![starts](https://img.shields.io/github/stars/BishopFox/CVE-2022-22274_CVE-2023-0656.svg) ![forks](https://img.shields.io/github/forks/BishopFox/CVE-2022-22274_CVE-2023-0656.svg)

## CVE-2023-0630
 The Slimstat Analytics WordPress plugin before 4.9.3.3 does not prevent subscribers from rendering shortcodes that concatenates attributes directly into an SQL query.



- [https://github.com/RandomRobbieBF/CVE-2023-0630](https://github.com/RandomRobbieBF/CVE-2023-0630) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2023-0630.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2023-0630.svg)

## CVE-2023-0464
 A security vulnerability has been identified in all supported versions

of OpenSSL related to the verification of X.509 certificate chains
that include policy constraints.  Attackers may be able to exploit this
vulnerability by creating a malicious certificate chain that triggers
exponential use of computational resources, leading to a denial-of-service
(DoS) attack on affected systems.

Policy processing is disabled by default but can be enabled by passing
the `-policy' argument to the command line utilities or by calling the
`X509_VERIFY_PARAM_set1_policies()' function.



- [https://github.com/Trinadh465/Openssl_1.1.1g_CVE-2023-0464](https://github.com/Trinadh465/Openssl_1.1.1g_CVE-2023-0464) :  ![starts](https://img.shields.io/github/stars/Trinadh465/Openssl_1.1.1g_CVE-2023-0464.svg) ![forks](https://img.shields.io/github/forks/Trinadh465/Openssl_1.1.1g_CVE-2023-0464.svg)

## CVE-2023-0461
 There is a use-after-free vulnerability in the Linux Kernel which can be exploited to achieve local privilege escalation. To reach the vulnerability kernel configuration flag CONFIG_TLS or CONFIG_XFRM_ESPINTCP has to be configured, but the operation does not require any privilege.

There is a use-after-free bug of icsk_ulp_data of a struct inet_connection_sock.

When CONFIG_TLS is enabled, user can install a tls context (struct tls_context) on a connected tcp socket. The context is not cleared if this socket is disconnected and reused as a listener. If a new socket is created from the listener, the context is inherited and vulnerable.

The setsockopt TCP_ULP operation does not require any privilege.

We recommend upgrading past commit 2c02d41d71f90a5168391b6a5f2954112ba2307c



- [https://github.com/b1nhack/CVE-2023-0461](https://github.com/b1nhack/CVE-2023-0461) :  ![starts](https://img.shields.io/github/stars/b1nhack/CVE-2023-0461.svg) ![forks](https://img.shields.io/github/forks/b1nhack/CVE-2023-0461.svg)

## CVE-2023-0400
 
The protection bypass vulnerability in DLP for Windows 11.9.x is addressed in version 11.10.0. This allowed a local user to bypass DLP controls when uploading sensitive data from a mapped drive into a web email client. Loading from a local driver was correctly prevented. Versions prior to 11.9 correctly detected and blocked the attempted upload of sensitive data.





- [https://github.com/pinpinsec/CVE-2023-0400](https://github.com/pinpinsec/CVE-2023-0400) :  ![starts](https://img.shields.io/github/stars/pinpinsec/CVE-2023-0400.svg) ![forks](https://img.shields.io/github/forks/pinpinsec/CVE-2023-0400.svg)

## CVE-2023-0386
 A flaw was found in the Linux kernel, where unauthorized access to the execution of the setuid file with capabilities was found in the Linux kernel’s OverlayFS subsystem in how a user copies a capable file from a nosuid mount into another mount. This uid mapping bug allows a local user to escalate their privileges on the system.



- [https://github.com/xkaneiki/CVE-2023-0386](https://github.com/xkaneiki/CVE-2023-0386) :  ![starts](https://img.shields.io/github/stars/xkaneiki/CVE-2023-0386.svg) ![forks](https://img.shields.io/github/forks/xkaneiki/CVE-2023-0386.svg)

- [https://github.com/chenaotian/CVE-2023-0386](https://github.com/chenaotian/CVE-2023-0386) :  ![starts](https://img.shields.io/github/stars/chenaotian/CVE-2023-0386.svg) ![forks](https://img.shields.io/github/forks/chenaotian/CVE-2023-0386.svg)

- [https://github.com/sxlmnwb/CVE-2023-0386](https://github.com/sxlmnwb/CVE-2023-0386) :  ![starts](https://img.shields.io/github/stars/sxlmnwb/CVE-2023-0386.svg) ![forks](https://img.shields.io/github/forks/sxlmnwb/CVE-2023-0386.svg)

- [https://github.com/Fanxiaoyao66/CVE-2023-0386](https://github.com/Fanxiaoyao66/CVE-2023-0386) :  ![starts](https://img.shields.io/github/stars/Fanxiaoyao66/CVE-2023-0386.svg) ![forks](https://img.shields.io/github/forks/Fanxiaoyao66/CVE-2023-0386.svg)

- [https://github.com/veritas501/CVE-2023-0386](https://github.com/veritas501/CVE-2023-0386) :  ![starts](https://img.shields.io/github/stars/veritas501/CVE-2023-0386.svg) ![forks](https://img.shields.io/github/forks/veritas501/CVE-2023-0386.svg)

- [https://github.com/puckiestyle/CVE-2023-0386](https://github.com/puckiestyle/CVE-2023-0386) :  ![starts](https://img.shields.io/github/stars/puckiestyle/CVE-2023-0386.svg) ![forks](https://img.shields.io/github/forks/puckiestyle/CVE-2023-0386.svg)

- [https://github.com/P4x1s/CVE-2023-0386](https://github.com/P4x1s/CVE-2023-0386) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2023-0386.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2023-0386.svg)

- [https://github.com/Satheesh575555/linux-4.19.72_CVE-2023-0386](https://github.com/Satheesh575555/linux-4.19.72_CVE-2023-0386) :  ![starts](https://img.shields.io/github/stars/Satheesh575555/linux-4.19.72_CVE-2023-0386.svg) ![forks](https://img.shields.io/github/forks/Satheesh575555/linux-4.19.72_CVE-2023-0386.svg)

- [https://github.com/Anekant-Singhai/Exploits](https://github.com/Anekant-Singhai/Exploits) :  ![starts](https://img.shields.io/github/stars/Anekant-Singhai/Exploits.svg) ![forks](https://img.shields.io/github/forks/Anekant-Singhai/Exploits.svg)

- [https://github.com/churamanib/CVE-2023-0386](https://github.com/churamanib/CVE-2023-0386) :  ![starts](https://img.shields.io/github/stars/churamanib/CVE-2023-0386.svg) ![forks](https://img.shields.io/github/forks/churamanib/CVE-2023-0386.svg)

- [https://github.com/letsr00t/CVE-2023-0386](https://github.com/letsr00t/CVE-2023-0386) :  ![starts](https://img.shields.io/github/stars/letsr00t/CVE-2023-0386.svg) ![forks](https://img.shields.io/github/forks/letsr00t/CVE-2023-0386.svg)

- [https://github.com/EstamelGG/CVE-2023-0386-libs](https://github.com/EstamelGG/CVE-2023-0386-libs) :  ![starts](https://img.shields.io/github/stars/EstamelGG/CVE-2023-0386-libs.svg) ![forks](https://img.shields.io/github/forks/EstamelGG/CVE-2023-0386-libs.svg)

## CVE-2023-0315
 Command Injection in GitHub repository froxlor/froxlor prior to 2.0.8.



- [https://github.com/mhaskar/CVE-2023-0315](https://github.com/mhaskar/CVE-2023-0315) :  ![starts](https://img.shields.io/github/stars/mhaskar/CVE-2023-0315.svg) ![forks](https://img.shields.io/github/forks/mhaskar/CVE-2023-0315.svg)

## CVE-2023-0297
 Code Injection in GitHub repository pyload/pyload prior to 0.5.0b3.dev31.



- [https://github.com/bAuh0lz/CVE-2023-0297_Pre-auth_RCE_in_pyLoad](https://github.com/bAuh0lz/CVE-2023-0297_Pre-auth_RCE_in_pyLoad) :  ![starts](https://img.shields.io/github/stars/bAuh0lz/CVE-2023-0297_Pre-auth_RCE_in_pyLoad.svg) ![forks](https://img.shields.io/github/forks/bAuh0lz/CVE-2023-0297_Pre-auth_RCE_in_pyLoad.svg)

- [https://github.com/JacobEbben/CVE-2023-0297](https://github.com/JacobEbben/CVE-2023-0297) :  ![starts](https://img.shields.io/github/stars/JacobEbben/CVE-2023-0297.svg) ![forks](https://img.shields.io/github/forks/JacobEbben/CVE-2023-0297.svg)

- [https://github.com/Small-ears/CVE-2023-0297](https://github.com/Small-ears/CVE-2023-0297) :  ![starts](https://img.shields.io/github/stars/Small-ears/CVE-2023-0297.svg) ![forks](https://img.shields.io/github/forks/Small-ears/CVE-2023-0297.svg)

- [https://github.com/overgrowncarrot1/CVE-2023-0297](https://github.com/overgrowncarrot1/CVE-2023-0297) :  ![starts](https://img.shields.io/github/stars/overgrowncarrot1/CVE-2023-0297.svg) ![forks](https://img.shields.io/github/forks/overgrowncarrot1/CVE-2023-0297.svg)

## CVE-2023-0266
 A use after free vulnerability exists in the ALSA PCM package in the Linux Kernel. SNDRV_CTL_IOCTL_ELEM_{READ|WRITE}32 is missing locks that can be used in a use-after-free that can result in a priviledge escalation to gain ring0 access from the system user. We recommend upgrading past commit 56b88b50565cd8b946a2d00b0c83927b7ebb055e



- [https://github.com/SeanHeelan/claude_opus_cve_2023_0266](https://github.com/SeanHeelan/claude_opus_cve_2023_0266) :  ![starts](https://img.shields.io/github/stars/SeanHeelan/claude_opus_cve_2023_0266.svg) ![forks](https://img.shields.io/github/forks/SeanHeelan/claude_opus_cve_2023_0266.svg)

## CVE-2023-0264
 A flaw was found in Keycloaks OpenID Connect user authentication, which may incorrectly authenticate requests. An authenticated attacker who could obtain information from a user request within the same realm could use that data to impersonate the victim and generate new session tokens. This issue could impact confidentiality, integrity, and availability.



- [https://github.com/twwd/CVE-2023-0264](https://github.com/twwd/CVE-2023-0264) :  ![starts](https://img.shields.io/github/stars/twwd/CVE-2023-0264.svg) ![forks](https://img.shields.io/github/forks/twwd/CVE-2023-0264.svg)

## CVE-2023-0179
 A buffer overflow vulnerability was found in the Netfilter subsystem in the Linux Kernel. This issue could allow the leakage of both stack and heap addresses, and potentially allow Local Privilege Escalation to the root user via arbitrary code execution.



- [https://github.com/TurtleARM/CVE-2023-0179-PoC](https://github.com/TurtleARM/CVE-2023-0179-PoC) :  ![starts](https://img.shields.io/github/stars/TurtleARM/CVE-2023-0179-PoC.svg) ![forks](https://img.shields.io/github/forks/TurtleARM/CVE-2023-0179-PoC.svg)

- [https://github.com/H4K6/CVE-2023-0179-PoC](https://github.com/H4K6/CVE-2023-0179-PoC) :  ![starts](https://img.shields.io/github/stars/H4K6/CVE-2023-0179-PoC.svg) ![forks](https://img.shields.io/github/forks/H4K6/CVE-2023-0179-PoC.svg)

## CVE-2023-0159
 The Extensive VC Addons for WPBakery page builder WordPress plugin before 1.9.1 does not validate a parameter passed to the php extract function when loading templates, allowing an unauthenticated attacker to override the template path to read arbitrary files from the hosts file system. This may be escalated to RCE using PHP filter chains.



- [https://github.com/im-hanzou/EVCer](https://github.com/im-hanzou/EVCer) :  ![starts](https://img.shields.io/github/stars/im-hanzou/EVCer.svg) ![forks](https://img.shields.io/github/forks/im-hanzou/EVCer.svg)

- [https://github.com/Sn20393873/Extensive](https://github.com/Sn20393873/Extensive) :  ![starts](https://img.shields.io/github/stars/Sn20393873/Extensive.svg) ![forks](https://img.shields.io/github/forks/Sn20393873/Extensive.svg)

## CVE-2023-0157
 The All-In-One Security (AIOS) WordPress plugin before 5.1.5 does not escape the content of log files before outputting it to the plugin admin page, allowing an authorized user (admin+) to plant bogus log files containing malicious JavaScript code that will be executed in the context of any administrator visiting this page.



- [https://github.com/b0marek/CVE-2023-0157](https://github.com/b0marek/CVE-2023-0157) :  ![starts](https://img.shields.io/github/stars/b0marek/CVE-2023-0157.svg) ![forks](https://img.shields.io/github/forks/b0marek/CVE-2023-0157.svg)

## CVE-2023-0156
 The All-In-One Security (AIOS) WordPress plugin before 5.1.5 does not limit what log files to display in it's settings pages, allowing an authorized user (admin+) to view the contents of arbitrary files and list directories anywhere on the server (to which the web server has access). The plugin only displays the last 50 lines of the file.



- [https://github.com/b0marek/CVE-2023-0156](https://github.com/b0marek/CVE-2023-0156) :  ![starts](https://img.shields.io/github/stars/b0marek/CVE-2023-0156.svg) ![forks](https://img.shields.io/github/forks/b0marek/CVE-2023-0156.svg)

## CVE-2023-0110
 Cross-site Scripting (XSS) - Stored in GitHub repository usememos/memos prior to 0.10.0.



- [https://github.com/emotest1/cve_2023_0110](https://github.com/emotest1/cve_2023_0110) :  ![starts](https://img.shields.io/github/stars/emotest1/cve_2023_0110.svg) ![forks](https://img.shields.io/github/forks/emotest1/cve_2023_0110.svg)

## CVE-2023-0099
 The Simple URLs WordPress plugin before 115 does not sanitise and escape some parameters before outputting them back in some pages, leading to Reflected Cross-Site Scripting which could be used against high privilege users such as admin.



- [https://github.com/amirzargham/CVE-2023-0099-exploit](https://github.com/amirzargham/CVE-2023-0099-exploit) :  ![starts](https://img.shields.io/github/stars/amirzargham/CVE-2023-0099-exploit.svg) ![forks](https://img.shields.io/github/forks/amirzargham/CVE-2023-0099-exploit.svg)

## CVE-2023-0045
 The current implementation of the prctl syscall does not issue an IBPB immediately during the syscall. The ib_prctl_set  function updates the Thread Information Flags (TIFs) for the task and updates the SPEC_CTRL MSR on the function __speculation_ctrl_update, but the IBPB is only issued on the next schedule, when the TIF bits are checked. This leaves the victim vulnerable to values already injected on the BTB, prior to the prctl syscall.  The patch that added the support for the conditional mitigation via prctl (ib_prctl_set) dates back to the kernel 4.9.176.

We recommend upgrading past commit a664ec9158eeddd75121d39c9a0758016097fa96



- [https://github.com/es0j/CVE-2023-0045](https://github.com/es0j/CVE-2023-0045) :  ![starts](https://img.shields.io/github/stars/es0j/CVE-2023-0045.svg) ![forks](https://img.shields.io/github/forks/es0j/CVE-2023-0045.svg)

- [https://github.com/ASkyeye/CVE-2023-0045](https://github.com/ASkyeye/CVE-2023-0045) :  ![starts](https://img.shields.io/github/stars/ASkyeye/CVE-2023-0045.svg) ![forks](https://img.shields.io/github/forks/ASkyeye/CVE-2023-0045.svg)

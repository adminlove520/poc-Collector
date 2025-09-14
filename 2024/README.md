## CVE-2024-57725
 An issue in the Arcadyan Livebox Fibra PRV3399B_B_LT allows a remote or local attacker to modify the GPON link value without authentication, causing an internet service disruption via the /firstconnection.cgi endpoint.



- [https://github.com/pointedsec/CVE-2024-57725](https://github.com/pointedsec/CVE-2024-57725) :  ![starts](https://img.shields.io/github/stars/pointedsec/CVE-2024-57725.svg) ![forks](https://img.shields.io/github/forks/pointedsec/CVE-2024-57725.svg)

## CVE-2024-57698
 An issue in modernwms v.1.0 allows an attacker view the MD5 hash of the administrator password and other attributes without authentication, even after initial configuration and password change. This happens due to excessive exposure of information and the lack of adequate access control on the /user/list?culture=en-us endpoint.



- [https://github.com/rodolfomarianocy/xpl-ModernWMS-CVE-2024-57698](https://github.com/rodolfomarianocy/xpl-ModernWMS-CVE-2024-57698) :  ![starts](https://img.shields.io/github/stars/rodolfomarianocy/xpl-ModernWMS-CVE-2024-57698.svg) ![forks](https://img.shields.io/github/forks/rodolfomarianocy/xpl-ModernWMS-CVE-2024-57698.svg)

## CVE-2024-57488
 Code-Projects Online Car Rental System 1.0 is vulnerable to Cross Site Scripting (XSS) via the vehicalorcview parameter in /admin/edit-vehicle.php.



- [https://github.com/aaryan-11-x/CVE-2024-57487-and-CVE-2024-57488](https://github.com/aaryan-11-x/CVE-2024-57487-and-CVE-2024-57488) :  ![starts](https://img.shields.io/github/stars/aaryan-11-x/CVE-2024-57487-and-CVE-2024-57488.svg) ![forks](https://img.shields.io/github/forks/aaryan-11-x/CVE-2024-57487-and-CVE-2024-57488.svg)

## CVE-2024-57487
 In Code-Projects Online Car Rental System 1.0, the file upload feature does not validate file extensions or MIME types allowing an attacker to upload a PHP shell without any restrictions and execute commands on the server.



- [https://github.com/aaryan-11-x/CVE-2024-57487-and-CVE-2024-57488](https://github.com/aaryan-11-x/CVE-2024-57487-and-CVE-2024-57488) :  ![starts](https://img.shields.io/github/stars/aaryan-11-x/CVE-2024-57487-and-CVE-2024-57488.svg) ![forks](https://img.shields.io/github/forks/aaryan-11-x/CVE-2024-57487-and-CVE-2024-57488.svg)

## CVE-2024-57394
 The quarantine - restore function in Qi-ANXIN Tianqing Endpoint Security Management System v10.0 allows user to restore a malicious file to an arbitrary file path. Attackers can write malicious DLL to system path and perform privilege escalation by leveraging Windows DLL hijacking vulnerabilities.



- [https://github.com/cwjchoi01/CVE-2024-57394](https://github.com/cwjchoi01/CVE-2024-57394) :  ![starts](https://img.shields.io/github/stars/cwjchoi01/CVE-2024-57394.svg) ![forks](https://img.shields.io/github/forks/cwjchoi01/CVE-2024-57394.svg)

## CVE-2024-57376
 Buffer Overflow vulnerability in D-Link DSR-150, DSR-150N, DSR-250, DSR-250N, DSR-500N, DSR-1000N from 3.13 to 3.17B901C allows unauthenticated users to execute remote code execution.



- [https://github.com/DelspoN/CVE-2024-57376](https://github.com/DelspoN/CVE-2024-57376) :  ![starts](https://img.shields.io/github/stars/DelspoN/CVE-2024-57376.svg) ![forks](https://img.shields.io/github/forks/DelspoN/CVE-2024-57376.svg)

## CVE-2024-57241
 Dedecms 5.71sp1 and earlier is vulnerable to URL redirect. In the web application, a logic error does not judge the input GET request resulting in URL redirection.



- [https://github.com/woshidaheike/CVE-2024-57241](https://github.com/woshidaheike/CVE-2024-57241) :  ![starts](https://img.shields.io/github/stars/woshidaheike/CVE-2024-57241.svg) ![forks](https://img.shields.io/github/forks/woshidaheike/CVE-2024-57241.svg)

## CVE-2024-56512
 Apache NiFi 1.10.0 through 2.0.0 are missing fine-grained authorization checking for Parameter Contexts, referenced Controller Services, and referenced Parameter Providers, when creating new Process Groups.

Creating a new Process Group can include binding to a Parameter Context, but in cases where the Process Group did not reference any Parameter values, the framework did not check user authorization for the bound Parameter Context. Missing authorization for a bound Parameter Context enabled clients to download non-sensitive Parameter values after creating the Process Group.

Creating a new Process Group can also include referencing existing Controller Services or Parameter Providers. The framework did not check user authorization for referenced Controller Services or Parameter Providers, enabling clients to create Process Groups and use these components that were otherwise unauthorized.

This vulnerability is limited in scope to authenticated users authorized to create Process Groups. The scope is further limited to deployments with component-based authorization policies. Upgrading to Apache NiFi 2.1.0 is the recommended mitigation, which includes authorization checking for Parameter and Controller Service references on Process Group creation.



- [https://github.com/absholi7ly/CVE-2024-56512-Apache-NiFi-Exploit](https://github.com/absholi7ly/CVE-2024-56512-Apache-NiFi-Exploit) :  ![starts](https://img.shields.io/github/stars/absholi7ly/CVE-2024-56512-Apache-NiFi-Exploit.svg) ![forks](https://img.shields.io/github/forks/absholi7ly/CVE-2024-56512-Apache-NiFi-Exploit.svg)

## CVE-2024-56433
 shadow-utils (aka shadow) 4.4 through 4.17.0 establishes a default /etc/subuid behavior (e.g., uid 100000 through 165535 for the first user account) that can realistically conflict with the uids of users defined on locally administered networks, potentially leading to account takeover, e.g., by leveraging newuidmap for access to an NFS home directory (or same-host resources in the case of remote logins by these local network users). NOTE: it may also be argued that system administrators should not have assigned uids, within local networks, that are within the range that can occur in /etc/subuid.



- [https://github.com/JonnyWhatshisface/CVE-2024-56433](https://github.com/JonnyWhatshisface/CVE-2024-56433) :  ![starts](https://img.shields.io/github/stars/JonnyWhatshisface/CVE-2024-56433.svg) ![forks](https://img.shields.io/github/forks/JonnyWhatshisface/CVE-2024-56433.svg)

## CVE-2024-56431
 oc_huff_tree_unpack in huffdec.c in libtheora in Theora through 1.0 7180717 has an invalid negative left shift. NOTE: this is disputed by third parties because there is no evidence of a security impact, e.g., an application would not crash.



- [https://github.com/UnionTech-Software/libtheora-CVE-2024-56431-PoC](https://github.com/UnionTech-Software/libtheora-CVE-2024-56431-PoC) :  ![starts](https://img.shields.io/github/stars/UnionTech-Software/libtheora-CVE-2024-56431-PoC.svg) ![forks](https://img.shields.io/github/forks/UnionTech-Software/libtheora-CVE-2024-56431-PoC.svg)

## CVE-2024-56429
 itech iLabClient 3.7.1 relies on the hard-coded YngAYdgAE/kKZYu2F2wm6w== key (found in iLabClient.jar) for local users to read or write to the database.



- [https://github.com/lisa-2905/CVE-2024-56429](https://github.com/lisa-2905/CVE-2024-56429) :  ![starts](https://img.shields.io/github/stars/lisa-2905/CVE-2024-56429.svg) ![forks](https://img.shields.io/github/forks/lisa-2905/CVE-2024-56429.svg)

## CVE-2024-56428
 The local iLabClient database in itech iLabClient 3.7.1 allows local attackers to read cleartext credentials (from the CONFIGS table) for their servers configured in the client.



- [https://github.com/lisa-2905/CVE-2024-56428](https://github.com/lisa-2905/CVE-2024-56428) :  ![starts](https://img.shields.io/github/stars/lisa-2905/CVE-2024-56428.svg) ![forks](https://img.shields.io/github/forks/lisa-2905/CVE-2024-56428.svg)

## CVE-2024-56337
 Time-of-check Time-of-use (TOCTOU) Race Condition vulnerability in Apache Tomcat.

This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.1, from 10.1.0-M1 through 10.1.33, from 9.0.0.M1 through 9.0.97.
The following versions were EOL at the time the CVE was created but are 
known to be affected: 8.5.0 though 8.5.100. Other, older, EOL versions 
may also be affected.


The mitigation for CVE-2024-50379 was incomplete.

Users running Tomcat on a case insensitive file system with the default servlet write enabled (readonly initialisation 
parameter set to the non-default value of false) may need additional configuration to fully mitigate CVE-2024-50379 depending on which version of Java they are using with Tomcat:
- running on Java 8 or Java 11: the system property sun.io.useCanonCaches must be explicitly set to false (it defaults to true)
- running on Java 17: the system property sun.io.useCanonCaches, if set, must be set to false (it defaults to false)
- running on Java 21 onwards: no further configuration is required (the system property and the problematic cache have been removed)

Tomcat 11.0.3, 10.1.35 and 9.0.99 onwards will include checks that sun.io.useCanonCaches is set appropriately before allowing the default servlet to be write enabled on a case insensitive file system. Tomcat will also set sun.io.useCanonCaches to false by default where it can.



- [https://github.com/SleepingBag945/CVE-2024-50379](https://github.com/SleepingBag945/CVE-2024-50379) :  ![starts](https://img.shields.io/github/stars/SleepingBag945/CVE-2024-50379.svg) ![forks](https://img.shields.io/github/forks/SleepingBag945/CVE-2024-50379.svg)

## CVE-2024-56331
 Uptime Kuma is an open source, self-hosted monitoring tool. An **Improper URL Handling Vulnerability** allows an attacker to access sensitive local files on the server by exploiting the `file:///` protocol. This vulnerability is triggered via the **"real-browser"** request type, which takes a screenshot of the URL provided by the attacker. By supplying local file paths, such as `file:///etc/passwd`, an attacker can read sensitive data from the server. This vulnerability arises because the system does not properly validate or sanitize the user input for the URL field. Specifically: 1. The URL input (`input data-v-5f5c86d7="" id="url" type="url" class="form-control" pattern="https?://.+" required=""`) allows users to input arbitrary file paths, including those using the `file:///` protocol, without server-side validation. 2. The server then uses the user-provided URL to make a request, passing it to a browser instance that performs the "real-browser" request, which takes a screenshot of the content at the given URL. If a local file path is entered (e.g., `file:///etc/passwd`), the browser fetches and captures the file’s content. Since the user input is not validated, an attacker can manipulate the URL to request local files (e.g., `file:///etc/passwd`), and the system will capture a screenshot of the file's content, potentially exposing sensitive data. Any **authenticated user** who can submit a URL in "real-browser" mode is at risk of exposing sensitive data through screenshots of these files. This issue has been addressed in version 1.23.16 and all users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/griisemine/CVE-2024-56331](https://github.com/griisemine/CVE-2024-56331) :  ![starts](https://img.shields.io/github/stars/griisemine/CVE-2024-56331.svg) ![forks](https://img.shields.io/github/forks/griisemine/CVE-2024-56331.svg)

## CVE-2024-56289
 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Groundhogg Inc. Groundhogg allows Reflected XSS.This issue affects Groundhogg: from n/a through 3.7.3.3.



- [https://github.com/DoTTak/CVE-2024-56289](https://github.com/DoTTak/CVE-2024-56289) :  ![starts](https://img.shields.io/github/stars/DoTTak/CVE-2024-56289.svg) ![forks](https://img.shields.io/github/forks/DoTTak/CVE-2024-56289.svg)

## CVE-2024-56278
 Improper Control of Generation of Code ('Code Injection') vulnerability in Smackcoders WP Ultimate Exporter allows PHP Remote File Inclusion.This issue affects WP Ultimate Exporter: from n/a through 2.9.1.



- [https://github.com/DoTTak/CVE-2024-56278](https://github.com/DoTTak/CVE-2024-56278) :  ![starts](https://img.shields.io/github/stars/DoTTak/CVE-2024-56278.svg) ![forks](https://img.shields.io/github/forks/DoTTak/CVE-2024-56278.svg)

## CVE-2024-56145
 Craft is a flexible, user-friendly CMS for creating custom digital experiences on the web and beyond. Users of affected versions are affected by this vulnerability if their php.ini configuration has `register_argc_argv` enabled. For these users an unspecified remote code execution vector is present. Users are advised to update to version 3.9.14, 4.13.2, or 5.5.2. Users unable to upgrade should disable `register_argc_argv` to mitigate the issue.



- [https://github.com/Chocapikk/CVE-2024-56145](https://github.com/Chocapikk/CVE-2024-56145) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-56145.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-56145.svg)

- [https://github.com/Sachinart/CVE-2024-56145-craftcms-rce](https://github.com/Sachinart/CVE-2024-56145-craftcms-rce) :  ![starts](https://img.shields.io/github/stars/Sachinart/CVE-2024-56145-craftcms-rce.svg) ![forks](https://img.shields.io/github/forks/Sachinart/CVE-2024-56145-craftcms-rce.svg)

- [https://github.com/hmhlol/craft-cms-RCE-CVE-2024-56145](https://github.com/hmhlol/craft-cms-RCE-CVE-2024-56145) :  ![starts](https://img.shields.io/github/stars/hmhlol/craft-cms-RCE-CVE-2024-56145.svg) ![forks](https://img.shields.io/github/forks/hmhlol/craft-cms-RCE-CVE-2024-56145.svg)

## CVE-2024-56116
 A Cross-Site Request Forgery vulnerability in Amiro.CMS before 7.8.4 allows remote attackers to create an administrator account.



- [https://github.com/ComplianceControl/CVE-2024-56116](https://github.com/ComplianceControl/CVE-2024-56116) :  ![starts](https://img.shields.io/github/stars/ComplianceControl/CVE-2024-56116.svg) ![forks](https://img.shields.io/github/forks/ComplianceControl/CVE-2024-56116.svg)

## CVE-2024-56115
 A vulnerability in Amiro.CMS before 7.8.4 exists due to the failure to take measures to neutralize special elements. It allows remote attackers to conduct a Cross-Site Scripting (XSS) attack.



- [https://github.com/ComplianceControl/CVE-2024-56115](https://github.com/ComplianceControl/CVE-2024-56115) :  ![starts](https://img.shields.io/github/stars/ComplianceControl/CVE-2024-56115.svg) ![forks](https://img.shields.io/github/forks/ComplianceControl/CVE-2024-56115.svg)

## CVE-2024-56071
 Incorrect Privilege Assignment vulnerability in Mike Leembruggen Simple Dashboard allows Privilege Escalation.This issue affects Simple Dashboard: from n/a through 2.0.



- [https://github.com/Nxploited/CVE-2024-56071](https://github.com/Nxploited/CVE-2024-56071) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-56071.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-56071.svg)

## CVE-2024-56067
 Missing Authorization vulnerability in Azzaroco WP SuperBackup allows Exploiting Incorrectly Configured Access Control Security Levels.This issue affects WP SuperBackup: from n/a through 2.3.3.



- [https://github.com/RandomRobbieBF/CVE-2024-56067](https://github.com/RandomRobbieBF/CVE-2024-56067) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-56067.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-56067.svg)

## CVE-2024-56064
 Unrestricted Upload of File with Dangerous Type vulnerability in Azzaroco WP SuperBackup allows Upload a Web Shell to a Web Server.This issue affects WP SuperBackup: from n/a through 2.3.3.



- [https://github.com/RandomRobbieBF/CVE-2024-56064](https://github.com/RandomRobbieBF/CVE-2024-56064) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-56064.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-56064.svg)

## CVE-2024-56059
 Improperly Controlled Modification of Object Prototype Attributes ('Prototype Pollution') vulnerability in Mighty Digital Partners allows Object Injection.This issue affects Partners: from n/a through 0.2.0.



- [https://github.com/RandomRobbieBF/CVE-2024-56059](https://github.com/RandomRobbieBF/CVE-2024-56059) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-56059.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-56059.svg)

## CVE-2024-56058
 Deserialization of Untrusted Data vulnerability in Gueststream VRPConnector allows Object Injection.This issue affects VRPConnector: from n/a through 2.0.1.



- [https://github.com/RandomRobbieBF/CVE-2024-56058](https://github.com/RandomRobbieBF/CVE-2024-56058) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-56058.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-56058.svg)

## CVE-2024-55988
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Amol Nirmala Waman Navayan CSV Export allows Blind SQL Injection.This issue affects Navayan CSV Export: from n/a through 1.0.9.



- [https://github.com/RandomRobbieBF/CVE-2024-55988](https://github.com/RandomRobbieBF/CVE-2024-55988) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-55988.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-55988.svg)

## CVE-2024-55982
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in richteam Share Buttons – Social Media allows Blind SQL Injection.This issue affects Share Buttons – Social Media: from n/a through 1.0.2.



- [https://github.com/RandomRobbieBF/CVE-2024-55982](https://github.com/RandomRobbieBF/CVE-2024-55982) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-55982.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-55982.svg)

## CVE-2024-55981
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Nabajit Roy Nabz Image Gallery allows SQL Injection.This issue affects Nabz Image Gallery: from n/a through v1.00.



- [https://github.com/RandomRobbieBF/CVE-2024-55981](https://github.com/RandomRobbieBF/CVE-2024-55981) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-55981.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-55981.svg)

## CVE-2024-55980
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Webriderz Wr Age Verification allows SQL Injection.This issue affects Wr Age Verification: from n/a through 2.0.0.



- [https://github.com/RandomRobbieBF/CVE-2024-55980](https://github.com/RandomRobbieBF/CVE-2024-55980) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-55980.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-55980.svg)

## CVE-2024-55978
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WalletStation.com Code Generator Pro allows SQL Injection.This issue affects Code Generator Pro: from n/a through 1.2.



- [https://github.com/RandomRobbieBF/CVE-2024-55978](https://github.com/RandomRobbieBF/CVE-2024-55978) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-55978.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-55978.svg)

## CVE-2024-55976
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Mike Leembruggen Critical Site Intel allows SQL Injection.This issue affects Critical Site Intel: from n/a through 1.0.



- [https://github.com/RandomRobbieBF/CVE-2024-55976](https://github.com/RandomRobbieBF/CVE-2024-55976) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-55976.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-55976.svg)

## CVE-2024-55972
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Chris Carvache eTemplates allows SQL Injection.This issue affects eTemplates: from n/a through 0.2.1.



- [https://github.com/RandomRobbieBF/CVE-2024-55972](https://github.com/RandomRobbieBF/CVE-2024-55972) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-55972.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-55972.svg)

## CVE-2024-55968
 An issue was discovered in DTEX DEC-M (DTEX Forwarder) 6.1.1. The com.dtexsystems.helper service, responsible for handling privileged operations within the macOS DTEX Event Forwarder agent, fails to implement critical client validation during XPC interprocess communication (IPC). Specifically, the service does not verify the code requirements, entitlements, security flags, or version of any client attempting to establish a connection. This lack of proper logic validation allows malicious actors to exploit the service's methods via unauthorized client connections, and escalate privileges to root by abusing the DTConnectionHelperProtocol protocol's submitQuery method over an unauthorized XPC connection.



- [https://github.com/null-event/CVE-2024-55968](https://github.com/null-event/CVE-2024-55968) :  ![starts](https://img.shields.io/github/stars/null-event/CVE-2024-55968.svg) ![forks](https://img.shields.io/github/forks/null-event/CVE-2024-55968.svg)

- [https://github.com/Wi1DN00B/CVE-2024-55968](https://github.com/Wi1DN00B/CVE-2024-55968) :  ![starts](https://img.shields.io/github/stars/Wi1DN00B/CVE-2024-55968.svg) ![forks](https://img.shields.io/github/forks/Wi1DN00B/CVE-2024-55968.svg)

## CVE-2024-55963
 An issue was discovered in Appsmith before 1.51. A user on Appsmith that doesn't have admin permissions can trigger the restart API on Appsmith, causing a server restart. This is still within the Appsmith container, and the impact is limited to Appsmith's own server only, but there is a denial of service because it can be continually restarted. This is due to incorrect access control checks, which should check for super user permissions on the incoming request.



- [https://github.com/superswan/CVE-2024-55963](https://github.com/superswan/CVE-2024-55963) :  ![starts](https://img.shields.io/github/stars/superswan/CVE-2024-55963.svg) ![forks](https://img.shields.io/github/forks/superswan/CVE-2024-55963.svg)

## CVE-2024-55875
 http4k is a functional toolkit for Kotlin HTTP applications. Prior to version 5.41.0.0, there is a potential XXE (XML External Entity Injection) vulnerability when http4k handling malicious XML contents within requests, which might allow attackers to read local sensitive information on server, trigger Server-side Request Forgery and even execute code under some circumstances. Version 5.41.0.0 contains a patch for the issue.



- [https://github.com/JAckLosingHeart/CVE-2024-55875](https://github.com/JAckLosingHeart/CVE-2024-55875) :  ![starts](https://img.shields.io/github/stars/JAckLosingHeart/CVE-2024-55875.svg) ![forks](https://img.shields.io/github/forks/JAckLosingHeart/CVE-2024-55875.svg)

## CVE-2024-55656
 RedisBloom adds a set of probabilistic data structures to Redis. There is an integer overflow vulnerability in RedisBloom, which is a module used in Redis. The integer overflow vulnerability allows an attacker (a redis client which knows the password) to allocate memory in the heap lesser than the required memory due to wraparound. Then read and write can be performed beyond this allocated memory, leading to info leak and OOB write. The integer overflow is in CMS.INITBYDIM command, which initialize a Count-Min Sketch to dimensions specified by user. It accepts two values (width and depth) and uses them to allocate memory in NewCMSketch(). This vulnerability is fixed in 2.2.19, 2.4.12, 2.6.14, and 2.8.2.



- [https://github.com/rick2600/redis-stack-CVE-2024-55656](https://github.com/rick2600/redis-stack-CVE-2024-55656) :  ![starts](https://img.shields.io/github/stars/rick2600/redis-stack-CVE-2024-55656.svg) ![forks](https://img.shields.io/github/forks/rick2600/redis-stack-CVE-2024-55656.svg)

## CVE-2024-55591
 An Authentication Bypass Using an Alternate Path or Channel vulnerability [CWE-288] affecting FortiOS version 7.0.0 through 7.0.16 and FortiProxy version 7.0.0 through 7.0.19 and 7.2.0 through 7.2.12 allows a remote attacker to gain super-admin privileges via crafted requests to Node.js websocket module.



- [https://github.com/UMChacker/CVE-2024-55591-POC](https://github.com/UMChacker/CVE-2024-55591-POC) :  ![starts](https://img.shields.io/github/stars/UMChacker/CVE-2024-55591-POC.svg) ![forks](https://img.shields.io/github/forks/UMChacker/CVE-2024-55591-POC.svg)

- [https://github.com/binarywarm/exp-cmd-add-admin-vpn-CVE-2024-55591](https://github.com/binarywarm/exp-cmd-add-admin-vpn-CVE-2024-55591) :  ![starts](https://img.shields.io/github/stars/binarywarm/exp-cmd-add-admin-vpn-CVE-2024-55591.svg) ![forks](https://img.shields.io/github/forks/binarywarm/exp-cmd-add-admin-vpn-CVE-2024-55591.svg)

## CVE-2024-55587
 python-libarchive through 4.2.1 allows directory traversal (to create files) in extract in zip.py for ZipFile.extractall and ZipFile.extract.



- [https://github.com/CSIRTTrizna/CVE-2024-55587](https://github.com/CSIRTTrizna/CVE-2024-55587) :  ![starts](https://img.shields.io/github/stars/CSIRTTrizna/CVE-2024-55587.svg) ![forks](https://img.shields.io/github/forks/CSIRTTrizna/CVE-2024-55587.svg)

## CVE-2024-55557
 ui/pref/ProxyPrefView.java in weasis-core in Weasis 4.5.1 has a hardcoded key for symmetric encryption of proxy credentials.



- [https://github.com/partywavesec/CVE-2024-55557](https://github.com/partywavesec/CVE-2024-55557) :  ![starts](https://img.shields.io/github/stars/partywavesec/CVE-2024-55557.svg) ![forks](https://img.shields.io/github/forks/partywavesec/CVE-2024-55557.svg)

## CVE-2024-55555
 Invoice Ninja before 5.10.43 allows remote code execution from a pre-authenticated route when an attacker knows the APP_KEY. This is exacerbated by .env files, available from the product's repository, that have default APP_KEY values. The route/{hash} route defined in the invoiceninja/routes/client.php file can be accessed without authentication. The parameter {hash} is passed to the function decrypt that expects a Laravel ciphered value containing a serialized object. (Furthermore, Laravel contains several gadget chains usable to trigger remote command execution from arbitrary deserialization.) Therefore, an attacker in possession of the APP_KEY is able to fully control a string passed to an unserialize function.



- [https://github.com/Yucaerin/CVE-2024-55555](https://github.com/Yucaerin/CVE-2024-55555) :  ![starts](https://img.shields.io/github/stars/Yucaerin/CVE-2024-55555.svg) ![forks](https://img.shields.io/github/forks/Yucaerin/CVE-2024-55555.svg)

## CVE-2024-55503
 An issue in termius before v.9.9.0 allows a local attacker to execute arbitrary code via a crafted script to the DYLD_INSERT_LIBRARIES component.



- [https://github.com/SyFi/CVE-2024-55503](https://github.com/SyFi/CVE-2024-55503) :  ![starts](https://img.shields.io/github/stars/SyFi/CVE-2024-55503.svg) ![forks](https://img.shields.io/github/forks/SyFi/CVE-2024-55503.svg)

## CVE-2024-55466
 An arbitrary file upload vulnerability in the Image Gallery of ThingsBoard Community, ThingsBoard Cloud and ThingsBoard Professional v3.8.1 allows attackers to execute arbitrary code via uploading a crafted file.



- [https://github.com/cybsecsid/ThingsBoard-IoT-Platform-CVE-2024-55466](https://github.com/cybsecsid/ThingsBoard-IoT-Platform-CVE-2024-55466) :  ![starts](https://img.shields.io/github/stars/cybsecsid/ThingsBoard-IoT-Platform-CVE-2024-55466.svg) ![forks](https://img.shields.io/github/forks/cybsecsid/ThingsBoard-IoT-Platform-CVE-2024-55466.svg)

## CVE-2024-55457
 MasterSAM Star Gate 11 is vulnerable to directory traversal via /adama/adama/downloadService. An attacker can exploit this vulnerability by manipulating the file parameter to access arbitrary files on the server, potentially exposing sensitive information.



- [https://github.com/h13nh04ng/CVE-2024-55457-PoC](https://github.com/h13nh04ng/CVE-2024-55457-PoC) :  ![starts](https://img.shields.io/github/stars/h13nh04ng/CVE-2024-55457-PoC.svg) ![forks](https://img.shields.io/github/forks/h13nh04ng/CVE-2024-55457-PoC.svg)

## CVE-2024-55215
 An issue in trojan v.2.0.0 through v.2.15.3 allows a remote attacker to escalate privileges via the initialization interface /auth/register.



- [https://github.com/ainrm/Jrohy-trojan-unauth-poc](https://github.com/ainrm/Jrohy-trojan-unauth-poc) :  ![starts](https://img.shields.io/github/stars/ainrm/Jrohy-trojan-unauth-poc.svg) ![forks](https://img.shields.io/github/forks/ainrm/Jrohy-trojan-unauth-poc.svg)

## CVE-2024-55211
 An issue in Think Router Tk-Rt-Wr135G V3.0.2-X000 allows attackers to bypass authentication via a crafted cookie.



- [https://github.com/micaelmaciel/CVE-2024-55211](https://github.com/micaelmaciel/CVE-2024-55211) :  ![starts](https://img.shields.io/github/stars/micaelmaciel/CVE-2024-55211.svg) ![forks](https://img.shields.io/github/forks/micaelmaciel/CVE-2024-55211.svg)

## CVE-2024-55099
 A SQL Injection vulnerability was found in /admin/index.php in phpgurukul Online Nurse Hiring System v1.0, which allows remote attackers to execute arbitrary SQL commands to get unauthorized database access via the username parameter.



- [https://github.com/ugurkarakoc1/CVE-2024-55099-Online-Nurse-Hiring-System-v1.0-SQL-Injection-Vulnerability-](https://github.com/ugurkarakoc1/CVE-2024-55099-Online-Nurse-Hiring-System-v1.0-SQL-Injection-Vulnerability-) :  ![starts](https://img.shields.io/github/stars/ugurkarakoc1/CVE-2024-55099-Online-Nurse-Hiring-System-v1.0-SQL-Injection-Vulnerability-.svg) ![forks](https://img.shields.io/github/forks/ugurkarakoc1/CVE-2024-55099-Online-Nurse-Hiring-System-v1.0-SQL-Injection-Vulnerability-.svg)

## CVE-2024-55040
 Cross Site Scripting vulnerability in Sensaphone WEB600 Monitoring System v.1.6.5.H and before allows a remote attacker to execute arbitrary code via a crafted GET requests to /@.xml, placing payloads in the g7200, g7300, g4601, and g1F02 parameters.



- [https://github.com/tcbutler320/CVE-2024-55040-Sensaphone-XSS](https://github.com/tcbutler320/CVE-2024-55040-Sensaphone-XSS) :  ![starts](https://img.shields.io/github/stars/tcbutler320/CVE-2024-55040-Sensaphone-XSS.svg) ![forks](https://img.shields.io/github/forks/tcbutler320/CVE-2024-55040-Sensaphone-XSS.svg)

## CVE-2024-54910
 Hasleo Backup Suite Free v4.9.4 and before is vulnerable to Insecure Permissions via the File recovery function.



- [https://github.com/KrakenEU/CVE-2024-54910](https://github.com/KrakenEU/CVE-2024-54910) :  ![starts](https://img.shields.io/github/stars/KrakenEU/CVE-2024-54910.svg) ![forks](https://img.shields.io/github/forks/KrakenEU/CVE-2024-54910.svg)

## CVE-2024-54820
 XOne Web Monitor v02.10.2024.530 framework 1.0.4.9 was discovered to contain a SQL injection vulnerability in the login page. This vulnerability allows attackers to extract all usernames and passwords via a crafted input.



- [https://github.com/jcarabantes/CVE-2024-54820](https://github.com/jcarabantes/CVE-2024-54820) :  ![starts](https://img.shields.io/github/stars/jcarabantes/CVE-2024-54820.svg) ![forks](https://img.shields.io/github/forks/jcarabantes/CVE-2024-54820.svg)

## CVE-2024-54819
 I, Librarian before and including 5.11.1 is vulnerable to Server-Side Request Forgery (SSRF) due to improper input validation in classes/security/validation.php



- [https://github.com/partywavesec/CVE-2024-54819](https://github.com/partywavesec/CVE-2024-54819) :  ![starts](https://img.shields.io/github/stars/partywavesec/CVE-2024-54819.svg) ![forks](https://img.shields.io/github/forks/partywavesec/CVE-2024-54819.svg)

## CVE-2024-54761
 BigAnt Office Messenger 5.6.06 is vulnerable to SQL Injection via the 'dev_code' parameter.



- [https://github.com/nscan9/CVE-2024-54761](https://github.com/nscan9/CVE-2024-54761) :  ![starts](https://img.shields.io/github/stars/nscan9/CVE-2024-54761.svg) ![forks](https://img.shields.io/github/forks/nscan9/CVE-2024-54761.svg)

## CVE-2024-54756
 A remote code execution (RCE) vulnerability in the ZScript function of ZDoom Team GZDoom v4.13.1 allows attackers to execute arbitrary code via supplying a crafted PK3 file containing a malicious ZScript source file.



- [https://github.com/Chainmanner/GZDoom-Arbitrary-Code-Execution-via-ZScript-PoC](https://github.com/Chainmanner/GZDoom-Arbitrary-Code-Execution-via-ZScript-PoC) :  ![starts](https://img.shields.io/github/stars/Chainmanner/GZDoom-Arbitrary-Code-Execution-via-ZScript-PoC.svg) ![forks](https://img.shields.io/github/forks/Chainmanner/GZDoom-Arbitrary-Code-Execution-via-ZScript-PoC.svg)

## CVE-2024-54679
 CyberPanel (aka Cyber Panel) before 6778ad1 does not require the FilemanagerAdmin capability for restartMySQL actions.



- [https://github.com/hotplugin0x01/CVE-2024-54679](https://github.com/hotplugin0x01/CVE-2024-54679) :  ![starts](https://img.shields.io/github/stars/hotplugin0x01/CVE-2024-54679.svg) ![forks](https://img.shields.io/github/forks/hotplugin0x01/CVE-2024-54679.svg)

## CVE-2024-54498
 A path handling issue was addressed with improved validation. This issue is fixed in macOS Sequoia 15.2, macOS Ventura 13.7.2, macOS Sonoma 14.7.2. An app may be able to break out of its sandbox.



- [https://github.com/wh1te4ever/CVE-2024-54498-PoC](https://github.com/wh1te4ever/CVE-2024-54498-PoC) :  ![starts](https://img.shields.io/github/stars/wh1te4ever/CVE-2024-54498-PoC.svg) ![forks](https://img.shields.io/github/forks/wh1te4ever/CVE-2024-54498-PoC.svg)

## CVE-2024-54385
 Server-Side Request Forgery (SSRF) vulnerability in SoftLab Radio Player allows Server Side Request Forgery.This issue affects Radio Player: from n/a through 2.0.82.



- [https://github.com/RandomRobbieBF/CVE-2024-54385](https://github.com/RandomRobbieBF/CVE-2024-54385) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-54385.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-54385.svg)

## CVE-2024-54379
 Missing Authorization vulnerability in Blokhaus Minterpress allows Privilege Escalation.This issue affects Minterpress: from n/a through 1.0.5.



- [https://github.com/RandomRobbieBF/CVE-2024-54379](https://github.com/RandomRobbieBF/CVE-2024-54379) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-54379.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-54379.svg)

## CVE-2024-54378
 Missing Authorization vulnerability in Quietly Quietly Insights allows Privilege Escalation.This issue affects Quietly Insights: from n/a through 1.2.2.



- [https://github.com/RandomRobbieBF/CVE-2024-54378](https://github.com/RandomRobbieBF/CVE-2024-54378) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-54378.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-54378.svg)

## CVE-2024-54374
 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Sabri Taieb Sogrid allows PHP Local File Inclusion.This issue affects Sogrid: from n/a through 1.5.6.



- [https://github.com/RandomRobbieBF/CVE-2024-54374](https://github.com/RandomRobbieBF/CVE-2024-54374) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-54374.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-54374.svg)

## CVE-2024-54369
 Missing Authorization vulnerability in ThemeHunk Zita Site Builder allows Accessing Functionality Not Properly Constrained by ACLs.This issue affects Zita Site Builder: from n/a through 1.0.2.



- [https://github.com/RandomRobbieBF/CVE-2024-54369](https://github.com/RandomRobbieBF/CVE-2024-54369) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-54369.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-54369.svg)

## CVE-2024-54363
 Incorrect Privilege Assignment vulnerability in nssTheme Wp NssUser Register allows Privilege Escalation.This issue affects Wp NssUser Register: from n/a through 1.0.0.



- [https://github.com/RandomRobbieBF/CVE-2024-54363](https://github.com/RandomRobbieBF/CVE-2024-54363) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-54363.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-54363.svg)

## CVE-2024-54330
 Server-Side Request Forgery (SSRF) vulnerability in Hep Hep Hurra (HHH) Hurrakify allows Server Side Request Forgery.This issue affects Hurrakify: from n/a through 2.4.



- [https://github.com/RandomRobbieBF/CVE-2024-54330](https://github.com/RandomRobbieBF/CVE-2024-54330) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-54330.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-54330.svg)

## CVE-2024-54292
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Appsplate Appsplate allows SQL Injection.This issue affects Appsplate: from n/a through 2.1.3.



- [https://github.com/RandomRobbieBF/CVE-2024-54292](https://github.com/RandomRobbieBF/CVE-2024-54292) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-54292.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-54292.svg)

## CVE-2024-54262
 Unrestricted Upload of File with Dangerous Type vulnerability in Siddharth Nagar Import Export For WooCommerce allows Upload a Web Shell to a Web Server.This issue affects Import Export For WooCommerce: from n/a through 1.5.



- [https://github.com/RandomRobbieBF/CVE-2024-54262](https://github.com/RandomRobbieBF/CVE-2024-54262) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-54262.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-54262.svg)

## CVE-2024-54160
 dashboards-reporting (aka Dashboards Reports) before 2.19.0.0, as shipped in OpenSearch before 2.19, allows XSS because Markdown is not sanitized when previewing a header or footer.



- [https://github.com/Jflye/CVE-2024-54160-Opensearch-HTML-And-Injection-Stored-XSS](https://github.com/Jflye/CVE-2024-54160-Opensearch-HTML-And-Injection-Stored-XSS) :  ![starts](https://img.shields.io/github/stars/Jflye/CVE-2024-54160-Opensearch-HTML-And-Injection-Stored-XSS.svg) ![forks](https://img.shields.io/github/forks/Jflye/CVE-2024-54160-Opensearch-HTML-And-Injection-Stored-XSS.svg)

## CVE-2024-54152
 Angular Expressions provides expressions for the Angular.JS web framework as a standalone module. Prior to version 1.4.3, an attacker can write a malicious expression that escapes the sandbox to execute arbitrary code on the system. With a more complex (undisclosed) payload, one can get full access to Arbitrary code execution on the system. The problem has been patched in version 1.4.3 of Angular Expressions. Two possible workarounds are available. One may either disable access to `__proto__` globally or make sure that one uses the function with just one argument.



- [https://github.com/math-x-io/CVE-2024-54152-poc](https://github.com/math-x-io/CVE-2024-54152-poc) :  ![starts](https://img.shields.io/github/stars/math-x-io/CVE-2024-54152-poc.svg) ![forks](https://img.shields.io/github/forks/math-x-io/CVE-2024-54152-poc.svg)

## CVE-2024-54085
 AMI’s SPx contains
a vulnerability in the BMC where an Attacker may bypass authentication remotely through the Redfish Host Interface. A successful exploitation
of this vulnerability may lead to a loss of confidentiality, integrity, and/or
availability.



- [https://github.com/Mr-Zapi/CVE-2024-54085](https://github.com/Mr-Zapi/CVE-2024-54085) :  ![starts](https://img.shields.io/github/stars/Mr-Zapi/CVE-2024-54085.svg) ![forks](https://img.shields.io/github/forks/Mr-Zapi/CVE-2024-54085.svg)

## CVE-2024-53924
 Pycel through 1.0b30, when operating on an untrusted spreadsheet, allows code execution via a crafted formula in a cell, such as one beginning with the =IF(A1=200, eval("__import__('os').system( substring.



- [https://github.com/aelmosalamy/CVE-2024-53924](https://github.com/aelmosalamy/CVE-2024-53924) :  ![starts](https://img.shields.io/github/stars/aelmosalamy/CVE-2024-53924.svg) ![forks](https://img.shields.io/github/forks/aelmosalamy/CVE-2024-53924.svg)

## CVE-2024-53900
 Mongoose before 8.8.3 can improperly use $where in match, leading to search injection.



- [https://github.com/Gokul-Krishnan-V-R/CVE-2024-53900](https://github.com/Gokul-Krishnan-V-R/CVE-2024-53900) :  ![starts](https://img.shields.io/github/stars/Gokul-Krishnan-V-R/CVE-2024-53900.svg) ![forks](https://img.shields.io/github/forks/Gokul-Krishnan-V-R/CVE-2024-53900.svg)

## CVE-2024-53703
 A vulnerability in the SonicWall SMA100 SSLVPN firmware 10.2.1.13-72sv and earlier versions mod_httprp library loaded by the Apache web server allows remote attackers to cause Stack-based buffer overflow and potentially lead to code execution.



- [https://github.com/scrt/cve-2024-53703-poc](https://github.com/scrt/cve-2024-53703-poc) :  ![starts](https://img.shields.io/github/stars/scrt/cve-2024-53703-poc.svg) ![forks](https://img.shields.io/github/forks/scrt/cve-2024-53703-poc.svg)

## CVE-2024-53691
 A link following vulnerability has been reported to affect several QNAP operating system versions. If exploited, the vulnerability could allow remote attackers who have gained user access to traverse the file system to unintended locations.

We have already fixed the vulnerability in the following versions:
QTS 5.1.8.2823 build 20240712 and later
QTS 5.2.0.2802 build 20240620 and later
QuTS hero h5.1.8.2823 build 20240712 and later
QuTS hero h5.2.0.2802 build 20240620 and later



- [https://github.com/C411e/CVE-2024-53691](https://github.com/C411e/CVE-2024-53691) :  ![starts](https://img.shields.io/github/stars/C411e/CVE-2024-53691.svg) ![forks](https://img.shields.io/github/forks/C411e/CVE-2024-53691.svg)

## CVE-2024-53677
 File upload logic in Apache Struts is flawed. An attacker can manipulate file upload params to enable paths traversal and under some circumstances this can lead to uploading a malicious file which can be used to perform Remote Code Execution.

This issue affects Apache Struts: from 2.0.0 before 6.4.0.

Users are recommended to upgrade to version 6.4.0 at least and migrate to the new  file upload mechanism https://struts.apache.org/core-developers/file-upload . If you are not using an old file upload logic based on FileuploadInterceptor your application is safe.

You can find more details in  https://cwiki.apache.org/confluence/display/WW/S2-067



- [https://github.com/TAM-K592/CVE-2024-53677-S2-067](https://github.com/TAM-K592/CVE-2024-53677-S2-067) :  ![starts](https://img.shields.io/github/stars/TAM-K592/CVE-2024-53677-S2-067.svg) ![forks](https://img.shields.io/github/forks/TAM-K592/CVE-2024-53677-S2-067.svg)

- [https://github.com/cloudwafs/s2-067-CVE-2024-53677](https://github.com/cloudwafs/s2-067-CVE-2024-53677) :  ![starts](https://img.shields.io/github/stars/cloudwafs/s2-067-CVE-2024-53677.svg) ![forks](https://img.shields.io/github/forks/cloudwafs/s2-067-CVE-2024-53677.svg)

- [https://github.com/EQSTLab/CVE-2024-53677](https://github.com/EQSTLab/CVE-2024-53677) :  ![starts](https://img.shields.io/github/stars/EQSTLab/CVE-2024-53677.svg) ![forks](https://img.shields.io/github/forks/EQSTLab/CVE-2024-53677.svg)

- [https://github.com/XiaomingX/CVE-2024-53677-S2-067](https://github.com/XiaomingX/CVE-2024-53677-S2-067) :  ![starts](https://img.shields.io/github/stars/XiaomingX/CVE-2024-53677-S2-067.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/CVE-2024-53677-S2-067.svg)

- [https://github.com/yangyanglo/CVE-2024-53677](https://github.com/yangyanglo/CVE-2024-53677) :  ![starts](https://img.shields.io/github/stars/yangyanglo/CVE-2024-53677.svg) ![forks](https://img.shields.io/github/forks/yangyanglo/CVE-2024-53677.svg)

- [https://github.com/SeanRickerd/CVE-2024-53677](https://github.com/SeanRickerd/CVE-2024-53677) :  ![starts](https://img.shields.io/github/stars/SeanRickerd/CVE-2024-53677.svg) ![forks](https://img.shields.io/github/forks/SeanRickerd/CVE-2024-53677.svg)

- [https://github.com/c4oocO/CVE-2024-53677-Docker](https://github.com/c4oocO/CVE-2024-53677-Docker) :  ![starts](https://img.shields.io/github/stars/c4oocO/CVE-2024-53677-Docker.svg) ![forks](https://img.shields.io/github/forks/c4oocO/CVE-2024-53677-Docker.svg)

- [https://github.com/r007sec/CVE-2024-53677](https://github.com/r007sec/CVE-2024-53677) :  ![starts](https://img.shields.io/github/stars/r007sec/CVE-2024-53677.svg) ![forks](https://img.shields.io/github/forks/r007sec/CVE-2024-53677.svg)

- [https://github.com/dustblessnotdust/CVE-2024-53677-S2-067-thread](https://github.com/dustblessnotdust/CVE-2024-53677-S2-067-thread) :  ![starts](https://img.shields.io/github/stars/dustblessnotdust/CVE-2024-53677-S2-067-thread.svg) ![forks](https://img.shields.io/github/forks/dustblessnotdust/CVE-2024-53677-S2-067-thread.svg)

- [https://github.com/punitdarji/Apache-struts-cve-2024-53677](https://github.com/punitdarji/Apache-struts-cve-2024-53677) :  ![starts](https://img.shields.io/github/stars/punitdarji/Apache-struts-cve-2024-53677.svg) ![forks](https://img.shields.io/github/forks/punitdarji/Apache-struts-cve-2024-53677.svg)

- [https://github.com/BuludX/CVE-2024-53677](https://github.com/BuludX/CVE-2024-53677) :  ![starts](https://img.shields.io/github/stars/BuludX/CVE-2024-53677.svg) ![forks](https://img.shields.io/github/forks/BuludX/CVE-2024-53677.svg)

- [https://github.com/0xdeviner/CVE-2024-53677](https://github.com/0xdeviner/CVE-2024-53677) :  ![starts](https://img.shields.io/github/stars/0xdeviner/CVE-2024-53677.svg) ![forks](https://img.shields.io/github/forks/0xdeviner/CVE-2024-53677.svg)

- [https://github.com/0xPThree/struts_cve-2024-53677](https://github.com/0xPThree/struts_cve-2024-53677) :  ![starts](https://img.shields.io/github/stars/0xPThree/struts_cve-2024-53677.svg) ![forks](https://img.shields.io/github/forks/0xPThree/struts_cve-2024-53677.svg)

## CVE-2024-53617
 A Cross Site Scripting vulnerability in LibrePhotos before commit 32237 allows attackers to takeover any account via uploading an HTML file on behalf of the admin user using IDOR in file upload.



- [https://github.com/ii5mai1/CVE-2024-53617](https://github.com/ii5mai1/CVE-2024-53617) :  ![starts](https://img.shields.io/github/stars/ii5mai1/CVE-2024-53617.svg) ![forks](https://img.shields.io/github/forks/ii5mai1/CVE-2024-53617.svg)

## CVE-2024-53615
 A command injection vulnerability in the video thumbnail rendering component of Karl Ward's files.gallery v0.3.0 through 0.11.0 allows remote attackers to execute arbitrary code via a crafted video file.



- [https://github.com/beune/CVE-2024-53615](https://github.com/beune/CVE-2024-53615) :  ![starts](https://img.shields.io/github/stars/beune/CVE-2024-53615.svg) ![forks](https://img.shields.io/github/forks/beune/CVE-2024-53615.svg)

## CVE-2024-53591
 An issue in the login page of Seclore v3.27.5.0 allows attackers to bypass authentication via a brute force attack.



- [https://github.com/aljoharasubaie/CVE-2024-53591](https://github.com/aljoharasubaie/CVE-2024-53591) :  ![starts](https://img.shields.io/github/stars/aljoharasubaie/CVE-2024-53591.svg) ![forks](https://img.shields.io/github/forks/aljoharasubaie/CVE-2024-53591.svg)

## CVE-2024-53522
 Bangkok Medical Software HOSxP XE v4.64.11.3 was discovered to contain a hardcoded IDEA Key-IV pair in the HOSxPXE4.exe and HOS-WIN32.INI components. This allows attackers to access sensitive information.



- [https://github.com/Safecloudth/CVE-2024-53522](https://github.com/Safecloudth/CVE-2024-53522) :  ![starts](https://img.shields.io/github/stars/Safecloudth/CVE-2024-53522.svg) ![forks](https://img.shields.io/github/forks/Safecloudth/CVE-2024-53522.svg)

## CVE-2024-53476
 A race condition vulnerability in SimplCommerce at commit 230310c8d7a0408569b292c5a805c459d47a1d8f allows attackers to bypass inventory restrictions by simultaneously submitting purchase requests from multiple accounts for the same product. This can lead to overselling when stock is limited, as the system fails to accurately track inventory under high concurrency, resulting in potential loss and unfulfilled orders.



- [https://github.com/AbdullahAlmutawa/CVE-2024-53476](https://github.com/AbdullahAlmutawa/CVE-2024-53476) :  ![starts](https://img.shields.io/github/stars/AbdullahAlmutawa/CVE-2024-53476.svg) ![forks](https://img.shields.io/github/forks/AbdullahAlmutawa/CVE-2024-53476.svg)

## CVE-2024-53376
 CyberPanel before 2.3.8 allows remote authenticated users to execute arbitrary commands via shell metacharacters in the phpSelection field to the websites/submitWebsiteCreation URI.



- [https://github.com/ThottySploity/CVE-2024-53376](https://github.com/ThottySploity/CVE-2024-53376) :  ![starts](https://img.shields.io/github/stars/ThottySploity/CVE-2024-53376.svg) ![forks](https://img.shields.io/github/forks/ThottySploity/CVE-2024-53376.svg)

## CVE-2024-53345
 An authenticated arbitrary file upload vulnerability in Car Rental Management System v1.0 to v1.3 allows attackers to execute arbitrary code via uploading a crafted file.



- [https://github.com/ShadowByte1/CVE-2024-53345](https://github.com/ShadowByte1/CVE-2024-53345) :  ![starts](https://img.shields.io/github/stars/ShadowByte1/CVE-2024-53345.svg) ![forks](https://img.shields.io/github/forks/ShadowByte1/CVE-2024-53345.svg)

## CVE-2024-53259
 quic-go is an implementation of the QUIC protocol in Go. An off-path attacker can inject an ICMP Packet Too Large packet. Since affected quic-go versions used IP_PMTUDISC_DO, the kernel would then return a "message too large" error on sendmsg, i.e. when quic-go attempts to send a packet that exceeds the MTU claimed in that ICMP packet. By setting this value to smaller than 1200 bytes (the minimum MTU for QUIC), the attacker can disrupt a QUIC connection. Crucially, this can be done after completion of the handshake, thereby circumventing any TCP fallback that might be implemented on the application layer (for example, many browsers fall back to HTTP over TCP if they're unable to establish a QUIC connection). The attacker needs to at least know the client's IP and port tuple to mount an attack. This vulnerability is fixed in 0.48.2.



- [https://github.com/kota-yata/cve-2024-53259](https://github.com/kota-yata/cve-2024-53259) :  ![starts](https://img.shields.io/github/stars/kota-yata/cve-2024-53259.svg) ![forks](https://img.shields.io/github/forks/kota-yata/cve-2024-53259.svg)

## CVE-2024-53255
 BoidCMS is a free and open-source flat file CMS for building simple websites and blogs, developed using PHP and uses JSON as a database. In affected versions a reflected Cross-site Scripting (XSS) vulnerability exists in the /admin?page=media endpoint in the file parameter, allowing an attacker to inject arbitrary JavaScript code. This code could be used to steal the user's session cookie, perform phishing attacks, or deface the website. This issue has been addressed in version 2.1.2 and all users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/0x4M3R/CVE-2024-53255](https://github.com/0x4M3R/CVE-2024-53255) :  ![starts](https://img.shields.io/github/stars/0x4M3R/CVE-2024-53255.svg) ![forks](https://img.shields.io/github/forks/0x4M3R/CVE-2024-53255.svg)

## CVE-2024-53027
 Transient DOS may occur while processing the country IE.



- [https://github.com/ladyg00se/CVE-2024-53027-WIP](https://github.com/ladyg00se/CVE-2024-53027-WIP) :  ![starts](https://img.shields.io/github/stars/ladyg00se/CVE-2024-53027-WIP.svg) ![forks](https://img.shields.io/github/forks/ladyg00se/CVE-2024-53027-WIP.svg)

## CVE-2024-52940
 AnyDesk through 8.1.0 on Windows, when Allow Direct Connections is enabled, inadvertently exposes a public IP address within network traffic. The attacker must know the victim's AnyDesk ID.



- [https://github.com/MKultra6969/AnySniff](https://github.com/MKultra6969/AnySniff) :  ![starts](https://img.shields.io/github/stars/MKultra6969/AnySniff.svg) ![forks](https://img.shields.io/github/forks/MKultra6969/AnySniff.svg)

## CVE-2024-52800
 veraPDF is an open source PDF/A validation library. Executing policy checks using custom schematron files via the CLI invokes an XSL transformation that may theoretically lead to a remote code execution (RCE) vulnerability. This doesn't affect the standard validation and policy checks functionality, veraPDF's common use cases. Most veraPDF users don't insert any custom XSLT code into policy profiles, which are based on Schematron syntax rather than direct XSL transforms. For users who do, only load custom policy files from sources you trust. This issue has not yet been patched. Users are advised to be cautious of XSLT code until a patch is available.



- [https://github.com/JAckLosingHeart/GHSA-4cx5-89vm-833x-POC](https://github.com/JAckLosingHeart/GHSA-4cx5-89vm-833x-POC) :  ![starts](https://img.shields.io/github/stars/JAckLosingHeart/GHSA-4cx5-89vm-833x-POC.svg) ![forks](https://img.shields.io/github/forks/JAckLosingHeart/GHSA-4cx5-89vm-833x-POC.svg)

## CVE-2024-52794
 Discourse is an open source platform for community discussion. Users clicking on the lightbox thumbnails could be affected. This problem is patched in the latest version of Discourse. Users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/Beesco00/CVE-2024-52794-Discourse-Stored-XSS](https://github.com/Beesco00/CVE-2024-52794-Discourse-Stored-XSS) :  ![starts](https://img.shields.io/github/stars/Beesco00/CVE-2024-52794-Discourse-Stored-XSS.svg) ![forks](https://img.shields.io/github/forks/Beesco00/CVE-2024-52794-Discourse-Stored-XSS.svg)

## CVE-2024-52711
 DI-8100 v16.07.26A1 is vulnerable to Buffer Overflow In the ip_position_asp function via the ip parameter.



- [https://github.com/14mb1v45h/cyberspace-CVE-2024-52711](https://github.com/14mb1v45h/cyberspace-CVE-2024-52711) :  ![starts](https://img.shields.io/github/stars/14mb1v45h/cyberspace-CVE-2024-52711.svg) ![forks](https://img.shields.io/github/forks/14mb1v45h/cyberspace-CVE-2024-52711.svg)

## CVE-2024-52550
 Jenkins Pipeline: Groovy Plugin 3990.vd281dd77a_388 and earlier, except 3975.3977.v478dd9e956c3 does not check whether the main (Jenkinsfile) script for a rebuilt build is approved, allowing attackers with Item/Build permission to rebuild a previous build whose (Jenkinsfile) script is no longer approved.



- [https://github.com/Anton-ai111/CVE-2024-52550](https://github.com/Anton-ai111/CVE-2024-52550) :  ![starts](https://img.shields.io/github/stars/Anton-ai111/CVE-2024-52550.svg) ![forks](https://img.shields.io/github/forks/Anton-ai111/CVE-2024-52550.svg)

## CVE-2024-52510
 The Nextcloud Desktop Client is a tool to synchronize files from Nextcloud Server with your computer. The Desktop client did not stop with an error but allowed by-passing the signature validation, if a manipulated server sends an empty initial signature. It is recommended that the Nextcloud Desktop client is upgraded to 3.14.2 or later.



- [https://github.com/d-xuan/CVE-2024-52510](https://github.com/d-xuan/CVE-2024-52510) :  ![starts](https://img.shields.io/github/stars/d-xuan/CVE-2024-52510.svg) ![forks](https://img.shields.io/github/forks/d-xuan/CVE-2024-52510.svg)

## CVE-2024-52475
 Authentication Bypass Using an Alternate Path or Channel vulnerability in Automation Web Platform Wawp allows Authentication Bypass.This issue affects Wawp: from n/a before 3.0.18.



- [https://github.com/ubaydev/CVE-2024-52475](https://github.com/ubaydev/CVE-2024-52475) :  ![starts](https://img.shields.io/github/stars/ubaydev/CVE-2024-52475.svg) ![forks](https://img.shields.io/github/forks/ubaydev/CVE-2024-52475.svg)

## CVE-2024-52433
 Deserialization of Untrusted Data vulnerability in Mindstien Technologies My Geo Posts Free allows Object Injection.This issue affects My Geo Posts Free: from n/a through 1.2.



- [https://github.com/RandomRobbieBF/CVE-2024-52433](https://github.com/RandomRobbieBF/CVE-2024-52433) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-52433.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-52433.svg)

## CVE-2024-52430
 Deserialization of Untrusted Data vulnerability in Lis Lis Video Gallery allows Object Injection.This issue affects Lis Video Gallery: from n/a through 0.2.1.



- [https://github.com/RandomRobbieBF/CVE-2024-52430](https://github.com/RandomRobbieBF/CVE-2024-52430) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-52430.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-52430.svg)

## CVE-2024-52429
 Unrestricted Upload of File with Dangerous Type vulnerability in Anton Hoelstad WP Quick Setup allows Upload a Web Shell to a Web Server.This issue affects WP Quick Setup: from n/a through 2.0.



- [https://github.com/RandomRobbieBF/CVE-2024-52429](https://github.com/RandomRobbieBF/CVE-2024-52429) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-52429.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-52429.svg)

## CVE-2024-52382
 Missing Authorization vulnerability in Medma Technologies Matix Popup Builder allows Privilege Escalation.This issue affects Matix Popup Builder: from n/a through 1.0.0.



- [https://github.com/RandomRobbieBF/CVE-2024-52382](https://github.com/RandomRobbieBF/CVE-2024-52382) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-52382.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-52382.svg)

## CVE-2024-52380
 Unrestricted Upload of File with Dangerous Type vulnerability in Softpulse Infotech Picsmize allows Upload a Web Shell to a Web Server.This issue affects Picsmize: from n/a through 1.0.0.



- [https://github.com/RandomRobbieBF/CVE-2024-52380](https://github.com/RandomRobbieBF/CVE-2024-52380) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-52380.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-52380.svg)

- [https://github.com/0xshoriful/CVE-2024-52380](https://github.com/0xshoriful/CVE-2024-52380) :  ![starts](https://img.shields.io/github/stars/0xshoriful/CVE-2024-52380.svg) ![forks](https://img.shields.io/github/forks/0xshoriful/CVE-2024-52380.svg)

## CVE-2024-52318
 Incorrect object recycling and reuse vulnerability in Apache Tomcat.

This issue affects Apache Tomcat: 11.0.0, 10.1.31, 9.0.96.

Users are recommended to upgrade to version 11.0.1, 10.1.32 or 9.0.97, which fixes the issue.



- [https://github.com/TAM-K592/CVE-2024-52318](https://github.com/TAM-K592/CVE-2024-52318) :  ![starts](https://img.shields.io/github/stars/TAM-K592/CVE-2024-52318.svg) ![forks](https://img.shields.io/github/forks/TAM-K592/CVE-2024-52318.svg)

## CVE-2024-52317
 Incorrect object re-cycling and re-use vulnerability in Apache Tomcat. Incorrect recycling of the request and response used by HTTP/2 requests 
could lead to request and/or response mix-up between users.

This issue affects Apache Tomcat: from 11.0.0-M23 through 11.0.0-M26, from 10.1.27 through 10.1.30, from 9.0.92 through 9.0.95.

Users are recommended to upgrade to version 11.0.0, 10.1.31 or 9.0.96, which fixes the issue.



- [https://github.com/TAM-K592/CVE-2024-52317](https://github.com/TAM-K592/CVE-2024-52317) :  ![starts](https://img.shields.io/github/stars/TAM-K592/CVE-2024-52317.svg) ![forks](https://img.shields.io/github/forks/TAM-K592/CVE-2024-52317.svg)

## CVE-2024-52316
 Unchecked Error Condition vulnerability in Apache Tomcat. If Tomcat is configured to use a custom Jakarta Authentication (formerly JASPIC) ServerAuthContext component which may throw an exception during the authentication process without explicitly setting an HTTP status to indicate failure, the authentication may not fail, allowing the user to bypass the authentication process. There are no known Jakarta Authentication components that behave in this way.

This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.0-M26, from 10.1.0-M1 through 10.1.30, from 9.0.0-M1 through 9.0.95.

The following versions were EOL at the time the CVE was created but are 
known to be affected: 8.5.0 though 8.5.100.


Users are recommended to upgrade to version 11.0.0, 10.1.31 or 9.0.96, which fix the issue.



- [https://github.com/TAM-K592/CVE-2024-52316](https://github.com/TAM-K592/CVE-2024-52316) :  ![starts](https://img.shields.io/github/stars/TAM-K592/CVE-2024-52316.svg) ![forks](https://img.shields.io/github/forks/TAM-K592/CVE-2024-52316.svg)

## CVE-2024-52302
 common-user-management is a robust Spring Boot application featuring user management services designed to control user access dynamically. There is a critical security vulnerability in the application endpoint /api/v1/customer/profile-picture. This endpoint allows file uploads without proper validation or restrictions, enabling attackers to upload malicious files that can lead to Remote Code Execution (RCE).



- [https://github.com/d3sca/CVE-2024-52302](https://github.com/d3sca/CVE-2024-52302) :  ![starts](https://img.shields.io/github/stars/d3sca/CVE-2024-52302.svg) ![forks](https://img.shields.io/github/forks/d3sca/CVE-2024-52302.svg)

## CVE-2024-52301
 Laravel is a web application framework. When the register_argc_argv php directive is set to on , and users call any URL with a special crafted query string, they are able to change the environment used by the framework when handling the request. The vulnerability fixed in 6.20.45, 7.30.7, 8.83.28, 9.52.17, 10.48.23, and 11.31.0. The framework now ignores argv values for environment detection on non-cli SAPIs.



- [https://github.com/Nyamort/CVE-2024-52301](https://github.com/Nyamort/CVE-2024-52301) :  ![starts](https://img.shields.io/github/stars/Nyamort/CVE-2024-52301.svg) ![forks](https://img.shields.io/github/forks/Nyamort/CVE-2024-52301.svg)

- [https://github.com/martinhaunschmid/CVE-2024-52301-Research](https://github.com/martinhaunschmid/CVE-2024-52301-Research) :  ![starts](https://img.shields.io/github/stars/martinhaunschmid/CVE-2024-52301-Research.svg) ![forks](https://img.shields.io/github/forks/martinhaunschmid/CVE-2024-52301-Research.svg)

- [https://github.com/nanwinata/CVE-2024-52301](https://github.com/nanwinata/CVE-2024-52301) :  ![starts](https://img.shields.io/github/stars/nanwinata/CVE-2024-52301.svg) ![forks](https://img.shields.io/github/forks/nanwinata/CVE-2024-52301.svg)

## CVE-2024-52033
 Exposure of sensitive system information to an unauthorized control sphere issue exists in Rakuten Turbo 5G firmware version V1.3.18 and earlier. If this vulnerability is exploited, a remote unauthenticated attacker may obtain information of the other devices connected through the Wi-Fi.



- [https://github.com/0xNslabs/Rakuten5GTurboAPI](https://github.com/0xNslabs/Rakuten5GTurboAPI) :  ![starts](https://img.shields.io/github/stars/0xNslabs/Rakuten5GTurboAPI.svg) ![forks](https://img.shields.io/github/forks/0xNslabs/Rakuten5GTurboAPI.svg)

## CVE-2024-52002
 Combodo iTop is a simple, web based IT Service Management tool. Several url endpoints are subject to a Cross-Site Request Forgery (CSRF) vulnerability. Please refer to the linked GHSA for the complete list. This issue has been addressed in version 3.2.0 and all users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/Harshit-Mashru/iTop-CVEs-exploit](https://github.com/Harshit-Mashru/iTop-CVEs-exploit) :  ![starts](https://img.shields.io/github/stars/Harshit-Mashru/iTop-CVEs-exploit.svg) ![forks](https://img.shields.io/github/forks/Harshit-Mashru/iTop-CVEs-exploit.svg)

## CVE-2024-51996
 Symphony process is a module for the Symphony PHP framework which executes commands in sub-processes. When consuming a persisted remember-me cookie, Symfony does not check if the username persisted in the database matches the username attached with the cookie, leading to authentication bypass. This vulnerability is fixed in 5.4.47, 6.4.15, and 7.1.8.



- [https://github.com/moften/CVE-2024-51996](https://github.com/moften/CVE-2024-51996) :  ![starts](https://img.shields.io/github/stars/moften/CVE-2024-51996.svg) ![forks](https://img.shields.io/github/forks/moften/CVE-2024-51996.svg)

## CVE-2024-51984
 An authenticated attacker can reconfigure the target device to use an external service (such as LDAP or FTP) controlled by the attacker. If an existing password is present for an external service, the attacker can force the target device to authenticate to an attacker controlled device using the existing credentials for that external service. In the case of an external LDAP or FTP service, this will disclose the plaintext password for that external service to the attacker.



- [https://github.com/sfewer-r7/BrotherVulnerabilities](https://github.com/sfewer-r7/BrotherVulnerabilities) :  ![starts](https://img.shields.io/github/stars/sfewer-r7/BrotherVulnerabilities.svg) ![forks](https://img.shields.io/github/forks/sfewer-r7/BrotherVulnerabilities.svg)

## CVE-2024-51983
 An unauthenticated attacker who can connect to the Web Services feature (HTTP TCP port 80) can issue a WS-Scan SOAP request containing an unexpected JobToken value which will crash the target device. The device will reboot, after which the attacker can reissue the command to repeatedly crash the device.



- [https://github.com/sfewer-r7/BrotherVulnerabilities](https://github.com/sfewer-r7/BrotherVulnerabilities) :  ![starts](https://img.shields.io/github/stars/sfewer-r7/BrotherVulnerabilities.svg) ![forks](https://img.shields.io/github/forks/sfewer-r7/BrotherVulnerabilities.svg)

## CVE-2024-51982
 An unauthenticated attacker who can connect to TCP port 9100 can issue a Printer Job Language (PJL) command that will crash the target device. The device will reboot, after which the attacker can reissue the command to repeatedly crash the device. A malformed PJL variable FORMLINES is set to a non number value causing the target to crash.



- [https://github.com/sfewer-r7/BrotherVulnerabilities](https://github.com/sfewer-r7/BrotherVulnerabilities) :  ![starts](https://img.shields.io/github/stars/sfewer-r7/BrotherVulnerabilities.svg) ![forks](https://img.shields.io/github/forks/sfewer-r7/BrotherVulnerabilities.svg)

## CVE-2024-51981
 An unauthenticated attacker may perform a blind server side request forgery (SSRF), due to a CLRF injection issue that can be leveraged to perform HTTP request smuggling. This SSRF leverages the WS-Addressing feature used during a WS-Eventing subscription SOAP operation. The attacker can control all the HTTP data sent in the SSRF connection, but the attacker can not receive any data back from this connection.



- [https://github.com/sfewer-r7/BrotherVulnerabilities](https://github.com/sfewer-r7/BrotherVulnerabilities) :  ![starts](https://img.shields.io/github/stars/sfewer-r7/BrotherVulnerabilities.svg) ![forks](https://img.shields.io/github/forks/sfewer-r7/BrotherVulnerabilities.svg)

## CVE-2024-51980
 An unauthenticated attacker may perform a limited server side request forgery (SSRF), forcing the target device to open a TCP connection to an arbitrary port number on an arbitrary IP address. This SSRF leverages the WS-Addressing ReplyTo element in a Web service (HTTP TCP port 80) SOAP request. The attacker can not control the data sent in the SSRF connection, nor can the attacker receive any data back. This SSRF is suitable for TCP port scanning of an internal network when the Web service (HTTP TCP port 80) is exposed across a network segment.



- [https://github.com/sfewer-r7/BrotherVulnerabilities](https://github.com/sfewer-r7/BrotherVulnerabilities) :  ![starts](https://img.shields.io/github/stars/sfewer-r7/BrotherVulnerabilities.svg) ![forks](https://img.shields.io/github/forks/sfewer-r7/BrotherVulnerabilities.svg)

## CVE-2024-51979
 An authenticated attacker may trigger a stack based buffer overflow by performing a malformed request to either the HTTP service (TCP port 80), the HTTPS service (TCP port 443), or the IPP service (TCP port 631). The malformed request will contain an empty Origin header value and a malformed Referer header value. The Referer header value will trigger a stack based buffer overflow when the host value in the Referer header is processed and is greater than 64 bytes in length.



- [https://github.com/sfewer-r7/BrotherVulnerabilities](https://github.com/sfewer-r7/BrotherVulnerabilities) :  ![starts](https://img.shields.io/github/stars/sfewer-r7/BrotherVulnerabilities.svg) ![forks](https://img.shields.io/github/forks/sfewer-r7/BrotherVulnerabilities.svg)

## CVE-2024-51978
 An unauthenticated attacker who knows the target device's serial number, can generate the default administrator password for the device. An unauthenticated attacker can first discover the target device's serial number via CVE-2024-51977 over HTTP/HTTPS/IPP, or via a PJL request, or via an SNMP request.



- [https://github.com/sfewer-r7/BrotherVulnerabilities](https://github.com/sfewer-r7/BrotherVulnerabilities) :  ![starts](https://img.shields.io/github/stars/sfewer-r7/BrotherVulnerabilities.svg) ![forks](https://img.shields.io/github/forks/sfewer-r7/BrotherVulnerabilities.svg)

## CVE-2024-51977
 An unauthenticated attacker who can access either the HTTP service (TCP port 80), the HTTPS service (TCP port 443), or the IPP service (TCP port 631), can leak several pieces of sensitive information from a vulnerable device. The URI path /etc/mnt_info.csv can be accessed via a GET request and no authentication is required. The returned result is a comma separated value (CSV) table of information. The leaked information includes the device’s model, firmware version, IP address, and serial number.



- [https://github.com/sfewer-r7/BrotherVulnerabilities](https://github.com/sfewer-r7/BrotherVulnerabilities) :  ![starts](https://img.shields.io/github/stars/sfewer-r7/BrotherVulnerabilities.svg) ![forks](https://img.shields.io/github/forks/sfewer-r7/BrotherVulnerabilities.svg)

## CVE-2024-51818
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in NotFound Fancy Product Designer. This issue affects Fancy Product Designer: from n/a through 6.4.3.



- [https://github.com/RandomRobbieBF/CVE-2024-51818](https://github.com/RandomRobbieBF/CVE-2024-51818) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-51818.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-51818.svg)

## CVE-2024-51793
 Unrestricted Upload of File with Dangerous Type vulnerability in Webful Creations Computer Repair Shop allows Upload a Web Shell to a Web Server.This issue affects Computer Repair Shop: from n/a through 3.8115.



- [https://github.com/KTN1990/CVE-2024-51793](https://github.com/KTN1990/CVE-2024-51793) :  ![starts](https://img.shields.io/github/stars/KTN1990/CVE-2024-51793.svg) ![forks](https://img.shields.io/github/forks/KTN1990/CVE-2024-51793.svg)

## CVE-2024-51747
 Kanboard is project management software that focuses on the Kanban methodology. An authenticated Kanboard admin can read and delete arbitrary files from the server. File attachments, that are viewable or downloadable in Kanboard are resolved through its `path` entry in the `project_has_files`  SQLite db. Thus, an attacker who can upload a modified sqlite.db through the dedicated feature, can set arbitrary file links, by abusing path traversals. Once the modified db is uploaded and the project page is accessed, a file download can be triggered and all files, readable in the context of the Kanboard application permissions, can be downloaded. This issue has been addressed in version 1.2.42 and all users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/l20170217b/CVE-2024-51747](https://github.com/l20170217b/CVE-2024-51747) :  ![starts](https://img.shields.io/github/stars/l20170217b/CVE-2024-51747.svg) ![forks](https://img.shields.io/github/forks/l20170217b/CVE-2024-51747.svg)

## CVE-2024-51665
 Server-Side Request Forgery (SSRF) vulnerability in Noor alam Magical Addons For Elementor allows Server Side Request Forgery.This issue affects Magical Addons For Elementor: from n/a through 1.2.1.



- [https://github.com/RandomRobbieBF/CVE-2024-51665](https://github.com/RandomRobbieBF/CVE-2024-51665) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-51665.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-51665.svg)

## CVE-2024-51567
 upgrademysqlstatus in databases/views.py in CyberPanel (aka Cyber Panel) before 5b08cd6 allows remote attackers to bypass authentication and execute arbitrary commands via /dataBases/upgrademysqlstatus by bypassing secMiddleware (which is only for a POST request) and using shell metacharacters in the statusfile property, as exploited in the wild in October 2024 by PSAUX. Versions through 2.3.6 and (unpatched) 2.3.7 are affected.



- [https://github.com/XiaomingX/cve-2024-51567-poc](https://github.com/XiaomingX/cve-2024-51567-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-51567-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-51567-poc.svg)

- [https://github.com/thehash007/CVE-2024-51567-RCE-EXPLOIT](https://github.com/thehash007/CVE-2024-51567-RCE-EXPLOIT) :  ![starts](https://img.shields.io/github/stars/thehash007/CVE-2024-51567-RCE-EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/thehash007/CVE-2024-51567-RCE-EXPLOIT.svg)

## CVE-2024-51442
 Command Injection in Minidlna version v1.3.3 and before allows an attacker to execute arbitrary OS commands via a specially crafted minidlna.conf configuration file.



- [https://github.com/mselbrede/CVE-2024-51442](https://github.com/mselbrede/CVE-2024-51442) :  ![starts](https://img.shields.io/github/stars/mselbrede/CVE-2024-51442.svg) ![forks](https://img.shields.io/github/forks/mselbrede/CVE-2024-51442.svg)

## CVE-2024-51228
 An issue in TOTOLINK-CX-A3002RU V1.0.4-B20171106.1512 and TOTOLINK-CX-N150RT V2.1.6-B20171121.1002 and TOTOLINK-CX-N300RT V2.1.6-B20170724.1420 and TOTOLINK-CX-N300RT V2.1.8-B20171113.1408 and TOTOLINK-CX-N300RT V2.1.8-B20191010.1107 and TOTOLINK-CX-N302RE V2.0.2-B20170511.1523 allows a remote attacker to execute arbitrary code via the /boafrm/formSysCmd component.



- [https://github.com/tequilasunsh1ne/CVE_2024_51228](https://github.com/tequilasunsh1ne/CVE_2024_51228) :  ![starts](https://img.shields.io/github/stars/tequilasunsh1ne/CVE_2024_51228.svg) ![forks](https://img.shields.io/github/forks/tequilasunsh1ne/CVE_2024_51228.svg)

## CVE-2024-51179
 An issue in Open 5GS v.2.7.1 allows a remote attacker to cause a denial of service via the Network Function Virtualizations (NFVs) such as the User Plane Function (UPF) and the Session Management Function (SMF), The Packet Data Unit (PDU) session establishment process.



- [https://github.com/Lakshmirnr/CVE-2024-51179](https://github.com/Lakshmirnr/CVE-2024-51179) :  ![starts](https://img.shields.io/github/stars/Lakshmirnr/CVE-2024-51179.svg) ![forks](https://img.shields.io/github/forks/Lakshmirnr/CVE-2024-51179.svg)

## CVE-2024-51032
 A Cross-site Scripting (XSS) vulnerability in manage_recipient.php of Sourcecodester Toll Tax Management System 1.0 allows remote authenticated users to inject arbitrary web scripts via the "owner" input field.



- [https://github.com/Shree-Chandragiri/CVE-2024-51032](https://github.com/Shree-Chandragiri/CVE-2024-51032) :  ![starts](https://img.shields.io/github/stars/Shree-Chandragiri/CVE-2024-51032.svg) ![forks](https://img.shields.io/github/forks/Shree-Chandragiri/CVE-2024-51032.svg)

## CVE-2024-51031
 A Cross-site Scripting (XSS) vulnerability in manage_account.php in Sourcecodester Cab Management System 1.0 allows remote authenticated users to inject arbitrary web scripts via the "First Name," "Middle Name," and "Last Name" fields.



- [https://github.com/vighneshnair7/CVE-2024-51031](https://github.com/vighneshnair7/CVE-2024-51031) :  ![starts](https://img.shields.io/github/stars/vighneshnair7/CVE-2024-51031.svg) ![forks](https://img.shields.io/github/forks/vighneshnair7/CVE-2024-51031.svg)

## CVE-2024-51030
 A SQL injection vulnerability in manage_client.php and view_cab.php of Sourcecodester Cab Management System 1.0 allows remote attackers to execute arbitrary SQL commands via the id parameter, leading to unauthorized access and potential compromise of sensitive data within the database.



- [https://github.com/vighneshnair7/CVE-2024-51030](https://github.com/vighneshnair7/CVE-2024-51030) :  ![starts](https://img.shields.io/github/stars/vighneshnair7/CVE-2024-51030.svg) ![forks](https://img.shields.io/github/forks/vighneshnair7/CVE-2024-51030.svg)

## CVE-2024-51026
 The NetAdmin IAM system (version 4.0.30319) has a Cross Site Scripting (XSS) vulnerability in the /BalloonSave.ashx endpoint, where it is possible to inject a malicious payload into the Content= field.



- [https://github.com/BrotherOfJhonny/CVE-2024-51026_Overview](https://github.com/BrotherOfJhonny/CVE-2024-51026_Overview) :  ![starts](https://img.shields.io/github/stars/BrotherOfJhonny/CVE-2024-51026_Overview.svg) ![forks](https://img.shields.io/github/forks/BrotherOfJhonny/CVE-2024-51026_Overview.svg)

## CVE-2024-50986
 An issue in Clementine v.1.3.1 allows a local attacker to execute arbitrary code via a crafted DLL file.



- [https://github.com/riftsandroses/CVE-2024-50986](https://github.com/riftsandroses/CVE-2024-50986) :  ![starts](https://img.shields.io/github/stars/riftsandroses/CVE-2024-50986.svg) ![forks](https://img.shields.io/github/forks/riftsandroses/CVE-2024-50986.svg)

## CVE-2024-50972
 A SQL injection vulnerability in printtool.php of Itsourcecode Construction Management System 1.0 allows remote attackers to execute arbitrary SQL commands via the borrow_id parameter.



- [https://github.com/Akhlak2511/CVE-2024-50972](https://github.com/Akhlak2511/CVE-2024-50972) :  ![starts](https://img.shields.io/github/stars/Akhlak2511/CVE-2024-50972.svg) ![forks](https://img.shields.io/github/forks/Akhlak2511/CVE-2024-50972.svg)

## CVE-2024-50971
 A SQL injection vulnerability in print.php of Itsourcecode Construction Management System 1.0 allows remote attackers to execute arbitrary SQL commands via the map_id parameter.



- [https://github.com/Akhlak2511/CVE-2024-50971](https://github.com/Akhlak2511/CVE-2024-50971) :  ![starts](https://img.shields.io/github/stars/Akhlak2511/CVE-2024-50971.svg) ![forks](https://img.shields.io/github/forks/Akhlak2511/CVE-2024-50971.svg)

## CVE-2024-50970
 A SQL injection vulnerability in orderview1.php of Itsourcecode Online Furniture Shopping Project 1.0 allows remote attackers to execute arbitrary SQL commands via the id parameter.



- [https://github.com/Akhlak2511/CVE-2024-50970](https://github.com/Akhlak2511/CVE-2024-50970) :  ![starts](https://img.shields.io/github/stars/Akhlak2511/CVE-2024-50970.svg) ![forks](https://img.shields.io/github/forks/Akhlak2511/CVE-2024-50970.svg)

## CVE-2024-50969
 A Reflected cross-site scripting (XSS) vulnerability in browse.php of Code-projects Jonnys Liquor 1.0 allows remote attackers to inject arbitrary web scripts or HTML via the search parameter.



- [https://github.com/Akhlak2511/CVE-2024-50969](https://github.com/Akhlak2511/CVE-2024-50969) :  ![starts](https://img.shields.io/github/stars/Akhlak2511/CVE-2024-50969.svg) ![forks](https://img.shields.io/github/forks/Akhlak2511/CVE-2024-50969.svg)

## CVE-2024-50968
 A business logic vulnerability exists in the Add to Cart function of itsourcecode Agri-Trading Online Shopping System 1.0, which allows remote attackers to manipulate the quant parameter when adding a product to the cart. By setting the quantity value to -0, an attacker can exploit a flaw in the application's total price calculation logic. This vulnerability causes the total price to be reduced to zero, allowing the attacker to add items to the cart and proceed to checkout.



- [https://github.com/Akhlak2511/CVE-2024-50968](https://github.com/Akhlak2511/CVE-2024-50968) :  ![starts](https://img.shields.io/github/stars/Akhlak2511/CVE-2024-50968.svg) ![forks](https://img.shields.io/github/forks/Akhlak2511/CVE-2024-50968.svg)

## CVE-2024-50945
 An improper access control vulnerability exists in SimplCommerce at commit 230310c8d7a0408569b292c5a805c459d47a1d8f, allowing users to submit reviews without verifying if they have purchased the product.



- [https://github.com/AbdullahAlmutawa/CVE-2024-50945](https://github.com/AbdullahAlmutawa/CVE-2024-50945) :  ![starts](https://img.shields.io/github/stars/AbdullahAlmutawa/CVE-2024-50945.svg) ![forks](https://img.shields.io/github/forks/AbdullahAlmutawa/CVE-2024-50945.svg)

## CVE-2024-50944
 Integer overflow vulnerability exists in SimplCommerce at commit 230310c8d7a0408569b292c5a805c459d47a1d8f in the shopping cart functionality. The issue lies in the quantity parameter in the CartController's AddToCart method.



- [https://github.com/AbdullahAlmutawa/CVE-2024-50944](https://github.com/AbdullahAlmutawa/CVE-2024-50944) :  ![starts](https://img.shields.io/github/stars/AbdullahAlmutawa/CVE-2024-50944.svg) ![forks](https://img.shields.io/github/forks/AbdullahAlmutawa/CVE-2024-50944.svg)

## CVE-2024-50849
 A Stored Cross-Site Scripting (XSS) vulnerability in the "Rules" functionality of WorldServer v11.8.2 allows a remote authenticated attacker to execute arbitrary JavaScript code.



- [https://github.com/Wh1teSnak3/CVE-2024-50849](https://github.com/Wh1teSnak3/CVE-2024-50849) :  ![starts](https://img.shields.io/github/stars/Wh1teSnak3/CVE-2024-50849.svg) ![forks](https://img.shields.io/github/forks/Wh1teSnak3/CVE-2024-50849.svg)

## CVE-2024-50848
 An XML External Entity (XXE) vulnerability in the Import object and Translation Memory import functionalities of WorldServer v11.8.2 to access sensitive information and execute arbitrary commands via supplying a crafted .tmx file.



- [https://github.com/Wh1teSnak3/CVE-2024-50848](https://github.com/Wh1teSnak3/CVE-2024-50848) :  ![starts](https://img.shields.io/github/stars/Wh1teSnak3/CVE-2024-50848.svg) ![forks](https://img.shields.io/github/forks/Wh1teSnak3/CVE-2024-50848.svg)

## CVE-2024-50804
 Insecure Permissions vulnerability in Micro-star International MSI Center Pro 2.1.37.0 allows a local attacker to execute arbitrary code via the Device_DeviceID.dat.bak file within the C:\ProgramData\MSI\One Dragon Center\Data folder



- [https://github.com/g3tsyst3m/CVE-2024-50804](https://github.com/g3tsyst3m/CVE-2024-50804) :  ![starts](https://img.shields.io/github/stars/g3tsyst3m/CVE-2024-50804.svg) ![forks](https://img.shields.io/github/forks/g3tsyst3m/CVE-2024-50804.svg)

## CVE-2024-50803
 The mediapool feature of the Redaxo Core CMS application v 5.17.1 is vulnerable to Cross Site Scripting(XSS) which allows a remote attacker to escalate privileges



- [https://github.com/Praison001/CVE-2024-50803-Redaxo](https://github.com/Praison001/CVE-2024-50803-Redaxo) :  ![starts](https://img.shields.io/github/stars/Praison001/CVE-2024-50803-Redaxo.svg) ![forks](https://img.shields.io/github/forks/Praison001/CVE-2024-50803-Redaxo.svg)

## CVE-2024-50677
 A cross-site scripting (XSS) vulnerability in OroPlatform CMS v5.1 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the Search parameter.



- [https://github.com/ZumiYumi/CVE-2024-50677](https://github.com/ZumiYumi/CVE-2024-50677) :  ![starts](https://img.shields.io/github/stars/ZumiYumi/CVE-2024-50677.svg) ![forks](https://img.shields.io/github/forks/ZumiYumi/CVE-2024-50677.svg)

## CVE-2024-50657
 An issue in Owncloud android apk v.4.3.1 allows a physically proximate attacker to escalate privileges via the PassCodeViewModel class, specifically in the checkPassCodeIsValid method



- [https://github.com/SAHALLL/CVE-2024-50657](https://github.com/SAHALLL/CVE-2024-50657) :  ![starts](https://img.shields.io/github/stars/SAHALLL/CVE-2024-50657.svg) ![forks](https://img.shields.io/github/forks/SAHALLL/CVE-2024-50657.svg)

## CVE-2024-50623
 In Cleo Harmony before 5.8.0.21, VLTrader before 5.8.0.21, and LexiCom before 5.8.0.21, there is an unrestricted file upload and download that could lead to remote code execution.



- [https://github.com/watchtowrlabs/CVE-2024-50623](https://github.com/watchtowrlabs/CVE-2024-50623) :  ![starts](https://img.shields.io/github/stars/watchtowrlabs/CVE-2024-50623.svg) ![forks](https://img.shields.io/github/forks/watchtowrlabs/CVE-2024-50623.svg)

- [https://github.com/verylazytech/CVE-2024-50623](https://github.com/verylazytech/CVE-2024-50623) :  ![starts](https://img.shields.io/github/stars/verylazytech/CVE-2024-50623.svg) ![forks](https://img.shields.io/github/forks/verylazytech/CVE-2024-50623.svg)

- [https://github.com/iSee857/Cleo-CVE-2024-50623-PoC](https://github.com/iSee857/Cleo-CVE-2024-50623-PoC) :  ![starts](https://img.shields.io/github/stars/iSee857/Cleo-CVE-2024-50623-PoC.svg) ![forks](https://img.shields.io/github/forks/iSee857/Cleo-CVE-2024-50623-PoC.svg)

## CVE-2024-50603
 An issue was discovered in Aviatrix Controller before 7.1.4191 and 7.2.x before 7.2.4996. Due to the improper neutralization of special elements used in an OS command, an unauthenticated attacker is able to execute arbitrary code. Shell metacharacters can be sent to /v1/api in cloud_type for list_flightpath_destination_instances, or src_cloud_type for flightpath_connection_test.



- [https://github.com/th3gokul/CVE-2024-50603](https://github.com/th3gokul/CVE-2024-50603) :  ![starts](https://img.shields.io/github/stars/th3gokul/CVE-2024-50603.svg) ![forks](https://img.shields.io/github/forks/th3gokul/CVE-2024-50603.svg)

- [https://github.com/newlinesec/CVE-2024-50603](https://github.com/newlinesec/CVE-2024-50603) :  ![starts](https://img.shields.io/github/stars/newlinesec/CVE-2024-50603.svg) ![forks](https://img.shields.io/github/forks/newlinesec/CVE-2024-50603.svg)

## CVE-2024-50510
 Unrestricted Upload of File with Dangerous Type vulnerability in Web and Print Design AR For Woocommerce allows Upload a Web Shell to a Web Server.This issue affects AR For Woocommerce: from n/a through 6.2.



- [https://github.com/RandomRobbieBF/CVE-2024-50510](https://github.com/RandomRobbieBF/CVE-2024-50510) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50510.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50510.svg)

## CVE-2024-50509
 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Chetan Khandla Woocommerce Product Design allows Path Traversal.This issue affects Woocommerce Product Design: from n/a through 1.0.0.



- [https://github.com/RandomRobbieBF/CVE-2024-50509](https://github.com/RandomRobbieBF/CVE-2024-50509) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50509.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50509.svg)

## CVE-2024-50508
 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Chetan Khandla Woocommerce Product Design allows Path Traversal.This issue affects Woocommerce Product Design: from n/a through 1.0.0.



- [https://github.com/RandomRobbieBF/CVE-2024-50508](https://github.com/RandomRobbieBF/CVE-2024-50508) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50508.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50508.svg)

## CVE-2024-50507
 Deserialization of Untrusted Data vulnerability in Daniel Schmitzer DS.DownloadList allows Object Injection.This issue affects DS.DownloadList: from n/a through 1.3.



- [https://github.com/RandomRobbieBF/CVE-2024-50507](https://github.com/RandomRobbieBF/CVE-2024-50507) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50507.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50507.svg)

## CVE-2024-50498
 Improper Control of Generation of Code ('Code Injection') vulnerability in LUBUS WP Query Console allows Code Injection.This issue affects WP Query Console: from n/a through 1.0.



- [https://github.com/RandomRobbieBF/CVE-2024-50498](https://github.com/RandomRobbieBF/CVE-2024-50498) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50498.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50498.svg)

- [https://github.com/p0et08/CVE-2024-50498](https://github.com/p0et08/CVE-2024-50498) :  ![starts](https://img.shields.io/github/stars/p0et08/CVE-2024-50498.svg) ![forks](https://img.shields.io/github/forks/p0et08/CVE-2024-50498.svg)

- [https://github.com/Nxploited/CVE-2024-50498](https://github.com/Nxploited/CVE-2024-50498) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-50498.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-50498.svg)

## CVE-2024-50493
 Unrestricted Upload of File with Dangerous Type vulnerability in masterhomepage Automatic Translation allows Upload a Web Shell to a Web Server.This issue affects Automatic Translation: from n/a through 1.0.4.



- [https://github.com/RandomRobbieBF/CVE-2024-50493](https://github.com/RandomRobbieBF/CVE-2024-50493) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50493.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50493.svg)

## CVE-2024-50491
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Micah Blu RSVP ME allows SQL Injection.This issue affects RSVP ME: from n/a through 1.9.9.



- [https://github.com/RandomRobbieBF/CVE-2024-50491](https://github.com/RandomRobbieBF/CVE-2024-50491) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50491.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50491.svg)

## CVE-2024-50490
 Missing Authorization vulnerability in Szabolcs Szecsenyi PegaPoll allows Accessing Functionality Not Properly Constrained by ACLs.This issue affects PegaPoll: from n/a through 1.0.2.



- [https://github.com/RandomRobbieBF/CVE-2024-50490](https://github.com/RandomRobbieBF/CVE-2024-50490) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50490.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50490.svg)

## CVE-2024-50488
 Authentication Bypass Using an Alternate Path or Channel vulnerability in Priyabrata Sarkar Token Login allows Authentication Bypass.This issue affects Token Login: from n/a through 1.0.3.



- [https://github.com/RandomRobbieBF/CVE-2024-50488](https://github.com/RandomRobbieBF/CVE-2024-50488) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50488.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50488.svg)

## CVE-2024-50485
 : Incorrect Privilege Assignment vulnerability in Udit Rawat Exam Matrix allows Privilege Escalation.This issue affects Exam Matrix: from n/a through 1.5.



- [https://github.com/RandomRobbieBF/CVE-2024-50485](https://github.com/RandomRobbieBF/CVE-2024-50485) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50485.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50485.svg)

## CVE-2024-50483
 Authorization Bypass Through User-Controlled Key vulnerability in Meetup allows Privilege Escalation.This issue affects Meetup: from n/a through 0.1.



- [https://github.com/RandomRobbieBF/CVE-2024-50483](https://github.com/RandomRobbieBF/CVE-2024-50483) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50483.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50483.svg)

## CVE-2024-50482
 Unrestricted Upload of File with Dangerous Type vulnerability in Chetan Khandla Woocommerce Product Design allows Upload a Web Shell to a Web Server.This issue affects Woocommerce Product Design: from n/a through 1.0.0.



- [https://github.com/RandomRobbieBF/CVE-2024-50482](https://github.com/RandomRobbieBF/CVE-2024-50482) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50482.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50482.svg)

## CVE-2024-50478
 Authentication Bypass by Primary Weakness vulnerability in Swoop 1-Click Login: Passwordless Authentication allows Authentication Bypass.This issue affects 1-Click Login: Passwordless Authentication: 1.4.5.



- [https://github.com/RandomRobbieBF/CVE-2024-50478](https://github.com/RandomRobbieBF/CVE-2024-50478) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50478.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50478.svg)

## CVE-2024-50477
 Authentication Bypass Using an Alternate Path or Channel vulnerability in Stacks Stacks Mobile App Builder stacks-mobile-app-builder allows Authentication Bypass.This issue affects Stacks Mobile App Builder: from n/a through 5.2.3.



- [https://github.com/RandomRobbieBF/CVE-2024-50477](https://github.com/RandomRobbieBF/CVE-2024-50477) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50477.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50477.svg)

## CVE-2024-50476
 Missing Authorization vulnerability in GRÜN Software Group GmbH GRÜN spendino Spendenformular allows Privilege Escalation.This issue affects GRÜN spendino Spendenformular: from n/a through 1.0.1.



- [https://github.com/RandomRobbieBF/CVE-2024-50476](https://github.com/RandomRobbieBF/CVE-2024-50476) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50476.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50476.svg)

## CVE-2024-50475
 Missing Authorization vulnerability in Scott Gamon Signup Page allows Privilege Escalation.This issue affects Signup Page: from n/a through 1.0.



- [https://github.com/RandomRobbieBF/CVE-2024-50475](https://github.com/RandomRobbieBF/CVE-2024-50475) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50475.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50475.svg)

## CVE-2024-50473
 Unrestricted Upload of File with Dangerous Type vulnerability in Ajar Productions Ajar in5 Embed allows Upload a Web Shell to a Web Server.This issue affects Ajar in5 Embed: from n/a through 3.1.3.



- [https://github.com/RandomRobbieBF/CVE-2024-50473](https://github.com/RandomRobbieBF/CVE-2024-50473) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50473.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50473.svg)

## CVE-2024-50450
 Improper Control of Generation of Code ('Code Injection') vulnerability in realmag777 WordPress Meta Data and Taxonomies Filter (MDTF) allows Code Injection.This issue affects WordPress Meta Data and Taxonomies Filter (MDTF): from n/a through 1.3.3.4.



- [https://github.com/RandomRobbieBF/CVE-2024-50450](https://github.com/RandomRobbieBF/CVE-2024-50450) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50450.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50450.svg)

## CVE-2024-50427
 Unrestricted Upload of File with Dangerous Type vulnerability in Devsoft Baltic OÜ SurveyJS: Drag & Drop WordPress Form Builder.This issue affects SurveyJS: Drag & Drop WordPress Form Builder: from n/a through 1.9.136.



- [https://github.com/RandomRobbieBF/CVE-2024-50427](https://github.com/RandomRobbieBF/CVE-2024-50427) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-50427.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-50427.svg)

## CVE-2024-50404
 A link following vulnerability has been reported to affect Qsync Central. If exploited, the vulnerability could allow remote attackers who have gained user access to traverse the file system to unintended locations.

We have already fixed the vulnerability in the following versions:
Qsync Central 4.4.0.16_20240819 ( 2024/08/19 ) and later



- [https://github.com/C411e/CVE-2024-50404](https://github.com/C411e/CVE-2024-50404) :  ![starts](https://img.shields.io/github/stars/C411e/CVE-2024-50404.svg) ![forks](https://img.shields.io/github/forks/C411e/CVE-2024-50404.svg)

## CVE-2024-50395
 An authorization bypass through user-controlled key vulnerability has been reported to affect Media Streaming add-on. If exploited, the vulnerability could allow local network attackers to gain privilege.

We have already fixed the vulnerability in the following version:
Media Streaming add-on 500.1.1.6 ( 2024/08/02 ) and later



- [https://github.com/neko-hat/CVE-2024-50395](https://github.com/neko-hat/CVE-2024-50395) :  ![starts](https://img.shields.io/github/stars/neko-hat/CVE-2024-50395.svg) ![forks](https://img.shields.io/github/forks/neko-hat/CVE-2024-50395.svg)

## CVE-2024-50379
 Time-of-check Time-of-use (TOCTOU) Race Condition vulnerability during JSP compilation in Apache Tomcat permits an RCE on case insensitive file systems when the default servlet is enabled for write (non-default configuration).

This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.1, from 10.1.0-M1 through 10.1.33, from 9.0.0.M1 through 9.0.97.

The following versions were EOL at the time the CVE was created but are 
known to be affected: 8.5.0 though 8.5.100. Other, older, EOL versions may also be affected.

Users are recommended to upgrade to version 11.0.2, 10.1.34 or 9.0.98, which fixes the issue.



- [https://github.com/SleepingBag945/CVE-2024-50379](https://github.com/SleepingBag945/CVE-2024-50379) :  ![starts](https://img.shields.io/github/stars/SleepingBag945/CVE-2024-50379.svg) ![forks](https://img.shields.io/github/forks/SleepingBag945/CVE-2024-50379.svg)

- [https://github.com/ph0ebus/Tomcat-CVE-2024-50379-Poc](https://github.com/ph0ebus/Tomcat-CVE-2024-50379-Poc) :  ![starts](https://img.shields.io/github/stars/ph0ebus/Tomcat-CVE-2024-50379-Poc.svg) ![forks](https://img.shields.io/github/forks/ph0ebus/Tomcat-CVE-2024-50379-Poc.svg)

- [https://github.com/iSee857/CVE-2024-50379-PoC](https://github.com/iSee857/CVE-2024-50379-PoC) :  ![starts](https://img.shields.io/github/stars/iSee857/CVE-2024-50379-PoC.svg) ![forks](https://img.shields.io/github/forks/iSee857/CVE-2024-50379-PoC.svg)

- [https://github.com/v3153/CVE-2024-50379-POC](https://github.com/v3153/CVE-2024-50379-POC) :  ![starts](https://img.shields.io/github/stars/v3153/CVE-2024-50379-POC.svg) ![forks](https://img.shields.io/github/forks/v3153/CVE-2024-50379-POC.svg)

- [https://github.com/dragonked2/CVE-2024-50379-POC](https://github.com/dragonked2/CVE-2024-50379-POC) :  ![starts](https://img.shields.io/github/stars/dragonked2/CVE-2024-50379-POC.svg) ![forks](https://img.shields.io/github/forks/dragonked2/CVE-2024-50379-POC.svg)

- [https://github.com/JFOZ1010/Nuclei-Template-CVE-2024-50379](https://github.com/JFOZ1010/Nuclei-Template-CVE-2024-50379) :  ![starts](https://img.shields.io/github/stars/JFOZ1010/Nuclei-Template-CVE-2024-50379.svg) ![forks](https://img.shields.io/github/forks/JFOZ1010/Nuclei-Template-CVE-2024-50379.svg)

- [https://github.com/yiliufeng168/CVE-2024-50379-POC](https://github.com/yiliufeng168/CVE-2024-50379-POC) :  ![starts](https://img.shields.io/github/stars/yiliufeng168/CVE-2024-50379-POC.svg) ![forks](https://img.shields.io/github/forks/yiliufeng168/CVE-2024-50379-POC.svg)

- [https://github.com/dear-cell/CVE-2024-50379](https://github.com/dear-cell/CVE-2024-50379) :  ![starts](https://img.shields.io/github/stars/dear-cell/CVE-2024-50379.svg) ![forks](https://img.shields.io/github/forks/dear-cell/CVE-2024-50379.svg)

- [https://github.com/gomtaengi/CVE-2024-50379-exp](https://github.com/gomtaengi/CVE-2024-50379-exp) :  ![starts](https://img.shields.io/github/stars/gomtaengi/CVE-2024-50379-exp.svg) ![forks](https://img.shields.io/github/forks/gomtaengi/CVE-2024-50379-exp.svg)

- [https://github.com/Alchemist3dot14/CVE-2024-50379](https://github.com/Alchemist3dot14/CVE-2024-50379) :  ![starts](https://img.shields.io/github/stars/Alchemist3dot14/CVE-2024-50379.svg) ![forks](https://img.shields.io/github/forks/Alchemist3dot14/CVE-2024-50379.svg)

- [https://github.com/dkstar11q/CVE-2024-50379-nuclei](https://github.com/dkstar11q/CVE-2024-50379-nuclei) :  ![starts](https://img.shields.io/github/stars/dkstar11q/CVE-2024-50379-nuclei.svg) ![forks](https://img.shields.io/github/forks/dkstar11q/CVE-2024-50379-nuclei.svg)

## CVE-2024-50340
 symfony/runtime is a module for the Symphony PHP framework which enables decoupling PHP applications from global state. When the `register_argv_argc` php directive is set to `on` , and users call any URL with a special crafted query string, they are able to change the environment or debug mode used by the kernel when handling the request. As of versions 5.4.46, 6.4.14, and 7.1.7 the `SymfonyRuntime` now ignores the `argv` values for non-SAPI PHP runtimes. All users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/Nyamort/CVE-2024-50340](https://github.com/Nyamort/CVE-2024-50340) :  ![starts](https://img.shields.io/github/stars/Nyamort/CVE-2024-50340.svg) ![forks](https://img.shields.io/github/forks/Nyamort/CVE-2024-50340.svg)

## CVE-2024-50335
 SuiteCRM is an open-source, enterprise-ready Customer Relationship Management (CRM) software application. The "Publish Key" field in SuiteCRM's Edit Profile page is vulnerable to Reflected Cross-Site Scripting (XSS), allowing an attacker to inject malicious JavaScript code. This can be exploited to steal CSRF tokens and perform unauthorized actions, such as creating new administrative users without proper authentication. The vulnerability arises due to insufficient input validation and sanitization of the Publish Key field within the SuiteCRM application. When an attacker injects a malicious script, it gets executed within the context of an authenticated user's session. The injected script (o.js) then leverages the captured CSRF token to forge requests that create new administrative users, effectively compromising the integrity and security of the CRM instance. This issue has been addressed in versions 7.14.6 and 8.7.1. Users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/shellkraft/CVE-2024-50335](https://github.com/shellkraft/CVE-2024-50335) :  ![starts](https://img.shields.io/github/stars/shellkraft/CVE-2024-50335.svg) ![forks](https://img.shields.io/github/forks/shellkraft/CVE-2024-50335.svg)

## CVE-2024-50251
 In the Linux kernel, the following vulnerability has been resolved:

netfilter: nft_payload: sanitize offset and length before calling skb_checksum()

If access to offset + length is larger than the skbuff length, then
skb_checksum() triggers BUG_ON().

skb_checksum() internally subtracts the length parameter while iterating
over skbuff, BUG_ON(len) at the end of it checks that the expected
length to be included in the checksum calculation is fully consumed.



- [https://github.com/slavin-ayu/CVE-2024-50251-PoC](https://github.com/slavin-ayu/CVE-2024-50251-PoC) :  ![starts](https://img.shields.io/github/stars/slavin-ayu/CVE-2024-50251-PoC.svg) ![forks](https://img.shields.io/github/forks/slavin-ayu/CVE-2024-50251-PoC.svg)

## CVE-2024-49699
 Deserialization of Untrusted Data vulnerability in NotFound ARPrice allows Object Injection. This issue affects ARPrice: from n/a through 4.0.3.



- [https://github.com/RandomRobbieBF/CVE-2024-49699](https://github.com/RandomRobbieBF/CVE-2024-49699) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-49699.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-49699.svg)

## CVE-2024-49681
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in SWIT WP Sessions Time Monitoring Full Automatic allows SQL Injection.This issue affects WP Sessions Time Monitoring Full Automatic: from n/a through 1.0.9.



- [https://github.com/RandomRobbieBF/CVE-2024-49681](https://github.com/RandomRobbieBF/CVE-2024-49681) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-49681.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-49681.svg)

## CVE-2024-49607
 Unrestricted Upload of File with Dangerous Type vulnerability in Redwan Hilali WP Dropbox Dropins allows Upload a Web Shell to a Web Server.This issue affects WP Dropbox Dropins: from n/a through 1.0.



- [https://github.com/RandomRobbieBF/CVE-2024-49607](https://github.com/RandomRobbieBF/CVE-2024-49607) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-49607.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-49607.svg)

## CVE-2024-49379
 Umbrel is a home server OS for self-hosting. The login functionality of Umbrel before version 1.2.2 contains a reflected cross-site scripting (XSS) vulnerability in use-auth.tsx. An attacker can specify a malicious redirect query parameter to trigger the vulnerability. If a JavaScript URL is passed to the redirect parameter the attacker provided JavaScript will be executed after the user entered their password and clicked on login. This vulnerability is fixed in 1.2.2.



- [https://github.com/OHDUDEOKNICE/CVE-2024-49379](https://github.com/OHDUDEOKNICE/CVE-2024-49379) :  ![starts](https://img.shields.io/github/stars/OHDUDEOKNICE/CVE-2024-49379.svg) ![forks](https://img.shields.io/github/forks/OHDUDEOKNICE/CVE-2024-49379.svg)

## CVE-2024-49369
 Icinga is a monitoring system which checks the availability of network resources, notifies users of outages, and generates performance data for reporting. The TLS certificate validation in all Icinga 2 versions starting from 2.4.0 was flawed, allowing an attacker to impersonate both trusted cluster nodes as well as any API users that use TLS client certificates for authentication (ApiUser objects with the client_cn attribute set). This vulnerability has been fixed in v2.14.3, v2.13.10, v2.12.11, and v2.11.12.



- [https://github.com/Quantum-Sicarius/CVE-2024-49369](https://github.com/Quantum-Sicarius/CVE-2024-49369) :  ![starts](https://img.shields.io/github/stars/Quantum-Sicarius/CVE-2024-49369.svg) ![forks](https://img.shields.io/github/forks/Quantum-Sicarius/CVE-2024-49369.svg)

## CVE-2024-49368
 Nginx UI is a web user interface for the Nginx web server. Prior to version 2.0.0-beta.36, when Nginx UI configures logrotate, it does not verify the input and directly passes it to exec.Command, causing arbitrary command execution. Version 2.0.0-beta.36 fixes this issue.



- [https://github.com/Aashay221999/CVE-2024-49368](https://github.com/Aashay221999/CVE-2024-49368) :  ![starts](https://img.shields.io/github/stars/Aashay221999/CVE-2024-49368.svg) ![forks](https://img.shields.io/github/forks/Aashay221999/CVE-2024-49368.svg)

## CVE-2024-49328
 Authentication Bypass Using an Alternate Path or Channel vulnerability in Vivek Tamrakar WP REST API FNS allows Authentication Bypass.This issue affects WP REST API FNS: from n/a through 1.0.0.



- [https://github.com/RandomRobbieBF/CVE-2024-49328](https://github.com/RandomRobbieBF/CVE-2024-49328) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-49328.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-49328.svg)

- [https://github.com/Nxploited/CVE-2024-49328-exploit](https://github.com/Nxploited/CVE-2024-49328-exploit) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-49328-exploit.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-49328-exploit.svg)

## CVE-2024-49138
 Windows Common Log File System Driver Elevation of Privilege Vulnerability



- [https://github.com/MrAle98/CVE-2024-49138-POC](https://github.com/MrAle98/CVE-2024-49138-POC) :  ![starts](https://img.shields.io/github/stars/MrAle98/CVE-2024-49138-POC.svg) ![forks](https://img.shields.io/github/forks/MrAle98/CVE-2024-49138-POC.svg)

- [https://github.com/1rhino2/SCRAPPED](https://github.com/1rhino2/SCRAPPED) :  ![starts](https://img.shields.io/github/stars/1rhino2/SCRAPPED.svg) ![forks](https://img.shields.io/github/forks/1rhino2/SCRAPPED.svg)

- [https://github.com/CyprianAtsyor/letsdefend-cve-2024-49138-investigation](https://github.com/CyprianAtsyor/letsdefend-cve-2024-49138-investigation) :  ![starts](https://img.shields.io/github/stars/CyprianAtsyor/letsdefend-cve-2024-49138-investigation.svg) ![forks](https://img.shields.io/github/forks/CyprianAtsyor/letsdefend-cve-2024-49138-investigation.svg)

- [https://github.com/Glitch-ao/SOC335-CVE-2024-49138-Exploitation-Detected](https://github.com/Glitch-ao/SOC335-CVE-2024-49138-Exploitation-Detected) :  ![starts](https://img.shields.io/github/stars/Glitch-ao/SOC335-CVE-2024-49138-Exploitation-Detected.svg) ![forks](https://img.shields.io/github/forks/Glitch-ao/SOC335-CVE-2024-49138-Exploitation-Detected.svg)

## CVE-2024-49124
 Lightweight Directory Access Protocol (LDAP) Client Remote Code Execution Vulnerability



- [https://github.com/mutkus/Microsoft-2024-December-Update-Control](https://github.com/mutkus/Microsoft-2024-December-Update-Control) :  ![starts](https://img.shields.io/github/stars/mutkus/Microsoft-2024-December-Update-Control.svg) ![forks](https://img.shields.io/github/forks/mutkus/Microsoft-2024-December-Update-Control.svg)

## CVE-2024-49122
 Microsoft Message Queuing (MSMQ) Remote Code Execution Vulnerability



- [https://github.com/mutkus/Microsoft-2024-December-Update-Control](https://github.com/mutkus/Microsoft-2024-December-Update-Control) :  ![starts](https://img.shields.io/github/stars/mutkus/Microsoft-2024-December-Update-Control.svg) ![forks](https://img.shields.io/github/forks/mutkus/Microsoft-2024-December-Update-Control.svg)

## CVE-2024-49118
 Microsoft Message Queuing (MSMQ) Remote Code Execution Vulnerability



- [https://github.com/mutkus/Microsoft-2024-December-Update-Control](https://github.com/mutkus/Microsoft-2024-December-Update-Control) :  ![starts](https://img.shields.io/github/stars/mutkus/Microsoft-2024-December-Update-Control.svg) ![forks](https://img.shields.io/github/forks/mutkus/Microsoft-2024-December-Update-Control.svg)

## CVE-2024-49117
 Windows Hyper-V Remote Code Execution Vulnerability



- [https://github.com/mutkus/Microsoft-2024-December-Update-Control](https://github.com/mutkus/Microsoft-2024-December-Update-Control) :  ![starts](https://img.shields.io/github/stars/mutkus/Microsoft-2024-December-Update-Control.svg) ![forks](https://img.shields.io/github/forks/mutkus/Microsoft-2024-December-Update-Control.svg)

## CVE-2024-49113
 Windows Lightweight Directory Access Protocol (LDAP) Denial of Service Vulnerability



- [https://github.com/SafeBreach-Labs/CVE-2024-49113](https://github.com/SafeBreach-Labs/CVE-2024-49113) :  ![starts](https://img.shields.io/github/stars/SafeBreach-Labs/CVE-2024-49113.svg) ![forks](https://img.shields.io/github/forks/SafeBreach-Labs/CVE-2024-49113.svg)

- [https://github.com/barcrange/CVE-2024-49113-Checker](https://github.com/barcrange/CVE-2024-49113-Checker) :  ![starts](https://img.shields.io/github/stars/barcrange/CVE-2024-49113-Checker.svg) ![forks](https://img.shields.io/github/forks/barcrange/CVE-2024-49113-Checker.svg)

- [https://github.com/Sachinart/CVE-2024-49113-Checker](https://github.com/Sachinart/CVE-2024-49113-Checker) :  ![starts](https://img.shields.io/github/stars/Sachinart/CVE-2024-49113-Checker.svg) ![forks](https://img.shields.io/github/forks/Sachinart/CVE-2024-49113-Checker.svg)

## CVE-2024-49112
 Windows Lightweight Directory Access Protocol (LDAP) Remote Code Execution Vulnerability



- [https://github.com/tnkr/poc_monitor](https://github.com/tnkr/poc_monitor) :  ![starts](https://img.shields.io/github/stars/tnkr/poc_monitor.svg) ![forks](https://img.shields.io/github/forks/tnkr/poc_monitor.svg)

- [https://github.com/bo0l3an/CVE-2024-49112-PoC](https://github.com/bo0l3an/CVE-2024-49112-PoC) :  ![starts](https://img.shields.io/github/stars/bo0l3an/CVE-2024-49112-PoC.svg) ![forks](https://img.shields.io/github/forks/bo0l3an/CVE-2024-49112-PoC.svg)

- [https://github.com/CCIEVoice2009/CVE-2024-49112](https://github.com/CCIEVoice2009/CVE-2024-49112) :  ![starts](https://img.shields.io/github/stars/CCIEVoice2009/CVE-2024-49112.svg) ![forks](https://img.shields.io/github/forks/CCIEVoice2009/CVE-2024-49112.svg)

## CVE-2024-49039
 Windows Task Scheduler Elevation of Privilege Vulnerability



- [https://github.com/je5442804/WPTaskScheduler_CVE-2024-49039](https://github.com/je5442804/WPTaskScheduler_CVE-2024-49039) :  ![starts](https://img.shields.io/github/stars/je5442804/WPTaskScheduler_CVE-2024-49039.svg) ![forks](https://img.shields.io/github/forks/je5442804/WPTaskScheduler_CVE-2024-49039.svg)

## CVE-2024-48990
 Qualys discovered that needrestart, before version 3.8, allows local attackers to execute arbitrary code as root by tricking needrestart into running the Python interpreter with an attacker-controlled PYTHONPATH environment variable.



- [https://github.com/makuga01/CVE-2024-48990-PoC](https://github.com/makuga01/CVE-2024-48990-PoC) :  ![starts](https://img.shields.io/github/stars/makuga01/CVE-2024-48990-PoC.svg) ![forks](https://img.shields.io/github/forks/makuga01/CVE-2024-48990-PoC.svg)

- [https://github.com/pentestfunctions/CVE-2024-48990-PoC-Testing](https://github.com/pentestfunctions/CVE-2024-48990-PoC-Testing) :  ![starts](https://img.shields.io/github/stars/pentestfunctions/CVE-2024-48990-PoC-Testing.svg) ![forks](https://img.shields.io/github/forks/pentestfunctions/CVE-2024-48990-PoC-Testing.svg)

- [https://github.com/ns989/CVE-2024-48990](https://github.com/ns989/CVE-2024-48990) :  ![starts](https://img.shields.io/github/stars/ns989/CVE-2024-48990.svg) ![forks](https://img.shields.io/github/forks/ns989/CVE-2024-48990.svg)

- [https://github.com/Cyb3rFr0g/CVE-2024-48990-PoC](https://github.com/Cyb3rFr0g/CVE-2024-48990-PoC) :  ![starts](https://img.shields.io/github/stars/Cyb3rFr0g/CVE-2024-48990-PoC.svg) ![forks](https://img.shields.io/github/forks/Cyb3rFr0g/CVE-2024-48990-PoC.svg)

- [https://github.com/R0XDEADBEEF/CVE-2024-48990](https://github.com/R0XDEADBEEF/CVE-2024-48990) :  ![starts](https://img.shields.io/github/stars/R0XDEADBEEF/CVE-2024-48990.svg) ![forks](https://img.shields.io/github/forks/R0XDEADBEEF/CVE-2024-48990.svg)

- [https://github.com/ally-petitt/CVE-2024-48990-Exploit](https://github.com/ally-petitt/CVE-2024-48990-Exploit) :  ![starts](https://img.shields.io/github/stars/ally-petitt/CVE-2024-48990-Exploit.svg) ![forks](https://img.shields.io/github/forks/ally-petitt/CVE-2024-48990-Exploit.svg)

- [https://github.com/NullByte-7w7/CVE-2024-48990](https://github.com/NullByte-7w7/CVE-2024-48990) :  ![starts](https://img.shields.io/github/stars/NullByte-7w7/CVE-2024-48990.svg) ![forks](https://img.shields.io/github/forks/NullByte-7w7/CVE-2024-48990.svg)

- [https://github.com/CyberCrowCC/CVE-2024-48990](https://github.com/CyberCrowCC/CVE-2024-48990) :  ![starts](https://img.shields.io/github/stars/CyberCrowCC/CVE-2024-48990.svg) ![forks](https://img.shields.io/github/forks/CyberCrowCC/CVE-2024-48990.svg)

- [https://github.com/felmoltor/CVE-2024-48990](https://github.com/felmoltor/CVE-2024-48990) :  ![starts](https://img.shields.io/github/stars/felmoltor/CVE-2024-48990.svg) ![forks](https://img.shields.io/github/forks/felmoltor/CVE-2024-48990.svg)

## CVE-2024-48895
 Improper neutralization of special elements used in an OS command ('OS Command Injection') issue exists in Rakuten Turbo 5G firmware version V1.3.18 and earlier. If this vulnerability is exploited, a remote authenticated attacker may execute an arbitrary OS command.



- [https://github.com/0xNslabs/Rakuten5GTurboAPI](https://github.com/0xNslabs/Rakuten5GTurboAPI) :  ![starts](https://img.shields.io/github/stars/0xNslabs/Rakuten5GTurboAPI.svg) ![forks](https://img.shields.io/github/forks/0xNslabs/Rakuten5GTurboAPI.svg)

## CVE-2024-48887
 A  unverified password change vulnerability in Fortinet FortiSwitch GUI may allow a remote unauthenticated attacker to change admin passwords via a specially crafted request



- [https://github.com/groshi215/CVE-2024-48887-Exploit](https://github.com/groshi215/CVE-2024-48887-Exploit) :  ![starts](https://img.shields.io/github/stars/groshi215/CVE-2024-48887-Exploit.svg) ![forks](https://img.shields.io/github/forks/groshi215/CVE-2024-48887-Exploit.svg)

- [https://github.com/cybersecplayground/CVE-2024-48887-FortiSwitch-Exploit](https://github.com/cybersecplayground/CVE-2024-48887-FortiSwitch-Exploit) :  ![starts](https://img.shields.io/github/stars/cybersecplayground/CVE-2024-48887-FortiSwitch-Exploit.svg) ![forks](https://img.shields.io/github/forks/cybersecplayground/CVE-2024-48887-FortiSwitch-Exploit.svg)

## CVE-2024-48705
 Wavlink AC1200 with firmware versions M32A3_V1410_230602 and M32A3_V1410_240222 are vulnerable to a post-authentication command injection while resetting the password. This vulnerability is specifically found within the "set_sys_adm" function of the "adm.cgi" binary, and is due to improper santization of the user provided "newpass" field



- [https://github.com/L41KAA/CVE-2024-48705](https://github.com/L41KAA/CVE-2024-48705) :  ![starts](https://img.shields.io/github/stars/L41KAA/CVE-2024-48705.svg) ![forks](https://img.shields.io/github/forks/L41KAA/CVE-2024-48705.svg)

## CVE-2024-48322
 UsersController.php in Run.codes 1.5.2 and older has a reset password race condition vulnerability.



- [https://github.com/trqt/CVE-2024-48322](https://github.com/trqt/CVE-2024-48322) :  ![starts](https://img.shields.io/github/stars/trqt/CVE-2024-48322.svg) ![forks](https://img.shields.io/github/forks/trqt/CVE-2024-48322.svg)

## CVE-2024-48246
 Vehicle Management System 1.0 contains a Stored Cross-Site Scripting (XSS) vulnerability in the "Name" parameter of /vehicle-management/booking.php.



- [https://github.com/ShadowByte1/CVE-2024-48246](https://github.com/ShadowByte1/CVE-2024-48246) :  ![starts](https://img.shields.io/github/stars/ShadowByte1/CVE-2024-48246.svg) ![forks](https://img.shields.io/github/forks/ShadowByte1/CVE-2024-48246.svg)

## CVE-2024-48245
 Vehicle Management System 1.0 is vulnerable to SQL Injection. A guest user can exploit vulnerable POST parameters in various administrative actions, such as booking a vehicle or confirming a booking. The affected parameters include "Booking ID", "Action Name", and "Payment Confirmation ID", which are present in /newvehicle.php and /newdriver.php.



- [https://github.com/ShadowByte1/CVE-2024-48245](https://github.com/ShadowByte1/CVE-2024-48245) :  ![starts](https://img.shields.io/github/stars/ShadowByte1/CVE-2024-48245.svg) ![forks](https://img.shields.io/github/forks/ShadowByte1/CVE-2024-48245.svg)

## CVE-2024-48197
 Cross Site Scripting vulnerability in Audiocodes MP-202b v.4.4.3 allows a remote attacker to escalate privileges via the login page of the web interface.



- [https://github.com/GCatt-AS/CVE-2024-48197](https://github.com/GCatt-AS/CVE-2024-48197) :  ![starts](https://img.shields.io/github/stars/GCatt-AS/CVE-2024-48197.svg) ![forks](https://img.shields.io/github/forks/GCatt-AS/CVE-2024-48197.svg)

## CVE-2024-48139
 A prompt injection vulnerability in the chatbox of Blackbox AI v1.3.95 allows attackers to access and exfiltrate all previous and subsequent chat data between the user and the AI assistant via a crafted message.



- [https://github.com/hannahbellesheart/blackbox.ai.security.analysis](https://github.com/hannahbellesheart/blackbox.ai.security.analysis) :  ![starts](https://img.shields.io/github/stars/hannahbellesheart/blackbox.ai.security.analysis.svg) ![forks](https://img.shields.io/github/forks/hannahbellesheart/blackbox.ai.security.analysis.svg)

## CVE-2024-48061
 langflow =1.0.18 is vulnerable to Remote Code Execution (RCE) as any component provided the code functionality and the components run on the local machine rather than in a sandbox.



- [https://github.com/BwithE/CVE-2024-48061](https://github.com/BwithE/CVE-2024-48061) :  ![starts](https://img.shields.io/github/stars/BwithE/CVE-2024-48061.svg) ![forks](https://img.shields.io/github/forks/BwithE/CVE-2024-48061.svg)

## CVE-2024-47865
 Missing authentication for critical function vulnerability exists in Rakuten Turbo 5G firmware version V1.3.18 and earlier. If this vulnerability is exploited, a remote unauthenticated attacker may update or downgrade the firmware on the device.



- [https://github.com/0xNslabs/Rakuten5GTurboAPI](https://github.com/0xNslabs/Rakuten5GTurboAPI) :  ![starts](https://img.shields.io/github/stars/0xNslabs/Rakuten5GTurboAPI.svg) ![forks](https://img.shields.io/github/forks/0xNslabs/Rakuten5GTurboAPI.svg)

## CVE-2024-47799
 Exposure of sensitive system information to an unauthorized control sphere issue exists in Mesh Wi-Fi router RP562B firmware version v1.0.2 and earlier. If this vulnerability is exploited, a network-adjacent authenticated attacker may obtain information of the other devices connected through the Wi-Fi.



- [https://github.com/0xNslabs/SoftBankMeshAPI](https://github.com/0xNslabs/SoftBankMeshAPI) :  ![starts](https://img.shields.io/github/stars/0xNslabs/SoftBankMeshAPI.svg) ![forks](https://img.shields.io/github/forks/0xNslabs/SoftBankMeshAPI.svg)

## CVE-2024-47773
 Discourse is an open source platform for community discussion. An attacker can make several XHR requests until the cache is poisoned with a response without any preloaded data. This issue only affects anonymous visitors of the site. This problem has been patched in the latest version of Discourse. Users are advised to upgrade. Users unable to upgrade should disable anonymous cache by setting the `DISCOURSE_DISABLE_ANON_CACHE` environment variable to a non-empty value.



- [https://github.com/ibrahmsql/CVE-2024-47773](https://github.com/ibrahmsql/CVE-2024-47773) :  ![starts](https://img.shields.io/github/stars/ibrahmsql/CVE-2024-47773.svg) ![forks](https://img.shields.io/github/forks/ibrahmsql/CVE-2024-47773.svg)

## CVE-2024-47575
 A missing authentication for critical function in FortiManager 7.6.0, FortiManager 7.4.0 through 7.4.4, FortiManager 7.2.0 through 7.2.7, FortiManager 7.0.0 through 7.0.12, FortiManager 6.4.0 through 6.4.14, FortiManager 6.2.0 through 6.2.12, Fortinet FortiManager Cloud 7.4.1 through 7.4.4, FortiManager Cloud 7.2.1 through 7.2.7, FortiManager Cloud 7.0.1 through 7.0.12, FortiManager Cloud 6.4.1 through 6.4.7 allows attacker to execute arbitrary code or commands via specially crafted requests.



- [https://github.com/watchtowrlabs/Fortijump-Exploit-CVE-2024-47575](https://github.com/watchtowrlabs/Fortijump-Exploit-CVE-2024-47575) :  ![starts](https://img.shields.io/github/stars/watchtowrlabs/Fortijump-Exploit-CVE-2024-47575.svg) ![forks](https://img.shields.io/github/forks/watchtowrlabs/Fortijump-Exploit-CVE-2024-47575.svg)

- [https://github.com/XiaomingX/cve-2024-47575-exp](https://github.com/XiaomingX/cve-2024-47575-exp) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-47575-exp.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-47575-exp.svg)

- [https://github.com/SkyGodling/exploit-cve-2024-47575](https://github.com/SkyGodling/exploit-cve-2024-47575) :  ![starts](https://img.shields.io/github/stars/SkyGodling/exploit-cve-2024-47575.svg) ![forks](https://img.shields.io/github/forks/SkyGodling/exploit-cve-2024-47575.svg)

- [https://github.com/AnnnNix/CVE-2024-47575](https://github.com/AnnnNix/CVE-2024-47575) :  ![starts](https://img.shields.io/github/stars/AnnnNix/CVE-2024-47575.svg) ![forks](https://img.shields.io/github/forks/AnnnNix/CVE-2024-47575.svg)

- [https://github.com/revanslbw/CVE-2024-47575-POC](https://github.com/revanslbw/CVE-2024-47575-POC) :  ![starts](https://img.shields.io/github/stars/revanslbw/CVE-2024-47575-POC.svg) ![forks](https://img.shields.io/github/forks/revanslbw/CVE-2024-47575-POC.svg)

## CVE-2024-47062
 Navidrome is an open source web-based music collection server and streamer. Navidrome automatically adds parameters in the URL to SQL queries. This can be exploited to access information by adding parameters like `password=...` in the URL (ORM Leak). Furthermore, the names of the parameters are not properly escaped, leading to SQL Injections. Finally, the username is used in a `LIKE` statement, allowing people to log in with `%` instead of their username. When adding parameters to the URL, they are automatically included in an SQL `LIKE` statement (depending on the parameter's name). This allows attackers to potentially retrieve arbitrary information. For example, attackers can use the following request to test whether some encrypted passwords start with `AAA`. This results in an SQL query like `password LIKE 'AAA%'`, allowing attackers to slowly brute-force passwords. When adding parameters to the URL, they are automatically added to an SQL query. The names of the parameters are not properly escaped. This behavior can be used to inject arbitrary SQL code (SQL Injection). These vulnerabilities can be used to leak information and dump the contents of the database and have been addressed in release version 0.53.0. Users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/saisathvik1/CVE-2024-47062](https://github.com/saisathvik1/CVE-2024-47062) :  ![starts](https://img.shields.io/github/stars/saisathvik1/CVE-2024-47062.svg) ![forks](https://img.shields.io/github/forks/saisathvik1/CVE-2024-47062.svg)

## CVE-2024-46982
 Next.js is a React framework for building full-stack web applications. By sending a crafted HTTP request, it is possible to poison the cache of a non-dynamic server-side rendered route in the pages router (this does not affect the app router). When this crafted request is sent it could coerce Next.js to cache a route that is meant to not be cached and send a `Cache-Control: s-maxage=1, stale-while-revalidate` header which some upstream CDNs may cache as well. To be potentially affected all of the following must apply: 1. Next.js between 13.5.1 and 14.2.9, 2. Using pages router, & 3. Using non-dynamic server-side rendered routes e.g. `pages/dashboard.tsx` not `pages/blog/[slug].tsx`. This vulnerability was resolved in Next.js v13.5.7, v14.2.10, and later. We recommend upgrading regardless of whether you can reproduce the issue or not. There are no official or recommended workarounds for this issue, we recommend that users patch to a safe version.



- [https://github.com/CodePontiff/next_js_poisoning](https://github.com/CodePontiff/next_js_poisoning) :  ![starts](https://img.shields.io/github/stars/CodePontiff/next_js_poisoning.svg) ![forks](https://img.shields.io/github/forks/CodePontiff/next_js_poisoning.svg)

## CVE-2024-46542
 Veritas / Arctera Data Insight before 7.1.1 allows Application Administrators to conduct SQL injection attacks.



- [https://github.com/MarioTesoro/CVE-2024-46542](https://github.com/MarioTesoro/CVE-2024-46542) :  ![starts](https://img.shields.io/github/stars/MarioTesoro/CVE-2024-46542.svg) ![forks](https://img.shields.io/github/forks/MarioTesoro/CVE-2024-46542.svg)

## CVE-2024-46538
 A cross-site scripting (XSS) vulnerability in pfsense v2.5.2 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the $pconfig variable at interfaces_groups_edit.php.



- [https://github.com/LauLeysen/CVE-2024-46538](https://github.com/LauLeysen/CVE-2024-46538) :  ![starts](https://img.shields.io/github/stars/LauLeysen/CVE-2024-46538.svg) ![forks](https://img.shields.io/github/forks/LauLeysen/CVE-2024-46538.svg)

## CVE-2024-45827
 Improper neutralization of special elements used in an OS command ('OS Command Injection') issue exists in Mesh Wi-Fi router RP562B firmware version v1.0.2 and earlier. If this vulnerability is exploited, a network-adjacent authenticated attacker may execute an arbitrary OS command.



- [https://github.com/0xNslabs/SoftBankMeshAPI](https://github.com/0xNslabs/SoftBankMeshAPI) :  ![starts](https://img.shields.io/github/stars/0xNslabs/SoftBankMeshAPI.svg) ![forks](https://img.shields.io/github/forks/0xNslabs/SoftBankMeshAPI.svg)

## CVE-2024-45622
 ASIS (aka Aplikasi Sistem Sekolah using CodeIgniter 3) 3.0.0 through 3.2.0 allows index.php username SQL injection for Authentication Bypass.



- [https://github.com/atoz-chevara/cve](https://github.com/atoz-chevara/cve) :  ![starts](https://img.shields.io/github/stars/atoz-chevara/cve.svg) ![forks](https://img.shields.io/github/forks/atoz-chevara/cve.svg)

## CVE-2024-45519
 The postjournal service in Zimbra Collaboration (ZCS) before 8.8.15 Patch 46, 9 before 9.0.0 Patch 41, 10 before 10.0.9, and 10.1 before 10.1.1 sometimes allows unauthenticated users to execute commands.



- [https://github.com/XiaomingX/cve-2024-45519-poc](https://github.com/XiaomingX/cve-2024-45519-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-45519-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-45519-poc.svg)

## CVE-2024-45440
 core/authorize.php in Drupal 11.x-dev allows Full Path Disclosure (even when error logging is None) if the value of hash_salt is file_get_contents of a file that does not exist.



- [https://github.com/w0r1i0g1ht/CVE-2024-45440](https://github.com/w0r1i0g1ht/CVE-2024-45440) :  ![starts](https://img.shields.io/github/stars/w0r1i0g1ht/CVE-2024-45440.svg) ![forks](https://img.shields.io/github/forks/w0r1i0g1ht/CVE-2024-45440.svg)

## CVE-2024-45436
 extractFromZipFile in model.go in Ollama before 0.1.47 can extract members of a ZIP archive outside of the parent directory.



- [https://github.com/XiaomingX/cve-2024-45436-exp](https://github.com/XiaomingX/cve-2024-45436-exp) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-45436-exp.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-45436-exp.svg)

- [https://github.com/srcx404/CVE-2024-45436](https://github.com/srcx404/CVE-2024-45436) :  ![starts](https://img.shields.io/github/stars/srcx404/CVE-2024-45436.svg) ![forks](https://img.shields.io/github/forks/srcx404/CVE-2024-45436.svg)

## CVE-2024-45352
 An code execution vulnerability exists in the Xiaomi smarthome application product. The vulnerability is caused by improper input validation and can be exploited by attackers to execute malicious code.



- [https://github.com/Edwins907/-CVE-2024-45352](https://github.com/Edwins907/-CVE-2024-45352) :  ![starts](https://img.shields.io/github/stars/Edwins907/-CVE-2024-45352.svg) ![forks](https://img.shields.io/github/forks/Edwins907/-CVE-2024-45352.svg)

- [https://github.com/Edwins907/CVE-2024-45352](https://github.com/Edwins907/CVE-2024-45352) :  ![starts](https://img.shields.io/github/stars/Edwins907/CVE-2024-45352.svg) ![forks](https://img.shields.io/github/forks/Edwins907/CVE-2024-45352.svg)

- [https://github.com/Edwins907/xiaomi-cve-2024-45352](https://github.com/Edwins907/xiaomi-cve-2024-45352) :  ![starts](https://img.shields.io/github/stars/Edwins907/xiaomi-cve-2024-45352.svg) ![forks](https://img.shields.io/github/forks/Edwins907/xiaomi-cve-2024-45352.svg)

- [https://github.com/Edwins907/CVE-2024-45352-xiaomi](https://github.com/Edwins907/CVE-2024-45352-xiaomi) :  ![starts](https://img.shields.io/github/stars/Edwins907/CVE-2024-45352-xiaomi.svg) ![forks](https://img.shields.io/github/forks/Edwins907/CVE-2024-45352-xiaomi.svg)

## CVE-2024-45337
 Applications and libraries which misuse connection.serverAuthenticate (via callback field ServerConfig.PublicKeyCallback) may be susceptible to an authorization bypass. The documentation for ServerConfig.PublicKeyCallback says that "A call to this function does not guarantee that the key offered is in fact used to authenticate." Specifically, the SSH protocol allows clients to inquire about whether a public key is acceptable before proving control of the corresponding private key. PublicKeyCallback may be called with multiple keys, and the order in which the keys were provided cannot be used to infer which key the client successfully authenticated with, if any. Some applications, which store the key(s) passed to PublicKeyCallback (or derived information) and make security relevant determinations based on it once the connection is established, may make incorrect assumptions. For example, an attacker may send public keys A and B, and then authenticate with A. PublicKeyCallback would be called only twice, first with A and then with B. A vulnerable application may then make authorization decisions based on key B for which the attacker does not actually control the private key. Since this API is widely misused, as a partial mitigation golang.org/x/cry...@v0.31.0 enforces the property that, when successfully authenticating via public key, the last key passed to ServerConfig.PublicKeyCallback will be the key used to authenticate the connection. PublicKeyCallback will now be called multiple times with the same key, if necessary. Note that the client may still not control the last key passed to PublicKeyCallback if the connection is then authenticated with a different method, such as PasswordCallback, KeyboardInteractiveCallback, or NoClientAuth. Users should be using the Extensions field of the Permissions return value from the various authentication callbacks to record data associated with the authentication attempt instead of referencing external state. Once the connection is established the state corresponding to the successful authentication attempt can be retrieved via the ServerConn.Permissions field. Note that some third-party libraries misuse the Permissions type by sharing it across authentication attempts; users of third-party libraries should refer to the relevant projects for guidance.



- [https://github.com/NHAS/CVE-2024-45337-POC](https://github.com/NHAS/CVE-2024-45337-POC) :  ![starts](https://img.shields.io/github/stars/NHAS/CVE-2024-45337-POC.svg) ![forks](https://img.shields.io/github/forks/NHAS/CVE-2024-45337-POC.svg)

- [https://github.com/NHAS/VULNERABLE-CVE-2024-45337](https://github.com/NHAS/VULNERABLE-CVE-2024-45337) :  ![starts](https://img.shields.io/github/stars/NHAS/VULNERABLE-CVE-2024-45337.svg) ![forks](https://img.shields.io/github/forks/NHAS/VULNERABLE-CVE-2024-45337.svg)

## CVE-2024-45244
 Hyperledger Fabric through 3.0.0 and 2.5.x through 2.5.9 do not verify that a request has a timestamp within the expected time window.



- [https://github.com/shanker-sec/hlf-time-oracle](https://github.com/shanker-sec/hlf-time-oracle) :  ![starts](https://img.shields.io/github/stars/shanker-sec/hlf-time-oracle.svg) ![forks](https://img.shields.io/github/forks/shanker-sec/hlf-time-oracle.svg)

- [https://github.com/shanker-sec/HLF_TxTime_spoofing](https://github.com/shanker-sec/HLF_TxTime_spoofing) :  ![starts](https://img.shields.io/github/stars/shanker-sec/HLF_TxTime_spoofing.svg) ![forks](https://img.shields.io/github/forks/shanker-sec/HLF_TxTime_spoofing.svg)

## CVE-2024-45216
 Improper Authentication vulnerability in Apache Solr.

Solr instances using the PKIAuthenticationPlugin, which is enabled by default when Solr Authentication is used, are vulnerable to Authentication bypass.
A fake ending at the end of any Solr API URL path, will allow requests to skip Authentication while maintaining the API contract with the original URL Path.
This fake ending looks like an unprotected API path, however it is stripped off internally after authentication but before API routing.


This issue affects Apache Solr: from 5.3.0 before 8.11.4, from 9.0.0 before 9.7.0.

Users are recommended to upgrade to version 9.7.0, or 8.11.4, which fix the issue.



- [https://github.com/congdong007/CVE-2024-45216-Poc](https://github.com/congdong007/CVE-2024-45216-Poc) :  ![starts](https://img.shields.io/github/stars/congdong007/CVE-2024-45216-Poc.svg) ![forks](https://img.shields.io/github/forks/congdong007/CVE-2024-45216-Poc.svg)

## CVE-2024-45195
 Direct Request ('Forced Browsing') vulnerability in Apache OFBiz.

This issue affects Apache OFBiz: before 18.12.16.

Users are recommended to upgrade to version 18.12.16, which fixes the issue.



- [https://github.com/wyyazjjl/CVE-2024-45195](https://github.com/wyyazjjl/CVE-2024-45195) :  ![starts](https://img.shields.io/github/stars/wyyazjjl/CVE-2024-45195.svg) ![forks](https://img.shields.io/github/forks/wyyazjjl/CVE-2024-45195.svg)

## CVE-2024-44871
 An arbitrary file upload vulnerability in the component /admin/index.php of moziloCMS v3.0 allows attackers to execute arbitrary code via uploading a crafted file.



- [https://github.com/vances25/CVE-2024-44871](https://github.com/vances25/CVE-2024-44871) :  ![starts](https://img.shields.io/github/stars/vances25/CVE-2024-44871.svg) ![forks](https://img.shields.io/github/forks/vances25/CVE-2024-44871.svg)

## CVE-2024-44765
 An Improper Authorization (Access Control Misconfiguration) vulnerability in MGT-COMMERCE GmbH CloudPanel v2.0.0 to v2.4.2 allows low-privilege users to bypass access controls and gain unauthorized access to sensitive configuration files and administrative functionality.



- [https://github.com/josephgodwinkimani/cloudpanel-2.4.2-CVE-2024-44765-recovery](https://github.com/josephgodwinkimani/cloudpanel-2.4.2-CVE-2024-44765-recovery) :  ![starts](https://img.shields.io/github/stars/josephgodwinkimani/cloudpanel-2.4.2-CVE-2024-44765-recovery.svg) ![forks](https://img.shields.io/github/forks/josephgodwinkimani/cloudpanel-2.4.2-CVE-2024-44765-recovery.svg)

## CVE-2024-44625
 Gogs =0.13.0 is vulnerable to Directory Traversal via the editFilePost function of internal/route/repo/editor.go.



- [https://github.com/Fysac/CVE-2024-44625](https://github.com/Fysac/CVE-2024-44625) :  ![starts](https://img.shields.io/github/stars/Fysac/CVE-2024-44625.svg) ![forks](https://img.shields.io/github/forks/Fysac/CVE-2024-44625.svg)

## CVE-2024-44610
 PCAN-Ethernet Gateway FD before 1.3.0 and PCAN-Ethernet Gateway before 2.11.0 are vulnerable to Command injection via shell metacharacters in a Software Update to processing.php.



- [https://github.com/BertoldVdb/PcanExploit](https://github.com/BertoldVdb/PcanExploit) :  ![starts](https://img.shields.io/github/stars/BertoldVdb/PcanExploit.svg) ![forks](https://img.shields.io/github/forks/BertoldVdb/PcanExploit.svg)

## CVE-2024-44541
 evilnapsis Inventio Lite Versions v4 and before is vulnerable to SQL Injection via the "username" parameter in "/?action=processlogin."



- [https://github.com/pointedsec/CVE-2024-44541](https://github.com/pointedsec/CVE-2024-44541) :  ![starts](https://img.shields.io/github/stars/pointedsec/CVE-2024-44541.svg) ![forks](https://img.shields.io/github/forks/pointedsec/CVE-2024-44541.svg)

## CVE-2024-44349
 A SQL injection vulnerability in login portal in AnteeoWMS before v4.7.34 allows unauthenticated attackers to execute arbitrary SQL commands via the username parameter and disclosure of some data in the underlying DB.



- [https://github.com/AndreaF17/PoC-CVE-2024-44349](https://github.com/AndreaF17/PoC-CVE-2024-44349) :  ![starts](https://img.shields.io/github/stars/AndreaF17/PoC-CVE-2024-44349.svg) ![forks](https://img.shields.io/github/forks/AndreaF17/PoC-CVE-2024-44349.svg)

## CVE-2024-44308
 The issue was addressed with improved checks. This issue is fixed in Safari 18.1.1, iOS 17.7.2 and iPadOS 17.7.2, macOS Sequoia 15.1.1, iOS 18.1.1 and iPadOS 18.1.1, visionOS 2.1.1. Processing maliciously crafted web content may lead to arbitrary code execution. Apple is aware of a report that this issue may have been actively exploited on Intel-based Mac systems.



- [https://github.com/migopp/cve-2024-44308](https://github.com/migopp/cve-2024-44308) :  ![starts](https://img.shields.io/github/stars/migopp/cve-2024-44308.svg) ![forks](https://img.shields.io/github/forks/migopp/cve-2024-44308.svg)

## CVE-2024-44285
 A use-after-free issue was addressed with improved memory management. This issue is fixed in iOS 18.1 and iPadOS 18.1, watchOS 11.1, visionOS 2.1, tvOS 18.1. An app may be able to cause unexpected system termination or corrupt kernel memory.



- [https://github.com/slds1/explt](https://github.com/slds1/explt) :  ![starts](https://img.shields.io/github/stars/slds1/explt.svg) ![forks](https://img.shields.io/github/forks/slds1/explt.svg)

## CVE-2024-44258
 This issue was addressed with improved handling of symlinks. This issue is fixed in iOS 18.1 and iPadOS 18.1, iOS 17.7.1 and iPadOS 17.7.1, visionOS 2.1, tvOS 18.1. Restoring a maliciously crafted backup file may lead to modification of protected system files.



- [https://github.com/missaels235/POC-CVE-2024-44258-Py](https://github.com/missaels235/POC-CVE-2024-44258-Py) :  ![starts](https://img.shields.io/github/stars/missaels235/POC-CVE-2024-44258-Py.svg) ![forks](https://img.shields.io/github/forks/missaels235/POC-CVE-2024-44258-Py.svg)

## CVE-2024-44235
 The issue was addressed with improved checks. This issue is fixed in iOS 18.1 and iPadOS 18.1. An attacker may be able to view restricted content from the lock screen.



- [https://github.com/richeeta/DEFCON33-Siriously-Leaky](https://github.com/richeeta/DEFCON33-Siriously-Leaky) :  ![starts](https://img.shields.io/github/stars/richeeta/DEFCON33-Siriously-Leaky.svg) ![forks](https://img.shields.io/github/forks/richeeta/DEFCON33-Siriously-Leaky.svg)

## CVE-2024-44133
 This issue was addressed by removing the vulnerable code. This issue is fixed in macOS Sequoia 15. On MDM managed devices, an app may be able to bypass certain Privacy preferences.



- [https://github.com/yo-yo-yo-jbo/hm-surf](https://github.com/yo-yo-yo-jbo/hm-surf) :  ![starts](https://img.shields.io/github/stars/yo-yo-yo-jbo/hm-surf.svg) ![forks](https://img.shields.io/github/forks/yo-yo-yo-jbo/hm-surf.svg)

- [https://github.com/Ununp3ntium115/prevent_cve_2024_44133](https://github.com/Ununp3ntium115/prevent_cve_2024_44133) :  ![starts](https://img.shields.io/github/stars/Ununp3ntium115/prevent_cve_2024_44133.svg) ![forks](https://img.shields.io/github/forks/Ununp3ntium115/prevent_cve_2024_44133.svg)

## CVE-2024-43919
 Access Control vulnerability in YARPP YARPP allows .

This issue affects YARPP: from n/a through 5.30.10.



- [https://github.com/RandomRobbieBF/CVE-2024-43919](https://github.com/RandomRobbieBF/CVE-2024-43919) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-43919.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-43919.svg)

## CVE-2024-43788
 Webpack is a module bundler. Its main purpose is to bundle JavaScript files for usage in a browser, yet it is also capable of transforming, bundling, or packaging just about any resource or asset. The webpack developers have discovered a DOM Clobbering vulnerability in Webpack’s `AutoPublicPathRuntimeModule`. The DOM Clobbering gadget in the module can lead to cross-site scripting (XSS) in web pages where scriptless attacker-controlled HTML elements (e.g., an `img` tag with an unsanitized `name` attribute) are present. Real-world exploitation of this gadget has been observed in the Canvas LMS which allows a XSS attack to happen through a javascript code compiled by Webpack (the vulnerable part is from Webpack). DOM Clobbering is a type of code-reuse attack where the attacker first embeds a piece of non-script, seemingly benign HTML markups in the webpage (e.g. through a post or comment) and leverages the gadgets (pieces of js code) living in the existing javascript code to transform it into executable code. This vulnerability can lead to cross-site scripting (XSS) on websites that include Webpack-generated files and allow users to inject certain scriptless HTML tags with improperly sanitized name or id attributes. This issue has been addressed in release version 5.94.0. All users are advised to upgrade. There are no known workarounds for this issue.



- [https://github.com/batzionb/webpack-cve-2024-43788](https://github.com/batzionb/webpack-cve-2024-43788) :  ![starts](https://img.shields.io/github/stars/batzionb/webpack-cve-2024-43788.svg) ![forks](https://img.shields.io/github/forks/batzionb/webpack-cve-2024-43788.svg)

## CVE-2024-43468
 Microsoft Configuration Manager Remote Code Execution Vulnerability



- [https://github.com/synacktiv/CVE-2024-43468](https://github.com/synacktiv/CVE-2024-43468) :  ![starts](https://img.shields.io/github/stars/synacktiv/CVE-2024-43468.svg) ![forks](https://img.shields.io/github/forks/synacktiv/CVE-2024-43468.svg)

## CVE-2024-43425
 A flaw was found in Moodle. Additional restrictions are required to avoid a remote code execution risk in calculated question types. Note: This requires the capability to add/update questions.



- [https://github.com/aayush256-sys/Moodle-authenticated-RCE](https://github.com/aayush256-sys/Moodle-authenticated-RCE) :  ![starts](https://img.shields.io/github/stars/aayush256-sys/Moodle-authenticated-RCE.svg) ![forks](https://img.shields.io/github/forks/aayush256-sys/Moodle-authenticated-RCE.svg)

- [https://github.com/aninfosec/CVE-2024-43425-Poc](https://github.com/aninfosec/CVE-2024-43425-Poc) :  ![starts](https://img.shields.io/github/stars/aninfosec/CVE-2024-43425-Poc.svg) ![forks](https://img.shields.io/github/forks/aninfosec/CVE-2024-43425-Poc.svg)

## CVE-2024-43416
 GLPI is a free asset and IT management software package. Starting in version 0.80 and prior to version 10.0.17, an unauthenticated user can use an application endpoint to check if an email address corresponds to a valid GLPI user. Version 10.0.17 fixes the issue.



- [https://github.com/0xmupa/CVE-2024-43416-PoC](https://github.com/0xmupa/CVE-2024-43416-PoC) :  ![starts](https://img.shields.io/github/stars/0xmupa/CVE-2024-43416-PoC.svg) ![forks](https://img.shields.io/github/forks/0xmupa/CVE-2024-43416-PoC.svg)

## CVE-2024-43044
 Jenkins 2.470 and earlier, LTS 2.452.3 and earlier allows agent processes to read arbitrary files from the Jenkins controller file system by using the `ClassLoaderProxy#fetchJar` method in the Remoting library.



- [https://github.com/v9d0g/CVE-2024-43044-POC](https://github.com/v9d0g/CVE-2024-43044-POC) :  ![starts](https://img.shields.io/github/stars/v9d0g/CVE-2024-43044-POC.svg) ![forks](https://img.shields.io/github/forks/v9d0g/CVE-2024-43044-POC.svg)

- [https://github.com/HwMex0/CVE-2024-43044](https://github.com/HwMex0/CVE-2024-43044) :  ![starts](https://img.shields.io/github/stars/HwMex0/CVE-2024-43044.svg) ![forks](https://img.shields.io/github/forks/HwMex0/CVE-2024-43044.svg)

- [https://github.com/jenkinsci-cert/SECURITY-3430](https://github.com/jenkinsci-cert/SECURITY-3430) :  ![starts](https://img.shields.io/github/stars/jenkinsci-cert/SECURITY-3430.svg) ![forks](https://img.shields.io/github/forks/jenkinsci-cert/SECURITY-3430.svg)

- [https://github.com/DACC4/CVE-2024-43044-jenkins-creds](https://github.com/DACC4/CVE-2024-43044-jenkins-creds) :  ![starts](https://img.shields.io/github/stars/DACC4/CVE-2024-43044-jenkins-creds.svg) ![forks](https://img.shields.io/github/forks/DACC4/CVE-2024-43044-jenkins-creds.svg)

## CVE-2024-43018
 Piwigo 13.8.0 and below is vulnerable to SQL Injection in the parameters max_level and min_register. These parameters are used in ws_user_gerList function from file include\ws_functions\pwg.users.php and this same function is called by ws.php file at some point can be used for searching users in advanced way in /admin.php?page=user_list.



- [https://github.com/joaosilva21/CVE-2024-43018](https://github.com/joaosilva21/CVE-2024-43018) :  ![starts](https://img.shields.io/github/stars/joaosilva21/CVE-2024-43018.svg) ![forks](https://img.shields.io/github/forks/joaosilva21/CVE-2024-43018.svg)

## CVE-2024-42845
 An eval Injection vulnerability in the component invesalius/reader/dicom.py of InVesalius 3.1.99991 through 3.1.99998 allows attackers to execute arbitrary code via loading a crafted DICOM file.



- [https://github.com/theexploiters/CVE-2024-42845-Exploit](https://github.com/theexploiters/CVE-2024-42845-Exploit) :  ![starts](https://img.shields.io/github/stars/theexploiters/CVE-2024-42845-Exploit.svg) ![forks](https://img.shields.io/github/forks/theexploiters/CVE-2024-42845-Exploit.svg)

## CVE-2024-42640
 angular-base64-upload prior to v0.1.21 is vulnerable to unauthenticated remote code execution via demo/server.php. Exploiting this vulnerability allows an attacker to upload arbitrary content to the server, which can subsequently be accessed through demo/uploads. This leads to the execution of previously uploaded content and enables the attacker to achieve code execution on the server. NOTE: This vulnerability only affects products that are no longer supported by the maintainer.



- [https://github.com/KTN1990/CVE-2024-42640](https://github.com/KTN1990/CVE-2024-42640) :  ![starts](https://img.shields.io/github/stars/KTN1990/CVE-2024-42640.svg) ![forks](https://img.shields.io/github/forks/KTN1990/CVE-2024-42640.svg)

## CVE-2024-42471
 actions/artifact is the GitHub ToolKit for developing GitHub Actions.  Versions of `actions/artifact` on the 2.x branch before 2.1.2 are vulnerable to arbitrary file write when using `downloadArtifactInternal`, `downloadArtifactPublic`, or `streamExtractExternal` for extracting a specifically crafted artifact that contains path traversal filenames. Users are advised to upgrade to version 2.1.2 or higher. There are no known workarounds for this issue.



- [https://github.com/theMcSam/CVE-2024-42471-PoC](https://github.com/theMcSam/CVE-2024-42471-PoC) :  ![starts](https://img.shields.io/github/stars/theMcSam/CVE-2024-42471-PoC.svg) ![forks](https://img.shields.io/github/forks/theMcSam/CVE-2024-42471-PoC.svg)

## CVE-2024-42461
 In the Elliptic package 6.5.6 for Node.js, ECDSA signature malleability occurs because BER-encoded signatures are allowed.



- [https://github.com/fevar54/CVE-2024-42461](https://github.com/fevar54/CVE-2024-42461) :  ![starts](https://img.shields.io/github/stars/fevar54/CVE-2024-42461.svg) ![forks](https://img.shields.io/github/forks/fevar54/CVE-2024-42461.svg)

## CVE-2024-42448
 From the VSPC management agent machine, under condition that the management agent is authorized on the server, it is possible to perform Remote Code Execution (RCE) on the VSPC server machine.



- [https://github.com/h3lye/CVE-2024-42448-RCE](https://github.com/h3lye/CVE-2024-42448-RCE) :  ![starts](https://img.shields.io/github/stars/h3lye/CVE-2024-42448-RCE.svg) ![forks](https://img.shields.io/github/forks/h3lye/CVE-2024-42448-RCE.svg)

## CVE-2024-42364
 Homepage is a highly customizable homepage with Docker and service API integrations. The default setup of homepage 0.9.1 is vulnerable to DNS rebinding. Homepage is setup without certificate and authentication by default, leaving it to vulnerable to DNS rebinding. In this attack, an attacker will ask a user to visit his/her website. The attacker website will then change the DNS records of their domain from their IP address to the internal IP address of the homepage instance. To tell which IP addresses are valid, we can rebind a subdomain to each IP address we want to check, and see if there is a response. Once potential candidates have been found, the attacker can launch the attack by reading the response of the webserver after the IP address has changed. When the attacker domain is fetched, the response will be from the homepage instance, not the attacker website, because the IP address has been changed. Due to a lack of authentication, a user’s private information such as API keys (fixed after first report) and other private information can then be extracted by the attacker website.



- [https://github.com/ibrahmsql/CVE-2024-42364](https://github.com/ibrahmsql/CVE-2024-42364) :  ![starts](https://img.shields.io/github/stars/ibrahmsql/CVE-2024-42364.svg) ![forks](https://img.shields.io/github/forks/ibrahmsql/CVE-2024-42364.svg)

## CVE-2024-42346
 Galaxy is a free, open-source system for analyzing data, authoring workflows, training and education, publishing tools, managing infrastructure, and more. The editor visualization, /visualizations endpoint, can be used to store HTML tags and trigger javascript execution upon edit operation. All supported branches of Galaxy (and more back to release_20.05) were amended with the supplied patches. Users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/partywavesec/CVE-2024-42346](https://github.com/partywavesec/CVE-2024-42346) :  ![starts](https://img.shields.io/github/stars/partywavesec/CVE-2024-42346.svg) ![forks](https://img.shields.io/github/forks/partywavesec/CVE-2024-42346.svg)

## CVE-2024-42327
 A non-admin user account on the Zabbix frontend with the default User role, or with any other role that gives API access can exploit this vulnerability. An SQLi exists in the CUser class in the addRelatedObjects function, this function is being called from the CUser.get function which is available for every user who has API access.



- [https://github.com/BridgerAlderson/Zabbix-CVE-2024-42327-SQL-Injection-RCE](https://github.com/BridgerAlderson/Zabbix-CVE-2024-42327-SQL-Injection-RCE) :  ![starts](https://img.shields.io/github/stars/BridgerAlderson/Zabbix-CVE-2024-42327-SQL-Injection-RCE.svg) ![forks](https://img.shields.io/github/forks/BridgerAlderson/Zabbix-CVE-2024-42327-SQL-Injection-RCE.svg)

- [https://github.com/aramosf/cve-2024-42327](https://github.com/aramosf/cve-2024-42327) :  ![starts](https://img.shields.io/github/stars/aramosf/cve-2024-42327.svg) ![forks](https://img.shields.io/github/forks/aramosf/cve-2024-42327.svg)

- [https://github.com/compr00t/CVE-2024-42327](https://github.com/compr00t/CVE-2024-42327) :  ![starts](https://img.shields.io/github/stars/compr00t/CVE-2024-42327.svg) ![forks](https://img.shields.io/github/forks/compr00t/CVE-2024-42327.svg)

- [https://github.com/watchdog1337/CVE-2024-42327_Zabbix_SQLI](https://github.com/watchdog1337/CVE-2024-42327_Zabbix_SQLI) :  ![starts](https://img.shields.io/github/stars/watchdog1337/CVE-2024-42327_Zabbix_SQLI.svg) ![forks](https://img.shields.io/github/forks/watchdog1337/CVE-2024-42327_Zabbix_SQLI.svg)

- [https://github.com/depers-rus/CVE-2024-42327](https://github.com/depers-rus/CVE-2024-42327) :  ![starts](https://img.shields.io/github/stars/depers-rus/CVE-2024-42327.svg) ![forks](https://img.shields.io/github/forks/depers-rus/CVE-2024-42327.svg)

- [https://github.com/igorbf495/CVE-2024-42327](https://github.com/igorbf495/CVE-2024-42327) :  ![starts](https://img.shields.io/github/stars/igorbf495/CVE-2024-42327.svg) ![forks](https://img.shields.io/github/forks/igorbf495/CVE-2024-42327.svg)

- [https://github.com/itform-fr/Zabbix---CVE-2024-42327](https://github.com/itform-fr/Zabbix---CVE-2024-42327) :  ![starts](https://img.shields.io/github/stars/itform-fr/Zabbix---CVE-2024-42327.svg) ![forks](https://img.shields.io/github/forks/itform-fr/Zabbix---CVE-2024-42327.svg)

- [https://github.com/874anthony/CVE-2024-42327_Zabbix_SQLi](https://github.com/874anthony/CVE-2024-42327_Zabbix_SQLi) :  ![starts](https://img.shields.io/github/stars/874anthony/CVE-2024-42327_Zabbix_SQLi.svg) ![forks](https://img.shields.io/github/forks/874anthony/CVE-2024-42327_Zabbix_SQLi.svg)

## CVE-2024-42009
 A Cross-Site Scripting vulnerability in Roundcube through 1.5.7 and 1.6.x through 1.6.7 allows a remote attacker to steal and send emails of a victim via a crafted e-mail message that abuses a Desanitization issue in message_body() in program/actions/mail/show.php.



- [https://github.com/DaniTheHack3r/CVE-2024-42009-PoC](https://github.com/DaniTheHack3r/CVE-2024-42009-PoC) :  ![starts](https://img.shields.io/github/stars/DaniTheHack3r/CVE-2024-42009-PoC.svg) ![forks](https://img.shields.io/github/forks/DaniTheHack3r/CVE-2024-42009-PoC.svg)

- [https://github.com/Foxer131/CVE-2024-42008-9-exploit](https://github.com/Foxer131/CVE-2024-42008-9-exploit) :  ![starts](https://img.shields.io/github/stars/Foxer131/CVE-2024-42008-9-exploit.svg) ![forks](https://img.shields.io/github/forks/Foxer131/CVE-2024-42008-9-exploit.svg)

## CVE-2024-42008
 A Cross-Site Scripting vulnerability in rcmail_action_mail_get-run() in Roundcube through 1.5.7 and 1.6.x through 1.6.7 allows a remote attacker to steal and send emails of a victim via a malicious e-mail attachment served with a dangerous Content-Type header.



- [https://github.com/rpgsec/Roundcube-CVE-2024-42008-POC](https://github.com/rpgsec/Roundcube-CVE-2024-42008-POC) :  ![starts](https://img.shields.io/github/stars/rpgsec/Roundcube-CVE-2024-42008-POC.svg) ![forks](https://img.shields.io/github/forks/rpgsec/Roundcube-CVE-2024-42008-POC.svg)

- [https://github.com/Foxer131/CVE-2024-42008-9-exploit](https://github.com/Foxer131/CVE-2024-42008-9-exploit) :  ![starts](https://img.shields.io/github/stars/Foxer131/CVE-2024-42008-9-exploit.svg) ![forks](https://img.shields.io/github/forks/Foxer131/CVE-2024-42008-9-exploit.svg)

## CVE-2024-42007
 SPX (aka php-spx) through 0.4.15 allows SPX_UI_URI Directory Traversal to read arbitrary files.



- [https://github.com/BubblyCola/CVE_2024_42007](https://github.com/BubblyCola/CVE_2024_42007) :  ![starts](https://img.shields.io/github/stars/BubblyCola/CVE_2024_42007.svg) ![forks](https://img.shields.io/github/forks/BubblyCola/CVE_2024_42007.svg)

## CVE-2024-41958
 mailcow: dockerized is an open source groupware/email suite based on docker. A vulnerability has been discovered in the two-factor authentication (2FA) mechanism. This flaw allows an authenticated attacker to bypass the 2FA protection, enabling unauthorized access to other accounts that are otherwise secured with 2FA. To exploit this vulnerability, the attacker must first have access to an account within the system and possess the credentials of the target account that has 2FA enabled. By leveraging these credentials, the attacker can circumvent the 2FA process and gain access to the protected account. This issue has been addressed in the `2024-07` release. All users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/OrangeJuiceHU/CVE-2024-41958-PoC](https://github.com/OrangeJuiceHU/CVE-2024-41958-PoC) :  ![starts](https://img.shields.io/github/stars/OrangeJuiceHU/CVE-2024-41958-PoC.svg) ![forks](https://img.shields.io/github/forks/OrangeJuiceHU/CVE-2024-41958-PoC.svg)

## CVE-2024-41713
 A vulnerability in the NuPoint Unified Messaging (NPM) component of Mitel MiCollab through 9.8 SP1 FP2 (9.8.1.201) could allow an unauthenticated attacker to conduct a path traversal attack, due to insufficient input validation. A successful exploit could allow unauthorized access, enabling the attacker to view, corrupt, or delete users' data and system configurations.



- [https://github.com/watchtowrlabs/Mitel-MiCollab-Auth-Bypass_CVE-2024-41713](https://github.com/watchtowrlabs/Mitel-MiCollab-Auth-Bypass_CVE-2024-41713) :  ![starts](https://img.shields.io/github/stars/watchtowrlabs/Mitel-MiCollab-Auth-Bypass_CVE-2024-41713.svg) ![forks](https://img.shields.io/github/forks/watchtowrlabs/Mitel-MiCollab-Auth-Bypass_CVE-2024-41713.svg)

- [https://github.com/Sanandd/cve-2024-CVE-2024-41713](https://github.com/Sanandd/cve-2024-CVE-2024-41713) :  ![starts](https://img.shields.io/github/stars/Sanandd/cve-2024-CVE-2024-41713.svg) ![forks](https://img.shields.io/github/forks/Sanandd/cve-2024-CVE-2024-41713.svg)

- [https://github.com/amanverma-wsu/CVE-2024-41713-Scan](https://github.com/amanverma-wsu/CVE-2024-41713-Scan) :  ![starts](https://img.shields.io/github/stars/amanverma-wsu/CVE-2024-41713-Scan.svg) ![forks](https://img.shields.io/github/forks/amanverma-wsu/CVE-2024-41713-Scan.svg)

- [https://github.com/zxj-hub/CVE-2024-41713POC](https://github.com/zxj-hub/CVE-2024-41713POC) :  ![starts](https://img.shields.io/github/stars/zxj-hub/CVE-2024-41713POC.svg) ![forks](https://img.shields.io/github/forks/zxj-hub/CVE-2024-41713POC.svg)

- [https://github.com/gunyakit/CVE-2024-41713-PoC-exploit](https://github.com/gunyakit/CVE-2024-41713-PoC-exploit) :  ![starts](https://img.shields.io/github/stars/gunyakit/CVE-2024-41713-PoC-exploit.svg) ![forks](https://img.shields.io/github/forks/gunyakit/CVE-2024-41713-PoC-exploit.svg)

## CVE-2024-41662
 VNote is a note-taking platform. A Cross-Site Scripting (XSS) vulnerability has been identified in the Markdown rendering functionality of versions 3.18.1 and prior of the VNote note-taking application. This vulnerability allows the injection and execution of arbitrary JavaScript code through which remote code execution can be achieved. A patch for this issue is available at commit f1af78573a0ef51d6ef6a0bc4080cddc8f30a545. Other mitigation strategies include implementing rigorous input sanitization for all Markdown content and utilizing a secure Markdown parser that appropriately escapes or strips potentially dangerous content.



- [https://github.com/sh3bu/CVE-2024-41662](https://github.com/sh3bu/CVE-2024-41662) :  ![starts](https://img.shields.io/github/stars/sh3bu/CVE-2024-41662.svg) ![forks](https://img.shields.io/github/forks/sh3bu/CVE-2024-41662.svg)

## CVE-2024-41651
 An issue in Prestashop v.8.1.7 and before allows a remote attacker to execute arbitrary code via the module upgrade functionality. NOTE: this is disputed by multiple parties, who report that exploitation requires that an attacker be able to hijack network requests made by an admin user (who, by design, is allowed to change the code that is running on the server).



- [https://github.com/Fckroun/CVE-2024-41651](https://github.com/Fckroun/CVE-2024-41651) :  ![starts](https://img.shields.io/github/stars/Fckroun/CVE-2024-41651.svg) ![forks](https://img.shields.io/github/forks/Fckroun/CVE-2024-41651.svg)

## CVE-2024-41640
 Cross Site Scripting (XSS) vulnerability in AML Surety Eco up to 3.5 allows an attacker to run arbitrary code via crafted GET request using the id parameter.



- [https://github.com/alemusix/CVE-2024-41640](https://github.com/alemusix/CVE-2024-41640) :  ![starts](https://img.shields.io/github/stars/alemusix/CVE-2024-41640.svg) ![forks](https://img.shields.io/github/forks/alemusix/CVE-2024-41640.svg)

## CVE-2024-41628
 Directory Traversal vulnerability in Severalnines Cluster Control 1.9.8 before 1.9.8-9778, 2.0.0 before 2.0.0-9779, and 2.1.0 before 2.1.0-9780 allows a remote attacker to include and display file content in an HTTP request via the CMON API.



- [https://github.com/Redshift-CyberSecurity/CVE-2024-41628](https://github.com/Redshift-CyberSecurity/CVE-2024-41628) :  ![starts](https://img.shields.io/github/stars/Redshift-CyberSecurity/CVE-2024-41628.svg) ![forks](https://img.shields.io/github/forks/Redshift-CyberSecurity/CVE-2024-41628.svg)

## CVE-2024-41570
 An Unauthenticated Server-Side Request Forgery (SSRF) in demon callback handling in Havoc 2 0.7 allows attackers to send arbitrary network traffic originating from the team server.



- [https://github.com/chebuya/Havoc-C2-SSRF-poc](https://github.com/chebuya/Havoc-C2-SSRF-poc) :  ![starts](https://img.shields.io/github/stars/chebuya/Havoc-C2-SSRF-poc.svg) ![forks](https://img.shields.io/github/forks/chebuya/Havoc-C2-SSRF-poc.svg)

## CVE-2024-41505
 Jetimob Plataforma Imobiliaria 20240627-0 is vulnerable to Cross Site Scripting (XSS) in the "Pessoas" (persons) section via the field "Profisso" (professor).



- [https://github.com/rafaelbaldasso/CVE-2024-41505](https://github.com/rafaelbaldasso/CVE-2024-41505) :  ![starts](https://img.shields.io/github/stars/rafaelbaldasso/CVE-2024-41505.svg) ![forks](https://img.shields.io/github/forks/rafaelbaldasso/CVE-2024-41505.svg)

## CVE-2024-41504
 Jetimob Plataforma Imobiliaria 20240627-0 is vulnerable to Cross Site Scripting (XSS). In the "Oportunidades" (opportunities) section of the application when creating or editing an "Atividade" (activity), the form field "Descrico" allows injection of JavaScript.



- [https://github.com/rafaelbaldasso/CVE-2024-41504](https://github.com/rafaelbaldasso/CVE-2024-41504) :  ![starts](https://img.shields.io/github/stars/rafaelbaldasso/CVE-2024-41504.svg) ![forks](https://img.shields.io/github/forks/rafaelbaldasso/CVE-2024-41504.svg)

## CVE-2024-41503
 Jetimob Plataforma Imobiliaria 20240627-0 is vulnerable to Cross Site Scripting (XSS) in the field "Ttulo" (title) inside the filter Save option in the "Busca" (search) function.



- [https://github.com/rafaelbaldasso/CVE-2024-41503](https://github.com/rafaelbaldasso/CVE-2024-41503) :  ![starts](https://img.shields.io/github/stars/rafaelbaldasso/CVE-2024-41503.svg) ![forks](https://img.shields.io/github/forks/rafaelbaldasso/CVE-2024-41503.svg)

## CVE-2024-41502
 Jetimob Plataforma Imobiliaria 20240627-0 is vulnerable to Cross Site Scripting (XSS) via the form field "Observaces" (observances) in the "Pessoas" (persons) section when creating or editing either a legal or a natural person.



- [https://github.com/rafaelbaldasso/CVE-2024-41502](https://github.com/rafaelbaldasso/CVE-2024-41502) :  ![starts](https://img.shields.io/github/stars/rafaelbaldasso/CVE-2024-41502.svg) ![forks](https://img.shields.io/github/forks/rafaelbaldasso/CVE-2024-41502.svg)

## CVE-2024-41454
 An arbitrary file upload vulnerability in the UI login page logo upload function of Process Maker pm4core-docker 4.1.21-RC7 allows attackers to execute arbitrary code via uploading a crafted PHP or HTML file.



- [https://github.com/code5ecure/CVE-2024-41453_CVE-2024-41454](https://github.com/code5ecure/CVE-2024-41453_CVE-2024-41454) :  ![starts](https://img.shields.io/github/stars/code5ecure/CVE-2024-41453_CVE-2024-41454.svg) ![forks](https://img.shields.io/github/forks/code5ecure/CVE-2024-41453_CVE-2024-41454.svg)

## CVE-2024-41453
 A cross-site scripting (XSS) vulnerability in Process Maker pm4core-docker 4.1.21-RC7 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the Name parameter.



- [https://github.com/code5ecure/CVE-2024-41453_CVE-2024-41454](https://github.com/code5ecure/CVE-2024-41453_CVE-2024-41454) :  ![starts](https://img.shields.io/github/stars/code5ecure/CVE-2024-41453_CVE-2024-41454.svg) ![forks](https://img.shields.io/github/forks/code5ecure/CVE-2024-41453_CVE-2024-41454.svg)

## CVE-2024-41319
 TOTOLINK A6000R V1.0.1-B20201211.2000 was discovered to contain a command injection vulnerability via the cmd parameter in the webcmd function.



- [https://github.com/NingXin2002/TOTOLINK_poc](https://github.com/NingXin2002/TOTOLINK_poc) :  ![starts](https://img.shields.io/github/stars/NingXin2002/TOTOLINK_poc.svg) ![forks](https://img.shields.io/github/forks/NingXin2002/TOTOLINK_poc.svg)

## CVE-2024-41276
 A vulnerability in Kaiten version 57.131.12 and earlier allows attackers to bypass the PIN code authentication mechanism. The application requires users to input a 6-digit PIN code sent to their email for authorization after entering their login credentials. However, the request limiting mechanism can be easily bypassed, enabling attackers to perform a brute force attack to guess the correct PIN and gain unauthorized access to the application.



- [https://github.com/artemy-ccrsky/CVE-2024-41276](https://github.com/artemy-ccrsky/CVE-2024-41276) :  ![starts](https://img.shields.io/github/stars/artemy-ccrsky/CVE-2024-41276.svg) ![forks](https://img.shields.io/github/forks/artemy-ccrsky/CVE-2024-41276.svg)

## CVE-2024-41110
 Moby is an open-source project created by Docker for software containerization. A security vulnerability has been detected in certain versions of Docker Engine, which could allow an attacker to bypass authorization plugins (AuthZ) under specific circumstances. The base likelihood of this being exploited is low.

Using a specially-crafted API request, an Engine API client could make the daemon forward the request or response to an authorization plugin without the body. In certain circumstances, the authorization plugin may allow a request which it would have otherwise denied if the body had been forwarded to it.

A security issue was discovered In 2018, where an attacker could bypass AuthZ plugins using a specially crafted API request. This could lead to unauthorized actions, including privilege escalation. Although this issue was fixed in Docker Engine v18.09.1 in January 2019, the fix was not carried forward to later major versions, resulting in a regression. Anyone who depends on authorization plugins that introspect the request and/or response body to make access control decisions is potentially impacted.

Docker EE v19.03.x and all versions of Mirantis Container Runtime are not vulnerable.

docker-ce v27.1.1 containes patches to fix the vulnerability. Patches have also been merged into the master, 19.03, 20.0, 23.0, 24.0, 25.0, 26.0, and 26.1 release branches. If one is unable to upgrade immediately, avoid using AuthZ plugins and/or restrict access to the Docker API to trusted parties, following the principle of least privilege.



- [https://github.com/vvpoglazov/cve-2024-41110-checker](https://github.com/vvpoglazov/cve-2024-41110-checker) :  ![starts](https://img.shields.io/github/stars/vvpoglazov/cve-2024-41110-checker.svg) ![forks](https://img.shields.io/github/forks/vvpoglazov/cve-2024-41110-checker.svg)

- [https://github.com/PauloParoPP/CVE-2024-41110-SCAN](https://github.com/PauloParoPP/CVE-2024-41110-SCAN) :  ![starts](https://img.shields.io/github/stars/PauloParoPP/CVE-2024-41110-SCAN.svg) ![forks](https://img.shields.io/github/forks/PauloParoPP/CVE-2024-41110-SCAN.svg)

## CVE-2024-41107
 The CloudStack SAML authentication (disabled by default) does not enforce signature check. In CloudStack environments where SAML authentication is enabled, an attacker that initiates CloudStack SAML single sign-on authentication can bypass SAML authentication by submitting a spoofed SAML response with no signature and known or guessed username and other user details of a SAML-enabled CloudStack user-account. In such environments, this can result in a complete compromise of the resources owned and/or accessible by a SAML enabled user-account.

Affected users are recommended to disable the SAML authentication plugin by setting the "saml2.enabled" global setting to "false", or upgrade to version 4.18.2.2, 4.19.1.0 or later, which addresses this issue.



- [https://github.com/d0rb/CVE-2024-41107](https://github.com/d0rb/CVE-2024-41107) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2024-41107.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2024-41107.svg)

## CVE-2024-40898
 SSRF in Apache HTTP Server on Windows with mod_rewrite in server/vhost context, allows to potentially leak NTML hashes to a malicious server via SSRF and malicious requests.

Users are recommended to upgrade to version 2.4.62 which fixes this issue. 



- [https://github.com/TAM-K592/CVE-2024-40725-CVE-2024-40898](https://github.com/TAM-K592/CVE-2024-40725-CVE-2024-40898) :  ![starts](https://img.shields.io/github/stars/TAM-K592/CVE-2024-40725-CVE-2024-40898.svg) ![forks](https://img.shields.io/github/forks/TAM-K592/CVE-2024-40725-CVE-2024-40898.svg)

- [https://github.com/ForceEA001/CVE-2024-40898-SSL-Bypass-Detection](https://github.com/ForceEA001/CVE-2024-40898-SSL-Bypass-Detection) :  ![starts](https://img.shields.io/github/stars/ForceEA001/CVE-2024-40898-SSL-Bypass-Detection.svg) ![forks](https://img.shields.io/github/forks/ForceEA001/CVE-2024-40898-SSL-Bypass-Detection.svg)

## CVE-2024-40725
 A partial fix for  CVE-2024-39884 in the core of Apache HTTP Server 2.4.61 ignores some use of the legacy content-type based configuration of handlers. "AddType" and similar configuration, under some circumstances where files are requested indirectly, result in source code disclosure of local content. For example, PHP scripts may be served instead of interpreted.

Users are recommended to upgrade to version 2.4.62, which fixes this issue.





- [https://github.com/TAM-K592/CVE-2024-40725-CVE-2024-40898](https://github.com/TAM-K592/CVE-2024-40725-CVE-2024-40898) :  ![starts](https://img.shields.io/github/stars/TAM-K592/CVE-2024-40725-CVE-2024-40898.svg) ![forks](https://img.shields.io/github/forks/TAM-K592/CVE-2024-40725-CVE-2024-40898.svg)

- [https://github.com/soltanali0/CVE-2024-40725](https://github.com/soltanali0/CVE-2024-40725) :  ![starts](https://img.shields.io/github/stars/soltanali0/CVE-2024-40725.svg) ![forks](https://img.shields.io/github/forks/soltanali0/CVE-2024-40725.svg)

## CVE-2024-40711
 A deserialization of untrusted data vulnerability with a malicious payload can allow an unauthenticated remote code execution (RCE).



- [https://github.com/XiaomingX/cve-2024-40711-poc](https://github.com/XiaomingX/cve-2024-40711-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-40711-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-40711-poc.svg)

## CVE-2024-40676
 In checkKeyIntent of AccountManagerService.java, there is a possible way to bypass intent security check and install an unknown app due to a confused deputy. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/CrackerCat/accounts_CVE-2024-40676-](https://github.com/CrackerCat/accounts_CVE-2024-40676-) :  ![starts](https://img.shields.io/github/stars/CrackerCat/accounts_CVE-2024-40676-.svg) ![forks](https://img.shields.io/github/forks/CrackerCat/accounts_CVE-2024-40676-.svg)

## CVE-2024-40662
 In scheme of Uri.java, there is a possible way to craft a malformed Uri object due to improper input validation. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/bb33bb/net_G2.5_CVE-2024-40662](https://github.com/bb33bb/net_G2.5_CVE-2024-40662) :  ![starts](https://img.shields.io/github/stars/bb33bb/net_G2.5_CVE-2024-40662.svg) ![forks](https://img.shields.io/github/forks/bb33bb/net_G2.5_CVE-2024-40662.svg)

## CVE-2024-40635
 containerd is an open-source container runtime. A bug was found in containerd prior to versions 1.6.38, 1.7.27, and 2.0.4 where containers launched with a User set as a `UID:GID` larger than the maximum 32-bit signed integer can cause an overflow condition where the container ultimately runs as root (UID 0). This could cause unexpected behavior for environments that require containers to run as a non-root user. This bug has been fixed in containerd 1.6.38, 1.7.27, and 2.04. As a workaround, ensure that only trusted images are used and that only trusted users have permissions to import images.



- [https://github.com/yen5004/CVE-2024-40635_POC](https://github.com/yen5004/CVE-2024-40635_POC) :  ![starts](https://img.shields.io/github/stars/yen5004/CVE-2024-40635_POC.svg) ![forks](https://img.shields.io/github/forks/yen5004/CVE-2024-40635_POC.svg)

## CVE-2024-40617
 Path traversal vulnerability exists in FUJITSU Network Edgiot GW1500 (M2M-GW for FENICS). If a remote authenticated attacker with User Class privilege sends a specially crafted request to the affected product, access restricted files containing sensitive information may be accessed. As a result, Administrator Class privileges of the product may be hijacked.



- [https://github.com/KyssK00L/CVE-2024-40617](https://github.com/KyssK00L/CVE-2024-40617) :  ![starts](https://img.shields.io/github/stars/KyssK00L/CVE-2024-40617.svg) ![forks](https://img.shields.io/github/forks/KyssK00L/CVE-2024-40617.svg)

## CVE-2024-40586
 An Improper Access Control vulnerability [CWE-284] in FortiClient Windows version 7.4.0, version 7.2.6 and below, version 7.0.13 and below may allow a local user to escalate his privileges via FortiSSLVPNd service pipe.



- [https://github.com/Hagrid29/CVE-2024-40586-Windows-Coerced-Authentication-in-FortiClient](https://github.com/Hagrid29/CVE-2024-40586-Windows-Coerced-Authentication-in-FortiClient) :  ![starts](https://img.shields.io/github/stars/Hagrid29/CVE-2024-40586-Windows-Coerced-Authentication-in-FortiClient.svg) ![forks](https://img.shields.io/github/forks/Hagrid29/CVE-2024-40586-Windows-Coerced-Authentication-in-FortiClient.svg)

## CVE-2024-40512
 Cross Site Scripting vulnerability in openPetra v.2023.02 allows a remote attacker to obtain sensitive information via the serverMReporting.asmx function.



- [https://github.com/Jansen-C-Moreira/CVE-2024-40512](https://github.com/Jansen-C-Moreira/CVE-2024-40512) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40512.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40512.svg)

## CVE-2024-40511
 Cross Site Scripting vulnerability in openPetra v.2023.02 allows a remote attacker to obtain sensitive information via the serverMServerAdmin.asmx function.



- [https://github.com/Jansen-C-Moreira/CVE-2024-40511](https://github.com/Jansen-C-Moreira/CVE-2024-40511) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40511.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40511.svg)

## CVE-2024-40510
 Cross Site Scripting vulnerability in openPetra v.2023.02 allows a remote attacker to obtain sensitive information via the serverMCommon.asmx function.



- [https://github.com/Jansen-C-Moreira/CVE-2024-40510](https://github.com/Jansen-C-Moreira/CVE-2024-40510) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40510.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40510.svg)

## CVE-2024-40509
 Cross Site Scripting vulnerability in openPetra v.2023.02 allows a remote attacker to obtain sensitive information via the serverMFinDev.asmx function.



- [https://github.com/Jansen-C-Moreira/CVE-2024-40509](https://github.com/Jansen-C-Moreira/CVE-2024-40509) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40509.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40509.svg)

## CVE-2024-40508
 Cross Site Scripting vulnerability in openPetra v.2023.02 allows a remote attacker to obtain sensitive information via the serverMConference.asmx function.



- [https://github.com/Jansen-C-Moreira/CVE-2024-40508](https://github.com/Jansen-C-Moreira/CVE-2024-40508) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40508.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40508.svg)

## CVE-2024-40507
 Cross Site Scripting vulnerability in openPetra v.2023.02 allows a remote attacker to obtain sensitive information via the serverMPersonnel.asmx function.



- [https://github.com/Jansen-C-Moreira/CVE-2024-40507](https://github.com/Jansen-C-Moreira/CVE-2024-40507) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40507.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40507.svg)

## CVE-2024-40506
 Cross Site Scripting vulnerability in openPetra v.2023.02 allows a remote attacker to obtain sensitive information via the serverMHospitality.asmx function.



- [https://github.com/Jansen-C-Moreira/CVE-2024-40506](https://github.com/Jansen-C-Moreira/CVE-2024-40506) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40506.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40506.svg)

## CVE-2024-40498
 SQL Injection vulnerability in PuneethReddyHC Online Shopping sysstem advanced v.1.0 allows an attacker to execute arbitrary code via the register.php



- [https://github.com/Dirac231/CVE-2024-40498](https://github.com/Dirac231/CVE-2024-40498) :  ![starts](https://img.shields.io/github/stars/Dirac231/CVE-2024-40498.svg) ![forks](https://img.shields.io/github/forks/Dirac231/CVE-2024-40498.svg)

## CVE-2024-40492
 Cross Site Scripting vulnerability in Heartbeat Chat v.15.2.1 allows a remote attacker to execute arbitrary code via the setname function.



- [https://github.com/minendie/POC_CVE-2024-40492](https://github.com/minendie/POC_CVE-2024-40492) :  ![starts](https://img.shields.io/github/stars/minendie/POC_CVE-2024-40492.svg) ![forks](https://img.shields.io/github/forks/minendie/POC_CVE-2024-40492.svg)

## CVE-2024-40446
 An issue in forkosh Mime Tex before v.1.77 allows an attacker to execute arbitrary code via a crafted script



- [https://github.com/TaiYou-TW/CVE-2024-40445_CVE-2024-40446](https://github.com/TaiYou-TW/CVE-2024-40445_CVE-2024-40446) :  ![starts](https://img.shields.io/github/stars/TaiYou-TW/CVE-2024-40445_CVE-2024-40446.svg) ![forks](https://img.shields.io/github/forks/TaiYou-TW/CVE-2024-40445_CVE-2024-40446.svg)

## CVE-2024-40445
 A directory traversal vulnerability in forkosh Mime TeX before version 1.77 allows attackers on Windows systems to read or append arbitrary files by manipulating crafted input paths.



- [https://github.com/TaiYou-TW/CVE-2024-40445_CVE-2024-40446](https://github.com/TaiYou-TW/CVE-2024-40445_CVE-2024-40446) :  ![starts](https://img.shields.io/github/stars/TaiYou-TW/CVE-2024-40445_CVE-2024-40446.svg) ![forks](https://img.shields.io/github/forks/TaiYou-TW/CVE-2024-40445_CVE-2024-40446.svg)

## CVE-2024-40443
 SQL Injection vulnerability in Simple Laboratory Management System using PHP and MySQL v.1.0 allows a remote attacker to cause a denial of service via the delete_users function in the Useres.php



- [https://github.com/Yuma-Tsushima07/CVE-2024-40443](https://github.com/Yuma-Tsushima07/CVE-2024-40443) :  ![starts](https://img.shields.io/github/stars/Yuma-Tsushima07/CVE-2024-40443.svg) ![forks](https://img.shields.io/github/forks/Yuma-Tsushima07/CVE-2024-40443.svg)

## CVE-2024-40422
 The snapshot_path parameter in the /api/get-browser-snapshot endpoint in stitionai devika v1 is susceptible to a path traversal attack. An attacker can manipulate the snapshot_path parameter to traverse directories and access sensitive files on the server. This can potentially lead to unauthorized access to critical system files and compromise the confidentiality and integrity of the system.



- [https://github.com/j3r1ch0123/CVE-2024-40422](https://github.com/j3r1ch0123/CVE-2024-40422) :  ![starts](https://img.shields.io/github/stars/j3r1ch0123/CVE-2024-40422.svg) ![forks](https://img.shields.io/github/forks/j3r1ch0123/CVE-2024-40422.svg)

## CVE-2024-40348
 An issue in the component /api/swaggerui/static of Bazaar v1.4.3 allows unauthenticated attackers to execute a directory traversal.



- [https://github.com/bigb0x/CVE-2024-40348](https://github.com/bigb0x/CVE-2024-40348) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-40348.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-40348.svg)

- [https://github.com/NingXin2002/Bazaar_poc](https://github.com/NingXin2002/Bazaar_poc) :  ![starts](https://img.shields.io/github/stars/NingXin2002/Bazaar_poc.svg) ![forks](https://img.shields.io/github/forks/NingXin2002/Bazaar_poc.svg)

## CVE-2024-40324
 A CRLF injection vulnerability in E-Staff v5.1 allows attackers to insert Carriage Return (CR) and Line Feed (LF) characters into input fields, leading to HTTP response splitting and header manipulation.



- [https://github.com/aleksey-vi/CVE-2024-40324](https://github.com/aleksey-vi/CVE-2024-40324) :  ![starts](https://img.shields.io/github/stars/aleksey-vi/CVE-2024-40324.svg) ![forks](https://img.shields.io/github/forks/aleksey-vi/CVE-2024-40324.svg)

## CVE-2024-40318
 An arbitrary file upload vulnerability in Webkul Qloapps v1.6.0.0 allows attackers to execute arbitrary code via uploading a crafted file.



- [https://github.com/3v1lC0d3/RCE-QloApps-CVE-2024-40318](https://github.com/3v1lC0d3/RCE-QloApps-CVE-2024-40318) :  ![starts](https://img.shields.io/github/stars/3v1lC0d3/RCE-QloApps-CVE-2024-40318.svg) ![forks](https://img.shields.io/github/forks/3v1lC0d3/RCE-QloApps-CVE-2024-40318.svg)

## CVE-2024-40119
 Nepstech Wifi Router xpon (terminal) model NTPL-Xpon1GFEVN v.1.0 Firmware V2.0.1 contains a Cross-Site Request Forgery (CSRF) vulnerability in the password change function, which allows remote attackers to change the admin password without the user's consent, leading to a potential account takeover.



- [https://github.com/baroi-ai/nepstech-xpon-router-CVE-2024-40119](https://github.com/baroi-ai/nepstech-xpon-router-CVE-2024-40119) :  ![starts](https://img.shields.io/github/stars/baroi-ai/nepstech-xpon-router-CVE-2024-40119.svg) ![forks](https://img.shields.io/github/forks/baroi-ai/nepstech-xpon-router-CVE-2024-40119.svg)

## CVE-2024-40111
 A persistent (stored) cross-site scripting (XSS) vulnerability has been identified in Automad 2.0.0-alpha.4. This vulnerability enables an attacker to inject malicious JavaScript code into the template body. The injected code is stored within the flat file CMS and is executed in the browser of any user visiting the forum.



- [https://github.com/theexploiters/CVE-2024-40111-Exploit](https://github.com/theexploiters/CVE-2024-40111-Exploit) :  ![starts](https://img.shields.io/github/stars/theexploiters/CVE-2024-40111-Exploit.svg) ![forks](https://img.shields.io/github/forks/theexploiters/CVE-2024-40111-Exploit.svg)

## CVE-2024-40110
 Sourcecodester Poultry Farm Management System v1.0 contains an Unauthenticated Remote Code Execution (RCE) vulnerability via the productimage parameter at /farm/product.php.



- [https://github.com/thiagosmith/CVE-2024-40110](https://github.com/thiagosmith/CVE-2024-40110) :  ![starts](https://img.shields.io/github/stars/thiagosmith/CVE-2024-40110.svg) ![forks](https://img.shields.io/github/forks/thiagosmith/CVE-2024-40110.svg)

- [https://github.com/Abdurahmon3236/CVE-2024-40110](https://github.com/Abdurahmon3236/CVE-2024-40110) :  ![starts](https://img.shields.io/github/stars/Abdurahmon3236/CVE-2024-40110.svg) ![forks](https://img.shields.io/github/forks/Abdurahmon3236/CVE-2024-40110.svg)

## CVE-2024-39943
 rejetto HFS (aka HTTP File Server) 3 before 0.52.10 on Linux, UNIX, and macOS allows OS command execution by remote authenticated users (if they have Upload permissions). This occurs because a shell is used to execute df (i.e., with execSync instead of spawnSync in child_process in Node.js).



- [https://github.com/truonghuuphuc/CVE-2024-39943-Poc](https://github.com/truonghuuphuc/CVE-2024-39943-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-39943-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-39943-Poc.svg)

- [https://github.com/tequilasunsh1ne/CVE_2024_39943](https://github.com/tequilasunsh1ne/CVE_2024_39943) :  ![starts](https://img.shields.io/github/stars/tequilasunsh1ne/CVE_2024_39943.svg) ![forks](https://img.shields.io/github/forks/tequilasunsh1ne/CVE_2024_39943.svg)

- [https://github.com/JenmrR/Node.js-CVE-2024-39943](https://github.com/JenmrR/Node.js-CVE-2024-39943) :  ![starts](https://img.shields.io/github/stars/JenmrR/Node.js-CVE-2024-39943.svg) ![forks](https://img.shields.io/github/forks/JenmrR/Node.js-CVE-2024-39943.svg)

## CVE-2024-39930
 The built-in SSH server of Gogs through 0.13.0 allows argument injection in internal/ssh/ssh.go, leading to remote code execution. Authenticated attackers can exploit this by opening an SSH connection and sending a malicious --split-string env request if the built-in SSH server is activated. Windows installations are unaffected.



- [https://github.com/alexander47777/-CVE-2024-39930](https://github.com/alexander47777/-CVE-2024-39930) :  ![starts](https://img.shields.io/github/stars/alexander47777/-CVE-2024-39930.svg) ![forks](https://img.shields.io/github/forks/alexander47777/-CVE-2024-39930.svg)

- [https://github.com/theMcSam/CVE-2024-39930-PoC](https://github.com/theMcSam/CVE-2024-39930-PoC) :  ![starts](https://img.shields.io/github/stars/theMcSam/CVE-2024-39930-PoC.svg) ![forks](https://img.shields.io/github/forks/theMcSam/CVE-2024-39930-PoC.svg)

## CVE-2024-39929
 Exim through 4.97.1 misparses a multiline RFC 2231 header filename, and thus remote attackers can bypass a $mime_filename extension-blocking protection mechanism, and potentially deliver executable attachments to the mailboxes of end users.



- [https://github.com/michael-david-fry/CVE-2024-39929](https://github.com/michael-david-fry/CVE-2024-39929) :  ![starts](https://img.shields.io/github/stars/michael-david-fry/CVE-2024-39929.svg) ![forks](https://img.shields.io/github/forks/michael-david-fry/CVE-2024-39929.svg)

- [https://github.com/rxerium/CVE-2024-39929](https://github.com/rxerium/CVE-2024-39929) :  ![starts](https://img.shields.io/github/stars/rxerium/CVE-2024-39929.svg) ![forks](https://img.shields.io/github/forks/rxerium/CVE-2024-39929.svg)

## CVE-2024-39924
 An issue was discovered in Vaultwarden (formerly Bitwarden_RS) 1.30.3. A vulnerability has been identified in the authentication and authorization process of the endpoint responsible for altering the metadata of an emergency access. It permits an attacker with granted emergency access to escalate their privileges by changing the access level and modifying the wait time. Consequently, the attacker can gain full control over the vault (when only intended to have read access) while bypassing the necessary wait period.



- [https://github.com/l4rm4nd/PoC-CVE-2024-39924](https://github.com/l4rm4nd/PoC-CVE-2024-39924) :  ![starts](https://img.shields.io/github/stars/l4rm4nd/PoC-CVE-2024-39924.svg) ![forks](https://img.shields.io/github/forks/l4rm4nd/PoC-CVE-2024-39924.svg)

## CVE-2024-39914
 FOG is a cloning/imaging/rescue suite/inventory management system. Prior to 1.5.10.34, packages/web/lib/fog/reportmaker.class.php in FOG was affected by a command injection via the filename parameter to /fog/management/export.php. This vulnerability is fixed in 1.5.10.34.



- [https://github.com/9874621368/FOG-Project](https://github.com/9874621368/FOG-Project) :  ![starts](https://img.shields.io/github/stars/9874621368/FOG-Project.svg) ![forks](https://img.shields.io/github/forks/9874621368/FOG-Project.svg)

## CVE-2024-39908
  REXML is an XML toolkit for Ruby. The REXML gem before 3.3.1 has some DoS vulnerabilities when it parses an XML that has many specific characters such as ``, `0` and `%`. If you need to parse untrusted XMLs, you many be impacted to these vulnerabilities. The REXML gem 3.3.2 or later include the patches to fix these vulnerabilities. Users are advised to upgrade. Users unable to upgrade should avoid parsing untrusted XML strings.



- [https://github.com/SpiralBL0CK/CVE-2024-39908](https://github.com/SpiralBL0CK/CVE-2024-39908) :  ![starts](https://img.shields.io/github/stars/SpiralBL0CK/CVE-2024-39908.svg) ![forks](https://img.shields.io/github/forks/SpiralBL0CK/CVE-2024-39908.svg)

## CVE-2024-39844
 In ZNC before 1.9.1, remote code execution can occur in modtcl via a KICK.



- [https://github.com/ph1ns/CVE-2024-39844](https://github.com/ph1ns/CVE-2024-39844) :  ![starts](https://img.shields.io/github/stars/ph1ns/CVE-2024-39844.svg) ![forks](https://img.shields.io/github/forks/ph1ns/CVE-2024-39844.svg)

## CVE-2024-39722
 An issue was discovered in Ollama before 0.1.46. It exposes which files exist on the server on which it is deployed via path traversal in the api/push route.



- [https://github.com/srcx404/CVE-2024-39722](https://github.com/srcx404/CVE-2024-39722) :  ![starts](https://img.shields.io/github/stars/srcx404/CVE-2024-39722.svg) ![forks](https://img.shields.io/github/forks/srcx404/CVE-2024-39722.svg)

## CVE-2024-39719
 An issue was discovered in Ollama through 0.3.14. File existence disclosure can occur via api/create. When calling the CreateModel route with a path parameter that does not exist, it reflects the "File does not exist" error message to the attacker, providing a primitive for file existence on the server.



- [https://github.com/srcx404/CVE-2024-39719](https://github.com/srcx404/CVE-2024-39719) :  ![starts](https://img.shields.io/github/stars/srcx404/CVE-2024-39719.svg) ![forks](https://img.shields.io/github/forks/srcx404/CVE-2024-39719.svg)

## CVE-2024-39700
 JupyterLab extension template is a  `copier` template for JupyterLab extensions. Repositories created using this template with `test` option include `update-integration-tests.yml` workflow which has an RCE vulnerability. Extension authors hosting their code on GitHub are urged to upgrade the template to the latest version. Users who made changes to `update-integration-tests.yml`, accept overwriting of this file and re-apply your changes later. Users may wish to temporarily disable GitHub Actions while working on the upgrade. We recommend rebasing all open pull requests from untrusted users as actions may run using the version from the `main` branch at the time when the pull request was created. Users who are upgrading from template version prior to 4.3.0 may wish to leave out proposed changes to the release workflow for now as it requires additional configuration.



- [https://github.com/LOURC0D3/CVE-2024-39700-PoC](https://github.com/LOURC0D3/CVE-2024-39700-PoC) :  ![starts](https://img.shields.io/github/stars/LOURC0D3/CVE-2024-39700-PoC.svg) ![forks](https://img.shields.io/github/forks/LOURC0D3/CVE-2024-39700-PoC.svg)

## CVE-2024-39689
 Certifi is a curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. Certifi starting in 2021.5.30 and prior to 2024.7.4 recognized root certificates from `GLOBALTRUST`. Certifi 2024.7.04 removes root certificates from `GLOBALTRUST` from the root store. These are in the process of being removed from Mozilla's trust store. `GLOBALTRUST`'s root certificates are being removed pursuant to an investigation which identified "long-running and unresolved compliance issues."



- [https://github.com/roy-aladin/InfraTest](https://github.com/roy-aladin/InfraTest) :  ![starts](https://img.shields.io/github/stars/roy-aladin/InfraTest.svg) ![forks](https://img.shields.io/github/forks/roy-aladin/InfraTest.svg)

## CVE-2024-39614
 An issue was discovered in Django 5.0 before 5.0.7 and 4.2 before 4.2.14. get_supported_language_variant() was subject to a potential denial-of-service attack when used with very long strings containing specific characters.



- [https://github.com/Abdurahmon3236/-CVE-2024-39614](https://github.com/Abdurahmon3236/-CVE-2024-39614) :  ![starts](https://img.shields.io/github/stars/Abdurahmon3236/-CVE-2024-39614.svg) ![forks](https://img.shields.io/github/forks/Abdurahmon3236/-CVE-2024-39614.svg)

## CVE-2024-39345
 AdTran 834-5 HDC17600021F1 (SmartOS 11.1.1.1) devices enable the SSH service by default and have a hidden, undocumented, hard-coded support account whose password is based on the devices MAC address. All of the devices internet interfaces share a similar MAC address that only varies in their final octet. This allows network-adjacent attackers to derive the support user's SSH password by decrementing the final octet of the connected gateway address or via the BSSID. An attacker can then execute arbitrary OS commands with root-level privileges. NOTE: The vendor states that there is no intended functionality allowing an attacker to execute arbitrary OS Commands with root-level privileges. The vendor also states that this issue was fixed in SmartOS 12.5.5.1.



- [https://github.com/actuator/BSIDES-Security-Las-Vegas-2024](https://github.com/actuator/BSIDES-Security-Las-Vegas-2024) :  ![starts](https://img.shields.io/github/stars/actuator/BSIDES-Security-Las-Vegas-2024.svg) ![forks](https://img.shields.io/github/forks/actuator/BSIDES-Security-Las-Vegas-2024.svg)

## CVE-2024-39306
 ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: CVE-2024-39304. Reason: This candidate is a duplicate of CVE-2024-39304. Notes: All CVE users should reference CVE-2024-39304 instead of this candidate. This CVE was issued to a vulnerability that is dependent on CVE-2024-39304. According to rule 4.2.15 of the CVE CNA rules, "CNAs MUST NOT assign a different CVE ID to a Vulnerability that is fully interdependent with another Vulnerability. The Vulnerabilities are effectively the same single Vulnerability and MUST use one CVE ID."



- [https://github.com/apena-ba/CVE-2024-39306](https://github.com/apena-ba/CVE-2024-39306) :  ![starts](https://img.shields.io/github/stars/apena-ba/CVE-2024-39306.svg) ![forks](https://img.shields.io/github/forks/apena-ba/CVE-2024-39306.svg)

## CVE-2024-39304
 ChurchCRM is an open-source church management system. Versions of the application prior to 5.9.2 are vulnerable to an authenticated SQL injection due to an improper sanitization of user input. Authentication is required, but no elevated privileges are necessary. This allows attackers to inject SQL statements directly into the database query due to inadequate sanitization of the EID parameter in in a GET request to `/GetText.php`. Version 5.9.2 patches the issue.



- [https://github.com/apena-ba/CVE-2024-39304](https://github.com/apena-ba/CVE-2024-39304) :  ![starts](https://img.shields.io/github/stars/apena-ba/CVE-2024-39304.svg) ![forks](https://img.shields.io/github/forks/apena-ba/CVE-2024-39304.svg)

## CVE-2024-39250
 EfroTech Timetrax v8.3 was discovered to contain an unauthenticated SQL injection vulnerability via the q parameter in the search web interface.



- [https://github.com/efrann/CVE-2024-39250](https://github.com/efrann/CVE-2024-39250) :  ![starts](https://img.shields.io/github/stars/efrann/CVE-2024-39250.svg) ![forks](https://img.shields.io/github/forks/efrann/CVE-2024-39250.svg)

## CVE-2024-39248
 A cross-site scripting (XSS) vulnerability in SimpCMS v0.1 allows attackers to execute arbitrary web scripts or HTML via a crafted payload injected into the Title field at /admin.php.



- [https://github.com/jasonthename/CVE-2024-39248](https://github.com/jasonthename/CVE-2024-39248) :  ![starts](https://img.shields.io/github/stars/jasonthename/CVE-2024-39248.svg) ![forks](https://img.shields.io/github/forks/jasonthename/CVE-2024-39248.svg)

## CVE-2024-39211
 Kaiten 57.128.8 allows remote attackers to enumerate user accounts via a crafted POST request, because a login response contains a user_email field only if the user account exists.



- [https://github.com/artemy-ccrsky/CVE-2024-39211](https://github.com/artemy-ccrsky/CVE-2024-39211) :  ![starts](https://img.shields.io/github/stars/artemy-ccrsky/CVE-2024-39211.svg) ![forks](https://img.shields.io/github/forks/artemy-ccrsky/CVE-2024-39211.svg)

## CVE-2024-39210
 Best House Rental Management System v1.0 was discovered to contain an arbitrary file read vulnerability via the Page parameter at index.php. This vulnerability allows attackers to read arbitrary PHP files and access other sensitive information within the application.



- [https://github.com/KRookieSec/CVE-2024-39210](https://github.com/KRookieSec/CVE-2024-39210) :  ![starts](https://img.shields.io/github/stars/KRookieSec/CVE-2024-39210.svg) ![forks](https://img.shields.io/github/forks/KRookieSec/CVE-2024-39210.svg)

## CVE-2024-39203
 A cross-site scripting (XSS) vulnerability in the Backend Theme Management module of Z-BlogPHP v1.7.3 allows attackers to execute arbitrary web scripts or HTML via a crafted payload.



- [https://github.com/5r1an/CVE-2024-39203](https://github.com/5r1an/CVE-2024-39203) :  ![starts](https://img.shields.io/github/stars/5r1an/CVE-2024-39203.svg) ![forks](https://img.shields.io/github/forks/5r1an/CVE-2024-39203.svg)

## CVE-2024-39123
 In janeczku Calibre-Web 0.6.0 to 0.6.21, the edit_book_comments function is vulnerable to Cross Site Scripting (XSS) due to improper sanitization performed by the clean_string function. The vulnerability arises from the way the clean_string function handles HTML sanitization.



- [https://github.com/theexploiters/CVE-2024-39123-Exploit](https://github.com/theexploiters/CVE-2024-39123-Exploit) :  ![starts](https://img.shields.io/github/stars/theexploiters/CVE-2024-39123-Exploit.svg) ![forks](https://img.shields.io/github/forks/theexploiters/CVE-2024-39123-Exploit.svg)

## CVE-2024-39119
 idccms v1.35 was discovered to contain a Cross-Site Request Forgery (CSRF) via admin/info_deal.php?mudi=rev&nohrefStr=close.



- [https://github.com/phtcloud-dev/CVE-2024-39199](https://github.com/phtcloud-dev/CVE-2024-39199) :  ![starts](https://img.shields.io/github/stars/phtcloud-dev/CVE-2024-39199.svg) ![forks](https://img.shields.io/github/forks/phtcloud-dev/CVE-2024-39199.svg)

## CVE-2024-39090
 The PHPGurukul Online Shopping Portal Project version 2.0 contains a vulnerability that allows Cross-Site Request Forgery (CSRF) to lead to Stored Cross-Site Scripting (XSS). An attacker can exploit this vulnerability to execute arbitrary JavaScript code in the context of a user's session, potentially leading to account takeover.



- [https://github.com/ghostwirez/CVE-2024-39090-PoC](https://github.com/ghostwirez/CVE-2024-39090-PoC) :  ![starts](https://img.shields.io/github/stars/ghostwirez/CVE-2024-39090-PoC.svg) ![forks](https://img.shields.io/github/forks/ghostwirez/CVE-2024-39090-PoC.svg)

## CVE-2024-39081
 An issue in SMART TYRE CAR & BIKE v4.2.0 allows attackers to perform a man-in-the-middle attack via Bluetooth communications.



- [https://github.com/Amirasaiyad/BLE-TPMS](https://github.com/Amirasaiyad/BLE-TPMS) :  ![starts](https://img.shields.io/github/stars/Amirasaiyad/BLE-TPMS.svg) ![forks](https://img.shields.io/github/forks/Amirasaiyad/BLE-TPMS.svg)

## CVE-2024-39069
 An issue in ifood Order Manager v3.35.5 'Gestor de Peddios.exe' allows attackers to execute arbitrary code via a DLL hijacking attack.



- [https://github.com/AungSoePaing/CVE-2024-39069](https://github.com/AungSoePaing/CVE-2024-39069) :  ![starts](https://img.shields.io/github/stars/AungSoePaing/CVE-2024-39069.svg) ![forks](https://img.shields.io/github/forks/AungSoePaing/CVE-2024-39069.svg)

## CVE-2024-39031
 In Silverpeas Core = 6.3.5, in Mes Agendas, a user can create new events and add them to their calendar. Additionally, users can invite others from the same domain, including administrators, to these events. A standard user can inject an XSS payload into the "Titre" and "Description" fields when creating an event and then add the administrator or any user to the event. When the invited user (victim) views their own profile, the payload will be executed on their side, even if they do not click on the event.



- [https://github.com/toneemarqus/CVE-2024-39031](https://github.com/toneemarqus/CVE-2024-39031) :  ![starts](https://img.shields.io/github/stars/toneemarqus/CVE-2024-39031.svg) ![forks](https://img.shields.io/github/forks/toneemarqus/CVE-2024-39031.svg)

## CVE-2024-38998
 DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: none. Reason: This candidate was withdrawn by its CNA. Further investigation showed that it was not a security issue. Notes: none.



- [https://github.com/z3ldr1/PP_CVE-2024-38998](https://github.com/z3ldr1/PP_CVE-2024-38998) :  ![starts](https://img.shields.io/github/stars/z3ldr1/PP_CVE-2024-38998.svg) ![forks](https://img.shields.io/github/forks/z3ldr1/PP_CVE-2024-38998.svg)

- [https://github.com/cesarbtakeda/PP_CVE-2024-38998](https://github.com/cesarbtakeda/PP_CVE-2024-38998) :  ![starts](https://img.shields.io/github/stars/cesarbtakeda/PP_CVE-2024-38998.svg) ![forks](https://img.shields.io/github/forks/cesarbtakeda/PP_CVE-2024-38998.svg)

## CVE-2024-38856
 Incorrect Authorization vulnerability in Apache OFBiz.

This issue affects Apache OFBiz: through 18.12.14.

Users are recommended to upgrade to version 18.12.15, which fixes the issue.

Unauthenticated endpoints could allow execution of screen rendering code of screens if some preconditions are met (such as when the screen definitions don't explicitly check user's permissions because they rely on the configuration of their endpoints).



- [https://github.com/securelayer7/CVE-2024-38856_Scanner](https://github.com/securelayer7/CVE-2024-38856_Scanner) :  ![starts](https://img.shields.io/github/stars/securelayer7/CVE-2024-38856_Scanner.svg) ![forks](https://img.shields.io/github/forks/securelayer7/CVE-2024-38856_Scanner.svg)

- [https://github.com/XiaomingX/cve-2024-38856-poc](https://github.com/XiaomingX/cve-2024-38856-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-38856-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-38856-poc.svg)

- [https://github.com/ThatNotEasy/CVE-2024-38856](https://github.com/ThatNotEasy/CVE-2024-38856) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2024-38856.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2024-38856.svg)

- [https://github.com/FakesiteSecurity/CVE-2024-38856_Scen](https://github.com/FakesiteSecurity/CVE-2024-38856_Scen) :  ![starts](https://img.shields.io/github/stars/FakesiteSecurity/CVE-2024-38856_Scen.svg) ![forks](https://img.shields.io/github/forks/FakesiteSecurity/CVE-2024-38856_Scen.svg)

- [https://github.com/guinea-offensive-security/Ofbiz-RCE](https://github.com/guinea-offensive-security/Ofbiz-RCE) :  ![starts](https://img.shields.io/github/stars/guinea-offensive-security/Ofbiz-RCE.svg) ![forks](https://img.shields.io/github/forks/guinea-offensive-security/Ofbiz-RCE.svg)

## CVE-2024-38828
 Spring MVC controller methods with an @RequestBody byte[] method parameter are vulnerable to a DoS attack.



- [https://github.com/funcid/CVE-2024-38828](https://github.com/funcid/CVE-2024-38828) :  ![starts](https://img.shields.io/github/stars/funcid/CVE-2024-38828.svg) ![forks](https://img.shields.io/github/forks/funcid/CVE-2024-38828.svg)

- [https://github.com/First-Roman/sprig-mvc-demo-patch](https://github.com/First-Roman/sprig-mvc-demo-patch) :  ![starts](https://img.shields.io/github/stars/First-Roman/sprig-mvc-demo-patch.svg) ![forks](https://img.shields.io/github/forks/First-Roman/sprig-mvc-demo-patch.svg)

- [https://github.com/topilov/axiom-jdk](https://github.com/topilov/axiom-jdk) :  ![starts](https://img.shields.io/github/stars/topilov/axiom-jdk.svg) ![forks](https://img.shields.io/github/forks/topilov/axiom-jdk.svg)

## CVE-2024-38819
 Applications serving static resources through the functional web frameworks WebMvc.fn or WebFlux.fn are vulnerable to path traversal attacks. An attacker can craft malicious HTTP requests and obtain any file on the file system that is also accessible to the process in which the Spring application is running.



- [https://github.com/masa42/CVE-2024-38819-POC](https://github.com/masa42/CVE-2024-38819-POC) :  ![starts](https://img.shields.io/github/stars/masa42/CVE-2024-38819-POC.svg) ![forks](https://img.shields.io/github/forks/masa42/CVE-2024-38819-POC.svg)

- [https://github.com/GhostS3c/CVE-2024-38819](https://github.com/GhostS3c/CVE-2024-38819) :  ![starts](https://img.shields.io/github/stars/GhostS3c/CVE-2024-38819.svg) ![forks](https://img.shields.io/github/forks/GhostS3c/CVE-2024-38819.svg)

- [https://github.com/jaloon/spring-webmvc5](https://github.com/jaloon/spring-webmvc5) :  ![starts](https://img.shields.io/github/stars/jaloon/spring-webmvc5.svg) ![forks](https://img.shields.io/github/forks/jaloon/spring-webmvc5.svg)

## CVE-2024-38816
 Applications serving static resources through the functional web frameworks WebMvc.fn or WebFlux.fn are vulnerable to path traversal attacks. An attacker can craft malicious HTTP requests and obtain any file on the file system that is also accessible to the process in which the Spring application is running.

Specifically, an application is vulnerable when both of the following are true:

  *  the web application uses RouterFunctions to serve static resources
  *  resource handling is explicitly configured with a FileSystemResource location


However, malicious requests are blocked and rejected when any of the following is true:

  *  the  Spring Security HTTP Firewall https://docs.spring.io/spring-security/reference/servlet/exploits/firewall.html  is in use
  *  the application runs on Tomcat or Jetty



- [https://github.com/Anthony1078/App-vulnerable](https://github.com/Anthony1078/App-vulnerable) :  ![starts](https://img.shields.io/github/stars/Anthony1078/App-vulnerable.svg) ![forks](https://img.shields.io/github/forks/Anthony1078/App-vulnerable.svg)

- [https://github.com/wdragondragon/spring-framework](https://github.com/wdragondragon/spring-framework) :  ![starts](https://img.shields.io/github/stars/wdragondragon/spring-framework.svg) ![forks](https://img.shields.io/github/forks/wdragondragon/spring-framework.svg)

- [https://github.com/jaloon/spring-webmvc5](https://github.com/jaloon/spring-webmvc5) :  ![starts](https://img.shields.io/github/stars/jaloon/spring-webmvc5.svg) ![forks](https://img.shields.io/github/forks/jaloon/spring-webmvc5.svg)

## CVE-2024-38537
 Fides is an open-source privacy engineering platform. `fides.js`, a client-side script used to interact with the consent management features of Fides, used the `polyfill.io` domain in a very limited edge case, when it detected a legacy browser such as IE11 that did not support the fetch standard. Therefore it was possible for users of legacy, pre-2017 browsers who navigate to a page serving `fides.js` to download and execute malicious scripts from the `polyfill.io` domain when the domain was compromised and serving malware. No exploitation of `fides.js` via `polyfill.io` has been identified as of time of publication.

The vulnerability has been patched in Fides version `2.39.1`. Users are advised to upgrade to this version or later to secure their systems against this threat. On Thursday, June 27, 2024, Cloudflare and Namecheap intervened at a domain level to ensure `polyfill.io` and its subdomains could not resolve to the compromised service, rendering this vulnerability unexploitable. Prior to the domain level intervention, there were no server-side workarounds and the confidentiality, integrity, and availability impacts of this vulnerability were high. Clients could ensure they were not affected by using a modern browser that supported the fetch standard.



- [https://github.com/Havoc10-sw/Detect_polyfill_CVE-2024-38537-](https://github.com/Havoc10-sw/Detect_polyfill_CVE-2024-38537-) :  ![starts](https://img.shields.io/github/stars/Havoc10-sw/Detect_polyfill_CVE-2024-38537-.svg) ![forks](https://img.shields.io/github/forks/Havoc10-sw/Detect_polyfill_CVE-2024-38537-.svg)

## CVE-2024-38475
 Improper escaping of output in mod_rewrite in Apache HTTP Server 2.4.59 and earlier allows an attacker to map URLs to filesystem locations that are permitted to be served by the server but are not intentionally/directly reachable by any URL, resulting in code execution or source code disclosure. 

Substitutions in server context that use a backreferences or variables as the first segment of the substitution are affected.  Some unsafe RewiteRules will be broken by this change and the rewrite flag "UnsafePrefixStat" can be used to opt back in once ensuring the substitution is appropriately constrained.



- [https://github.com/soltanali0/CVE-2024-38475](https://github.com/soltanali0/CVE-2024-38475) :  ![starts](https://img.shields.io/github/stars/soltanali0/CVE-2024-38475.svg) ![forks](https://img.shields.io/github/forks/soltanali0/CVE-2024-38475.svg)

- [https://github.com/syaifulandy/CVE-2024-38475](https://github.com/syaifulandy/CVE-2024-38475) :  ![starts](https://img.shields.io/github/stars/syaifulandy/CVE-2024-38475.svg) ![forks](https://img.shields.io/github/forks/syaifulandy/CVE-2024-38475.svg)

- [https://github.com/abrewer251/CVE-2024-38475_SonicBoom_Apache_URL_Traversal_PoC](https://github.com/abrewer251/CVE-2024-38475_SonicBoom_Apache_URL_Traversal_PoC) :  ![starts](https://img.shields.io/github/stars/abrewer251/CVE-2024-38475_SonicBoom_Apache_URL_Traversal_PoC.svg) ![forks](https://img.shields.io/github/forks/abrewer251/CVE-2024-38475_SonicBoom_Apache_URL_Traversal_PoC.svg)

## CVE-2024-38473
 Encoding problem in mod_proxy in Apache HTTP Server 2.4.59 and earlier allows request URLs with incorrect encoding to be sent to backend services, potentially bypassing authentication via crafted requests.
Users are recommended to upgrade to version 2.4.60, which fixes this issue.



- [https://github.com/Abdurahmon3236/CVE-2024-38473](https://github.com/Abdurahmon3236/CVE-2024-38473) :  ![starts](https://img.shields.io/github/stars/Abdurahmon3236/CVE-2024-38473.svg) ![forks](https://img.shields.io/github/forks/Abdurahmon3236/CVE-2024-38473.svg)

## CVE-2024-38472
 SSRF in Apache HTTP Server on Windows allows to potentially leak NTLM hashes to a malicious server via SSRF and malicious requests or content 
Users are recommended to upgrade to version 2.4.60 which fixes this issue.  Note: Existing configurations that access UNC paths will have to configure new directive "UNCList" to allow access during request processing.



- [https://github.com/Abdurahmon3236/CVE-2024-38472](https://github.com/Abdurahmon3236/CVE-2024-38472) :  ![starts](https://img.shields.io/github/stars/Abdurahmon3236/CVE-2024-38472.svg) ![forks](https://img.shields.io/github/forks/Abdurahmon3236/CVE-2024-38472.svg)

## CVE-2024-38396
 An issue was discovered in iTerm2 3.5.x before 3.5.2. Unfiltered use of an escape sequence to report a window title, in combination with the built-in tmux integration feature (enabled by default), allows an attacker to inject arbitrary code into the terminal, a different vulnerability than CVE-2024-38395.



- [https://github.com/vin01/poc-cve-2024-38396](https://github.com/vin01/poc-cve-2024-38396) :  ![starts](https://img.shields.io/github/stars/vin01/poc-cve-2024-38396.svg) ![forks](https://img.shields.io/github/forks/vin01/poc-cve-2024-38396.svg)

## CVE-2024-38395
 In iTerm2 before 3.5.2, the "Terminal may report window title" setting is not honored, and thus remote code execution might occur but "is not trivially exploitable."



- [https://github.com/vin01/poc-cve-2024-38396](https://github.com/vin01/poc-cve-2024-38396) :  ![starts](https://img.shields.io/github/stars/vin01/poc-cve-2024-38396.svg) ![forks](https://img.shields.io/github/forks/vin01/poc-cve-2024-38396.svg)

## CVE-2024-38366
 trunk.cocoapods.org is the authentication server for the CoacoaPods dependency manager. The part of trunk which verifies whether a user has a real email address on signup used a rfc-822 library which executes a shell command to validate the email domain MX records validity. It works via an DNS MX. This lookup could be manipulated to also execute a command on the trunk server, effectively giving root access to the server and the infrastructure. This issue was patched server-side with commit 001cc3a430e75a16307f5fd6cdff1363ad2f40f3 in September 2023. This RCE triggered a full user-session reset, as an attacker could have used this method to write to any Podspec in trunk.



- [https://github.com/ReeFSpeK/CocoaPods-RCE_CVE-2024-38366](https://github.com/ReeFSpeK/CocoaPods-RCE_CVE-2024-38366) :  ![starts](https://img.shields.io/github/stars/ReeFSpeK/CocoaPods-RCE_CVE-2024-38366.svg) ![forks](https://img.shields.io/github/forks/ReeFSpeK/CocoaPods-RCE_CVE-2024-38366.svg)

## CVE-2024-38193
 Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability



- [https://github.com/killvxk/CVE-2024-38193-Nephster](https://github.com/killvxk/CVE-2024-38193-Nephster) :  ![starts](https://img.shields.io/github/stars/killvxk/CVE-2024-38193-Nephster.svg) ![forks](https://img.shields.io/github/forks/killvxk/CVE-2024-38193-Nephster.svg)

## CVE-2024-38112
 Windows MSHTML Platform Spoofing Vulnerability



- [https://github.com/BunBunCodes/CPSC253_CybersecurityFinalProjectReports](https://github.com/BunBunCodes/CPSC253_CybersecurityFinalProjectReports) :  ![starts](https://img.shields.io/github/stars/BunBunCodes/CPSC253_CybersecurityFinalProjectReports.svg) ![forks](https://img.shields.io/github/forks/BunBunCodes/CPSC253_CybersecurityFinalProjectReports.svg)

## CVE-2024-38077
 Windows Remote Desktop Licensing Service Remote Code Execution Vulnerability



- [https://github.com/qi4L/CVE-2024-38077](https://github.com/qi4L/CVE-2024-38077) :  ![starts](https://img.shields.io/github/stars/qi4L/CVE-2024-38077.svg) ![forks](https://img.shields.io/github/forks/qi4L/CVE-2024-38077.svg)

- [https://github.com/murphysecurity/RDL-detect](https://github.com/murphysecurity/RDL-detect) :  ![starts](https://img.shields.io/github/stars/murphysecurity/RDL-detect.svg) ![forks](https://img.shields.io/github/forks/murphysecurity/RDL-detect.svg)

- [https://github.com/SecStarBot/CVE-2024-38077-POC](https://github.com/SecStarBot/CVE-2024-38077-POC) :  ![starts](https://img.shields.io/github/stars/SecStarBot/CVE-2024-38077-POC.svg) ![forks](https://img.shields.io/github/forks/SecStarBot/CVE-2024-38077-POC.svg)

- [https://github.com/zhuxi1965/CVE-2024-38077-RDLCheck](https://github.com/zhuxi1965/CVE-2024-38077-RDLCheck) :  ![starts](https://img.shields.io/github/stars/zhuxi1965/CVE-2024-38077-RDLCheck.svg) ![forks](https://img.shields.io/github/forks/zhuxi1965/CVE-2024-38077-RDLCheck.svg)

- [https://github.com/Wlibang/CVE-2024-38077](https://github.com/Wlibang/CVE-2024-38077) :  ![starts](https://img.shields.io/github/stars/Wlibang/CVE-2024-38077.svg) ![forks](https://img.shields.io/github/forks/Wlibang/CVE-2024-38077.svg)

- [https://github.com/psl-b/CVE-2024-38077-check](https://github.com/psl-b/CVE-2024-38077-check) :  ![starts](https://img.shields.io/github/stars/psl-b/CVE-2024-38077-check.svg) ![forks](https://img.shields.io/github/forks/psl-b/CVE-2024-38077-check.svg)

- [https://github.com/atlassion/CVE-2024-38077-check](https://github.com/atlassion/CVE-2024-38077-check) :  ![starts](https://img.shields.io/github/stars/atlassion/CVE-2024-38077-check.svg) ![forks](https://img.shields.io/github/forks/atlassion/CVE-2024-38077-check.svg)

- [https://github.com/Sec-Link/CVE-2024-38077](https://github.com/Sec-Link/CVE-2024-38077) :  ![starts](https://img.shields.io/github/stars/Sec-Link/CVE-2024-38077.svg) ![forks](https://img.shields.io/github/forks/Sec-Link/CVE-2024-38077.svg)

- [https://github.com/lworld0x00/CVE-2024-38077-notes](https://github.com/lworld0x00/CVE-2024-38077-notes) :  ![starts](https://img.shields.io/github/stars/lworld0x00/CVE-2024-38077-notes.svg) ![forks](https://img.shields.io/github/forks/lworld0x00/CVE-2024-38077-notes.svg)

## CVE-2024-38063
 Windows TCP/IP Remote Code Execution Vulnerability



- [https://github.com/Dragkob/CVE-2024-38063](https://github.com/Dragkob/CVE-2024-38063) :  ![starts](https://img.shields.io/github/stars/Dragkob/CVE-2024-38063.svg) ![forks](https://img.shields.io/github/forks/Dragkob/CVE-2024-38063.svg)

- [https://github.com/Skac44/CVE-2024-38063](https://github.com/Skac44/CVE-2024-38063) :  ![starts](https://img.shields.io/github/stars/Skac44/CVE-2024-38063.svg) ![forks](https://img.shields.io/github/forks/Skac44/CVE-2024-38063.svg)

- [https://github.com/fredagsguf/Windows-CVE-2024-38063](https://github.com/fredagsguf/Windows-CVE-2024-38063) :  ![starts](https://img.shields.io/github/stars/fredagsguf/Windows-CVE-2024-38063.svg) ![forks](https://img.shields.io/github/forks/fredagsguf/Windows-CVE-2024-38063.svg)

- [https://github.com/AliHj98/cve-2024-38063-Anonyvader](https://github.com/AliHj98/cve-2024-38063-Anonyvader) :  ![starts](https://img.shields.io/github/stars/AliHj98/cve-2024-38063-Anonyvader.svg) ![forks](https://img.shields.io/github/forks/AliHj98/cve-2024-38063-Anonyvader.svg)

## CVE-2024-37888
 The Open Link is a CKEditor plugin, extending context menu with a possibility to open link in a new tab. The vulnerability allowed to execute JavaScript code by abusing link href attribute. It affects all users using the Open Link plugin at version  **1.0.5**.



- [https://github.com/7Ragnarok7/CVE-2024-37888](https://github.com/7Ragnarok7/CVE-2024-37888) :  ![starts](https://img.shields.io/github/stars/7Ragnarok7/CVE-2024-37888.svg) ![forks](https://img.shields.io/github/forks/7Ragnarok7/CVE-2024-37888.svg)

## CVE-2024-37843
 Craft CMS up to v3.7.31 was discovered to contain a SQL injection vulnerability via the GraphQL API endpoint.



- [https://github.com/gsmith257-cyber/CVE-2024-37843-POC](https://github.com/gsmith257-cyber/CVE-2024-37843-POC) :  ![starts](https://img.shields.io/github/stars/gsmith257-cyber/CVE-2024-37843-POC.svg) ![forks](https://img.shields.io/github/forks/gsmith257-cyber/CVE-2024-37843-POC.svg)

## CVE-2024-37791
 DuxCMS3 v3.1.3 was discovered to contain a SQL injection vulnerability via the keyword parameter at /article/Content/index?class_id.



- [https://github.com/czheisenberg/CVE-2024-37791](https://github.com/czheisenberg/CVE-2024-37791) :  ![starts](https://img.shields.io/github/stars/czheisenberg/CVE-2024-37791.svg) ![forks](https://img.shields.io/github/forks/czheisenberg/CVE-2024-37791.svg)

## CVE-2024-37770
 14Finger v1.1 was discovered to contain a remote command execution (RCE) vulnerability in the fingerprint function. This vulnerability allows attackers to execute arbitrary commands via a crafted payload.



- [https://github.com/k3ppf0r/CVE-2024-37770](https://github.com/k3ppf0r/CVE-2024-37770) :  ![starts](https://img.shields.io/github/stars/k3ppf0r/CVE-2024-37770.svg) ![forks](https://img.shields.io/github/forks/k3ppf0r/CVE-2024-37770.svg)

## CVE-2024-37765
 Machform up to version 19 is affected by an authenticated Blind SQL injection in the user account settings page.



- [https://github.com/Atreb92/cve-2024-37765](https://github.com/Atreb92/cve-2024-37765) :  ![starts](https://img.shields.io/github/stars/Atreb92/cve-2024-37765.svg) ![forks](https://img.shields.io/github/forks/Atreb92/cve-2024-37765.svg)

## CVE-2024-37764
 MachForm up to version 19 is affected by an authenticated stored cross-site scripting.



- [https://github.com/Atreb92/cve-2024-37764](https://github.com/Atreb92/cve-2024-37764) :  ![starts](https://img.shields.io/github/stars/Atreb92/cve-2024-37764.svg) ![forks](https://img.shields.io/github/forks/Atreb92/cve-2024-37764.svg)

## CVE-2024-37763
 MachForm up to version 19 is affected by an unauthenticated stored cross-site scripting which affects users with valid sessions whom can view compiled forms results.



- [https://github.com/Atreb92/cve-2024-37763](https://github.com/Atreb92/cve-2024-37763) :  ![starts](https://img.shields.io/github/stars/Atreb92/cve-2024-37763.svg) ![forks](https://img.shields.io/github/forks/Atreb92/cve-2024-37763.svg)

## CVE-2024-37762
 MachForm up to version 21 is affected by an authenticated unrestricted file upload which leads to a remote code execution.



- [https://github.com/Atreb92/cve-2024-37762](https://github.com/Atreb92/cve-2024-37762) :  ![starts](https://img.shields.io/github/stars/Atreb92/cve-2024-37762.svg) ![forks](https://img.shields.io/github/forks/Atreb92/cve-2024-37762.svg)

## CVE-2024-37759
 DataGear v5.0.0 and earlier was discovered to contain a SpEL (Spring Expression Language) expression injection vulnerability via the Data Viewing interface.



- [https://github.com/crumbledwall/CVE-2024-37759_PoC](https://github.com/crumbledwall/CVE-2024-37759_PoC) :  ![starts](https://img.shields.io/github/stars/crumbledwall/CVE-2024-37759_PoC.svg) ![forks](https://img.shields.io/github/forks/crumbledwall/CVE-2024-37759_PoC.svg)

## CVE-2024-37742
 Insecure Access Control in Safe Exam Browser (SEB) = 3.5.0 on Windows. The vulnerability allows an attacker to share clipboard data between the SEB kiosk mode and the underlying system, compromising exam integrity. By exploiting this flaw, an attacker can bypass exam controls and gain an unfair advantage during exams.



- [https://github.com/cha0sk3rn3l/CVE-2024-37742](https://github.com/cha0sk3rn3l/CVE-2024-37742) :  ![starts](https://img.shields.io/github/stars/cha0sk3rn3l/CVE-2024-37742.svg) ![forks](https://img.shields.io/github/forks/cha0sk3rn3l/CVE-2024-37742.svg)

## CVE-2024-37726
 Insecure Permissions vulnerability in Micro-Star International Co., Ltd MSI Center v.2.0.36.0 allows a local attacker to escalate privileges via the Export System Info function in MSI.CentralServer.exe



- [https://github.com/carsonchan12345/CVE-2024-37726-MSI-Center-Local-Privilege-Escalation](https://github.com/carsonchan12345/CVE-2024-37726-MSI-Center-Local-Privilege-Escalation) :  ![starts](https://img.shields.io/github/stars/carsonchan12345/CVE-2024-37726-MSI-Center-Local-Privilege-Escalation.svg) ![forks](https://img.shields.io/github/forks/carsonchan12345/CVE-2024-37726-MSI-Center-Local-Privilege-Escalation.svg)

- [https://github.com/NextGenPentesters/CVE-2024-37726-MSI-Center-Local-Privilege-Escalation](https://github.com/NextGenPentesters/CVE-2024-37726-MSI-Center-Local-Privilege-Escalation) :  ![starts](https://img.shields.io/github/stars/NextGenPentesters/CVE-2024-37726-MSI-Center-Local-Privilege-Escalation.svg) ![forks](https://img.shields.io/github/forks/NextGenPentesters/CVE-2024-37726-MSI-Center-Local-Privilege-Escalation.svg)

## CVE-2024-37606
 A Stack overflow vulnerability in D-Link DCS-932L REVB_FIRMWARE_2.18.01 allows attackers to cause a Denial of Service (DoS) via a crafted HTTP request.



- [https://github.com/itwizardo/DCS932L-Emulation-CVE-2024-37606-Attack](https://github.com/itwizardo/DCS932L-Emulation-CVE-2024-37606-Attack) :  ![starts](https://img.shields.io/github/stars/itwizardo/DCS932L-Emulation-CVE-2024-37606-Attack.svg) ![forks](https://img.shields.io/github/forks/itwizardo/DCS932L-Emulation-CVE-2024-37606-Attack.svg)

## CVE-2024-37393
 Multiple LDAP injections vulnerabilities exist in SecurEnvoy MFA before 9.4.514 due to improper validation of user-supplied input. An unauthenticated remote attacker could exfiltrate data from Active Directory through blind LDAP injection attacks against the DESKTOP service exposed on the /secserver HTTP endpoint. This may include ms-Mcs-AdmPwd, which has a cleartext password for the Local Administrator Password Solution (LAPS) feature.



- [https://github.com/noways-io/securenvoy-cve-2024-37393](https://github.com/noways-io/securenvoy-cve-2024-37393) :  ![starts](https://img.shields.io/github/stars/noways-io/securenvoy-cve-2024-37393.svg) ![forks](https://img.shields.io/github/forks/noways-io/securenvoy-cve-2024-37393.svg)

## CVE-2024-37383
 Roundcube Webmail before 1.5.7 and 1.6.x before 1.6.7 allows XSS via SVG animate attributes.



- [https://github.com/amirzargham/CVE-2024-37383-exploit](https://github.com/amirzargham/CVE-2024-37383-exploit) :  ![starts](https://img.shields.io/github/stars/amirzargham/CVE-2024-37383-exploit.svg) ![forks](https://img.shields.io/github/forks/amirzargham/CVE-2024-37383-exploit.svg)

## CVE-2024-37147
 GLPI is an open-source asset and IT management software package that provides ITIL Service Desk features, licenses tracking and software auditing. An authenticated user can attach a document to any item, even if the user has no write access on it. Upgrade to 10.0.16.



- [https://github.com/0xmupa/CVE-2024-37147-PoC](https://github.com/0xmupa/CVE-2024-37147-PoC) :  ![starts](https://img.shields.io/github/stars/0xmupa/CVE-2024-37147-PoC.svg) ![forks](https://img.shields.io/github/forks/0xmupa/CVE-2024-37147-PoC.svg)

## CVE-2024-37085
 VMware ESXi contains an authentication bypass vulnerability. A malicious actor with sufficient Active Directory (AD) permissions can gain full access to an ESXi host that was previously  configured to use AD for user management https://blogs.vmware.com/vsphere/2012/09/joining-vsphere-hosts-to-active-directory.html  by re-creating the configured AD group ('ESXi Admins' by default) after it was deleted from AD.



- [https://github.com/mahmutaymahmutay/CVE-2024-37085](https://github.com/mahmutaymahmutay/CVE-2024-37085) :  ![starts](https://img.shields.io/github/stars/mahmutaymahmutay/CVE-2024-37085.svg) ![forks](https://img.shields.io/github/forks/mahmutaymahmutay/CVE-2024-37085.svg)

- [https://github.com/WTN-arny/Vmware-ESXI](https://github.com/WTN-arny/Vmware-ESXI) :  ![starts](https://img.shields.io/github/stars/WTN-arny/Vmware-ESXI.svg) ![forks](https://img.shields.io/github/forks/WTN-arny/Vmware-ESXI.svg)

## CVE-2024-37084
 In Spring Cloud Data Flow versions prior to 2.11.4,  a malicious user who has access to the Skipper server api can use a crafted upload request to write an arbitrary file to any location on the file system which could lead to compromising the server



- [https://github.com/XiaomingX/cve-2024-37084-Poc](https://github.com/XiaomingX/cve-2024-37084-Poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-37084-Poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-37084-Poc.svg)

## CVE-2024-37081
 The vCenter Server contains multiple local privilege escalation vulnerabilities due to misconfiguration of sudo. An authenticated local user with non-administrative privileges may exploit these issues to elevate privileges to root on vCenter Server Appliance.



- [https://github.com/Mr-r00t11/CVE-2024-37081](https://github.com/Mr-r00t11/CVE-2024-37081) :  ![starts](https://img.shields.io/github/stars/Mr-r00t11/CVE-2024-37081.svg) ![forks](https://img.shields.io/github/forks/Mr-r00t11/CVE-2024-37081.svg)

- [https://github.com/mbadanoiu/CVE-2024-37081](https://github.com/mbadanoiu/CVE-2024-37081) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2024-37081.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2024-37081.svg)

- [https://github.com/CERTologists/Modified-CVE-2024-37081-POC](https://github.com/CERTologists/Modified-CVE-2024-37081-POC) :  ![starts](https://img.shields.io/github/stars/CERTologists/Modified-CVE-2024-37081-POC.svg) ![forks](https://img.shields.io/github/forks/CERTologists/Modified-CVE-2024-37081-POC.svg)

- [https://github.com/CERTologists/-CVE-2024-37081-POC](https://github.com/CERTologists/-CVE-2024-37081-POC) :  ![starts](https://img.shields.io/github/stars/CERTologists/-CVE-2024-37081-POC.svg) ![forks](https://img.shields.io/github/forks/CERTologists/-CVE-2024-37081-POC.svg)

## CVE-2024-37051
 GitHub access token could be exposed to third-party sites in JetBrains IDEs after version 2023.1 and less than: IntelliJ IDEA 2023.1.7, 2023.2.7, 2023.3.7, 2024.1.3, 2024.2 EAP3; Aqua 2024.1.2; CLion 2023.1.7, 2023.2.4, 2023.3.5, 2024.1.3, 2024.2 EAP2; DataGrip 2023.1.3, 2023.2.4, 2023.3.5, 2024.1.4; DataSpell 2023.1.6, 2023.2.7, 2023.3.6, 2024.1.2, 2024.2 EAP1; GoLand 2023.1.6, 2023.2.7, 2023.3.7, 2024.1.3, 2024.2 EAP3; MPS 2023.2.1, 2023.3.1, 2024.1 EAP2; PhpStorm 2023.1.6, 2023.2.6, 2023.3.7, 2024.1.3, 2024.2 EAP3; PyCharm 2023.1.6, 2023.2.7, 2023.3.6, 2024.1.3, 2024.2 EAP2; Rider 2023.1.7, 2023.2.5, 2023.3.6, 2024.1.3; RubyMine 2023.1.7, 2023.2.7, 2023.3.7, 2024.1.3, 2024.2 EAP4; RustRover 2024.1.1; WebStorm 2023.1.6, 2023.2.7, 2023.3.7, 2024.1.4



- [https://github.com/LeadroyaL/CVE-2024-37051-EXP](https://github.com/LeadroyaL/CVE-2024-37051-EXP) :  ![starts](https://img.shields.io/github/stars/LeadroyaL/CVE-2024-37051-EXP.svg) ![forks](https://img.shields.io/github/forks/LeadroyaL/CVE-2024-37051-EXP.svg)

- [https://github.com/mrblackstar26/CVE-2024-37051](https://github.com/mrblackstar26/CVE-2024-37051) :  ![starts](https://img.shields.io/github/stars/mrblackstar26/CVE-2024-37051.svg) ![forks](https://img.shields.io/github/forks/mrblackstar26/CVE-2024-37051.svg)

## CVE-2024-37032
 Ollama before 0.1.34 does not validate the format of the digest (sha256 with 64 hex digits) when getting the model path, and thus mishandles the TestGetBlobsPath test cases such as fewer than 64 hex digits, more than 64 hex digits, or an initial ../ substring.



- [https://github.com/Bi0x/CVE-2024-37032](https://github.com/Bi0x/CVE-2024-37032) :  ![starts](https://img.shields.io/github/stars/Bi0x/CVE-2024-37032.svg) ![forks](https://img.shields.io/github/forks/Bi0x/CVE-2024-37032.svg)

- [https://github.com/ahboon/CVE-2024-37032-scanner](https://github.com/ahboon/CVE-2024-37032-scanner) :  ![starts](https://img.shields.io/github/stars/ahboon/CVE-2024-37032-scanner.svg) ![forks](https://img.shields.io/github/forks/ahboon/CVE-2024-37032-scanner.svg)

## CVE-2024-36991
 In Splunk Enterprise on Windows versions below 9.2.2, 9.1.5, and 9.0.10, an attacker could perform a path traversal on the /modules/messaging/ endpoint in Splunk Enterprise on Windows. This vulnerability should only affect Splunk Enterprise on Windows.



- [https://github.com/bigb0x/CVE-2024-36991](https://github.com/bigb0x/CVE-2024-36991) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-36991.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-36991.svg)

- [https://github.com/Mr-xn/CVE-2024-36991](https://github.com/Mr-xn/CVE-2024-36991) :  ![starts](https://img.shields.io/github/stars/Mr-xn/CVE-2024-36991.svg) ![forks](https://img.shields.io/github/forks/Mr-xn/CVE-2024-36991.svg)

- [https://github.com/Zin0D/CVE-2024-36991](https://github.com/Zin0D/CVE-2024-36991) :  ![starts](https://img.shields.io/github/stars/Zin0D/CVE-2024-36991.svg) ![forks](https://img.shields.io/github/forks/Zin0D/CVE-2024-36991.svg)

- [https://github.com/th3gokul/CVE-2024-36991](https://github.com/th3gokul/CVE-2024-36991) :  ![starts](https://img.shields.io/github/stars/th3gokul/CVE-2024-36991.svg) ![forks](https://img.shields.io/github/forks/th3gokul/CVE-2024-36991.svg)

- [https://github.com/Cappricio-Securities/CVE-2024-36991](https://github.com/Cappricio-Securities/CVE-2024-36991) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2024-36991.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2024-36991.svg)

- [https://github.com/sardine-web/CVE-2024-36991](https://github.com/sardine-web/CVE-2024-36991) :  ![starts](https://img.shields.io/github/stars/sardine-web/CVE-2024-36991.svg) ![forks](https://img.shields.io/github/forks/sardine-web/CVE-2024-36991.svg)

## CVE-2024-36877
 Micro-Star International Z-series motherboards (Z590, Z490, and Z790) and B-series motherboards (B760, B560, B660, and B460) with firmware 7D25v14, 7D25v17 to 7D25v19, and 7D25v1A to 7D25v1H was discovered to contain a write-what-where condition in the in the SW handler for SMI 0xE3. Motherboard's with the following chipsets are affected: Intel 300, Intel 400, Intel 500, Intel 600, Intel 700, AMD 300, AMD 400, AMD 500, AMD 600 and AMD 700.



- [https://github.com/jjensn/CVE-2024-36877](https://github.com/jjensn/CVE-2024-36877) :  ![starts](https://img.shields.io/github/stars/jjensn/CVE-2024-36877.svg) ![forks](https://img.shields.io/github/forks/jjensn/CVE-2024-36877.svg)

## CVE-2024-36842
 An issue in Oncord+ Android Infotainment Systems OS Android 12, Model Hardware TS17,Hardware part Number F57L_V3.2_20220301, and Build Number PlatformVER:K24-2023/05/09-v0.01 allows a remote attacker to execute arbitrary code via the ADB port component.



- [https://github.com/abbiy/CVE-2024-36842-Backdooring-Oncord-Android-Sterio-](https://github.com/abbiy/CVE-2024-36842-Backdooring-Oncord-Android-Sterio-) :  ![starts](https://img.shields.io/github/stars/abbiy/CVE-2024-36842-Backdooring-Oncord-Android-Sterio-.svg) ![forks](https://img.shields.io/github/forks/abbiy/CVE-2024-36842-Backdooring-Oncord-Android-Sterio-.svg)

## CVE-2024-36840
 SQL Injection vulnerability in Boelter Blue System Management v.1.3 allows a remote attacker to execute arbitrary code and obtain sensitive information via the id parameter to news_details.php and location_details.php; and the section parameter to services.php.



- [https://github.com/theexploiters/CVE-2024-36840-Exploit](https://github.com/theexploiters/CVE-2024-36840-Exploit) :  ![starts](https://img.shields.io/github/stars/theexploiters/CVE-2024-36840-Exploit.svg) ![forks](https://img.shields.io/github/forks/theexploiters/CVE-2024-36840-Exploit.svg)

## CVE-2024-36837
 SQL Injection vulnerability in CRMEB v.5.2.2 allows a remote attacker to obtain sensitive information via the getProductList function in the ProductController.php file.



- [https://github.com/phtcloud-dev/CVE-2024-36837](https://github.com/phtcloud-dev/CVE-2024-36837) :  ![starts](https://img.shields.io/github/stars/phtcloud-dev/CVE-2024-36837.svg) ![forks](https://img.shields.io/github/forks/phtcloud-dev/CVE-2024-36837.svg)

## CVE-2024-36823
 The encrypt() function of Ninja Core v7.0.0 was discovered to use a weak cryptographic algorithm, leading to a possible leakage of sensitive information.



- [https://github.com/JAckLosingHeart/CVE-2024-36823-POC](https://github.com/JAckLosingHeart/CVE-2024-36823-POC) :  ![starts](https://img.shields.io/github/stars/JAckLosingHeart/CVE-2024-36823-POC.svg) ![forks](https://img.shields.io/github/forks/JAckLosingHeart/CVE-2024-36823-POC.svg)

## CVE-2024-36821
 Insecure permissions in Linksys Velop WiFi 5 (WHW01v1) 1.1.13.202617 allows attackers to escalate privileges from Guest to root.



- [https://github.com/IvanGlinkin/CVE-2024-36821](https://github.com/IvanGlinkin/CVE-2024-36821) :  ![starts](https://img.shields.io/github/stars/IvanGlinkin/CVE-2024-36821.svg) ![forks](https://img.shields.io/github/forks/IvanGlinkin/CVE-2024-36821.svg)

## CVE-2024-36587
 Insecure permissions in DNSCrypt-proxy v2.0.0alpha9 to v2.1.5 allows non-privileged attackers to escalate privileges to root via overwriting the binary dnscrypt-proxy.



- [https://github.com/meeeeing/CVE-2024-36587](https://github.com/meeeeing/CVE-2024-36587) :  ![starts](https://img.shields.io/github/stars/meeeeing/CVE-2024-36587.svg) ![forks](https://img.shields.io/github/forks/meeeeing/CVE-2024-36587.svg)

## CVE-2024-36539
 Insecure permissions in contour v1.28.3 allows attackers to access sensitive data and escalate privileges by obtaining the service account's token.



- [https://github.com/Abdurahmon3236/CVE-2024-36539](https://github.com/Abdurahmon3236/CVE-2024-36539) :  ![starts](https://img.shields.io/github/stars/Abdurahmon3236/CVE-2024-36539.svg) ![forks](https://img.shields.io/github/forks/Abdurahmon3236/CVE-2024-36539.svg)

## CVE-2024-36527
 puppeteer-renderer v.3.2.0 and before is vulnerable to Directory Traversal. Attackers can exploit the URL parameter using the file protocol to read sensitive information from the server.



- [https://github.com/bigb0x/CVE-2024-36527](https://github.com/bigb0x/CVE-2024-36527) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-36527.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-36527.svg)

## CVE-2024-36424
 K7RKScan.sys in K7 Ultimate Security before 17.0.2019 allows local users to cause a denial of service (BSOD) because of a NULL pointer dereference.



- [https://github.com/secunnix/CVE-2024-36424](https://github.com/secunnix/CVE-2024-36424) :  ![starts](https://img.shields.io/github/stars/secunnix/CVE-2024-36424.svg) ![forks](https://img.shields.io/github/forks/secunnix/CVE-2024-36424.svg)

## CVE-2024-36416
 SuiteCRM is an open-source Customer Relationship Management (CRM) software application. Prior to versions 7.14.4 and 8.6.1, a deprecated v4 API example with no log rotation allows denial of service by logging excessive data. Versions 7.14.4 and 8.6.1 contain a fix for this issue.



- [https://github.com/kva55/CVE-2024-36416](https://github.com/kva55/CVE-2024-36416) :  ![starts](https://img.shields.io/github/stars/kva55/CVE-2024-36416.svg) ![forks](https://img.shields.io/github/forks/kva55/CVE-2024-36416.svg)

## CVE-2024-36404
 GeoTools is an open source Java library that provides tools for geospatial data. Prior to versions 31.2, 30.4, and 29.6, Remote Code Execution (RCE) is possible if an application uses certain GeoTools functionality to evaluate XPath expressions supplied by user input. Versions 31.2, 30.4, and 29.6 contain a fix for this issue. As a workaround, GeoTools can operate with reduced functionality by removing the `gt-complex` jar from one's application. As an example of the impact, application schema `datastore` would not function without the ability to use XPath expressions to query complex content. Alternatively, one may utilize a drop-in replacement GeoTools jar from SourceForge for versions 31.1, 30.3, 30.2, 29.2, 28.2, 27.5, 27.4, 26.7, 26.4, 25.2, and 24.0. These jars are for download only and are not available from maven central, intended to quickly provide a fix to affected applications.



- [https://github.com/whitebear-ch/GeoServerExploit](https://github.com/whitebear-ch/GeoServerExploit) :  ![starts](https://img.shields.io/github/stars/whitebear-ch/GeoServerExploit.svg) ![forks](https://img.shields.io/github/forks/whitebear-ch/GeoServerExploit.svg)

## CVE-2024-36401
 GeoServer is an open source server that allows users to share and edit geospatial data. Prior to versions 2.22.6, 2.23.6, 2.24.4, and 2.25.2, multiple OGC request parameters allow Remote Code Execution (RCE) by unauthenticated users through specially crafted input against a default GeoServer installation due to unsafely evaluating property names as XPath expressions.

The GeoTools library API that GeoServer calls evaluates property/attribute names for feature types in a way that unsafely passes them to the commons-jxpath library which can execute arbitrary code when evaluating XPath expressions. This XPath evaluation is intended to be used only by complex feature types (i.e., Application Schema data stores) but is incorrectly being applied to simple feature types as well which makes this vulnerability apply to **ALL** GeoServer instances. No public PoC is provided but this vulnerability has been confirmed to be exploitable through WFS GetFeature, WFS GetPropertyValue, WMS GetMap, WMS GetFeatureInfo, WMS GetLegendGraphic and WPS Execute requests. This vulnerability can lead to executing arbitrary code.

Versions 2.22.6, 2.23.6, 2.24.4, and 2.25.2 contain a patch for the issue. A workaround exists by removing the `gt-complex-x.y.jar` file from the GeoServer where `x.y` is the GeoTools version (e.g., `gt-complex-31.1.jar` if running GeoServer 2.25.1). This will remove the vulnerable code from GeoServer but may break some GeoServer functionality or prevent GeoServer from deploying if the gt-complex module is needed.



- [https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance](https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance) :  ![starts](https://img.shields.io/github/stars/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg) ![forks](https://img.shields.io/github/forks/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg)

- [https://github.com/whitebear-ch/GeoServerExploit](https://github.com/whitebear-ch/GeoServerExploit) :  ![starts](https://img.shields.io/github/stars/whitebear-ch/GeoServerExploit.svg) ![forks](https://img.shields.io/github/forks/whitebear-ch/GeoServerExploit.svg)

- [https://github.com/Chocapikk/CVE-2024-36401](https://github.com/Chocapikk/CVE-2024-36401) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-36401.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-36401.svg)

- [https://github.com/Mr-xn/CVE-2024-36401](https://github.com/Mr-xn/CVE-2024-36401) :  ![starts](https://img.shields.io/github/stars/Mr-xn/CVE-2024-36401.svg) ![forks](https://img.shields.io/github/forks/Mr-xn/CVE-2024-36401.svg)

- [https://github.com/ahisec/geoserver-](https://github.com/ahisec/geoserver-) :  ![starts](https://img.shields.io/github/stars/ahisec/geoserver-.svg) ![forks](https://img.shields.io/github/forks/ahisec/geoserver-.svg)

- [https://github.com/bigb0x/CVE-2024-36401](https://github.com/bigb0x/CVE-2024-36401) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-36401.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-36401.svg)

- [https://github.com/bmth666/GeoServer-Tools-CVE-2024-36401](https://github.com/bmth666/GeoServer-Tools-CVE-2024-36401) :  ![starts](https://img.shields.io/github/stars/bmth666/GeoServer-Tools-CVE-2024-36401.svg) ![forks](https://img.shields.io/github/forks/bmth666/GeoServer-Tools-CVE-2024-36401.svg)

- [https://github.com/XiaomingX/cve-2024-36401-poc](https://github.com/XiaomingX/cve-2024-36401-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-36401-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-36401-poc.svg)

- [https://github.com/Niuwoo/CVE-2024-36401](https://github.com/Niuwoo/CVE-2024-36401) :  ![starts](https://img.shields.io/github/stars/Niuwoo/CVE-2024-36401.svg) ![forks](https://img.shields.io/github/forks/Niuwoo/CVE-2024-36401.svg)

- [https://github.com/0x0d3ad/CVE-2024-36401](https://github.com/0x0d3ad/CVE-2024-36401) :  ![starts](https://img.shields.io/github/stars/0x0d3ad/CVE-2024-36401.svg) ![forks](https://img.shields.io/github/forks/0x0d3ad/CVE-2024-36401.svg)

- [https://github.com/RevoltSecurities/CVE-2024-36401](https://github.com/RevoltSecurities/CVE-2024-36401) :  ![starts](https://img.shields.io/github/stars/RevoltSecurities/CVE-2024-36401.svg) ![forks](https://img.shields.io/github/forks/RevoltSecurities/CVE-2024-36401.svg)

- [https://github.com/amoy6228/CVE-2024-36401_Geoserver_RCE_POC](https://github.com/amoy6228/CVE-2024-36401_Geoserver_RCE_POC) :  ![starts](https://img.shields.io/github/stars/amoy6228/CVE-2024-36401_Geoserver_RCE_POC.svg) ![forks](https://img.shields.io/github/forks/amoy6228/CVE-2024-36401_Geoserver_RCE_POC.svg)

- [https://github.com/holokitty/Exploit-CVE-2024-36401](https://github.com/holokitty/Exploit-CVE-2024-36401) :  ![starts](https://img.shields.io/github/stars/holokitty/Exploit-CVE-2024-36401.svg) ![forks](https://img.shields.io/github/forks/holokitty/Exploit-CVE-2024-36401.svg)

- [https://github.com/funnyDog896/CVE-2024-36401-WoodpeckerPlugin](https://github.com/funnyDog896/CVE-2024-36401-WoodpeckerPlugin) :  ![starts](https://img.shields.io/github/stars/funnyDog896/CVE-2024-36401-WoodpeckerPlugin.svg) ![forks](https://img.shields.io/github/forks/funnyDog896/CVE-2024-36401-WoodpeckerPlugin.svg)

- [https://github.com/y1s4s/CVE-2024-36401-PoC](https://github.com/y1s4s/CVE-2024-36401-PoC) :  ![starts](https://img.shields.io/github/stars/y1s4s/CVE-2024-36401-PoC.svg) ![forks](https://img.shields.io/github/forks/y1s4s/CVE-2024-36401-PoC.svg)

- [https://github.com/jakabakos/CVE-2024-36401-GeoServer-RCE](https://github.com/jakabakos/CVE-2024-36401-GeoServer-RCE) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2024-36401-GeoServer-RCE.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2024-36401-GeoServer-RCE.svg)

## CVE-2024-36104
 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache OFBiz. This issue affects Apache OFBiz: before 18.12.14.

Users are recommended to upgrade to version 18.12.14, which fixes the issue.



- [https://github.com/Mr-xn/CVE-2024-32113](https://github.com/Mr-xn/CVE-2024-32113) :  ![starts](https://img.shields.io/github/stars/Mr-xn/CVE-2024-32113.svg) ![forks](https://img.shields.io/github/forks/Mr-xn/CVE-2024-32113.svg)

- [https://github.com/ggfzx/CVE-2024-36104](https://github.com/ggfzx/CVE-2024-36104) :  ![starts](https://img.shields.io/github/stars/ggfzx/CVE-2024-36104.svg) ![forks](https://img.shields.io/github/forks/ggfzx/CVE-2024-36104.svg)

## CVE-2024-36079
 An issue was discovered in Vaultize 21.07.27. When uploading files, there is no check that the filename parameter is correct. As a result, a temporary file will be created outside the specified directory when the file is downloaded. To exploit this, an authenticated user would upload a file with an incorrect file name, and then download it.



- [https://github.com/DxRvs/vaultize_CVE-2024-36079](https://github.com/DxRvs/vaultize_CVE-2024-36079) :  ![starts](https://img.shields.io/github/stars/DxRvs/vaultize_CVE-2024-36079.svg) ![forks](https://img.shields.io/github/forks/DxRvs/vaultize_CVE-2024-36079.svg)

## CVE-2024-35511
 phpgurukul Men Salon Management System v2.0 is vulnerable to SQL Injection via the "username" parameter of /msms/admin/index.php.



- [https://github.com/efekaanakkar/CVE-2024-35511](https://github.com/efekaanakkar/CVE-2024-35511) :  ![starts](https://img.shields.io/github/stars/efekaanakkar/CVE-2024-35511.svg) ![forks](https://img.shields.io/github/forks/efekaanakkar/CVE-2024-35511.svg)

## CVE-2024-35475
 A Cross-Site Request Forgery (CSRF) vulnerability was discovered in OpenKM Community Edition on or before version 6.3.12. The vulnerability exists in /admin/DatabaseQuery, which allows an attacker to manipulate a victim with administrative privileges to execute arbitrary SQL commands.



- [https://github.com/carsonchan12345/CVE-2024-35475](https://github.com/carsonchan12345/CVE-2024-35475) :  ![starts](https://img.shields.io/github/stars/carsonchan12345/CVE-2024-35475.svg) ![forks](https://img.shields.io/github/forks/carsonchan12345/CVE-2024-35475.svg)

## CVE-2024-35469
 A SQL injection vulnerability in /hrm/user/ in SourceCodester Human Resource Management System 1.0 allows attackers to execute arbitrary SQL commands via the password parameter.



- [https://github.com/dovankha/CVE-2024-35469](https://github.com/dovankha/CVE-2024-35469) :  ![starts](https://img.shields.io/github/stars/dovankha/CVE-2024-35469.svg) ![forks](https://img.shields.io/github/forks/dovankha/CVE-2024-35469.svg)

## CVE-2024-35468
 A SQL injection vulnerability in /hrm/index.php in SourceCodester Human Resource Management System 1.0 allows attackers to execute arbitrary SQL commands via the password parameter.



- [https://github.com/dovankha/CVE-2024-35468](https://github.com/dovankha/CVE-2024-35468) :  ![starts](https://img.shields.io/github/stars/dovankha/CVE-2024-35468.svg) ![forks](https://img.shields.io/github/forks/dovankha/CVE-2024-35468.svg)

## CVE-2024-35333
 A stack-buffer-overflow vulnerability exists in the read_charset_decl function of html2xhtml 1.3. This vulnerability occurs due to improper bounds checking when copying data into a fixed-size stack buffer. An attacker can exploit this vulnerability by providing a specially crafted input to the vulnerable function, causing a buffer overflow and potentially leading to arbitrary code execution, denial of service, or data corruption.



- [https://github.com/momo1239/CVE-2024-35333](https://github.com/momo1239/CVE-2024-35333) :  ![starts](https://img.shields.io/github/stars/momo1239/CVE-2024-35333.svg) ![forks](https://img.shields.io/github/forks/momo1239/CVE-2024-35333.svg)

## CVE-2024-35315
 A vulnerability in the Desktop Client of Mitel MiCollab through 9.7.1.110, and MiVoice Business Solution Virtual Instance (MiVB SVI) 1.0.0.25, could allow an authenticated attacker to conduct a privilege escalation attack due to improper file validation. A successful exploit could allow an attacker to run arbitrary code with elevated privileges.



- [https://github.com/ewilded/CVE-2024-35315-POC](https://github.com/ewilded/CVE-2024-35315-POC) :  ![starts](https://img.shields.io/github/stars/ewilded/CVE-2024-35315-POC.svg) ![forks](https://img.shields.io/github/forks/ewilded/CVE-2024-35315-POC.svg)

## CVE-2024-35286
 A vulnerability in NuPoint Messenger (NPM) of Mitel MiCollab through 9.8.0.33 allows an unauthenticated attacker to conduct a SQL injection attack due to insufficient sanitization of user input. A successful exploit could allow an attacker to access sensitive information and execute arbitrary database and management operations.



- [https://github.com/lu4m575/CVE-2024-35286_scan.nse](https://github.com/lu4m575/CVE-2024-35286_scan.nse) :  ![starts](https://img.shields.io/github/stars/lu4m575/CVE-2024-35286_scan.nse.svg) ![forks](https://img.shields.io/github/forks/lu4m575/CVE-2024-35286_scan.nse.svg)

## CVE-2024-35250
 Windows Kernel-Mode Driver Elevation of Privilege Vulnerability



- [https://github.com/yinsel/CVE-2024-35250-BOF](https://github.com/yinsel/CVE-2024-35250-BOF) :  ![starts](https://img.shields.io/github/stars/yinsel/CVE-2024-35250-BOF.svg) ![forks](https://img.shields.io/github/forks/yinsel/CVE-2024-35250-BOF.svg)

- [https://github.com/0xROOTPLS/GiveMeKernel](https://github.com/0xROOTPLS/GiveMeKernel) :  ![starts](https://img.shields.io/github/stars/0xROOTPLS/GiveMeKernel.svg) ![forks](https://img.shields.io/github/forks/0xROOTPLS/GiveMeKernel.svg)

## CVE-2024-35242
 Composer is a dependency manager for PHP. On the 2.x branch prior to versions 2.2.24 and 2.7.7, the `composer install` command running inside a git/hg repository which has specially crafted branch names can lead to command injection. This requires cloning untrusted repositories. Patches are available in version 2.2.24 for 2.2 LTS or 2.7.7 for mainline. As a workaround, avoid cloning potentially compromised repositories.



- [https://github.com/KKkai0315/CVE-2024-35242](https://github.com/KKkai0315/CVE-2024-35242) :  ![starts](https://img.shields.io/github/stars/KKkai0315/CVE-2024-35242.svg) ![forks](https://img.shields.io/github/forks/KKkai0315/CVE-2024-35242.svg)

## CVE-2024-35205
 The WPS Office (aka cn.wps.moffice_eng) application before 17.0.0 for Android fails to properly sanitize file names before processing them through external application interactions, leading to a form of path traversal. This potentially enables any application to dispatch a crafted library file, aiming to overwrite an existing native library utilized by WPS Office. Successful exploitation could result in the execution of arbitrary commands under the guise of WPS Office's application ID.



- [https://github.com/cyb3r-w0lf/Dirty_Stream-Android-POC](https://github.com/cyb3r-w0lf/Dirty_Stream-Android-POC) :  ![starts](https://img.shields.io/github/stars/cyb3r-w0lf/Dirty_Stream-Android-POC.svg) ![forks](https://img.shields.io/github/forks/cyb3r-w0lf/Dirty_Stream-Android-POC.svg)

## CVE-2024-35176
  REXML is an XML toolkit for Ruby. The REXML gem before 3.2.6 has a denial of service vulnerability when it parses an XML that has many ``s in an attribute value. Those who need to parse untrusted XMLs may be impacted to this vulnerability. The REXML gem 3.2.7 or later include the patch to fix this vulnerability. As a workaround, don't parse untrusted XMLs.



- [https://github.com/SpiralBL0CK/CVE-2024-35176](https://github.com/SpiralBL0CK/CVE-2024-35176) :  ![starts](https://img.shields.io/github/stars/SpiralBL0CK/CVE-2024-35176.svg) ![forks](https://img.shields.io/github/forks/SpiralBL0CK/CVE-2024-35176.svg)

## CVE-2024-34958
 idccms v1.35 was discovered to contain a Cross-Site Request Forgery (CSRF) via the component admin/banner_deal.php?mudi=add



- [https://github.com/Gr-1m/CVE-2024-34958](https://github.com/Gr-1m/CVE-2024-34958) :  ![starts](https://img.shields.io/github/stars/Gr-1m/CVE-2024-34958.svg) ![forks](https://img.shields.io/github/forks/Gr-1m/CVE-2024-34958.svg)

## CVE-2024-34833
 Sourcecodester Payroll Management System v1.0 is vulnerable to File Upload. Users can upload images via the "save_settings" page. An unauthenticated attacker can leverage this functionality to upload a malicious PHP file instead. Successful exploitation of this vulnerability results in the ability to execute arbitrary code as the user running the web server.



- [https://github.com/ShellUnease/CVE-2024-34833-payroll-management-system-rce](https://github.com/ShellUnease/CVE-2024-34833-payroll-management-system-rce) :  ![starts](https://img.shields.io/github/stars/ShellUnease/CVE-2024-34833-payroll-management-system-rce.svg) ![forks](https://img.shields.io/github/forks/ShellUnease/CVE-2024-34833-payroll-management-system-rce.svg)

## CVE-2024-34832
 Directory Traversal vulnerability in CubeCart v.6.5.5 and before allows an attacker to execute arbitrary code via a crafted file uploaded to the _g and node parameters.



- [https://github.com/julio-cfa/CVE-2024-34832](https://github.com/julio-cfa/CVE-2024-34832) :  ![starts](https://img.shields.io/github/stars/julio-cfa/CVE-2024-34832.svg) ![forks](https://img.shields.io/github/forks/julio-cfa/CVE-2024-34832.svg)

## CVE-2024-34716
 PrestaShop is an open source e-commerce web application. A cross-site scripting (XSS) vulnerability that only affects PrestaShops with customer-thread feature flag enabled is present starting from PrestaShop 8.1.0 and prior to PrestaShop 8.1.6. When the customer thread feature flag is enabled through the front-office contact form, a hacker can upload a malicious file containing an XSS that will be executed when an admin opens the attached file in back office. The script injected can access the session and the security token, which allows it to perform any authenticated action in the scope of the administrator's right. This vulnerability is patched in 8.1.6. A workaround is to disable the customer-thread feature-flag.



- [https://github.com/aelmokhtar/CVE-2024-34716](https://github.com/aelmokhtar/CVE-2024-34716) :  ![starts](https://img.shields.io/github/stars/aelmokhtar/CVE-2024-34716.svg) ![forks](https://img.shields.io/github/forks/aelmokhtar/CVE-2024-34716.svg)

## CVE-2024-34693
 Improper Input Validation vulnerability in Apache Superset, allows for an authenticated attacker to create a MariaDB connection with local_infile enabled. If both the MariaDB server (off by default) and the local mysql client on the web server are set to allow for local infile, it's possible for the attacker to execute a specific MySQL/MariaDB SQL command that is able to read files from the server and insert their content on a MariaDB database table.This issue affects Apache Superset: before 3.1.3 and version 4.0.0

Users are recommended to upgrade to version 4.0.1 or 3.1.3, which fixes the issue.



- [https://github.com/mbadanoiu/CVE-2024-34693](https://github.com/mbadanoiu/CVE-2024-34693) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2024-34693.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2024-34693.svg)

- [https://github.com/Mr-r00t11/CVE-2024-34693](https://github.com/Mr-r00t11/CVE-2024-34693) :  ![starts](https://img.shields.io/github/stars/Mr-r00t11/CVE-2024-34693.svg) ![forks](https://img.shields.io/github/forks/Mr-r00t11/CVE-2024-34693.svg)

## CVE-2024-34582
 Sunhillo SureLine through 8.10.0 on RICI 5000 devices allows cgi/usrPasswd.cgi userid_change XSS within the Forgot Password feature.



- [https://github.com/silent6trinity/CVE-2024-34582](https://github.com/silent6trinity/CVE-2024-34582) :  ![starts](https://img.shields.io/github/stars/silent6trinity/CVE-2024-34582.svg) ![forks](https://img.shields.io/github/forks/silent6trinity/CVE-2024-34582.svg)

## CVE-2024-34474
 Clario through 2024-04-11 for Desktop has weak permissions for %PROGRAMDATA%\Clario and tries to load DLLs from there as SYSTEM.



- [https://github.com/Alaatk/CVE-2024-34474](https://github.com/Alaatk/CVE-2024-34474) :  ![starts](https://img.shields.io/github/stars/Alaatk/CVE-2024-34474.svg) ![forks](https://img.shields.io/github/forks/Alaatk/CVE-2024-34474.svg)

## CVE-2024-34472
 An issue was discovered in HSC Mailinspector 5.2.17-3 through v.5.2.18. An authenticated blind SQL injection vulnerability exists in the mliRealtimeEmails.php file. The ordemGrid parameter in a POST request to /mailinspector/mliRealtimeEmails.php does not properly sanitize input, allowing an authenticated attacker to execute arbitrary SQL commands, leading to the potential disclosure of the entire application database.



- [https://github.com/osvaldotenorio/CVE-2024-34472](https://github.com/osvaldotenorio/CVE-2024-34472) :  ![starts](https://img.shields.io/github/stars/osvaldotenorio/CVE-2024-34472.svg) ![forks](https://img.shields.io/github/forks/osvaldotenorio/CVE-2024-34472.svg)

## CVE-2024-34471
 An issue was discovered in HSC Mailinspector 5.2.17-3. A Path Traversal vulnerability (resulting in file deletion) exists in the mliRealtimeEmails.php file. The filename parameter in the export HTML functionality does not properly validate the file location, allowing an attacker to read and delete arbitrary files on the server. This was observed when the mliRealtimeEmails.php file itself was read and subsequently deleted, resulting in a 404 error for the file and disruption of email information loading.



- [https://github.com/osvaldotenorio/CVE-2024-34471](https://github.com/osvaldotenorio/CVE-2024-34471) :  ![starts](https://img.shields.io/github/stars/osvaldotenorio/CVE-2024-34471.svg) ![forks](https://img.shields.io/github/forks/osvaldotenorio/CVE-2024-34471.svg)

## CVE-2024-34470
 An issue was discovered in HSC Mailinspector 5.2.17-3 through v.5.2.18. An Unauthenticated Path Traversal vulnerability exists in the /public/loader.php file. The path parameter does not properly filter whether the file and directory passed are part of the webroot, allowing an attacker to read arbitrary files on the server.



- [https://github.com/Mr-r00t11/CVE-2024-34470](https://github.com/Mr-r00t11/CVE-2024-34470) :  ![starts](https://img.shields.io/github/stars/Mr-r00t11/CVE-2024-34470.svg) ![forks](https://img.shields.io/github/forks/Mr-r00t11/CVE-2024-34470.svg)

- [https://github.com/bigb0x/CVE-2024-34470](https://github.com/bigb0x/CVE-2024-34470) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-34470.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-34470.svg)

- [https://github.com/th3gokul/CVE-2024-34470](https://github.com/th3gokul/CVE-2024-34470) :  ![starts](https://img.shields.io/github/stars/th3gokul/CVE-2024-34470.svg) ![forks](https://img.shields.io/github/forks/th3gokul/CVE-2024-34470.svg)

- [https://github.com/Cappricio-Securities/CVE-2024-34470](https://github.com/Cappricio-Securities/CVE-2024-34470) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2024-34470.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2024-34470.svg)

- [https://github.com/osvaldotenorio/CVE-2024-34470](https://github.com/osvaldotenorio/CVE-2024-34470) :  ![starts](https://img.shields.io/github/stars/osvaldotenorio/CVE-2024-34470.svg) ![forks](https://img.shields.io/github/forks/osvaldotenorio/CVE-2024-34470.svg)

## CVE-2024-34469
 Rukovoditel before 3.5.3 allows XSS via user_photo to index.php?module=users/registration&action=save.



- [https://github.com/Toxich4/CVE-2024-34469](https://github.com/Toxich4/CVE-2024-34469) :  ![starts](https://img.shields.io/github/stars/Toxich4/CVE-2024-34469.svg) ![forks](https://img.shields.io/github/forks/Toxich4/CVE-2024-34469.svg)

## CVE-2024-34452
 CMSimple_XH 1.7.6 allows XSS by uploading a crafted SVG document.



- [https://github.com/surajhacx/CVE-2024-34452](https://github.com/surajhacx/CVE-2024-34452) :  ![starts](https://img.shields.io/github/stars/surajhacx/CVE-2024-34452.svg) ![forks](https://img.shields.io/github/forks/surajhacx/CVE-2024-34452.svg)

## CVE-2024-34361
 Pi-hole is a DNS sinkhole that protects devices from unwanted content without installing any client-side software. A vulnerability in versions prior to 5.18.3 allows an authenticated user to make internal requests to the server via the `gravity_DownloadBlocklistFromUrl()` function. Depending on some circumstances, the vulnerability could lead to remote command execution. Version 5.18.3 contains a patch for this issue.



- [https://github.com/T0X1Cx/CVE-2024-34361-PiHole-SSRF-to-RCE](https://github.com/T0X1Cx/CVE-2024-34361-PiHole-SSRF-to-RCE) :  ![starts](https://img.shields.io/github/stars/T0X1Cx/CVE-2024-34361-PiHole-SSRF-to-RCE.svg) ![forks](https://img.shields.io/github/forks/T0X1Cx/CVE-2024-34361-PiHole-SSRF-to-RCE.svg)

## CVE-2024-34351
 Next.js is a React framework that can provide building blocks to create web applications. A Server-Side Request Forgery (SSRF) vulnerability was identified in Next.js Server Actions. If the `Host` header is modified, and the below conditions are also met, an attacker may be able to make requests that appear to be originating from the Next.js application server itself. The required conditions are 1) Next.js is running in a self-hosted manner; 2) the Next.js application makes use of Server Actions; and 3) the Server Action performs a redirect to a relative path which starts with a `/`. This vulnerability was fixed in Next.js `14.1.1`.



- [https://github.com/Voorivex/CVE-2024-34351](https://github.com/Voorivex/CVE-2024-34351) :  ![starts](https://img.shields.io/github/stars/Voorivex/CVE-2024-34351.svg) ![forks](https://img.shields.io/github/forks/Voorivex/CVE-2024-34351.svg)

- [https://github.com/avergnaud/Next.js_exploit_CVE-2024-34351](https://github.com/avergnaud/Next.js_exploit_CVE-2024-34351) :  ![starts](https://img.shields.io/github/stars/avergnaud/Next.js_exploit_CVE-2024-34351.svg) ![forks](https://img.shields.io/github/forks/avergnaud/Next.js_exploit_CVE-2024-34351.svg)

## CVE-2024-34350
 Next.js is a React framework that can provide building blocks to create web applications. Prior to 13.5.1, an inconsistent interpretation of a crafted HTTP request meant that requests are treated as both a single request, and two separate requests by Next.js, leading to desynchronized responses. This led to a response queue poisoning vulnerability in the affected Next.js versions. For a request to be exploitable, the affected route also had to be making use of the [rewrites](https://nextjs.org/docs/app/api-reference/next-config-js/rewrites) feature in Next.js. The vulnerability is resolved in Next.js `13.5.1` and newer.



- [https://github.com/Sudistark/rewrites-nextjs-CVE-2024-34350](https://github.com/Sudistark/rewrites-nextjs-CVE-2024-34350) :  ![starts](https://img.shields.io/github/stars/Sudistark/rewrites-nextjs-CVE-2024-34350.svg) ![forks](https://img.shields.io/github/forks/Sudistark/rewrites-nextjs-CVE-2024-34350.svg)

## CVE-2024-34342
 react-pdf displays PDFs in React apps. If PDF.js is used to load a malicious PDF, and PDF.js is configured with `isEvalSupported` set to `true` (which is the default value), unrestricted attacker-controlled JavaScript will be executed in the context of the hosting domain. This vulnerability is fixed in 7.7.3 and 8.0.2.



- [https://github.com/LOURC0D3/CVE-2024-4367-PoC](https://github.com/LOURC0D3/CVE-2024-4367-PoC) :  ![starts](https://img.shields.io/github/stars/LOURC0D3/CVE-2024-4367-PoC.svg) ![forks](https://img.shields.io/github/forks/LOURC0D3/CVE-2024-4367-PoC.svg)

## CVE-2024-34329
 Insecure permissions in Entrust Datacard XPS Card Printer Driver 8.5 and earlier without the dxp1-patch-E24-004 patch allows unauthenticated attackers to execute arbitrary code as SYSTEM via a crafted DLL payload.



- [https://github.com/pamoutaf/CVE-2024-34329](https://github.com/pamoutaf/CVE-2024-34329) :  ![starts](https://img.shields.io/github/stars/pamoutaf/CVE-2024-34329.svg) ![forks](https://img.shields.io/github/forks/pamoutaf/CVE-2024-34329.svg)

## CVE-2024-34328
 An open redirect in Sielox AnyWare v2.1.2 allows attackers to execute a man-in-the-middle attack via a crafted URL.



- [https://github.com/0xsu3ks/CVE-2024-34328](https://github.com/0xsu3ks/CVE-2024-34328) :  ![starts](https://img.shields.io/github/stars/0xsu3ks/CVE-2024-34328.svg) ![forks](https://img.shields.io/github/forks/0xsu3ks/CVE-2024-34328.svg)

## CVE-2024-34327
 Sielox AnyWare v2.1.2 was discovered to contain a SQL injection vulnerability via the email address field of the password reset form.



- [https://github.com/0xsu3ks/CVE-2024-34327](https://github.com/0xsu3ks/CVE-2024-34327) :  ![starts](https://img.shields.io/github/stars/0xsu3ks/CVE-2024-34327.svg) ![forks](https://img.shields.io/github/forks/0xsu3ks/CVE-2024-34327.svg)

## CVE-2024-34313
 An issue in VPL Jail System up to v4.0.2 allows attackers to execute a directory traversal via a crafted request to a public endpoint.



- [https://github.com/vincentscode/CVE-2024-34313](https://github.com/vincentscode/CVE-2024-34313) :  ![starts](https://img.shields.io/github/stars/vincentscode/CVE-2024-34313.svg) ![forks](https://img.shields.io/github/forks/vincentscode/CVE-2024-34313.svg)

## CVE-2024-34312
 Virtual Programming Lab for Moodle up to v4.2.3 was discovered to contain a cross-site scripting (XSS) vulnerability via the component vplide.js.



- [https://github.com/vincentscode/CVE-2024-34312](https://github.com/vincentscode/CVE-2024-34312) :  ![starts](https://img.shields.io/github/stars/vincentscode/CVE-2024-34312.svg) ![forks](https://img.shields.io/github/forks/vincentscode/CVE-2024-34312.svg)

## CVE-2024-34310
 Jin Fang Times Content Management System v3.2.3 was discovered to contain a SQL injection vulnerability via the id parameter.



- [https://github.com/3309899621/CVE-2024-34310](https://github.com/3309899621/CVE-2024-34310) :  ![starts](https://img.shields.io/github/stars/3309899621/CVE-2024-34310.svg) ![forks](https://img.shields.io/github/forks/3309899621/CVE-2024-34310.svg)

## CVE-2024-34226
 SQL injection vulnerability in /php-sqlite-vms/?page=manage_visitor&id=1 in SourceCodester Visitor Management System 1.0 allow attackers to execute arbitrary SQL commands via the id parameters.



- [https://github.com/dovankha/CVE-2024-34226](https://github.com/dovankha/CVE-2024-34226) :  ![starts](https://img.shields.io/github/stars/dovankha/CVE-2024-34226.svg) ![forks](https://img.shields.io/github/forks/dovankha/CVE-2024-34226.svg)

## CVE-2024-34225
 Cross Site Scripting vulnerability in php-lms/admin/?page=system_info in Computer Laboratory Management System using PHP and MySQL 1.0 allow remote attackers to inject arbitrary web script or HTML via the name, shortname parameters.



- [https://github.com/dovankha/CVE-2024-34225](https://github.com/dovankha/CVE-2024-34225) :  ![starts](https://img.shields.io/github/stars/dovankha/CVE-2024-34225.svg) ![forks](https://img.shields.io/github/forks/dovankha/CVE-2024-34225.svg)

## CVE-2024-34224
 Cross Site Scripting vulnerability in /php-lms/classes/Users.php?f=save in Computer Laboratory Management System using PHP and MySQL 1.0 allow remote attackers to inject arbitrary web script or HTML via the firstname, middlename, lastname parameters.



- [https://github.com/dovankha/CVE-2024-34224](https://github.com/dovankha/CVE-2024-34224) :  ![starts](https://img.shields.io/github/stars/dovankha/CVE-2024-34224.svg) ![forks](https://img.shields.io/github/forks/dovankha/CVE-2024-34224.svg)

## CVE-2024-34223
 Insecure permission vulnerability in /hrm/leaverequest.php in SourceCodester Human Resource Management System 1.0 allow attackers to approve or reject leave ticket.



- [https://github.com/dovankha/CVE-2024-34223](https://github.com/dovankha/CVE-2024-34223) :  ![starts](https://img.shields.io/github/stars/dovankha/CVE-2024-34223.svg) ![forks](https://img.shields.io/github/forks/dovankha/CVE-2024-34223.svg)

## CVE-2024-34222
 Sourcecodester Human Resource Management System 1.0 is vulnerable to SQL Injection via the searccountry parameter.



- [https://github.com/dovankha/CVE-2024-34222](https://github.com/dovankha/CVE-2024-34222) :  ![starts](https://img.shields.io/github/stars/dovankha/CVE-2024-34222.svg) ![forks](https://img.shields.io/github/forks/dovankha/CVE-2024-34222.svg)

## CVE-2024-34221
 Sourcecodester Human Resource Management System 1.0 is vulnerable to Insecure Permissions resulting in privilege escalation.



- [https://github.com/dovankha/CVE-2024-34221](https://github.com/dovankha/CVE-2024-34221) :  ![starts](https://img.shields.io/github/stars/dovankha/CVE-2024-34221.svg) ![forks](https://img.shields.io/github/forks/dovankha/CVE-2024-34221.svg)

## CVE-2024-34220
 Sourcecodester Human Resource Management System 1.0 is vulnerable to SQL Injection via the 'leave' parameter.



- [https://github.com/dovankha/CVE-2024-34220](https://github.com/dovankha/CVE-2024-34220) :  ![starts](https://img.shields.io/github/stars/dovankha/CVE-2024-34220.svg) ![forks](https://img.shields.io/github/forks/dovankha/CVE-2024-34220.svg)

## CVE-2024-34144
 A sandbox bypass vulnerability involving crafted constructor bodies in Jenkins Script Security Plugin 1335.vf07d9ce377a_e and earlier allows attackers with permission to define and run sandboxed scripts, including Pipelines, to bypass the sandbox protection and execute arbitrary code in the context of the Jenkins controller JVM.



- [https://github.com/MXWXZ/CVE-2024-34144](https://github.com/MXWXZ/CVE-2024-34144) :  ![starts](https://img.shields.io/github/stars/MXWXZ/CVE-2024-34144.svg) ![forks](https://img.shields.io/github/forks/MXWXZ/CVE-2024-34144.svg)

## CVE-2024-34102
 Adobe Commerce versions 2.4.7, 2.4.6-p5, 2.4.5-p7, 2.4.4-p8 and earlier are affected by an Improper Restriction of XML External Entity Reference ('XXE') vulnerability that could result in arbitrary code execution. An attacker could exploit this vulnerability by sending a crafted XML document that references external entities. Exploitation of this issue does not require user interaction.



- [https://github.com/Chocapikk/CVE-2024-34102](https://github.com/Chocapikk/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-34102.svg)

- [https://github.com/bigb0x/CVE-2024-34102](https://github.com/bigb0x/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-34102.svg)

- [https://github.com/th3gokul/CVE-2024-34102](https://github.com/th3gokul/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/th3gokul/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/th3gokul/CVE-2024-34102.svg)

- [https://github.com/jakabakos/CVE-2024-34102-CosmicSting-XXE-in-Adobe-Commerce-and-Magento](https://github.com/jakabakos/CVE-2024-34102-CosmicSting-XXE-in-Adobe-Commerce-and-Magento) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2024-34102-CosmicSting-XXE-in-Adobe-Commerce-and-Magento.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2024-34102-CosmicSting-XXE-in-Adobe-Commerce-and-Magento.svg)

- [https://github.com/bughuntar/CVE-2024-34102](https://github.com/bughuntar/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/bughuntar/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/bughuntar/CVE-2024-34102.svg)

- [https://github.com/EQSTLab/CVE-2024-34102](https://github.com/EQSTLab/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/EQSTLab/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/EQSTLab/CVE-2024-34102.svg)

- [https://github.com/11whoami99/CVE-2024-34102](https://github.com/11whoami99/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/11whoami99/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/11whoami99/CVE-2024-34102.svg)

- [https://github.com/wubinworks/magento2-jwt-auth-patch](https://github.com/wubinworks/magento2-jwt-auth-patch) :  ![starts](https://img.shields.io/github/stars/wubinworks/magento2-jwt-auth-patch.svg) ![forks](https://img.shields.io/github/forks/wubinworks/magento2-jwt-auth-patch.svg)

- [https://github.com/0x0d3ad/CVE-2024-34102](https://github.com/0x0d3ad/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/0x0d3ad/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/0x0d3ad/CVE-2024-34102.svg)

- [https://github.com/Phantom-IN/CVE-2024-34102](https://github.com/Phantom-IN/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/Phantom-IN/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/Phantom-IN/CVE-2024-34102.svg)

- [https://github.com/wubinworks/magento2-cosmic-sting-patch](https://github.com/wubinworks/magento2-cosmic-sting-patch) :  ![starts](https://img.shields.io/github/stars/wubinworks/magento2-cosmic-sting-patch.svg) ![forks](https://img.shields.io/github/forks/wubinworks/magento2-cosmic-sting-patch.svg)

- [https://github.com/unknownzerobit/poc](https://github.com/unknownzerobit/poc) :  ![starts](https://img.shields.io/github/stars/unknownzerobit/poc.svg) ![forks](https://img.shields.io/github/forks/unknownzerobit/poc.svg)

- [https://github.com/Koray123-debug/CVE-2024-34102](https://github.com/Koray123-debug/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/Koray123-debug/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/Koray123-debug/CVE-2024-34102.svg)

- [https://github.com/d0rb/CVE-2024-34102](https://github.com/d0rb/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2024-34102.svg)

- [https://github.com/cmsec423/CVE-2024-34102](https://github.com/cmsec423/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/cmsec423/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/cmsec423/CVE-2024-34102.svg)

- [https://github.com/mksundaram69/CVE-2024-34102](https://github.com/mksundaram69/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/mksundaram69/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/mksundaram69/CVE-2024-34102.svg)

- [https://github.com/crynomore/CVE-2024-34102](https://github.com/crynomore/CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/crynomore/CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/crynomore/CVE-2024-34102.svg)

- [https://github.com/ArturArz1/TestCVE-2024-34102](https://github.com/ArturArz1/TestCVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/ArturArz1/TestCVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/ArturArz1/TestCVE-2024-34102.svg)

- [https://github.com/bughuntar/CVE-2024-34102-Python](https://github.com/bughuntar/CVE-2024-34102-Python) :  ![starts](https://img.shields.io/github/stars/bughuntar/CVE-2024-34102-Python.svg) ![forks](https://img.shields.io/github/forks/bughuntar/CVE-2024-34102-Python.svg)

- [https://github.com/SamJUK/cosmicsting-validator](https://github.com/SamJUK/cosmicsting-validator) :  ![starts](https://img.shields.io/github/stars/SamJUK/cosmicsting-validator.svg) ![forks](https://img.shields.io/github/forks/SamJUK/cosmicsting-validator.svg)

- [https://github.com/cmsec423/Magento-XXE-CVE-2024-34102](https://github.com/cmsec423/Magento-XXE-CVE-2024-34102) :  ![starts](https://img.shields.io/github/stars/cmsec423/Magento-XXE-CVE-2024-34102.svg) ![forks](https://img.shields.io/github/forks/cmsec423/Magento-XXE-CVE-2024-34102.svg)

- [https://github.com/wubinworks/magento2-encryption-key-manager-cli](https://github.com/wubinworks/magento2-encryption-key-manager-cli) :  ![starts](https://img.shields.io/github/stars/wubinworks/magento2-encryption-key-manager-cli.svg) ![forks](https://img.shields.io/github/forks/wubinworks/magento2-encryption-key-manager-cli.svg)

- [https://github.com/wubinworks/magento2-enhanced-xml-security](https://github.com/wubinworks/magento2-enhanced-xml-security) :  ![starts](https://img.shields.io/github/stars/wubinworks/magento2-enhanced-xml-security.svg) ![forks](https://img.shields.io/github/forks/wubinworks/magento2-enhanced-xml-security.svg)

## CVE-2024-33911
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Weblizar School Management Pro.This issue affects School Management Pro: from n/a through 10.3.4.





- [https://github.com/xbz0n/CVE-2024-33911](https://github.com/xbz0n/CVE-2024-33911) :  ![starts](https://img.shields.io/github/stars/xbz0n/CVE-2024-33911.svg) ![forks](https://img.shields.io/github/forks/xbz0n/CVE-2024-33911.svg)

## CVE-2024-33901
 Issue in KeePassXC 2.7.7 allows an attacker (who has the privileges of the victim) to recover some passwords stored in the .kdbx database via a memory dump. NOTE: the vendor disputes this because memory-management constraints make this unavoidable in the current design and other realistic designs.



- [https://github.com/gmikisilva/CVE-2024-33901-ProofOfConcept](https://github.com/gmikisilva/CVE-2024-33901-ProofOfConcept) :  ![starts](https://img.shields.io/github/stars/gmikisilva/CVE-2024-33901-ProofOfConcept.svg) ![forks](https://img.shields.io/github/forks/gmikisilva/CVE-2024-33901-ProofOfConcept.svg)

## CVE-2024-33883
 The ejs (aka Embedded JavaScript templates) package before 3.1.10 for Node.js lacks certain pollution protection.



- [https://github.com/Grantzile/PoC-CVE-2024-33883](https://github.com/Grantzile/PoC-CVE-2024-33883) :  ![starts](https://img.shields.io/github/stars/Grantzile/PoC-CVE-2024-33883.svg) ![forks](https://img.shields.io/github/forks/Grantzile/PoC-CVE-2024-33883.svg)

## CVE-2024-33775
 An issue with the Autodiscover component in Nagios XI 2024R1.01 allows a remote attacker to escalate privileges via a crafted Dashlet.



- [https://github.com/Neo-XeD/CVE-2024-33775](https://github.com/Neo-XeD/CVE-2024-33775) :  ![starts](https://img.shields.io/github/stars/Neo-XeD/CVE-2024-33775.svg) ![forks](https://img.shields.io/github/forks/Neo-XeD/CVE-2024-33775.svg)

## CVE-2024-33724
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/fuzzlove/soplanning-1.52-exploits](https://github.com/fuzzlove/soplanning-1.52-exploits) :  ![starts](https://img.shields.io/github/stars/fuzzlove/soplanning-1.52-exploits.svg) ![forks](https://img.shields.io/github/forks/fuzzlove/soplanning-1.52-exploits.svg)

## CVE-2024-33722
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/fuzzlove/soplanning-1.52-exploits](https://github.com/fuzzlove/soplanning-1.52-exploits) :  ![starts](https://img.shields.io/github/stars/fuzzlove/soplanning-1.52-exploits.svg) ![forks](https://img.shields.io/github/forks/fuzzlove/soplanning-1.52-exploits.svg)

## CVE-2024-33559
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in 8theme XStore allows SQL Injection.This issue affects XStore: from n/a through 9.3.5.





- [https://github.com/absholi7ly/WordPress-XStore-theme-SQL-Injection](https://github.com/absholi7ly/WordPress-XStore-theme-SQL-Injection) :  ![starts](https://img.shields.io/github/stars/absholi7ly/WordPress-XStore-theme-SQL-Injection.svg) ![forks](https://img.shields.io/github/forks/absholi7ly/WordPress-XStore-theme-SQL-Injection.svg)

## CVE-2024-33438
 File Upload vulnerability in CubeCart before 6.5.5 allows an authenticated user to execute arbitrary code via a crafted .phar file.



- [https://github.com/julio-cfa/CVE-2024-33438](https://github.com/julio-cfa/CVE-2024-33438) :  ![starts](https://img.shields.io/github/stars/julio-cfa/CVE-2024-33438.svg) ![forks](https://img.shields.io/github/forks/julio-cfa/CVE-2024-33438.svg)

## CVE-2024-33437
 An issue in CSS Exfil Protection v.1.1.0 allows a remote attacker to obtain sensitive information due to missing support for CSS Style Rules.



- [https://github.com/randshell/CSS-Exfil-Protection-POC](https://github.com/randshell/CSS-Exfil-Protection-POC) :  ![starts](https://img.shields.io/github/stars/randshell/CSS-Exfil-Protection-POC.svg) ![forks](https://img.shields.io/github/forks/randshell/CSS-Exfil-Protection-POC.svg)

## CVE-2024-33436
 An issue in CSS Exfil Protection v.1.1.0 allows a remote attacker to obtain sensitive information due to missing support for CSS variables



- [https://github.com/randshell/CSS-Exfil-Protection-POC](https://github.com/randshell/CSS-Exfil-Protection-POC) :  ![starts](https://img.shields.io/github/stars/randshell/CSS-Exfil-Protection-POC.svg) ![forks](https://img.shields.io/github/forks/randshell/CSS-Exfil-Protection-POC.svg)

## CVE-2024-33352
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/mmiszczyk/CVE-2024-33352](https://github.com/mmiszczyk/CVE-2024-33352) :  ![starts](https://img.shields.io/github/stars/mmiszczyk/CVE-2024-33352.svg) ![forks](https://img.shields.io/github/forks/mmiszczyk/CVE-2024-33352.svg)

- [https://github.com/geniuszly/GenBlueStacksInjector](https://github.com/geniuszly/GenBlueStacksInjector) :  ![starts](https://img.shields.io/github/stars/geniuszly/GenBlueStacksInjector.svg) ![forks](https://img.shields.io/github/forks/geniuszly/GenBlueStacksInjector.svg)

## CVE-2024-33299
 Cross Site Scripting vulnerability in Microweber v.2.0.9 allows a remote attacker to execute arbitrary code via the First Name and Last Name parameters in the endpoint /admin/module/view?type=users



- [https://github.com/MathSabo/CVE-2024-33299](https://github.com/MathSabo/CVE-2024-33299) :  ![starts](https://img.shields.io/github/stars/MathSabo/CVE-2024-33299.svg) ![forks](https://img.shields.io/github/forks/MathSabo/CVE-2024-33299.svg)

## CVE-2024-33298
 Microweber Cross Site Scripting vulnerability in Microweber v.2.0.9 allows a remote attacker to execute arbitrary code via the create new backup function in the endpoint /admin/module/view?type=admin__backup



- [https://github.com/MathSabo/CVE-2024-33298](https://github.com/MathSabo/CVE-2024-33298) :  ![starts](https://img.shields.io/github/stars/MathSabo/CVE-2024-33298.svg) ![forks](https://img.shields.io/github/forks/MathSabo/CVE-2024-33298.svg)

## CVE-2024-33297
 Cross Site Scripting vulnerability in Microweber v.2.0.9 allows a remote attacker to execute arbitrary code via the campaign Name (Internal Name) field in the Add new campaign function



- [https://github.com/MathSabo/CVE-2024-33297](https://github.com/MathSabo/CVE-2024-33297) :  ![starts](https://img.shields.io/github/stars/MathSabo/CVE-2024-33297.svg) ![forks](https://img.shields.io/github/forks/MathSabo/CVE-2024-33297.svg)

## CVE-2024-33113
 D-LINK DIR-845L =v1.01KRb03 is vulnerable to Information disclosurey via bsc_sms_inbox.php.



- [https://github.com/FaLLenSKiLL1/CVE-2024-33113](https://github.com/FaLLenSKiLL1/CVE-2024-33113) :  ![starts](https://img.shields.io/github/stars/FaLLenSKiLL1/CVE-2024-33113.svg) ![forks](https://img.shields.io/github/forks/FaLLenSKiLL1/CVE-2024-33113.svg)

- [https://github.com/tekua/CVE-2024-33113](https://github.com/tekua/CVE-2024-33113) :  ![starts](https://img.shields.io/github/stars/tekua/CVE-2024-33113.svg) ![forks](https://img.shields.io/github/forks/tekua/CVE-2024-33113.svg)

## CVE-2024-33111
 D-Link DIR-845L router =v1.01KRb03 is vulnerable to Cross Site Scripting (XSS) via /htdocs/webinc/js/bsc_sms_inbox.php.



- [https://github.com/FaLLenSKiLL1/CVE-2024-33111](https://github.com/FaLLenSKiLL1/CVE-2024-33111) :  ![starts](https://img.shields.io/github/stars/FaLLenSKiLL1/CVE-2024-33111.svg) ![forks](https://img.shields.io/github/forks/FaLLenSKiLL1/CVE-2024-33111.svg)

## CVE-2024-32830
 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in ThemeKraft BuddyForms allows Server Side Request Forgery, Relative Path Traversal.This issue affects BuddyForms: from n/a through 2.8.8.



- [https://github.com/ptrstr/CVE-2024-32830-poc](https://github.com/ptrstr/CVE-2024-32830-poc) :  ![starts](https://img.shields.io/github/stars/ptrstr/CVE-2024-32830-poc.svg) ![forks](https://img.shields.io/github/forks/ptrstr/CVE-2024-32830-poc.svg)

## CVE-2024-32709
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Plechev Andrey WP-Recall.This issue affects WP-Recall: from n/a through 16.26.5.





- [https://github.com/truonghuuphuc/CVE-2024-32709-Poc](https://github.com/truonghuuphuc/CVE-2024-32709-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-32709-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-32709-Poc.svg)

## CVE-2024-32700
 Unrestricted Upload of File with Dangerous Type vulnerability in Kognetiks Kognetiks Chatbot for WordPress.This issue affects Kognetiks Chatbot for WordPress: from n/a through 2.0.0.



- [https://github.com/nastar-id/CVE-2024-32700](https://github.com/nastar-id/CVE-2024-32700) :  ![starts](https://img.shields.io/github/stars/nastar-id/CVE-2024-32700.svg) ![forks](https://img.shields.io/github/forks/nastar-id/CVE-2024-32700.svg)

## CVE-2024-32651
 changedetection.io is an open source web page change detection, website watcher, restock monitor and notification service. There is a Server Side Template Injection (SSTI) in Jinja2 that allows Remote Command Execution on the server host. Attackers can run any system command without any restriction and they could use a reverse shell. The impact is critical as the attacker can completely takeover the server machine. This can be reduced if changedetection is behind a login page, but this isn't required by the application (not by default and not enforced).



- [https://github.com/zcrosman/cve-2024-32651](https://github.com/zcrosman/cve-2024-32651) :  ![starts](https://img.shields.io/github/stars/zcrosman/cve-2024-32651.svg) ![forks](https://img.shields.io/github/forks/zcrosman/cve-2024-32651.svg)

## CVE-2024-32640
 MASA CMS is an Enterprise Content Management platform based on open source technology. Versions prior to 7.4.6, 7.3.13, and 7.2.8 contain a SQL injection vulnerability in the `processAsyncObject` method that can result in remote code execution. Versions 7.4.6, 7.3.13, and 7.2.8 contain a fix for the issue.



- [https://github.com/Stuub/CVE-2024-32640-SQLI-MuraCMS](https://github.com/Stuub/CVE-2024-32640-SQLI-MuraCMS) :  ![starts](https://img.shields.io/github/stars/Stuub/CVE-2024-32640-SQLI-MuraCMS.svg) ![forks](https://img.shields.io/github/forks/Stuub/CVE-2024-32640-SQLI-MuraCMS.svg)

- [https://github.com/pizza-power/CVE-2024-32640](https://github.com/pizza-power/CVE-2024-32640) :  ![starts](https://img.shields.io/github/stars/pizza-power/CVE-2024-32640.svg) ![forks](https://img.shields.io/github/forks/pizza-power/CVE-2024-32640.svg)

- [https://github.com/0xYumeko/CVE-2024-32640-SQLI-MuraCMS](https://github.com/0xYumeko/CVE-2024-32640-SQLI-MuraCMS) :  ![starts](https://img.shields.io/github/stars/0xYumeko/CVE-2024-32640-SQLI-MuraCMS.svg) ![forks](https://img.shields.io/github/forks/0xYumeko/CVE-2024-32640-SQLI-MuraCMS.svg)

- [https://github.com/sammings/CVE-2024-32640](https://github.com/sammings/CVE-2024-32640) :  ![starts](https://img.shields.io/github/stars/sammings/CVE-2024-32640.svg) ![forks](https://img.shields.io/github/forks/sammings/CVE-2024-32640.svg)

## CVE-2024-32523
 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in EverPress Mailster allows PHP Local File Inclusion.This issue affects Mailster: from n/a through 4.0.6.



- [https://github.com/truonghuuphuc/CVE-2024-32523-Poc](https://github.com/truonghuuphuc/CVE-2024-32523-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-32523-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-32523-Poc.svg)

## CVE-2024-32462
 Flatpak is a system for building, distributing, and running sandboxed desktop applications on Linux. in versions before 1.10.9, 1.12.9, 1.14.6, and 1.15.8, a malicious or compromised Flatpak app could execute arbitrary code outside its sandbox. Normally, the `--command` argument of `flatpak run` expects to be given a command to run in the specified Flatpak app, optionally along with some arguments. However it is possible to instead pass `bwrap` arguments to `--command=`, such as `--bind`. It's possible to pass an arbitrary `commandline` to the portal interface `org.freedesktop.portal.Background.RequestBackground` from within a Flatpak app. When this is converted into a `--command` and arguments, it achieves the same effect of passing arguments directly to `bwrap`, and thus can be used for a sandbox escape. The solution is to pass the `--` argument to `bwrap`, which makes it stop processing options. This has been supported since bubblewrap 0.3.0. All supported versions of Flatpak require at least that version of bubblewrap. xdg-desktop-portal version 1.18.4 will mitigate this vulnerability by only allowing Flatpak apps to create .desktop files for commands that do not start with --. The vulnerability is patched in 1.15.8, 1.10.9, 1.12.9, and 1.14.6.



- [https://github.com/SpiralBL0CK/CVE-2024-32462](https://github.com/SpiralBL0CK/CVE-2024-32462) :  ![starts](https://img.shields.io/github/stars/SpiralBL0CK/CVE-2024-32462.svg) ![forks](https://img.shields.io/github/forks/SpiralBL0CK/CVE-2024-32462.svg)

## CVE-2024-32459
 FreeRDP is a free implementation of the Remote Desktop Protocol. FreeRDP based clients and servers that use a version of FreeRDP prior to 3.5.0 or 2.11.6 are vulnerable to out-of-bounds read. Versions 3.5.0 and 2.11.6 patch the issue. No known workarounds are available.



- [https://github.com/absholi7ly/FreeRDP-Out-of-Bounds-Read-CVE-2024-32459-](https://github.com/absholi7ly/FreeRDP-Out-of-Bounds-Read-CVE-2024-32459-) :  ![starts](https://img.shields.io/github/stars/absholi7ly/FreeRDP-Out-of-Bounds-Read-CVE-2024-32459-.svg) ![forks](https://img.shields.io/github/forks/absholi7ly/FreeRDP-Out-of-Bounds-Read-CVE-2024-32459-.svg)

## CVE-2024-32399
 Directory Traversal vulnerability in RaidenMAILD Mail Server v.4.9.4 and before allows a remote attacker to obtain sensitive information via the /webeditor/ component.



- [https://github.com/NN0b0dy/CVE-2024-32399](https://github.com/NN0b0dy/CVE-2024-32399) :  ![starts](https://img.shields.io/github/stars/NN0b0dy/CVE-2024-32399.svg) ![forks](https://img.shields.io/github/forks/NN0b0dy/CVE-2024-32399.svg)

## CVE-2024-32371
 An issue in HSC Cybersecurity HC Mailinspector 5.2.17-3 through 5.2.18 allows a regular user account to escalate their privileges and gain administrative access by changing the type parameter from 1 to 0.



- [https://github.com/chucrutis/CVE-2024-32371](https://github.com/chucrutis/CVE-2024-32371) :  ![starts](https://img.shields.io/github/stars/chucrutis/CVE-2024-32371.svg) ![forks](https://img.shields.io/github/forks/chucrutis/CVE-2024-32371.svg)

## CVE-2024-32370
 An issue in HSC Cybersecurity HC Mailinspector 5.2.17-3 through 5.2.18 allows a remote attacker to obtain sensitive information via a crafted payload to the id parameter in the mliSystemUsers.php component.



- [https://github.com/chucrutis/CVE-2024-32370](https://github.com/chucrutis/CVE-2024-32370) :  ![starts](https://img.shields.io/github/stars/chucrutis/CVE-2024-32370.svg) ![forks](https://img.shields.io/github/forks/chucrutis/CVE-2024-32370.svg)

## CVE-2024-32369
 SQL Injection vulnerability in HSC Cybersecurity HC Mailinspector 5.2.17-3 through 5.2.18 allows a remote attacker to obtain sensitive information via a crafted payload to the start and limit parameter in the mliWhiteList.php component.



- [https://github.com/chucrutis/CVE-2024-32369](https://github.com/chucrutis/CVE-2024-32369) :  ![starts](https://img.shields.io/github/stars/chucrutis/CVE-2024-32369.svg) ![forks](https://img.shields.io/github/forks/chucrutis/CVE-2024-32369.svg)

## CVE-2024-32258
 The network server of fceux 2.7.0 has a path traversal vulnerability, allowing attackers to overwrite any files on the server without authentication by fake ROM.



- [https://github.com/secnotes/CVE-2024-32258](https://github.com/secnotes/CVE-2024-32258) :  ![starts](https://img.shields.io/github/stars/secnotes/CVE-2024-32258.svg) ![forks](https://img.shields.io/github/forks/secnotes/CVE-2024-32258.svg)

## CVE-2024-32238
 H3C ER8300G2-X is vulnerable to Incorrect Access Control. The password for the router's management system can be accessed via the management system page login interface.



- [https://github.com/FuBoLuSec/CVE-2024-32238](https://github.com/FuBoLuSec/CVE-2024-32238) :  ![starts](https://img.shields.io/github/stars/FuBoLuSec/CVE-2024-32238.svg) ![forks](https://img.shields.io/github/forks/FuBoLuSec/CVE-2024-32238.svg)

- [https://github.com/asdfjkl11/CVE-2024-32238](https://github.com/asdfjkl11/CVE-2024-32238) :  ![starts](https://img.shields.io/github/stars/asdfjkl11/CVE-2024-32238.svg) ![forks](https://img.shields.io/github/forks/asdfjkl11/CVE-2024-32238.svg)

## CVE-2024-32205
 DO NOT USE THIS CVE RECORD. ConsultIDs: none. Reason: This record was withdrawn by its CNA. Further investigation showed that it was not a security issue. Notes: none.



- [https://github.com/Lucky-lm/CVE-2024-32205](https://github.com/Lucky-lm/CVE-2024-32205) :  ![starts](https://img.shields.io/github/stars/Lucky-lm/CVE-2024-32205.svg) ![forks](https://img.shields.io/github/forks/Lucky-lm/CVE-2024-32205.svg)

## CVE-2024-32136
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Xenioushk BWL Advanced FAQ Manager.This issue affects BWL Advanced FAQ Manager: from n/a through 2.0.3.





- [https://github.com/xbz0n/CVE-2024-32136](https://github.com/xbz0n/CVE-2024-32136) :  ![starts](https://img.shields.io/github/stars/xbz0n/CVE-2024-32136.svg) ![forks](https://img.shields.io/github/forks/xbz0n/CVE-2024-32136.svg)

## CVE-2024-32113
 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache OFBiz.This issue affects Apache OFBiz: before 18.12.13.

Users are recommended to upgrade to version 18.12.13, which fixes the issue.



- [https://github.com/Mr-xn/CVE-2024-32113](https://github.com/Mr-xn/CVE-2024-32113) :  ![starts](https://img.shields.io/github/stars/Mr-xn/CVE-2024-32113.svg) ![forks](https://img.shields.io/github/forks/Mr-xn/CVE-2024-32113.svg)

- [https://github.com/RacerZ-fighting/CVE-2024-32113-POC](https://github.com/RacerZ-fighting/CVE-2024-32113-POC) :  ![starts](https://img.shields.io/github/stars/RacerZ-fighting/CVE-2024-32113-POC.svg) ![forks](https://img.shields.io/github/forks/RacerZ-fighting/CVE-2024-32113-POC.svg)

- [https://github.com/YongYe-Security/CVE-2024-32113](https://github.com/YongYe-Security/CVE-2024-32113) :  ![starts](https://img.shields.io/github/stars/YongYe-Security/CVE-2024-32113.svg) ![forks](https://img.shields.io/github/forks/YongYe-Security/CVE-2024-32113.svg)

- [https://github.com/guinea-offensive-security/Ofbiz-RCE](https://github.com/guinea-offensive-security/Ofbiz-RCE) :  ![starts](https://img.shields.io/github/stars/guinea-offensive-security/Ofbiz-RCE.svg) ![forks](https://img.shields.io/github/forks/guinea-offensive-security/Ofbiz-RCE.svg)

## CVE-2024-32104
 Cross-Site Request Forgery (CSRF) vulnerability in XLPlugins NextMove Lite.This issue affects NextMove Lite: from n/a through 2.18.1.





- [https://github.com/Cerberus-HiproPlus/CVE-2024-32104](https://github.com/Cerberus-HiproPlus/CVE-2024-32104) :  ![starts](https://img.shields.io/github/stars/Cerberus-HiproPlus/CVE-2024-32104.svg) ![forks](https://img.shields.io/github/forks/Cerberus-HiproPlus/CVE-2024-32104.svg)

## CVE-2024-32030
 Kafka UI is an Open-Source Web UI for Apache Kafka Management. Kafka UI API allows users to connect to different Kafka brokers by specifying their network address and port. As a separate feature, it also provides the ability to monitor the performance of Kafka brokers by connecting to their JMX ports. JMX is based on the RMI protocol, so it is inherently susceptible to deserialization attacks. A potential attacker can exploit this feature by connecting Kafka UI backend to its own malicious broker. This vulnerability affects the deployments where one of the following occurs: 1. dynamic.config.enabled property is set in settings. It's not enabled by default, but it's suggested to be enabled in many tutorials for Kafka UI, including its own README.md. OR  2. an attacker has access to the Kafka cluster that is being connected to Kafka UI. In this scenario the attacker can exploit this vulnerability to expand their access and execute code on Kafka UI as well. Instead of setting up a legitimate JMX port, an attacker can create an RMI listener that returns a malicious serialized object for any RMI call. In the worst case it could lead to remote code execution as Kafka UI has the required gadget chains in its classpath. This issue may lead to post-auth remote code execution. This is particularly dangerous as Kafka-UI does not have authentication enabled by default. This issue has been addressed in version 0.7.2. All users are advised to upgrade. There are no known workarounds for this vulnerability. These issues were discovered and reported by the GitHub Security lab and is also tracked as GHSL-2023-230.



- [https://github.com/huseyinstif/CVE-2024-32030-Nuclei-Template](https://github.com/huseyinstif/CVE-2024-32030-Nuclei-Template) :  ![starts](https://img.shields.io/github/stars/huseyinstif/CVE-2024-32030-Nuclei-Template.svg) ![forks](https://img.shields.io/github/forks/huseyinstif/CVE-2024-32030-Nuclei-Template.svg)

## CVE-2024-32019
 Netdata is an open source observability tool. In affected versions the `ndsudo` tool shipped with affected versions of the Netdata Agent allows an attacker to run arbitrary programs with root permissions. The `ndsudo` tool is packaged as a `root`-owned executable with the SUID bit set. It only runs a restricted set of external commands, but its search paths are supplied by the `PATH` environment variable. This allows an attacker to control where `ndsudo` looks for these commands, which may be a path the attacker has write access to. This may lead to local privilege escalation. This vulnerability has been addressed in versions 1.45.3 and 1.45.2-169. Users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/AzureADTrent/CVE-2024-32019-POC](https://github.com/AzureADTrent/CVE-2024-32019-POC) :  ![starts](https://img.shields.io/github/stars/AzureADTrent/CVE-2024-32019-POC.svg) ![forks](https://img.shields.io/github/forks/AzureADTrent/CVE-2024-32019-POC.svg)

- [https://github.com/AliElKhatteb/CVE-2024-32019-POC](https://github.com/AliElKhatteb/CVE-2024-32019-POC) :  ![starts](https://img.shields.io/github/stars/AliElKhatteb/CVE-2024-32019-POC.svg) ![forks](https://img.shields.io/github/forks/AliElKhatteb/CVE-2024-32019-POC.svg)

## CVE-2024-32004
 Git is a revision control system. Prior to versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4, an attacker can prepare a local repository in such a way that, when cloned, will execute arbitrary code during the operation. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4. As a workaround, avoid cloning repositories from untrusted sources.



- [https://github.com/Wadewfsssss/CVE-2024-32004](https://github.com/Wadewfsssss/CVE-2024-32004) :  ![starts](https://img.shields.io/github/stars/Wadewfsssss/CVE-2024-32004.svg) ![forks](https://img.shields.io/github/forks/Wadewfsssss/CVE-2024-32004.svg)

- [https://github.com/10cks/CVE-2024-32004-POC](https://github.com/10cks/CVE-2024-32004-POC) :  ![starts](https://img.shields.io/github/stars/10cks/CVE-2024-32004-POC.svg) ![forks](https://img.shields.io/github/forks/10cks/CVE-2024-32004-POC.svg)

## CVE-2024-32002
 Git is a revision control system. Prior to versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4, repositories with submodules can be crafted in a way that exploits a bug in Git whereby it can be fooled into writing files not into the submodule's worktree but into a `.git/` directory. This allows writing a hook that will be executed while the clone operation is still running, giving the user no opportunity to inspect the code that is being executed. The problem has been patched in versions 2.45.1, 2.44.1, 2.43.4, 2.42.2, 2.41.1, 2.40.2, and 2.39.4. If symbolic link support is disabled in Git (e.g. via `git config --global core.symlinks false`), the described attack won't work. As always, it is best to avoid cloning repositories from untrusted sources.



- [https://github.com/amalmurali47/git_rce](https://github.com/amalmurali47/git_rce) :  ![starts](https://img.shields.io/github/stars/amalmurali47/git_rce.svg) ![forks](https://img.shields.io/github/forks/amalmurali47/git_rce.svg)

- [https://github.com/safebuffer/CVE-2024-32002](https://github.com/safebuffer/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/safebuffer/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/safebuffer/CVE-2024-32002.svg)

- [https://github.com/amalmurali47/hook](https://github.com/amalmurali47/hook) :  ![starts](https://img.shields.io/github/stars/amalmurali47/hook.svg) ![forks](https://img.shields.io/github/forks/amalmurali47/hook.svg)

- [https://github.com/M507/CVE-2024-32002](https://github.com/M507/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/M507/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/M507/CVE-2024-32002.svg)

- [https://github.com/YukaFake/CVE-2024-32002-Reverse-Shell](https://github.com/YukaFake/CVE-2024-32002-Reverse-Shell) :  ![starts](https://img.shields.io/github/stars/YukaFake/CVE-2024-32002-Reverse-Shell.svg) ![forks](https://img.shields.io/github/forks/YukaFake/CVE-2024-32002-Reverse-Shell.svg)

- [https://github.com/jweny/CVE-2024-32002_EXP](https://github.com/jweny/CVE-2024-32002_EXP) :  ![starts](https://img.shields.io/github/stars/jweny/CVE-2024-32002_EXP.svg) ![forks](https://img.shields.io/github/forks/jweny/CVE-2024-32002_EXP.svg)

- [https://github.com/jweny/CVE-2024-32002_HOOK](https://github.com/jweny/CVE-2024-32002_HOOK) :  ![starts](https://img.shields.io/github/stars/jweny/CVE-2024-32002_HOOK.svg) ![forks](https://img.shields.io/github/forks/jweny/CVE-2024-32002_HOOK.svg)

- [https://github.com/XiaomingX/cve-2024-32002-poc](https://github.com/XiaomingX/cve-2024-32002-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-32002-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-32002-poc.svg)

- [https://github.com/NishanthAnand21/CVE-2024-32002-PoC](https://github.com/NishanthAnand21/CVE-2024-32002-PoC) :  ![starts](https://img.shields.io/github/stars/NishanthAnand21/CVE-2024-32002-PoC.svg) ![forks](https://img.shields.io/github/forks/NishanthAnand21/CVE-2024-32002-PoC.svg)

- [https://github.com/markuta/CVE-2024-32002](https://github.com/markuta/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/markuta/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/markuta/CVE-2024-32002.svg)

- [https://github.com/bfengj/CVE-2024-32002-Exploit](https://github.com/bfengj/CVE-2024-32002-Exploit) :  ![starts](https://img.shields.io/github/stars/bfengj/CVE-2024-32002-Exploit.svg) ![forks](https://img.shields.io/github/forks/bfengj/CVE-2024-32002-Exploit.svg)

- [https://github.com/10cks/CVE-2024-32002-EXP](https://github.com/10cks/CVE-2024-32002-EXP) :  ![starts](https://img.shields.io/github/stars/10cks/CVE-2024-32002-EXP.svg) ![forks](https://img.shields.io/github/forks/10cks/CVE-2024-32002-EXP.svg)

- [https://github.com/Basyaact/CVE-2024-32002-PoC_Chinese](https://github.com/Basyaact/CVE-2024-32002-PoC_Chinese) :  ![starts](https://img.shields.io/github/stars/Basyaact/CVE-2024-32002-PoC_Chinese.svg) ![forks](https://img.shields.io/github/forks/Basyaact/CVE-2024-32002-PoC_Chinese.svg)

- [https://github.com/10cks/hook](https://github.com/10cks/hook) :  ![starts](https://img.shields.io/github/stars/10cks/hook.svg) ![forks](https://img.shields.io/github/forks/10cks/hook.svg)

- [https://github.com/CrackerCat/CVE-2024-32002_EXP](https://github.com/CrackerCat/CVE-2024-32002_EXP) :  ![starts](https://img.shields.io/github/stars/CrackerCat/CVE-2024-32002_EXP.svg) ![forks](https://img.shields.io/github/forks/CrackerCat/CVE-2024-32002_EXP.svg)

- [https://github.com/fadhilthomas/poc-cve-2024-32002](https://github.com/fadhilthomas/poc-cve-2024-32002) :  ![starts](https://img.shields.io/github/stars/fadhilthomas/poc-cve-2024-32002.svg) ![forks](https://img.shields.io/github/forks/fadhilthomas/poc-cve-2024-32002.svg)

- [https://github.com/Goplush/CVE-2024-32002-git-rce](https://github.com/Goplush/CVE-2024-32002-git-rce) :  ![starts](https://img.shields.io/github/stars/Goplush/CVE-2024-32002-git-rce.svg) ![forks](https://img.shields.io/github/forks/Goplush/CVE-2024-32002-git-rce.svg)

- [https://github.com/JakobTheDev/cve-2024-32002-poc-rce](https://github.com/JakobTheDev/cve-2024-32002-poc-rce) :  ![starts](https://img.shields.io/github/stars/JakobTheDev/cve-2024-32002-poc-rce.svg) ![forks](https://img.shields.io/github/forks/JakobTheDev/cve-2024-32002-poc-rce.svg)

- [https://github.com/LoongBa/ReplaceAllGit](https://github.com/LoongBa/ReplaceAllGit) :  ![starts](https://img.shields.io/github/stars/LoongBa/ReplaceAllGit.svg) ![forks](https://img.shields.io/github/forks/LoongBa/ReplaceAllGit.svg)

- [https://github.com/Dre4m017/fuzzy](https://github.com/Dre4m017/fuzzy) :  ![starts](https://img.shields.io/github/stars/Dre4m017/fuzzy.svg) ![forks](https://img.shields.io/github/forks/Dre4m017/fuzzy.svg)

- [https://github.com/vincepsh/CVE-2024-32002-hook](https://github.com/vincepsh/CVE-2024-32002-hook) :  ![starts](https://img.shields.io/github/stars/vincepsh/CVE-2024-32002-hook.svg) ![forks](https://img.shields.io/github/forks/vincepsh/CVE-2024-32002-hook.svg)

- [https://github.com/Roronoawjd/git_rce](https://github.com/Roronoawjd/git_rce) :  ![starts](https://img.shields.io/github/stars/Roronoawjd/git_rce.svg) ![forks](https://img.shields.io/github/forks/Roronoawjd/git_rce.svg)

- [https://github.com/charlesgargasson/CVE-2024-32002](https://github.com/charlesgargasson/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/charlesgargasson/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/charlesgargasson/CVE-2024-32002.svg)

- [https://github.com/bonnettheo/CVE-2024-32002](https://github.com/bonnettheo/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/bonnettheo/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/bonnettheo/CVE-2024-32002.svg)

- [https://github.com/431m/rcetest](https://github.com/431m/rcetest) :  ![starts](https://img.shields.io/github/stars/431m/rcetest.svg) ![forks](https://img.shields.io/github/forks/431m/rcetest.svg)

- [https://github.com/AD-Appledog/CVE-2024-32002](https://github.com/AD-Appledog/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/AD-Appledog/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/AD-Appledog/CVE-2024-32002.svg)

- [https://github.com/vincepsh/CVE-2024-32002](https://github.com/vincepsh/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/vincepsh/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/vincepsh/CVE-2024-32002.svg)

- [https://github.com/blackninja23/CVE-2024-32002](https://github.com/blackninja23/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/blackninja23/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/blackninja23/CVE-2024-32002.svg)

- [https://github.com/WOOOOONG/CVE-2024-32002](https://github.com/WOOOOONG/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/WOOOOONG/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/WOOOOONG/CVE-2024-32002.svg)

- [https://github.com/daemon-reconfig/CVE-2024-32002](https://github.com/daemon-reconfig/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/daemon-reconfig/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/daemon-reconfig/CVE-2024-32002.svg)

- [https://github.com/tobelight/cve_2024_32002](https://github.com/tobelight/cve_2024_32002) :  ![starts](https://img.shields.io/github/stars/tobelight/cve_2024_32002.svg) ![forks](https://img.shields.io/github/forks/tobelight/cve_2024_32002.svg)

- [https://github.com/YukaFake/CVE-2024-32002](https://github.com/YukaFake/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/YukaFake/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/YukaFake/CVE-2024-32002.svg)

- [https://github.com/FlojBoj/CVE-2024-32002](https://github.com/FlojBoj/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/FlojBoj/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/FlojBoj/CVE-2024-32002.svg)

- [https://github.com/SpycioKon/CVE-2024-32002](https://github.com/SpycioKon/CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/SpycioKon/CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/SpycioKon/CVE-2024-32002.svg)

- [https://github.com/1mxml/CVE-2024-32002-poc](https://github.com/1mxml/CVE-2024-32002-poc) :  ![starts](https://img.shields.io/github/stars/1mxml/CVE-2024-32002-poc.svg) ![forks](https://img.shields.io/github/forks/1mxml/CVE-2024-32002-poc.svg)

- [https://github.com/10cks/CVE-2024-32002-POC](https://github.com/10cks/CVE-2024-32002-POC) :  ![starts](https://img.shields.io/github/stars/10cks/CVE-2024-32002-POC.svg) ![forks](https://img.shields.io/github/forks/10cks/CVE-2024-32002-POC.svg)

- [https://github.com/bfengj/CVE-2024-32002-hook](https://github.com/bfengj/CVE-2024-32002-hook) :  ![starts](https://img.shields.io/github/stars/bfengj/CVE-2024-32002-hook.svg) ![forks](https://img.shields.io/github/forks/bfengj/CVE-2024-32002-hook.svg)

- [https://github.com/Roronoawjd/hook](https://github.com/Roronoawjd/hook) :  ![starts](https://img.shields.io/github/stars/Roronoawjd/hook.svg) ![forks](https://img.shields.io/github/forks/Roronoawjd/hook.svg)

- [https://github.com/10cks/CVE-2024-32002-submod](https://github.com/10cks/CVE-2024-32002-submod) :  ![starts](https://img.shields.io/github/stars/10cks/CVE-2024-32002-submod.svg) ![forks](https://img.shields.io/github/forks/10cks/CVE-2024-32002-submod.svg)

- [https://github.com/10cks/CVE-2024-32002-hulk](https://github.com/10cks/CVE-2024-32002-hulk) :  ![starts](https://img.shields.io/github/stars/10cks/CVE-2024-32002-hulk.svg) ![forks](https://img.shields.io/github/forks/10cks/CVE-2024-32002-hulk.svg)

- [https://github.com/fadhilthomas/hook](https://github.com/fadhilthomas/hook) :  ![starts](https://img.shields.io/github/stars/fadhilthomas/hook.svg) ![forks](https://img.shields.io/github/forks/fadhilthomas/hook.svg)

- [https://github.com/WOOOOONG/hook](https://github.com/WOOOOONG/hook) :  ![starts](https://img.shields.io/github/stars/WOOOOONG/hook.svg) ![forks](https://img.shields.io/github/forks/WOOOOONG/hook.svg)

- [https://github.com/sysonlai/CVE-2024-32002-hook](https://github.com/sysonlai/CVE-2024-32002-hook) :  ![starts](https://img.shields.io/github/stars/sysonlai/CVE-2024-32002-hook.svg) ![forks](https://img.shields.io/github/forks/sysonlai/CVE-2024-32002-hook.svg)

- [https://github.com/tobelight/cve_2024_32002_hook](https://github.com/tobelight/cve_2024_32002_hook) :  ![starts](https://img.shields.io/github/stars/tobelight/cve_2024_32002_hook.svg) ![forks](https://img.shields.io/github/forks/tobelight/cve_2024_32002_hook.svg)

- [https://github.com/aitorcastel/poc_CVE-2024-32002](https://github.com/aitorcastel/poc_CVE-2024-32002) :  ![starts](https://img.shields.io/github/stars/aitorcastel/poc_CVE-2024-32002.svg) ![forks](https://img.shields.io/github/forks/aitorcastel/poc_CVE-2024-32002.svg)

- [https://github.com/10cks/CVE-2024-32002-smash](https://github.com/10cks/CVE-2024-32002-smash) :  ![starts](https://img.shields.io/github/stars/10cks/CVE-2024-32002-smash.svg) ![forks](https://img.shields.io/github/forks/10cks/CVE-2024-32002-smash.svg)

- [https://github.com/10cks/CVE-2024-32002-linux-submod](https://github.com/10cks/CVE-2024-32002-linux-submod) :  ![starts](https://img.shields.io/github/stars/10cks/CVE-2024-32002-linux-submod.svg) ![forks](https://img.shields.io/github/forks/10cks/CVE-2024-32002-linux-submod.svg)

- [https://github.com/TSY244/CVE-2024-32002-git-rce](https://github.com/TSY244/CVE-2024-32002-git-rce) :  ![starts](https://img.shields.io/github/stars/TSY244/CVE-2024-32002-git-rce.svg) ![forks](https://img.shields.io/github/forks/TSY244/CVE-2024-32002-git-rce.svg)

- [https://github.com/10cks/CVE-2024-32002-linux-hulk](https://github.com/10cks/CVE-2024-32002-linux-hulk) :  ![starts](https://img.shields.io/github/stars/10cks/CVE-2024-32002-linux-hulk.svg) ![forks](https://img.shields.io/github/forks/10cks/CVE-2024-32002-linux-hulk.svg)

- [https://github.com/JakobTheDev/cve-2024-32002-submodule-aw](https://github.com/JakobTheDev/cve-2024-32002-submodule-aw) :  ![starts](https://img.shields.io/github/stars/JakobTheDev/cve-2024-32002-submodule-aw.svg) ![forks](https://img.shields.io/github/forks/JakobTheDev/cve-2024-32002-submodule-aw.svg)

- [https://github.com/JakobTheDev/cve-2024-32002-submodule-rce](https://github.com/JakobTheDev/cve-2024-32002-submodule-rce) :  ![starts](https://img.shields.io/github/stars/JakobTheDev/cve-2024-32002-submodule-rce.svg) ![forks](https://img.shields.io/github/forks/JakobTheDev/cve-2024-32002-submodule-rce.svg)

- [https://github.com/JakobTheDev/cve-2024-32002-poc-aw](https://github.com/JakobTheDev/cve-2024-32002-poc-aw) :  ![starts](https://img.shields.io/github/stars/JakobTheDev/cve-2024-32002-poc-aw.svg) ![forks](https://img.shields.io/github/forks/JakobTheDev/cve-2024-32002-poc-aw.svg)

- [https://github.com/10cks/CVE-2024-32002-linux-smash](https://github.com/10cks/CVE-2024-32002-linux-smash) :  ![starts](https://img.shields.io/github/stars/10cks/CVE-2024-32002-linux-smash.svg) ![forks](https://img.shields.io/github/forks/10cks/CVE-2024-32002-linux-smash.svg)

- [https://github.com/aitorcastel/poc_CVE-2024-32002_submodule](https://github.com/aitorcastel/poc_CVE-2024-32002_submodule) :  ![starts](https://img.shields.io/github/stars/aitorcastel/poc_CVE-2024-32002_submodule.svg) ![forks](https://img.shields.io/github/forks/aitorcastel/poc_CVE-2024-32002_submodule.svg)

- [https://github.com/markuta/hooky](https://github.com/markuta/hooky) :  ![starts](https://img.shields.io/github/stars/markuta/hooky.svg) ![forks](https://img.shields.io/github/forks/markuta/hooky.svg)

- [https://github.com/TSY244/CVE-2024-32002-git-rce-father-poc](https://github.com/TSY244/CVE-2024-32002-git-rce-father-poc) :  ![starts](https://img.shields.io/github/stars/TSY244/CVE-2024-32002-git-rce-father-poc.svg) ![forks](https://img.shields.io/github/forks/TSY244/CVE-2024-32002-git-rce-father-poc.svg)

- [https://github.com/chrisWalker11/running-CVE-2024-32002-locally-for-tesing](https://github.com/chrisWalker11/running-CVE-2024-32002-locally-for-tesing) :  ![starts](https://img.shields.io/github/stars/chrisWalker11/running-CVE-2024-32002-locally-for-tesing.svg) ![forks](https://img.shields.io/github/forks/chrisWalker11/running-CVE-2024-32002-locally-for-tesing.svg)

- [https://github.com/sreevatsa1997/test_cve_32002](https://github.com/sreevatsa1997/test_cve_32002) :  ![starts](https://img.shields.io/github/stars/sreevatsa1997/test_cve_32002.svg) ![forks](https://img.shields.io/github/forks/sreevatsa1997/test_cve_32002.svg)

- [https://github.com/jolibb55/donald](https://github.com/jolibb55/donald) :  ![starts](https://img.shields.io/github/stars/jolibb55/donald.svg) ![forks](https://img.shields.io/github/forks/jolibb55/donald.svg)

- [https://github.com/YukaFake/malicious-hook](https://github.com/YukaFake/malicious-hook) :  ![starts](https://img.shields.io/github/stars/YukaFake/malicious-hook.svg) ![forks](https://img.shields.io/github/forks/YukaFake/malicious-hook.svg)

## CVE-2024-31989
 Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. It has been discovered that an unprivileged pod in a different namespace on the same cluster could connect to the Redis server on port 6379. Despite having installed the latest version of the VPC CNI plugin on the EKS cluster, it requires manual enablement through configuration to enforce network policies. This raises concerns that many clients might unknowingly have open access to their Redis servers. This vulnerability could lead to Privilege Escalation to the level of cluster controller, or to information leakage, affecting anyone who does not have strict access controls on their Redis instance. This issue has been patched in version(s) 2.8.19, 2.9.15 and 2.10.10.



- [https://github.com/vt0x78/CVE-2024-31989](https://github.com/vt0x78/CVE-2024-31989) :  ![starts](https://img.shields.io/github/stars/vt0x78/CVE-2024-31989.svg) ![forks](https://img.shields.io/github/forks/vt0x78/CVE-2024-31989.svg)

## CVE-2024-31982
 XWiki Platform is a generic wiki platform. Starting in version 2.4-milestone-1 and prior to versions 4.10.20, 15.5.4, and 15.10-rc-1, XWiki's database search allows remote code execution through the search text. This allows remote code execution for any visitor of a public wiki or user of a closed wiki as the database search is by default accessible for all users. This impacts the confidentiality, integrity and availability of the whole XWiki installation. This vulnerability has been patched in XWiki 14.10.20, 15.5.4 and 15.10RC1. As a workaround, one may manually apply the patch to the page `Main.DatabaseSearch`. Alternatively, unless database search is explicitly used by users, this page can be deleted as this is not the default search interface of XWiki.



- [https://github.com/bigb0x/CVE-2024-31982](https://github.com/bigb0x/CVE-2024-31982) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-31982.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-31982.svg)

- [https://github.com/NanoWraith/CVE-2024-31982](https://github.com/NanoWraith/CVE-2024-31982) :  ![starts](https://img.shields.io/github/stars/NanoWraith/CVE-2024-31982.svg) ![forks](https://img.shields.io/github/forks/NanoWraith/CVE-2024-31982.svg)

- [https://github.com/th3gokul/CVE-2024-31982](https://github.com/th3gokul/CVE-2024-31982) :  ![starts](https://img.shields.io/github/stars/th3gokul/CVE-2024-31982.svg) ![forks](https://img.shields.io/github/forks/th3gokul/CVE-2024-31982.svg)

## CVE-2024-31977
 Adtran 834-5 11.1.0.101-202106231430, and fixed as of SmartOS Version 12.6.3.1, devices allow OS Command Injection via shell metacharacters to the Ping or Traceroute utility.



- [https://github.com/actuator/BSIDES-Security-Las-Vegas-2024](https://github.com/actuator/BSIDES-Security-Las-Vegas-2024) :  ![starts](https://img.shields.io/github/stars/actuator/BSIDES-Security-Las-Vegas-2024.svg) ![forks](https://img.shields.io/github/forks/actuator/BSIDES-Security-Las-Vegas-2024.svg)

## CVE-2024-31974
 The com.solarized.firedown (aka Solarized FireDown Browser & Downloader) application 1.0.76 for Android allows a remote attacker to execute arbitrary JavaScript code via a crafted intent. com.solarized.firedown.IntentActivity uses a WebView component to display web content and doesn't adequately sanitize the URI or any extra data passed in the intent by any installed application (with no permissions).



- [https://github.com/actuator/com.solarized.firedown](https://github.com/actuator/com.solarized.firedown) :  ![starts](https://img.shields.io/github/stars/actuator/com.solarized.firedown.svg) ![forks](https://img.shields.io/github/forks/actuator/com.solarized.firedown.svg)

## CVE-2024-31971
 Multiple stored cross-site scripting (XSS) vulnerabilities on AdTran NetVanta 3120 18.01.01.00.E devices allow remote attackers to inject arbitrary JavaScript, as demonstrated by /mainPassword.html, /processIdentity.html, /public.html, /dhcp.html, /private.html, /hostname.html, /connectivity.html, /NetworkMonitor.html, /trafficMonitoringConfig.html, and /wizardMain.html.



- [https://github.com/actuator/BSIDES-Security-Las-Vegas-2024](https://github.com/actuator/BSIDES-Security-Las-Vegas-2024) :  ![starts](https://img.shields.io/github/stars/actuator/BSIDES-Security-Las-Vegas-2024.svg) ![forks](https://img.shields.io/github/forks/actuator/BSIDES-Security-Las-Vegas-2024.svg)

## CVE-2024-31970
 AdTran SRG 834-5 HDC17600021F1 devices (with SmartOS 11.1.1.1 and fixed in Version 12.1.3.1) have SSH enabled by default, accessible both over the LAN and the Internet. During a window of time when the device is being set up, it uses a default username and password combination of admin/admin with root-level privileges. An attacker can exploit this window to gain unauthorized root access by either modifying the existing admin account or creating a new account with equivalent privileges. This vulnerability allows attackers to execute arbitrary commands. NOTE: The vendor has disputed this, finding the report not applicable. According to AdTran, SSH has never been accessible (from WAN) on SmartOS official builds. Furthermore, the vendor adds that test build 11.1.0.101-202106231430 was never released to end users.



- [https://github.com/actuator/BSIDES-Security-Las-Vegas-2024](https://github.com/actuator/BSIDES-Security-Las-Vegas-2024) :  ![starts](https://img.shields.io/github/stars/actuator/BSIDES-Security-Las-Vegas-2024.svg) ![forks](https://img.shields.io/github/forks/actuator/BSIDES-Security-Las-Vegas-2024.svg)

## CVE-2024-31964
 A vulnerability on Mitel 6800 Series and 6900 Series SIP Phones through 6.3 SP3 HF4, 6900w Series SIP Phone through 6.3.3, and 6970 Conference Unit through 5.1.1 SP8 allows an unauthenticated attacker to conduct an authentication bypass attack due to improper authentication control. A successful exploit could allow an attacker to modify system configuration settings and potentially cause a denial of service.



- [https://github.com/d-Raco/CVE-2024-31964](https://github.com/d-Raco/CVE-2024-31964) :  ![starts](https://img.shields.io/github/stars/d-Raco/CVE-2024-31964.svg) ![forks](https://img.shields.io/github/forks/d-Raco/CVE-2024-31964.svg)

## CVE-2024-31851
 A path traversal vulnerability exists in the Java version of CData Sync  23.4.8843 when running using the embedded Jetty server, which could allow an unauthenticated remote attacker to gain access to sensitive information and perform limited actions.



- [https://github.com/Stuub/CVE-2024-31848-PoC](https://github.com/Stuub/CVE-2024-31848-PoC) :  ![starts](https://img.shields.io/github/stars/Stuub/CVE-2024-31848-PoC.svg) ![forks](https://img.shields.io/github/forks/Stuub/CVE-2024-31848-PoC.svg)

## CVE-2024-31850
 A path traversal vulnerability exists in the Java version of CData Arc  23.4.8839 when running using the embedded Jetty server, which could allow an unauthenticated remote attacker to gain access to sensitive information and perform limited actions.



- [https://github.com/Stuub/CVE-2024-31848-PoC](https://github.com/Stuub/CVE-2024-31848-PoC) :  ![starts](https://img.shields.io/github/stars/Stuub/CVE-2024-31848-PoC.svg) ![forks](https://img.shields.io/github/forks/Stuub/CVE-2024-31848-PoC.svg)

## CVE-2024-31849
 A path traversal vulnerability exists in the Java version of CData Connect  23.4.8846 when running using the embedded Jetty server, which could allow an unauthenticated remote attacker to gain complete administrative access to the application.



- [https://github.com/Stuub/CVE-2024-31848-PoC](https://github.com/Stuub/CVE-2024-31848-PoC) :  ![starts](https://img.shields.io/github/stars/Stuub/CVE-2024-31848-PoC.svg) ![forks](https://img.shields.io/github/forks/Stuub/CVE-2024-31848-PoC.svg)

## CVE-2024-31848
 A path traversal vulnerability exists in the Java version of CData API Server  23.4.8844 when running using the embedded Jetty server, which could allow an unauthenticated remote attacker to gain complete administrative access to the application.



- [https://github.com/Stuub/CVE-2024-31848-PoC](https://github.com/Stuub/CVE-2024-31848-PoC) :  ![starts](https://img.shields.io/github/stars/Stuub/CVE-2024-31848-PoC.svg) ![forks](https://img.shields.io/github/forks/Stuub/CVE-2024-31848-PoC.svg)

## CVE-2024-31819
 An issue in WWBN AVideo v.12.4 through v.14.2 allows a remote attacker to execute arbitrary code via the systemRootPath parameter of the submitIndex.php component.



- [https://github.com/Chocapikk/CVE-2024-31819](https://github.com/Chocapikk/CVE-2024-31819) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-31819.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-31819.svg)

- [https://github.com/dream434/CVE-2024-31819](https://github.com/dream434/CVE-2024-31819) :  ![starts](https://img.shields.io/github/stars/dream434/CVE-2024-31819.svg) ![forks](https://img.shields.io/github/forks/dream434/CVE-2024-31819.svg)

## CVE-2024-31777
 File Upload vulnerability in openeclass v.3.15 and before allows an attacker to execute arbitrary code via a crafted file to the certbadge.php endpoint.



- [https://github.com/FreySolarEye/Exploit-CVE-2024-31777](https://github.com/FreySolarEye/Exploit-CVE-2024-31777) :  ![starts](https://img.shields.io/github/stars/FreySolarEye/Exploit-CVE-2024-31777.svg) ![forks](https://img.shields.io/github/forks/FreySolarEye/Exploit-CVE-2024-31777.svg)

## CVE-2024-31771
 Insecure Permission vulnerability in TotalAV v.6.0.740 allows a local attacker to escalate privileges via a crafted file



- [https://github.com/restdone/CVE-2024-31771](https://github.com/restdone/CVE-2024-31771) :  ![starts](https://img.shields.io/github/stars/restdone/CVE-2024-31771.svg) ![forks](https://img.shields.io/github/forks/restdone/CVE-2024-31771.svg)

## CVE-2024-31719
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/VoltaireYoung/CVE-2024-31719----AMI-Aptio-5-Vulnerability](https://github.com/VoltaireYoung/CVE-2024-31719----AMI-Aptio-5-Vulnerability) :  ![starts](https://img.shields.io/github/stars/VoltaireYoung/CVE-2024-31719----AMI-Aptio-5-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/VoltaireYoung/CVE-2024-31719----AMI-Aptio-5-Vulnerability.svg)

## CVE-2024-31666
 An issue in flusity-CMS v.2.33 allows a remote attacker to execute arbitrary code via a crafted script to the edit_addon_post.php component.



- [https://github.com/hapa3/CVE-2024-31666](https://github.com/hapa3/CVE-2024-31666) :  ![starts](https://img.shields.io/github/stars/hapa3/CVE-2024-31666.svg) ![forks](https://img.shields.io/github/forks/hapa3/CVE-2024-31666.svg)

## CVE-2024-31497
 In PuTTY 0.68 through 0.80 before 0.81, biased ECDSA nonce generation allows an attacker to recover a user's NIST P-521 secret key via a quick attack in approximately 60 signatures. This is especially important in a scenario where an adversary is able to read messages signed by PuTTY or Pageant. The required set of signed messages may be publicly readable because they are stored in a public Git service that supports use of SSH for commit signing, and the signatures were made by Pageant through an agent-forwarding mechanism. In other words, an adversary may already have enough signature information to compromise a victim's private key, even if there is no further use of vulnerable PuTTY versions. After a key compromise, an adversary may be able to conduct supply-chain attacks on software maintained in Git. A second, independent scenario is that the adversary is an operator of an SSH server to which the victim authenticates (for remote login or file copy), even though this server is not fully trusted by the victim, and the victim uses the same private key for SSH connections to other services operated by other entities. Here, the rogue server operator (who would otherwise have no way to determine the victim's private key) can derive the victim's private key, and then use it for unauthorized access to those other services. If the other services include Git services, then again it may be possible to conduct supply-chain attacks on software maintained in Git. This also affects, for example, FileZilla before 3.67.0, WinSCP before 6.3.3, TortoiseGit before 2.15.0.1, and TortoiseSVN through 1.14.6.



- [https://github.com/HugoBond/CVE-2024-31497-POC](https://github.com/HugoBond/CVE-2024-31497-POC) :  ![starts](https://img.shields.io/github/stars/HugoBond/CVE-2024-31497-POC.svg) ![forks](https://img.shields.io/github/forks/HugoBond/CVE-2024-31497-POC.svg)

- [https://github.com/edutko/cve-2024-31497](https://github.com/edutko/cve-2024-31497) :  ![starts](https://img.shields.io/github/stars/edutko/cve-2024-31497.svg) ![forks](https://img.shields.io/github/forks/edutko/cve-2024-31497.svg)

- [https://github.com/sh1k4ku/CVE-2024-31497](https://github.com/sh1k4ku/CVE-2024-31497) :  ![starts](https://img.shields.io/github/stars/sh1k4ku/CVE-2024-31497.svg) ![forks](https://img.shields.io/github/forks/sh1k4ku/CVE-2024-31497.svg)

- [https://github.com/RUB-NDS/SSH-Client-Signatures-Artifacts](https://github.com/RUB-NDS/SSH-Client-Signatures-Artifacts) :  ![starts](https://img.shields.io/github/stars/RUB-NDS/SSH-Client-Signatures-Artifacts.svg) ![forks](https://img.shields.io/github/forks/RUB-NDS/SSH-Client-Signatures-Artifacts.svg)

## CVE-2024-31449
 Redis is an open source, in-memory database that persists on disk. An authenticated user may use a specially crafted Lua script to trigger a stack buffer overflow in the bit library, which may potentially lead to remote code execution. The problem exists in all versions of Redis with Lua scripting. This problem has been fixed in Redis versions 6.2.16, 7.2.6, and 7.4.1. Users are advised to upgrade. There are no known workarounds for this vulnerability.



- [https://github.com/daeseong1209/CVE-2024-31449](https://github.com/daeseong1209/CVE-2024-31449) :  ![starts](https://img.shields.io/github/stars/daeseong1209/CVE-2024-31449.svg) ![forks](https://img.shields.io/github/forks/daeseong1209/CVE-2024-31449.svg)

## CVE-2024-31351
 Unrestricted Upload of File with Dangerous Type vulnerability in Copymatic Copymatic – AI Content Writer & Generator.This issue affects Copymatic – AI Content Writer & Generator: from n/a through 1.6.



- [https://github.com/KTN1990/CVE-2024-31351_wordpress_exploit](https://github.com/KTN1990/CVE-2024-31351_wordpress_exploit) :  ![starts](https://img.shields.io/github/stars/KTN1990/CVE-2024-31351_wordpress_exploit.svg) ![forks](https://img.shields.io/github/forks/KTN1990/CVE-2024-31351_wordpress_exploit.svg)

## CVE-2024-31317
 In multiple functions of ZygoteProcess.java, there is a possible way to achieve code execution as any app via WRITE_SECURE_SETTINGS due to unsafe deserialization. This could lead to local escalation of privilege with User execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/fuhei/CVE-2024-31317](https://github.com/fuhei/CVE-2024-31317) :  ![starts](https://img.shields.io/github/stars/fuhei/CVE-2024-31317.svg) ![forks](https://img.shields.io/github/forks/fuhei/CVE-2024-31317.svg)

- [https://github.com/Anonymous941/zygote-injection-toolkit](https://github.com/Anonymous941/zygote-injection-toolkit) :  ![starts](https://img.shields.io/github/stars/Anonymous941/zygote-injection-toolkit.svg) ![forks](https://img.shields.io/github/forks/Anonymous941/zygote-injection-toolkit.svg)

- [https://github.com/WebLDix/CVE-2024-31317-PoC-Deployer](https://github.com/WebLDix/CVE-2024-31317-PoC-Deployer) :  ![starts](https://img.shields.io/github/stars/WebLDix/CVE-2024-31317-PoC-Deployer.svg) ![forks](https://img.shields.io/github/forks/WebLDix/CVE-2024-31317-PoC-Deployer.svg)

- [https://github.com/agg23/cve-2024-31317](https://github.com/agg23/cve-2024-31317) :  ![starts](https://img.shields.io/github/stars/agg23/cve-2024-31317.svg) ![forks](https://img.shields.io/github/forks/agg23/cve-2024-31317.svg)

- [https://github.com/mianliupindao/CVE-2024-31317-PoC-Deployer](https://github.com/mianliupindao/CVE-2024-31317-PoC-Deployer) :  ![starts](https://img.shields.io/github/stars/mianliupindao/CVE-2024-31317-PoC-Deployer.svg) ![forks](https://img.shields.io/github/forks/mianliupindao/CVE-2024-31317-PoC-Deployer.svg)

- [https://github.com/rifting/Zygotroller](https://github.com/rifting/Zygotroller) :  ![starts](https://img.shields.io/github/stars/rifting/Zygotroller.svg) ![forks](https://img.shields.io/github/forks/rifting/Zygotroller.svg)

## CVE-2024-31309
 HTTP/2 CONTINUATION DoS attack can cause Apache Traffic Server to consume more resources on the server.  Version from 8.0.0 through 8.1.9, from 9.0.0 through 9.2.3 are affected.

Users can set a new setting (proxy.config.http2.max_continuation_frames_per_minute) to limit the number of CONTINUATION frames per minute.  ATS does have a fixed amount of memory a request can use and ATS adheres to these limits in previous releases.
Users are recommended to upgrade to versions 8.1.10 or 9.2.4 which fixes the issue.



- [https://github.com/lockness-Ko/CVE-2024-27316](https://github.com/lockness-Ko/CVE-2024-27316) :  ![starts](https://img.shields.io/github/stars/lockness-Ko/CVE-2024-27316.svg) ![forks](https://img.shields.io/github/forks/lockness-Ko/CVE-2024-27316.svg)

## CVE-2024-31211
 WordPress is an open publishing platform for the Web. Unserialization of instances of the `WP_HTML_Token` class allows for code execution via its `__destruct()` magic method. This issue was fixed in WordPress 6.4.2 on December 6th, 2023. Versions prior to 6.4.0 are not affected.



- [https://github.com/Abdurahmon3236/-CVE-2024-31211](https://github.com/Abdurahmon3236/-CVE-2024-31211) :  ![starts](https://img.shields.io/github/stars/Abdurahmon3236/-CVE-2024-31211.svg) ![forks](https://img.shields.io/github/forks/Abdurahmon3236/-CVE-2024-31211.svg)

## CVE-2024-30998
 SQL Injection vulnerability in PHPGurukul Men Salon Management System v.2.0, allows remote attackers to execute arbitrary code and obtain sensitive information via the email parameter in the index.php component.



- [https://github.com/efekaanakkar/CVE-2024-30998](https://github.com/efekaanakkar/CVE-2024-30998) :  ![starts](https://img.shields.io/github/stars/efekaanakkar/CVE-2024-30998.svg) ![forks](https://img.shields.io/github/forks/efekaanakkar/CVE-2024-30998.svg)

## CVE-2024-30973
 An issue in V-SOL G/EPON ONU HG323AC-B with firmware version V2.0.08-210715 allows an attacker to execute arbtirary code and obtain sensitive information via crafted POST request to /boaform/getASPdata/formFirewall, /boaform/getASPdata/formAcc.



- [https://github.com/Athos-Zago/CVE-2024-30973](https://github.com/Athos-Zago/CVE-2024-30973) :  ![starts](https://img.shields.io/github/stars/Athos-Zago/CVE-2024-30973.svg) ![forks](https://img.shields.io/github/forks/Athos-Zago/CVE-2024-30973.svg)

## CVE-2024-30956
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/leoCottret/CVE-2024-30956](https://github.com/leoCottret/CVE-2024-30956) :  ![starts](https://img.shields.io/github/stars/leoCottret/CVE-2024-30956.svg) ![forks](https://img.shields.io/github/forks/leoCottret/CVE-2024-30956.svg)

## CVE-2024-30896
 InfluxDB OSS 2.x through 2.7.11 stores the administrative operator token under the default organization which allows authorized users with read access to the authorization resource of the default organization to retrieve the operator token. InfluxDB OSS 1.x, Enterprise, Cloud, Cloud Dedicated and Clustered are not affected. NOTE: The researcher states that InfluxDB allows allAccess administrators to retrieve all raw tokens via an "influx auth ls" command. The supplier indicates that the organizations feature is operating as intended and that users may choose to add users to non-default organizations. A future release of InfluxDB 2.x will remove the ability to retrieve tokens from the API.



- [https://github.com/XenoM0rph97/CVE-2024-30896](https://github.com/XenoM0rph97/CVE-2024-30896) :  ![starts](https://img.shields.io/github/stars/XenoM0rph97/CVE-2024-30896.svg) ![forks](https://img.shields.io/github/forks/XenoM0rph97/CVE-2024-30896.svg)

## CVE-2024-30851
 Directory Traversal vulnerability in codesiddhant Jasmin Ransomware v.1.0.1 allows an attacker to obtain sensitive information via the download_file.php component.



- [https://github.com/chebuya/CVE-2024-30851-jasmin-ransomware-path-traversal-poc](https://github.com/chebuya/CVE-2024-30851-jasmin-ransomware-path-traversal-poc) :  ![starts](https://img.shields.io/github/stars/chebuya/CVE-2024-30851-jasmin-ransomware-path-traversal-poc.svg) ![forks](https://img.shields.io/github/forks/chebuya/CVE-2024-30851-jasmin-ransomware-path-traversal-poc.svg)

## CVE-2024-30850
 An issue in tiagorlampert CHAOS v5.0.1 allows a remote attacker to execute arbitrary code via the BuildClient function within client_service.go



- [https://github.com/chebuya/CVE-2024-30850-chaos-rat-rce-poc](https://github.com/chebuya/CVE-2024-30850-chaos-rat-rce-poc) :  ![starts](https://img.shields.io/github/stars/chebuya/CVE-2024-30850-chaos-rat-rce-poc.svg) ![forks](https://img.shields.io/github/forks/chebuya/CVE-2024-30850-chaos-rat-rce-poc.svg)

## CVE-2024-30656
 An issue in Fireboltt Dream Wristphone BSW202_FB_AAC_v2.0_20240110-20240110-1956 allows attackers to cause a Denial of Service (DoS) via a crafted deauth frame.



- [https://github.com/Yashodhanvivek/Firebolt-wristphone-vulnerability](https://github.com/Yashodhanvivek/Firebolt-wristphone-vulnerability) :  ![starts](https://img.shields.io/github/stars/Yashodhanvivek/Firebolt-wristphone-vulnerability.svg) ![forks](https://img.shields.io/github/forks/Yashodhanvivek/Firebolt-wristphone-vulnerability.svg)

## CVE-2024-30614
 An issue in Ametys CMS v4.5.0 and before allows attackers to obtain sensitive information via exposed resources to the error scope.



- [https://github.com/Lucky-lm/CVE-2024-30614](https://github.com/Lucky-lm/CVE-2024-30614) :  ![starts](https://img.shields.io/github/stars/Lucky-lm/CVE-2024-30614.svg) ![forks](https://img.shields.io/github/forks/Lucky-lm/CVE-2024-30614.svg)

## CVE-2024-30491
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in Metagauss ProfileGrid.This issue affects ProfileGrid : from n/a through 5.7.8.





- [https://github.com/truonghuuphuc/CVE-2024-30491-Poc](https://github.com/truonghuuphuc/CVE-2024-30491-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-30491-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-30491-Poc.svg)

## CVE-2024-30270
 mailcow: dockerized is an open source groupware/email suite based on docker. A security vulnerability has been identified in mailcow affecting versions prior to 2024-04. This vulnerability is a combination of path traversal and arbitrary code execution, specifically targeting the `rspamd_maps()` function. It allows authenticated admin users to overwrite any file writable by the www-data user by exploiting improper path validation. The exploit chain can lead to the execution of arbitrary commands on the server. Version 2024-04 contains a patch for the issue.



- [https://github.com/Alchemist3dot14/CVE-2024-30270-PoC](https://github.com/Alchemist3dot14/CVE-2024-30270-PoC) :  ![starts](https://img.shields.io/github/stars/Alchemist3dot14/CVE-2024-30270-PoC.svg) ![forks](https://img.shields.io/github/forks/Alchemist3dot14/CVE-2024-30270-PoC.svg)

## CVE-2024-30255
 Envoy is a cloud-native, open source edge and service proxy. The HTTP/2 protocol stack in Envoy versions prior to 1.29.3, 1.28.2, 1.27.4, and 1.26.8 are vulnerable to CPU exhaustion due to flood of CONTINUATION frames. Envoy's HTTP/2 codec allows the client to send an unlimited number of CONTINUATION frames even after exceeding Envoy's header map limits. This allows an attacker to send a sequence of CONTINUATION frames without the END_HEADERS bit set causing CPU utilization, consuming approximately 1 core per 300Mbit/s of traffic and culminating in denial of service through CPU exhaustion. Users should upgrade to version 1.29.3, 1.28.2, 1.27.4, or 1.26.8 to mitigate the effects of the CONTINUATION flood. As a workaround, disable HTTP/2 protocol for downstream connections.



- [https://github.com/lockness-Ko/CVE-2024-27316](https://github.com/lockness-Ko/CVE-2024-27316) :  ![starts](https://img.shields.io/github/stars/lockness-Ko/CVE-2024-27316.svg) ![forks](https://img.shields.io/github/forks/lockness-Ko/CVE-2024-27316.svg)

- [https://github.com/blackmagic2023/Envoy-CPU-Exhaustion-Vulnerability-PoC](https://github.com/blackmagic2023/Envoy-CPU-Exhaustion-Vulnerability-PoC) :  ![starts](https://img.shields.io/github/stars/blackmagic2023/Envoy-CPU-Exhaustion-Vulnerability-PoC.svg) ![forks](https://img.shields.io/github/forks/blackmagic2023/Envoy-CPU-Exhaustion-Vulnerability-PoC.svg)

## CVE-2024-30212
 If a SCSI READ(10) command is initiated via USB using the largest LBA 
(0xFFFFFFFF) with it's default block size of 512 and a count of 1,

the first 512 byte of the 0x80000000 memory area is returned to the 
user. If the block count is increased, the full RAM can be exposed.

The same method works to write to this memory area. If RAM contains 
pointers, those can be - depending on the application - overwritten to

return data from any other offset including Progam and Boot Flash.



- [https://github.com/Fehr-GmbH/blackleak](https://github.com/Fehr-GmbH/blackleak) :  ![starts](https://img.shields.io/github/stars/Fehr-GmbH/blackleak.svg) ![forks](https://img.shields.io/github/forks/Fehr-GmbH/blackleak.svg)

## CVE-2024-30088
 Windows Kernel Elevation of Privilege Vulnerability



- [https://github.com/exploits-forsale/collateral-damage](https://github.com/exploits-forsale/collateral-damage) :  ![starts](https://img.shields.io/github/stars/exploits-forsale/collateral-damage.svg) ![forks](https://img.shields.io/github/forks/exploits-forsale/collateral-damage.svg)

- [https://github.com/tykawaii98/CVE-2024-30088](https://github.com/tykawaii98/CVE-2024-30088) :  ![starts](https://img.shields.io/github/stars/tykawaii98/CVE-2024-30088.svg) ![forks](https://img.shields.io/github/forks/tykawaii98/CVE-2024-30088.svg)

- [https://github.com/Zombie-Kaiser/CVE-2024-30088-Windows-poc](https://github.com/Zombie-Kaiser/CVE-2024-30088-Windows-poc) :  ![starts](https://img.shields.io/github/stars/Zombie-Kaiser/CVE-2024-30088-Windows-poc.svg) ![forks](https://img.shields.io/github/forks/Zombie-Kaiser/CVE-2024-30088-Windows-poc.svg)

- [https://github.com/NextGenPentesters/CVE-2024-30088-](https://github.com/NextGenPentesters/CVE-2024-30088-) :  ![starts](https://img.shields.io/github/stars/NextGenPentesters/CVE-2024-30088-.svg) ![forks](https://img.shields.io/github/forks/NextGenPentesters/CVE-2024-30088-.svg)

- [https://github.com/Admin9961/CVE-2024-30088](https://github.com/Admin9961/CVE-2024-30088) :  ![starts](https://img.shields.io/github/stars/Admin9961/CVE-2024-30088.svg) ![forks](https://img.shields.io/github/forks/Admin9961/CVE-2024-30088.svg)

## CVE-2024-30085
 Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability



- [https://github.com/Adamkadaban/CVE-2024-30085](https://github.com/Adamkadaban/CVE-2024-30085) :  ![starts](https://img.shields.io/github/stars/Adamkadaban/CVE-2024-30085.svg) ![forks](https://img.shields.io/github/forks/Adamkadaban/CVE-2024-30085.svg)

- [https://github.com/murdok1982/Exploit-PoC-para-CVE-2024-30085](https://github.com/murdok1982/Exploit-PoC-para-CVE-2024-30085) :  ![starts](https://img.shields.io/github/stars/murdok1982/Exploit-PoC-para-CVE-2024-30085.svg) ![forks](https://img.shields.io/github/forks/murdok1982/Exploit-PoC-para-CVE-2024-30085.svg)

## CVE-2024-30078
 Windows Wi-Fi Driver Remote Code Execution Vulnerability



- [https://github.com/blkph0x/CVE_2024_30078_POC_WIFI](https://github.com/blkph0x/CVE_2024_30078_POC_WIFI) :  ![starts](https://img.shields.io/github/stars/blkph0x/CVE_2024_30078_POC_WIFI.svg) ![forks](https://img.shields.io/github/forks/blkph0x/CVE_2024_30078_POC_WIFI.svg)

- [https://github.com/lvyitian/CVE-2024-30078-](https://github.com/lvyitian/CVE-2024-30078-) :  ![starts](https://img.shields.io/github/stars/lvyitian/CVE-2024-30078-.svg) ![forks](https://img.shields.io/github/forks/lvyitian/CVE-2024-30078-.svg)

- [https://github.com/52by/CVE-2024-30078](https://github.com/52by/CVE-2024-30078) :  ![starts](https://img.shields.io/github/stars/52by/CVE-2024-30078.svg) ![forks](https://img.shields.io/github/forks/52by/CVE-2024-30078.svg)

- [https://github.com/Jailman/CVE_2024_30078_A_POC](https://github.com/Jailman/CVE_2024_30078_A_POC) :  ![starts](https://img.shields.io/github/stars/Jailman/CVE_2024_30078_A_POC.svg) ![forks](https://img.shields.io/github/forks/Jailman/CVE_2024_30078_A_POC.svg)

- [https://github.com/a-roshbaik/CVE_2024_30078_POC_WIFI](https://github.com/a-roshbaik/CVE_2024_30078_POC_WIFI) :  ![starts](https://img.shields.io/github/stars/a-roshbaik/CVE_2024_30078_POC_WIFI.svg) ![forks](https://img.shields.io/github/forks/a-roshbaik/CVE_2024_30078_POC_WIFI.svg)

## CVE-2024-30056
 Microsoft Edge (Chromium-based) Information Disclosure Vulnerability



- [https://github.com/absholi7ly/Microsoft-Edge-Information-Disclosure](https://github.com/absholi7ly/Microsoft-Edge-Information-Disclosure) :  ![starts](https://img.shields.io/github/stars/absholi7ly/Microsoft-Edge-Information-Disclosure.svg) ![forks](https://img.shields.io/github/forks/absholi7ly/Microsoft-Edge-Information-Disclosure.svg)

## CVE-2024-30043
 Microsoft SharePoint Server Information Disclosure Vulnerability



- [https://github.com/W01fh4cker/CVE-2024-30043-XXE](https://github.com/W01fh4cker/CVE-2024-30043-XXE) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/CVE-2024-30043-XXE.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/CVE-2024-30043-XXE.svg)

## CVE-2024-29988
 SmartScreen Prompt Security Feature Bypass Vulnerability



- [https://github.com/Sploitus/CVE-2024-29988-exploit](https://github.com/Sploitus/CVE-2024-29988-exploit) :  ![starts](https://img.shields.io/github/stars/Sploitus/CVE-2024-29988-exploit.svg) ![forks](https://img.shields.io/github/forks/Sploitus/CVE-2024-29988-exploit.svg)

## CVE-2024-29976
 ** UNSUPPORTED WHEN ASSIGNED **
The improper privilege management vulnerability in the command “show_allsessions” in Zyxel NAS326 firmware versions before V5.21(AAZF.17)C0 and NAS542 firmware versions before V5.21(ABAG.14)C0 could allow an authenticated attacker to obtain a logged-in administrator’s session information containing cookies on an affected device.



- [https://github.com/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc](https://github.com/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc) :  ![starts](https://img.shields.io/github/stars/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc.svg) ![forks](https://img.shields.io/github/forks/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc.svg)

## CVE-2024-29975
 ** UNSUPPORTED WHEN ASSIGNED **
The improper privilege management vulnerability in the SUID executable binary in Zyxel NAS326 firmware versions before V5.21(AAZF.17)C0 and NAS542 firmware versions before V5.21(ABAG.14)C0 could allow an authenticated local attacker with administrator privileges to execute some system commands as the “root” user on a vulnerable device.



- [https://github.com/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc](https://github.com/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc) :  ![starts](https://img.shields.io/github/stars/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc.svg) ![forks](https://img.shields.io/github/forks/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc.svg)

## CVE-2024-29974
 ** UNSUPPORTED WHEN ASSIGNED **
The remote code execution vulnerability in the CGI program “file_upload-cgi” in Zyxel NAS326 firmware versions before V5.21(AAZF.17)C0 and NAS542 firmware versions before V5.21(ABAG.14)C0 could allow an unauthenticated attacker to execute arbitrary code by uploading a crafted configuration file to a vulnerable device.



- [https://github.com/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc](https://github.com/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc) :  ![starts](https://img.shields.io/github/stars/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc.svg) ![forks](https://img.shields.io/github/forks/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc.svg)

## CVE-2024-29973
 ** UNSUPPORTED WHEN ASSIGNED **
The command injection vulnerability in the “setCookie” parameter in Zyxel NAS326 firmware versions before V5.21(AAZF.17)C0 and NAS542 firmware versions before V5.21(ABAG.14)C0 could allow an unauthenticated attacker to execute some operating system (OS) commands by sending a crafted HTTP POST request.



- [https://github.com/NanoWraith/CVE-2024-29973](https://github.com/NanoWraith/CVE-2024-29973) :  ![starts](https://img.shields.io/github/stars/NanoWraith/CVE-2024-29973.svg) ![forks](https://img.shields.io/github/forks/NanoWraith/CVE-2024-29973.svg)

- [https://github.com/bigb0x/CVE-2024-29973](https://github.com/bigb0x/CVE-2024-29973) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-29973.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-29973.svg)

- [https://github.com/RevoltSecurities/CVE-2024-29973](https://github.com/RevoltSecurities/CVE-2024-29973) :  ![starts](https://img.shields.io/github/stars/RevoltSecurities/CVE-2024-29973.svg) ![forks](https://img.shields.io/github/forks/RevoltSecurities/CVE-2024-29973.svg)

- [https://github.com/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc](https://github.com/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc) :  ![starts](https://img.shields.io/github/stars/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc.svg) ![forks](https://img.shields.io/github/forks/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc.svg)

- [https://github.com/momika233/CVE-2024-29973](https://github.com/momika233/CVE-2024-29973) :  ![starts](https://img.shields.io/github/stars/momika233/CVE-2024-29973.svg) ![forks](https://img.shields.io/github/forks/momika233/CVE-2024-29973.svg)

- [https://github.com/p0et08/CVE-2024-29973](https://github.com/p0et08/CVE-2024-29973) :  ![starts](https://img.shields.io/github/stars/p0et08/CVE-2024-29973.svg) ![forks](https://img.shields.io/github/forks/p0et08/CVE-2024-29973.svg)

## CVE-2024-29972
 ** UNSUPPORTED WHEN ASSIGNED **
The command injection vulnerability in the CGI program "remote_help-cgi" in Zyxel NAS326 firmware versions before V5.21(AAZF.17)C0 and NAS542 firmware versions before V5.21(ABAG.14)C0 could allow an unauthenticated attacker to execute some operating system (OS) commands by sending a crafted HTTP POST request.



- [https://github.com/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc](https://github.com/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc) :  ![starts](https://img.shields.io/github/stars/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc.svg) ![forks](https://img.shields.io/github/forks/Pommaq/CVE-2024-29972-CVE-2024-29976-CVE-2024-29973-CVE-2024-29975-CVE-2024-29974-poc.svg)

- [https://github.com/WanLiChangChengWanLiChang/CVE-2024-29972](https://github.com/WanLiChangChengWanLiChang/CVE-2024-29972) :  ![starts](https://img.shields.io/github/stars/WanLiChangChengWanLiChang/CVE-2024-29972.svg) ![forks](https://img.shields.io/github/forks/WanLiChangChengWanLiChang/CVE-2024-29972.svg)

## CVE-2024-29943
 An attacker was able to perform an out-of-bounds read or write on a JavaScript object by fooling range-based bounds check elimination. This vulnerability affects Firefox  124.0.1.



- [https://github.com/bjrjk/CVE-2024-29943](https://github.com/bjrjk/CVE-2024-29943) :  ![starts](https://img.shields.io/github/stars/bjrjk/CVE-2024-29943.svg) ![forks](https://img.shields.io/github/forks/bjrjk/CVE-2024-29943.svg)

## CVE-2024-29895
 Cacti provides an operational monitoring and fault management framework. A command injection vulnerability on the 1.3.x DEV branch allows any unauthenticated user to execute arbitrary command on the server when `register_argc_argv` option of PHP is `On`. In `cmd_realtime.php` line 119, the `$poller_id` used as part of the command execution is sourced from `$_SERVER['argv']`, which can be controlled by URL when `register_argc_argv` option of PHP is `On`. And this option is `On` by default in many environments such as the main PHP Docker image for PHP. Commit 53e8014d1f082034e0646edc6286cde3800c683d contains a patch for the issue, but this commit was reverted in commit 99633903cad0de5ace636249de16f77e57a3c8fc.



- [https://github.com/Stuub/CVE-2024-29895-CactiRCE-PoC](https://github.com/Stuub/CVE-2024-29895-CactiRCE-PoC) :  ![starts](https://img.shields.io/github/stars/Stuub/CVE-2024-29895-CactiRCE-PoC.svg) ![forks](https://img.shields.io/github/forks/Stuub/CVE-2024-29895-CactiRCE-PoC.svg)

- [https://github.com/Rubioo02/CVE-2024-29895](https://github.com/Rubioo02/CVE-2024-29895) :  ![starts](https://img.shields.io/github/stars/Rubioo02/CVE-2024-29895.svg) ![forks](https://img.shields.io/github/forks/Rubioo02/CVE-2024-29895.svg)

- [https://github.com/secunnix/CVE-2024-29895](https://github.com/secunnix/CVE-2024-29895) :  ![starts](https://img.shields.io/github/stars/secunnix/CVE-2024-29895.svg) ![forks](https://img.shields.io/github/forks/secunnix/CVE-2024-29895.svg)

- [https://github.com/ticofookfook/CVE-2024-29895.py](https://github.com/ticofookfook/CVE-2024-29895.py) :  ![starts](https://img.shields.io/github/stars/ticofookfook/CVE-2024-29895.py.svg) ![forks](https://img.shields.io/github/forks/ticofookfook/CVE-2024-29895.py.svg)

## CVE-2024-29868
 Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG) vulnerability in Apache StreamPipes user self-registration and password recovery mechanism.
This allows an attacker to guess the recovery token in a reasonable time and thereby to take over the attacked user's account.
This issue affects Apache StreamPipes: from 0.69.0 through 0.93.0.

Users are recommended to upgrade to version 0.95.0, which fixes the issue.





- [https://github.com/DEVisions/CVE-2024-29868](https://github.com/DEVisions/CVE-2024-29868) :  ![starts](https://img.shields.io/github/stars/DEVisions/CVE-2024-29868.svg) ![forks](https://img.shields.io/github/forks/DEVisions/CVE-2024-29868.svg)

## CVE-2024-29863
 A race condition in the installer executable in Qlik Qlikview before versions May 2022 SR3 (12.70.20300) and May 2023 SR2 (12,80.20200) may allow an existing lower privileged user to cause code to be executed in the context of a Windows Administrator.



- [https://github.com/pawlokk/qlikview-poc-CVE-2024-29863](https://github.com/pawlokk/qlikview-poc-CVE-2024-29863) :  ![starts](https://img.shields.io/github/stars/pawlokk/qlikview-poc-CVE-2024-29863.svg) ![forks](https://img.shields.io/github/forks/pawlokk/qlikview-poc-CVE-2024-29863.svg)

## CVE-2024-29855
 Hard-coded JWT secret allows authentication bypass in Veeam Recovery Orchestrator



- [https://github.com/sinsinology/CVE-2024-29855](https://github.com/sinsinology/CVE-2024-29855) :  ![starts](https://img.shields.io/github/stars/sinsinology/CVE-2024-29855.svg) ![forks](https://img.shields.io/github/forks/sinsinology/CVE-2024-29855.svg)

## CVE-2024-29849
 Veeam Backup Enterprise Manager allows unauthenticated users to log in as any user to enterprise manager web interface.



- [https://github.com/sinsinology/CVE-2024-29849](https://github.com/sinsinology/CVE-2024-29849) :  ![starts](https://img.shields.io/github/stars/sinsinology/CVE-2024-29849.svg) ![forks](https://img.shields.io/github/forks/sinsinology/CVE-2024-29849.svg)

## CVE-2024-29824
 An unspecified SQL Injection vulnerability in Core server of Ivanti EPM 2022 SU5 and prior allows an unauthenticated attacker within the same network to execute arbitrary code.



- [https://github.com/horizon3ai/CVE-2024-29824](https://github.com/horizon3ai/CVE-2024-29824) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2024-29824.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2024-29824.svg)

- [https://github.com/R4be1/CVE-2024-29824](https://github.com/R4be1/CVE-2024-29824) :  ![starts](https://img.shields.io/github/stars/R4be1/CVE-2024-29824.svg) ![forks](https://img.shields.io/github/forks/R4be1/CVE-2024-29824.svg)

## CVE-2024-29671
 Buffer Overflow vulnerability in NEXTU FLATA AX1500 Router v.1.0.2 allows a remote attacker to execute arbitrary code via the POST request handler component.



- [https://github.com/laskdjlaskdj12/CVE-2024-29671-POC](https://github.com/laskdjlaskdj12/CVE-2024-29671-POC) :  ![starts](https://img.shields.io/github/stars/laskdjlaskdj12/CVE-2024-29671-POC.svg) ![forks](https://img.shields.io/github/forks/laskdjlaskdj12/CVE-2024-29671-POC.svg)

## CVE-2024-29510
 Artifex Ghostscript before 10.03.1 allows memory corruption, and SAFER sandbox bypass, via format string injection with a uniprint device.



- [https://github.com/swsmith2391/CVE-2024-29510](https://github.com/swsmith2391/CVE-2024-29510) :  ![starts](https://img.shields.io/github/stars/swsmith2391/CVE-2024-29510.svg) ![forks](https://img.shields.io/github/forks/swsmith2391/CVE-2024-29510.svg)

## CVE-2024-29415
 The ip package through 2.0.1 for Node.js might allow SSRF because some IP addresses (such as 127.1, 01200034567, 012.1.2.3, 000:0:0000::01, and ::fFFf:127.0.0.1) are improperly categorized as globally routable via isPublic. NOTE: this issue exists because of an incomplete fix for CVE-2023-42282.



- [https://github.com/felipecruz91/node-ip-vex](https://github.com/felipecruz91/node-ip-vex) :  ![starts](https://img.shields.io/github/stars/felipecruz91/node-ip-vex.svg) ![forks](https://img.shields.io/github/forks/felipecruz91/node-ip-vex.svg)

## CVE-2024-29404
 An issue in Razer Synapse 3 v.3.9.131.20813 and Synapse 3 App v.20240213 allows a local attacker to execute arbitrary code via the export parameter of the Chroma Effects function in the Profiles component.



- [https://github.com/mansk1es/CVE-2024-29404_Razer](https://github.com/mansk1es/CVE-2024-29404_Razer) :  ![starts](https://img.shields.io/github/stars/mansk1es/CVE-2024-29404_Razer.svg) ![forks](https://img.shields.io/github/forks/mansk1es/CVE-2024-29404_Razer.svg)

## CVE-2024-29399
 An issue was discovered in GNU Savane v.3.13 and before, allows a remote attacker to execute arbitrary code and escalate privileges via a crafted file to the upload.php component.



- [https://github.com/ally-petitt/CVE-2024-29399](https://github.com/ally-petitt/CVE-2024-29399) :  ![starts](https://img.shields.io/github/stars/ally-petitt/CVE-2024-29399.svg) ![forks](https://img.shields.io/github/forks/ally-petitt/CVE-2024-29399.svg)

## CVE-2024-29384
 An issue in CSS Exfil Protection v.1.1.0 allows a remote attacker to obtain sensitive information via the content.js and parseCSSRules functions.



- [https://github.com/randshell/CSS-Exfil-Protection-POC](https://github.com/randshell/CSS-Exfil-Protection-POC) :  ![starts](https://img.shields.io/github/stars/randshell/CSS-Exfil-Protection-POC.svg) ![forks](https://img.shields.io/github/forks/randshell/CSS-Exfil-Protection-POC.svg)

## CVE-2024-29375
 CSV Injection vulnerability in Addactis IBNRS v.3.10.3.107 allows a remote attacker to execute arbitrary code via a crafted .ibnrs file to the Project Description, Identifiers, Custom Triangle Name (inside Input Triangles) and Yield Curve Name parameters.



- [https://github.com/ismailcemunver/CVE-2024-29375](https://github.com/ismailcemunver/CVE-2024-29375) :  ![starts](https://img.shields.io/github/stars/ismailcemunver/CVE-2024-29375.svg) ![forks](https://img.shields.io/github/forks/ismailcemunver/CVE-2024-29375.svg)

## CVE-2024-29296
 A user enumeration vulnerability was found in Portainer CE 2.19.4. This issue occurs during user authentication process, where a difference in response time could allow a remote unauthenticated user to determine if a username is valid or not.



- [https://github.com/ThaySolis/CVE-2024-29296](https://github.com/ThaySolis/CVE-2024-29296) :  ![starts](https://img.shields.io/github/stars/ThaySolis/CVE-2024-29296.svg) ![forks](https://img.shields.io/github/forks/ThaySolis/CVE-2024-29296.svg)

- [https://github.com/Lavender-exe/CVE-2024-29296-PoC](https://github.com/Lavender-exe/CVE-2024-29296-PoC) :  ![starts](https://img.shields.io/github/stars/Lavender-exe/CVE-2024-29296-PoC.svg) ![forks](https://img.shields.io/github/forks/Lavender-exe/CVE-2024-29296-PoC.svg)

## CVE-2024-29278
 funboot v1.1 is vulnerable to Cross Site Scripting (XSS) via the title field in "create a message ."



- [https://github.com/QDming/cve](https://github.com/QDming/cve) :  ![starts](https://img.shields.io/github/stars/QDming/cve.svg) ![forks](https://img.shields.io/github/forks/QDming/cve.svg)

## CVE-2024-29275
 SQL injection vulnerability in SeaCMS version 12.9, allows remote unauthenticated attackers to execute arbitrary code and obtain sensitive information via the id parameter in class.php.



- [https://github.com/Cyphercoda/nuclei_template](https://github.com/Cyphercoda/nuclei_template) :  ![starts](https://img.shields.io/github/stars/Cyphercoda/nuclei_template.svg) ![forks](https://img.shields.io/github/forks/Cyphercoda/nuclei_template.svg)

## CVE-2024-29272
 Arbitrary File Upload vulnerability in VvvebJs before version 1.7.5, allows unauthenticated remote attackers to execute arbitrary code and obtain sensitive information via the sanitizeFileName parameter in save.php.



- [https://github.com/awjkjflkwlekfdjs/CVE-2024-29272](https://github.com/awjkjflkwlekfdjs/CVE-2024-29272) :  ![starts](https://img.shields.io/github/stars/awjkjflkwlekfdjs/CVE-2024-29272.svg) ![forks](https://img.shields.io/github/forks/awjkjflkwlekfdjs/CVE-2024-29272.svg)

## CVE-2024-29269
 An issue discovered in Telesquare TLR-2005Ksh 1.0.0 and 1.1.4 allows attackers to run arbitrary system commands via the Cmd parameter.



- [https://github.com/Chocapikk/CVE-2024-29269](https://github.com/Chocapikk/CVE-2024-29269) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-29269.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-29269.svg)

- [https://github.com/wutalent/CVE-2024-29269](https://github.com/wutalent/CVE-2024-29269) :  ![starts](https://img.shields.io/github/stars/wutalent/CVE-2024-29269.svg) ![forks](https://img.shields.io/github/forks/wutalent/CVE-2024-29269.svg)

- [https://github.com/K3ysTr0K3R/CVE-2024-29269-EXPLOIT](https://github.com/K3ysTr0K3R/CVE-2024-29269-EXPLOIT) :  ![starts](https://img.shields.io/github/stars/K3ysTr0K3R/CVE-2024-29269-EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/K3ysTr0K3R/CVE-2024-29269-EXPLOIT.svg)

- [https://github.com/YongYe-Security/CVE-2024-29269](https://github.com/YongYe-Security/CVE-2024-29269) :  ![starts](https://img.shields.io/github/stars/YongYe-Security/CVE-2024-29269.svg) ![forks](https://img.shields.io/github/forks/YongYe-Security/CVE-2024-29269.svg)

- [https://github.com/dream434/CVE-2024-29269](https://github.com/dream434/CVE-2024-29269) :  ![starts](https://img.shields.io/github/stars/dream434/CVE-2024-29269.svg) ![forks](https://img.shields.io/github/forks/dream434/CVE-2024-29269.svg)

## CVE-2024-29075
 Active debug code vulnerability exists in Mesh Wi-Fi router RP562B firmware version v1.0.2 and earlier. If this vulnerability is exploited, a network-adjacent authenticated attacker may obtain or alter the settings of the device .



- [https://github.com/0xNslabs/SoftBankMeshAPI](https://github.com/0xNslabs/SoftBankMeshAPI) :  ![starts](https://img.shields.io/github/stars/0xNslabs/SoftBankMeshAPI.svg) ![forks](https://img.shields.io/github/forks/0xNslabs/SoftBankMeshAPI.svg)

## CVE-2024-29059
 .NET Framework Information Disclosure Vulnerability



- [https://github.com/codewhitesec/HttpRemotingObjRefLeak](https://github.com/codewhitesec/HttpRemotingObjRefLeak) :  ![starts](https://img.shields.io/github/stars/codewhitesec/HttpRemotingObjRefLeak.svg) ![forks](https://img.shields.io/github/forks/codewhitesec/HttpRemotingObjRefLeak.svg)

## CVE-2024-28999
 The SolarWinds Platform was determined to be affected by a Race Condition Vulnerability affecting the web console. 



- [https://github.com/HussainFathy/CVE-2024-28999](https://github.com/HussainFathy/CVE-2024-28999) :  ![starts](https://img.shields.io/github/stars/HussainFathy/CVE-2024-28999.svg) ![forks](https://img.shields.io/github/forks/HussainFathy/CVE-2024-28999.svg)

## CVE-2024-28995
 











SolarWinds Serv-U was susceptible to a directory transversal vulnerability that would allow access to read sensitive files on the host machine.    











- [https://github.com/Stuub/CVE-2024-28995](https://github.com/Stuub/CVE-2024-28995) :  ![starts](https://img.shields.io/github/stars/Stuub/CVE-2024-28995.svg) ![forks](https://img.shields.io/github/forks/Stuub/CVE-2024-28995.svg)

- [https://github.com/bigb0x/CVE-2024-28995](https://github.com/bigb0x/CVE-2024-28995) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-28995.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-28995.svg)

- [https://github.com/ggfzx/CVE-2024-28995](https://github.com/ggfzx/CVE-2024-28995) :  ![starts](https://img.shields.io/github/stars/ggfzx/CVE-2024-28995.svg) ![forks](https://img.shields.io/github/forks/ggfzx/CVE-2024-28995.svg)

- [https://github.com/0xc4t/CVE-2024-28995](https://github.com/0xc4t/CVE-2024-28995) :  ![starts](https://img.shields.io/github/stars/0xc4t/CVE-2024-28995.svg) ![forks](https://img.shields.io/github/forks/0xc4t/CVE-2024-28995.svg)

- [https://github.com/Praison001/CVE-2024-28995-SolarWinds-Serv-U](https://github.com/Praison001/CVE-2024-28995-SolarWinds-Serv-U) :  ![starts](https://img.shields.io/github/stars/Praison001/CVE-2024-28995-SolarWinds-Serv-U.svg) ![forks](https://img.shields.io/github/forks/Praison001/CVE-2024-28995-SolarWinds-Serv-U.svg)

- [https://github.com/demoAlitalia/CVE-2024-28995](https://github.com/demoAlitalia/CVE-2024-28995) :  ![starts](https://img.shields.io/github/stars/demoAlitalia/CVE-2024-28995.svg) ![forks](https://img.shields.io/github/forks/demoAlitalia/CVE-2024-28995.svg)

- [https://github.com/muhammetali20/CVE-2024-28995](https://github.com/muhammetali20/CVE-2024-28995) :  ![starts](https://img.shields.io/github/stars/muhammetali20/CVE-2024-28995.svg) ![forks](https://img.shields.io/github/forks/muhammetali20/CVE-2024-28995.svg)

- [https://github.com/huseyinstif/CVE-2024-28995-Nuclei-Template](https://github.com/huseyinstif/CVE-2024-28995-Nuclei-Template) :  ![starts](https://img.shields.io/github/stars/huseyinstif/CVE-2024-28995-Nuclei-Template.svg) ![forks](https://img.shields.io/github/forks/huseyinstif/CVE-2024-28995-Nuclei-Template.svg)

## CVE-2024-28987
 The SolarWinds Web Help Desk (WHD) software is affected by a hardcoded credential vulnerability, allowing remote unauthenticated user to access internal functionality and modify data.



- [https://github.com/alecclyde/CVE-2024-28987](https://github.com/alecclyde/CVE-2024-28987) :  ![starts](https://img.shields.io/github/stars/alecclyde/CVE-2024-28987.svg) ![forks](https://img.shields.io/github/forks/alecclyde/CVE-2024-28987.svg)

## CVE-2024-28955
 Affected devices create coredump files when crashed, storing them with world-readable permission. Any local user of the device can examine the coredump files, and research the memory contents. As for the details of affected product names, model numbers, and versions, refer to the information provided by the respective vendors listed under [References].



- [https://github.com/Stuub/CVE-2024-28995](https://github.com/Stuub/CVE-2024-28995) :  ![starts](https://img.shields.io/github/stars/Stuub/CVE-2024-28995.svg) ![forks](https://img.shields.io/github/forks/Stuub/CVE-2024-28995.svg)

## CVE-2024-28784
 IBM QRadar SIEM 7.5 is vulnerable to cross-site scripting. This vulnerability allows users to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials disclosure within a trusted session.  IBM X-Force ID:  285893.



- [https://github.com/CainSoulless/CVE-2024-28784](https://github.com/CainSoulless/CVE-2024-28784) :  ![starts](https://img.shields.io/github/stars/CainSoulless/CVE-2024-28784.svg) ![forks](https://img.shields.io/github/forks/CainSoulless/CVE-2024-28784.svg)

## CVE-2024-28757
 libexpat through 2.6.1 allows an XML Entity Expansion attack when there is isolated use of external parsers (created via XML_ExternalEntityParserCreate).



- [https://github.com/RenukaSelvar/expat_CVE-2024-28757](https://github.com/RenukaSelvar/expat_CVE-2024-28757) :  ![starts](https://img.shields.io/github/stars/RenukaSelvar/expat_CVE-2024-28757.svg) ![forks](https://img.shields.io/github/forks/RenukaSelvar/expat_CVE-2024-28757.svg)

- [https://github.com/saurabh2088/expat_2_1_1_CVE-2024-28757](https://github.com/saurabh2088/expat_2_1_1_CVE-2024-28757) :  ![starts](https://img.shields.io/github/stars/saurabh2088/expat_2_1_1_CVE-2024-28757.svg) ![forks](https://img.shields.io/github/forks/saurabh2088/expat_2_1_1_CVE-2024-28757.svg)

- [https://github.com/saurabh2088/expat_2_1_0_CVE-2024-28757](https://github.com/saurabh2088/expat_2_1_0_CVE-2024-28757) :  ![starts](https://img.shields.io/github/stars/saurabh2088/expat_2_1_0_CVE-2024-28757.svg) ![forks](https://img.shields.io/github/forks/saurabh2088/expat_2_1_0_CVE-2024-28757.svg)

## CVE-2024-28752
 A SSRF vulnerability using the Aegis DataBinding in versions of Apache CXF before 4.0.4, 3.6.3 and 3.5.8 allows an attacker to perform SSRF style attacks on webservices that take at least one parameter of any type. Users of other data bindings (including the default databinding) are not impacted.



- [https://github.com/ReaJason/CVE-2024-28752](https://github.com/ReaJason/CVE-2024-28752) :  ![starts](https://img.shields.io/github/stars/ReaJason/CVE-2024-28752.svg) ![forks](https://img.shields.io/github/forks/ReaJason/CVE-2024-28752.svg)

## CVE-2024-28741
 Cross Site Scripting vulnerability in EginDemirbilek NorthStar C2 v1 allows a remote attacker to execute arbitrary code via the login.php component.



- [https://github.com/chebuya/CVE-2024-28741-northstar-agent-rce-poc](https://github.com/chebuya/CVE-2024-28741-northstar-agent-rce-poc) :  ![starts](https://img.shields.io/github/stars/chebuya/CVE-2024-28741-northstar-agent-rce-poc.svg) ![forks](https://img.shields.io/github/forks/chebuya/CVE-2024-28741-northstar-agent-rce-poc.svg)

## CVE-2024-28715
 Cross Site Scripting vulnerability in DOraCMS v.2.18 and before allows a remote attacker to execute arbitrary code via the markdown0 function in the /app/public/apidoc/oas3/wrap-components/markdown.jsx endpoint.



- [https://github.com/Lq0ne/CVE-2024-28715](https://github.com/Lq0ne/CVE-2024-28715) :  ![starts](https://img.shields.io/github/stars/Lq0ne/CVE-2024-28715.svg) ![forks](https://img.shields.io/github/forks/Lq0ne/CVE-2024-28715.svg)

## CVE-2024-28589
 An issue was discovered in Axigen Mail Server for Windows versions 10.5.18 and before, allows local low-privileged attackers to execute arbitrary code and escalate privileges via insecure DLL loading from a world-writable directory during service initialization.



- [https://github.com/Alaatk/CVE-2024-28589](https://github.com/Alaatk/CVE-2024-28589) :  ![starts](https://img.shields.io/github/stars/Alaatk/CVE-2024-28589.svg) ![forks](https://img.shields.io/github/forks/Alaatk/CVE-2024-28589.svg)

## CVE-2024-28515
 Buffer Overflow vulnerability in CSAPP_Lab CSAPP Lab3 15-213 Fall 20xx allows a remote attacker to execute arbitrary code via the lab3 of csapp,lab3/buflab-update.pl component.



- [https://github.com/heshi906/CVE-2024-28515](https://github.com/heshi906/CVE-2024-28515) :  ![starts](https://img.shields.io/github/stars/heshi906/CVE-2024-28515.svg) ![forks](https://img.shields.io/github/forks/heshi906/CVE-2024-28515.svg)

## CVE-2024-28397
 An issue in the component js2py.disable_pyimport() of js2py up to v0.74 allows attackers to execute arbitrary code via a crafted API call.



- [https://github.com/Marven11/CVE-2024-28397-js2py-Sandbox-Escape](https://github.com/Marven11/CVE-2024-28397-js2py-Sandbox-Escape) :  ![starts](https://img.shields.io/github/stars/Marven11/CVE-2024-28397-js2py-Sandbox-Escape.svg) ![forks](https://img.shields.io/github/forks/Marven11/CVE-2024-28397-js2py-Sandbox-Escape.svg)

- [https://github.com/CYBER-WARRIOR-SEC/CVE-2024-28397-js2py-Sandbox-Escape](https://github.com/CYBER-WARRIOR-SEC/CVE-2024-28397-js2py-Sandbox-Escape) :  ![starts](https://img.shields.io/github/stars/CYBER-WARRIOR-SEC/CVE-2024-28397-js2py-Sandbox-Escape.svg) ![forks](https://img.shields.io/github/forks/CYBER-WARRIOR-SEC/CVE-2024-28397-js2py-Sandbox-Escape.svg)

## CVE-2024-28328
 CSV Injection vulnerability in the Asus RT-N12+ router allows administrator users to inject arbitrary commands or formulas in the client name parameter which can be triggered and executed in a different user session upon exporting to CSV format.



- [https://github.com/Redfox-Security/Asus-RT--N12-B1-s-CSV-Injection-CVE--2024--28328](https://github.com/Redfox-Security/Asus-RT--N12-B1-s-CSV-Injection-CVE--2024--28328) :  ![starts](https://img.shields.io/github/stars/Redfox-Security/Asus-RT--N12-B1-s-CSV-Injection-CVE--2024--28328.svg) ![forks](https://img.shields.io/github/forks/Redfox-Security/Asus-RT--N12-B1-s-CSV-Injection-CVE--2024--28328.svg)

## CVE-2024-28327
 Asus RT-N12+ B1 router stores user passwords in plaintext, which could allow local attackers to obtain unauthorized access and modify router settings.



- [https://github.com/Redfox-Security/Asus-RT--N12-B1-s-Insecure-Credential-Storage-CVE--2024--28327](https://github.com/Redfox-Security/Asus-RT--N12-B1-s-Insecure-Credential-Storage-CVE--2024--28327) :  ![starts](https://img.shields.io/github/stars/Redfox-Security/Asus-RT--N12-B1-s-Insecure-Credential-Storage-CVE--2024--28327.svg) ![forks](https://img.shields.io/github/forks/Redfox-Security/Asus-RT--N12-B1-s-Insecure-Credential-Storage-CVE--2024--28327.svg)

## CVE-2024-28326
 Incorrect Access Control in ASUS RT-N12+ B1 and RT-N12 D1 routers allows local attackers to obtain root terminal access via the the UART interface.



- [https://github.com/Redfox-Security/Asus-RT--N12-B1-s-Privilege-Escalation--CVE--2024--28326](https://github.com/Redfox-Security/Asus-RT--N12-B1-s-Privilege-Escalation--CVE--2024--28326) :  ![starts](https://img.shields.io/github/stars/Redfox-Security/Asus-RT--N12-B1-s-Privilege-Escalation--CVE--2024--28326.svg) ![forks](https://img.shields.io/github/forks/Redfox-Security/Asus-RT--N12-B1-s-Privilege-Escalation--CVE--2024--28326.svg)

## CVE-2024-28325
 Asus RT-N12+ B1 router stores credentials in cleartext, which could allow local attackers to obtain unauthorized access and modify router settings.



- [https://github.com/Redfox-Security/Asus-RT-N12-B1-s-Credentials-Stored-in-Cleartext--CVE--2024--28325](https://github.com/Redfox-Security/Asus-RT-N12-B1-s-Credentials-Stored-in-Cleartext--CVE--2024--28325) :  ![starts](https://img.shields.io/github/stars/Redfox-Security/Asus-RT-N12-B1-s-Credentials-Stored-in-Cleartext--CVE--2024--28325.svg) ![forks](https://img.shields.io/github/forks/Redfox-Security/Asus-RT-N12-B1-s-Credentials-Stored-in-Cleartext--CVE--2024--28325.svg)

## CVE-2024-28255
 OpenMetadata is a unified platform for discovery, observability, and governance powered by a central metadata repository, in-depth lineage, and seamless team collaboration. The `JwtFilter` handles the API authentication by requiring and verifying JWT tokens. When a new request comes in, the request's path is checked against this list. When the request's path contains any of the excluded endpoints the filter returns without validating the JWT. Unfortunately, an attacker may use Path Parameters to make any path contain any arbitrary strings. For example, a request to `GET /api/v1;v1%2fusers%2flogin/events/subscriptions/validation/condition/111` will match the excluded endpoint condition and therefore will be processed with no JWT validation allowing an attacker to bypass the authentication mechanism and reach any arbitrary endpoint, including the ones listed above that lead to arbitrary SpEL expression injection. This bypass will not work when the endpoint uses the `SecurityContext.getUserPrincipal()` since it will return `null` and will throw an NPE. This issue may lead to authentication bypass and has been addressed in version 1.2.4. Users are advised to upgrade. There are no known workarounds for this vulnerability. This issue is also tracked as `GHSL-2023-237`.



- [https://github.com/YongYe-Security/CVE-2024-28255](https://github.com/YongYe-Security/CVE-2024-28255) :  ![starts](https://img.shields.io/github/stars/YongYe-Security/CVE-2024-28255.svg) ![forks](https://img.shields.io/github/forks/YongYe-Security/CVE-2024-28255.svg)

## CVE-2024-28247
 The Pi-hole is a DNS sinkhole that protects your devices from unwanted content without installing any client-side software. A vulnerability has been discovered in Pihole that allows an authenticated user on the platform to read internal server files arbitrarily, and because the application runs from behind, reading files is done as a privileged user.If the URL that is in the list of "Adslists" begins with "file*" it is understood that it is updating from a local file, on the other hand if it does not begin with "file*" depending on the state of the response it does one thing or another. The problem resides in the update through local files. When updating from a file which contains non-domain lines, 5 of the non-domain lines are printed on the screen, so if you provide it with any file on the server which contains non-domain lines it will print them on the screen. This vulnerability is fixed by 5.18.



- [https://github.com/T0X1Cx/CVE-2024-28247-Pi-hole-Arbitrary-File-Read](https://github.com/T0X1Cx/CVE-2024-28247-Pi-hole-Arbitrary-File-Read) :  ![starts](https://img.shields.io/github/stars/T0X1Cx/CVE-2024-28247-Pi-hole-Arbitrary-File-Read.svg) ![forks](https://img.shields.io/github/forks/T0X1Cx/CVE-2024-28247-Pi-hole-Arbitrary-File-Read.svg)

## CVE-2024-28182
 nghttp2 is an implementation of the Hypertext Transfer Protocol version 2 in C. The nghttp2 library prior to version 1.61.0 keeps reading the unbounded number of HTTP/2 CONTINUATION frames even after a stream is reset to keep HPACK context in sync.  This causes excessive CPU usage to decode HPACK stream. nghttp2 v1.61.0 mitigates this vulnerability by limiting the number of CONTINUATION frames it accepts per stream. There is no workaround for this vulnerability.



- [https://github.com/lockness-Ko/CVE-2024-27316](https://github.com/lockness-Ko/CVE-2024-27316) :  ![starts](https://img.shields.io/github/stars/lockness-Ko/CVE-2024-27316.svg) ![forks](https://img.shields.io/github/forks/lockness-Ko/CVE-2024-27316.svg)

## CVE-2024-28116
 Grav is an open-source, flat-file content management system. Grav CMS prior to version 1.7.45 is vulnerable to a Server-Side Template Injection (SSTI), which allows any authenticated user (editor permissions are sufficient) to execute arbitrary code on the remote server bypassing the existing security sandbox. Version 1.7.45 contains a patch for this issue.



- [https://github.com/akabe1/Graver](https://github.com/akabe1/Graver) :  ![starts](https://img.shields.io/github/stars/akabe1/Graver.svg) ![forks](https://img.shields.io/github/forks/akabe1/Graver.svg)

## CVE-2024-28093
 The TELNET service of AdTran NetVanta 3120 18.01.01.00.E devices is enabled by default, and has default credentials for a root-level account.



- [https://github.com/actuator/BSIDES-Security-Las-Vegas-2024](https://github.com/actuator/BSIDES-Security-Las-Vegas-2024) :  ![starts](https://img.shields.io/github/stars/actuator/BSIDES-Security-Las-Vegas-2024.svg) ![forks](https://img.shields.io/github/forks/actuator/BSIDES-Security-Las-Vegas-2024.svg)

## CVE-2024-28088
 LangChain through 0.1.10 allows ../ directory traversal by an actor who is able to control the final part of the path parameter in a load_chain call. This bypasses the intended behavior of loading configurations only from the hwchase17/langchain-hub GitHub repository. The outcome can be disclosure of an API key for a large language model online service, or remote code execution. (A patch is available as of release 0.1.29 of langchain-core.)



- [https://github.com/levpachmanov/cve-2024-28088-poc](https://github.com/levpachmanov/cve-2024-28088-poc) :  ![starts](https://img.shields.io/github/stars/levpachmanov/cve-2024-28088-poc.svg) ![forks](https://img.shields.io/github/forks/levpachmanov/cve-2024-28088-poc.svg)

## CVE-2024-28085
 wall in util-linux through 2.40, often installed with setgid tty permissions, allows escape sequences to be sent to other users' terminals through argv. (Specifically, escape sequences received from stdin are blocked, but escape sequences received from argv are not blocked.) There may be plausible scenarios where this leads to account takeover.



- [https://github.com/skyler-ferrante/CVE-2024-28085](https://github.com/skyler-ferrante/CVE-2024-28085) :  ![starts](https://img.shields.io/github/stars/skyler-ferrante/CVE-2024-28085.svg) ![forks](https://img.shields.io/github/forks/skyler-ferrante/CVE-2024-28085.svg)

## CVE-2024-27983
 An attacker can make the Node.js HTTP/2 server completely unavailable by sending a small amount of HTTP/2 frames packets with a few HTTP/2 frames inside. It is possible to leave some data in nghttp2 memory after reset when headers with HTTP/2 CONTINUATION frame are sent to the server and then a TCP connection is abruptly closed by the client triggering the Http2Session destructor while header frames are still being processed (and stored in memory) causing a race condition.



- [https://github.com/lirantal/CVE-2024-27983-nodejs-http2](https://github.com/lirantal/CVE-2024-27983-nodejs-http2) :  ![starts](https://img.shields.io/github/stars/lirantal/CVE-2024-27983-nodejs-http2.svg) ![forks](https://img.shields.io/github/forks/lirantal/CVE-2024-27983-nodejs-http2.svg)

## CVE-2024-27972
 Improper Neutralization of Special Elements used in a Command ('Command Injection') vulnerability in Very Good Plugins WP Fusion Lite allows Command Injection.This issue affects WP Fusion Lite: from n/a through 3.41.24.





- [https://github.com/truonghuuphuc/CVE-2024-27972-Poc](https://github.com/truonghuuphuc/CVE-2024-27972-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-27972-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-27972-Poc.svg)

## CVE-2024-27971
 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Premmerce Premmerce Permalink Manager for WooCommerce allows PHP Local File Inclusion.This issue affects Premmerce Permalink Manager for WooCommerce: from n/a through 2.3.10.



- [https://github.com/truonghuuphuc/CVE-2024-27971-Note](https://github.com/truonghuuphuc/CVE-2024-27971-Note) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-27971-Note.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-27971-Note.svg)

## CVE-2024-27956
 Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in ValvePress Automatic allows SQL Injection.This issue affects Automatic: from n/a through 3.92.0.





- [https://github.com/AiGptCode/WordPress-Auto-Admin-Account-and-Reverse-Shell-cve-2024-27956](https://github.com/AiGptCode/WordPress-Auto-Admin-Account-and-Reverse-Shell-cve-2024-27956) :  ![starts](https://img.shields.io/github/stars/AiGptCode/WordPress-Auto-Admin-Account-and-Reverse-Shell-cve-2024-27956.svg) ![forks](https://img.shields.io/github/forks/AiGptCode/WordPress-Auto-Admin-Account-and-Reverse-Shell-cve-2024-27956.svg)

- [https://github.com/diego-tella/CVE-2024-27956-RCE](https://github.com/diego-tella/CVE-2024-27956-RCE) :  ![starts](https://img.shields.io/github/stars/diego-tella/CVE-2024-27956-RCE.svg) ![forks](https://img.shields.io/github/forks/diego-tella/CVE-2024-27956-RCE.svg)

- [https://github.com/truonghuuphuc/CVE-2024-27956](https://github.com/truonghuuphuc/CVE-2024-27956) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-27956.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-27956.svg)

- [https://github.com/ThatNotEasy/CVE-2024-27956](https://github.com/ThatNotEasy/CVE-2024-27956) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2024-27956.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2024-27956.svg)

- [https://github.com/itzheartzz/MASS-CVE-2024-27956](https://github.com/itzheartzz/MASS-CVE-2024-27956) :  ![starts](https://img.shields.io/github/stars/itzheartzz/MASS-CVE-2024-27956.svg) ![forks](https://img.shields.io/github/forks/itzheartzz/MASS-CVE-2024-27956.svg)

- [https://github.com/Cappricio-Securities/CVE-2024-27956](https://github.com/Cappricio-Securities/CVE-2024-27956) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2024-27956.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2024-27956.svg)

- [https://github.com/devsec23/CVE-2024-27956](https://github.com/devsec23/CVE-2024-27956) :  ![starts](https://img.shields.io/github/stars/devsec23/CVE-2024-27956.svg) ![forks](https://img.shields.io/github/forks/devsec23/CVE-2024-27956.svg)

- [https://github.com/FoxyProxys/CVE-2024-27956](https://github.com/FoxyProxys/CVE-2024-27956) :  ![starts](https://img.shields.io/github/stars/FoxyProxys/CVE-2024-27956.svg) ![forks](https://img.shields.io/github/forks/FoxyProxys/CVE-2024-27956.svg)

- [https://github.com/k3ppf0r/CVE-2024-27956](https://github.com/k3ppf0r/CVE-2024-27956) :  ![starts](https://img.shields.io/github/stars/k3ppf0r/CVE-2024-27956.svg) ![forks](https://img.shields.io/github/forks/k3ppf0r/CVE-2024-27956.svg)

- [https://github.com/X-Projetion/CVE-2024-27956-WORDPRESS-RCE-PLUGIN](https://github.com/X-Projetion/CVE-2024-27956-WORDPRESS-RCE-PLUGIN) :  ![starts](https://img.shields.io/github/stars/X-Projetion/CVE-2024-27956-WORDPRESS-RCE-PLUGIN.svg) ![forks](https://img.shields.io/github/forks/X-Projetion/CVE-2024-27956-WORDPRESS-RCE-PLUGIN.svg)

- [https://github.com/cve-2024/CVE-2024-27956-RCE](https://github.com/cve-2024/CVE-2024-27956-RCE) :  ![starts](https://img.shields.io/github/stars/cve-2024/CVE-2024-27956-RCE.svg) ![forks](https://img.shields.io/github/forks/cve-2024/CVE-2024-27956-RCE.svg)

- [https://github.com/m4nInTh3mIdDle/wordpress-CVE-2024-27956](https://github.com/m4nInTh3mIdDle/wordpress-CVE-2024-27956) :  ![starts](https://img.shields.io/github/stars/m4nInTh3mIdDle/wordpress-CVE-2024-27956.svg) ![forks](https://img.shields.io/github/forks/m4nInTh3mIdDle/wordpress-CVE-2024-27956.svg)

- [https://github.com/CERTologists/EXPLOITING-CVE-2024-27956](https://github.com/CERTologists/EXPLOITING-CVE-2024-27956) :  ![starts](https://img.shields.io/github/stars/CERTologists/EXPLOITING-CVE-2024-27956.svg) ![forks](https://img.shields.io/github/forks/CERTologists/EXPLOITING-CVE-2024-27956.svg)

- [https://github.com/7aRanchi/CVE-2024-27956-for-fscan](https://github.com/7aRanchi/CVE-2024-27956-for-fscan) :  ![starts](https://img.shields.io/github/stars/7aRanchi/CVE-2024-27956-for-fscan.svg) ![forks](https://img.shields.io/github/forks/7aRanchi/CVE-2024-27956-for-fscan.svg)

- [https://github.com/TadashiJei/Valve-Press-CVE-2024-27956-RCE](https://github.com/TadashiJei/Valve-Press-CVE-2024-27956-RCE) :  ![starts](https://img.shields.io/github/stars/TadashiJei/Valve-Press-CVE-2024-27956-RCE.svg) ![forks](https://img.shields.io/github/forks/TadashiJei/Valve-Press-CVE-2024-27956-RCE.svg)

- [https://github.com/W3BW/CVE-2024-27956-RCE-File-Package](https://github.com/W3BW/CVE-2024-27956-RCE-File-Package) :  ![starts](https://img.shields.io/github/stars/W3BW/CVE-2024-27956-RCE-File-Package.svg) ![forks](https://img.shields.io/github/forks/W3BW/CVE-2024-27956-RCE-File-Package.svg)

## CVE-2024-27954
 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in WP Automatic Automatic allows Path Traversal, Server Side Request Forgery.This issue affects Automatic: from n/a through 3.92.0.



- [https://github.com/r0otk3r/CVE-2024-27954](https://github.com/r0otk3r/CVE-2024-27954) :  ![starts](https://img.shields.io/github/stars/r0otk3r/CVE-2024-27954.svg) ![forks](https://img.shields.io/github/forks/r0otk3r/CVE-2024-27954.svg)

## CVE-2024-27919
 Envoy is a cloud-native, open-source edge and service proxy. In versions 1.29.0 and 1.29.1, theEnvoy HTTP/2 protocol stack is vulnerable to the flood of CONTINUATION frames. Envoy's HTTP/2 codec does not reset a request when header map limits have been exceeded. This allows an attacker to send an sequence of CONTINUATION frames without the END_HEADERS bit set causing unlimited memory consumption. This can lead to denial of service through memory exhaustion. Users should upgrade to versions 1.29.2 to mitigate the effects of the CONTINUATION flood. Note that this vulnerability is a regression in Envoy version 1.29.0 and 1.29.1 only. As a workaround, downgrade to version 1.28.1 or earlier or disable HTTP/2 protocol for downstream connections.



- [https://github.com/lockness-Ko/CVE-2024-27316](https://github.com/lockness-Ko/CVE-2024-27316) :  ![starts](https://img.shields.io/github/stars/lockness-Ko/CVE-2024-27316.svg) ![forks](https://img.shields.io/github/forks/lockness-Ko/CVE-2024-27316.svg)

## CVE-2024-27914
 GLPI is a Free Asset and IT Management Software package, Data center management, ITIL Service Desk, licenses tracking and software auditing. An unauthenticated user can provide a malicious link to a GLPI administrator in order to exploit a reflected XSS  vulnerability. The XSS will only trigger if the administrator navigates through the debug bar. This issue has been patched in version 10.0.13.




- [https://github.com/shellkraft/CVE-2024-27914](https://github.com/shellkraft/CVE-2024-27914) :  ![starts](https://img.shields.io/github/stars/shellkraft/CVE-2024-27914.svg) ![forks](https://img.shields.io/github/forks/shellkraft/CVE-2024-27914.svg)

## CVE-2024-27876
 A race condition was addressed with improved locking. This issue is fixed in macOS Ventura 13.7, iOS 17.7 and iPadOS 17.7, visionOS 2, iOS 18 and iPadOS 18, macOS Sonoma 14.7, macOS Sequoia 15. Unpacking a maliciously crafted archive may allow an attacker to write arbitrary files.



- [https://github.com/0xilis/CVE-2024-27876](https://github.com/0xilis/CVE-2024-27876) :  ![starts](https://img.shields.io/github/stars/0xilis/CVE-2024-27876.svg) ![forks](https://img.shields.io/github/forks/0xilis/CVE-2024-27876.svg)

## CVE-2024-27821
 A path handling issue was addressed with improved validation. This issue is fixed in iOS 17.5 and iPadOS 17.5, watchOS 10.5, macOS Sonoma 14.5. A shortcut may output sensitive user data without consent.



- [https://github.com/0xilis/CVE-2024-27821](https://github.com/0xilis/CVE-2024-27821) :  ![starts](https://img.shields.io/github/stars/0xilis/CVE-2024-27821.svg) ![forks](https://img.shields.io/github/forks/0xilis/CVE-2024-27821.svg)

## CVE-2024-27815
 An out-of-bounds write issue was addressed with improved input validation. This issue is fixed in tvOS 17.5, visionOS 1.2, iOS 17.5 and iPadOS 17.5, watchOS 10.5, macOS Sonoma 14.5. An app may be able to execute arbitrary code with kernel privileges.



- [https://github.com/jprx/CVE-2024-27815](https://github.com/jprx/CVE-2024-27815) :  ![starts](https://img.shields.io/github/stars/jprx/CVE-2024-27815.svg) ![forks](https://img.shields.io/github/forks/jprx/CVE-2024-27815.svg)

## CVE-2024-27804
 The issue was addressed with improved memory handling. This issue is fixed in iOS 17.5 and iPadOS 17.5, tvOS 17.5, watchOS 10.5, macOS Sonoma 14.5. An app may be able to execute arbitrary code with kernel privileges.



- [https://github.com/R00tkitSMM/CVE-2024-27804](https://github.com/R00tkitSMM/CVE-2024-27804) :  ![starts](https://img.shields.io/github/stars/R00tkitSMM/CVE-2024-27804.svg) ![forks](https://img.shields.io/github/forks/R00tkitSMM/CVE-2024-27804.svg)

- [https://github.com/a0zhar/QuarkPoC](https://github.com/a0zhar/QuarkPoC) :  ![starts](https://img.shields.io/github/stars/a0zhar/QuarkPoC.svg) ![forks](https://img.shields.io/github/forks/a0zhar/QuarkPoC.svg)

## CVE-2024-27766
 An issue in MariaDB v.11.1 allows a remote attacker to execute arbitrary code via the lib_mysqludf_sys.so function. NOTE: this is disputed by the MariaDB Foundation because no privilege boundary is crossed.



- [https://github.com/Ant1sec-ops/CVE-2024-27766](https://github.com/Ant1sec-ops/CVE-2024-27766) :  ![starts](https://img.shields.io/github/stars/Ant1sec-ops/CVE-2024-27766.svg) ![forks](https://img.shields.io/github/forks/Ant1sec-ops/CVE-2024-27766.svg)

## CVE-2024-27697
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/SanjinDedic/FuguHub-8.4-Authenticated-RCE-CVE-2024-27697](https://github.com/SanjinDedic/FuguHub-8.4-Authenticated-RCE-CVE-2024-27697) :  ![starts](https://img.shields.io/github/stars/SanjinDedic/FuguHub-8.4-Authenticated-RCE-CVE-2024-27697.svg) ![forks](https://img.shields.io/github/forks/SanjinDedic/FuguHub-8.4-Authenticated-RCE-CVE-2024-27697.svg)

## CVE-2024-27674
 Macro Expert through 4.9.4 allows BUILTIN\Users:(OI)(CI)(M) access to the "%PROGRAMFILES(X86)%\GrassSoft\Macro Expert" folder and thus an unprivileged user can escalate to SYSTEM by replacing the MacroService.exe binary.



- [https://github.com/Alaatk/CVE-2024-27674](https://github.com/Alaatk/CVE-2024-27674) :  ![starts](https://img.shields.io/github/stars/Alaatk/CVE-2024-27674.svg) ![forks](https://img.shields.io/github/forks/Alaatk/CVE-2024-27674.svg)

## CVE-2024-27673
 DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: none. Reason: This candidate was withdrawn by its CNA. Further investigation showed that it was not a security issue. Notes: none.



- [https://github.com/Alaatk/CVE-2024-27673](https://github.com/Alaatk/CVE-2024-27673) :  ![starts](https://img.shields.io/github/stars/Alaatk/CVE-2024-27673.svg) ![forks](https://img.shields.io/github/forks/Alaatk/CVE-2024-27673.svg)

## CVE-2024-27665
 Unifiedtransform v2.X is vulnerable to Stored Cross-Site Scripting (XSS) via file upload feature in Syllabus module.



- [https://github.com/Thirukrishnan/CVE-2024-27665](https://github.com/Thirukrishnan/CVE-2024-27665) :  ![starts](https://img.shields.io/github/stars/Thirukrishnan/CVE-2024-27665.svg) ![forks](https://img.shields.io/github/forks/Thirukrishnan/CVE-2024-27665.svg)

## CVE-2024-27632
 An issue in GNU Savane v.3.12 and before allows a remote attacker to escalate privileges via the form_id in the form_header() function.



- [https://github.com/ally-petitt/CVE-2024-27632](https://github.com/ally-petitt/CVE-2024-27632) :  ![starts](https://img.shields.io/github/stars/ally-petitt/CVE-2024-27632.svg) ![forks](https://img.shields.io/github/forks/ally-petitt/CVE-2024-27632.svg)

## CVE-2024-27631
 Cross Site Request Forgery vulnerability in GNU Savane v.3.12 and before allows a remote attacker to escalate privileges via siteadmin/usergroup.php



- [https://github.com/ally-petitt/CVE-2024-27631](https://github.com/ally-petitt/CVE-2024-27631) :  ![starts](https://img.shields.io/github/stars/ally-petitt/CVE-2024-27631.svg) ![forks](https://img.shields.io/github/forks/ally-petitt/CVE-2024-27631.svg)

## CVE-2024-27630
 Insecure Direct Object Reference (IDOR) in GNU Savane v.3.12 and before allows a remote attacker to delete arbitrary files via crafted input to the trackers_data_delete_file function.



- [https://github.com/ally-petitt/CVE-2024-27630](https://github.com/ally-petitt/CVE-2024-27630) :  ![starts](https://img.shields.io/github/stars/ally-petitt/CVE-2024-27630.svg) ![forks](https://img.shields.io/github/forks/ally-petitt/CVE-2024-27630.svg)

## CVE-2024-27619
 Dlink Dir-3040us A1 1.20b03a hotfix is vulnerable to Buffer Overflow. Any user having read/write access to ftp server can write directly to ram causing buffer overflow if file or files uploaded are greater than available ram. Ftp server allows change of directory to root which is one level up than root of usb flash directory. During upload ram is getting filled and causing system resource exhaustion (no free memory) which causes system to crash and reboot.



- [https://github.com/ioprojecton/dir-3040_dos](https://github.com/ioprojecton/dir-3040_dos) :  ![starts](https://img.shields.io/github/stars/ioprojecton/dir-3040_dos.svg) ![forks](https://img.shields.io/github/forks/ioprojecton/dir-3040_dos.svg)

## CVE-2024-27518
 An issue in SUPERAntiSyware Professional X 10.0.1262 and 10.0.1264 allows unprivileged attackers to escalate privileges via a restore of a crafted DLL file into the C:\Program Files\SUPERAntiSpyware folder.



- [https://github.com/secunnix/CVE-2024-27518](https://github.com/secunnix/CVE-2024-27518) :  ![starts](https://img.shields.io/github/stars/secunnix/CVE-2024-27518.svg) ![forks](https://img.shields.io/github/forks/secunnix/CVE-2024-27518.svg)

## CVE-2024-27477
 In Leantime 3.0.6, a Cross-Site Scripting vulnerability exists within the ticket creation and modification functionality, allowing attackers to inject malicious JavaScript code into the title field of tickets (also known as to-dos). This stored XSS vulnerability can be exploited to perform Server-Side Request Forgery (SSRF) attacks.



- [https://github.com/dead1nfluence/Leantime-POC](https://github.com/dead1nfluence/Leantime-POC) :  ![starts](https://img.shields.io/github/stars/dead1nfluence/Leantime-POC.svg) ![forks](https://img.shields.io/github/forks/dead1nfluence/Leantime-POC.svg)

## CVE-2024-27476
 Leantime 3.0.6 is vulnerable to HTML Injection via /dashboard/show#/tickets/newTicket.



- [https://github.com/dead1nfluence/Leantime-POC](https://github.com/dead1nfluence/Leantime-POC) :  ![starts](https://img.shields.io/github/stars/dead1nfluence/Leantime-POC.svg) ![forks](https://img.shields.io/github/forks/dead1nfluence/Leantime-POC.svg)

## CVE-2024-27474
 Leantime 3.0.6 is vulnerable to Cross Site Request Forgery (CSRF). This vulnerability allows malicious actors to perform unauthorized actions on behalf of authenticated users, specifically administrators.



- [https://github.com/dead1nfluence/Leantime-POC](https://github.com/dead1nfluence/Leantime-POC) :  ![starts](https://img.shields.io/github/stars/dead1nfluence/Leantime-POC.svg) ![forks](https://img.shields.io/github/forks/dead1nfluence/Leantime-POC.svg)

## CVE-2024-27462
 DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: none. Reason: This candidate was withdrawn by its CNA. Further investigation showed that it was not a security issue. Notes: none.



- [https://github.com/Alaatk/CVE-2024-27462](https://github.com/Alaatk/CVE-2024-27462) :  ![starts](https://img.shields.io/github/stars/Alaatk/CVE-2024-27462.svg) ![forks](https://img.shields.io/github/forks/Alaatk/CVE-2024-27462.svg)

## CVE-2024-27460
 A privilege escalation exists in the updater for Plantronics Hub 3.25.1 and below.



- [https://github.com/xct/CVE-2024-27460](https://github.com/xct/CVE-2024-27460) :  ![starts](https://img.shields.io/github/stars/xct/CVE-2024-27460.svg) ![forks](https://img.shields.io/github/forks/xct/CVE-2024-27460.svg)

- [https://github.com/Alaatk/CVE-2024-27460](https://github.com/Alaatk/CVE-2024-27460) :  ![starts](https://img.shields.io/github/stars/Alaatk/CVE-2024-27460.svg) ![forks](https://img.shields.io/github/forks/Alaatk/CVE-2024-27460.svg)

- [https://github.com/10cks/CVE-2024-27460-installer](https://github.com/10cks/CVE-2024-27460-installer) :  ![starts](https://img.shields.io/github/stars/10cks/CVE-2024-27460-installer.svg) ![forks](https://img.shields.io/github/forks/10cks/CVE-2024-27460-installer.svg)

## CVE-2024-27348
 RCE-Remote Command Execution vulnerability in Apache HugeGraph-Server.This issue affects Apache HugeGraph-Server: from 1.0.0 before 1.3.0 in Java8 & Java11

Users are recommended to upgrade to version 1.3.0 with Java11 & enable the Auth system, which fixes the issue.



- [https://github.com/Zeyad-Azima/CVE-2024-27348](https://github.com/Zeyad-Azima/CVE-2024-27348) :  ![starts](https://img.shields.io/github/stars/Zeyad-Azima/CVE-2024-27348.svg) ![forks](https://img.shields.io/github/forks/Zeyad-Azima/CVE-2024-27348.svg)

- [https://github.com/kljunowsky/CVE-2024-27348](https://github.com/kljunowsky/CVE-2024-27348) :  ![starts](https://img.shields.io/github/stars/kljunowsky/CVE-2024-27348.svg) ![forks](https://img.shields.io/github/forks/kljunowsky/CVE-2024-27348.svg)

- [https://github.com/jakabakos/CVE-2024-27348-Apache-HugeGraph-RCE](https://github.com/jakabakos/CVE-2024-27348-Apache-HugeGraph-RCE) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2024-27348-Apache-HugeGraph-RCE.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2024-27348-Apache-HugeGraph-RCE.svg)

## CVE-2024-27316
 HTTP/2 incoming headers exceeding the limit are temporarily buffered in nghttp2 in order to generate an informative HTTP 413 response. If a client does not stop sending headers, this leads to memory exhaustion.



- [https://github.com/lockness-Ko/CVE-2024-27316](https://github.com/lockness-Ko/CVE-2024-27316) :  ![starts](https://img.shields.io/github/stars/lockness-Ko/CVE-2024-27316.svg) ![forks](https://img.shields.io/github/forks/lockness-Ko/CVE-2024-27316.svg)

- [https://github.com/aeyesec/CVE-2024-27316_poc](https://github.com/aeyesec/CVE-2024-27316_poc) :  ![starts](https://img.shields.io/github/stars/aeyesec/CVE-2024-27316_poc.svg) ![forks](https://img.shields.io/github/forks/aeyesec/CVE-2024-27316_poc.svg)

## CVE-2024-27292
 Docassemble is an expert system for guided interviews and document assembly. The vulnerability allows attackers to gain unauthorized access to information on the system through URL manipulation. It affects versions 1.4.53 to 1.4.96. The vulnerability has been patched in version 1.4.97 of the master branch.



- [https://github.com/th3gokul/CVE-2024-27292](https://github.com/th3gokul/CVE-2024-27292) :  ![starts](https://img.shields.io/github/stars/th3gokul/CVE-2024-27292.svg) ![forks](https://img.shields.io/github/forks/th3gokul/CVE-2024-27292.svg)

- [https://github.com/NingXin2002/Docassemble_poc](https://github.com/NingXin2002/Docassemble_poc) :  ![starts](https://img.shields.io/github/stars/NingXin2002/Docassemble_poc.svg) ![forks](https://img.shields.io/github/forks/NingXin2002/Docassemble_poc.svg)

- [https://github.com/tequilasunsh1ne/CVE_2024_27292](https://github.com/tequilasunsh1ne/CVE_2024_27292) :  ![starts](https://img.shields.io/github/stars/tequilasunsh1ne/CVE_2024_27292.svg) ![forks](https://img.shields.io/github/forks/tequilasunsh1ne/CVE_2024_27292.svg)

## CVE-2024-27199
 In JetBrains TeamCity before 2023.11.4 path traversal allowing to perform limited admin actions  was possible



- [https://github.com/W01fh4cker/CVE-2024-27198-RCE](https://github.com/W01fh4cker/CVE-2024-27198-RCE) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/CVE-2024-27198-RCE.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/CVE-2024-27198-RCE.svg)

- [https://github.com/Stuub/RCity-CVE-2024-27198](https://github.com/Stuub/RCity-CVE-2024-27198) :  ![starts](https://img.shields.io/github/stars/Stuub/RCity-CVE-2024-27198.svg) ![forks](https://img.shields.io/github/forks/Stuub/RCity-CVE-2024-27198.svg)

- [https://github.com/Shimon03/Explora-o-RCE-n-o-autenticado-JetBrains-TeamCity-CVE-2024-27198-](https://github.com/Shimon03/Explora-o-RCE-n-o-autenticado-JetBrains-TeamCity-CVE-2024-27198-) :  ![starts](https://img.shields.io/github/stars/Shimon03/Explora-o-RCE-n-o-autenticado-JetBrains-TeamCity-CVE-2024-27198-.svg) ![forks](https://img.shields.io/github/forks/Shimon03/Explora-o-RCE-n-o-autenticado-JetBrains-TeamCity-CVE-2024-27198-.svg)

## CVE-2024-27198
 In JetBrains TeamCity before 2023.11.4 authentication bypass allowing to perform admin actions was possible



- [https://github.com/W01fh4cker/CVE-2024-27198-RCE](https://github.com/W01fh4cker/CVE-2024-27198-RCE) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/CVE-2024-27198-RCE.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/CVE-2024-27198-RCE.svg)

- [https://github.com/Chocapikk/CVE-2024-27198](https://github.com/Chocapikk/CVE-2024-27198) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-27198.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-27198.svg)

- [https://github.com/yoryio/CVE-2024-27198](https://github.com/yoryio/CVE-2024-27198) :  ![starts](https://img.shields.io/github/stars/yoryio/CVE-2024-27198.svg) ![forks](https://img.shields.io/github/forks/yoryio/CVE-2024-27198.svg)

- [https://github.com/Stuub/RCity-CVE-2024-27198](https://github.com/Stuub/RCity-CVE-2024-27198) :  ![starts](https://img.shields.io/github/stars/Stuub/RCity-CVE-2024-27198.svg) ![forks](https://img.shields.io/github/forks/Stuub/RCity-CVE-2024-27198.svg)

- [https://github.com/K3ysTr0K3R/CVE-2024-27198-EXPLOIT](https://github.com/K3ysTr0K3R/CVE-2024-27198-EXPLOIT) :  ![starts](https://img.shields.io/github/stars/K3ysTr0K3R/CVE-2024-27198-EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/K3ysTr0K3R/CVE-2024-27198-EXPLOIT.svg)

- [https://github.com/CharonDefalt/CVE-2024-27198-RCE](https://github.com/CharonDefalt/CVE-2024-27198-RCE) :  ![starts](https://img.shields.io/github/stars/CharonDefalt/CVE-2024-27198-RCE.svg) ![forks](https://img.shields.io/github/forks/CharonDefalt/CVE-2024-27198-RCE.svg)

- [https://github.com/passwa11/CVE-2024-27198-RCE](https://github.com/passwa11/CVE-2024-27198-RCE) :  ![starts](https://img.shields.io/github/stars/passwa11/CVE-2024-27198-RCE.svg) ![forks](https://img.shields.io/github/forks/passwa11/CVE-2024-27198-RCE.svg)

- [https://github.com/rampantspark/CVE-2024-27198](https://github.com/rampantspark/CVE-2024-27198) :  ![starts](https://img.shields.io/github/stars/rampantspark/CVE-2024-27198.svg) ![forks](https://img.shields.io/github/forks/rampantspark/CVE-2024-27198.svg)

- [https://github.com/HPT-Intern-Task-Submission/CVE-2024-27198](https://github.com/HPT-Intern-Task-Submission/CVE-2024-27198) :  ![starts](https://img.shields.io/github/stars/HPT-Intern-Task-Submission/CVE-2024-27198.svg) ![forks](https://img.shields.io/github/forks/HPT-Intern-Task-Submission/CVE-2024-27198.svg)

- [https://github.com/Shimon03/Explora-o-RCE-n-o-autenticado-JetBrains-TeamCity-CVE-2024-27198-](https://github.com/Shimon03/Explora-o-RCE-n-o-autenticado-JetBrains-TeamCity-CVE-2024-27198-) :  ![starts](https://img.shields.io/github/stars/Shimon03/Explora-o-RCE-n-o-autenticado-JetBrains-TeamCity-CVE-2024-27198-.svg) ![forks](https://img.shields.io/github/forks/Shimon03/Explora-o-RCE-n-o-autenticado-JetBrains-TeamCity-CVE-2024-27198-.svg)

## CVE-2024-27173
 Remote Command program allows an attacker to get Remote Code Execution by overwriting existing Python files containing executable code. This vulnerability can be executed in combination with other vulnerabilities and  difficult to execute alone. So, the CVSS score for this vulnerability alone is lower than the score listed in the "Base Score" of this vulnerability. For detail on related other vulnerabilities, please ask to the below contact point.
 https://www.toshibatec.com/contacts/products/ 
As for the affected products/models/versions, see the reference URL.



- [https://github.com/Ieakd/0day-POC-for-CVE-2024-27173](https://github.com/Ieakd/0day-POC-for-CVE-2024-27173) :  ![starts](https://img.shields.io/github/stars/Ieakd/0day-POC-for-CVE-2024-27173.svg) ![forks](https://img.shields.io/github/forks/Ieakd/0day-POC-for-CVE-2024-27173.svg)

## CVE-2024-27130
 A buffer copy without checking size of input vulnerability has been reported to affect several QNAP operating system versions. If exploited, the vulnerability could allow users to execute code via a network.

We have already fixed the vulnerability in the following version:
QTS 5.1.7.2770 build 20240520 and later
QuTS hero h5.1.7.2770 build 20240520 and later



- [https://github.com/watchtowrlabs/CVE-2024-27130](https://github.com/watchtowrlabs/CVE-2024-27130) :  ![starts](https://img.shields.io/github/stars/watchtowrlabs/CVE-2024-27130.svg) ![forks](https://img.shields.io/github/forks/watchtowrlabs/CVE-2024-27130.svg)

- [https://github.com/XiaomingX/cve-2024-27130-poc](https://github.com/XiaomingX/cve-2024-27130-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-27130-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-27130-poc.svg)

- [https://github.com/d0rb/CVE-2024-27130](https://github.com/d0rb/CVE-2024-27130) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2024-27130.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2024-27130.svg)

## CVE-2024-27115
 A unauthenticated Remote Code Execution (RCE) vulnerability is found in the SO Planning online planning tool. With this vulnerability, an attacker can upload executable files that are moved to a publicly accessible folder before verifying any requirements. This leads to the possibility of execution of code on the underlying system when the file is triggered. The vulnerability has been remediated in version 1.52.02.



- [https://github.com/theexploiters/CVE-2024-27115-Exploit](https://github.com/theexploiters/CVE-2024-27115-Exploit) :  ![starts](https://img.shields.io/github/stars/theexploiters/CVE-2024-27115-Exploit.svg) ![forks](https://img.shields.io/github/forks/theexploiters/CVE-2024-27115-Exploit.svg)

## CVE-2024-26817
 In the Linux kernel, the following vulnerability has been resolved:

amdkfd: use calloc instead of kzalloc to avoid integer overflow

This uses calloc instead of doing the multiplication which might
overflow.



- [https://github.com/MaherAzzouzi/CVE-2024-26817-amdkfd](https://github.com/MaherAzzouzi/CVE-2024-26817-amdkfd) :  ![starts](https://img.shields.io/github/stars/MaherAzzouzi/CVE-2024-26817-amdkfd.svg) ![forks](https://img.shields.io/github/forks/MaherAzzouzi/CVE-2024-26817-amdkfd.svg)

## CVE-2024-26574
 Insecure Permissions vulnerability in Wondershare Filmora v.13.0.51 allows a local attacker to execute arbitrary code via a crafted script to the WSNativePushService.exe



- [https://github.com/Alaatk/CVE-2024-26574](https://github.com/Alaatk/CVE-2024-26574) :  ![starts](https://img.shields.io/github/stars/Alaatk/CVE-2024-26574.svg) ![forks](https://img.shields.io/github/forks/Alaatk/CVE-2024-26574.svg)

## CVE-2024-26560
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/sajaljat/CVE-2024-26560](https://github.com/sajaljat/CVE-2024-26560) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-26560.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-26560.svg)

## CVE-2024-26535
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/sajaljat/CVE-2024-26535](https://github.com/sajaljat/CVE-2024-26535) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-26535.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-26535.svg)

## CVE-2024-26534
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/sajaljat/CVE-2024-26534](https://github.com/sajaljat/CVE-2024-26534) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-26534.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-26534.svg)

## CVE-2024-26521
 HTML Injection vulnerability in CE Phoenix v1.0.8.20 and before allows a remote attacker to execute arbitrary code, escalate privileges, and obtain sensitive information via a crafted payload to the english.php component.



- [https://github.com/hackervegas001/CVE-2024-26521](https://github.com/hackervegas001/CVE-2024-26521) :  ![starts](https://img.shields.io/github/stars/hackervegas001/CVE-2024-26521.svg) ![forks](https://img.shields.io/github/forks/hackervegas001/CVE-2024-26521.svg)

## CVE-2024-26503
 Unrestricted File Upload vulnerability in Greek Universities Network Open eClass v.3.15 and earlier allows attackers to run arbitrary code via upload of crafted file to certbadge.php endpoint.



- [https://github.com/RoboGR00t/Exploit-CVE-2024-26503](https://github.com/RoboGR00t/Exploit-CVE-2024-26503) :  ![starts](https://img.shields.io/github/stars/RoboGR00t/Exploit-CVE-2024-26503.svg) ![forks](https://img.shields.io/github/forks/RoboGR00t/Exploit-CVE-2024-26503.svg)

## CVE-2024-26475
 An issue in radareorg radare2 v.0.9.7 through v.5.8.6 and fixed in v.5.8.8 allows a local attacker to cause a denial of service via the grub_sfs_read_extent function.



- [https://github.com/TronciuVlad/CVE-2024-26475](https://github.com/TronciuVlad/CVE-2024-26475) :  ![starts](https://img.shields.io/github/stars/TronciuVlad/CVE-2024-26475.svg) ![forks](https://img.shields.io/github/forks/TronciuVlad/CVE-2024-26475.svg)

## CVE-2024-26308
 Allocation of Resources Without Limits or Throttling vulnerability in Apache Commons Compress.This issue affects Apache Commons Compress: from 1.21 before 1.26.

Users are recommended to upgrade to version 1.26, which fixes the issue.



- [https://github.com/crazycatMyopic/cve](https://github.com/crazycatMyopic/cve) :  ![starts](https://img.shields.io/github/stars/crazycatMyopic/cve.svg) ![forks](https://img.shields.io/github/forks/crazycatMyopic/cve.svg)

## CVE-2024-26230
 Windows Telephony Server Elevation of Privilege Vulnerability



- [https://github.com/kiwids0220/CVE-2024-26230](https://github.com/kiwids0220/CVE-2024-26230) :  ![starts](https://img.shields.io/github/stars/kiwids0220/CVE-2024-26230.svg) ![forks](https://img.shields.io/github/forks/kiwids0220/CVE-2024-26230.svg)

## CVE-2024-26229
 Windows CSC Service Elevation of Privilege Vulnerability



- [https://github.com/RalfHacker/CVE-2024-26229-exploit](https://github.com/RalfHacker/CVE-2024-26229-exploit) :  ![starts](https://img.shields.io/github/stars/RalfHacker/CVE-2024-26229-exploit.svg) ![forks](https://img.shields.io/github/forks/RalfHacker/CVE-2024-26229-exploit.svg)

- [https://github.com/Cracked5pider/eop24-26229](https://github.com/Cracked5pider/eop24-26229) :  ![starts](https://img.shields.io/github/stars/Cracked5pider/eop24-26229.svg) ![forks](https://img.shields.io/github/forks/Cracked5pider/eop24-26229.svg)

- [https://github.com/apkc/CVE-2024-26229-BOF](https://github.com/apkc/CVE-2024-26229-BOF) :  ![starts](https://img.shields.io/github/stars/apkc/CVE-2024-26229-BOF.svg) ![forks](https://img.shields.io/github/forks/apkc/CVE-2024-26229-BOF.svg)

- [https://github.com/team-MineDEV/CVE-2024-26229](https://github.com/team-MineDEV/CVE-2024-26229) :  ![starts](https://img.shields.io/github/stars/team-MineDEV/CVE-2024-26229.svg) ![forks](https://img.shields.io/github/forks/team-MineDEV/CVE-2024-26229.svg)

- [https://github.com/shinspace92/cve-2024-26229](https://github.com/shinspace92/cve-2024-26229) :  ![starts](https://img.shields.io/github/stars/shinspace92/cve-2024-26229.svg) ![forks](https://img.shields.io/github/forks/shinspace92/cve-2024-26229.svg)

- [https://github.com/dkstar11q/CVE-2024-26229-lpe](https://github.com/dkstar11q/CVE-2024-26229-lpe) :  ![starts](https://img.shields.io/github/stars/dkstar11q/CVE-2024-26229-lpe.svg) ![forks](https://img.shields.io/github/forks/dkstar11q/CVE-2024-26229-lpe.svg)

## CVE-2024-26218
 Windows Kernel Elevation of Privilege Vulnerability



- [https://github.com/exploits-forsale/CVE-2024-26218](https://github.com/exploits-forsale/CVE-2024-26218) :  ![starts](https://img.shields.io/github/stars/exploits-forsale/CVE-2024-26218.svg) ![forks](https://img.shields.io/github/forks/exploits-forsale/CVE-2024-26218.svg)

## CVE-2024-26144
 Rails is a web-application framework. Starting with version 5.2.0, there is a possible sensitive session information leak in Active Storage. By default, Active Storage sends a Set-Cookie header along with the user's session cookie when serving blobs. It also sets Cache-Control to public. Certain proxies may cache the Set-Cookie, leading to an information leak. The vulnerability is fixed in 7.0.8.1 and 6.1.7.7.



- [https://github.com/gmo-ierae/CVE-2024-26144-test](https://github.com/gmo-ierae/CVE-2024-26144-test) :  ![starts](https://img.shields.io/github/stars/gmo-ierae/CVE-2024-26144-test.svg) ![forks](https://img.shields.io/github/forks/gmo-ierae/CVE-2024-26144-test.svg)

## CVE-2024-26026
 


An SQL injection vulnerability exists in the BIG-IP Next Central Manager API (URI).  Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated





- [https://github.com/passwa11/CVE-2024-26026](https://github.com/passwa11/CVE-2024-26026) :  ![starts](https://img.shields.io/github/stars/passwa11/CVE-2024-26026.svg) ![forks](https://img.shields.io/github/forks/passwa11/CVE-2024-26026.svg)

- [https://github.com/GRTMALDET/Big-IP-Next-CVE-2024-26026](https://github.com/GRTMALDET/Big-IP-Next-CVE-2024-26026) :  ![starts](https://img.shields.io/github/stars/GRTMALDET/Big-IP-Next-CVE-2024-26026.svg) ![forks](https://img.shields.io/github/forks/GRTMALDET/Big-IP-Next-CVE-2024-26026.svg)

## CVE-2024-25897
 ChurchCRM 5.5.0 FRCatalog.php is vulnerable to Blind SQL Injection (Time-based) via the CurrentFundraiser GET parameter.



- [https://github.com/i-100-user/CVE-2024-25897](https://github.com/i-100-user/CVE-2024-25897) :  ![starts](https://img.shields.io/github/stars/i-100-user/CVE-2024-25897.svg) ![forks](https://img.shields.io/github/forks/i-100-user/CVE-2024-25897.svg)

## CVE-2024-25832
 F-logic DataCube3 v1.0 is vulnerable to unrestricted file upload, which could allow an authenticated malicious actor to upload a file of dangerous type by manipulating the filename extension.



- [https://github.com/0xNslabs/CVE-2024-25832-PoC](https://github.com/0xNslabs/CVE-2024-25832-PoC) :  ![starts](https://img.shields.io/github/stars/0xNslabs/CVE-2024-25832-PoC.svg) ![forks](https://img.shields.io/github/forks/0xNslabs/CVE-2024-25832-PoC.svg)

## CVE-2024-25830
 F-logic DataCube3 v1.0 is vulnerable to Incorrect Access Control due to an improper directory access restriction. An unauthenticated, remote attacker can exploit this, by sending a URI that contains the path of the configuration file. A successful exploit could allow the attacker to extract the root and admin password.



- [https://github.com/0xNslabs/CVE-2024-25832-PoC](https://github.com/0xNslabs/CVE-2024-25832-PoC) :  ![starts](https://img.shields.io/github/stars/0xNslabs/CVE-2024-25832-PoC.svg) ![forks](https://img.shields.io/github/forks/0xNslabs/CVE-2024-25832-PoC.svg)

## CVE-2024-25809
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/sajaljat/CVE-2024-25809](https://github.com/sajaljat/CVE-2024-25809) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-25809.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-25809.svg)

## CVE-2024-25733
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/hackintoanetwork/ARC-Browser-Address-Bar-Spoofing-PoC](https://github.com/hackintoanetwork/ARC-Browser-Address-Bar-Spoofing-PoC) :  ![starts](https://img.shields.io/github/stars/hackintoanetwork/ARC-Browser-Address-Bar-Spoofing-PoC.svg) ![forks](https://img.shields.io/github/forks/hackintoanetwork/ARC-Browser-Address-Bar-Spoofing-PoC.svg)

## CVE-2024-25731
 The Elink Smart eSmartCam (com.cn.dq.ipc) application 2.1.5 for Android contains hardcoded AES encryption keys that can be extracted from a binary file. Thus, encryption can be defeated by an attacker who can observe packet data (e.g., over Wi-Fi).



- [https://github.com/actuator/com.cn.dq.ipc](https://github.com/actuator/com.cn.dq.ipc) :  ![starts](https://img.shields.io/github/stars/actuator/com.cn.dq.ipc.svg) ![forks](https://img.shields.io/github/forks/actuator/com.cn.dq.ipc.svg)

## CVE-2024-25729
 Arris SBG6580 devices have predictable default WPA2 security passwords that could lead to unauthorized remote access. (They use the first 6 characters of the SSID and the last 6 characters of the BSSID, decrementing the last octet.)



- [https://github.com/actuator/BSIDES-Security-Las-Vegas-2024](https://github.com/actuator/BSIDES-Security-Las-Vegas-2024) :  ![starts](https://img.shields.io/github/stars/actuator/BSIDES-Security-Las-Vegas-2024.svg) ![forks](https://img.shields.io/github/forks/actuator/BSIDES-Security-Las-Vegas-2024.svg)

## CVE-2024-25723
 ZenML Server in the ZenML machine learning package before 0.46.7 for Python allows remote privilege escalation because the /api/v1/users/{user_name_or_id}/activate REST API endpoint allows access on the basis of a valid username along with a new password in the request body. These are also patched versions: 0.44.4, 0.43.1, and 0.42.2.



- [https://github.com/david-botelho-mariano/exploit-CVE-2024-25723](https://github.com/david-botelho-mariano/exploit-CVE-2024-25723) :  ![starts](https://img.shields.io/github/stars/david-botelho-mariano/exploit-CVE-2024-25723.svg) ![forks](https://img.shields.io/github/forks/david-botelho-mariano/exploit-CVE-2024-25723.svg)

## CVE-2024-25641
 Cacti provides an operational monitoring and fault management framework. Prior to version 1.2.27, an arbitrary file write vulnerability, exploitable through the "Package Import" feature, allows authenticated users having the "Import Templates" permission to execute arbitrary PHP code on the web server. The vulnerability is located within the `import_package()` function defined into the `/lib/import.php` script. The function blindly trusts the filename and file content provided within the XML data, and writes such files into the Cacti base path (or even outside, since path traversal sequences are not filtered). This can be exploited to write or overwrite arbitrary files on the web server, leading to execution of arbitrary PHP code or other security impacts. Version 1.2.27 contains a patch for this issue.



- [https://github.com/XiaomingX/cve-2024-25641-poc](https://github.com/XiaomingX/cve-2024-25641-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-25641-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-25641-poc.svg)

- [https://github.com/D3Ext/CVE-2024-25641](https://github.com/D3Ext/CVE-2024-25641) :  ![starts](https://img.shields.io/github/stars/D3Ext/CVE-2024-25641.svg) ![forks](https://img.shields.io/github/forks/D3Ext/CVE-2024-25641.svg)

## CVE-2024-25600
 Improper Control of Generation of Code ('Code Injection') vulnerability in Codeer Limited Bricks Builder allows Code Injection.This issue affects Bricks Builder: from n/a through 1.9.6.



- [https://github.com/gobysec/Goby](https://github.com/gobysec/Goby) :  ![starts](https://img.shields.io/github/stars/gobysec/Goby.svg) ![forks](https://img.shields.io/github/forks/gobysec/Goby.svg)

- [https://github.com/gobysec/GobyVuls](https://github.com/gobysec/GobyVuls) :  ![starts](https://img.shields.io/github/stars/gobysec/GobyVuls.svg) ![forks](https://img.shields.io/github/forks/gobysec/GobyVuls.svg)

- [https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance](https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance) :  ![starts](https://img.shields.io/github/stars/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg) ![forks](https://img.shields.io/github/forks/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg)

- [https://github.com/Chocapikk/CVE-2024-25600](https://github.com/Chocapikk/CVE-2024-25600) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-25600.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-25600.svg)

- [https://github.com/K3ysTr0K3R/CVE-2024-25600-EXPLOIT](https://github.com/K3ysTr0K3R/CVE-2024-25600-EXPLOIT) :  ![starts](https://img.shields.io/github/stars/K3ysTr0K3R/CVE-2024-25600-EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/K3ysTr0K3R/CVE-2024-25600-EXPLOIT.svg)

- [https://github.com/Christbowel/CVE-2024-25600_Nuclei-Template](https://github.com/Christbowel/CVE-2024-25600_Nuclei-Template) :  ![starts](https://img.shields.io/github/stars/Christbowel/CVE-2024-25600_Nuclei-Template.svg) ![forks](https://img.shields.io/github/forks/Christbowel/CVE-2024-25600_Nuclei-Template.svg)

- [https://github.com/Tornad0007/CVE-2024-25600-Bricks-Builder-plugin-for-WordPress](https://github.com/Tornad0007/CVE-2024-25600-Bricks-Builder-plugin-for-WordPress) :  ![starts](https://img.shields.io/github/stars/Tornad0007/CVE-2024-25600-Bricks-Builder-plugin-for-WordPress.svg) ![forks](https://img.shields.io/github/forks/Tornad0007/CVE-2024-25600-Bricks-Builder-plugin-for-WordPress.svg)

- [https://github.com/hy011121/CVE-2024-25600-wordpress-Exploit-RCE](https://github.com/hy011121/CVE-2024-25600-wordpress-Exploit-RCE) :  ![starts](https://img.shields.io/github/stars/hy011121/CVE-2024-25600-wordpress-Exploit-RCE.svg) ![forks](https://img.shields.io/github/forks/hy011121/CVE-2024-25600-wordpress-Exploit-RCE.svg)

- [https://github.com/X-Projetion/WORDPRESS-CVE-2024-25600-EXPLOIT-RCE](https://github.com/X-Projetion/WORDPRESS-CVE-2024-25600-EXPLOIT-RCE) :  ![starts](https://img.shields.io/github/stars/X-Projetion/WORDPRESS-CVE-2024-25600-EXPLOIT-RCE.svg) ![forks](https://img.shields.io/github/forks/X-Projetion/WORDPRESS-CVE-2024-25600-EXPLOIT-RCE.svg)

- [https://github.com/frankfm-labs/bricks-rce-writeup](https://github.com/frankfm-labs/bricks-rce-writeup) :  ![starts](https://img.shields.io/github/stars/frankfm-labs/bricks-rce-writeup.svg) ![forks](https://img.shields.io/github/forks/frankfm-labs/bricks-rce-writeup.svg)

- [https://github.com/meli0dasH4ck3r/cve-2024-25600](https://github.com/meli0dasH4ck3r/cve-2024-25600) :  ![starts](https://img.shields.io/github/stars/meli0dasH4ck3r/cve-2024-25600.svg) ![forks](https://img.shields.io/github/forks/meli0dasH4ck3r/cve-2024-25600.svg)

- [https://github.com/WanLiChangChengWanLiChang/CVE-2024-25600](https://github.com/WanLiChangChengWanLiChang/CVE-2024-25600) :  ![starts](https://img.shields.io/github/stars/WanLiChangChengWanLiChang/CVE-2024-25600.svg) ![forks](https://img.shields.io/github/forks/WanLiChangChengWanLiChang/CVE-2024-25600.svg)

- [https://github.com/r0otk3r/CVE-2024-25600](https://github.com/r0otk3r/CVE-2024-25600) :  ![starts](https://img.shields.io/github/stars/r0otk3r/CVE-2024-25600.svg) ![forks](https://img.shields.io/github/forks/r0otk3r/CVE-2024-25600.svg)

- [https://github.com/NanoWraith/CVE-2024-25600](https://github.com/NanoWraith/CVE-2024-25600) :  ![starts](https://img.shields.io/github/stars/NanoWraith/CVE-2024-25600.svg) ![forks](https://img.shields.io/github/forks/NanoWraith/CVE-2024-25600.svg)

- [https://github.com/svchostmm/CVE-2024-25600-mass](https://github.com/svchostmm/CVE-2024-25600-mass) :  ![starts](https://img.shields.io/github/stars/svchostmm/CVE-2024-25600-mass.svg) ![forks](https://img.shields.io/github/forks/svchostmm/CVE-2024-25600-mass.svg)

- [https://github.com/KaSooMi0228/CVE-2024-25600-Bricks-Builder-WordPress](https://github.com/KaSooMi0228/CVE-2024-25600-Bricks-Builder-WordPress) :  ![starts](https://img.shields.io/github/stars/KaSooMi0228/CVE-2024-25600-Bricks-Builder-WordPress.svg) ![forks](https://img.shields.io/github/forks/KaSooMi0228/CVE-2024-25600-Bricks-Builder-WordPress.svg)

- [https://github.com/ivanbg2004/ODH-BricksBuilder-CVE-2024-25600-THM](https://github.com/ivanbg2004/ODH-BricksBuilder-CVE-2024-25600-THM) :  ![starts](https://img.shields.io/github/stars/ivanbg2004/ODH-BricksBuilder-CVE-2024-25600-THM.svg) ![forks](https://img.shields.io/github/forks/ivanbg2004/ODH-BricksBuilder-CVE-2024-25600-THM.svg)

- [https://github.com/DedsecTeam-BlackHat/Poleposph](https://github.com/DedsecTeam-BlackHat/Poleposph) :  ![starts](https://img.shields.io/github/stars/DedsecTeam-BlackHat/Poleposph.svg) ![forks](https://img.shields.io/github/forks/DedsecTeam-BlackHat/Poleposph.svg)

## CVE-2024-25466
 Directory Traversal vulnerability in React Native Document Picker before v.9.1.1 and fixed in v.9.1.1 allows a local attacker to execute arbitrary code via a crafted script to the Android library component.



- [https://github.com/FixedOctocat/CVE-2024-25466](https://github.com/FixedOctocat/CVE-2024-25466) :  ![starts](https://img.shields.io/github/stars/FixedOctocat/CVE-2024-25466.svg) ![forks](https://img.shields.io/github/forks/FixedOctocat/CVE-2024-25466.svg)

## CVE-2024-25423
 An issue in MAXON CINEMA 4D R2024.2.0 allows a local attacker to execute arbitrary code via a crafted c4d_base.xdl64 file.



- [https://github.com/DriverUnload/cve-2024-25423](https://github.com/DriverUnload/cve-2024-25423) :  ![starts](https://img.shields.io/github/stars/DriverUnload/cve-2024-25423.svg) ![forks](https://img.shields.io/github/forks/DriverUnload/cve-2024-25423.svg)

## CVE-2024-25422
 SQL Injection vulnerability in SEMCMS v.4.8 allows a remote attacker to execute arbitrary code and obtain sensitive information via the SEMCMS_Menu.php component.



- [https://github.com/tzyyyyyyy/semcms](https://github.com/tzyyyyyyy/semcms) :  ![starts](https://img.shields.io/github/stars/tzyyyyyyy/semcms.svg) ![forks](https://img.shields.io/github/forks/tzyyyyyyy/semcms.svg)

## CVE-2024-25381
 There is a Stored XSS Vulnerability in Emlog Pro 2.2.8 Article Publishing, due to non-filtering of quoted content.



- [https://github.com/OoO7ce/CVE-2024-25381](https://github.com/OoO7ce/CVE-2024-25381) :  ![starts](https://img.shields.io/github/stars/OoO7ce/CVE-2024-25381.svg) ![forks](https://img.shields.io/github/forks/OoO7ce/CVE-2024-25381.svg)

## CVE-2024-25376
 An issue discovered in Thesycon Software Solutions Gmbh & Co. KG TUSBAudio MSI-based installers before 5.68.0 allows a local attacker to execute arbitrary code via the msiexec.exe repair mode.



- [https://github.com/ewilded/CVE-2024-25376-POC](https://github.com/ewilded/CVE-2024-25376-POC) :  ![starts](https://img.shields.io/github/stars/ewilded/CVE-2024-25376-POC.svg) ![forks](https://img.shields.io/github/forks/ewilded/CVE-2024-25376-POC.svg)

## CVE-2024-25281
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/sajaljat/CVE-2024-25281](https://github.com/sajaljat/CVE-2024-25281) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-25281.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-25281.svg)

## CVE-2024-25280
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/sajaljat/CVE-2024-25280](https://github.com/sajaljat/CVE-2024-25280) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-25280.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-25280.svg)

## CVE-2024-25279
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/sajaljat/CVE-2024-25279](https://github.com/sajaljat/CVE-2024-25279) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-25279.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-25279.svg)

## CVE-2024-25278
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/sajaljat/CVE-2024-25278](https://github.com/sajaljat/CVE-2024-25278) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-25278.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-25278.svg)

## CVE-2024-25277
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/maen08/CVE-2024-25277](https://github.com/maen08/CVE-2024-25277) :  ![starts](https://img.shields.io/github/stars/maen08/CVE-2024-25277.svg) ![forks](https://img.shields.io/github/forks/maen08/CVE-2024-25277.svg)

## CVE-2024-25251
 code-projects Agro-School Management System 1.0 is suffers from Incorrect Access Control.



- [https://github.com/ASR511-OO7/CVE-2024-25251](https://github.com/ASR511-OO7/CVE-2024-25251) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-25251.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-25251.svg)

## CVE-2024-25250
 SQL Injection vulnerability in code-projects Agro-School Management System 1.0 allows attackers to run arbitrary code via the Login page.



- [https://github.com/ASR511-OO7/CVE-2024-25250.](https://github.com/ASR511-OO7/CVE-2024-25250.) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-25250..svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-25250..svg)

## CVE-2024-25227
 SQL Injection vulnerability in ABO.CMS version 5.8, allows remote attackers to execute arbitrary code, cause a denial of service (DoS), escalate privileges, and obtain sensitive information via the tb_login parameter in admin login page.



- [https://github.com/thetrueartist/ABO.CMS-Login-SQLi-CVE-2024-25227](https://github.com/thetrueartist/ABO.CMS-Login-SQLi-CVE-2024-25227) :  ![starts](https://img.shields.io/github/stars/thetrueartist/ABO.CMS-Login-SQLi-CVE-2024-25227.svg) ![forks](https://img.shields.io/github/forks/thetrueartist/ABO.CMS-Login-SQLi-CVE-2024-25227.svg)

- [https://github.com/thetrueartist/ABO.CMS-EXPLOIT-Unauthenticated-Login-Bypass-CVE-2024-25227](https://github.com/thetrueartist/ABO.CMS-EXPLOIT-Unauthenticated-Login-Bypass-CVE-2024-25227) :  ![starts](https://img.shields.io/github/stars/thetrueartist/ABO.CMS-EXPLOIT-Unauthenticated-Login-Bypass-CVE-2024-25227.svg) ![forks](https://img.shields.io/github/forks/thetrueartist/ABO.CMS-EXPLOIT-Unauthenticated-Login-Bypass-CVE-2024-25227.svg)

## CVE-2024-25202
 Cross Site Scripting vulnerability in Phpgurukul User Registration & Login and User Management System 1.0 allows attackers to run arbitrary code via the search bar.



- [https://github.com/Agampreet-Singh/CVE-2024-25202](https://github.com/Agampreet-Singh/CVE-2024-25202) :  ![starts](https://img.shields.io/github/stars/Agampreet-Singh/CVE-2024-25202.svg) ![forks](https://img.shields.io/github/forks/Agampreet-Singh/CVE-2024-25202.svg)

## CVE-2024-25175
 An issue in Kickdler before v1.107.0 allows attackers to provide an XSS payload via a HTTP response splitting attack.



- [https://github.com/jet-pentest/CVE-2024-25175](https://github.com/jet-pentest/CVE-2024-25175) :  ![starts](https://img.shields.io/github/stars/jet-pentest/CVE-2024-25175.svg) ![forks](https://img.shields.io/github/forks/jet-pentest/CVE-2024-25175.svg)

## CVE-2024-25170
 An issue in Mezzanine v6.0.0 allows attackers to bypass access controls via manipulating the Host header.



- [https://github.com/shenhav12/CVE-2024-25170-Mezzanine-v6.0.0](https://github.com/shenhav12/CVE-2024-25170-Mezzanine-v6.0.0) :  ![starts](https://img.shields.io/github/stars/shenhav12/CVE-2024-25170-Mezzanine-v6.0.0.svg) ![forks](https://img.shields.io/github/forks/shenhav12/CVE-2024-25170-Mezzanine-v6.0.0.svg)

## CVE-2024-25169
 An issue in Mezzanine v6.0.0 allows attackers to bypass access control mechanisms in the admin panel via a crafted request.



- [https://github.com/shenhav12/CVE-2024-25169-Mezzanine-v6.0.0](https://github.com/shenhav12/CVE-2024-25169-Mezzanine-v6.0.0) :  ![starts](https://img.shields.io/github/stars/shenhav12/CVE-2024-25169-Mezzanine-v6.0.0.svg) ![forks](https://img.shields.io/github/forks/shenhav12/CVE-2024-25169-Mezzanine-v6.0.0.svg)

## CVE-2024-25153
 A directory traversal within the ‘ftpservlet’ of the FileCatalyst Workflow Web Portal allows files to be uploaded outside of the intended ‘uploadtemp’ directory with a specially crafted POST request. In situations where a file is successfully uploaded to web portal’s DocumentRoot, specially crafted JSP files could be used to execute code, including web shells.



- [https://github.com/nettitude/CVE-2024-25153](https://github.com/nettitude/CVE-2024-25153) :  ![starts](https://img.shields.io/github/stars/nettitude/CVE-2024-25153.svg) ![forks](https://img.shields.io/github/forks/nettitude/CVE-2024-25153.svg)

- [https://github.com/rainbowhatrkn/CVE-2024-25153](https://github.com/rainbowhatrkn/CVE-2024-25153) :  ![starts](https://img.shields.io/github/stars/rainbowhatrkn/CVE-2024-25153.svg) ![forks](https://img.shields.io/github/forks/rainbowhatrkn/CVE-2024-25153.svg)

## CVE-2024-25092
 Missing Authorization vulnerability in XLPlugins NextMove Lite.This issue affects NextMove Lite: from n/a through 2.17.0.



- [https://github.com/RandomRobbieBF/CVE-2024-25092](https://github.com/RandomRobbieBF/CVE-2024-25092) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-25092.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-25092.svg)

## CVE-2024-24926
 Deserialization of Untrusted Data vulnerability in UnitedThemes Brooklyn | Creative Multi-Purpose Responsive WordPress Theme.This issue affects Brooklyn | Creative Multi-Purpose Responsive WordPress Theme: from n/a through 4.9.7.6.





- [https://github.com/moften/CVE-2024-24926](https://github.com/moften/CVE-2024-24926) :  ![starts](https://img.shields.io/github/stars/moften/CVE-2024-24926.svg) ![forks](https://img.shields.io/github/forks/moften/CVE-2024-24926.svg)

## CVE-2024-24919
 Potentially allowing an attacker to read certain information on Check Point Security Gateways once connected to the internet and enabled with remote Access VPN or Mobile Access Software Blades. A Security fix that mitigates this vulnerability is available.



- [https://github.com/seed1337/CVE-2024-24919-POC](https://github.com/seed1337/CVE-2024-24919-POC) :  ![starts](https://img.shields.io/github/stars/seed1337/CVE-2024-24919-POC.svg) ![forks](https://img.shields.io/github/forks/seed1337/CVE-2024-24919-POC.svg)

- [https://github.com/ifconfig-me/CVE-2024-24919-Bulk-Scanner](https://github.com/ifconfig-me/CVE-2024-24919-Bulk-Scanner) :  ![starts](https://img.shields.io/github/stars/ifconfig-me/CVE-2024-24919-Bulk-Scanner.svg) ![forks](https://img.shields.io/github/forks/ifconfig-me/CVE-2024-24919-Bulk-Scanner.svg)

- [https://github.com/RevoltSecurities/CVE-2024-24919](https://github.com/RevoltSecurities/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/RevoltSecurities/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/RevoltSecurities/CVE-2024-24919.svg)

- [https://github.com/GoatSecurity/CVE-2024-24919](https://github.com/GoatSecurity/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/GoatSecurity/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/GoatSecurity/CVE-2024-24919.svg)

- [https://github.com/un9nplayer/CVE-2024-24919](https://github.com/un9nplayer/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/un9nplayer/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/un9nplayer/CVE-2024-24919.svg)

- [https://github.com/LucasKatashi/CVE-2024-24919](https://github.com/LucasKatashi/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/LucasKatashi/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/LucasKatashi/CVE-2024-24919.svg)

- [https://github.com/0nin0hanz0/CVE-2024-24919-PoC](https://github.com/0nin0hanz0/CVE-2024-24919-PoC) :  ![starts](https://img.shields.io/github/stars/0nin0hanz0/CVE-2024-24919-PoC.svg) ![forks](https://img.shields.io/github/forks/0nin0hanz0/CVE-2024-24919-PoC.svg)

- [https://github.com/verylazytech/CVE-2024-24919](https://github.com/verylazytech/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/verylazytech/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/verylazytech/CVE-2024-24919.svg)

- [https://github.com/c3rrberu5/CVE-2024-24919](https://github.com/c3rrberu5/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/c3rrberu5/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/c3rrberu5/CVE-2024-24919.svg)

- [https://github.com/GuayoyoCyber/CVE-2024-24919](https://github.com/GuayoyoCyber/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/GuayoyoCyber/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/GuayoyoCyber/CVE-2024-24919.svg)

- [https://github.com/emanueldosreis/CVE-2024-24919](https://github.com/emanueldosreis/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/emanueldosreis/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/emanueldosreis/CVE-2024-24919.svg)

- [https://github.com/zam89/CVE-2024-24919](https://github.com/zam89/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/zam89/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/zam89/CVE-2024-24919.svg)

- [https://github.com/smackerdodi/CVE-2024-24919-nuclei-templater](https://github.com/smackerdodi/CVE-2024-24919-nuclei-templater) :  ![starts](https://img.shields.io/github/stars/smackerdodi/CVE-2024-24919-nuclei-templater.svg) ![forks](https://img.shields.io/github/forks/smackerdodi/CVE-2024-24919-nuclei-templater.svg)

- [https://github.com/GlobalsecureAcademy/CVE-2024-24919](https://github.com/GlobalsecureAcademy/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/GlobalsecureAcademy/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/GlobalsecureAcademy/CVE-2024-24919.svg)

- [https://github.com/Bytenull00/CVE-2024-24919](https://github.com/Bytenull00/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/Bytenull00/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/Bytenull00/CVE-2024-24919.svg)

- [https://github.com/Rug4lo/CVE-2024-24919-Exploit](https://github.com/Rug4lo/CVE-2024-24919-Exploit) :  ![starts](https://img.shields.io/github/stars/Rug4lo/CVE-2024-24919-Exploit.svg) ![forks](https://img.shields.io/github/forks/Rug4lo/CVE-2024-24919-Exploit.svg)

- [https://github.com/protonnegativo/CVE-2024-24919](https://github.com/protonnegativo/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/protonnegativo/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/protonnegativo/CVE-2024-24919.svg)

- [https://github.com/bigb0x/CVE-2024-24919-Sniper](https://github.com/bigb0x/CVE-2024-24919-Sniper) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-24919-Sniper.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-24919-Sniper.svg)

- [https://github.com/r4p3c4/CVE-2024-24919-Exploit-PoC-Checkpoint-Firewall-VPN](https://github.com/r4p3c4/CVE-2024-24919-Exploit-PoC-Checkpoint-Firewall-VPN) :  ![starts](https://img.shields.io/github/stars/r4p3c4/CVE-2024-24919-Exploit-PoC-Checkpoint-Firewall-VPN.svg) ![forks](https://img.shields.io/github/forks/r4p3c4/CVE-2024-24919-Exploit-PoC-Checkpoint-Firewall-VPN.svg)

- [https://github.com/NingXin2002/Check-Point_poc](https://github.com/NingXin2002/Check-Point_poc) :  ![starts](https://img.shields.io/github/stars/NingXin2002/Check-Point_poc.svg) ![forks](https://img.shields.io/github/forks/NingXin2002/Check-Point_poc.svg)

- [https://github.com/ShadowByte1/CVE-2024-24919](https://github.com/ShadowByte1/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/ShadowByte1/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/ShadowByte1/CVE-2024-24919.svg)

- [https://github.com/nexblade12/CVE-2024-24919](https://github.com/nexblade12/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/nexblade12/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/nexblade12/CVE-2024-24919.svg)

- [https://github.com/fernandobortotti/CVE-2024-24919](https://github.com/fernandobortotti/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/fernandobortotti/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/fernandobortotti/CVE-2024-24919.svg)

- [https://github.com/SalehLardhi/CVE-2024-24919](https://github.com/SalehLardhi/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/SalehLardhi/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/SalehLardhi/CVE-2024-24919.svg)

- [https://github.com/satriarizka/CVE-2024-24919](https://github.com/satriarizka/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/satriarizka/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/satriarizka/CVE-2024-24919.svg)

- [https://github.com/0xYumeko/CVE-2024-24919](https://github.com/0xYumeko/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/0xYumeko/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/0xYumeko/CVE-2024-24919.svg)

- [https://github.com/Cappricio-Securities/CVE-2024-24919](https://github.com/Cappricio-Securities/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2024-24919.svg)

- [https://github.com/0xans/CVE-2024-24919](https://github.com/0xans/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/0xans/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/0xans/CVE-2024-24919.svg)

- [https://github.com/mr-kasim-mehar/CVE-2024-24919-Exploit](https://github.com/mr-kasim-mehar/CVE-2024-24919-Exploit) :  ![starts](https://img.shields.io/github/stars/mr-kasim-mehar/CVE-2024-24919-Exploit.svg) ![forks](https://img.shields.io/github/forks/mr-kasim-mehar/CVE-2024-24919-Exploit.svg)

- [https://github.com/birdlex/cve-2024-24919-checker](https://github.com/birdlex/cve-2024-24919-checker) :  ![starts](https://img.shields.io/github/stars/birdlex/cve-2024-24919-checker.svg) ![forks](https://img.shields.io/github/forks/birdlex/cve-2024-24919-checker.svg)

- [https://github.com/starlox0/CVE-2024-24919-POC](https://github.com/starlox0/CVE-2024-24919-POC) :  ![starts](https://img.shields.io/github/stars/starlox0/CVE-2024-24919-POC.svg) ![forks](https://img.shields.io/github/forks/starlox0/CVE-2024-24919-POC.svg)

- [https://github.com/r4p3c4/CVE-2024-24919-Checkpoint-Firewall-VPN-Check](https://github.com/r4p3c4/CVE-2024-24919-Checkpoint-Firewall-VPN-Check) :  ![starts](https://img.shields.io/github/stars/r4p3c4/CVE-2024-24919-Checkpoint-Firewall-VPN-Check.svg) ![forks](https://img.shields.io/github/forks/r4p3c4/CVE-2024-24919-Checkpoint-Firewall-VPN-Check.svg)

- [https://github.com/hendprw/CVE-2024-24919](https://github.com/hendprw/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/hendprw/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/hendprw/CVE-2024-24919.svg)

- [https://github.com/Vulnpire/CVE-2024-24919](https://github.com/Vulnpire/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/Vulnpire/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/Vulnpire/CVE-2024-24919.svg)

- [https://github.com/satchhacker/cve-2024-24919](https://github.com/satchhacker/cve-2024-24919) :  ![starts](https://img.shields.io/github/stars/satchhacker/cve-2024-24919.svg) ![forks](https://img.shields.io/github/forks/satchhacker/cve-2024-24919.svg)

- [https://github.com/am-eid/CVE-2024-24919](https://github.com/am-eid/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/am-eid/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/am-eid/CVE-2024-24919.svg)

- [https://github.com/P3wc0/CVE-2024-24919](https://github.com/P3wc0/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/P3wc0/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/P3wc0/CVE-2024-24919.svg)

- [https://github.com/Jutrm/cve-2024-24919](https://github.com/Jutrm/cve-2024-24919) :  ![starts](https://img.shields.io/github/stars/Jutrm/cve-2024-24919.svg) ![forks](https://img.shields.io/github/forks/Jutrm/cve-2024-24919.svg)

- [https://github.com/nicolvsrlr27/CVE-2024-24919](https://github.com/nicolvsrlr27/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/nicolvsrlr27/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/nicolvsrlr27/CVE-2024-24919.svg)

- [https://github.com/YN1337/CVE-2024-24919](https://github.com/YN1337/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/YN1337/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/YN1337/CVE-2024-24919.svg)

- [https://github.com/Tim-Hoekstra/CVE-2024-24919](https://github.com/Tim-Hoekstra/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/Tim-Hoekstra/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/Tim-Hoekstra/CVE-2024-24919.svg)

- [https://github.com/H3KEY/CVE-2024-24919](https://github.com/H3KEY/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/H3KEY/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/H3KEY/CVE-2024-24919.svg)

- [https://github.com/0xkalawy/CVE-2024-24919](https://github.com/0xkalawy/CVE-2024-24919) :  ![starts](https://img.shields.io/github/stars/0xkalawy/CVE-2024-24919.svg) ![forks](https://img.shields.io/github/forks/0xkalawy/CVE-2024-24919.svg)

- [https://github.com/nullcult/CVE-2024-24919-Exploit](https://github.com/nullcult/CVE-2024-24919-Exploit) :  ![starts](https://img.shields.io/github/stars/nullcult/CVE-2024-24919-Exploit.svg) ![forks](https://img.shields.io/github/forks/nullcult/CVE-2024-24919-Exploit.svg)

- [https://github.com/Expl0itD0g/CVE-2024-24919---Poc](https://github.com/Expl0itD0g/CVE-2024-24919---Poc) :  ![starts](https://img.shields.io/github/stars/Expl0itD0g/CVE-2024-24919---Poc.svg) ![forks](https://img.shields.io/github/forks/Expl0itD0g/CVE-2024-24919---Poc.svg)

- [https://github.com/B1naryo/CVE-2024-24919-POC](https://github.com/B1naryo/CVE-2024-24919-POC) :  ![starts](https://img.shields.io/github/stars/B1naryo/CVE-2024-24919-POC.svg) ![forks](https://img.shields.io/github/forks/B1naryo/CVE-2024-24919-POC.svg)

- [https://github.com/J4F9S5D2Q7/CVE-2024-24919-CHECKPOINT](https://github.com/J4F9S5D2Q7/CVE-2024-24919-CHECKPOINT) :  ![starts](https://img.shields.io/github/stars/J4F9S5D2Q7/CVE-2024-24919-CHECKPOINT.svg) ![forks](https://img.shields.io/github/forks/J4F9S5D2Q7/CVE-2024-24919-CHECKPOINT.svg)

- [https://github.com/CyprianAtsyor/CVE-2024-24919-Incident-Report.md](https://github.com/CyprianAtsyor/CVE-2024-24919-Incident-Report.md) :  ![starts](https://img.shields.io/github/stars/CyprianAtsyor/CVE-2024-24919-Incident-Report.md.svg) ![forks](https://img.shields.io/github/forks/CyprianAtsyor/CVE-2024-24919-Incident-Report.md.svg)

- [https://github.com/MacUchegit/Detecting-and-Analyzing-CVE-2024-24919-Exploitation](https://github.com/MacUchegit/Detecting-and-Analyzing-CVE-2024-24919-Exploitation) :  ![starts](https://img.shields.io/github/stars/MacUchegit/Detecting-and-Analyzing-CVE-2024-24919-Exploitation.svg) ![forks](https://img.shields.io/github/forks/MacUchegit/Detecting-and-Analyzing-CVE-2024-24919-Exploitation.svg)

- [https://github.com/Praison001/CVE-2024-24919-Check-Point-Remote-Access-VPN](https://github.com/Praison001/CVE-2024-24919-Check-Point-Remote-Access-VPN) :  ![starts](https://img.shields.io/github/stars/Praison001/CVE-2024-24919-Check-Point-Remote-Access-VPN.svg) ![forks](https://img.shields.io/github/forks/Praison001/CVE-2024-24919-Check-Point-Remote-Access-VPN.svg)

## CVE-2024-24816
 CKEditor4 is an open source what-you-see-is-what-you-get HTML editor. A cross-site scripting vulnerability vulnerability has been discovered in versions prior to 4.24.0-lts in samples that use the `preview` feature. All integrators that use these samples in the production code can be affected. The vulnerability allows an attacker to execute JavaScript code by abusing the misconfigured preview feature. It affects all users using the CKEditor 4 at version  4.24.0-lts with affected samples used in a production environment. A fix is available in version 4.24.0-lts.



- [https://github.com/afine-com/CVE-2024-24816](https://github.com/afine-com/CVE-2024-24816) :  ![starts](https://img.shields.io/github/stars/afine-com/CVE-2024-24816.svg) ![forks](https://img.shields.io/github/forks/afine-com/CVE-2024-24816.svg)

## CVE-2024-24787
 On Darwin, building a Go module which contains CGO can trigger arbitrary code execution when using the Apple version of ld, due to usage of the -lto_library flag in a "#cgo LDFLAGS" directive.



- [https://github.com/LOURC0D3/CVE-2024-24787-PoC](https://github.com/LOURC0D3/CVE-2024-24787-PoC) :  ![starts](https://img.shields.io/github/stars/LOURC0D3/CVE-2024-24787-PoC.svg) ![forks](https://img.shields.io/github/forks/LOURC0D3/CVE-2024-24787-PoC.svg)

## CVE-2024-24760
 mailcow is a dockerized email package, with multiple containers linked in one bridged network. A security vulnerability has been identified in mailcow affecting versions  2024-01c. This vulnerability potentially allows attackers on the same subnet to connect to exposed ports of a Docker container, even when the port is bound to 127.0.0.1. The vulnerability has been addressed by implementing additional iptables/nftables rules. These rules drop packets for Docker containers on ports 3306, 6379, 8983, and 12345, where the input interface is not `br-mailcow` and the output interface is `br-mailcow`.



- [https://github.com/killerbees19/CVE-2024-24760](https://github.com/killerbees19/CVE-2024-24760) :  ![starts](https://img.shields.io/github/stars/killerbees19/CVE-2024-24760.svg) ![forks](https://img.shields.io/github/forks/killerbees19/CVE-2024-24760.svg)

## CVE-2024-24590
 Deserialization of untrusted data can occur in versions 0.17.0 to 1.14.2 of the client SDK of Allegro AI’s ClearML platform, enabling a maliciously uploaded artifact to run arbitrary code on an end user’s system when interacted with.




- [https://github.com/diegogarciayala/CVE-2024-24590-ClearML-RCE-CMD-POC](https://github.com/diegogarciayala/CVE-2024-24590-ClearML-RCE-CMD-POC) :  ![starts](https://img.shields.io/github/stars/diegogarciayala/CVE-2024-24590-ClearML-RCE-CMD-POC.svg) ![forks](https://img.shields.io/github/forks/diegogarciayala/CVE-2024-24590-ClearML-RCE-CMD-POC.svg)

- [https://github.com/OxyDeV2/ClearML-CVE-2024-24590](https://github.com/OxyDeV2/ClearML-CVE-2024-24590) :  ![starts](https://img.shields.io/github/stars/OxyDeV2/ClearML-CVE-2024-24590.svg) ![forks](https://img.shields.io/github/forks/OxyDeV2/ClearML-CVE-2024-24590.svg)

- [https://github.com/xffsec/CVE-2024-24590-ClearML-RCE-Exploit](https://github.com/xffsec/CVE-2024-24590-ClearML-RCE-Exploit) :  ![starts](https://img.shields.io/github/stars/xffsec/CVE-2024-24590-ClearML-RCE-Exploit.svg) ![forks](https://img.shields.io/github/forks/xffsec/CVE-2024-24590-ClearML-RCE-Exploit.svg)

- [https://github.com/sviim/ClearML-CVE-2024-24590-RCE](https://github.com/sviim/ClearML-CVE-2024-24590-RCE) :  ![starts](https://img.shields.io/github/stars/sviim/ClearML-CVE-2024-24590-RCE.svg) ![forks](https://img.shields.io/github/forks/sviim/ClearML-CVE-2024-24590-RCE.svg)

- [https://github.com/junnythemarksman/CVE-2024-24590](https://github.com/junnythemarksman/CVE-2024-24590) :  ![starts](https://img.shields.io/github/stars/junnythemarksman/CVE-2024-24590.svg) ![forks](https://img.shields.io/github/forks/junnythemarksman/CVE-2024-24590.svg)

- [https://github.com/Bigb972003/cve-2024-24590](https://github.com/Bigb972003/cve-2024-24590) :  ![starts](https://img.shields.io/github/stars/Bigb972003/cve-2024-24590.svg) ![forks](https://img.shields.io/github/forks/Bigb972003/cve-2024-24590.svg)

## CVE-2024-24576
 Rust is a programming language. The Rust Security Response WG was notified that the Rust standard library prior to version 1.77.2 did not properly escape arguments when invoking batch files (with the `bat` and `cmd` extensions) on Windows using the `Command`. An attacker able to control the arguments passed to the spawned process could execute arbitrary shell commands by bypassing the escaping. The severity of this vulnerability is critical for those who invoke batch files on Windows with untrusted arguments. No other platform or use is affected.

The `Command::arg` and `Command::args` APIs state in their documentation that the arguments will be passed to the spawned process as-is, regardless of the content of the arguments, and will not be evaluated by a shell. This means it should be safe to pass untrusted input as an argument.

On Windows, the implementation of this is more complex than other platforms, because the Windows API only provides a single string containing all the arguments to the spawned process, and it's up to the spawned process to split them. Most programs use the standard C run-time argv, which in practice results in a mostly consistent way arguments are splitted.

One exception though is `cmd.exe` (used among other things to execute batch files), which has its own argument splitting logic. That forces the standard library to implement custom escaping for arguments passed to batch files. Unfortunately it was reported that our escaping logic was not thorough enough, and it was possible to pass malicious arguments that would result in arbitrary shell execution.

Due to the complexity of `cmd.exe`, we didn't identify a solution that would correctly escape arguments in all cases. To maintain our API guarantees, we improved the robustness of the escaping code, and changed the `Command` API to return an `InvalidInput` error when it cannot safely escape an argument. This error will be emitted when spawning the process.

The fix is included in Rust 1.77.2. Note that the new escaping logic for batch files errs on the conservative side, and could reject valid arguments. Those who implement the escaping themselves or only handle trusted inputs on Windows can also use the `CommandExt::raw_arg` method to bypass the standard library's escaping logic.



- [https://github.com/frostb1ten/CVE-2024-24576-PoC](https://github.com/frostb1ten/CVE-2024-24576-PoC) :  ![starts](https://img.shields.io/github/stars/frostb1ten/CVE-2024-24576-PoC.svg) ![forks](https://img.shields.io/github/forks/frostb1ten/CVE-2024-24576-PoC.svg)

- [https://github.com/aydinnyunus/CVE-2024-24576-Exploit](https://github.com/aydinnyunus/CVE-2024-24576-Exploit) :  ![starts](https://img.shields.io/github/stars/aydinnyunus/CVE-2024-24576-Exploit.svg) ![forks](https://img.shields.io/github/forks/aydinnyunus/CVE-2024-24576-Exploit.svg)

- [https://github.com/brains93/CVE-2024-24576-PoC-Python](https://github.com/brains93/CVE-2024-24576-PoC-Python) :  ![starts](https://img.shields.io/github/stars/brains93/CVE-2024-24576-PoC-Python.svg) ![forks](https://img.shields.io/github/forks/brains93/CVE-2024-24576-PoC-Python.svg)

- [https://github.com/corysabol/batbadbut-demo](https://github.com/corysabol/batbadbut-demo) :  ![starts](https://img.shields.io/github/stars/corysabol/batbadbut-demo.svg) ![forks](https://img.shields.io/github/forks/corysabol/batbadbut-demo.svg)

- [https://github.com/lpn/CVE-2024-24576.jl](https://github.com/lpn/CVE-2024-24576.jl) :  ![starts](https://img.shields.io/github/stars/lpn/CVE-2024-24576.jl.svg) ![forks](https://img.shields.io/github/forks/lpn/CVE-2024-24576.jl.svg)

- [https://github.com/mishl-dev/CVE-2024-24576-PoC-Python](https://github.com/mishl-dev/CVE-2024-24576-PoC-Python) :  ![starts](https://img.shields.io/github/stars/mishl-dev/CVE-2024-24576-PoC-Python.svg) ![forks](https://img.shields.io/github/forks/mishl-dev/CVE-2024-24576-PoC-Python.svg)

- [https://github.com/foxoman/CVE-2024-24576-PoC---Nim](https://github.com/foxoman/CVE-2024-24576-PoC---Nim) :  ![starts](https://img.shields.io/github/stars/foxoman/CVE-2024-24576-PoC---Nim.svg) ![forks](https://img.shields.io/github/forks/foxoman/CVE-2024-24576-PoC---Nim.svg)

- [https://github.com/SheL3G/CVE-2024-24576-PoC-BatBadBut](https://github.com/SheL3G/CVE-2024-24576-PoC-BatBadBut) :  ![starts](https://img.shields.io/github/stars/SheL3G/CVE-2024-24576-PoC-BatBadBut.svg) ![forks](https://img.shields.io/github/forks/SheL3G/CVE-2024-24576-PoC-BatBadBut.svg)

- [https://github.com/Gaurav1020/CVE-2024-24576-PoC-Rust](https://github.com/Gaurav1020/CVE-2024-24576-PoC-Rust) :  ![starts](https://img.shields.io/github/stars/Gaurav1020/CVE-2024-24576-PoC-Rust.svg) ![forks](https://img.shields.io/github/forks/Gaurav1020/CVE-2024-24576-PoC-Rust.svg)

## CVE-2024-24549
 Denial of Service due to improper input validation vulnerability for HTTP/2 requests in Apache Tomcat. When processing an HTTP/2 request, if the request exceeded any of the configured limits for headers, the associated HTTP/2 stream was not reset until after all of the headers had been processed.This issue affects Apache Tomcat: from 11.0.0-M1 through 11.0.0-M16, from 10.1.0-M1 through 10.1.18, from 9.0.0-M1 through 9.0.85, from 8.5.0 through 8.5.98.

Users are recommended to upgrade to version 11.0.0-M17, 10.1.19, 9.0.86 or 8.5.99 which fix the issue.



- [https://github.com/Abdurahmon3236/CVE-2024-24549](https://github.com/Abdurahmon3236/CVE-2024-24549) :  ![starts](https://img.shields.io/github/stars/Abdurahmon3236/CVE-2024-24549.svg) ![forks](https://img.shields.io/github/forks/Abdurahmon3236/CVE-2024-24549.svg)

- [https://github.com/JFOZ1010/CVE-2024-24549](https://github.com/JFOZ1010/CVE-2024-24549) :  ![starts](https://img.shields.io/github/stars/JFOZ1010/CVE-2024-24549.svg) ![forks](https://img.shields.io/github/forks/JFOZ1010/CVE-2024-24549.svg)

## CVE-2024-24488
 An issue in Shenzen Tenda Technology CP3V2.0 V11.10.00.2311090948 allows a local attacker to obtain sensitive information via the password component.



- [https://github.com/minj-ae/CVE-2024-24488](https://github.com/minj-ae/CVE-2024-24488) :  ![starts](https://img.shields.io/github/stars/minj-ae/CVE-2024-24488.svg) ![forks](https://img.shields.io/github/forks/minj-ae/CVE-2024-24488.svg)

## CVE-2024-24402
 An issue in Nagios XI 2024R1.01 allows a remote attacker to escalate privileges via a crafted script to the /usr/local/nagios/bin/npcd component.



- [https://github.com/MAWK0235/CVE-2024-24402](https://github.com/MAWK0235/CVE-2024-24402) :  ![starts](https://img.shields.io/github/stars/MAWK0235/CVE-2024-24402.svg) ![forks](https://img.shields.io/github/forks/MAWK0235/CVE-2024-24402.svg)

## CVE-2024-24401
 SQL Injection vulnerability in Nagios XI 2024R1.01 allows a remote attacker to execute arbitrary code via a crafted payload to the monitoringwizard.php component.



- [https://github.com/MAWK0235/CVE-2024-24401](https://github.com/MAWK0235/CVE-2024-24401) :  ![starts](https://img.shields.io/github/stars/MAWK0235/CVE-2024-24401.svg) ![forks](https://img.shields.io/github/forks/MAWK0235/CVE-2024-24401.svg)

## CVE-2024-24398
 Directory Traversal vulnerability in Stimulsoft GmbH Stimulsoft Dashboard.JS before v.2024.1.2 allows a remote attacker to execute arbitrary code via a crafted payload to the fileName parameter of the Save function.



- [https://github.com/trustcves/CVE-2024-24398](https://github.com/trustcves/CVE-2024-24398) :  ![starts](https://img.shields.io/github/stars/trustcves/CVE-2024-24398.svg) ![forks](https://img.shields.io/github/forks/trustcves/CVE-2024-24398.svg)

## CVE-2024-24397
 Cross Site Scripting vulnerability in Stimulsoft GmbH Stimulsoft Dashboard.JS before v.2024.1.2 allows a remote attacker to execute arbitrary code via a crafted payload to the ReportName field.



- [https://github.com/trustcves/CVE-2024-24397](https://github.com/trustcves/CVE-2024-24397) :  ![starts](https://img.shields.io/github/stars/trustcves/CVE-2024-24397.svg) ![forks](https://img.shields.io/github/forks/trustcves/CVE-2024-24397.svg)

## CVE-2024-24396
 Cross Site Scripting vulnerability in Stimulsoft GmbH Stimulsoft Dashboard.JS before v.2024.1.2 allows a remote attacker to execute arbitrary code via a crafted payload to the search bar component.



- [https://github.com/trustcves/CVE-2024-24396](https://github.com/trustcves/CVE-2024-24396) :  ![starts](https://img.shields.io/github/stars/trustcves/CVE-2024-24396.svg) ![forks](https://img.shields.io/github/forks/trustcves/CVE-2024-24396.svg)

## CVE-2024-24386
 An issue in VitalPBX v.3.2.4-5 allows an attacker to execute arbitrary code via a crafted payload to the /var/lib/vitalpbx/scripts folder.



- [https://github.com/erick-duarte/CVE-2024-24386](https://github.com/erick-duarte/CVE-2024-24386) :  ![starts](https://img.shields.io/github/stars/erick-duarte/CVE-2024-24386.svg) ![forks](https://img.shields.io/github/forks/erick-duarte/CVE-2024-24386.svg)

## CVE-2024-24206
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/l00neyhacker/CVE-2024-24206](https://github.com/l00neyhacker/CVE-2024-24206) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-24206.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-24206.svg)

## CVE-2024-24204
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/l00neyhacker/CVE-2024-24204](https://github.com/l00neyhacker/CVE-2024-24204) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-24204.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-24204.svg)

## CVE-2024-24203
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/l00neyhacker/CVE-2024-24203](https://github.com/l00neyhacker/CVE-2024-24203) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-24203.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-24203.svg)

## CVE-2024-24142
 Sourcecodester School Task Manager 1.0 allows SQL Injection via the 'subject' parameter.



- [https://github.com/BurakSevben/CVE-2024-24142](https://github.com/BurakSevben/CVE-2024-24142) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-24142.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-24142.svg)

## CVE-2024-24141
 Sourcecodester School Task Manager App 1.0 allows SQL Injection via the 'task' parameter.



- [https://github.com/BurakSevben/CVE-2024-24141](https://github.com/BurakSevben/CVE-2024-24141) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-24141.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-24141.svg)

## CVE-2024-24140
 Sourcecodester Daily Habit Tracker App 1.0 allows SQL Injection via the parameter 'tracker.'



- [https://github.com/BurakSevben/CVE-2024-24140](https://github.com/BurakSevben/CVE-2024-24140) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-24140.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-24140.svg)

## CVE-2024-24139
 Sourcecodester Login System with Email Verification 1.0 allows SQL Injection via the 'user' parameter.



- [https://github.com/BurakSevben/CVE-2024-24139](https://github.com/BurakSevben/CVE-2024-24139) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-24139.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-24139.svg)

## CVE-2024-24138
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/BurakSevben/CVE-2024-24138](https://github.com/BurakSevben/CVE-2024-24138) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-24138.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-24138.svg)

## CVE-2024-24137
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/BurakSevben/CVE-2024-24137](https://github.com/BurakSevben/CVE-2024-24137) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-24137.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-24137.svg)

## CVE-2024-24136
 The 'Your Name' field in the Submit Score section of Sourcecodester Math Game with Leaderboard v1.0 is vulnerable to Cross-Site Scripting (XSS) attacks.



- [https://github.com/BurakSevben/CVE-2024-24136](https://github.com/BurakSevben/CVE-2024-24136) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-24136.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-24136.svg)

## CVE-2024-24135
 Product Name and Product Code in the 'Add Product' section of Sourcecodester Product Inventory with Export to Excel 1.0 are vulnerable to XSS attacks.



- [https://github.com/BurakSevben/CVE-2024-24135](https://github.com/BurakSevben/CVE-2024-24135) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-24135.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-24135.svg)

## CVE-2024-24134
 Sourcecodester Online Food Menu 1.0 is vulnerable to Cross Site Scripting (XSS) via the 'Menu Name' and 'Description' fields in the Update Menu section.



- [https://github.com/BurakSevben/CVE-2024-24134](https://github.com/BurakSevben/CVE-2024-24134) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-24134.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-24134.svg)

## CVE-2024-24108
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/ASR511-OO7/CVE-2024-24108](https://github.com/ASR511-OO7/CVE-2024-24108) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24108.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24108.svg)

## CVE-2024-24105
 SQL Injection vulnerability in Code-projects Computer Science Time Table System 1.0 allows attackers to run arbitrary code via adminFormvalidation.php.



- [https://github.com/ASR511-OO7/CVE-2024-24105](https://github.com/ASR511-OO7/CVE-2024-24105) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24105.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24105.svg)

## CVE-2024-24104
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/ASR511-OO7/CVE-2024-24104](https://github.com/ASR511-OO7/CVE-2024-24104) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24104.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24104.svg)

## CVE-2024-24103
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/ASR511-OO7/CVE-2024-24103](https://github.com/ASR511-OO7/CVE-2024-24103) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24103.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24103.svg)

## CVE-2024-24102
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/ASR511-OO7/CVE-2024-24102](https://github.com/ASR511-OO7/CVE-2024-24102) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24102.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24102.svg)

## CVE-2024-24101
 Code-projects Scholars Tracking System 1.0 is vulnerable to SQL Injection under Eligibility Information Update.



- [https://github.com/ASR511-OO7/CVE-2024-24101](https://github.com/ASR511-OO7/CVE-2024-24101) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24101.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24101.svg)

## CVE-2024-24100
 Code-projects Computer Book Store 1.0 is vulnerable to SQL Injection via PublisherID.



- [https://github.com/ASR511-OO7/CVE-2024-24100](https://github.com/ASR511-OO7/CVE-2024-24100) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24100.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24100.svg)

## CVE-2024-24099
 Code-projects Scholars Tracking System 1.0 is vulnerable to SQL Injection under Employment Status Information Update.



- [https://github.com/ASR511-OO7/CVE-2024-24099](https://github.com/ASR511-OO7/CVE-2024-24099) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24099.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24099.svg)

## CVE-2024-24098
 Code-projects Scholars Tracking System 1.0 is vulnerable to SQL Injection via the News Feed.



- [https://github.com/ASR511-OO7/CVE-2024-24098](https://github.com/ASR511-OO7/CVE-2024-24098) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24098.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24098.svg)

## CVE-2024-24097
 Cross Site Scripting (XSS) vulnerability in Code-projects Scholars Tracking System 1.0 allows attackers to run arbitrary code via the News Feed.



- [https://github.com/ASR511-OO7/CVE-2024-24097](https://github.com/ASR511-OO7/CVE-2024-24097) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24097.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24097.svg)

## CVE-2024-24096
 Code-projects Computer Book Store 1.0 is vulnerable to SQL Injection via BookSBIN.



- [https://github.com/ASR511-OO7/CVE-2024-24096](https://github.com/ASR511-OO7/CVE-2024-24096) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24096.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24096.svg)

## CVE-2024-24095
 Code-projects Simple Stock System 1.0 is vulnerable to SQL Injection.



- [https://github.com/ASR511-OO7/CVE-2024-24095](https://github.com/ASR511-OO7/CVE-2024-24095) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24095.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24095.svg)

## CVE-2024-24094
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/ASR511-OO7/CVE-2024-24094](https://github.com/ASR511-OO7/CVE-2024-24094) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24094.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24094.svg)

## CVE-2024-24093
 SQL Injection vulnerability in Code-projects Scholars Tracking System 1.0 allows attackers to run arbitrary code via Personal Information Update information.



- [https://github.com/ASR511-OO7/CVE-2024-24093](https://github.com/ASR511-OO7/CVE-2024-24093) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24093.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24093.svg)

## CVE-2024-24092
 SQL Injection vulnerability in Code-projects.org Scholars Tracking System 1.0 allows attackers to run arbitrary code via login.php.



- [https://github.com/ASR511-OO7/CVE-2024-24092](https://github.com/ASR511-OO7/CVE-2024-24092) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24092.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24092.svg)

## CVE-2024-24035
 Cross Site Scripting (XSS) vulnerability in Setor Informatica SIL 3.1 allows attackers to run arbitrary code via the hmessage parameter.



- [https://github.com/ELIZEUOPAIN/PoC-CVE-2024-24035](https://github.com/ELIZEUOPAIN/PoC-CVE-2024-24035) :  ![starts](https://img.shields.io/github/stars/ELIZEUOPAIN/PoC-CVE-2024-24035.svg) ![forks](https://img.shields.io/github/forks/ELIZEUOPAIN/PoC-CVE-2024-24035.svg)

## CVE-2024-24034
 Setor Informatica S.I.L version 3.0 is vulnerable to Open Redirect via the hprinter parameter, allows remote attackers to execute arbitrary code.



- [https://github.com/ELIZEUOPAIN/PoC-CVE-2024-24034](https://github.com/ELIZEUOPAIN/PoC-CVE-2024-24034) :  ![starts](https://img.shields.io/github/stars/ELIZEUOPAIN/PoC-CVE-2024-24034.svg) ![forks](https://img.shields.io/github/forks/ELIZEUOPAIN/PoC-CVE-2024-24034.svg)

## CVE-2024-23898
 Jenkins 2.217 through 2.441 (both inclusive), LTS 2.222.1 through 2.426.2 (both inclusive) does not perform origin validation of requests made through the CLI WebSocket endpoint, resulting in a cross-site WebSocket hijacking (CSWSH) vulnerability, allowing attackers to execute CLI commands on the Jenkins controller.



- [https://github.com/jenkinsci-cert/SECURITY-3314-3315](https://github.com/jenkinsci-cert/SECURITY-3314-3315) :  ![starts](https://img.shields.io/github/stars/jenkinsci-cert/SECURITY-3314-3315.svg) ![forks](https://img.shields.io/github/forks/jenkinsci-cert/SECURITY-3314-3315.svg)

- [https://github.com/davidmgaviria/CVE2_Jenkins_RCE](https://github.com/davidmgaviria/CVE2_Jenkins_RCE) :  ![starts](https://img.shields.io/github/stars/davidmgaviria/CVE2_Jenkins_RCE.svg) ![forks](https://img.shields.io/github/forks/davidmgaviria/CVE2_Jenkins_RCE.svg)

## CVE-2024-23897
 Jenkins 2.441 and earlier, LTS 2.426.2 and earlier does not disable a feature of its CLI command parser that replaces an '@' character followed by a file path in an argument with the file's contents, allowing unauthenticated attackers to read arbitrary files on the Jenkins controller file system.



- [https://github.com/gobysec/Goby](https://github.com/gobysec/Goby) :  ![starts](https://img.shields.io/github/stars/gobysec/Goby.svg) ![forks](https://img.shields.io/github/forks/gobysec/Goby.svg)

- [https://github.com/gobysec/GobyVuls](https://github.com/gobysec/GobyVuls) :  ![starts](https://img.shields.io/github/stars/gobysec/GobyVuls.svg) ![forks](https://img.shields.io/github/forks/gobysec/GobyVuls.svg)

- [https://github.com/h4x0r-dz/CVE-2024-23897](https://github.com/h4x0r-dz/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/h4x0r-dz/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/h4x0r-dz/CVE-2024-23897.svg)

- [https://github.com/binganao/CVE-2024-23897](https://github.com/binganao/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/binganao/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/binganao/CVE-2024-23897.svg)

- [https://github.com/wjlin0/CVE-2024-23897](https://github.com/wjlin0/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/wjlin0/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/wjlin0/CVE-2024-23897.svg)

- [https://github.com/xaitax/CVE-2024-23897](https://github.com/xaitax/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/xaitax/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/xaitax/CVE-2024-23897.svg)

- [https://github.com/godylockz/CVE-2024-23897](https://github.com/godylockz/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/godylockz/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/godylockz/CVE-2024-23897.svg)

- [https://github.com/kaanatmacaa/CVE-2024-23897](https://github.com/kaanatmacaa/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/kaanatmacaa/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/kaanatmacaa/CVE-2024-23897.svg)

- [https://github.com/Vozec/CVE-2024-23897](https://github.com/Vozec/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/Vozec/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/Vozec/CVE-2024-23897.svg)

- [https://github.com/P4x1s/CVE-2024-23897](https://github.com/P4x1s/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2024-23897.svg)

- [https://github.com/Maalfer/CVE-2024-23897](https://github.com/Maalfer/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/Maalfer/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/Maalfer/CVE-2024-23897.svg)

- [https://github.com/jenkinsci-cert/SECURITY-3314-3315](https://github.com/jenkinsci-cert/SECURITY-3314-3315) :  ![starts](https://img.shields.io/github/stars/jenkinsci-cert/SECURITY-3314-3315.svg) ![forks](https://img.shields.io/github/forks/jenkinsci-cert/SECURITY-3314-3315.svg)

- [https://github.com/10T4/PoC-Fix-jenkins-rce_CVE-2024-23897](https://github.com/10T4/PoC-Fix-jenkins-rce_CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/10T4/PoC-Fix-jenkins-rce_CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/10T4/PoC-Fix-jenkins-rce_CVE-2024-23897.svg)

- [https://github.com/viszsec/CVE-2024-23897](https://github.com/viszsec/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/viszsec/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/viszsec/CVE-2024-23897.svg)

- [https://github.com/yoryio/CVE-2024-23897](https://github.com/yoryio/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/yoryio/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/yoryio/CVE-2024-23897.svg)

- [https://github.com/revkami/CVE-2024-23897-Jenkins-4.441](https://github.com/revkami/CVE-2024-23897-Jenkins-4.441) :  ![starts](https://img.shields.io/github/stars/revkami/CVE-2024-23897-Jenkins-4.441.svg) ![forks](https://img.shields.io/github/forks/revkami/CVE-2024-23897-Jenkins-4.441.svg)

- [https://github.com/Praison001/CVE-2024-23897-Jenkins-Arbitrary-Read-File-Vulnerability](https://github.com/Praison001/CVE-2024-23897-Jenkins-Arbitrary-Read-File-Vulnerability) :  ![starts](https://img.shields.io/github/stars/Praison001/CVE-2024-23897-Jenkins-Arbitrary-Read-File-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/Praison001/CVE-2024-23897-Jenkins-Arbitrary-Read-File-Vulnerability.svg)

- [https://github.com/ThatNotEasy/CVE-2024-23897](https://github.com/ThatNotEasy/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2024-23897.svg)

- [https://github.com/vmtyan/poc-cve-2024-23897](https://github.com/vmtyan/poc-cve-2024-23897) :  ![starts](https://img.shields.io/github/stars/vmtyan/poc-cve-2024-23897.svg) ![forks](https://img.shields.io/github/forks/vmtyan/poc-cve-2024-23897.svg)

- [https://github.com/Fineken/Jenkins-CVE-2024-23897-Lab](https://github.com/Fineken/Jenkins-CVE-2024-23897-Lab) :  ![starts](https://img.shields.io/github/stars/Fineken/Jenkins-CVE-2024-23897-Lab.svg) ![forks](https://img.shields.io/github/forks/Fineken/Jenkins-CVE-2024-23897-Lab.svg)

- [https://github.com/D1se0/CVE-2024-23897-Vulnerabilidad-Jenkins](https://github.com/D1se0/CVE-2024-23897-Vulnerabilidad-Jenkins) :  ![starts](https://img.shields.io/github/stars/D1se0/CVE-2024-23897-Vulnerabilidad-Jenkins.svg) ![forks](https://img.shields.io/github/forks/D1se0/CVE-2024-23897-Vulnerabilidad-Jenkins.svg)

- [https://github.com/Anekant-Singhai/Exploits](https://github.com/Anekant-Singhai/Exploits) :  ![starts](https://img.shields.io/github/stars/Anekant-Singhai/Exploits.svg) ![forks](https://img.shields.io/github/forks/Anekant-Singhai/Exploits.svg)

- [https://github.com/JAthulya/CVE-2024-23897](https://github.com/JAthulya/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/JAthulya/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/JAthulya/CVE-2024-23897.svg)

- [https://github.com/R0XDEADBEEF/CVE-2024-23897](https://github.com/R0XDEADBEEF/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/R0XDEADBEEF/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/R0XDEADBEEF/CVE-2024-23897.svg)

- [https://github.com/jopraveen/CVE-2024-23897](https://github.com/jopraveen/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/jopraveen/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/jopraveen/CVE-2024-23897.svg)

- [https://github.com/Nebian/CVE-2024-23897](https://github.com/Nebian/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/Nebian/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/Nebian/CVE-2024-23897.svg)

- [https://github.com/AbraXa5/Jenkins-CVE-2024-23897](https://github.com/AbraXa5/Jenkins-CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/AbraXa5/Jenkins-CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/AbraXa5/Jenkins-CVE-2024-23897.svg)

- [https://github.com/Marouane133/jenkins-lfi](https://github.com/Marouane133/jenkins-lfi) :  ![starts](https://img.shields.io/github/stars/Marouane133/jenkins-lfi.svg) ![forks](https://img.shields.io/github/forks/Marouane133/jenkins-lfi.svg)

- [https://github.com/B4CK4TT4CK/CVE-2024-23897](https://github.com/B4CK4TT4CK/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/B4CK4TT4CK/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/B4CK4TT4CK/CVE-2024-23897.svg)

- [https://github.com/ifconfig-me/CVE-2024-23897](https://github.com/ifconfig-me/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/ifconfig-me/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/ifconfig-me/CVE-2024-23897.svg)

- [https://github.com/cc3305/CVE-2024-23897](https://github.com/cc3305/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/cc3305/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/cc3305/CVE-2024-23897.svg)

- [https://github.com/murataydemir/CVE-2024-23897](https://github.com/murataydemir/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/murataydemir/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/murataydemir/CVE-2024-23897.svg)

- [https://github.com/tvasari/CVE-2024-23897](https://github.com/tvasari/CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/tvasari/CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/tvasari/CVE-2024-23897.svg)

- [https://github.com/tamatee/test_cve_2024_23897](https://github.com/tamatee/test_cve_2024_23897) :  ![starts](https://img.shields.io/github/stars/tamatee/test_cve_2024_23897.svg) ![forks](https://img.shields.io/github/forks/tamatee/test_cve_2024_23897.svg)

- [https://github.com/WLXQqwer/Jenkins-CVE-2024-23897-](https://github.com/WLXQqwer/Jenkins-CVE-2024-23897-) :  ![starts](https://img.shields.io/github/stars/WLXQqwer/Jenkins-CVE-2024-23897-.svg) ![forks](https://img.shields.io/github/forks/WLXQqwer/Jenkins-CVE-2024-23897-.svg)

- [https://github.com/pulentoski/CVE-2024-23897-Arbitrary-file-read](https://github.com/pulentoski/CVE-2024-23897-Arbitrary-file-read) :  ![starts](https://img.shields.io/github/stars/pulentoski/CVE-2024-23897-Arbitrary-file-read.svg) ![forks](https://img.shields.io/github/forks/pulentoski/CVE-2024-23897-Arbitrary-file-read.svg)

- [https://github.com/Surko888/Surko-Exploit-Jenkins-CVE-2024-23897](https://github.com/Surko888/Surko-Exploit-Jenkins-CVE-2024-23897) :  ![starts](https://img.shields.io/github/stars/Surko888/Surko-Exploit-Jenkins-CVE-2024-23897.svg) ![forks](https://img.shields.io/github/forks/Surko888/Surko-Exploit-Jenkins-CVE-2024-23897.svg)

## CVE-2024-23780
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/HazardLab-IO/CVE-2024-23780](https://github.com/HazardLab-IO/CVE-2024-23780) :  ![starts](https://img.shields.io/github/stars/HazardLab-IO/CVE-2024-23780.svg) ![forks](https://img.shields.io/github/forks/HazardLab-IO/CVE-2024-23780.svg)

## CVE-2024-23774
 An issue was discovered in Quest KACE Agent for Windows 12.0.38 and 13.1.23.0. An unquoted Windows search path vulnerability exists in the KSchedulerSvc.exe and AMPTools.exe components. This allows local attackers to execute code of their choice with NT Authority\SYSTEM privileges.



- [https://github.com/Verrideo/CVE-2024-23774](https://github.com/Verrideo/CVE-2024-23774) :  ![starts](https://img.shields.io/github/stars/Verrideo/CVE-2024-23774.svg) ![forks](https://img.shields.io/github/forks/Verrideo/CVE-2024-23774.svg)

## CVE-2024-23773
 An issue was discovered in Quest KACE Agent for Windows 12.0.38 and 13.1.23.0. An Arbitrary file delete vulnerability exists in the KSchedulerSvc.exe component. Local attackers can delete any file of their choice with NT Authority\SYSTEM privileges.



- [https://github.com/Verrideo/CVE-2024-23773](https://github.com/Verrideo/CVE-2024-23773) :  ![starts](https://img.shields.io/github/stars/Verrideo/CVE-2024-23773.svg) ![forks](https://img.shields.io/github/forks/Verrideo/CVE-2024-23773.svg)

## CVE-2024-23772
 An issue was discovered in Quest KACE Agent for Windows 12.0.38 and 13.1.23.0. An Arbitrary file create vulnerability exists in the KSchedulerSvc.exe, KUserAlert.exe, and Runkbot.exe components. This allows local attackers to create any file of their choice with NT Authority\SYSTEM privileges.



- [https://github.com/Verrideo/CVE-2024-23772](https://github.com/Verrideo/CVE-2024-23772) :  ![starts](https://img.shields.io/github/stars/Verrideo/CVE-2024-23772.svg) ![forks](https://img.shields.io/github/forks/Verrideo/CVE-2024-23772.svg)

## CVE-2024-23747
 The Moderna Sistemas ModernaNet Hospital Management System 2024 is susceptible to an Insecure Direct Object Reference (IDOR) vulnerability. This vulnerability resides in the system's handling of user data access through a /Modernanet/LAUDO/LAU0000100/Laudo?id= URI. By manipulating this id parameter, an attacker can gain access to sensitive medical information.



- [https://github.com/louiselalanne/CVE-2024-23747](https://github.com/louiselalanne/CVE-2024-23747) :  ![starts](https://img.shields.io/github/stars/louiselalanne/CVE-2024-23747.svg) ![forks](https://img.shields.io/github/forks/louiselalanne/CVE-2024-23747.svg)

## CVE-2024-23746
 Miro Desktop 0.8.18 on macOS allows local Electron code injection via a complex series of steps that might be usable in some environments (bypass a kTCCServiceSystemPolicyAppBundles requirement via a file copy, an app.app/Contents rename, an asar modification, and a rename back to app.app/Contents).



- [https://github.com/louiselalanne/CVE-2024-23746](https://github.com/louiselalanne/CVE-2024-23746) :  ![starts](https://img.shields.io/github/stars/louiselalanne/CVE-2024-23746.svg) ![forks](https://img.shields.io/github/forks/louiselalanne/CVE-2024-23746.svg)

## CVE-2024-23745
 In Notion Web Clipper 1.0.3(7), a .nib file is susceptible to the Dirty NIB attack. NIB files can be manipulated to execute arbitrary commands. Additionally, even if a NIB file is modified within an application, Gatekeeper may still permit the execution of the application, enabling the execution of arbitrary commands within the application's context. NOTE: the vendor's perspective is that this is simply an instance of CVE-2022-48505, cannot properly be categorized as a product-level vulnerability, and cannot have a product-level fix because it is about incorrect caching of file signatures on macOS.



- [https://github.com/louiselalanne/CVE-2024-23745](https://github.com/louiselalanne/CVE-2024-23745) :  ![starts](https://img.shields.io/github/stars/louiselalanne/CVE-2024-23745.svg) ![forks](https://img.shields.io/github/forks/louiselalanne/CVE-2024-23745.svg)

## CVE-2024-23743
 Notion through 3.1.0 on macOS might allow code execution because of RunAsNode and enableNodeClilnspectArguments. NOTE: the vendor states "the attacker must launch the Notion Desktop application with nonstandard flags that turn the Electron-based application into a Node.js execution environment."



- [https://github.com/giovannipajeu1/CVE-2024-23743](https://github.com/giovannipajeu1/CVE-2024-23743) :  ![starts](https://img.shields.io/github/stars/giovannipajeu1/CVE-2024-23743.svg) ![forks](https://img.shields.io/github/forks/giovannipajeu1/CVE-2024-23743.svg)

## CVE-2024-23742
 An issue in Loom on macOS version 0.196.1 and before, allows remote attackers to execute arbitrary code via the RunAsNode and enableNodeClilnspectArguments settings. NOTE: the vendor disputes this because it requires local access to a victim's machine.



- [https://github.com/giovannipajeu1/CVE-2024-23742](https://github.com/giovannipajeu1/CVE-2024-23742) :  ![starts](https://img.shields.io/github/stars/giovannipajeu1/CVE-2024-23742.svg) ![forks](https://img.shields.io/github/forks/giovannipajeu1/CVE-2024-23742.svg)

## CVE-2024-23741
 An issue in Hyper on macOS version 3.4.1 and before, allows remote attackers to execute arbitrary code via the RunAsNode and enableNodeClilnspectArguments settings.



- [https://github.com/giovannipajeu1/CVE-2024-23741](https://github.com/giovannipajeu1/CVE-2024-23741) :  ![starts](https://img.shields.io/github/stars/giovannipajeu1/CVE-2024-23741.svg) ![forks](https://img.shields.io/github/forks/giovannipajeu1/CVE-2024-23741.svg)

## CVE-2024-23740
 An issue in Kap for macOS version 3.6.0 and before, allows remote attackers to execute arbitrary code via the RunAsNode and enableNodeClilnspectArguments settings.



- [https://github.com/giovannipajeu1/CVE-2024-23740](https://github.com/giovannipajeu1/CVE-2024-23740) :  ![starts](https://img.shields.io/github/stars/giovannipajeu1/CVE-2024-23740.svg) ![forks](https://img.shields.io/github/forks/giovannipajeu1/CVE-2024-23740.svg)

## CVE-2024-23739
 An issue in Discord for macOS version 0.0.291 and before, allows remote attackers to execute arbitrary code via the RunAsNode and enableNodeClilnspectArguments settings.



- [https://github.com/giovannipajeu1/CVE-2024-23739](https://github.com/giovannipajeu1/CVE-2024-23739) :  ![starts](https://img.shields.io/github/stars/giovannipajeu1/CVE-2024-23739.svg) ![forks](https://img.shields.io/github/forks/giovannipajeu1/CVE-2024-23739.svg)

- [https://github.com/giovannipajeu1/CVE-2024-23740](https://github.com/giovannipajeu1/CVE-2024-23740) :  ![starts](https://img.shields.io/github/stars/giovannipajeu1/CVE-2024-23740.svg) ![forks](https://img.shields.io/github/forks/giovannipajeu1/CVE-2024-23740.svg)

## CVE-2024-23738
 An issue in Postman version 10.22 and before on macOS allows a remote attacker to execute arbitrary code via the RunAsNode and enableNodeClilnspectArguments settings. NOTE: the vendor states "we dispute the report's accuracy ... the configuration does not enable remote code execution.."



- [https://github.com/giovannipajeu1/CVE-2024-23738](https://github.com/giovannipajeu1/CVE-2024-23738) :  ![starts](https://img.shields.io/github/stars/giovannipajeu1/CVE-2024-23738.svg) ![forks](https://img.shields.io/github/forks/giovannipajeu1/CVE-2024-23738.svg)

## CVE-2024-23727
 The YI Smart Kami Vision com.kamivision.yismart application through 1.0.0_20231219 for Android allows a remote attacker to execute arbitrary JavaScript code via an implicit intent to the com.ants360.yicamera.activity.WebViewActivity component.



- [https://github.com/actuator/yi](https://github.com/actuator/yi) :  ![starts](https://img.shields.io/github/stars/actuator/yi.svg) ![forks](https://img.shields.io/github/forks/actuator/yi.svg)

## CVE-2024-23726
 Ubee DDW365 XCNDDW365 devices have predictable default WPA2 PSKs that could lead to unauthorized remote access. A remote attacker (in proximity to a Wi-Fi network) can derive the default WPA2-PSK value by observing a beacon frame. A PSK is generated by using the first six characters of the SSID and the last six of the BSSID, decrementing the last digit.



- [https://github.com/actuator/BSIDES-Security-Las-Vegas-2024](https://github.com/actuator/BSIDES-Security-Las-Vegas-2024) :  ![starts](https://img.shields.io/github/stars/actuator/BSIDES-Security-Las-Vegas-2024.svg) ![forks](https://img.shields.io/github/forks/actuator/BSIDES-Security-Las-Vegas-2024.svg)

## CVE-2024-23722
 In Fluent Bit 2.1.8 through 2.2.1, a NULL pointer dereference can be caused via an invalid HTTP payload with the content type of x-www-form-urlencoded. It crashes and does not restart. This could result in logs not being delivered properly.



- [https://github.com/alexcote1/CVE-2024-23722-poc](https://github.com/alexcote1/CVE-2024-23722-poc) :  ![starts](https://img.shields.io/github/stars/alexcote1/CVE-2024-23722-poc.svg) ![forks](https://img.shields.io/github/forks/alexcote1/CVE-2024-23722-poc.svg)

## CVE-2024-23709
 In multiple locations, there is a possible out of bounds write due to a heap buffer overflow. This could lead to remote information disclosure with no additional execution privileges needed. User interaction is needed for exploitation.



- [https://github.com/AbrarKhan/external_sonivox_CVE-2024-23709](https://github.com/AbrarKhan/external_sonivox_CVE-2024-23709) :  ![starts](https://img.shields.io/github/stars/AbrarKhan/external_sonivox_CVE-2024-23709.svg) ![forks](https://img.shields.io/github/forks/AbrarKhan/external_sonivox_CVE-2024-23709.svg)

## CVE-2024-23708
 In multiple functions of NotificationManagerService.java, there is a possible way to not show a toast message when a clipboard message has been accessed. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/uthrasri/CVE-2024-23708](https://github.com/uthrasri/CVE-2024-23708) :  ![starts](https://img.shields.io/github/stars/uthrasri/CVE-2024-23708.svg) ![forks](https://img.shields.io/github/forks/uthrasri/CVE-2024-23708.svg)

## CVE-2024-23692
 Rejetto HTTP File Server, up to and including version 2.3m, is vulnerable to a template injection vulnerability. This vulnerability allows a remote, unauthenticated attacker to execute arbitrary commands on the affected system by sending a specially crafted HTTP request. As of the CVE assignment date, Rejetto HFS 2.3m is no longer supported.



- [https://github.com/jakabakos/CVE-2024-23692-RCE-in-Rejetto-HFS](https://github.com/jakabakos/CVE-2024-23692-RCE-in-Rejetto-HFS) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2024-23692-RCE-in-Rejetto-HFS.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2024-23692-RCE-in-Rejetto-HFS.svg)

- [https://github.com/0x20c/CVE-2024-23692-EXP](https://github.com/0x20c/CVE-2024-23692-EXP) :  ![starts](https://img.shields.io/github/stars/0x20c/CVE-2024-23692-EXP.svg) ![forks](https://img.shields.io/github/forks/0x20c/CVE-2024-23692-EXP.svg)

- [https://github.com/vanboomqi/CVE-2024-23692](https://github.com/vanboomqi/CVE-2024-23692) :  ![starts](https://img.shields.io/github/stars/vanboomqi/CVE-2024-23692.svg) ![forks](https://img.shields.io/github/forks/vanboomqi/CVE-2024-23692.svg)

- [https://github.com/BBD-YZZ/CVE-2024-23692](https://github.com/BBD-YZZ/CVE-2024-23692) :  ![starts](https://img.shields.io/github/stars/BBD-YZZ/CVE-2024-23692.svg) ![forks](https://img.shields.io/github/forks/BBD-YZZ/CVE-2024-23692.svg)

- [https://github.com/XiaomingX/cve-2024-23692-poc](https://github.com/XiaomingX/cve-2024-23692-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-23692-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-23692-poc.svg)

- [https://github.com/NanoWraith/CVE-2024-23692](https://github.com/NanoWraith/CVE-2024-23692) :  ![starts](https://img.shields.io/github/stars/NanoWraith/CVE-2024-23692.svg) ![forks](https://img.shields.io/github/forks/NanoWraith/CVE-2024-23692.svg)

- [https://github.com/pradeepboo/Rejetto-HFS-2.x-RCE-CVE-2024-23692](https://github.com/pradeepboo/Rejetto-HFS-2.x-RCE-CVE-2024-23692) :  ![starts](https://img.shields.io/github/stars/pradeepboo/Rejetto-HFS-2.x-RCE-CVE-2024-23692.svg) ![forks](https://img.shields.io/github/forks/pradeepboo/Rejetto-HFS-2.x-RCE-CVE-2024-23692.svg)

- [https://github.com/NingXin2002/HFS2.3_poc](https://github.com/NingXin2002/HFS2.3_poc) :  ![starts](https://img.shields.io/github/stars/NingXin2002/HFS2.3_poc.svg) ![forks](https://img.shields.io/github/forks/NingXin2002/HFS2.3_poc.svg)

- [https://github.com/Tupler/CVE-2024-23692-exp](https://github.com/Tupler/CVE-2024-23692-exp) :  ![starts](https://img.shields.io/github/stars/Tupler/CVE-2024-23692-exp.svg) ![forks](https://img.shields.io/github/forks/Tupler/CVE-2024-23692-exp.svg)

- [https://github.com/Mr-r00t11/CVE-2024-23692](https://github.com/Mr-r00t11/CVE-2024-23692) :  ![starts](https://img.shields.io/github/stars/Mr-r00t11/CVE-2024-23692.svg) ![forks](https://img.shields.io/github/forks/Mr-r00t11/CVE-2024-23692.svg)

- [https://github.com/WanLiChangChengWanLiChang/CVE-2024-23692-RCE](https://github.com/WanLiChangChengWanLiChang/CVE-2024-23692-RCE) :  ![starts](https://img.shields.io/github/stars/WanLiChangChengWanLiChang/CVE-2024-23692-RCE.svg) ![forks](https://img.shields.io/github/forks/WanLiChangChengWanLiChang/CVE-2024-23692-RCE.svg)

## CVE-2024-23653
 BuildKit is a toolkit for converting source code to build artifacts in an efficient, expressive and repeatable manner. In addition to running containers as build steps, BuildKit also provides APIs for running interactive containers based on built images. It was possible to use these APIs to ask BuildKit to run a container with elevated privileges. Normally, running such containers is only allowed if special `security.insecure` entitlement is enabled both by buildkitd configuration and allowed by the user initializing the build request. The issue has been fixed in v0.12.5 . Avoid using BuildKit frontends from untrusted sources. 




- [https://github.com/666asd/CVE-2024-23653](https://github.com/666asd/CVE-2024-23653) :  ![starts](https://img.shields.io/github/stars/666asd/CVE-2024-23653.svg) ![forks](https://img.shields.io/github/forks/666asd/CVE-2024-23653.svg)

## CVE-2024-23652
 BuildKit is a toolkit for converting source code to build artifacts in an efficient, expressive and repeatable manner. A malicious BuildKit frontend or Dockerfile using RUN --mount could trick the feature that removes empty files created for the mountpoints into removing a file outside the container, from the host system. The issue has been fixed in v0.12.5. Workarounds include avoiding using BuildKit frontends from an untrusted source or building an untrusted Dockerfile containing RUN --mount feature.



- [https://github.com/abian2/CVE-2024-23652](https://github.com/abian2/CVE-2024-23652) :  ![starts](https://img.shields.io/github/stars/abian2/CVE-2024-23652.svg) ![forks](https://img.shields.io/github/forks/abian2/CVE-2024-23652.svg)

## CVE-2024-23443
 A high-privileged user, allowed to create custom osquery packs 17 could affect the availability of Kibana by uploading a maliciously crafted osquery pack.



- [https://github.com/zhazhalove/osquery_cve-2024-23443](https://github.com/zhazhalove/osquery_cve-2024-23443) :  ![starts](https://img.shields.io/github/stars/zhazhalove/osquery_cve-2024-23443.svg) ![forks](https://img.shields.io/github/forks/zhazhalove/osquery_cve-2024-23443.svg)

## CVE-2024-23346
 Pymatgen (Python Materials Genomics) is an open-source Python library for materials analysis. A critical security vulnerability exists in the `JonesFaithfulTransformation.from_transformation_str()` method within the `pymatgen` library prior to version 2024.2.20. This method insecurely utilizes `eval()` for processing input, enabling execution of arbitrary code when parsing untrusted input. Version 2024.2.20 fixes this issue.



- [https://github.com/9carlo6/CVE-2024-23346](https://github.com/9carlo6/CVE-2024-23346) :  ![starts](https://img.shields.io/github/stars/9carlo6/CVE-2024-23346.svg) ![forks](https://img.shields.io/github/forks/9carlo6/CVE-2024-23346.svg)

- [https://github.com/DAVIDAROCA27/CVE-2024-23346-exploit](https://github.com/DAVIDAROCA27/CVE-2024-23346-exploit) :  ![starts](https://img.shields.io/github/stars/DAVIDAROCA27/CVE-2024-23346-exploit.svg) ![forks](https://img.shields.io/github/forks/DAVIDAROCA27/CVE-2024-23346-exploit.svg)

- [https://github.com/mbanyamer/-Pymatgen-2024.1---Remote-Code-Execution-RCE-](https://github.com/mbanyamer/-Pymatgen-2024.1---Remote-Code-Execution-RCE-) :  ![starts](https://img.shields.io/github/stars/mbanyamer/-Pymatgen-2024.1---Remote-Code-Execution-RCE-.svg) ![forks](https://img.shields.io/github/forks/mbanyamer/-Pymatgen-2024.1---Remote-Code-Execution-RCE-.svg)

- [https://github.com/MAWK0235/CVE-2024-23346](https://github.com/MAWK0235/CVE-2024-23346) :  ![starts](https://img.shields.io/github/stars/MAWK0235/CVE-2024-23346.svg) ![forks](https://img.shields.io/github/forks/MAWK0235/CVE-2024-23346.svg)

## CVE-2024-23334
 aiohttp is an asynchronous HTTP client/server framework for asyncio and Python. When using aiohttp as a web server and configuring static routes, it is necessary to specify the root path for static files. Additionally, the option 'follow_symlinks' can be used to determine whether to follow symbolic links outside the static root directory. When 'follow_symlinks' is set to True, there is no validation to check if reading a file is within the root directory. This can lead to directory traversal vulnerabilities, resulting in unauthorized access to arbitrary files on the system, even when symlinks are not present.  Disabling follow_symlinks and using a reverse proxy are encouraged mitigations.  Version 3.9.2 fixes this issue.



- [https://github.com/jhonnybonny/CVE-2024-23334](https://github.com/jhonnybonny/CVE-2024-23334) :  ![starts](https://img.shields.io/github/stars/jhonnybonny/CVE-2024-23334.svg) ![forks](https://img.shields.io/github/forks/jhonnybonny/CVE-2024-23334.svg)

- [https://github.com/z3rObyte/CVE-2024-23334-PoC](https://github.com/z3rObyte/CVE-2024-23334-PoC) :  ![starts](https://img.shields.io/github/stars/z3rObyte/CVE-2024-23334-PoC.svg) ![forks](https://img.shields.io/github/forks/z3rObyte/CVE-2024-23334-PoC.svg)

- [https://github.com/ox1111/CVE-2024-23334](https://github.com/ox1111/CVE-2024-23334) :  ![starts](https://img.shields.io/github/stars/ox1111/CVE-2024-23334.svg) ![forks](https://img.shields.io/github/forks/ox1111/CVE-2024-23334.svg)

- [https://github.com/sxyrxyy/aiohttp-exploit-CVE-2024-23334-certstream](https://github.com/sxyrxyy/aiohttp-exploit-CVE-2024-23334-certstream) :  ![starts](https://img.shields.io/github/stars/sxyrxyy/aiohttp-exploit-CVE-2024-23334-certstream.svg) ![forks](https://img.shields.io/github/forks/sxyrxyy/aiohttp-exploit-CVE-2024-23334-certstream.svg)

- [https://github.com/TheRedP4nther/LFI-aiohttp-CVE-2024-23334-PoC](https://github.com/TheRedP4nther/LFI-aiohttp-CVE-2024-23334-PoC) :  ![starts](https://img.shields.io/github/stars/TheRedP4nther/LFI-aiohttp-CVE-2024-23334-PoC.svg) ![forks](https://img.shields.io/github/forks/TheRedP4nther/LFI-aiohttp-CVE-2024-23334-PoC.svg)

- [https://github.com/Betan423/CVE-2024-23334-PoC](https://github.com/Betan423/CVE-2024-23334-PoC) :  ![starts](https://img.shields.io/github/stars/Betan423/CVE-2024-23334-PoC.svg) ![forks](https://img.shields.io/github/forks/Betan423/CVE-2024-23334-PoC.svg)

- [https://github.com/Arc4he/CVE-2024-23334-PoC](https://github.com/Arc4he/CVE-2024-23334-PoC) :  ![starts](https://img.shields.io/github/stars/Arc4he/CVE-2024-23334-PoC.svg) ![forks](https://img.shields.io/github/forks/Arc4he/CVE-2024-23334-PoC.svg)

- [https://github.com/binaryninja/CVE-2024-23334](https://github.com/binaryninja/CVE-2024-23334) :  ![starts](https://img.shields.io/github/stars/binaryninja/CVE-2024-23334.svg) ![forks](https://img.shields.io/github/forks/binaryninja/CVE-2024-23334.svg)

- [https://github.com/Pylonet/CVE-2024-23334](https://github.com/Pylonet/CVE-2024-23334) :  ![starts](https://img.shields.io/github/stars/Pylonet/CVE-2024-23334.svg) ![forks](https://img.shields.io/github/forks/Pylonet/CVE-2024-23334.svg)

- [https://github.com/brian-edgar-re/poc-cve-2024-23334](https://github.com/brian-edgar-re/poc-cve-2024-23334) :  ![starts](https://img.shields.io/github/stars/brian-edgar-re/poc-cve-2024-23334.svg) ![forks](https://img.shields.io/github/forks/brian-edgar-re/poc-cve-2024-23334.svg)

- [https://github.com/BestDevOfc/CVE-2024-23334-PoC](https://github.com/BestDevOfc/CVE-2024-23334-PoC) :  ![starts](https://img.shields.io/github/stars/BestDevOfc/CVE-2024-23334-PoC.svg) ![forks](https://img.shields.io/github/forks/BestDevOfc/CVE-2024-23334-PoC.svg)

## CVE-2024-23298
 A logic issue was addressed with improved state management.



- [https://github.com/p1tsi/CVE-2024-23298.app](https://github.com/p1tsi/CVE-2024-23298.app) :  ![starts](https://img.shields.io/github/stars/p1tsi/CVE-2024-23298.app.svg) ![forks](https://img.shields.io/github/forks/p1tsi/CVE-2024-23298.app.svg)

## CVE-2024-23208
 The issue was addressed with improved memory handling. This issue is fixed in macOS Sonoma 14.3, watchOS 10.3, tvOS 17.3, iOS 17.3 and iPadOS 17.3. An app may be able to execute arbitrary code with kernel privileges.



- [https://github.com/hrtowii/CVE-2024-23208-test](https://github.com/hrtowii/CVE-2024-23208-test) :  ![starts](https://img.shields.io/github/stars/hrtowii/CVE-2024-23208-test.svg) ![forks](https://img.shields.io/github/forks/hrtowii/CVE-2024-23208-test.svg)

## CVE-2024-23200
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/l00neyhacker/CVE-2024-23200](https://github.com/l00neyhacker/CVE-2024-23200) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-23200.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-23200.svg)

## CVE-2024-23199
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/l00neyhacker/CVE-2024-23199](https://github.com/l00neyhacker/CVE-2024-23199) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-23199.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-23199.svg)

## CVE-2024-23113
 A use of externally-controlled format string in Fortinet FortiOS versions 7.4.0 through 7.4.2, 7.2.0 through 7.2.6, 7.0.0 through 7.0.13, FortiProxy versions 7.4.0 through 7.4.2, 7.2.0 through 7.2.8, 7.0.0 through 7.0.14, FortiPAM versions 1.2.0, 1.1.0 through 1.1.2, 1.0.0 through 1.0.3, FortiSwitchManager versions 7.2.0 through 7.2.3, 7.0.0 through 7.0.3 allows attacker to execute unauthorized code or commands via specially crafted packets.



- [https://github.com/XiaomingX/cve-2024-23113-exp](https://github.com/XiaomingX/cve-2024-23113-exp) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-23113-exp.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-23113-exp.svg)

- [https://github.com/XiaomingX/cve-2024-23113-poc](https://github.com/XiaomingX/cve-2024-23113-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-23113-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-23113-poc.svg)

- [https://github.com/valornode/CVE-2024-23113](https://github.com/valornode/CVE-2024-23113) :  ![starts](https://img.shields.io/github/stars/valornode/CVE-2024-23113.svg) ![forks](https://img.shields.io/github/forks/valornode/CVE-2024-23113.svg)

- [https://github.com/MAVRICK-1/cve-2024-23113-test-env](https://github.com/MAVRICK-1/cve-2024-23113-test-env) :  ![starts](https://img.shields.io/github/stars/MAVRICK-1/cve-2024-23113-test-env.svg) ![forks](https://img.shields.io/github/forks/MAVRICK-1/cve-2024-23113-test-env.svg)

## CVE-2024-23108
 An improper neutralization of special elements used in an os command ('os command injection') in Fortinet FortiSIEM version 7.1.0 through 7.1.1 and 7.0.0 through 7.0.2 and 6.7.0 through 6.7.8 and 6.6.0 through 6.6.3 and 6.5.0 through 6.5.2 and 6.4.0 through 6.4.2 allows attacker to execute unauthorized code or commands via via crafted API requests.



- [https://github.com/horizon3ai/CVE-2024-23108](https://github.com/horizon3ai/CVE-2024-23108) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2024-23108.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2024-23108.svg)

- [https://github.com/hitem/CVE-2024-23108](https://github.com/hitem/CVE-2024-23108) :  ![starts](https://img.shields.io/github/stars/hitem/CVE-2024-23108.svg) ![forks](https://img.shields.io/github/forks/hitem/CVE-2024-23108.svg)

## CVE-2024-23002
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/xiaomaoxxx/CVE-2024-23002](https://github.com/xiaomaoxxx/CVE-2024-23002) :  ![starts](https://img.shields.io/github/stars/xiaomaoxxx/CVE-2024-23002.svg) ![forks](https://img.shields.io/github/forks/xiaomaoxxx/CVE-2024-23002.svg)

## CVE-2024-22983
 SQL injection vulnerability in Projectworlds Visitor Management System in PHP v.1.0 allows a remote attacker to escalate privileges via the name parameter in the myform.php endpoint.



- [https://github.com/pwnpwnpur1n/CVE-2024-22983](https://github.com/pwnpwnpur1n/CVE-2024-22983) :  ![starts](https://img.shields.io/github/stars/pwnpwnpur1n/CVE-2024-22983.svg) ![forks](https://img.shields.io/github/forks/pwnpwnpur1n/CVE-2024-22983.svg)

## CVE-2024-22939
 Cross Site Request Forgery vulnerability in FlyCms v.1.0 allows a remote attacker to execute arbitrary code via the system/article/category_edit component.



- [https://github.com/NUDTTAN91/CVE-2024-22939](https://github.com/NUDTTAN91/CVE-2024-22939) :  ![starts](https://img.shields.io/github/stars/NUDTTAN91/CVE-2024-22939.svg) ![forks](https://img.shields.io/github/forks/NUDTTAN91/CVE-2024-22939.svg)

## CVE-2024-22922
 An issue in Projectworlds Vistor Management Systemin PHP v.1.0 allows a remtoe attacker to escalate privileges via a crafted script to the login page in the POST/index.php



- [https://github.com/pwnpwnpur1n/CVE-2024-22922](https://github.com/pwnpwnpur1n/CVE-2024-22922) :  ![starts](https://img.shields.io/github/stars/pwnpwnpur1n/CVE-2024-22922.svg) ![forks](https://img.shields.io/github/forks/pwnpwnpur1n/CVE-2024-22922.svg)

## CVE-2024-22917
 SQL injection vulnerability in Dynamic Lab Management System Project in PHP v.1.0 allows a remote attacker to execute arbitrary code via a crafted script.



- [https://github.com/ASR511-OO7/CVE-2024-22917](https://github.com/ASR511-OO7/CVE-2024-22917) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-22917.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-22917.svg)

## CVE-2024-22909
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/BurakSevben/CVE-2024-22909](https://github.com/BurakSevben/CVE-2024-22909) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-22909.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-22909.svg)

## CVE-2024-22903
 Vinchin Backup & Recovery v7.2 was discovered to contain an authenticated remote code execution (RCE) vulnerability via the deleteUpdateAPK function.



- [https://github.com/Chocapikk/CVE-2024-22899-to-22903-ExploitChain](https://github.com/Chocapikk/CVE-2024-22899-to-22903-ExploitChain) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-22899-to-22903-ExploitChain.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-22899-to-22903-ExploitChain.svg)

## CVE-2024-22902
 Vinchin Backup & Recovery v7.2 was discovered to be configured with default root credentials.



- [https://github.com/Chocapikk/CVE-2024-22899-to-22903-ExploitChain](https://github.com/Chocapikk/CVE-2024-22899-to-22903-ExploitChain) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-22899-to-22903-ExploitChain.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-22899-to-22903-ExploitChain.svg)

## CVE-2024-22901
 Vinchin Backup & Recovery v7.2 was discovered to use default MYSQL credentials.



- [https://github.com/Chocapikk/CVE-2024-22899-to-22903-ExploitChain](https://github.com/Chocapikk/CVE-2024-22899-to-22903-ExploitChain) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-22899-to-22903-ExploitChain.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-22899-to-22903-ExploitChain.svg)

## CVE-2024-22900
 Vinchin Backup & Recovery v7.2 was discovered to contain an authenticated remote code execution (RCE) vulnerability via the setNetworkCardInfo function.



- [https://github.com/Chocapikk/CVE-2024-22899-to-22903-ExploitChain](https://github.com/Chocapikk/CVE-2024-22899-to-22903-ExploitChain) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-22899-to-22903-ExploitChain.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-22899-to-22903-ExploitChain.svg)

## CVE-2024-22899
 Vinchin Backup & Recovery v7.2 was discovered to contain an authenticated remote code execution (RCE) vulnerability via the syncNtpTime function.



- [https://github.com/Chocapikk/CVE-2024-22899-to-22903-ExploitChain](https://github.com/Chocapikk/CVE-2024-22899-to-22903-ExploitChain) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-22899-to-22903-ExploitChain.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-22899-to-22903-ExploitChain.svg)

## CVE-2024-22894
 An issue fixed in AIT-Deutschland Alpha Innotec Heatpumps V2.88.3 or later, V3.89.0 or later, V4.81.3 or later and Novelan Heatpumps V2.88.3 or later, V3.89.0 or later, V4.81.3 or later, allows remote attackers to execute arbitrary code via the password component in the shadow file.



- [https://github.com/Jaarden/CVE-2024-22894](https://github.com/Jaarden/CVE-2024-22894) :  ![starts](https://img.shields.io/github/stars/Jaarden/CVE-2024-22894.svg) ![forks](https://img.shields.io/github/forks/Jaarden/CVE-2024-22894.svg)

## CVE-2024-22890
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/BurakSevben/CVE-2024-22890](https://github.com/BurakSevben/CVE-2024-22890) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-22890.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-22890.svg)

## CVE-2024-22889
 Due to incorrect access control in Plone version v6.0.9, remote attackers can view and list all files hosted on the website via sending a crafted request.



- [https://github.com/shenhav12/CVE-2024-22889-Plone-v6.0.9](https://github.com/shenhav12/CVE-2024-22889-Plone-v6.0.9) :  ![starts](https://img.shields.io/github/stars/shenhav12/CVE-2024-22889-Plone-v6.0.9.svg) ![forks](https://img.shields.io/github/forks/shenhav12/CVE-2024-22889-Plone-v6.0.9.svg)

## CVE-2024-22867
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/brandon-t-elliott/CVE-2024-22867](https://github.com/brandon-t-elliott/CVE-2024-22867) :  ![starts](https://img.shields.io/github/stars/brandon-t-elliott/CVE-2024-22867.svg) ![forks](https://img.shields.io/github/forks/brandon-t-elliott/CVE-2024-22867.svg)

## CVE-2024-22853
 D-LINK Go-RT-AC750 GORTAC750_A1_FW_v101b03 has a hardcoded password for the Alphanetworks account, which allows remote attackers to obtain root access via a telnet session.



- [https://github.com/FaLLenSKiLL1/CVE-2024-22853](https://github.com/FaLLenSKiLL1/CVE-2024-22853) :  ![starts](https://img.shields.io/github/stars/FaLLenSKiLL1/CVE-2024-22853.svg) ![forks](https://img.shields.io/github/forks/FaLLenSKiLL1/CVE-2024-22853.svg)

## CVE-2024-22774
 An issue in Panoramic Corporation Digital Imaging Software v.9.1.2.7600 allows a local attacker to escalate privileges via the ccsservice.exe component.



- [https://github.com/Gray-0men/CVE-2024-22774](https://github.com/Gray-0men/CVE-2024-22774) :  ![starts](https://img.shields.io/github/stars/Gray-0men/CVE-2024-22774.svg) ![forks](https://img.shields.io/github/forks/Gray-0men/CVE-2024-22774.svg)

## CVE-2024-22752
 Insecure permissions issue in EaseUS MobiMover 6.0.5 Build 21620 allows attackers to gain escalated privileges via use of crafted executable launched from the application installation directory.



- [https://github.com/hacker625/CVE-2024-22752](https://github.com/hacker625/CVE-2024-22752) :  ![starts](https://img.shields.io/github/stars/hacker625/CVE-2024-22752.svg) ![forks](https://img.shields.io/github/forks/hacker625/CVE-2024-22752.svg)

## CVE-2024-22734
 An issue was discovered in AMCS Group Trux Waste Management Software before version 7.19.0018.26912, allows local attackers to obtain sensitive information via a static, hard-coded AES Key-IV pair in the TxUtilities.dll and TruxUser.cfg components.



- [https://github.com/securekomodo/CVE-2024-22734](https://github.com/securekomodo/CVE-2024-22734) :  ![starts](https://img.shields.io/github/stars/securekomodo/CVE-2024-22734.svg) ![forks](https://img.shields.io/github/forks/securekomodo/CVE-2024-22734.svg)

## CVE-2024-22678
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/l00neyhacker/CVE-2024-22678](https://github.com/l00neyhacker/CVE-2024-22678) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-22678.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-22678.svg)

## CVE-2024-22676
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/l00neyhacker/CVE-2024-22676](https://github.com/l00neyhacker/CVE-2024-22676) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-22676.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-22676.svg)

## CVE-2024-22675
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/l00neyhacker/CVE-2024-22675](https://github.com/l00neyhacker/CVE-2024-22675) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-22675.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-22675.svg)

## CVE-2024-22641
 TCPDF version 6.6.5 and before is vulnerable to ReDoS (Regular Expression Denial of Service) if parsing an untrusted SVG file.



- [https://github.com/zunak/CVE-2024-22641](https://github.com/zunak/CVE-2024-22641) :  ![starts](https://img.shields.io/github/stars/zunak/CVE-2024-22641.svg) ![forks](https://img.shields.io/github/forks/zunak/CVE-2024-22641.svg)

## CVE-2024-22640
 TCPDF version =6.6.5 is vulnerable to ReDoS (Regular Expression Denial of Service) if parsing an untrusted HTML page with a crafted color.



- [https://github.com/zunak/CVE-2024-22640](https://github.com/zunak/CVE-2024-22640) :  ![starts](https://img.shields.io/github/stars/zunak/CVE-2024-22640.svg) ![forks](https://img.shields.io/github/forks/zunak/CVE-2024-22640.svg)

## CVE-2024-22534
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/austino2000/CVE-2024-22534](https://github.com/austino2000/CVE-2024-22534) :  ![starts](https://img.shields.io/github/stars/austino2000/CVE-2024-22534.svg) ![forks](https://img.shields.io/github/forks/austino2000/CVE-2024-22534.svg)

## CVE-2024-22532
 Buffer Overflow vulnerability in XNSoft NConvert 7.163 (for Windows x86) allows attackers to cause a denial of service via crafted xwd file.



- [https://github.com/pwndorei/CVE-2024-22532](https://github.com/pwndorei/CVE-2024-22532) :  ![starts](https://img.shields.io/github/stars/pwndorei/CVE-2024-22532.svg) ![forks](https://img.shields.io/github/forks/pwndorei/CVE-2024-22532.svg)

## CVE-2024-22515
 Unrestricted File Upload vulnerability in iSpyConnect.com Agent DVR 5.1.6.0 allows attackers to upload arbitrary files via the upload audio component.



- [https://github.com/Orange-418/AgentDVR-5.1.6.0-File-Upload-and-Remote-Code-Execution](https://github.com/Orange-418/AgentDVR-5.1.6.0-File-Upload-and-Remote-Code-Execution) :  ![starts](https://img.shields.io/github/stars/Orange-418/AgentDVR-5.1.6.0-File-Upload-and-Remote-Code-Execution.svg) ![forks](https://img.shields.io/github/forks/Orange-418/AgentDVR-5.1.6.0-File-Upload-and-Remote-Code-Execution.svg)

- [https://github.com/Orange-418/CVE-2024-22515-File-Upload-Vulnerability](https://github.com/Orange-418/CVE-2024-22515-File-Upload-Vulnerability) :  ![starts](https://img.shields.io/github/stars/Orange-418/CVE-2024-22515-File-Upload-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/Orange-418/CVE-2024-22515-File-Upload-Vulnerability.svg)

## CVE-2024-22514
 An issue discovered in iSpyConnect.com Agent DVR 5.1.6.0 allows attackers to run arbitrary files by restoring a crafted backup file.



- [https://github.com/Orange-418/AgentDVR-5.1.6.0-File-Upload-and-Remote-Code-Execution](https://github.com/Orange-418/AgentDVR-5.1.6.0-File-Upload-and-Remote-Code-Execution) :  ![starts](https://img.shields.io/github/stars/Orange-418/AgentDVR-5.1.6.0-File-Upload-and-Remote-Code-Execution.svg) ![forks](https://img.shields.io/github/forks/Orange-418/AgentDVR-5.1.6.0-File-Upload-and-Remote-Code-Execution.svg)

- [https://github.com/Orange-418/CVE-2024-22514-Remote-Code-Execution](https://github.com/Orange-418/CVE-2024-22514-Remote-Code-Execution) :  ![starts](https://img.shields.io/github/stars/Orange-418/CVE-2024-22514-Remote-Code-Execution.svg) ![forks](https://img.shields.io/github/forks/Orange-418/CVE-2024-22514-Remote-Code-Execution.svg)

## CVE-2024-22513
 djangorestframework-simplejwt version 5.3.1 and before is vulnerable to information disclosure. A user can access web application resources even after their account has been disabled due to missing user validation checks via the for_user method.



- [https://github.com/dmdhrumilmistry/CVEs](https://github.com/dmdhrumilmistry/CVEs) :  ![starts](https://img.shields.io/github/stars/dmdhrumilmistry/CVEs.svg) ![forks](https://img.shields.io/github/forks/dmdhrumilmistry/CVEs.svg)

## CVE-2024-22416
 pyLoad is a free and open-source Download Manager written in pure Python. The `pyload` API allows any API call to be made using GET requests. Since the session cookie is not set to `SameSite: strict`, this opens the library up to severe attack possibilities via a Cross-Site Request Forgery (CSRF) attack. As a result any API call can be made via a CSRF attack by an unauthenticated user. This issue has been addressed in release `0.5.0b3.dev78`. All users are advised to upgrade.



- [https://github.com/mindstorm38/ensimag-secu3a-cve-2024-22416](https://github.com/mindstorm38/ensimag-secu3a-cve-2024-22416) :  ![starts](https://img.shields.io/github/stars/mindstorm38/ensimag-secu3a-cve-2024-22416.svg) ![forks](https://img.shields.io/github/forks/mindstorm38/ensimag-secu3a-cve-2024-22416.svg)

## CVE-2024-22411
 Avo is a framework to create admin panels for Ruby on Rails apps. In Avo 3 pre12, any HTML inside text that is passed to `error` or `succeed` in an `Avo::BaseAction` subclass will be rendered directly without sanitization in the toast/notification that appears in the UI on Action completion. A malicious user could exploit this vulnerability to trigger a cross site scripting attack on an unsuspecting user. This issue has been addressed in the 3.3.0 and 2.47.0 releases of Avo. Users are advised to upgrade.



- [https://github.com/tamaloa/avo-CVE-2024-22411](https://github.com/tamaloa/avo-CVE-2024-22411) :  ![starts](https://img.shields.io/github/stars/tamaloa/avo-CVE-2024-22411.svg) ![forks](https://img.shields.io/github/forks/tamaloa/avo-CVE-2024-22411.svg)

## CVE-2024-22393
 Unrestricted Upload of File with Dangerous Type vulnerability in Apache Answer.This issue affects Apache Answer: through 1.2.1.

Pixel Flood Attack by uploading large pixel files will cause server out of memory. A logged-in user can cause such an attack by uploading an image when posting content.
Users are recommended to upgrade to version [1.2.5], which fixes the issue.



- [https://github.com/omranisecurity/CVE-2024-22393](https://github.com/omranisecurity/CVE-2024-22393) :  ![starts](https://img.shields.io/github/stars/omranisecurity/CVE-2024-22393.svg) ![forks](https://img.shields.io/github/forks/omranisecurity/CVE-2024-22393.svg)

## CVE-2024-22369
 Deserialization of Untrusted Data vulnerability in Apache Camel SQL ComponentThis issue affects Apache Camel: from 3.0.0 before 3.21.4, from 3.22.0 before 3.22.1, from 4.0.0 before 4.0.4, from 4.1.0 before 4.4.0.

Users are recommended to upgrade to version 4.4.0, which fixes the issue. If users are on the 4.0.x LTS releases stream, then they are suggested to upgrade to 4.0.4. If users are on 3.x, they are suggested to move to 3.21.4 or 3.22.1





- [https://github.com/oscerd/CVE-2024-22369](https://github.com/oscerd/CVE-2024-22369) :  ![starts](https://img.shields.io/github/stars/oscerd/CVE-2024-22369.svg) ![forks](https://img.shields.io/github/forks/oscerd/CVE-2024-22369.svg)

## CVE-2024-22275
 The vCenter Server contains a partial file read vulnerability. A malicious actor with administrative privileges on the vCenter appliance shell may exploit this issue to partially read arbitrary files containing sensitive data.



- [https://github.com/mbadanoiu/CVE-2024-22275](https://github.com/mbadanoiu/CVE-2024-22275) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2024-22275.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2024-22275.svg)

## CVE-2024-22274
 The vCenter Server contains an authenticated remote code execution vulnerability. A malicious actor with administrative privileges on the vCenter appliance shell may exploit this issue to run arbitrary commands on the underlying operating system.



- [https://github.com/l0n3m4n/CVE-2024-22274-RCE](https://github.com/l0n3m4n/CVE-2024-22274-RCE) :  ![starts](https://img.shields.io/github/stars/l0n3m4n/CVE-2024-22274-RCE.svg) ![forks](https://img.shields.io/github/forks/l0n3m4n/CVE-2024-22274-RCE.svg)

- [https://github.com/mbadanoiu/CVE-2024-22274](https://github.com/mbadanoiu/CVE-2024-22274) :  ![starts](https://img.shields.io/github/stars/mbadanoiu/CVE-2024-22274.svg) ![forks](https://img.shields.io/github/forks/mbadanoiu/CVE-2024-22274.svg)

- [https://github.com/ninhpn1337/CVE-2024-22274](https://github.com/ninhpn1337/CVE-2024-22274) :  ![starts](https://img.shields.io/github/stars/ninhpn1337/CVE-2024-22274.svg) ![forks](https://img.shields.io/github/forks/ninhpn1337/CVE-2024-22274.svg)

- [https://github.com/Mustafa1986/CVE-2024-22274-RCE](https://github.com/Mustafa1986/CVE-2024-22274-RCE) :  ![starts](https://img.shields.io/github/stars/Mustafa1986/CVE-2024-22274-RCE.svg) ![forks](https://img.shields.io/github/forks/Mustafa1986/CVE-2024-22274-RCE.svg)

## CVE-2024-22262
 Applications that use UriComponentsBuilder to parse an externally provided URL (e.g. through a query parameter) AND perform validation checks on the host of the parsed URL may be vulnerable to a  open redirect https://cwe.mitre.org/data/definitions/601.html  attack or to a SSRF attack if the URL is used after passing validation checks.

This is the same as  CVE-2024-22259 https://spring.io/security/cve-2024-22259  and  CVE-2024-22243 https://spring.io/security/cve-2024-22243 , but with different input.



- [https://github.com/Performant-Labs/CVE-2024-22262](https://github.com/Performant-Labs/CVE-2024-22262) :  ![starts](https://img.shields.io/github/stars/Performant-Labs/CVE-2024-22262.svg) ![forks](https://img.shields.io/github/forks/Performant-Labs/CVE-2024-22262.svg)

## CVE-2024-22243
 Applications that use UriComponentsBuilder to parse an externally provided URL (e.g. through a query parameter) AND perform validation checks on the host of the parsed URL may be vulnerable to a  open redirect https://cwe.mitre.org/data/definitions/601.html  attack or to a SSRF attack if the URL is used after passing validation checks.



- [https://github.com/SeanPesce/CVE-2024-22243](https://github.com/SeanPesce/CVE-2024-22243) :  ![starts](https://img.shields.io/github/stars/SeanPesce/CVE-2024-22243.svg) ![forks](https://img.shields.io/github/forks/SeanPesce/CVE-2024-22243.svg)

- [https://github.com/shellfeel/CVE-2024-22243-CVE-2024-22234](https://github.com/shellfeel/CVE-2024-22243-CVE-2024-22234) :  ![starts](https://img.shields.io/github/stars/shellfeel/CVE-2024-22243-CVE-2024-22234.svg) ![forks](https://img.shields.io/github/forks/shellfeel/CVE-2024-22243-CVE-2024-22234.svg)

## CVE-2024-22234
 In Spring Security, versions 6.1.x prior to 6.1.7 and versions 6.2.x prior to 6.2.2, an application is vulnerable to broken access control when it directly uses the AuthenticationTrustResolver.isFullyAuthenticated(Authentication) method.

Specifically, an application is vulnerable if:

  *  The application uses AuthenticationTrustResolver.isFullyAuthenticated(Authentication) directly and a null authentication parameter is passed to it resulting in an erroneous true return value.


An application is not vulnerable if any of the following is true:

  *  The application does not use AuthenticationTrustResolver.isFullyAuthenticated(Authentication) directly.
  *  The application does not pass null to AuthenticationTrustResolver.isFullyAuthenticated
  *  The application only uses isFullyAuthenticated via  Method Security https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html  or  HTTP Request Security https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html



- [https://github.com/shellfeel/CVE-2024-22243-CVE-2024-22234](https://github.com/shellfeel/CVE-2024-22243-CVE-2024-22234) :  ![starts](https://img.shields.io/github/stars/shellfeel/CVE-2024-22243-CVE-2024-22234.svg) ![forks](https://img.shields.io/github/forks/shellfeel/CVE-2024-22243-CVE-2024-22234.svg)

## CVE-2024-22198
 Nginx-UI is a web interface to manage Nginx configurations. It is vulnerable to arbitrary command execution by abusing the configuration settings. The `Home  Preference` page exposes a list of system settings such as `Run Mode`, `Jwt Secret`, `Node Secret` and `Terminal Start Command`. While the UI doesn't allow users to modify the `Terminal Start Command` setting, it is possible to do so by sending a request to the API. This issue may lead to authenticated remote code execution, privilege escalation, and information disclosure. This vulnerability has been patched in version 2.0.0.beta.9.



- [https://github.com/xiw1ll/CVE-2024-22198_Checker](https://github.com/xiw1ll/CVE-2024-22198_Checker) :  ![starts](https://img.shields.io/github/stars/xiw1ll/CVE-2024-22198_Checker.svg) ![forks](https://img.shields.io/github/forks/xiw1ll/CVE-2024-22198_Checker.svg)

## CVE-2024-22145
 Improper Privilege Management vulnerability in InstaWP Team InstaWP Connect allows Privilege Escalation.This issue affects InstaWP Connect: from n/a through 0.1.0.8.



- [https://github.com/RandomRobbieBF/CVE-2024-22145](https://github.com/RandomRobbieBF/CVE-2024-22145) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-22145.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-22145.svg)

## CVE-2024-22120
 Zabbix server can perform command execution for configured scripts. After command is executed, audit entry is added to "Audit Log". Due to "clientip" field is not sanitized, it is possible to injection SQL into "clientip" and exploit time based blind SQL injection.



- [https://github.com/W01fh4cker/CVE-2024-22120-RCE](https://github.com/W01fh4cker/CVE-2024-22120-RCE) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/CVE-2024-22120-RCE.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/CVE-2024-22120-RCE.svg)

- [https://github.com/isPique/CVE-2024-22120-RCE-with-gopher](https://github.com/isPique/CVE-2024-22120-RCE-with-gopher) :  ![starts](https://img.shields.io/github/stars/isPique/CVE-2024-22120-RCE-with-gopher.svg) ![forks](https://img.shields.io/github/forks/isPique/CVE-2024-22120-RCE-with-gopher.svg)

## CVE-2024-22026
 A local privilege escalation vulnerability in EPMM before 12.1.0.0 allows an authenticated local user to bypass shell restriction and execute arbitrary commands on the appliance.



- [https://github.com/securekomodo/CVE-2024-22026](https://github.com/securekomodo/CVE-2024-22026) :  ![starts](https://img.shields.io/github/stars/securekomodo/CVE-2024-22026.svg) ![forks](https://img.shields.io/github/forks/securekomodo/CVE-2024-22026.svg)

## CVE-2024-22024
 An XML external entity or XXE vulnerability in the SAML component of Ivanti Connect Secure (9.x, 22.x), Ivanti Policy Secure (9.x, 22.x) and ZTA gateways which allows an attacker to access certain restricted resources without authentication.



- [https://github.com/0dteam/CVE-2024-22024](https://github.com/0dteam/CVE-2024-22024) :  ![starts](https://img.shields.io/github/stars/0dteam/CVE-2024-22024.svg) ![forks](https://img.shields.io/github/forks/0dteam/CVE-2024-22024.svg)

## CVE-2024-22017
 setuid() does not affect libuv's internal io_uring operations if initialized before the call to setuid().
This allows the process to perform privileged operations despite presumably having dropped such privileges through a call to setuid().
This vulnerability affects all users using version greater or equal than Node.js 18.18.0, Node.js 20.4.0 and Node.js 21.



- [https://github.com/SpiralBL0CK/cve-2024-22017_to_test](https://github.com/SpiralBL0CK/cve-2024-22017_to_test) :  ![starts](https://img.shields.io/github/stars/SpiralBL0CK/cve-2024-22017_to_test.svg) ![forks](https://img.shields.io/github/forks/SpiralBL0CK/cve-2024-22017_to_test.svg)

## CVE-2024-22002
 CORSAIR iCUE 5.9.105 with iCUE Murals on Windows allows unprivileged users to insert DLL files in the cuepkg-1.2.6 subdirectory of the installation directory.



- [https://github.com/0xkickit/iCUE_DllHijack_LPE-CVE-2024-22002](https://github.com/0xkickit/iCUE_DllHijack_LPE-CVE-2024-22002) :  ![starts](https://img.shields.io/github/stars/0xkickit/iCUE_DllHijack_LPE-CVE-2024-22002.svg) ![forks](https://img.shields.io/github/forks/0xkickit/iCUE_DllHijack_LPE-CVE-2024-22002.svg)

## CVE-2024-21980
 Improper restriction of write operations in SNP firmware could allow a malicious hypervisor to potentially overwrite a guest's memory or UMC seed resulting in loss of confidentiality and integrity.



- [https://github.com/Freax13/cve-2024-21980-poc](https://github.com/Freax13/cve-2024-21980-poc) :  ![starts](https://img.shields.io/github/stars/Freax13/cve-2024-21980-poc.svg) ![forks](https://img.shields.io/github/forks/Freax13/cve-2024-21980-poc.svg)

## CVE-2024-21978
 Improper input validation in SEV-SNP could allow a malicious hypervisor to read or overwrite guest memory potentially leading to data leakage or data corruption.



- [https://github.com/Freax13/cve-2024-21978-poc](https://github.com/Freax13/cve-2024-21978-poc) :  ![starts](https://img.shields.io/github/stars/Freax13/cve-2024-21978-poc.svg) ![forks](https://img.shields.io/github/forks/Freax13/cve-2024-21978-poc.svg)

## CVE-2024-21893
 A server-side request forgery vulnerability in the SAML component of Ivanti Connect Secure (9.x, 22.x) and Ivanti Policy Secure (9.x, 22.x) and Ivanti Neurons for ZTA allows an attacker to access certain restricted resources without authentication.



- [https://github.com/gobysec/Goby](https://github.com/gobysec/Goby) :  ![starts](https://img.shields.io/github/stars/gobysec/Goby.svg) ![forks](https://img.shields.io/github/forks/gobysec/Goby.svg)

- [https://github.com/gobysec/GobyVuls](https://github.com/gobysec/GobyVuls) :  ![starts](https://img.shields.io/github/stars/gobysec/GobyVuls.svg) ![forks](https://img.shields.io/github/forks/gobysec/GobyVuls.svg)

- [https://github.com/h4x0r-dz/CVE-2024-21893.py](https://github.com/h4x0r-dz/CVE-2024-21893.py) :  ![starts](https://img.shields.io/github/stars/h4x0r-dz/CVE-2024-21893.py.svg) ![forks](https://img.shields.io/github/forks/h4x0r-dz/CVE-2024-21893.py.svg)

- [https://github.com/Chocapikk/CVE-2024-21893-to-CVE-2024-21887](https://github.com/Chocapikk/CVE-2024-21893-to-CVE-2024-21887) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-21893-to-CVE-2024-21887.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-21893-to-CVE-2024-21887.svg)

## CVE-2024-21887
 A command injection vulnerability in web components of Ivanti Connect Secure (9.x, 22.x) and Ivanti Policy Secure (9.x, 22.x)  allows an authenticated administrator to send specially crafted requests and execute arbitrary commands on the appliance.



- [https://github.com/gobysec/Goby](https://github.com/gobysec/Goby) :  ![starts](https://img.shields.io/github/stars/gobysec/Goby.svg) ![forks](https://img.shields.io/github/forks/gobysec/Goby.svg)

- [https://github.com/gobysec/GobyVuls](https://github.com/gobysec/GobyVuls) :  ![starts](https://img.shields.io/github/stars/gobysec/GobyVuls.svg) ![forks](https://img.shields.io/github/forks/gobysec/GobyVuls.svg)

- [https://github.com/Chocapikk/CVE-2024-21887](https://github.com/Chocapikk/CVE-2024-21887) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-21887.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-21887.svg)

- [https://github.com/Chocapikk/CVE-2024-21893-to-CVE-2024-21887](https://github.com/Chocapikk/CVE-2024-21893-to-CVE-2024-21887) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-21893-to-CVE-2024-21887.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-21893-to-CVE-2024-21887.svg)

- [https://github.com/duy-31/CVE-2023-46805_CVE-2024-21887](https://github.com/duy-31/CVE-2023-46805_CVE-2024-21887) :  ![starts](https://img.shields.io/github/stars/duy-31/CVE-2023-46805_CVE-2024-21887.svg) ![forks](https://img.shields.io/github/forks/duy-31/CVE-2023-46805_CVE-2024-21887.svg)

- [https://github.com/seajaysec/Ivanti-Connect-Around-Scan](https://github.com/seajaysec/Ivanti-Connect-Around-Scan) :  ![starts](https://img.shields.io/github/stars/seajaysec/Ivanti-Connect-Around-Scan.svg) ![forks](https://img.shields.io/github/forks/seajaysec/Ivanti-Connect-Around-Scan.svg)

- [https://github.com/yoryio/CVE-2023-46805](https://github.com/yoryio/CVE-2023-46805) :  ![starts](https://img.shields.io/github/stars/yoryio/CVE-2023-46805.svg) ![forks](https://img.shields.io/github/forks/yoryio/CVE-2023-46805.svg)

- [https://github.com/oways/ivanti-CVE-2024-21887](https://github.com/oways/ivanti-CVE-2024-21887) :  ![starts](https://img.shields.io/github/stars/oways/ivanti-CVE-2024-21887.svg) ![forks](https://img.shields.io/github/forks/oways/ivanti-CVE-2024-21887.svg)

- [https://github.com/raminkarimkhani1996/CVE-2023-46805_CVE-2024-21887](https://github.com/raminkarimkhani1996/CVE-2023-46805_CVE-2024-21887) :  ![starts](https://img.shields.io/github/stars/raminkarimkhani1996/CVE-2023-46805_CVE-2024-21887.svg) ![forks](https://img.shields.io/github/forks/raminkarimkhani1996/CVE-2023-46805_CVE-2024-21887.svg)

- [https://github.com/tucommenceapousser/CVE-2024-21887](https://github.com/tucommenceapousser/CVE-2024-21887) :  ![starts](https://img.shields.io/github/stars/tucommenceapousser/CVE-2024-21887.svg) ![forks](https://img.shields.io/github/forks/tucommenceapousser/CVE-2024-21887.svg)

- [https://github.com/rxwx/pulse-meter](https://github.com/rxwx/pulse-meter) :  ![starts](https://img.shields.io/github/stars/rxwx/pulse-meter.svg) ![forks](https://img.shields.io/github/forks/rxwx/pulse-meter.svg)

- [https://github.com/mickdec/CVE-2023-46805_CVE-2024-21887_scan_grouped](https://github.com/mickdec/CVE-2023-46805_CVE-2024-21887_scan_grouped) :  ![starts](https://img.shields.io/github/stars/mickdec/CVE-2023-46805_CVE-2024-21887_scan_grouped.svg) ![forks](https://img.shields.io/github/forks/mickdec/CVE-2023-46805_CVE-2024-21887_scan_grouped.svg)

## CVE-2024-21793
 
An OData injection vulnerability exists in the BIG-IP Next Central Manager API (URI).  Note: Software versions which have reached End of Technical Support (EoTS) are not evaluated.



- [https://github.com/FeatherStark/CVE-2024-21793](https://github.com/FeatherStark/CVE-2024-21793) :  ![starts](https://img.shields.io/github/stars/FeatherStark/CVE-2024-21793.svg) ![forks](https://img.shields.io/github/forks/FeatherStark/CVE-2024-21793.svg)

## CVE-2024-21762
 A out-of-bounds write in Fortinet FortiOS versions 7.4.0 through 7.4.2, 7.2.0 through 7.2.6, 7.0.0 through 7.0.13, 6.4.0 through 6.4.14, 6.2.0 through 6.2.15, 6.0.0 through 6.0.17, FortiProxy versions 7.4.0 through 7.4.2, 7.2.0 through 7.2.8, 7.0.0 through 7.0.14, 2.0.0 through 2.0.13, 1.2.0 through 1.2.13, 1.1.0 through 1.1.6, 1.0.0 through 1.0.7 allows attacker to execute unauthorized code or commands via specifically crafted requests



- [https://github.com/h4x0r-dz/CVE-2024-21762](https://github.com/h4x0r-dz/CVE-2024-21762) :  ![starts](https://img.shields.io/github/stars/h4x0r-dz/CVE-2024-21762.svg) ![forks](https://img.shields.io/github/forks/h4x0r-dz/CVE-2024-21762.svg)

- [https://github.com/BishopFox/cve-2024-21762-check](https://github.com/BishopFox/cve-2024-21762-check) :  ![starts](https://img.shields.io/github/stars/BishopFox/cve-2024-21762-check.svg) ![forks](https://img.shields.io/github/forks/BishopFox/cve-2024-21762-check.svg)

- [https://github.com/cleverg0d/CVE-2024-21762-Checker](https://github.com/cleverg0d/CVE-2024-21762-Checker) :  ![starts](https://img.shields.io/github/stars/cleverg0d/CVE-2024-21762-Checker.svg) ![forks](https://img.shields.io/github/forks/cleverg0d/CVE-2024-21762-Checker.svg)

- [https://github.com/r4p3c4/CVE-2024-21762-Exploit-PoC-Fortinet-SSL-VPN-Check](https://github.com/r4p3c4/CVE-2024-21762-Exploit-PoC-Fortinet-SSL-VPN-Check) :  ![starts](https://img.shields.io/github/stars/r4p3c4/CVE-2024-21762-Exploit-PoC-Fortinet-SSL-VPN-Check.svg) ![forks](https://img.shields.io/github/forks/r4p3c4/CVE-2024-21762-Exploit-PoC-Fortinet-SSL-VPN-Check.svg)

- [https://github.com/d0rb/CVE-2024-21762](https://github.com/d0rb/CVE-2024-21762) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2024-21762.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2024-21762.svg)

- [https://github.com/XiaomingX/cve-2024-21762-poc](https://github.com/XiaomingX/cve-2024-21762-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-21762-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-21762-poc.svg)

- [https://github.com/rdoix/cve-2024-21762-checker](https://github.com/rdoix/cve-2024-21762-checker) :  ![starts](https://img.shields.io/github/stars/rdoix/cve-2024-21762-checker.svg) ![forks](https://img.shields.io/github/forks/rdoix/cve-2024-21762-checker.svg)

- [https://github.com/bsekercioglu/cve2024-21762-ShodanChecker](https://github.com/bsekercioglu/cve2024-21762-ShodanChecker) :  ![starts](https://img.shields.io/github/stars/bsekercioglu/cve2024-21762-ShodanChecker.svg) ![forks](https://img.shields.io/github/forks/bsekercioglu/cve2024-21762-ShodanChecker.svg)

- [https://github.com/abrewer251/CVE-2024-21762_FortiNet_PoC](https://github.com/abrewer251/CVE-2024-21762_FortiNet_PoC) :  ![starts](https://img.shields.io/github/stars/abrewer251/CVE-2024-21762_FortiNet_PoC.svg) ![forks](https://img.shields.io/github/forks/abrewer251/CVE-2024-21762_FortiNet_PoC.svg)

## CVE-2024-21754
 A use of password hash with insufficient computational effort vulnerability [CWE-916] affecting FortiOS version 7.4.3 and below, 7.2 all versions, 7.0 all versions, 6.4 all versions and FortiProxy version 7.4.2 and below, 7.2 all versions, 7.0 all versions, 2.0 all versions may allow a privileged attacker with super-admin profile and CLI access to decrypting the backup file.



- [https://github.com/CyberSecuritist/CVE-2024-21754-Forti-RCE](https://github.com/CyberSecuritist/CVE-2024-21754-Forti-RCE) :  ![starts](https://img.shields.io/github/stars/CyberSecuritist/CVE-2024-21754-Forti-RCE.svg) ![forks](https://img.shields.io/github/forks/CyberSecuritist/CVE-2024-21754-Forti-RCE.svg)

## CVE-2024-21683
 This High severity RCE (Remote Code Execution) vulnerability was introduced in version 5.2 of Confluence Data Center and Server.

This RCE (Remote Code Execution) vulnerability, with a CVSS Score of 7.2, allows an authenticated attacker to execute arbitrary code which has high impact to confidentiality, high impact to integrity, high impact to availability, and requires no user interaction. 

Atlassian recommends that Confluence Data Center and Server customers upgrade to latest version. If you are unable to do so, upgrade your instance to one of the specified supported fixed versions. See the release notes https://confluence.atlassian.com/doc/confluence-release-notes-327.html

You can download the latest version of Confluence Data Center and Server from the download center https://www.atlassian.com/software/confluence/download-archives.

This vulnerability was found internally.



- [https://github.com/W01fh4cker/CVE-2024-21683-RCE](https://github.com/W01fh4cker/CVE-2024-21683-RCE) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/CVE-2024-21683-RCE.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/CVE-2024-21683-RCE.svg)

- [https://github.com/absholi7ly/-CVE-2024-21683-RCE-in-Confluence-Data-Center-and-Server](https://github.com/absholi7ly/-CVE-2024-21683-RCE-in-Confluence-Data-Center-and-Server) :  ![starts](https://img.shields.io/github/stars/absholi7ly/-CVE-2024-21683-RCE-in-Confluence-Data-Center-and-Server.svg) ![forks](https://img.shields.io/github/forks/absholi7ly/-CVE-2024-21683-RCE-in-Confluence-Data-Center-and-Server.svg)

- [https://github.com/XiaomingX/cve-2024-21683-rce](https://github.com/XiaomingX/cve-2024-21683-rce) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-21683-rce.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-21683-rce.svg)

- [https://github.com/r00t7oo2jm/-CVE-2024-21683-RCE-in-Confluence-Data-Center-and-Server](https://github.com/r00t7oo2jm/-CVE-2024-21683-RCE-in-Confluence-Data-Center-and-Server) :  ![starts](https://img.shields.io/github/stars/r00t7oo2jm/-CVE-2024-21683-RCE-in-Confluence-Data-Center-and-Server.svg) ![forks](https://img.shields.io/github/forks/r00t7oo2jm/-CVE-2024-21683-RCE-in-Confluence-Data-Center-and-Server.svg)

- [https://github.com/phucrio/CVE-2024-21683-RCE](https://github.com/phucrio/CVE-2024-21683-RCE) :  ![starts](https://img.shields.io/github/stars/phucrio/CVE-2024-21683-RCE.svg) ![forks](https://img.shields.io/github/forks/phucrio/CVE-2024-21683-RCE.svg)

- [https://github.com/xh4vm/CVE-2024-21683](https://github.com/xh4vm/CVE-2024-21683) :  ![starts](https://img.shields.io/github/stars/xh4vm/CVE-2024-21683.svg) ![forks](https://img.shields.io/github/forks/xh4vm/CVE-2024-21683.svg)

## CVE-2024-21644
 pyLoad is the free and open-source Download Manager written in pure Python. Any unauthenticated user can browse to a specific URL to expose the Flask config, including the `SECRET_KEY` variable. This issue has been patched in version 0.5.0b3.dev77.



- [https://github.com/ltranquility/CVE-2024-21644-Poc](https://github.com/ltranquility/CVE-2024-21644-Poc) :  ![starts](https://img.shields.io/github/stars/ltranquility/CVE-2024-21644-Poc.svg) ![forks](https://img.shields.io/github/forks/ltranquility/CVE-2024-21644-Poc.svg)

## CVE-2024-21633
 Apktool is a tool for reverse engineering Android APK files. In versions 2.9.1 and prior, Apktool infers resource files' output path according to their resource names which can be manipulated by attacker to place files at desired location on the system Apktool runs on. Affected environments are those in which an attacker may write/overwrite any file that user has write access, and either user name is known or cwd is under user folder. Commit d348c43b24a9de350ff6e5bd610545a10c1fc712 contains a patch for this issue.



- [https://github.com/0x33c0unt/CVE-2024-21633](https://github.com/0x33c0unt/CVE-2024-21633) :  ![starts](https://img.shields.io/github/stars/0x33c0unt/CVE-2024-21633.svg) ![forks](https://img.shields.io/github/forks/0x33c0unt/CVE-2024-21633.svg)

## CVE-2024-21626
 runc is a CLI tool for spawning and running containers on Linux according to the OCI specification. In runc 1.1.11 and earlier, due to an internal file descriptor leak, an attacker could cause a newly-spawned container process (from runc exec) to have a working directory in the host filesystem namespace, allowing for a container escape by giving access to the host filesystem ("attack 2"). The same attack could be used by a malicious image to allow a container process to gain access to the host filesystem through runc run ("attack 1"). Variants of attacks 1 and 2 could be also be used to overwrite semi-arbitrary host binaries, allowing for complete container escapes ("attack 3a" and "attack 3b"). runc 1.1.12 includes patches for this issue.



- [https://github.com/NitroCao/CVE-2024-21626](https://github.com/NitroCao/CVE-2024-21626) :  ![starts](https://img.shields.io/github/stars/NitroCao/CVE-2024-21626.svg) ![forks](https://img.shields.io/github/forks/NitroCao/CVE-2024-21626.svg)

- [https://github.com/Wall1e/CVE-2024-21626-POC](https://github.com/Wall1e/CVE-2024-21626-POC) :  ![starts](https://img.shields.io/github/stars/Wall1e/CVE-2024-21626-POC.svg) ![forks](https://img.shields.io/github/forks/Wall1e/CVE-2024-21626-POC.svg)

- [https://github.com/V0WKeep3r/CVE-2024-21626-runcPOC](https://github.com/V0WKeep3r/CVE-2024-21626-runcPOC) :  ![starts](https://img.shields.io/github/stars/V0WKeep3r/CVE-2024-21626-runcPOC.svg) ![forks](https://img.shields.io/github/forks/V0WKeep3r/CVE-2024-21626-runcPOC.svg)

- [https://github.com/cdxiaodong/CVE-2024-21626](https://github.com/cdxiaodong/CVE-2024-21626) :  ![starts](https://img.shields.io/github/stars/cdxiaodong/CVE-2024-21626.svg) ![forks](https://img.shields.io/github/forks/cdxiaodong/CVE-2024-21626.svg)

- [https://github.com/zhangguanzhang/CVE-2024-21626](https://github.com/zhangguanzhang/CVE-2024-21626) :  ![starts](https://img.shields.io/github/stars/zhangguanzhang/CVE-2024-21626.svg) ![forks](https://img.shields.io/github/forks/zhangguanzhang/CVE-2024-21626.svg)

- [https://github.com/laysakura/CVE-2024-21626-demo](https://github.com/laysakura/CVE-2024-21626-demo) :  ![starts](https://img.shields.io/github/stars/laysakura/CVE-2024-21626-demo.svg) ![forks](https://img.shields.io/github/forks/laysakura/CVE-2024-21626-demo.svg)

- [https://github.com/dorser/cve-2024-21626](https://github.com/dorser/cve-2024-21626) :  ![starts](https://img.shields.io/github/stars/dorser/cve-2024-21626.svg) ![forks](https://img.shields.io/github/forks/dorser/cve-2024-21626.svg)

- [https://github.com/KubernetesBachelor/CVE-2024-21626](https://github.com/KubernetesBachelor/CVE-2024-21626) :  ![starts](https://img.shields.io/github/stars/KubernetesBachelor/CVE-2024-21626.svg) ![forks](https://img.shields.io/github/forks/KubernetesBachelor/CVE-2024-21626.svg)

- [https://github.com/Sk3pper/CVE-2024-21626](https://github.com/Sk3pper/CVE-2024-21626) :  ![starts](https://img.shields.io/github/stars/Sk3pper/CVE-2024-21626.svg) ![forks](https://img.shields.io/github/forks/Sk3pper/CVE-2024-21626.svg)

- [https://github.com/zpxlz/CVE-2024-21626-POC](https://github.com/zpxlz/CVE-2024-21626-POC) :  ![starts](https://img.shields.io/github/stars/zpxlz/CVE-2024-21626-POC.svg) ![forks](https://img.shields.io/github/forks/zpxlz/CVE-2024-21626-POC.svg)

- [https://github.com/abian2/CVE-2024-21626](https://github.com/abian2/CVE-2024-21626) :  ![starts](https://img.shields.io/github/stars/abian2/CVE-2024-21626.svg) ![forks](https://img.shields.io/github/forks/abian2/CVE-2024-21626.svg)

- [https://github.com/R4mbb/CVE-2024-21626-PoC](https://github.com/R4mbb/CVE-2024-21626-PoC) :  ![starts](https://img.shields.io/github/stars/R4mbb/CVE-2024-21626-PoC.svg) ![forks](https://img.shields.io/github/forks/R4mbb/CVE-2024-21626-PoC.svg)

- [https://github.com/Sk3pper/CVE-2024-21626-old-docker-versions](https://github.com/Sk3pper/CVE-2024-21626-old-docker-versions) :  ![starts](https://img.shields.io/github/stars/Sk3pper/CVE-2024-21626-old-docker-versions.svg) ![forks](https://img.shields.io/github/forks/Sk3pper/CVE-2024-21626-old-docker-versions.svg)

- [https://github.com/adaammmeeee/little-joke](https://github.com/adaammmeeee/little-joke) :  ![starts](https://img.shields.io/github/stars/adaammmeeee/little-joke.svg) ![forks](https://img.shields.io/github/forks/adaammmeeee/little-joke.svg)

## CVE-2024-21546
 Versions of the package unisharp/laravel-filemanager before 2.9.1 are vulnerable to Remote Code Execution (RCE) through using a valid mimetype and inserting the . character after the php file extension. This allows the attacker to execute malicious code.



- [https://github.com/ajdumanhug/CVE-2024-21546](https://github.com/ajdumanhug/CVE-2024-21546) :  ![starts](https://img.shields.io/github/stars/ajdumanhug/CVE-2024-21546.svg) ![forks](https://img.shields.io/github/forks/ajdumanhug/CVE-2024-21546.svg)

## CVE-2024-21542
 Versions of the package luigi before 3.6.0 are vulnerable to Arbitrary File Write via Archive Extraction (Zip Slip) due to improper destination file path validation in the _extract_packages_archive function.



- [https://github.com/L3ster1337/Poc-CVE-2024-21542](https://github.com/L3ster1337/Poc-CVE-2024-21542) :  ![starts](https://img.shields.io/github/stars/L3ster1337/Poc-CVE-2024-21542.svg) ![forks](https://img.shields.io/github/forks/L3ster1337/Poc-CVE-2024-21542.svg)

## CVE-2024-21534
 All versions of the package jsonpath-plus are vulnerable to Remote Code Execution (RCE) due to improper input sanitization. An attacker can execute aribitrary code on the system by exploiting the unsafe default usage of vm in Node.**Note:**There were several attempts to fix it in versions [10.0.0-10.1.0](https://github.com/JSONPath-Plus/JSONPath/compare/v9.0.0...v10.1.0) but it could still be exploited using [different payloads](https://github.com/JSONPath-Plus/JSONPath/issues/226).



- [https://github.com/XiaomingX/cve-2024-21534-poc](https://github.com/XiaomingX/cve-2024-21534-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-21534-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-21534-poc.svg)

- [https://github.com/verylazytech/cve-2024-21534](https://github.com/verylazytech/cve-2024-21534) :  ![starts](https://img.shields.io/github/stars/verylazytech/cve-2024-21534.svg) ![forks](https://img.shields.io/github/forks/verylazytech/cve-2024-21534.svg)

- [https://github.com/pabloopez/CVE-2024-21534](https://github.com/pabloopez/CVE-2024-21534) :  ![starts](https://img.shields.io/github/stars/pabloopez/CVE-2024-21534.svg) ![forks](https://img.shields.io/github/forks/pabloopez/CVE-2024-21534.svg)

## CVE-2024-21533
 All versions of the package ggit are vulnerable to Arbitrary Argument Injection via the clone() API, which allows specifying the remote URL to clone and the file on disk to clone to. The library does not sanitize for user input or validate a given URL scheme, nor does it properly pass command-line flags to the git binary using the double-dash POSIX characters (--) to communicate the end of options.



- [https://github.com/lirantal/CVE-2024-21533-PoC-ggit](https://github.com/lirantal/CVE-2024-21533-PoC-ggit) :  ![starts](https://img.shields.io/github/stars/lirantal/CVE-2024-21533-PoC-ggit.svg) ![forks](https://img.shields.io/github/forks/lirantal/CVE-2024-21533-PoC-ggit.svg)

## CVE-2024-21532
 All versions of the package ggit are vulnerable to Command Injection via the fetchTags(branch) API, which allows user input to specify the branch to be fetched and then concatenates this string along with a git command which is then passed to the unsafe exec() Node.js child process API.



- [https://github.com/lirantal/CVE-2024-21532-PoC-ggit](https://github.com/lirantal/CVE-2024-21532-PoC-ggit) :  ![starts](https://img.shields.io/github/stars/lirantal/CVE-2024-21532-PoC-ggit.svg) ![forks](https://img.shields.io/github/forks/lirantal/CVE-2024-21532-PoC-ggit.svg)

## CVE-2024-21520
 Versions of the package djangorestframework before 3.15.2 are vulnerable to Cross-site Scripting (XSS) via the break_long_headers template filter due to improper input sanitization before splitting and joining with br tags.



- [https://github.com/ch4n3-yoon/CVE-2024-21520-Demo](https://github.com/ch4n3-yoon/CVE-2024-21520-Demo) :  ![starts](https://img.shields.io/github/stars/ch4n3-yoon/CVE-2024-21520-Demo.svg) ![forks](https://img.shields.io/github/forks/ch4n3-yoon/CVE-2024-21520-Demo.svg)

## CVE-2024-21514
 This affects versions of the package opencart/opencart from 0.0.0. An SQL Injection issue was identified in the Divido payment extension for OpenCart, which is included by default in version 3.0.3.9. As an anonymous unauthenticated user, if the Divido payment module is installed (it does not have to be enabled), it is possible to exploit SQL injection to gain unauthorised access to the backend database. For any site which is vulnerable, any unauthenticated user could exploit this to dump the entire OpenCart database, including customer PII data.



- [https://github.com/bigb0x/CVE-2024-21514](https://github.com/bigb0x/CVE-2024-21514) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-21514.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-21514.svg)

## CVE-2024-21513
 Versions of the package langchain-experimental from 0.0.15 and before 0.0.21 are vulnerable to Arbitrary Code Execution when retrieving values from the database, the code will attempt to call 'eval' on all values. An attacker can exploit this vulnerability and execute arbitrary python code if they can control the input prompt and the server is configured with VectorSQLDatabaseChain.**Notes:**Impact on the Confidentiality, Integrity and Availability of the vulnerable component:Confidentiality: Code execution happens within the impacted component, in this case langchain-experimental, so all resources are necessarily accessible.Integrity: There is nothing protected by the impacted component inherently. Although anything returned from the component counts as 'information' for which the trustworthiness can be compromised.Availability: The loss of availability isn't caused by the attack itself, but it happens as a result during the attacker's post-exploitation steps.Impact on the Confidentiality, Integrity and Availability of the subsequent system:As a legitimate low-privileged user of the package (PR:L) the attacker does not have more access to data owned by the package as a result of this vulnerability than they did with normal usage (e.g. can query the DB). The unintended action that one can perform by breaking out of the app environment and exfiltrating files, making remote connections etc. happens during the post exploitation phase in the subsequent system - in this case, the OS.AT:P: An attacker needs to be able to influence the input prompt, whilst the server is configured with the VectorSQLDatabaseChain plugin.



- [https://github.com/nskath/CVE-2024-21513](https://github.com/nskath/CVE-2024-21513) :  ![starts](https://img.shields.io/github/stars/nskath/CVE-2024-21513.svg) ![forks](https://img.shields.io/github/forks/nskath/CVE-2024-21513.svg)

## CVE-2024-21413
 Microsoft Outlook Remote Code Execution Vulnerability



- [https://github.com/xaitax/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability](https://github.com/xaitax/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability) :  ![starts](https://img.shields.io/github/stars/xaitax/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/xaitax/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability.svg)

- [https://github.com/duy-31/CVE-2024-21413](https://github.com/duy-31/CVE-2024-21413) :  ![starts](https://img.shields.io/github/stars/duy-31/CVE-2024-21413.svg) ![forks](https://img.shields.io/github/forks/duy-31/CVE-2024-21413.svg)

- [https://github.com/CMNatic/CVE-2024-21413](https://github.com/CMNatic/CVE-2024-21413) :  ![starts](https://img.shields.io/github/stars/CMNatic/CVE-2024-21413.svg) ![forks](https://img.shields.io/github/forks/CMNatic/CVE-2024-21413.svg)

- [https://github.com/r00tb1t/CVE-2024-21413-POC](https://github.com/r00tb1t/CVE-2024-21413-POC) :  ![starts](https://img.shields.io/github/stars/r00tb1t/CVE-2024-21413-POC.svg) ![forks](https://img.shields.io/github/forks/r00tb1t/CVE-2024-21413-POC.svg)

- [https://github.com/Mdusmandasthaheer/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability](https://github.com/Mdusmandasthaheer/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability) :  ![starts](https://img.shields.io/github/stars/Mdusmandasthaheer/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/Mdusmandasthaheer/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability.svg)

- [https://github.com/ahmetkarakayaoffical/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability](https://github.com/ahmetkarakayaoffical/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability) :  ![starts](https://img.shields.io/github/stars/ahmetkarakayaoffical/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/ahmetkarakayaoffical/CVE-2024-21413-Microsoft-Outlook-Remote-Code-Execution-Vulnerability.svg)

- [https://github.com/dshabani96/CVE-2024-21413](https://github.com/dshabani96/CVE-2024-21413) :  ![starts](https://img.shields.io/github/stars/dshabani96/CVE-2024-21413.svg) ![forks](https://img.shields.io/github/forks/dshabani96/CVE-2024-21413.svg)

- [https://github.com/X-Projetion/CVE-2024-21413-Microsoft-Outlook-RCE-Exploit](https://github.com/X-Projetion/CVE-2024-21413-Microsoft-Outlook-RCE-Exploit) :  ![starts](https://img.shields.io/github/stars/X-Projetion/CVE-2024-21413-Microsoft-Outlook-RCE-Exploit.svg) ![forks](https://img.shields.io/github/forks/X-Projetion/CVE-2024-21413-Microsoft-Outlook-RCE-Exploit.svg)

- [https://github.com/D1se0/CVE-2024-21413-Vulnerabilidad-Outlook-LAB](https://github.com/D1se0/CVE-2024-21413-Vulnerabilidad-Outlook-LAB) :  ![starts](https://img.shields.io/github/stars/D1se0/CVE-2024-21413-Vulnerabilidad-Outlook-LAB.svg) ![forks](https://img.shields.io/github/forks/D1se0/CVE-2024-21413-Vulnerabilidad-Outlook-LAB.svg)

- [https://github.com/PolarisXSec/CVE-2024-21413](https://github.com/PolarisXSec/CVE-2024-21413) :  ![starts](https://img.shields.io/github/stars/PolarisXSec/CVE-2024-21413.svg) ![forks](https://img.shields.io/github/forks/PolarisXSec/CVE-2024-21413.svg)

- [https://github.com/olebris/CVE-2024-21413](https://github.com/olebris/CVE-2024-21413) :  ![starts](https://img.shields.io/github/stars/olebris/CVE-2024-21413.svg) ![forks](https://img.shields.io/github/forks/olebris/CVE-2024-21413.svg)

- [https://github.com/th3Hellion/CVE-2024-21413](https://github.com/th3Hellion/CVE-2024-21413) :  ![starts](https://img.shields.io/github/stars/th3Hellion/CVE-2024-21413.svg) ![forks](https://img.shields.io/github/forks/th3Hellion/CVE-2024-21413.svg)

- [https://github.com/MSeymenD/CVE-2024-21413](https://github.com/MSeymenD/CVE-2024-21413) :  ![starts](https://img.shields.io/github/stars/MSeymenD/CVE-2024-21413.svg) ![forks](https://img.shields.io/github/forks/MSeymenD/CVE-2024-21413.svg)

- [https://github.com/ShubhamKanhere307/CVE-2024-21413](https://github.com/ShubhamKanhere307/CVE-2024-21413) :  ![starts](https://img.shields.io/github/stars/ShubhamKanhere307/CVE-2024-21413.svg) ![forks](https://img.shields.io/github/forks/ShubhamKanhere307/CVE-2024-21413.svg)

- [https://github.com/MQKGitHub/Moniker-Link-CVE-2024-21413](https://github.com/MQKGitHub/Moniker-Link-CVE-2024-21413) :  ![starts](https://img.shields.io/github/stars/MQKGitHub/Moniker-Link-CVE-2024-21413.svg) ![forks](https://img.shields.io/github/forks/MQKGitHub/Moniker-Link-CVE-2024-21413.svg)

- [https://github.com/Redfox-Security/Unveiling-Moniker-Link-CVE-2024-21413-Navigating-the-Latest-Cybersecurity-Landscape](https://github.com/Redfox-Security/Unveiling-Moniker-Link-CVE-2024-21413-Navigating-the-Latest-Cybersecurity-Landscape) :  ![starts](https://img.shields.io/github/stars/Redfox-Security/Unveiling-Moniker-Link-CVE-2024-21413-Navigating-the-Latest-Cybersecurity-Landscape.svg) ![forks](https://img.shields.io/github/forks/Redfox-Security/Unveiling-Moniker-Link-CVE-2024-21413-Navigating-the-Latest-Cybersecurity-Landscape.svg)

## CVE-2024-21412
 Internet Shortcut Files Security Feature Bypass Vulnerability



- [https://github.com/lsr00ter/CVE-2024-21412_Water-Hydra](https://github.com/lsr00ter/CVE-2024-21412_Water-Hydra) :  ![starts](https://img.shields.io/github/stars/lsr00ter/CVE-2024-21412_Water-Hydra.svg) ![forks](https://img.shields.io/github/forks/lsr00ter/CVE-2024-21412_Water-Hydra.svg)

## CVE-2024-21388
 Microsoft Edge (Chromium-based) Elevation of Privilege Vulnerability



- [https://github.com/d0rb/CVE-2024-21388](https://github.com/d0rb/CVE-2024-21388) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2024-21388.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2024-21388.svg)

## CVE-2024-21378
 Microsoft Outlook Remote Code Execution Vulnerability



- [https://github.com/d0rb/CVE-2024-21378](https://github.com/d0rb/CVE-2024-21378) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2024-21378.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2024-21378.svg)

## CVE-2024-21345
 Windows Kernel Elevation of Privilege Vulnerability



- [https://github.com/exploits-forsale/CVE-2024-21345](https://github.com/exploits-forsale/CVE-2024-21345) :  ![starts](https://img.shields.io/github/stars/exploits-forsale/CVE-2024-21345.svg) ![forks](https://img.shields.io/github/forks/exploits-forsale/CVE-2024-21345.svg)

- [https://github.com/FoxyProxys/CVE-2024-21345](https://github.com/FoxyProxys/CVE-2024-21345) :  ![starts](https://img.shields.io/github/stars/FoxyProxys/CVE-2024-21345.svg) ![forks](https://img.shields.io/github/forks/FoxyProxys/CVE-2024-21345.svg)

## CVE-2024-21338
 Windows Kernel Elevation of Privilege Vulnerability



- [https://github.com/hakaioffsec/CVE-2024-21338](https://github.com/hakaioffsec/CVE-2024-21338) :  ![starts](https://img.shields.io/github/stars/hakaioffsec/CVE-2024-21338.svg) ![forks](https://img.shields.io/github/forks/hakaioffsec/CVE-2024-21338.svg)

- [https://github.com/Crowdfense/CVE-2024-21338](https://github.com/Crowdfense/CVE-2024-21338) :  ![starts](https://img.shields.io/github/stars/Crowdfense/CVE-2024-21338.svg) ![forks](https://img.shields.io/github/forks/Crowdfense/CVE-2024-21338.svg)

- [https://github.com/tykawaii98/CVE-2024-21338_PoC](https://github.com/tykawaii98/CVE-2024-21338_PoC) :  ![starts](https://img.shields.io/github/stars/tykawaii98/CVE-2024-21338_PoC.svg) ![forks](https://img.shields.io/github/forks/tykawaii98/CVE-2024-21338_PoC.svg)

- [https://github.com/Zombie-Kaiser/CVE-2024-21338-x64-build-](https://github.com/Zombie-Kaiser/CVE-2024-21338-x64-build-) :  ![starts](https://img.shields.io/github/stars/Zombie-Kaiser/CVE-2024-21338-x64-build-.svg) ![forks](https://img.shields.io/github/forks/Zombie-Kaiser/CVE-2024-21338-x64-build-.svg)

- [https://github.com/UMU618/CVE-2024-21338](https://github.com/UMU618/CVE-2024-21338) :  ![starts](https://img.shields.io/github/stars/UMU618/CVE-2024-21338.svg) ![forks](https://img.shields.io/github/forks/UMU618/CVE-2024-21338.svg)

- [https://github.com/hackyboiz/kcfg-bypass](https://github.com/hackyboiz/kcfg-bypass) :  ![starts](https://img.shields.io/github/stars/hackyboiz/kcfg-bypass.svg) ![forks](https://img.shields.io/github/forks/hackyboiz/kcfg-bypass.svg)

- [https://github.com/wusijie/CVE-2024-21338-1](https://github.com/wusijie/CVE-2024-21338-1) :  ![starts](https://img.shields.io/github/stars/wusijie/CVE-2024-21338-1.svg) ![forks](https://img.shields.io/github/forks/wusijie/CVE-2024-21338-1.svg)

## CVE-2024-21306
 Microsoft Bluetooth Driver Spoofing Vulnerability



- [https://github.com/Danyw24/blueXploit](https://github.com/Danyw24/blueXploit) :  ![starts](https://img.shields.io/github/stars/Danyw24/blueXploit.svg) ![forks](https://img.shields.io/github/forks/Danyw24/blueXploit.svg)

- [https://github.com/PhucHauDeveloper/BadBlue](https://github.com/PhucHauDeveloper/BadBlue) :  ![starts](https://img.shields.io/github/stars/PhucHauDeveloper/BadBlue.svg) ![forks](https://img.shields.io/github/forks/PhucHauDeveloper/BadBlue.svg)

- [https://github.com/d4rks1d33/C-PoC-for-CVE-2024-21306](https://github.com/d4rks1d33/C-PoC-for-CVE-2024-21306) :  ![starts](https://img.shields.io/github/stars/d4rks1d33/C-PoC-for-CVE-2024-21306.svg) ![forks](https://img.shields.io/github/forks/d4rks1d33/C-PoC-for-CVE-2024-21306.svg)

## CVE-2024-21305
 Hypervisor-Protected Code Integrity (HVCI) Security Feature Bypass Vulnerability



- [https://github.com/tandasat/CVE-2024-21305](https://github.com/tandasat/CVE-2024-21305) :  ![starts](https://img.shields.io/github/stars/tandasat/CVE-2024-21305.svg) ![forks](https://img.shields.io/github/forks/tandasat/CVE-2024-21305.svg)

## CVE-2024-21182
 Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions that are affected are 12.2.1.4.0 and  14.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server.  Successful attacks of this vulnerability can result in  unauthorized access to critical data or complete access to all Oracle WebLogic Server accessible data. CVSS 3.1 Base Score 7.5 (Confidentiality impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N).



- [https://github.com/kursadalsan/CVE-2024-21182](https://github.com/kursadalsan/CVE-2024-21182) :  ![starts](https://img.shields.io/github/stars/kursadalsan/CVE-2024-21182.svg) ![forks](https://img.shields.io/github/forks/kursadalsan/CVE-2024-21182.svg)

- [https://github.com/k4it0k1d/CVE-2024-21182](https://github.com/k4it0k1d/CVE-2024-21182) :  ![starts](https://img.shields.io/github/stars/k4it0k1d/CVE-2024-21182.svg) ![forks](https://img.shields.io/github/forks/k4it0k1d/CVE-2024-21182.svg)

## CVE-2024-21111
 Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).  Supported versions that are affected are Prior to 7.0.16. Easily exploitable vulnerability allows low privileged attacker with logon to the infrastructure where Oracle VM VirtualBox executes to compromise Oracle VM VirtualBox.  Successful attacks of this vulnerability can result in takeover of Oracle VM VirtualBox. Note: This vulnerability applies to Windows hosts only. CVSS 3.1 Base Score 7.8 (Confidentiality, Integrity and Availability impacts).  CVSS Vector: (CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H).



- [https://github.com/mansk1es/CVE-2024-21111](https://github.com/mansk1es/CVE-2024-21111) :  ![starts](https://img.shields.io/github/stars/mansk1es/CVE-2024-21111.svg) ![forks](https://img.shields.io/github/forks/mansk1es/CVE-2024-21111.svg)

- [https://github.com/x0rsys/CVE-2024-21111](https://github.com/x0rsys/CVE-2024-21111) :  ![starts](https://img.shields.io/github/stars/x0rsys/CVE-2024-21111.svg) ![forks](https://img.shields.io/github/forks/x0rsys/CVE-2024-21111.svg)

- [https://github.com/10cks/CVE-2024-21111-del](https://github.com/10cks/CVE-2024-21111-del) :  ![starts](https://img.shields.io/github/stars/10cks/CVE-2024-21111-del.svg) ![forks](https://img.shields.io/github/forks/10cks/CVE-2024-21111-del.svg)

## CVE-2024-21107
 Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).  Supported versions that are affected are Prior to 7.0.16. Easily exploitable vulnerability allows high privileged attacker with logon to the infrastructure where Oracle VM VirtualBox executes to compromise Oracle VM VirtualBox.  Successful attacks of this vulnerability can result in takeover of Oracle VM VirtualBox. Note: This vulnerability applies to Windows hosts only. CVSS 3.1 Base Score 6.7 (Confidentiality, Integrity and Availability impacts).  CVSS Vector: (CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H).



- [https://github.com/Alaatk/CVE-2024-21107](https://github.com/Alaatk/CVE-2024-21107) :  ![starts](https://img.shields.io/github/stars/Alaatk/CVE-2024-21107.svg) ![forks](https://img.shields.io/github/forks/Alaatk/CVE-2024-21107.svg)

## CVE-2024-21006
 Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions that are affected are 12.2.1.4.0 and  14.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server.  Successful attacks of this vulnerability can result in  unauthorized access to critical data or complete access to all Oracle WebLogic Server accessible data. CVSS 3.1 Base Score 7.5 (Confidentiality impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N).



- [https://github.com/lightr3d/CVE-2024-21006_jar](https://github.com/lightr3d/CVE-2024-21006_jar) :  ![starts](https://img.shields.io/github/stars/lightr3d/CVE-2024-21006_jar.svg) ![forks](https://img.shields.io/github/forks/lightr3d/CVE-2024-21006_jar.svg)

- [https://github.com/momika233/CVE-2024-21006](https://github.com/momika233/CVE-2024-21006) :  ![starts](https://img.shields.io/github/stars/momika233/CVE-2024-21006.svg) ![forks](https://img.shields.io/github/forks/momika233/CVE-2024-21006.svg)

- [https://github.com/dadvlingd/CVE-2024-21006](https://github.com/dadvlingd/CVE-2024-21006) :  ![starts](https://img.shields.io/github/stars/dadvlingd/CVE-2024-21006.svg) ![forks](https://img.shields.io/github/forks/dadvlingd/CVE-2024-21006.svg)

## CVE-2024-20931
 Vulnerability in the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Core).  Supported versions that are affected are 12.2.1.4.0 and  14.1.1.0.0. Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server.  Successful attacks of this vulnerability can result in  unauthorized access to critical data or complete access to all Oracle WebLogic Server accessible data. CVSS 3.1 Base Score 7.5 (Confidentiality impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N).



- [https://github.com/gobysec/Goby](https://github.com/gobysec/Goby) :  ![starts](https://img.shields.io/github/stars/gobysec/Goby.svg) ![forks](https://img.shields.io/github/forks/gobysec/Goby.svg)

- [https://github.com/gobysec/GobyVuls](https://github.com/gobysec/GobyVuls) :  ![starts](https://img.shields.io/github/stars/gobysec/GobyVuls.svg) ![forks](https://img.shields.io/github/forks/gobysec/GobyVuls.svg)

- [https://github.com/GlassyAmadeus/CVE-2024-20931](https://github.com/GlassyAmadeus/CVE-2024-20931) :  ![starts](https://img.shields.io/github/stars/GlassyAmadeus/CVE-2024-20931.svg) ![forks](https://img.shields.io/github/forks/GlassyAmadeus/CVE-2024-20931.svg)

- [https://github.com/dinosn/CVE-2024-20931](https://github.com/dinosn/CVE-2024-20931) :  ![starts](https://img.shields.io/github/stars/dinosn/CVE-2024-20931.svg) ![forks](https://img.shields.io/github/forks/dinosn/CVE-2024-20931.svg)

- [https://github.com/Leocodefocus/CVE-2024-20931-Poc](https://github.com/Leocodefocus/CVE-2024-20931-Poc) :  ![starts](https://img.shields.io/github/stars/Leocodefocus/CVE-2024-20931-Poc.svg) ![forks](https://img.shields.io/github/forks/Leocodefocus/CVE-2024-20931-Poc.svg)

- [https://github.com/ATonysan/CVE-2024-20931_weblogic](https://github.com/ATonysan/CVE-2024-20931_weblogic) :  ![starts](https://img.shields.io/github/stars/ATonysan/CVE-2024-20931_weblogic.svg) ![forks](https://img.shields.io/github/forks/ATonysan/CVE-2024-20931_weblogic.svg)

## CVE-2024-20767
 ColdFusion versions 2023.6, 2021.12 and earlier are affected by an Improper Access Control vulnerability that could result in arbitrary file system read. An attacker could leverage this vulnerability to access or modify restricted files. Exploitation of this issue does not require user interaction. Exploitation of this issue requires the admin panel be exposed to the internet.



- [https://github.com/yoryio/CVE-2024-20767](https://github.com/yoryio/CVE-2024-20767) :  ![starts](https://img.shields.io/github/stars/yoryio/CVE-2024-20767.svg) ![forks](https://img.shields.io/github/forks/yoryio/CVE-2024-20767.svg)

- [https://github.com/Chocapikk/CVE-2024-20767](https://github.com/Chocapikk/CVE-2024-20767) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-20767.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-20767.svg)

- [https://github.com/m-cetin/CVE-2024-20767](https://github.com/m-cetin/CVE-2024-20767) :  ![starts](https://img.shields.io/github/stars/m-cetin/CVE-2024-20767.svg) ![forks](https://img.shields.io/github/forks/m-cetin/CVE-2024-20767.svg)

- [https://github.com/Praison001/CVE-2024-20767-Adobe-ColdFusion](https://github.com/Praison001/CVE-2024-20767-Adobe-ColdFusion) :  ![starts](https://img.shields.io/github/stars/Praison001/CVE-2024-20767-Adobe-ColdFusion.svg) ![forks](https://img.shields.io/github/forks/Praison001/CVE-2024-20767-Adobe-ColdFusion.svg)

- [https://github.com/alm6no5/CVE-2024-20767](https://github.com/alm6no5/CVE-2024-20767) :  ![starts](https://img.shields.io/github/stars/alm6no5/CVE-2024-20767.svg) ![forks](https://img.shields.io/github/forks/alm6no5/CVE-2024-20767.svg)

## CVE-2024-20698
 Windows Kernel Elevation of Privilege Vulnerability



- [https://github.com/RomanRybachek/CVE-2024-20698](https://github.com/RomanRybachek/CVE-2024-20698) :  ![starts](https://img.shields.io/github/stars/RomanRybachek/CVE-2024-20698.svg) ![forks](https://img.shields.io/github/forks/RomanRybachek/CVE-2024-20698.svg)

## CVE-2024-20696
 Windows libarchive Remote Code Execution Vulnerability



- [https://github.com/clearbluejar/CVE-2024-20696](https://github.com/clearbluejar/CVE-2024-20696) :  ![starts](https://img.shields.io/github/stars/clearbluejar/CVE-2024-20696.svg) ![forks](https://img.shields.io/github/forks/clearbluejar/CVE-2024-20696.svg)

## CVE-2024-20674
 Windows Kerberos Security Feature Bypass Vulnerability



- [https://github.com/gpotter2/CVE-2024-20674](https://github.com/gpotter2/CVE-2024-20674) :  ![starts](https://img.shields.io/github/stars/gpotter2/CVE-2024-20674.svg) ![forks](https://img.shields.io/github/forks/gpotter2/CVE-2024-20674.svg)

## CVE-2024-20666
 BitLocker Security Feature Bypass Vulnerability



- [https://github.com/nnotwen/Script-For-CVE-2024-20666](https://github.com/nnotwen/Script-For-CVE-2024-20666) :  ![starts](https://img.shields.io/github/stars/nnotwen/Script-For-CVE-2024-20666.svg) ![forks](https://img.shields.io/github/forks/nnotwen/Script-For-CVE-2024-20666.svg)

- [https://github.com/invaderslabs/CVE-2024-20666](https://github.com/invaderslabs/CVE-2024-20666) :  ![starts](https://img.shields.io/github/stars/invaderslabs/CVE-2024-20666.svg) ![forks](https://img.shields.io/github/forks/invaderslabs/CVE-2024-20666.svg)

## CVE-2024-20656
 Visual Studio Elevation of Privilege Vulnerability



- [https://github.com/Wh04m1001/CVE-2024-20656](https://github.com/Wh04m1001/CVE-2024-20656) :  ![starts](https://img.shields.io/github/stars/Wh04m1001/CVE-2024-20656.svg) ![forks](https://img.shields.io/github/forks/Wh04m1001/CVE-2024-20656.svg)

## CVE-2024-20405
 A vulnerability in the web-based management interface of Cisco Finesse could allow an unauthenticated, remote attacker to conduct a stored XSS attack by exploiting an RFI vulnerability. 
 This vulnerability is due to insufficient validation of user-supplied input for specific HTTP requests that are sent to an affected device. An attacker could exploit this vulnerability by persuading a user to click a crafted link. A successful exploit could allow the attacker to execute arbitrary script code in the context of the affected interface or access sensitive information on the affected device.



- [https://github.com/AbdElRahmanEzzat1995/CVE-2024-20405](https://github.com/AbdElRahmanEzzat1995/CVE-2024-20405) :  ![starts](https://img.shields.io/github/stars/AbdElRahmanEzzat1995/CVE-2024-20405.svg) ![forks](https://img.shields.io/github/forks/AbdElRahmanEzzat1995/CVE-2024-20405.svg)

## CVE-2024-20404
 A vulnerability in the web-based management interface of Cisco Finesse could allow an unauthenticated, remote attacker to conduct an SSRF attack on an affected system.
 This vulnerability is due to insufficient validation of user-supplied input for specific HTTP requests that are sent to an affected system. An attacker could exploit this vulnerability by sending a crafted HTTP request to the affected device. A successful exploit could allow the attacker to obtain limited sensitive information for services that are associated to the affected device.



- [https://github.com/AbdElRahmanEzzat1995/CVE-2024-20404](https://github.com/AbdElRahmanEzzat1995/CVE-2024-20404) :  ![starts](https://img.shields.io/github/stars/AbdElRahmanEzzat1995/CVE-2024-20404.svg) ![forks](https://img.shields.io/github/forks/AbdElRahmanEzzat1995/CVE-2024-20404.svg)

## CVE-2024-20356
 A vulnerability in the web-based management interface of Cisco Integrated Management Controller (IMC) could allow an authenticated, remote attacker with Administrator-level privileges to perform command injection attacks on an affected system and elevate their privileges to root. This vulnerability is due to insufficient user input validation. An attacker could exploit this vulnerability by sending crafted commands to the web-based management interface of the affected software. A successful exploit could allow the attacker to elevate their privileges to root.



- [https://github.com/nettitude/CVE-2024-20356](https://github.com/nettitude/CVE-2024-20356) :  ![starts](https://img.shields.io/github/stars/nettitude/CVE-2024-20356.svg) ![forks](https://img.shields.io/github/forks/nettitude/CVE-2024-20356.svg)

- [https://github.com/SherllyNeo/CVE_2024_20356](https://github.com/SherllyNeo/CVE_2024_20356) :  ![starts](https://img.shields.io/github/stars/SherllyNeo/CVE_2024_20356.svg) ![forks](https://img.shields.io/github/forks/SherllyNeo/CVE_2024_20356.svg)

## CVE-2024-20338
 A vulnerability in the ISE Posture (System Scan) module of Cisco Secure Client for Linux could allow an authenticated, local attacker to elevate privileges on an affected device.
 This vulnerability is due to the use of an uncontrolled search path element. An attacker could exploit this vulnerability by copying a malicious library file to a specific directory in the filesystem and persuading an administrator to restart a specific process. A successful exploit could allow the attacker to execute arbitrary code on an affected device with root privileges.



- [https://github.com/annmuor/CVE-2024-20338](https://github.com/annmuor/CVE-2024-20338) :  ![starts](https://img.shields.io/github/stars/annmuor/CVE-2024-20338.svg) ![forks](https://img.shields.io/github/forks/annmuor/CVE-2024-20338.svg)

## CVE-2024-20291
 A vulnerability in the access control list (ACL) programming for port channel subinterfaces of Cisco Nexus 3000 and 9000 Series Switches in standalone NX-OS mode could allow an unauthenticated, remote attacker to send traffic that should be blocked through an affected device.
 This vulnerability is due to incorrect hardware programming that occurs when configuration changes are made to port channel member ports. An attacker could exploit this vulnerability by attempting to send traffic through an affected device. A successful exploit could allow the attacker to access network resources that should be protected by an ACL that was applied on port channel subinterfaces.



- [https://github.com/Instructor-Team8/CVE-2024-20291-POC](https://github.com/Instructor-Team8/CVE-2024-20291-POC) :  ![starts](https://img.shields.io/github/stars/Instructor-Team8/CVE-2024-20291-POC.svg) ![forks](https://img.shields.io/github/forks/Instructor-Team8/CVE-2024-20291-POC.svg)

## CVE-2024-20137
 In wlan driver, there is a possible client disconnection due to improper handling of exceptional conditions. This could lead to remote denial of service with no additional execution privileges needed. User interaction is not needed for exploitation. Patch ID: WCNCR00384543; Issue ID: MSV-1727.



- [https://github.com/takistmr/CVE-2024-20137](https://github.com/takistmr/CVE-2024-20137) :  ![starts](https://img.shields.io/github/stars/takistmr/CVE-2024-20137.svg) ![forks](https://img.shields.io/github/forks/takistmr/CVE-2024-20137.svg)

## CVE-2024-13800
 The ConvertPlus plugin for WordPress is vulnerable to unauthorized modification of data that can lead to a denial of service due to a missing capability check on the 'cp_dismiss_notice' AJAX endpoint in all versions up to, and including, 3.5.30. This makes it possible for authenticated attackers, with Subscriber-level access and above, to update option values to '1' on the WordPress site. This can be leveraged to update an option that would create an error on the site and deny service to legitimate users or be used to set some values to true such as registration.



- [https://github.com/RandomRobbieBF/CVE-2024-13800](https://github.com/RandomRobbieBF/CVE-2024-13800) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-13800.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-13800.svg)

## CVE-2024-13513
 The Oliver POS – A WooCommerce Point of Sale (POS) plugin for WordPress is vulnerable to Sensitive Information Exposure in all versions up to, and including, 2.4.2.3 via the logging functionality. This makes it possible for unauthenticated attackers to extract sensitive data including the plugin's clientToken, which in turn can be used to change user account information including emails and account type. This allows attackers to then change account passwords resulting in a complete site takeover. Version 2.4.2.3 disabled logging but left sites with existing log files vulnerable.



- [https://github.com/KTN1990/CVE-2024-13513](https://github.com/KTN1990/CVE-2024-13513) :  ![starts](https://img.shields.io/github/stars/KTN1990/CVE-2024-13513.svg) ![forks](https://img.shields.io/github/forks/KTN1990/CVE-2024-13513.svg)

## CVE-2024-12986
 A vulnerability, which was classified as critical, has been found in DrayTek Vigor2960 and Vigor300B 1.5.1.3/1.5.1.4. This issue affects some unknown processing of the file /cgi-bin/mainfunction.cgi/apmcfgupptim of the component Web Management Interface. The manipulation of the argument session leads to os command injection. The attack may be initiated remotely. The exploit has been disclosed to the public and may be used. Upgrading to version 1.5.1.5 is able to address this issue. It is recommended to upgrade the affected component.



- [https://github.com/Aether-0/CVE-2024-12986](https://github.com/Aether-0/CVE-2024-12986) :  ![starts](https://img.shields.io/github/stars/Aether-0/CVE-2024-12986.svg) ![forks](https://img.shields.io/github/forks/Aether-0/CVE-2024-12986.svg)

## CVE-2024-12970
 Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') vulnerability in TUBITAK BILGEM Pardus OS My Computer allows OS Command Injection.This issue affects Pardus OS My Computer: before 0.7.2.



- [https://github.com/osmancanvural/CVE-2024-12970](https://github.com/osmancanvural/CVE-2024-12970) :  ![starts](https://img.shields.io/github/stars/osmancanvural/CVE-2024-12970.svg) ![forks](https://img.shields.io/github/forks/osmancanvural/CVE-2024-12970.svg)

## CVE-2024-12905
 An Improper Link Resolution Before File Access ("Link Following") and Improper Limitation of a Pathname to a Restricted Directory ("Path Traversal"). This vulnerability occurs when extracting a maliciously crafted tar file, which can result in unauthorized file writes or overwrites outside the intended extraction directory. The issue is associated with index.js in the tar-fs package.

This issue affects tar-fs: from 0.0.0 before 1.16.4, from 2.0.0 before 2.1.2, from 3.0.0 before 3.0.8.



- [https://github.com/theMcSam/CVE-2024-12905-PoC](https://github.com/theMcSam/CVE-2024-12905-PoC) :  ![starts](https://img.shields.io/github/stars/theMcSam/CVE-2024-12905-PoC.svg) ![forks](https://img.shields.io/github/forks/theMcSam/CVE-2024-12905-PoC.svg)

## CVE-2024-12883
 A vulnerability was found in code-projects Job Recruitment 1.0. It has been declared as problematic. Affected by this vulnerability is an unknown functionality of the file /_email.php. The manipulation of the argument email leads to cross site scripting. The attack can be launched remotely. The exploit has been disclosed to the public and may be used.



- [https://github.com/mhtsec/cve-2024-12883](https://github.com/mhtsec/cve-2024-12883) :  ![starts](https://img.shields.io/github/stars/mhtsec/cve-2024-12883.svg) ![forks](https://img.shields.io/github/forks/mhtsec/cve-2024-12883.svg)

## CVE-2024-12856
 The Four-Faith router models F3x24 and F3x36 are affected by an operating system (OS) command injection vulnerability. At least firmware version 2.0 allows authenticated and remote attackers to execute arbitrary OS commands over HTTP when modifying the system time via apply.cgi. Additionally, this firmware version has default credentials which, if not changed, would effectively change this vulnerability into an unauthenticated and remote OS command execution issue.



- [https://github.com/nu113d/CVE-2024-12856](https://github.com/nu113d/CVE-2024-12856) :  ![starts](https://img.shields.io/github/stars/nu113d/CVE-2024-12856.svg) ![forks](https://img.shields.io/github/forks/nu113d/CVE-2024-12856.svg)

## CVE-2024-12849
 The Error Log Viewer By WP Guru plugin for WordPress is vulnerable to Arbitrary File Read in all versions up to, and including, 1.0.1.3 via the wp_ajax_nopriv_elvwp_log_download AJAX action. This makes it possible for unauthenticated attackers to read the contents of arbitrary files on the server, which can contain sensitive information.



- [https://github.com/RandomRobbieBF/CVE-2024-12849](https://github.com/RandomRobbieBF/CVE-2024-12849) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12849.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12849.svg)

- [https://github.com/Nxploited/CVE-2024-12849-Poc](https://github.com/Nxploited/CVE-2024-12849-Poc) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-12849-Poc.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-12849-Poc.svg)

## CVE-2024-12594
 The Custom Login Page Styler – Login Protected Private Site , Change wp-admin login url , WordPress login logo , Temporary admin login access , Rename login , Login customizer, Hide wp-login – Limit Login Attempts – Locked Site plugin for WordPress is vulnerable to privilege escalation due to a missing capability check on the 'lps_generate_temp_access_url' AJAX action in all versions up to, and including, 7.1.1. This makes it possible for authenticated attackers, with Subscriber-level access and above, to login as other users such as subscribers.



- [https://github.com/RandomRobbieBF/CVE-2024-12594](https://github.com/RandomRobbieBF/CVE-2024-12594) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12594.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12594.svg)

## CVE-2024-12583
 The Dynamics 365 Integration plugin for WordPress is vulnerable to Remote Code Execution and Arbitrary File Read in all versions up to, and including, 1.3.23 via Twig Server-Side Template Injection. This is due to missing input validation and sanitization on the render function. This makes it possible for authenticated attackers, with Contributor-level access and above, to execute code on the server.



- [https://github.com/pouriam23/CVE-2024-12583](https://github.com/pouriam23/CVE-2024-12583) :  ![starts](https://img.shields.io/github/stars/pouriam23/CVE-2024-12583.svg) ![forks](https://img.shields.io/github/forks/pouriam23/CVE-2024-12583.svg)

## CVE-2024-12558
 The WP BASE Booking of Appointments, Services and Events plugin for WordPress is vulnerable to unauthorized access of data due to a missing capability check on the export_db function in all versions up to, and including, 4.9.2. This makes it possible for authenticated attackers, with Subscriber-level access and above, to expose sensitive information from the database, such as the hashed administrator password.



- [https://github.com/RandomRobbieBF/CVE-2024-12558](https://github.com/RandomRobbieBF/CVE-2024-12558) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12558.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12558.svg)

- [https://github.com/Nxploited/CVE-2024-12558-exploit](https://github.com/Nxploited/CVE-2024-12558-exploit) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-12558-exploit.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-12558-exploit.svg)

## CVE-2024-12542
 The linkID plugin for WordPress is vulnerable to unauthorized access of data due to a missing capability check when including the 'phpinfo' function in all versions up to, and including, 0.1.2. This makes it possible for unauthenticated attackers to read configuration settings and predefined variables on the site's server. The plugin does not need to be activated for the vulnerability to be exploited.



- [https://github.com/RandomRobbieBF/CVE-2024-12542](https://github.com/RandomRobbieBF/CVE-2024-12542) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12542.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12542.svg)

## CVE-2024-12535
 The Host PHP Info plugin for WordPress is vulnerable to unauthorized access of data due to a missing capability check when including the 'phpinfo' function in all versions up to, and including, 1.0.4. This makes it possible for unauthenticated attackers to read configuration settings and predefined variables on the site's server. The plugin does not need to be activated for the vulnerability to be exploited.



- [https://github.com/RandomRobbieBF/CVE-2024-12535](https://github.com/RandomRobbieBF/CVE-2024-12535) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12535.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12535.svg)

## CVE-2024-12484
 A vulnerability classified as critical was found in Codezips Technical Discussion Forum 1.0. This vulnerability affects unknown code of the file /signuppost.php. The manipulation of the argument Username leads to sql injection. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. Other parameters might be affected as well.



- [https://github.com/LiChaser/CVE-2024-12484](https://github.com/LiChaser/CVE-2024-12484) :  ![starts](https://img.shields.io/github/stars/LiChaser/CVE-2024-12484.svg) ![forks](https://img.shields.io/github/forks/LiChaser/CVE-2024-12484.svg)

## CVE-2024-12471
 The Post Saint: ChatGPT, GPT4, DALL-E, Stable Diffusion, Pexels, Dezgo AI Text & Image Generator plugin for WordPress is vulnerable to arbitrary files uploads due to a missing capability check and file type validation on the add_image_to_library AJAX action function in all versions up to, and including, 1.3.1. This makes it possible for authenticated attackers, with subscriber-level access and above, to upload arbitrary files that make remote code execution possible.



- [https://github.com/RandomRobbieBF/CVE-2024-12471](https://github.com/RandomRobbieBF/CVE-2024-12471) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12471.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12471.svg)

## CVE-2024-12404
 The CF Internal Link Shortcode plugin for WordPress is vulnerable to SQL Injection via the 'post_title' parameter in all versions up to, and including, 1.1.0 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/RandomRobbieBF/CVE-2024-12404](https://github.com/RandomRobbieBF/CVE-2024-12404) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12404.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12404.svg)

## CVE-2024-12345
 A vulnerability classified as problematic was found in INW Krbyyyzo 25.2002. Affected by this vulnerability is an unknown functionality of the file /gbo.aspx of the component Daily Huddle Site. The manipulation of the argument s leads to resource consumption. It is possible to launch the attack on the local host. Other endpoints might be affected as well.



- [https://github.com/RoyaRadin/CVE-2024-12345-POC](https://github.com/RoyaRadin/CVE-2024-12345-POC) :  ![starts](https://img.shields.io/github/stars/RoyaRadin/CVE-2024-12345-POC.svg) ![forks](https://img.shields.io/github/forks/RoyaRadin/CVE-2024-12345-POC.svg)

## CVE-2024-12342
 A vulnerability was found in TP-Link VN020 F3v(T) TT_V6.2.1021. It has been rated as critical. This issue affects some unknown processing of the file /control/WANIPConnection of the component Incomplete SOAP Request Handler. The manipulation leads to denial of service. The attack can only be initiated within the local network. The exploit has been disclosed to the public and may be used.



- [https://github.com/becrevex/TPLink-VN020-DoS](https://github.com/becrevex/TPLink-VN020-DoS) :  ![starts](https://img.shields.io/github/stars/becrevex/TPLink-VN020-DoS.svg) ![forks](https://img.shields.io/github/forks/becrevex/TPLink-VN020-DoS.svg)

## CVE-2024-12270
 The Beautiful taxonomy filters plugin for WordPress is vulnerable to SQL Injection via the 'selects[0][term]' parameter in all versions up to, and including, 2.4.3 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/RandomRobbieBF/CVE-2024-12270](https://github.com/RandomRobbieBF/CVE-2024-12270) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12270.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12270.svg)

## CVE-2024-12252
 The SEO LAT Auto Post plugin for WordPress is vulnerable to file overwrite due to a missing capability check on the remote_update AJAX action in all versions up to, and including, 2.2.1. This makes it possible for unauthenticated attackers to overwrite the seo-beginner-auto-post.php file which can be leveraged to achieve remote code execution.



- [https://github.com/RandomRobbieBF/CVE-2024-12252](https://github.com/RandomRobbieBF/CVE-2024-12252) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12252.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12252.svg)

## CVE-2024-12209
 The WP Umbrella: Update Backup Restore & Monitoring plugin for WordPress is vulnerable to Local File Inclusion in all versions up to, and including, 2.17.0 via the 'filename' parameter of the 'umbrella-restore' action. This makes it possible for unauthenticated attackers to include and execute arbitrary files on the server, allowing the execution of any PHP code in those files. This can be used to bypass access controls, obtain sensitive data, or achieve code execution in cases where images and other “safe” file types can be uploaded and included.



- [https://github.com/Nxploited/CVE-2024-12209](https://github.com/Nxploited/CVE-2024-12209) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-12209.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-12209.svg)

- [https://github.com/RandomRobbieBF/CVE-2024-12209](https://github.com/RandomRobbieBF/CVE-2024-12209) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12209.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12209.svg)

## CVE-2024-12172
 The WP Courses LMS – Online Courses Builder, eLearning Courses, Courses Solution, Education Courses plugin for WordPress is vulnerable to unauthorized access due to a missing capability check on the wpc_update_user_meta_option() function in all versions up to, and including, 3.2.21. This makes it possible for authenticated attackers, with Subscriber-level access and above, to update arbitrary user's metadata which can be levereged to block an administrator from accessing their site when wp_capabilities is set to 0.



- [https://github.com/RandomRobbieBF/CVE-2024-12172](https://github.com/RandomRobbieBF/CVE-2024-12172) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12172.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12172.svg)

## CVE-2024-12157
 The Popup – MailChimp, GetResponse and ActiveCampaign Intergrations plugin for WordPress is vulnerable to SQL Injection via the 'id' parameter of the 'upc_delete_db_record' AJAX action in all versions up to, and including, 3.2.6 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/RandomRobbieBF/CVE-2024-12157](https://github.com/RandomRobbieBF/CVE-2024-12157) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12157.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12157.svg)

## CVE-2024-12085
 A flaw was found in rsync which could be triggered when rsync compares file checksums. This flaw allows an attacker to manipulate the checksum length (s2length) to cause a comparison between a checksum and uninitialized memory and leak one byte of uninitialized stack data at a time.



- [https://github.com/Otsutez/cve-2024-12085](https://github.com/Otsutez/cve-2024-12085) :  ![starts](https://img.shields.io/github/stars/Otsutez/cve-2024-12085.svg) ![forks](https://img.shields.io/github/forks/Otsutez/cve-2024-12085.svg)

## CVE-2024-12025
 The Collapsing Categories plugin for WordPress is vulnerable to SQL Injection via the 'taxonomy' parameter of the /wp-json/collapsing-categories/v1/get REST API in all versions up to, and including, 3.0.8 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/RandomRobbieBF/CVE-2024-12025](https://github.com/RandomRobbieBF/CVE-2024-12025) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-12025.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-12025.svg)

## CVE-2024-11972
 The Hunk Companion WordPress plugin before 1.9.0 does not correctly authorize some REST API endpoints, allowing unauthenticated requests to install and activate arbitrary Hunk Companion WordPress plugin before 1.9.0 from the WordPress.org repo, including vulnerable Hunk Companion WordPress plugin before 1.9.0 that have been closed.



- [https://github.com/JunTakemura/exploit-CVE-2024-11972](https://github.com/JunTakemura/exploit-CVE-2024-11972) :  ![starts](https://img.shields.io/github/stars/JunTakemura/exploit-CVE-2024-11972.svg) ![forks](https://img.shields.io/github/forks/JunTakemura/exploit-CVE-2024-11972.svg)

- [https://github.com/RonF98/CVE-2024-11972-POC](https://github.com/RonF98/CVE-2024-11972-POC) :  ![starts](https://img.shields.io/github/stars/RonF98/CVE-2024-11972-POC.svg) ![forks](https://img.shields.io/github/forks/RonF98/CVE-2024-11972-POC.svg)

## CVE-2024-11728
 The KiviCare – Clinic & Patient Management System (EHR) plugin for WordPress is vulnerable to SQL Injection via the 'visit_type[service_id]' parameter of the tax_calculated_data AJAX action in all versions up to, and including, 3.6.4 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/samogod/CVE-2024-11728](https://github.com/samogod/CVE-2024-11728) :  ![starts](https://img.shields.io/github/stars/samogod/CVE-2024-11728.svg) ![forks](https://img.shields.io/github/forks/samogod/CVE-2024-11728.svg)

## CVE-2024-11680
 ProjectSend versions prior to r1720 are affected by an improper authentication vulnerability. Remote, unauthenticated attackers can exploit this flaw by sending crafted HTTP requests to options.php, enabling unauthorized modification of the application's configuration. Successful exploitation allows attackers to create accounts, upload webshells, and embed malicious JavaScript.



- [https://github.com/D3N14LD15K/CVE-2024-11680_PoC_Exploit](https://github.com/D3N14LD15K/CVE-2024-11680_PoC_Exploit) :  ![starts](https://img.shields.io/github/stars/D3N14LD15K/CVE-2024-11680_PoC_Exploit.svg) ![forks](https://img.shields.io/github/forks/D3N14LD15K/CVE-2024-11680_PoC_Exploit.svg)

## CVE-2024-11643
 The Accessibility by AllAccessible plugin for WordPress is vulnerable to unauthorized modification of data that can lead to privilege escalation due to a missing capability check on the 'AllAccessible_save_settings' function in all versions up to, and including, 1.3.4. This makes it possible for authenticated attackers, with Subscriber-level access and above, to update arbitrary options on the WordPress site. This can be leveraged to update the default role for registration to administrator and enable user registration for attackers to gain administrative user access to a vulnerable site.



- [https://github.com/RandomRobbieBF/CVE-2024-11643](https://github.com/RandomRobbieBF/CVE-2024-11643) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-11643.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-11643.svg)

## CVE-2024-11616
 Netskope was made aware of a security vulnerability in Netskope Endpoint DLP’s Content Control Driver where a double-fetch issue leads to heap overflow. The vulnerability arises from the fact that the NumberOfBytes argument to ExAllocatePoolWithTag, and the Length argument for RtlCopyMemory, both independently dereference their value from the user supplied input buffer inside the EpdlpSetUsbAction function, known as a double-fetch. If this length value grows to a higher value in between these two calls, it will result in the RtlCopyMemory call copying user-supplied memory contents outside the range of the allocated buffer, resulting in a heap overflow. A malicious attacker will need admin privileges to exploit the issue.
This issue affects Endpoint DLP version below R119.



- [https://github.com/inb1ts/CVE-2024-11616](https://github.com/inb1ts/CVE-2024-11616) :  ![starts](https://img.shields.io/github/stars/inb1ts/CVE-2024-11616.svg) ![forks](https://img.shields.io/github/forks/inb1ts/CVE-2024-11616.svg)

## CVE-2024-11613
 The WordPress File Upload plugin for WordPress is vulnerable to Remote Code Execution, Arbitrary File Read, and Arbitrary File Deletion in all versions up to, and including, 4.24.15 via the 'wfu_file_downloader.php' file. This is due to lack of proper sanitization of the 'source' parameter and allowing a user-defined directory path. This makes it possible for unauthenticated attackers to execute code on the server.



- [https://github.com/Sachinart/CVE-2024-11613-wp-file-upload](https://github.com/Sachinart/CVE-2024-11613-wp-file-upload) :  ![starts](https://img.shields.io/github/stars/Sachinart/CVE-2024-11613-wp-file-upload.svg) ![forks](https://img.shields.io/github/forks/Sachinart/CVE-2024-11613-wp-file-upload.svg)

## CVE-2024-11477
 7-Zip Zstandard Decompression Integer Underflow Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of 7-Zip. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation.

The specific flaw exists within the implementation of Zstandard decompression. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process. Was ZDI-CAN-24346.



- [https://github.com/TheN00bBuilder/cve-2024-11477-writeup](https://github.com/TheN00bBuilder/cve-2024-11477-writeup) :  ![starts](https://img.shields.io/github/stars/TheN00bBuilder/cve-2024-11477-writeup.svg) ![forks](https://img.shields.io/github/forks/TheN00bBuilder/cve-2024-11477-writeup.svg)

## CVE-2024-11423
 The Ultimate Gift Cards for WooCommerce – Create WooCommerce Gift Cards, Gift Vouchers, Redeem & Manage Digital Gift Coupons. Offer Gift Certificates, Schedule Gift Cards, and Use Advance Coupons With Personalized Templates plugin for WordPress is vulnerable to unauthorized modification of data due to a missing capability check on several REST API endpoints such as /wp-json/gifting/recharge-giftcard in all versions up to, and including, 3.0.6. This makes it possible for unauthenticated attackers to recharge a gift card balance, without making a payment along with reducing gift card balances without purchasing anything.



- [https://github.com/RandomRobbieBF/CVE-2024-11423](https://github.com/RandomRobbieBF/CVE-2024-11423) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-11423.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-11423.svg)

## CVE-2024-11396
 The Event Monster – Event Management, Tickets Booking, Upcoming Event plugin for WordPress is vulnerable to Information Exposure in all versions up to, and including, 1.4.3 via the Visitors List Export file. During the export, a CSV file is created in the wp-content folder with a hardcoded filename that is publicly accessible. This makes it possible for unauthenticated attackers to extract data about event visitors, that includes first and last names, email, and phone number.



- [https://github.com/RandomRobbieBF/CVE-2024-11396](https://github.com/RandomRobbieBF/CVE-2024-11396) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-11396.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-11396.svg)

## CVE-2024-11394
 Hugging Face Transformers Trax Model Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hugging Face Transformers. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the handling of model files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user. Was ZDI-CAN-25012.



- [https://github.com/Piyush-Bhor/CVE-2024-11394](https://github.com/Piyush-Bhor/CVE-2024-11394) :  ![starts](https://img.shields.io/github/stars/Piyush-Bhor/CVE-2024-11394.svg) ![forks](https://img.shields.io/github/forks/Piyush-Bhor/CVE-2024-11394.svg)

## CVE-2024-11393
 Hugging Face Transformers MaskFormer Model Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hugging Face Transformers. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the parsing of model files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user. Was ZDI-CAN-25191.



- [https://github.com/Piyush-Bhor/CVE-2024-11393](https://github.com/Piyush-Bhor/CVE-2024-11393) :  ![starts](https://img.shields.io/github/stars/Piyush-Bhor/CVE-2024-11393.svg) ![forks](https://img.shields.io/github/forks/Piyush-Bhor/CVE-2024-11393.svg)

## CVE-2024-11392
 Hugging Face Transformers MobileViTV2 Deserialization of Untrusted Data Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hugging Face Transformers. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the handling of configuration files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user. Was ZDI-CAN-24322.



- [https://github.com/Piyush-Bhor/CVE-2024-11392](https://github.com/Piyush-Bhor/CVE-2024-11392) :  ![starts](https://img.shields.io/github/stars/Piyush-Bhor/CVE-2024-11392.svg) ![forks](https://img.shields.io/github/forks/Piyush-Bhor/CVE-2024-11392.svg)

## CVE-2024-11320
 Arbitrary commands execution on the server by exploiting a command injection vulnerability in the LDAP authentication mechanism. This issue affects Pandora FMS: from 700 through =777.4



- [https://github.com/mhaskar/CVE-2024-11320](https://github.com/mhaskar/CVE-2024-11320) :  ![starts](https://img.shields.io/github/stars/mhaskar/CVE-2024-11320.svg) ![forks](https://img.shields.io/github/forks/mhaskar/CVE-2024-11320.svg)

## CVE-2024-11318
 An IDOR (Insecure Direct Object Reference) vulnerability has been discovered in AbsysNet, affecting version 2.3.1. This vulnerability could allow a remote attacker to obtain the session of an unauthenticated user by brute-force attacking the session identifier on the "/cgi-bin/ocap/" endpoint.



- [https://github.com/xthalach/CVE-2024-11318](https://github.com/xthalach/CVE-2024-11318) :  ![starts](https://img.shields.io/github/stars/xthalach/CVE-2024-11318.svg) ![forks](https://img.shields.io/github/forks/xthalach/CVE-2024-11318.svg)

## CVE-2024-11252
 The Social Sharing Plugin – Sassy Social Share plugin for WordPress is vulnerable to Reflected Cross-Site Scripting via the heateor_mastodon_share parameter in all versions up to, and including, 3.3.69 due to insufficient input sanitization and output escaping. This makes it possible for unauthenticated attackers to inject arbitrary web scripts in pages that execute if they can successfully trick a user into performing an action such as clicking on a link.



- [https://github.com/reinh3rz/CVE-2024-11252-Sassy-Social-Share-XSS](https://github.com/reinh3rz/CVE-2024-11252-Sassy-Social-Share-XSS) :  ![starts](https://img.shields.io/github/stars/reinh3rz/CVE-2024-11252-Sassy-Social-Share-XSS.svg) ![forks](https://img.shields.io/github/forks/reinh3rz/CVE-2024-11252-Sassy-Social-Share-XSS.svg)

## CVE-2024-11201
 The myCred – Loyalty Points and Rewards plugin for WordPress and WooCommerce – Give Points, Ranks, Badges, Cashback, WooCommerce rewards, and WooCommerce credits for Gamification plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the plugin's mycred_send shortcode in all versions up to, and including, 2.7.5.2 due to insufficient input sanitization and output escaping on user supplied attributes. This makes it possible for authenticated attackers, with contributor-level access and above, to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page.



- [https://github.com/NSQAQ/CVE-2024-11201](https://github.com/NSQAQ/CVE-2024-11201) :  ![starts](https://img.shields.io/github/stars/NSQAQ/CVE-2024-11201.svg) ![forks](https://img.shields.io/github/forks/NSQAQ/CVE-2024-11201.svg)

## CVE-2024-11003
 Qualys discovered that needrestart, before version 3.8, passes unsanitized data to a library (Modules::ScanDeps) which expects safe input. This could allow a local attacker to execute arbitrary shell commands. Please see the related CVE-2024-10224 in Modules::ScanDeps.



- [https://github.com/unknown-user-from/CVE-2024-11003-PoC](https://github.com/unknown-user-from/CVE-2024-11003-PoC) :  ![starts](https://img.shields.io/github/stars/unknown-user-from/CVE-2024-11003-PoC.svg) ![forks](https://img.shields.io/github/forks/unknown-user-from/CVE-2024-11003-PoC.svg)

## CVE-2024-10958
 The The WP Photo Album Plus plugin for WordPress is vulnerable to arbitrary shortcode execution via getshortcodedrenderedfenodelay AJAX action in all versions up to, and including, 8.8.08.007 . This is due to the software allowing users to execute an action that does not properly validate a value before running do_shortcode. This makes it possible for unauthenticated attackers to execute arbitrary shortcodes.



- [https://github.com/reinh3rz/CVE-2024-10958-WPPA-Exploit](https://github.com/reinh3rz/CVE-2024-10958-WPPA-Exploit) :  ![starts](https://img.shields.io/github/stars/reinh3rz/CVE-2024-10958-WPPA-Exploit.svg) ![forks](https://img.shields.io/github/forks/reinh3rz/CVE-2024-10958-WPPA-Exploit.svg)

## CVE-2024-10924
 The Really Simple Security (Free, Pro, and Pro Multisite) plugins for WordPress are vulnerable to authentication bypass in versions 9.0.0 to 9.1.1.1. This is due to improper user check error handling in the two-factor REST API actions with the 'check_login_and_get_user' function. This makes it possible for unauthenticated attackers to log in as any existing user on the site, such as an administrator, when the "Two-Factor Authentication" setting is enabled (disabled by default).



- [https://github.com/m3ssap0/wordpress-really-simple-security-authn-bypass-exploit](https://github.com/m3ssap0/wordpress-really-simple-security-authn-bypass-exploit) :  ![starts](https://img.shields.io/github/stars/m3ssap0/wordpress-really-simple-security-authn-bypass-exploit.svg) ![forks](https://img.shields.io/github/forks/m3ssap0/wordpress-really-simple-security-authn-bypass-exploit.svg)

- [https://github.com/m3ssap0/wordpress-really-simple-security-authn-bypass-vulnerable-application](https://github.com/m3ssap0/wordpress-really-simple-security-authn-bypass-vulnerable-application) :  ![starts](https://img.shields.io/github/stars/m3ssap0/wordpress-really-simple-security-authn-bypass-vulnerable-application.svg) ![forks](https://img.shields.io/github/forks/m3ssap0/wordpress-really-simple-security-authn-bypass-vulnerable-application.svg)

- [https://github.com/RandomRobbieBF/CVE-2024-10924](https://github.com/RandomRobbieBF/CVE-2024-10924) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-10924.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-10924.svg)

- [https://github.com/Maalfer/CVE-2024-10924-PoC](https://github.com/Maalfer/CVE-2024-10924-PoC) :  ![starts](https://img.shields.io/github/stars/Maalfer/CVE-2024-10924-PoC.svg) ![forks](https://img.shields.io/github/forks/Maalfer/CVE-2024-10924-PoC.svg)

- [https://github.com/Trackflaw/CVE-2024-10924-Wordpress-Docker](https://github.com/Trackflaw/CVE-2024-10924-Wordpress-Docker) :  ![starts](https://img.shields.io/github/stars/Trackflaw/CVE-2024-10924-Wordpress-Docker.svg) ![forks](https://img.shields.io/github/forks/Trackflaw/CVE-2024-10924-Wordpress-Docker.svg)

- [https://github.com/D1se0/CVE-2024-10924-Bypass-MFA-Wordpress-LAB](https://github.com/D1se0/CVE-2024-10924-Bypass-MFA-Wordpress-LAB) :  ![starts](https://img.shields.io/github/stars/D1se0/CVE-2024-10924-Bypass-MFA-Wordpress-LAB.svg) ![forks](https://img.shields.io/github/forks/D1se0/CVE-2024-10924-Bypass-MFA-Wordpress-LAB.svg)

- [https://github.com/julesbsz/CVE-2024-10924](https://github.com/julesbsz/CVE-2024-10924) :  ![starts](https://img.shields.io/github/stars/julesbsz/CVE-2024-10924.svg) ![forks](https://img.shields.io/github/forks/julesbsz/CVE-2024-10924.svg)

- [https://github.com/MattJButler/CVE-2024-10924](https://github.com/MattJButler/CVE-2024-10924) :  ![starts](https://img.shields.io/github/stars/MattJButler/CVE-2024-10924.svg) ![forks](https://img.shields.io/github/forks/MattJButler/CVE-2024-10924.svg)

- [https://github.com/OliveiraaX/-CVE-2024-10924](https://github.com/OliveiraaX/-CVE-2024-10924) :  ![starts](https://img.shields.io/github/stars/OliveiraaX/-CVE-2024-10924.svg) ![forks](https://img.shields.io/github/forks/OliveiraaX/-CVE-2024-10924.svg)

- [https://github.com/Hunt3r850/CVE-2024-10924-Wordpress-Docker](https://github.com/Hunt3r850/CVE-2024-10924-Wordpress-Docker) :  ![starts](https://img.shields.io/github/stars/Hunt3r850/CVE-2024-10924-Wordpress-Docker.svg) ![forks](https://img.shields.io/github/forks/Hunt3r850/CVE-2024-10924-Wordpress-Docker.svg)

- [https://github.com/Hunt3r850/CVE-2024-10924-PoC](https://github.com/Hunt3r850/CVE-2024-10924-PoC) :  ![starts](https://img.shields.io/github/stars/Hunt3r850/CVE-2024-10924-PoC.svg) ![forks](https://img.shields.io/github/forks/Hunt3r850/CVE-2024-10924-PoC.svg)

## CVE-2024-10915
 A vulnerability was found in D-Link DNS-320, DNS-320LW, DNS-325 and DNS-340L up to 20241028. It has been rated as critical. Affected by this issue is the function cgi_user_add of the file /cgi-bin/account_mgr.cgi?cmd=cgi_user_add. The manipulation of the argument group leads to os command injection. The attack may be launched remotely. The complexity of an attack is rather high. The exploitation is known to be difficult. The exploit has been disclosed to the public and may be used.



- [https://github.com/r0otk3r/CVE-2024-10915](https://github.com/r0otk3r/CVE-2024-10915) :  ![starts](https://img.shields.io/github/stars/r0otk3r/CVE-2024-10915.svg) ![forks](https://img.shields.io/github/forks/r0otk3r/CVE-2024-10915.svg)

## CVE-2024-10914
 A vulnerability was found in D-Link DNS-320, DNS-320LW, DNS-325 and DNS-340L up to 20241028. It has been declared as critical. Affected by this vulnerability is the function cgi_user_add of the file /cgi-bin/account_mgr.cgi?cmd=cgi_user_add. The manipulation of the argument name leads to os command injection. The attack can be launched remotely. The complexity of an attack is rather high. The exploitation appears to be difficult. The exploit has been disclosed to the public and may be used.



- [https://github.com/verylazytech/CVE-2024-10914](https://github.com/verylazytech/CVE-2024-10914) :  ![starts](https://img.shields.io/github/stars/verylazytech/CVE-2024-10914.svg) ![forks](https://img.shields.io/github/forks/verylazytech/CVE-2024-10914.svg)

- [https://github.com/imnotcha0s/CVE-2024-10914](https://github.com/imnotcha0s/CVE-2024-10914) :  ![starts](https://img.shields.io/github/stars/imnotcha0s/CVE-2024-10914.svg) ![forks](https://img.shields.io/github/forks/imnotcha0s/CVE-2024-10914.svg)

- [https://github.com/ThemeHackers/CVE-2024-10914](https://github.com/ThemeHackers/CVE-2024-10914) :  ![starts](https://img.shields.io/github/stars/ThemeHackers/CVE-2024-10914.svg) ![forks](https://img.shields.io/github/forks/ThemeHackers/CVE-2024-10914.svg)

- [https://github.com/K3ysTr0K3R/CVE-2024-10914-EXPLOIT](https://github.com/K3ysTr0K3R/CVE-2024-10914-EXPLOIT) :  ![starts](https://img.shields.io/github/stars/K3ysTr0K3R/CVE-2024-10914-EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/K3ysTr0K3R/CVE-2024-10914-EXPLOIT.svg)

- [https://github.com/redspy-sec/D-Link](https://github.com/redspy-sec/D-Link) :  ![starts](https://img.shields.io/github/stars/redspy-sec/D-Link.svg) ![forks](https://img.shields.io/github/forks/redspy-sec/D-Link.svg)

- [https://github.com/Bu0uCat/D-Link-NAS-CVE-2024-10914-](https://github.com/Bu0uCat/D-Link-NAS-CVE-2024-10914-) :  ![starts](https://img.shields.io/github/stars/Bu0uCat/D-Link-NAS-CVE-2024-10914-.svg) ![forks](https://img.shields.io/github/forks/Bu0uCat/D-Link-NAS-CVE-2024-10914-.svg)

- [https://github.com/dragonXZH/CVE-2024-10914](https://github.com/dragonXZH/CVE-2024-10914) :  ![starts](https://img.shields.io/github/stars/dragonXZH/CVE-2024-10914.svg) ![forks](https://img.shields.io/github/forks/dragonXZH/CVE-2024-10914.svg)

- [https://github.com/Egi08/CVE-2024-10914](https://github.com/Egi08/CVE-2024-10914) :  ![starts](https://img.shields.io/github/stars/Egi08/CVE-2024-10914.svg) ![forks](https://img.shields.io/github/forks/Egi08/CVE-2024-10914.svg)

- [https://github.com/retuci0/cve-2024-10914-port](https://github.com/retuci0/cve-2024-10914-port) :  ![starts](https://img.shields.io/github/stars/retuci0/cve-2024-10914-port.svg) ![forks](https://img.shields.io/github/forks/retuci0/cve-2024-10914-port.svg)

- [https://github.com/jahithoque/CVE-2024-10914-Exploit](https://github.com/jahithoque/CVE-2024-10914-Exploit) :  ![starts](https://img.shields.io/github/stars/jahithoque/CVE-2024-10914-Exploit.svg) ![forks](https://img.shields.io/github/forks/jahithoque/CVE-2024-10914-Exploit.svg)

## CVE-2024-10858
 The Jetpack  WordPress plugin before 14.1 does not properly checks the postmessage origin in its 13.x versions, allowing it to be bypassed and leading to DOM-XSS. The issue only affects websites hosted on WordPress.com.



- [https://github.com/iamarit/CVE-2024-10858](https://github.com/iamarit/CVE-2024-10858) :  ![starts](https://img.shields.io/github/stars/iamarit/CVE-2024-10858.svg) ![forks](https://img.shields.io/github/forks/iamarit/CVE-2024-10858.svg)

## CVE-2024-10793
 The WP Activity Log plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the user_id parameter in all versions up to, and including, 5.2.1 due to insufficient input sanitization and output escaping. This makes it possible for unauthenticated attackers to inject arbitrary web scripts in pages that will execute whenever an administrative user accesses an injected page.



- [https://github.com/MAHajian/CVE-2024-10793](https://github.com/MAHajian/CVE-2024-10793) :  ![starts](https://img.shields.io/github/stars/MAHajian/CVE-2024-10793.svg) ![forks](https://img.shields.io/github/forks/MAHajian/CVE-2024-10793.svg)

- [https://github.com/djayaGit/CVE-2024-10793](https://github.com/djayaGit/CVE-2024-10793) :  ![starts](https://img.shields.io/github/stars/djayaGit/CVE-2024-10793.svg) ![forks](https://img.shields.io/github/forks/djayaGit/CVE-2024-10793.svg)

## CVE-2024-10728
 The Post Grid Gutenberg Blocks and WordPress Blog Plugin – PostX plugin for WordPress is vulnerable to unauthorized plugin installation/activation due to a missing capability check on the 'install_required_plugin_callback' function in all versions up to, and including, 4.1.16. This makes it possible for authenticated attackers, with Subscriber-level access and above, to install and activate arbitrary plugins which can be leveraged to achieve remote code execution if another vulnerable plugin is installed and activated.



- [https://github.com/RandomRobbieBF/CVE-2024-10728](https://github.com/RandomRobbieBF/CVE-2024-10728) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-10728.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-10728.svg)

## CVE-2024-10629
 The GPX Viewer plugin for WordPress is vulnerable to arbitrary file creation due to a missing capability check and file type validation in the gpxv_file_upload() function in all versions up to, and including, 2.2.8. This makes it possible for authenticated attackers, with subscriber-level access and above, to create arbitrary files on the affected site's server which may make remote code execution possible.



- [https://github.com/RandomRobbieBF/CVE-2024-10629](https://github.com/RandomRobbieBF/CVE-2024-10629) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-10629.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-10629.svg)

## CVE-2024-10586
 The Debug Tool plugin for WordPress is vulnerable to arbitrary file creation due to a missing capability check on the dbt_pull_image() function and missing file type validation in all versions up to, and including, 2.2. This makes it possible for unauthenticated attackers to to create arbitrary files such as .php files that can be leveraged for remote code execution.



- [https://github.com/RandomRobbieBF/CVE-2024-10586](https://github.com/RandomRobbieBF/CVE-2024-10586) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-10586.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-10586.svg)

- [https://github.com/Nxploited/CVE-2024-10586-Poc](https://github.com/Nxploited/CVE-2024-10586-Poc) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-10586-Poc.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-10586-Poc.svg)

## CVE-2024-10571
 The Chartify – WordPress Chart Plugin plugin for WordPress is vulnerable to Local File Inclusion in all versions up to, and including, 2.9.5 via the 'source' parameter. This makes it possible for unauthenticated attackers to include and execute arbitrary files on the server, allowing the execution of any PHP code in those files. This can be used to bypass access controls, obtain sensitive data, or achieve code execution in cases where images and other “safe” file types can be uploaded and included.



- [https://github.com/RandomRobbieBF/CVE-2024-10571](https://github.com/RandomRobbieBF/CVE-2024-10571) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-10571.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-10571.svg)

## CVE-2024-10542
 The Spam protection, Anti-Spam, FireWall by CleanTalk plugin for WordPress is vulnerable to unauthorized Arbitrary Plugin Installation due to an authorization bypass via reverse DNS spoofing on the checkWithoutToken function in all versions up to, and including, 6.43.2. This makes it possible for unauthenticated attackers to install and activate arbitrary plugins which can be leveraged to achieve remote code execution if another vulnerable plugin is installed and activated.



- [https://github.com/ubaydev/CVE-2024-10542](https://github.com/ubaydev/CVE-2024-10542) :  ![starts](https://img.shields.io/github/stars/ubaydev/CVE-2024-10542.svg) ![forks](https://img.shields.io/github/forks/ubaydev/CVE-2024-10542.svg)

## CVE-2024-10516
 The Swift Performance Lite plugin for WordPress is vulnerable to Local PHP File Inclusion in all versions up to, and including, 2.3.7.1 via the 'ajaxify' function. This makes it possible for unauthenticated attackers to include and execute arbitrary files on the server, allowing the execution of any PHP code in those files. This can be used to bypass access controls, obtain sensitive data, or achieve code execution in cases where images and other “safe” file types can be uploaded and included.



- [https://github.com/RandomRobbieBF/CVE-2024-10516](https://github.com/RandomRobbieBF/CVE-2024-10516) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-10516.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-10516.svg)

## CVE-2024-10511
 CWE-287: Improper Authentication vulnerability exists that could cause Denial of access to the web interface
when someone on the local network repeatedly requests the /accessdenied URL.



- [https://github.com/revengsmK/CVE-2024-10511](https://github.com/revengsmK/CVE-2024-10511) :  ![starts](https://img.shields.io/github/stars/revengsmK/CVE-2024-10511.svg) ![forks](https://img.shields.io/github/forks/revengsmK/CVE-2024-10511.svg)

## CVE-2024-10508
 The RegistrationMagic – User Registration Plugin with Custom Registration Forms plugin for WordPress is vulnerable to privilege escalation via account takeover in all versions up to, and including, 6.0.2.6. This is due to the plugin not properly validating the password reset token prior to updating a user's password. This makes it possible for unauthenticated attackers to reset the password of arbitrary users, including administrators, and gain access to these accounts.



- [https://github.com/Jenderal92/CVE-2024-10508](https://github.com/Jenderal92/CVE-2024-10508) :  ![starts](https://img.shields.io/github/stars/Jenderal92/CVE-2024-10508.svg) ![forks](https://img.shields.io/github/forks/Jenderal92/CVE-2024-10508.svg)

- [https://github.com/ubaydev/CVE-2024-10508](https://github.com/ubaydev/CVE-2024-10508) :  ![starts](https://img.shields.io/github/stars/ubaydev/CVE-2024-10508.svg) ![forks](https://img.shields.io/github/forks/ubaydev/CVE-2024-10508.svg)

## CVE-2024-10470
 The WPLMS Learning Management System for WordPress, WordPress LMS theme for WordPress is vulnerable to arbitrary file read and deletion due to insufficient file path validation and permissions checks in the readfile and unlink functions in all versions up to, and including, 4.962. This makes it possible for unauthenticated attackers to delete arbitrary files on the server, which can easily lead to remote code execution when the right file is deleted (such as wp-config.php). The theme is vulnerable even when it is not activated.



- [https://github.com/RandomRobbieBF/CVE-2024-10470](https://github.com/RandomRobbieBF/CVE-2024-10470) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-10470.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-10470.svg)

- [https://github.com/0xshoriful/CVE-2024-10470](https://github.com/0xshoriful/CVE-2024-10470) :  ![starts](https://img.shields.io/github/stars/0xshoriful/CVE-2024-10470.svg) ![forks](https://img.shields.io/github/forks/0xshoriful/CVE-2024-10470.svg)

## CVE-2024-10449
 A vulnerability, which was classified as critical, was found in Codezips Hospital Appointment System 1.0. This affects an unknown part of the file /loginAction.php. The manipulation of the argument Username leads to sql injection. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used.



- [https://github.com/g-u-i-d/CVE-2024-10449-patch](https://github.com/g-u-i-d/CVE-2024-10449-patch) :  ![starts](https://img.shields.io/github/stars/g-u-i-d/CVE-2024-10449-patch.svg) ![forks](https://img.shields.io/github/forks/g-u-i-d/CVE-2024-10449-patch.svg)

## CVE-2024-10400
 The Tutor LMS plugin for WordPress is vulnerable to SQL Injection via the ‘rating_filter’ parameter in all versions up to, and including, 2.7.6 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/k0ns0l/CVE-2024-10400](https://github.com/k0ns0l/CVE-2024-10400) :  ![starts](https://img.shields.io/github/stars/k0ns0l/CVE-2024-10400.svg) ![forks](https://img.shields.io/github/forks/k0ns0l/CVE-2024-10400.svg)

## CVE-2024-10245
 The Relais 2FA plugin for WordPress is vulnerable to authentication bypass in versions up to, and including, 1.0. This is due to incorrect authentication and capability checking in the 'rl_do_ajax' function. This makes it possible for unauthenticated attackers to log in as any existing user on the site, such as an administrator, if they have access to the email.



- [https://github.com/RandomRobbieBF/CVE-2024-10245](https://github.com/RandomRobbieBF/CVE-2024-10245) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-10245.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-10245.svg)

## CVE-2024-10220
 The Kubernetes kubelet component allows arbitrary command execution via specially crafted gitRepo volumes.This issue affects kubelet: through 1.28.11, from 1.29.0 through 1.29.6, from 1.30.0 through 1.30.2.



- [https://github.com/XiaomingX/cve-2024-10220-githooks](https://github.com/XiaomingX/cve-2024-10220-githooks) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-10220-githooks.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-10220-githooks.svg)

- [https://github.com/mochizuki875/CVE-2024-10220-githooks](https://github.com/mochizuki875/CVE-2024-10220-githooks) :  ![starts](https://img.shields.io/github/stars/mochizuki875/CVE-2024-10220-githooks.svg) ![forks](https://img.shields.io/github/forks/mochizuki875/CVE-2024-10220-githooks.svg)

- [https://github.com/candranapits/poc-CVE-2024-10220](https://github.com/candranapits/poc-CVE-2024-10220) :  ![starts](https://img.shields.io/github/stars/candranapits/poc-CVE-2024-10220.svg) ![forks](https://img.shields.io/github/forks/candranapits/poc-CVE-2024-10220.svg)

- [https://github.com/filipzag/CVE-2024-10220](https://github.com/filipzag/CVE-2024-10220) :  ![starts](https://img.shields.io/github/stars/filipzag/CVE-2024-10220.svg) ![forks](https://img.shields.io/github/forks/filipzag/CVE-2024-10220.svg)

- [https://github.com/any2sec/cve-2024-10220](https://github.com/any2sec/cve-2024-10220) :  ![starts](https://img.shields.io/github/stars/any2sec/cve-2024-10220.svg) ![forks](https://img.shields.io/github/forks/any2sec/cve-2024-10220.svg)

- [https://github.com/orgC/CVE-2024-10220-demo](https://github.com/orgC/CVE-2024-10220-demo) :  ![starts](https://img.shields.io/github/stars/orgC/CVE-2024-10220-demo.svg) ![forks](https://img.shields.io/github/forks/orgC/CVE-2024-10220-demo.svg)

## CVE-2024-10124
 The Vayu Blocks – Gutenberg Blocks for WordPress & WooCommerce plugin for WordPress is vulnerable to unauthorized arbitrary plugin installation and activation due to a missing capability check on the tp_install() function in all versions up to, and including, 1.1.1. This makes it possible for unauthenticated attackers to install and activate arbitrary plugins which can be leveraged to achieve remote code execution if another vulnerable plugin is installed and activated. This vulnerability was partially patched in version 1.1.1.



- [https://github.com/Nxploited/CVE-2024-10124-Poc](https://github.com/Nxploited/CVE-2024-10124-Poc) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-10124-Poc.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-10124-Poc.svg)

- [https://github.com/RandomRobbieBF/CVE-2024-10124](https://github.com/RandomRobbieBF/CVE-2024-10124) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-10124.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-10124.svg)

## CVE-2024-9950
 A vulnerability in Forescout SecureConnector v11.3.07.0109 on Windows allows 

unauthenticated user to modify compliance scripts due to insecure temporary directory.



- [https://github.com/0Nightsedge0/CVE-2024-9950-PoC](https://github.com/0Nightsedge0/CVE-2024-9950-PoC) :  ![starts](https://img.shields.io/github/stars/0Nightsedge0/CVE-2024-9950-PoC.svg) ![forks](https://img.shields.io/github/forks/0Nightsedge0/CVE-2024-9950-PoC.svg)

## CVE-2024-9935
 The PDF Generator Addon for Elementor Page Builder plugin for WordPress is vulnerable to Path Traversal in all versions up to, and including, 1.7.5 via the rtw_pgaepb_dwnld_pdf() function. This makes it possible for unauthenticated attackers to read the contents of arbitrary files on the server, which can contain sensitive information.



- [https://github.com/verylazytech/CVE-2024-9935](https://github.com/verylazytech/CVE-2024-9935) :  ![starts](https://img.shields.io/github/stars/verylazytech/CVE-2024-9935.svg) ![forks](https://img.shields.io/github/forks/verylazytech/CVE-2024-9935.svg)

- [https://github.com/RandomRobbieBF/CVE-2024-9935](https://github.com/RandomRobbieBF/CVE-2024-9935) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-9935.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-9935.svg)

- [https://github.com/Nxploited/CVE-2024-9935](https://github.com/Nxploited/CVE-2024-9935) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-9935.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-9935.svg)

## CVE-2024-9933
 The WatchTowerHQ plugin for WordPress is vulnerable to authentication bypass in versions up to, and including, 3.9.6. This is due to the 'watchtower_ota_token' default value is empty, and the not empty check is missing in the 'Password_Less_Access::login' function. This makes it possible for unauthenticated attackers to log in to the WatchTowerHQ client administrator user.



- [https://github.com/Nxploited/CVE-2024-9933](https://github.com/Nxploited/CVE-2024-9933) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-9933.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-9933.svg)

- [https://github.com/RandomRobbieBF/CVE-2024-9933](https://github.com/RandomRobbieBF/CVE-2024-9933) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-9933.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-9933.svg)

## CVE-2024-9932
 The Wux Blog Editor plugin for WordPress is vulnerable to arbitrary file uploads due to insufficient file type validation in the 'wuxbt_insertImageNew' function in versions up to, and including, 3.0.0. This makes it possible for unauthenticated attackers to upload arbitrary files on the affected site's server which may make remote code execution possible.



- [https://github.com/RandomRobbieBF/CVE-2024-9932](https://github.com/RandomRobbieBF/CVE-2024-9932) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-9932.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-9932.svg)

- [https://github.com/Nxploited/CVE-2024-9932-POC](https://github.com/Nxploited/CVE-2024-9932-POC) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-9932-POC.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-9932-POC.svg)

## CVE-2024-9890
 The User Toolkit plugin for WordPress is vulnerable to authentication bypass in versions up to, and including, 1.2.3. This is due to an improper capability check in the 'switchUser' function. This makes it possible for authenticated attackers, with subscriber-level permissions and above, to log in as any existing user on the site, such as an administrator.



- [https://github.com/RandomRobbieBF/CVE-2024-9890](https://github.com/RandomRobbieBF/CVE-2024-9890) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-9890.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-9890.svg)

## CVE-2024-9796
 The WP-Advanced-Search WordPress plugin before 3.3.9.2 does not sanitize and escape the t parameter before using it in a SQL statement, allowing unauthenticated users to perform SQL injection attacks



- [https://github.com/issamjr/CVE-2024-9796](https://github.com/issamjr/CVE-2024-9796) :  ![starts](https://img.shields.io/github/stars/issamjr/CVE-2024-9796.svg) ![forks](https://img.shields.io/github/forks/issamjr/CVE-2024-9796.svg)

## CVE-2024-9707
 The Hunk Companion plugin for WordPress is vulnerable to unauthorized plugin installation/activation due to a missing capability check on the /wp-json/hc/v1/themehunk-import REST API endpoint in all versions up to, and including, 1.8.4. This makes it possible for unauthenticated attackers to install and activate arbitrary plugins which can be leveraged to achieve remote code execution if another vulnerable plugin is installed and activated.



- [https://github.com/Nxploited/CVE-2024-9707-Poc](https://github.com/Nxploited/CVE-2024-9707-Poc) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-9707-Poc.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-9707-Poc.svg)

## CVE-2024-9680
 An attacker was able to achieve code execution in the content process by exploiting a use-after-free in Animation timelines. We have had reports of this vulnerability being exploited in the wild. This vulnerability affects Firefox  131.0.2, Firefox ESR  128.3.1, Firefox ESR  115.16.1, Thunderbird  131.0.1, Thunderbird  128.3.1, and Thunderbird  115.16.0.



- [https://github.com/PraiseImafidon/Version_Vulnerability_Scanner](https://github.com/PraiseImafidon/Version_Vulnerability_Scanner) :  ![starts](https://img.shields.io/github/stars/PraiseImafidon/Version_Vulnerability_Scanner.svg) ![forks](https://img.shields.io/github/forks/PraiseImafidon/Version_Vulnerability_Scanner.svg)

## CVE-2024-9593
 The Time Clock plugin and Time Clock Pro plugin for WordPress are vulnerable to Remote Code Execution in versions up to, and including, 1.2.2 (for Time Clock) and 1.1.4 (for Time Clock Pro) via the 'etimeclockwp_load_function_callback' function. This allows unauthenticated attackers to execute code on the server. The invoked function's parameters cannot be specified.



- [https://github.com/0x4f5da2-venom/CVE-2024-9593-EXP](https://github.com/0x4f5da2-venom/CVE-2024-9593-EXP) :  ![starts](https://img.shields.io/github/stars/0x4f5da2-venom/CVE-2024-9593-EXP.svg) ![forks](https://img.shields.io/github/forks/0x4f5da2-venom/CVE-2024-9593-EXP.svg)

- [https://github.com/Nxploited/CVE-2024-9593-Exploit](https://github.com/Nxploited/CVE-2024-9593-Exploit) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-9593-Exploit.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-9593-Exploit.svg)

## CVE-2024-9506
 Improper regular expression in Vue's parseHTML function leads to a potential regular expression denial of service vulnerability.



- [https://github.com/bio/vue-template-compiler-patched](https://github.com/bio/vue-template-compiler-patched) :  ![starts](https://img.shields.io/github/stars/bio/vue-template-compiler-patched.svg) ![forks](https://img.shields.io/github/forks/bio/vue-template-compiler-patched.svg)

## CVE-2024-9474
 A privilege escalation vulnerability in Palo Alto Networks PAN-OS software allows a PAN-OS administrator with access to the management web interface to perform actions on the firewall with root privileges.

Cloud NGFW and Prisma Access are not impacted by this vulnerability.



- [https://github.com/Chocapikk/CVE-2024-9474](https://github.com/Chocapikk/CVE-2024-9474) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-9474.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-9474.svg)

- [https://github.com/k4nfr3/CVE-2024-9474](https://github.com/k4nfr3/CVE-2024-9474) :  ![starts](https://img.shields.io/github/stars/k4nfr3/CVE-2024-9474.svg) ![forks](https://img.shields.io/github/forks/k4nfr3/CVE-2024-9474.svg)

- [https://github.com/TalatumLabs/CVE-2024-0012_CVE-2024-9474_PoC](https://github.com/TalatumLabs/CVE-2024-0012_CVE-2024-9474_PoC) :  ![starts](https://img.shields.io/github/stars/TalatumLabs/CVE-2024-0012_CVE-2024-9474_PoC.svg) ![forks](https://img.shields.io/github/forks/TalatumLabs/CVE-2024-0012_CVE-2024-9474_PoC.svg)

- [https://github.com/XiaomingX/cve-2024-0012-poc](https://github.com/XiaomingX/cve-2024-0012-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-0012-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-0012-poc.svg)

- [https://github.com/coskper-papa/PAN-OS_CVE-2024-9474](https://github.com/coskper-papa/PAN-OS_CVE-2024-9474) :  ![starts](https://img.shields.io/github/stars/coskper-papa/PAN-OS_CVE-2024-9474.svg) ![forks](https://img.shields.io/github/forks/coskper-papa/PAN-OS_CVE-2024-9474.svg)

- [https://github.com/Regent8SH/PanOsExploitMultitool](https://github.com/Regent8SH/PanOsExploitMultitool) :  ![starts](https://img.shields.io/github/stars/Regent8SH/PanOsExploitMultitool.svg) ![forks](https://img.shields.io/github/forks/Regent8SH/PanOsExploitMultitool.svg)

- [https://github.com/deathvu/CVE-2024-9474](https://github.com/deathvu/CVE-2024-9474) :  ![starts](https://img.shields.io/github/stars/deathvu/CVE-2024-9474.svg) ![forks](https://img.shields.io/github/forks/deathvu/CVE-2024-9474.svg)

## CVE-2024-9465
 An SQL injection vulnerability in Palo Alto Networks Expedition allows an unauthenticated attacker to reveal Expedition database contents, such as password hashes, usernames, device configurations, and device API keys. With this, attackers can also create and read arbitrary files on the Expedition system.



- [https://github.com/XiaomingX/cve-2024-9465-poc](https://github.com/XiaomingX/cve-2024-9465-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-9465-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-9465-poc.svg)

## CVE-2024-9464
 An OS command injection vulnerability in Palo Alto Networks Expedition allows an authenticated attacker to run arbitrary OS commands as root in Expedition, resulting in disclosure of usernames, cleartext passwords, device configurations, and device API keys of PAN-OS firewalls.



- [https://github.com/p33d/Palo-Alto-Expedition-Remote-Code-Execution-Exploit-CVE-2024-5910-CVE-2024-9464](https://github.com/p33d/Palo-Alto-Expedition-Remote-Code-Execution-Exploit-CVE-2024-5910-CVE-2024-9464) :  ![starts](https://img.shields.io/github/stars/p33d/Palo-Alto-Expedition-Remote-Code-Execution-Exploit-CVE-2024-5910-CVE-2024-9464.svg) ![forks](https://img.shields.io/github/forks/p33d/Palo-Alto-Expedition-Remote-Code-Execution-Exploit-CVE-2024-5910-CVE-2024-9464.svg)

## CVE-2024-9463
 An OS command injection vulnerability in Palo Alto Networks Expedition allows an unauthenticated attacker to run arbitrary OS commands as root in Expedition, resulting in disclosure of usernames, cleartext passwords, device configurations, and device API keys of PAN-OS firewalls.



- [https://github.com/momo1239/CVE-2024-9463-Proof-of-Concept](https://github.com/momo1239/CVE-2024-9463-Proof-of-Concept) :  ![starts](https://img.shields.io/github/stars/momo1239/CVE-2024-9463-Proof-of-Concept.svg) ![forks](https://img.shields.io/github/forks/momo1239/CVE-2024-9463-Proof-of-Concept.svg)

## CVE-2024-9441
 The Linear eMerge e3-Series through version 1.00-07 is vulnerable to an OS command injection vulnerability. A remote and unauthenticated attacker can execute arbitrary OS commands via the login_id parameter when invoking the forgot_password functionality over HTTP.



- [https://github.com/XiaomingX/cve-2024-9441-poc](https://github.com/XiaomingX/cve-2024-9441-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-9441-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-9441-poc.svg)

- [https://github.com/jk-mayne/CVE-2024-9441-Checker](https://github.com/jk-mayne/CVE-2024-9441-Checker) :  ![starts](https://img.shields.io/github/stars/jk-mayne/CVE-2024-9441-Checker.svg) ![forks](https://img.shields.io/github/forks/jk-mayne/CVE-2024-9441-Checker.svg)

## CVE-2024-9326
 A vulnerability classified as critical was found in PHPGurukul Online Shopping Portal 2.0. This vulnerability affects unknown code of the file /shopping/admin/index.php of the component Admin Panel. The manipulation of the argument username leads to sql injection. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used.



- [https://github.com/ghostwirez/CVE-2024-9326-PoC](https://github.com/ghostwirez/CVE-2024-9326-PoC) :  ![starts](https://img.shields.io/github/stars/ghostwirez/CVE-2024-9326-PoC.svg) ![forks](https://img.shields.io/github/forks/ghostwirez/CVE-2024-9326-PoC.svg)

## CVE-2024-9290
 The Super Backup & Clone - Migrate for WordPress plugin for WordPress is vulnerable to arbitrary file uploads due to missing file type validation and a missing capability check on the ibk_restore_migrate_check() function in all versions up to, and including, 2.3.3. This makes it possible for unauthenticated attackers to upload arbitrary files on the affected site's server which may make remote code execution possible.



- [https://github.com/Jenderal92/CVE-2024-9290](https://github.com/Jenderal92/CVE-2024-9290) :  ![starts](https://img.shields.io/github/stars/Jenderal92/CVE-2024-9290.svg) ![forks](https://img.shields.io/github/forks/Jenderal92/CVE-2024-9290.svg)

- [https://github.com/RandomRobbieBF/CVE-2024-9290](https://github.com/RandomRobbieBF/CVE-2024-9290) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-9290.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-9290.svg)

## CVE-2024-9264
 The SQL Expressions experimental feature of Grafana allows for the evaluation of `duckdb` queries containing user input. These queries are insufficiently sanitized before being passed to `duckdb`, leading to a command injection and local file inclusion vulnerability. Any user with the VIEWER or higher permission is capable of executing this attack.  The `duckdb` binary must be present in Grafana's $PATH for this attack to function; by default, this binary is not installed in Grafana distributions.



- [https://github.com/Cythonic1/CVE-2024-9264](https://github.com/Cythonic1/CVE-2024-9264) :  ![starts](https://img.shields.io/github/stars/Cythonic1/CVE-2024-9264.svg) ![forks](https://img.shields.io/github/forks/Cythonic1/CVE-2024-9264.svg)

- [https://github.com/rvizx/CVE-2024-9264](https://github.com/rvizx/CVE-2024-9264) :  ![starts](https://img.shields.io/github/stars/rvizx/CVE-2024-9264.svg) ![forks](https://img.shields.io/github/forks/rvizx/CVE-2024-9264.svg)

- [https://github.com/ruizii/CVE-2024-9264](https://github.com/ruizii/CVE-2024-9264) :  ![starts](https://img.shields.io/github/stars/ruizii/CVE-2024-9264.svg) ![forks](https://img.shields.io/github/forks/ruizii/CVE-2024-9264.svg)

- [https://github.com/Royall-Researchers/CVE-2024-9264](https://github.com/Royall-Researchers/CVE-2024-9264) :  ![starts](https://img.shields.io/github/stars/Royall-Researchers/CVE-2024-9264.svg) ![forks](https://img.shields.io/github/forks/Royall-Researchers/CVE-2024-9264.svg)

- [https://github.com/patrickpichler/grafana-CVE-2024-9264](https://github.com/patrickpichler/grafana-CVE-2024-9264) :  ![starts](https://img.shields.io/github/stars/patrickpichler/grafana-CVE-2024-9264.svg) ![forks](https://img.shields.io/github/forks/patrickpichler/grafana-CVE-2024-9264.svg)

## CVE-2024-9234
 The GutenKit – Page Builder Blocks, Patterns, and Templates for Gutenberg Block Editor plugin for WordPress is vulnerable to arbitrary file uploads due to a missing capability check on the install_and_activate_plugin_from_external() function  (install-active-plugin REST API endpoint) in all versions up to, and including, 2.1.0. This makes it possible for unauthenticated attackers to install and activate arbitrary plugins, or utilize the functionality to upload arbitrary files spoofed like plugins.



- [https://github.com/Nxploited/CVE-2024-9234](https://github.com/Nxploited/CVE-2024-9234) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-9234.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-9234.svg)

- [https://github.com/CallMeBatosay/CVE-2024-9234](https://github.com/CallMeBatosay/CVE-2024-9234) :  ![starts](https://img.shields.io/github/stars/CallMeBatosay/CVE-2024-9234.svg) ![forks](https://img.shields.io/github/forks/CallMeBatosay/CVE-2024-9234.svg)

## CVE-2024-9047
 The WordPress File Upload plugin for WordPress is vulnerable to Path Traversal in all versions up to, and including, 4.24.11 via wfu_file_downloader.php. This makes it possible for unauthenticated attackers to read or delete files outside of the originally intended directory. Successful exploitation requires the targeted WordPress installation to be using PHP 7.4 or earlier.



- [https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance](https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance) :  ![starts](https://img.shields.io/github/stars/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg) ![forks](https://img.shields.io/github/forks/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg)

- [https://github.com/verylazytech/CVE-2024-9047](https://github.com/verylazytech/CVE-2024-9047) :  ![starts](https://img.shields.io/github/stars/verylazytech/CVE-2024-9047.svg) ![forks](https://img.shields.io/github/forks/verylazytech/CVE-2024-9047.svg)

- [https://github.com/iSee857/CVE-2024-9047-PoC](https://github.com/iSee857/CVE-2024-9047-PoC) :  ![starts](https://img.shields.io/github/stars/iSee857/CVE-2024-9047-PoC.svg) ![forks](https://img.shields.io/github/forks/iSee857/CVE-2024-9047-PoC.svg)

## CVE-2024-9014
 pgAdmin versions 8.11 and earlier are vulnerable to a security flaw in OAuth2 authentication. This vulnerability allows an attacker to potentially obtain the client ID and secret, leading to unauthorized access to user data.



- [https://github.com/r0otk3r/CVE-2024-9014](https://github.com/r0otk3r/CVE-2024-9014) :  ![starts](https://img.shields.io/github/stars/r0otk3r/CVE-2024-9014.svg) ![forks](https://img.shields.io/github/forks/r0otk3r/CVE-2024-9014.svg)

## CVE-2024-8963
 Path Traversal in the Ivanti CSA before 4.6 Patch 519 allows a remote unauthenticated attacker to access restricted functionality.



- [https://github.com/patfire94/CVE-2024-8963](https://github.com/patfire94/CVE-2024-8963) :  ![starts](https://img.shields.io/github/stars/patfire94/CVE-2024-8963.svg) ![forks](https://img.shields.io/github/forks/patfire94/CVE-2024-8963.svg)

## CVE-2024-8868
 A vulnerability was found in code-projects Crud Operation System 1.0. It has been rated as critical. This issue affects some unknown processing of the file savedata.php. The manipulation of the argument sname leads to sql injection. The attack may be initiated remotely. The exploit has been disclosed to the public and may be used.



- [https://github.com/M0onc/CVE-2024-8868](https://github.com/M0onc/CVE-2024-8868) :  ![starts](https://img.shields.io/github/stars/M0onc/CVE-2024-8868.svg) ![forks](https://img.shields.io/github/forks/M0onc/CVE-2024-8868.svg)

## CVE-2024-8856
 The Backup and Staging by WP Time Capsule plugin for WordPress is vulnerable to arbitrary file uploads due to missing file type validation in the the UploadHandler.php file and no direct file access prevention in all versions up to, and including, 1.22.21. This makes it possible for unauthenticated attackers to upload arbitrary files on the affected site's server which may make remote code execution possible.



- [https://github.com/ubaydev/CVE-2024-8856](https://github.com/ubaydev/CVE-2024-8856) :  ![starts](https://img.shields.io/github/stars/ubaydev/CVE-2024-8856.svg) ![forks](https://img.shields.io/github/forks/ubaydev/CVE-2024-8856.svg)

- [https://github.com/Jenderal92/CVE-2024-8856](https://github.com/Jenderal92/CVE-2024-8856) :  ![starts](https://img.shields.io/github/stars/Jenderal92/CVE-2024-8856.svg) ![forks](https://img.shields.io/github/forks/Jenderal92/CVE-2024-8856.svg)

## CVE-2024-8743
 The Bit File Manager – 100% Free & Open Source File Manager and Code Editor for WordPress plugin for WordPress is vulnerable to Limited JavaScript File Upload in all versions up to, and including, 6.5.7. This is due to a lack of proper checks on allowed file types. This makes it possible for authenticated attackers, with Subscriber-level access and above, and granted permissions by an administrator, to upload .css and .js files, which could lead to Stored Cross-Site Scripting.



- [https://github.com/siunam321/CVE-2024-8743-PoC](https://github.com/siunam321/CVE-2024-8743-PoC) :  ![starts](https://img.shields.io/github/stars/siunam321/CVE-2024-8743-PoC.svg) ![forks](https://img.shields.io/github/forks/siunam321/CVE-2024-8743-PoC.svg)

## CVE-2024-8682
 The JNews - WordPress Newspaper Magazine Blog AMP Theme theme for WordPress is vulnerable to unauthorized user registration in all versions up to, and including, 11.6.6. This is due to the plugin not properly validate if the user can register option is enabled prior to creating a user though the register_handler() function. This makes it possible for unauthenticated attackers to register as a user even when user registration is disabled.



- [https://github.com/4minx/CVE-2024-8682](https://github.com/4minx/CVE-2024-8682) :  ![starts](https://img.shields.io/github/stars/4minx/CVE-2024-8682.svg) ![forks](https://img.shields.io/github/forks/4minx/CVE-2024-8682.svg)

## CVE-2024-8672
 The Widget Options – The #1 WordPress Widget & Block Control Plugin plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, 4.0.7 via the display logic functionality that extends several page builders. This is due to the plugin allowing users to supply input that will be passed through eval() without any filtering or capability checks. This makes it possible for authenticated attackers, with contributor-level access and above, to execute code on the server. Special note: We suggested the vendor implement an allowlist of functions and limit the ability to execute commands to just administrators, however, they did not take our advice. We are considering this patched, however, we believe it could still be further hardened and there may be residual risk with how the issue is currently patched.



- [https://github.com/Chocapikk/CVE-2024-8672](https://github.com/Chocapikk/CVE-2024-8672) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-8672.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-8672.svg)

## CVE-2024-8636
 Heap buffer overflow in Skia in Google Chrome prior to 128.0.6613.137 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/HyHy100/Chrome-Skia-CVE-2024-8636](https://github.com/HyHy100/Chrome-Skia-CVE-2024-8636) :  ![starts](https://img.shields.io/github/stars/HyHy100/Chrome-Skia-CVE-2024-8636.svg) ![forks](https://img.shields.io/github/forks/HyHy100/Chrome-Skia-CVE-2024-8636.svg)

## CVE-2024-8517
 SPIP before 4.3.2, 4.2.16, and 
4.1.18 is vulnerable to a command injection issue. A 
remote and unauthenticated attacker can execute arbitrary operating system commands by sending a crafted multipart file upload HTTP request.



- [https://github.com/saadhassan77/SPIP-BigUp-Unauthenticated-RCE-Exploit-CVE-2024-8517](https://github.com/saadhassan77/SPIP-BigUp-Unauthenticated-RCE-Exploit-CVE-2024-8517) :  ![starts](https://img.shields.io/github/stars/saadhassan77/SPIP-BigUp-Unauthenticated-RCE-Exploit-CVE-2024-8517.svg) ![forks](https://img.shields.io/github/forks/saadhassan77/SPIP-BigUp-Unauthenticated-RCE-Exploit-CVE-2024-8517.svg)

## CVE-2024-8425
 The WooCommerce Ultimate Gift Card plugin for WordPress is vulnerable to arbitrary file uploads due to insufficient file type validation in the 'mwb_wgm_preview_mail' and 'mwb_wgm_woocommerce_add_cart_item_data' functions in all versions up to, and including, 2.6.0. This makes it possible for unauthenticated attackers to upload arbitrary files on the affected site's server which may make remote code execution possible.



- [https://github.com/KTN1990/CVE-2024-8425](https://github.com/KTN1990/CVE-2024-8425) :  ![starts](https://img.shields.io/github/stars/KTN1990/CVE-2024-8425.svg) ![forks](https://img.shields.io/github/forks/KTN1990/CVE-2024-8425.svg)

## CVE-2024-8198
 Heap buffer overflow in Skia in Google Chrome prior to 128.0.6613.113 allowed a remote attacker who had compromised the renderer process to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/HyHy100/Chrome-Skia-CVE-2024-8198](https://github.com/HyHy100/Chrome-Skia-CVE-2024-8198) :  ![starts](https://img.shields.io/github/stars/HyHy100/Chrome-Skia-CVE-2024-8198.svg) ![forks](https://img.shields.io/github/forks/HyHy100/Chrome-Skia-CVE-2024-8198.svg)

## CVE-2024-8193
 Heap buffer overflow in Skia in Google Chrome prior to 128.0.6613.113 allowed a remote attacker who had compromised the renderer process to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/HyHy100/Chrome-Skia-CVE-2024-8193](https://github.com/HyHy100/Chrome-Skia-CVE-2024-8193) :  ![starts](https://img.shields.io/github/stars/HyHy100/Chrome-Skia-CVE-2024-8193.svg) ![forks](https://img.shields.io/github/forks/HyHy100/Chrome-Skia-CVE-2024-8193.svg)

## CVE-2024-8176
 A stack overflow vulnerability exists in the libexpat library due to the way it handles recursive entity expansion in XML documents. When parsing an XML document with deeply nested entity references, libexpat can be forced to recurse indefinitely, exhausting the stack space and causing a crash. This issue could lead to denial of service (DoS) or, in some cases, exploitable memory corruption, depending on the environment and library usage.



- [https://github.com/uthrasri/Expat_2.6.2_CVE-2024-8176](https://github.com/uthrasri/Expat_2.6.2_CVE-2024-8176) :  ![starts](https://img.shields.io/github/stars/uthrasri/Expat_2.6.2_CVE-2024-8176.svg) ![forks](https://img.shields.io/github/forks/uthrasri/Expat_2.6.2_CVE-2024-8176.svg)

## CVE-2024-8118
 In Grafana, the wrong permission is applied to the alert rule write API endpoint, allowing users with permission to write external alert instances to also write alert rules.



- [https://github.com/nurarifin05/POC-CVE-2024-8118](https://github.com/nurarifin05/POC-CVE-2024-8118) :  ![starts](https://img.shields.io/github/stars/nurarifin05/POC-CVE-2024-8118.svg) ![forks](https://img.shields.io/github/forks/nurarifin05/POC-CVE-2024-8118.svg)

## CVE-2024-8069
 Limited remote code execution with privilege of a NetworkService Account access in Citrix Session Recording if the attacker is an authenticated user on the same intranet as the session recording server



- [https://github.com/XiaomingX/cve-2024-8069-exp-Citrix-Virtual-Apps-XEN](https://github.com/XiaomingX/cve-2024-8069-exp-Citrix-Virtual-Apps-XEN) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-8069-exp-Citrix-Virtual-Apps-XEN.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-8069-exp-Citrix-Virtual-Apps-XEN.svg)

## CVE-2024-7971
 Type confusion in V8 in Google Chrome prior to 128.0.6613.84 allowed a remote attacker to exploit heap corruption via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/mistymntncop/CVE-2024-7971](https://github.com/mistymntncop/CVE-2024-7971) :  ![starts](https://img.shields.io/github/stars/mistymntncop/CVE-2024-7971.svg) ![forks](https://img.shields.io/github/forks/mistymntncop/CVE-2024-7971.svg)

## CVE-2024-7966
 Out of bounds memory access in Skia in Google Chrome prior to 128.0.6613.84 allowed a remote attacker who had compromised the renderer process to perform out of bounds memory access via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/HyHy100/Chrome-Skia-CVE-2024-7966](https://github.com/HyHy100/Chrome-Skia-CVE-2024-7966) :  ![starts](https://img.shields.io/github/stars/HyHy100/Chrome-Skia-CVE-2024-7966.svg) ![forks](https://img.shields.io/github/forks/HyHy100/Chrome-Skia-CVE-2024-7966.svg)

## CVE-2024-7965
 Inappropriate implementation in V8 in Google Chrome prior to 128.0.6613.84 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/XiaomingX/cve-2024-7965-poc](https://github.com/XiaomingX/cve-2024-7965-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-7965-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-7965-poc.svg)

## CVE-2024-7954
 The porte_plume plugin used by SPIP before 4.30-alpha2, 4.2.13, and 4.1.16 is vulnerable to an arbitrary code execution vulnerability. A remote and unauthenticated attacker can execute arbitrary PHP as the SPIP user by sending a crafted HTTP request.



- [https://github.com/Chocapikk/CVE-2024-7954](https://github.com/Chocapikk/CVE-2024-7954) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-7954.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-7954.svg)

- [https://github.com/0dayan0n/RCE_CVE-2024-7954-](https://github.com/0dayan0n/RCE_CVE-2024-7954-) :  ![starts](https://img.shields.io/github/stars/0dayan0n/RCE_CVE-2024-7954-.svg) ![forks](https://img.shields.io/github/forks/0dayan0n/RCE_CVE-2024-7954-.svg)

- [https://github.com/issamjr/CVE-2024-7954](https://github.com/issamjr/CVE-2024-7954) :  ![starts](https://img.shields.io/github/stars/issamjr/CVE-2024-7954.svg) ![forks](https://img.shields.io/github/forks/issamjr/CVE-2024-7954.svg)

- [https://github.com/r0otk3r/CVE-2024-7954](https://github.com/r0otk3r/CVE-2024-7954) :  ![starts](https://img.shields.io/github/stars/r0otk3r/CVE-2024-7954.svg) ![forks](https://img.shields.io/github/forks/r0otk3r/CVE-2024-7954.svg)

- [https://github.com/zxj-hub/CVE-2024-7954POC](https://github.com/zxj-hub/CVE-2024-7954POC) :  ![starts](https://img.shields.io/github/stars/zxj-hub/CVE-2024-7954POC.svg) ![forks](https://img.shields.io/github/forks/zxj-hub/CVE-2024-7954POC.svg)

## CVE-2024-7808
 A vulnerability was found in code-projects Job Portal 1.0. It has been classified as critical. Affected is an unknown function of the file logindbc.php. The manipulation of the argument email leads to sql injection. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used.



- [https://github.com/TheUnknownSoul/CVE-2024-7808](https://github.com/TheUnknownSoul/CVE-2024-7808) :  ![starts](https://img.shields.io/github/stars/TheUnknownSoul/CVE-2024-7808.svg) ![forks](https://img.shields.io/github/forks/TheUnknownSoul/CVE-2024-7808.svg)

## CVE-2024-7627
 The Bit File Manager plugin for WordPress is vulnerable to Remote Code Execution in versions 6.0 to 6.5.5 via the 'checkSyntax' function. This is due to writing a temporary file to a publicly accessible directory before performing file validation. This makes it possible for unauthenticated attackers to execute code on the server if an administrator has allowed Guest User read permissions.



- [https://github.com/siunam321/CVE-2024-7627-PoC](https://github.com/siunam321/CVE-2024-7627-PoC) :  ![starts](https://img.shields.io/github/stars/siunam321/CVE-2024-7627-PoC.svg) ![forks](https://img.shields.io/github/forks/siunam321/CVE-2024-7627-PoC.svg)

## CVE-2024-7399
 Improper limitation of a pathname to a restricted directory vulnerability in Samsung MagicINFO 9 Server version before 21.1050 allows attackers to write arbitrary file as system authority.



- [https://github.com/davidxbors/CVE-2024-7399-POC](https://github.com/davidxbors/CVE-2024-7399-POC) :  ![starts](https://img.shields.io/github/stars/davidxbors/CVE-2024-7399-POC.svg) ![forks](https://img.shields.io/github/forks/davidxbors/CVE-2024-7399-POC.svg)

## CVE-2024-7339
 A vulnerability has been found in TVT DVR TD-2104TS-CL, DVR TD-2108TS-HP, Provision-ISR DVR SH-4050A5-5L(MM) and AVISION DVR AV108T and classified as problematic. This vulnerability affects unknown code of the file /queryDevInfo. The manipulation leads to information disclosure. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. VDB-273262 is the identifier assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/RevoltSecurities/CVE-2024-7339](https://github.com/RevoltSecurities/CVE-2024-7339) :  ![starts](https://img.shields.io/github/stars/RevoltSecurities/CVE-2024-7339.svg) ![forks](https://img.shields.io/github/forks/RevoltSecurities/CVE-2024-7339.svg)

## CVE-2024-7135
 The Tainacan plugin for WordPress is vulnerable to unauthorized access of data due to a missing capability check on the 'get_file' function in all versions up to, and including, 0.21.7. The function is also vulnerable to directory traversal. This makes it possible for authenticated attackers, with Subscriber-level access and above, to read the contents of arbitrary files on the server, which can contain sensitive information.



- [https://github.com/Nxploited/CVE-2024-7135](https://github.com/Nxploited/CVE-2024-7135) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-7135.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-7135.svg)

## CVE-2024-7124
 Improper Neutralization of Input During Web Page Generation vulnerability in DInGO dLibra software in the parameter 'filter' in the endpoint 'indexsearch' allows a Reflected Cross-Site Scripting (XSS). An attacker might trick somebody into using a crafted URL, which will cause a script to be run in user's browser. This issue affects DInGO dLibra software in versions from 6.0 before 6.3.20.



- [https://github.com/kac89/CVE-2024-7124](https://github.com/kac89/CVE-2024-7124) :  ![starts](https://img.shields.io/github/stars/kac89/CVE-2024-7124.svg) ![forks](https://img.shields.io/github/forks/kac89/CVE-2024-7124.svg)

## CVE-2024-7120
 A vulnerability, which was classified as critical, was found in Raisecom MSG1200, MSG2100E, MSG2200 and MSG2300 3.90. This affects an unknown part of the file list_base_config.php of the component Web Interface. The manipulation of the argument template leads to os command injection. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-272451.



- [https://github.com/jokeir07x/CVE-2024-7120-Exploit-by-Dark-07x](https://github.com/jokeir07x/CVE-2024-7120-Exploit-by-Dark-07x) :  ![starts](https://img.shields.io/github/stars/jokeir07x/CVE-2024-7120-Exploit-by-Dark-07x.svg) ![forks](https://img.shields.io/github/forks/jokeir07x/CVE-2024-7120-Exploit-by-Dark-07x.svg)

## CVE-2024-6783
 A vulnerability has been discovered in Vue, that allows an attacker to perform XSS via prototype pollution. The attacker could change the prototype chain of some properties such as `Object.prototype.staticClass` or `Object.prototype.staticStyle` to execute arbitrary JavaScript code.



- [https://github.com/bio/vue-template-compiler-patched](https://github.com/bio/vue-template-compiler-patched) :  ![starts](https://img.shields.io/github/stars/bio/vue-template-compiler-patched.svg) ![forks](https://img.shields.io/github/forks/bio/vue-template-compiler-patched.svg)

## CVE-2024-6782
 Improper access control in Calibre 6.9.0 ~ 7.14.0 allow unauthenticated attackers to achieve remote code execution.



- [https://github.com/zangjiahe/CVE-2024-6782](https://github.com/zangjiahe/CVE-2024-6782) :  ![starts](https://img.shields.io/github/stars/zangjiahe/CVE-2024-6782.svg) ![forks](https://img.shields.io/github/forks/zangjiahe/CVE-2024-6782.svg)

- [https://github.com/NketiahGodfred/CVE-2024-6782](https://github.com/NketiahGodfred/CVE-2024-6782) :  ![starts](https://img.shields.io/github/stars/NketiahGodfred/CVE-2024-6782.svg) ![forks](https://img.shields.io/github/forks/NketiahGodfred/CVE-2024-6782.svg)

- [https://github.com/jdpsl/CVE-2024-6782](https://github.com/jdpsl/CVE-2024-6782) :  ![starts](https://img.shields.io/github/stars/jdpsl/CVE-2024-6782.svg) ![forks](https://img.shields.io/github/forks/jdpsl/CVE-2024-6782.svg)

## CVE-2024-6768
 A Denial of Service in CLFS.sys in Microsoft Windows 10, Windows 11, Windows Server 2016, Windows Server 2019, and Windows Server 2022 allows a malicious authenticated low-privilege user to cause a Blue Screen of Death via a forced call to the KeBugCheckEx function.



- [https://github.com/fortra/CVE-2024-6768](https://github.com/fortra/CVE-2024-6768) :  ![starts](https://img.shields.io/github/stars/fortra/CVE-2024-6768.svg) ![forks](https://img.shields.io/github/forks/fortra/CVE-2024-6768.svg)

## CVE-2024-6648
 Absolute Path Traversal vulnerability in AP Page Builder versions prior to 4.0.0 could allow an unauthenticated remote user to modify the 'product_item_path' within the 'config' JSON file, allowing them to read any file on the system.



- [https://github.com/n0d0n/CVE-2024-6648](https://github.com/n0d0n/CVE-2024-6648) :  ![starts](https://img.shields.io/github/stars/n0d0n/CVE-2024-6648.svg) ![forks](https://img.shields.io/github/forks/n0d0n/CVE-2024-6648.svg)

## CVE-2024-6536
 The Zephyr Project Manager WordPress plugin before 3.3.99 does not sanitise and escape some of its settings, which could allow high privilege users such as editors and admins to perform Stored Cross-Site Scripting attacks even when the unfiltered_html capability is disallowed (for example in multisite setup)



- [https://github.com/apena-ba/CVE-2024-6536](https://github.com/apena-ba/CVE-2024-6536) :  ![starts](https://img.shields.io/github/stars/apena-ba/CVE-2024-6536.svg) ![forks](https://img.shields.io/github/forks/apena-ba/CVE-2024-6536.svg)

## CVE-2024-6529
 The Ultimate Classified Listings WordPress plugin before 1.4 does not sanitise and escape a parameter before outputting it back in the page, leading to a Reflected Cross-Site Scripting which could be used against high privilege users such as admin



- [https://github.com/Abdurahmon3236/CVE-2024-6529](https://github.com/Abdurahmon3236/CVE-2024-6529) :  ![starts](https://img.shields.io/github/stars/Abdurahmon3236/CVE-2024-6529.svg) ![forks](https://img.shields.io/github/forks/Abdurahmon3236/CVE-2024-6529.svg)

## CVE-2024-6523
 A vulnerability was found in ZKTeco BioTime up to 9.5.2. It has been classified as problematic. Affected is an unknown function of the component system-group-add Handler. The manipulation of the argument user with the input scriptalert('XSS')/script leads to cross site scripting. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. VDB-270366 is the identifier assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/CBaekhyunC/cve-2024-65230](https://github.com/CBaekhyunC/cve-2024-65230) :  ![starts](https://img.shields.io/github/stars/CBaekhyunC/cve-2024-65230.svg) ![forks](https://img.shields.io/github/forks/CBaekhyunC/cve-2024-65230.svg)

## CVE-2024-6485
 A security vulnerability has been discovered in bootstrap that could enable Cross-Site Scripting (XSS) attacks. The vulnerability is associated with the data-loading-text attribute within the button plugin. This vulnerability can be exploited by injecting malicious JavaScript code into the attribute, which would then be executed when the button's loading state is triggered.



- [https://github.com/Yumeae/Bootstrap-with-XSS](https://github.com/Yumeae/Bootstrap-with-XSS) :  ![starts](https://img.shields.io/github/stars/Yumeae/Bootstrap-with-XSS.svg) ![forks](https://img.shields.io/github/forks/Yumeae/Bootstrap-with-XSS.svg)

## CVE-2024-6409
 A race condition vulnerability was discovered in how signals are handled by OpenSSH's server (sshd). If a remote attacker does not authenticate within a set time period, then sshd's SIGALRM handler is called asynchronously. However, this signal handler calls various functions that are not async-signal-safe, for example, syslog(). As a consequence of a successful attack, in the worst case scenario, an attacker may be able to perform a remote code execution (RCE) as an unprivileged user running the sshd server.



- [https://github.com/password123456/cve-security-response-guidelines](https://github.com/password123456/cve-security-response-guidelines) :  ![starts](https://img.shields.io/github/stars/password123456/cve-security-response-guidelines.svg) ![forks](https://img.shields.io/github/forks/password123456/cve-security-response-guidelines.svg)

## CVE-2024-6387
 A security regression (CVE-2006-5051) was discovered in OpenSSH's server (sshd). There is a race condition which can lead sshd to handle some signals in an unsafe manner. An unauthenticated, remote attacker may be able to trigger it by failing to authenticate within a set time period.



- [https://github.com/xaitax/CVE-2024-6387_Check](https://github.com/xaitax/CVE-2024-6387_Check) :  ![starts](https://img.shields.io/github/stars/xaitax/CVE-2024-6387_Check.svg) ![forks](https://img.shields.io/github/forks/xaitax/CVE-2024-6387_Check.svg)

- [https://github.com/zgzhang/cve-2024-6387-poc](https://github.com/zgzhang/cve-2024-6387-poc) :  ![starts](https://img.shields.io/github/stars/zgzhang/cve-2024-6387-poc.svg) ![forks](https://img.shields.io/github/forks/zgzhang/cve-2024-6387-poc.svg)

- [https://github.com/acrono/cve-2024-6387-poc](https://github.com/acrono/cve-2024-6387-poc) :  ![starts](https://img.shields.io/github/stars/acrono/cve-2024-6387-poc.svg) ![forks](https://img.shields.io/github/forks/acrono/cve-2024-6387-poc.svg)

- [https://github.com/Karmakstylez/CVE-2024-6387](https://github.com/Karmakstylez/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/Karmakstylez/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/Karmakstylez/CVE-2024-6387.svg)

- [https://github.com/lflare/cve-2024-6387-poc](https://github.com/lflare/cve-2024-6387-poc) :  ![starts](https://img.shields.io/github/stars/lflare/cve-2024-6387-poc.svg) ![forks](https://img.shields.io/github/forks/lflare/cve-2024-6387-poc.svg)

- [https://github.com/filipi86/CVE-2024-6387-Vulnerability-Checker](https://github.com/filipi86/CVE-2024-6387-Vulnerability-Checker) :  ![starts](https://img.shields.io/github/stars/filipi86/CVE-2024-6387-Vulnerability-Checker.svg) ![forks](https://img.shields.io/github/forks/filipi86/CVE-2024-6387-Vulnerability-Checker.svg)

- [https://github.com/l0n3m4n/CVE-2024-6387](https://github.com/l0n3m4n/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/l0n3m4n/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/l0n3m4n/CVE-2024-6387.svg)

- [https://github.com/theaog/spirit](https://github.com/theaog/spirit) :  ![starts](https://img.shields.io/github/stars/theaog/spirit.svg) ![forks](https://img.shields.io/github/forks/theaog/spirit.svg)

- [https://github.com/xonoxitron/regreSSHion](https://github.com/xonoxitron/regreSSHion) :  ![starts](https://img.shields.io/github/stars/xonoxitron/regreSSHion.svg) ![forks](https://img.shields.io/github/forks/xonoxitron/regreSSHion.svg)

- [https://github.com/d0rb/CVE-2024-6387](https://github.com/d0rb/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2024-6387.svg)

- [https://github.com/bigb0x/CVE-2024-6387](https://github.com/bigb0x/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-6387.svg)

- [https://github.com/getdrive/CVE-2024-6387-PoC](https://github.com/getdrive/CVE-2024-6387-PoC) :  ![starts](https://img.shields.io/github/stars/getdrive/CVE-2024-6387-PoC.svg) ![forks](https://img.shields.io/github/forks/getdrive/CVE-2024-6387-PoC.svg)

- [https://github.com/thegenetic/CVE-2024-6387-exploit](https://github.com/thegenetic/CVE-2024-6387-exploit) :  ![starts](https://img.shields.io/github/stars/thegenetic/CVE-2024-6387-exploit.svg) ![forks](https://img.shields.io/github/forks/thegenetic/CVE-2024-6387-exploit.svg)

- [https://github.com/sxlmnwb/CVE-2024-6387](https://github.com/sxlmnwb/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/sxlmnwb/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/sxlmnwb/CVE-2024-6387.svg)

- [https://github.com/YassDEV221608/CVE-2024-6387_PoC](https://github.com/YassDEV221608/CVE-2024-6387_PoC) :  ![starts](https://img.shields.io/github/stars/YassDEV221608/CVE-2024-6387_PoC.svg) ![forks](https://img.shields.io/github/forks/YassDEV221608/CVE-2024-6387_PoC.svg)

- [https://github.com/devarshishimpi/CVE-2024-6387-Check](https://github.com/devarshishimpi/CVE-2024-6387-Check) :  ![starts](https://img.shields.io/github/stars/devarshishimpi/CVE-2024-6387-Check.svg) ![forks](https://img.shields.io/github/forks/devarshishimpi/CVE-2024-6387-Check.svg)

- [https://github.com/AiGptCode/ssh_exploiter_CVE-2024-6387](https://github.com/AiGptCode/ssh_exploiter_CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/AiGptCode/ssh_exploiter_CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/AiGptCode/ssh_exploiter_CVE-2024-6387.svg)

- [https://github.com/TAM-K592/CVE-2024-6387](https://github.com/TAM-K592/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/TAM-K592/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/TAM-K592/CVE-2024-6387.svg)

- [https://github.com/l-urk/CVE-2024-6387](https://github.com/l-urk/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/l-urk/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/l-urk/CVE-2024-6387.svg)

- [https://github.com/0x4D31/cve-2024-6387_hassh](https://github.com/0x4D31/cve-2024-6387_hassh) :  ![starts](https://img.shields.io/github/stars/0x4D31/cve-2024-6387_hassh.svg) ![forks](https://img.shields.io/github/forks/0x4D31/cve-2024-6387_hassh.svg)

- [https://github.com/xonoxitron/regreSSHion-checker](https://github.com/xonoxitron/regreSSHion-checker) :  ![starts](https://img.shields.io/github/stars/xonoxitron/regreSSHion-checker.svg) ![forks](https://img.shields.io/github/forks/xonoxitron/regreSSHion-checker.svg)

- [https://github.com/P4x1s/CVE-2024-6387](https://github.com/P4x1s/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/P4x1s/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/P4x1s/CVE-2024-6387.svg)

- [https://github.com/wiggels/regresshion-check](https://github.com/wiggels/regresshion-check) :  ![starts](https://img.shields.io/github/stars/wiggels/regresshion-check.svg) ![forks](https://img.shields.io/github/forks/wiggels/regresshion-check.svg)

- [https://github.com/kuffsit/check_cve_2024_6387](https://github.com/kuffsit/check_cve_2024_6387) :  ![starts](https://img.shields.io/github/stars/kuffsit/check_cve_2024_6387.svg) ![forks](https://img.shields.io/github/forks/kuffsit/check_cve_2024_6387.svg)

- [https://github.com/azurejoga/CVE-2024-6387-how-to-fix](https://github.com/azurejoga/CVE-2024-6387-how-to-fix) :  ![starts](https://img.shields.io/github/stars/azurejoga/CVE-2024-6387-how-to-fix.svg) ![forks](https://img.shields.io/github/forks/azurejoga/CVE-2024-6387-how-to-fix.svg)

- [https://github.com/paradessia/CVE-2024-6387-nmap](https://github.com/paradessia/CVE-2024-6387-nmap) :  ![starts](https://img.shields.io/github/stars/paradessia/CVE-2024-6387-nmap.svg) ![forks](https://img.shields.io/github/forks/paradessia/CVE-2024-6387-nmap.svg)

- [https://github.com/lala-amber/CVE-2024-6387](https://github.com/lala-amber/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/lala-amber/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/lala-amber/CVE-2024-6387.svg)

- [https://github.com/th3gokul/CVE-2024-6387](https://github.com/th3gokul/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/th3gokul/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/th3gokul/CVE-2024-6387.svg)

- [https://github.com/MaulikxLakhani/SSHScout](https://github.com/MaulikxLakhani/SSHScout) :  ![starts](https://img.shields.io/github/stars/MaulikxLakhani/SSHScout.svg) ![forks](https://img.shields.io/github/forks/MaulikxLakhani/SSHScout.svg)

- [https://github.com/awusan125/test_for6387](https://github.com/awusan125/test_for6387) :  ![starts](https://img.shields.io/github/stars/awusan125/test_for6387.svg) ![forks](https://img.shields.io/github/forks/awusan125/test_for6387.svg)

- [https://github.com/MrR0b0t19/CVE-2024-6387-Exploit-POC](https://github.com/MrR0b0t19/CVE-2024-6387-Exploit-POC) :  ![starts](https://img.shields.io/github/stars/MrR0b0t19/CVE-2024-6387-Exploit-POC.svg) ![forks](https://img.shields.io/github/forks/MrR0b0t19/CVE-2024-6387-Exploit-POC.svg)

- [https://github.com/BrandonLynch2402/cve-2024-6387-nuclei-template](https://github.com/BrandonLynch2402/cve-2024-6387-nuclei-template) :  ![starts](https://img.shields.io/github/stars/BrandonLynch2402/cve-2024-6387-nuclei-template.svg) ![forks](https://img.shields.io/github/forks/BrandonLynch2402/cve-2024-6387-nuclei-template.svg)

- [https://github.com/PrincipalAnthony/CVE-2024-6387-Updated-x64bit](https://github.com/PrincipalAnthony/CVE-2024-6387-Updated-x64bit) :  ![starts](https://img.shields.io/github/stars/PrincipalAnthony/CVE-2024-6387-Updated-x64bit.svg) ![forks](https://img.shields.io/github/forks/PrincipalAnthony/CVE-2024-6387-Updated-x64bit.svg)

- [https://github.com/harshinsecurity/sentinelssh](https://github.com/harshinsecurity/sentinelssh) :  ![starts](https://img.shields.io/github/stars/harshinsecurity/sentinelssh.svg) ![forks](https://img.shields.io/github/forks/harshinsecurity/sentinelssh.svg)

- [https://github.com/betancour/OpenSSH-Vulnerability-test](https://github.com/betancour/OpenSSH-Vulnerability-test) :  ![starts](https://img.shields.io/github/stars/betancour/OpenSSH-Vulnerability-test.svg) ![forks](https://img.shields.io/github/forks/betancour/OpenSSH-Vulnerability-test.svg)

- [https://github.com/prelearn-code/CVE-2024-6387](https://github.com/prelearn-code/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/prelearn-code/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/prelearn-code/CVE-2024-6387.svg)

- [https://github.com/Symbolexe/CVE-2024-6387](https://github.com/Symbolexe/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/Symbolexe/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/Symbolexe/CVE-2024-6387.svg)

- [https://github.com/ahlfors/CVE-2024-6387](https://github.com/ahlfors/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/ahlfors/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/ahlfors/CVE-2024-6387.svg)

- [https://github.com/ThatNotEasy/CVE-2024-6387](https://github.com/ThatNotEasy/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2024-6387.svg)

- [https://github.com/sardine-web/CVE-2024-6387_Check](https://github.com/sardine-web/CVE-2024-6387_Check) :  ![starts](https://img.shields.io/github/stars/sardine-web/CVE-2024-6387_Check.svg) ![forks](https://img.shields.io/github/forks/sardine-web/CVE-2024-6387_Check.svg)

- [https://github.com/muyuanlove/CVE-2024-6387fixshell](https://github.com/muyuanlove/CVE-2024-6387fixshell) :  ![starts](https://img.shields.io/github/stars/muyuanlove/CVE-2024-6387fixshell.svg) ![forks](https://img.shields.io/github/forks/muyuanlove/CVE-2024-6387fixshell.svg)

- [https://github.com/ACHUX21/checker-CVE-2024-6387](https://github.com/ACHUX21/checker-CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/ACHUX21/checker-CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/ACHUX21/checker-CVE-2024-6387.svg)

- [https://github.com/sardine-web/CVE-2024-6387-template](https://github.com/sardine-web/CVE-2024-6387-template) :  ![starts](https://img.shields.io/github/stars/sardine-web/CVE-2024-6387-template.svg) ![forks](https://img.shields.io/github/forks/sardine-web/CVE-2024-6387-template.svg)

- [https://github.com/rumochnaya/openssh-cve-2024-6387.sh](https://github.com/rumochnaya/openssh-cve-2024-6387.sh) :  ![starts](https://img.shields.io/github/stars/rumochnaya/openssh-cve-2024-6387.sh.svg) ![forks](https://img.shields.io/github/forks/rumochnaya/openssh-cve-2024-6387.sh.svg)

- [https://github.com/redux-sibi-jose/mitigate_ssh](https://github.com/redux-sibi-jose/mitigate_ssh) :  ![starts](https://img.shields.io/github/stars/redux-sibi-jose/mitigate_ssh.svg) ![forks](https://img.shields.io/github/forks/redux-sibi-jose/mitigate_ssh.svg)

- [https://github.com/R4Tw1z/CVE-2024-6387](https://github.com/R4Tw1z/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/R4Tw1z/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/R4Tw1z/CVE-2024-6387.svg)

- [https://github.com/grupooruss/CVE-2024-6387](https://github.com/grupooruss/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/grupooruss/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/grupooruss/CVE-2024-6387.svg)

- [https://github.com/n1cks0n/Test_CVE-2024-6387](https://github.com/n1cks0n/Test_CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/n1cks0n/Test_CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/n1cks0n/Test_CVE-2024-6387.svg)

- [https://github.com/passwa11/cve-2024-6387-poc](https://github.com/passwa11/cve-2024-6387-poc) :  ![starts](https://img.shields.io/github/stars/passwa11/cve-2024-6387-poc.svg) ![forks](https://img.shields.io/github/forks/passwa11/cve-2024-6387-poc.svg)

- [https://github.com/shamo0/CVE-2024-6387_PoC](https://github.com/shamo0/CVE-2024-6387_PoC) :  ![starts](https://img.shields.io/github/stars/shamo0/CVE-2024-6387_PoC.svg) ![forks](https://img.shields.io/github/forks/shamo0/CVE-2024-6387_PoC.svg)

- [https://github.com/OhDamnn/Noregressh](https://github.com/OhDamnn/Noregressh) :  ![starts](https://img.shields.io/github/stars/OhDamnn/Noregressh.svg) ![forks](https://img.shields.io/github/forks/OhDamnn/Noregressh.svg)

- [https://github.com/turbobit/CVE-2024-6387-OpenSSH-Vulnerability-Checker](https://github.com/turbobit/CVE-2024-6387-OpenSSH-Vulnerability-Checker) :  ![starts](https://img.shields.io/github/stars/turbobit/CVE-2024-6387-OpenSSH-Vulnerability-Checker.svg) ![forks](https://img.shields.io/github/forks/turbobit/CVE-2024-6387-OpenSSH-Vulnerability-Checker.svg)

- [https://github.com/teamos-hub/regreSSHion](https://github.com/teamos-hub/regreSSHion) :  ![starts](https://img.shields.io/github/stars/teamos-hub/regreSSHion.svg) ![forks](https://img.shields.io/github/forks/teamos-hub/regreSSHion.svg)

- [https://github.com/X-Projetion/CVE-2023-4596-OpenSSH-Multi-Checker](https://github.com/X-Projetion/CVE-2023-4596-OpenSSH-Multi-Checker) :  ![starts](https://img.shields.io/github/stars/X-Projetion/CVE-2023-4596-OpenSSH-Multi-Checker.svg) ![forks](https://img.shields.io/github/forks/X-Projetion/CVE-2023-4596-OpenSSH-Multi-Checker.svg)

- [https://github.com/password123456/cve-security-response-guidelines](https://github.com/password123456/cve-security-response-guidelines) :  ![starts](https://img.shields.io/github/stars/password123456/cve-security-response-guidelines.svg) ![forks](https://img.shields.io/github/forks/password123456/cve-security-response-guidelines.svg)

- [https://github.com/xristos8574/regreSSHion-nmap-scanner](https://github.com/xristos8574/regreSSHion-nmap-scanner) :  ![starts](https://img.shields.io/github/stars/xristos8574/regreSSHion-nmap-scanner.svg) ![forks](https://img.shields.io/github/forks/xristos8574/regreSSHion-nmap-scanner.svg)

- [https://github.com/hssmo/cve-2024-6387_AImade](https://github.com/hssmo/cve-2024-6387_AImade) :  ![starts](https://img.shields.io/github/stars/hssmo/cve-2024-6387_AImade.svg) ![forks](https://img.shields.io/github/forks/hssmo/cve-2024-6387_AImade.svg)

- [https://github.com/FerasAlrimali/CVE-2024-6387-POC](https://github.com/FerasAlrimali/CVE-2024-6387-POC) :  ![starts](https://img.shields.io/github/stars/FerasAlrimali/CVE-2024-6387-POC.svg) ![forks](https://img.shields.io/github/forks/FerasAlrimali/CVE-2024-6387-POC.svg)

- [https://github.com/no-one-sec/CVE-2024-6387](https://github.com/no-one-sec/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/no-one-sec/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/no-one-sec/CVE-2024-6387.svg)

- [https://github.com/dawnl3ss/CVE-2024-6387](https://github.com/dawnl3ss/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/dawnl3ss/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/dawnl3ss/CVE-2024-6387.svg)

- [https://github.com/YassDEV221608/CVE-2024-6387](https://github.com/YassDEV221608/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/YassDEV221608/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/YassDEV221608/CVE-2024-6387.svg)

- [https://github.com/mrmtwoj/CVE-2024-6387](https://github.com/mrmtwoj/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/mrmtwoj/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/mrmtwoj/CVE-2024-6387.svg)

- [https://github.com/dream434/CVE-2024-6387](https://github.com/dream434/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/dream434/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/dream434/CVE-2024-6387.svg)

- [https://github.com/imv7/CVE-2024-6387](https://github.com/imv7/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/imv7/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/imv7/CVE-2024-6387.svg)

- [https://github.com/sms2056/CVE-2024-6387](https://github.com/sms2056/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/sms2056/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/sms2056/CVE-2024-6387.svg)

- [https://github.com/jack0we/CVE-2024-6387](https://github.com/jack0we/CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/jack0we/CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/jack0we/CVE-2024-6387.svg)

- [https://github.com/t3rry327/cve-2024-6387-poc](https://github.com/t3rry327/cve-2024-6387-poc) :  ![starts](https://img.shields.io/github/stars/t3rry327/cve-2024-6387-poc.svg) ![forks](https://img.shields.io/github/forks/t3rry327/cve-2024-6387-poc.svg)

- [https://github.com/shyrwall/cve-2024-6387-poc](https://github.com/shyrwall/cve-2024-6387-poc) :  ![starts](https://img.shields.io/github/stars/shyrwall/cve-2024-6387-poc.svg) ![forks](https://img.shields.io/github/forks/shyrwall/cve-2024-6387-poc.svg)

- [https://github.com/DimaMend/cve-2024-6387-poc](https://github.com/DimaMend/cve-2024-6387-poc) :  ![starts](https://img.shields.io/github/stars/DimaMend/cve-2024-6387-poc.svg) ![forks](https://img.shields.io/github/forks/DimaMend/cve-2024-6387-poc.svg)

- [https://github.com/RickGeex/CVE-2024-6387-Checker](https://github.com/RickGeex/CVE-2024-6387-Checker) :  ![starts](https://img.shields.io/github/stars/RickGeex/CVE-2024-6387-Checker.svg) ![forks](https://img.shields.io/github/forks/RickGeex/CVE-2024-6387-Checker.svg)

- [https://github.com/xiw1ll/CVE-2024-6387_Checker](https://github.com/xiw1ll/CVE-2024-6387_Checker) :  ![starts](https://img.shields.io/github/stars/xiw1ll/CVE-2024-6387_Checker.svg) ![forks](https://img.shields.io/github/forks/xiw1ll/CVE-2024-6387_Checker.svg)

- [https://github.com/Mufti22/CVE-2024-6387-checkher](https://github.com/Mufti22/CVE-2024-6387-checkher) :  ![starts](https://img.shields.io/github/stars/Mufti22/CVE-2024-6387-checkher.svg) ![forks](https://img.shields.io/github/forks/Mufti22/CVE-2024-6387-checkher.svg)

- [https://github.com/zenzue/CVE-2024-6387-Mitigation](https://github.com/zenzue/CVE-2024-6387-Mitigation) :  ![starts](https://img.shields.io/github/stars/zenzue/CVE-2024-6387-Mitigation.svg) ![forks](https://img.shields.io/github/forks/zenzue/CVE-2024-6387-Mitigation.svg)

- [https://github.com/jocker2410/CVE-2024-6387_poc](https://github.com/jocker2410/CVE-2024-6387_poc) :  ![starts](https://img.shields.io/github/stars/jocker2410/CVE-2024-6387_poc.svg) ![forks](https://img.shields.io/github/forks/jocker2410/CVE-2024-6387_poc.svg)

- [https://github.com/edsonjt81/CVE-2024-6387_Check](https://github.com/edsonjt81/CVE-2024-6387_Check) :  ![starts](https://img.shields.io/github/stars/edsonjt81/CVE-2024-6387_Check.svg) ![forks](https://img.shields.io/github/forks/edsonjt81/CVE-2024-6387_Check.svg)

- [https://github.com/CognisysGroup/CVE-2024-6387-Checker](https://github.com/CognisysGroup/CVE-2024-6387-Checker) :  ![starts](https://img.shields.io/github/stars/CognisysGroup/CVE-2024-6387-Checker.svg) ![forks](https://img.shields.io/github/forks/CognisysGroup/CVE-2024-6387-Checker.svg)

- [https://github.com/dgourillon/mitigate-CVE-2024-6387](https://github.com/dgourillon/mitigate-CVE-2024-6387) :  ![starts](https://img.shields.io/github/stars/dgourillon/mitigate-CVE-2024-6387.svg) ![forks](https://img.shields.io/github/forks/dgourillon/mitigate-CVE-2024-6387.svg)

- [https://github.com/SkyGodling/CVE-2024-6387-POC](https://github.com/SkyGodling/CVE-2024-6387-POC) :  ![starts](https://img.shields.io/github/stars/SkyGodling/CVE-2024-6387-POC.svg) ![forks](https://img.shields.io/github/forks/SkyGodling/CVE-2024-6387-POC.svg)

- [https://github.com/kubota/CVE-2024-6387-Vulnerability-Checker](https://github.com/kubota/CVE-2024-6387-Vulnerability-Checker) :  ![starts](https://img.shields.io/github/stars/kubota/CVE-2024-6387-Vulnerability-Checker.svg) ![forks](https://img.shields.io/github/forks/kubota/CVE-2024-6387-Vulnerability-Checker.svg)

- [https://github.com/4lxprime/regreSSHive](https://github.com/4lxprime/regreSSHive) :  ![starts](https://img.shields.io/github/stars/4lxprime/regreSSHive.svg) ![forks](https://img.shields.io/github/forks/4lxprime/regreSSHive.svg)

- [https://github.com/invaderslabs/regreSSHion-CVE-2024-6387-](https://github.com/invaderslabs/regreSSHion-CVE-2024-6387-) :  ![starts](https://img.shields.io/github/stars/invaderslabs/regreSSHion-CVE-2024-6387-.svg) ![forks](https://img.shields.io/github/forks/invaderslabs/regreSSHion-CVE-2024-6387-.svg)

- [https://github.com/JackSparrowhk/ssh-CVE-2024-6387-poc](https://github.com/JackSparrowhk/ssh-CVE-2024-6387-poc) :  ![starts](https://img.shields.io/github/stars/JackSparrowhk/ssh-CVE-2024-6387-poc.svg) ![forks](https://img.shields.io/github/forks/JackSparrowhk/ssh-CVE-2024-6387-poc.svg)

- [https://github.com/daniel-odrinski/CVE-2024-6387-Mitigation-Ansible-Playbook](https://github.com/daniel-odrinski/CVE-2024-6387-Mitigation-Ansible-Playbook) :  ![starts](https://img.shields.io/github/stars/daniel-odrinski/CVE-2024-6387-Mitigation-Ansible-Playbook.svg) ![forks](https://img.shields.io/github/forks/daniel-odrinski/CVE-2024-6387-Mitigation-Ansible-Playbook.svg)

- [https://github.com/vkaushik-chef/regreSSHion](https://github.com/vkaushik-chef/regreSSHion) :  ![starts](https://img.shields.io/github/stars/vkaushik-chef/regreSSHion.svg) ![forks](https://img.shields.io/github/forks/vkaushik-chef/regreSSHion.svg)

- [https://github.com/CiderAndWhisky/regression-scanner](https://github.com/CiderAndWhisky/regression-scanner) :  ![starts](https://img.shields.io/github/stars/CiderAndWhisky/regression-scanner.svg) ![forks](https://img.shields.io/github/forks/CiderAndWhisky/regression-scanner.svg)

- [https://github.com/alex14324/ssh_poc2024](https://github.com/alex14324/ssh_poc2024) :  ![starts](https://img.shields.io/github/stars/alex14324/ssh_poc2024.svg) ![forks](https://img.shields.io/github/forks/alex14324/ssh_poc2024.svg)

## CVE-2024-6366
 The User Profile Builder  WordPress plugin before 3.11.8 does not have proper authorisation, allowing unauthenticated users to upload media files via the async upload functionality of WP.



- [https://github.com/Abdurahmon3236/CVE-2024-6366](https://github.com/Abdurahmon3236/CVE-2024-6366) :  ![starts](https://img.shields.io/github/stars/Abdurahmon3236/CVE-2024-6366.svg) ![forks](https://img.shields.io/github/forks/Abdurahmon3236/CVE-2024-6366.svg)

## CVE-2024-6330
 The GEO my WP WordPress plugin before 4.5.0.2 does not prevent unauthenticated attackers from including arbitrary files in PHP's execution context, which leads to Remote Code Execution.



- [https://github.com/RandomRobbieBF/CVE-2024-6330](https://github.com/RandomRobbieBF/CVE-2024-6330) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-6330.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-6330.svg)

## CVE-2024-6205
 The PayPlus Payment Gateway WordPress plugin before 6.6.9 does not properly sanitise and escape a parameter before using it in a SQL statement via a WooCommerce API route available to unauthenticated users, leading to an SQL injection vulnerability.



- [https://github.com/j3r1ch0123/CVE-2024-6205](https://github.com/j3r1ch0123/CVE-2024-6205) :  ![starts](https://img.shields.io/github/stars/j3r1ch0123/CVE-2024-6205.svg) ![forks](https://img.shields.io/github/forks/j3r1ch0123/CVE-2024-6205.svg)

## CVE-2024-6050
 Improper Neutralization of Input During Web Page Generation vulnerability in SOKRATES-software SOWA OPAC allows a Reflected Cross-Site Scripting (XSS). An attacker might trick somebody into using a crafted URL, which will cause a script to be run in user's browser. This issue affects SOWA OPAC software in versions from 4.0 before 4.9.10, from 5.0 before 6.2.12.



- [https://github.com/kac89/CVE-2024-6050](https://github.com/kac89/CVE-2024-6050) :  ![starts](https://img.shields.io/github/stars/kac89/CVE-2024-6050.svg) ![forks](https://img.shields.io/github/forks/kac89/CVE-2024-6050.svg)

## CVE-2024-6028
 The Quiz Maker plugin for WordPress is vulnerable to time-based SQL Injection via the 'ays_questions' parameter in all versions up to, and including, 6.5.8.3 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/truonghuuphuc/CVE-2024-6028-Poc](https://github.com/truonghuuphuc/CVE-2024-6028-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-6028-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-6028-Poc.svg)

## CVE-2024-5961
 Improper neutralization of input during web page generation vulnerability in 2ClickPortal software allows reflected cross-site scripting (XSS). An attacker might trick somebody into using a crafted URL, which will cause a script to be run in user's browser. This issue affects 2ClickPortal software versions from 7.2.31 through 7.6.4.



- [https://github.com/kac89/CVE-2024-5961](https://github.com/kac89/CVE-2024-5961) :  ![starts](https://img.shields.io/github/stars/kac89/CVE-2024-5961.svg) ![forks](https://img.shields.io/github/forks/kac89/CVE-2024-5961.svg)

## CVE-2024-5947
 Deep Sea Electronics DSE855 Configuration Backup Missing Authentication Information Disclosure Vulnerability. This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Deep Sea Electronics DSE855 devices. Authentication is not required to exploit this vulnerability.

The specific flaw exists within the web-based UI. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise. Was ZDI-CAN-22679.



- [https://github.com/Cappricio-Securities/CVE-2024-5947](https://github.com/Cappricio-Securities/CVE-2024-5947) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2024-5947.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2024-5947.svg)

## CVE-2024-5910
 Missing authentication for a critical function in Palo Alto Networks Expedition can lead to an Expedition admin account takeover for attackers with network access to Expedition.

Note: Expedition is a tool aiding in configuration migration, tuning, and enrichment. Configuration secrets, credentials, and other data imported into Expedition is at risk due to this issue.



- [https://github.com/p33d/Palo-Alto-Expedition-Remote-Code-Execution-Exploit-CVE-2024-5910-CVE-2024-9464](https://github.com/p33d/Palo-Alto-Expedition-Remote-Code-Execution-Exploit-CVE-2024-5910-CVE-2024-9464) :  ![starts](https://img.shields.io/github/stars/p33d/Palo-Alto-Expedition-Remote-Code-Execution-Exploit-CVE-2024-5910-CVE-2024-9464.svg) ![forks](https://img.shields.io/github/forks/p33d/Palo-Alto-Expedition-Remote-Code-Execution-Exploit-CVE-2024-5910-CVE-2024-9464.svg)

## CVE-2024-5806
 Improper Authentication vulnerability in Progress MOVEit Transfer (SFTP module) can lead to Authentication Bypass.This issue affects MOVEit Transfer: from 2023.0.0 before 2023.0.11, from 2023.1.0 before 2023.1.6, from 2024.0.0 before 2024.0.2.



- [https://github.com/watchtowrlabs/watchTowr-vs-progress-moveit_CVE-2024-5806](https://github.com/watchtowrlabs/watchTowr-vs-progress-moveit_CVE-2024-5806) :  ![starts](https://img.shields.io/github/stars/watchtowrlabs/watchTowr-vs-progress-moveit_CVE-2024-5806.svg) ![forks](https://img.shields.io/github/forks/watchtowrlabs/watchTowr-vs-progress-moveit_CVE-2024-5806.svg)

## CVE-2024-5764
 Use of Hard-coded Credentials vulnerability in Sonatype Nexus Repository has been discovered in the code responsible for encrypting any secrets stored in the Nexus Repository configuration database (SMTP or HTTP proxy credentials, user tokens, tokens, among others). The affected versions relied on a static hard-coded encryption passphrase. While it was possible for an administrator to define an alternate encryption passphrase, it could only be done at first boot and not updated.

This issue affects Nexus Repository: from 3.0.0 through 3.72.0.



- [https://github.com/fin3ss3g0d/CVE-2024-5764](https://github.com/fin3ss3g0d/CVE-2024-5764) :  ![starts](https://img.shields.io/github/stars/fin3ss3g0d/CVE-2024-5764.svg) ![forks](https://img.shields.io/github/forks/fin3ss3g0d/CVE-2024-5764.svg)

## CVE-2024-5737
 Script afGdStream.php in AdmirorFrames Joomla! extension doesn’t specify a content type and as a result default (text/html) is used. An attacker may embed HTML tags directly in image data which is rendered by a webpage as HTML. This issue affects AdmirorFrames: before 5.0.



- [https://github.com/afine-com/CVE-2024-5737](https://github.com/afine-com/CVE-2024-5737) :  ![starts](https://img.shields.io/github/stars/afine-com/CVE-2024-5737.svg) ![forks](https://img.shields.io/github/forks/afine-com/CVE-2024-5737.svg)

## CVE-2024-5736
 Server Side Request Forgery (SSRF) vulnerability in AdmirorFrames Joomla! extension in afGdStream.php script allows to access local files or server pages available only from localhost. This issue affects AdmirorFrames: before 5.0.



- [https://github.com/afine-com/CVE-2024-5736](https://github.com/afine-com/CVE-2024-5736) :  ![starts](https://img.shields.io/github/stars/afine-com/CVE-2024-5736.svg) ![forks](https://img.shields.io/github/forks/afine-com/CVE-2024-5736.svg)

## CVE-2024-5735
 Full Path Disclosure vulnerability in AdmirorFrames Joomla! extension in afHelper.php script allows an unauthorised attacker to retrieve location of web root folder. This issue affects AdmirorFrames: before 5.0.



- [https://github.com/afine-com/CVE-2024-5735](https://github.com/afine-com/CVE-2024-5735) :  ![starts](https://img.shields.io/github/stars/afine-com/CVE-2024-5735.svg) ![forks](https://img.shields.io/github/forks/afine-com/CVE-2024-5735.svg)

## CVE-2024-5643
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/JonnyWhatshisface/CVE-2024-56433](https://github.com/JonnyWhatshisface/CVE-2024-56433) :  ![starts](https://img.shields.io/github/stars/JonnyWhatshisface/CVE-2024-56433.svg) ![forks](https://img.shields.io/github/forks/JonnyWhatshisface/CVE-2024-56433.svg)

- [https://github.com/UnionTech-Software/libtheora-CVE-2024-56431-PoC](https://github.com/UnionTech-Software/libtheora-CVE-2024-56431-PoC) :  ![starts](https://img.shields.io/github/stars/UnionTech-Software/libtheora-CVE-2024-56431-PoC.svg) ![forks](https://img.shields.io/github/forks/UnionTech-Software/libtheora-CVE-2024-56431-PoC.svg)

## CVE-2024-5633
 Longse model LBH30FE200W cameras, as well as products based on this device, provide an unrestricted access for an attacker located in the same local network to an undocumented binary service CoolView on one of the ports. 
An attacker with a knowledge of the available commands is able to perform read/write operations on the device's memory, which might result in e.g. bypassing telnet login and obtaining full access to the device.



- [https://github.com/Adikso/CVE-2024-5633](https://github.com/Adikso/CVE-2024-5633) :  ![starts](https://img.shields.io/github/stars/Adikso/CVE-2024-5633.svg) ![forks](https://img.shields.io/github/forks/Adikso/CVE-2024-5633.svg)

## CVE-2024-5522
 The HTML5 Video Player  WordPress plugin before 2.5.27 does not sanitize and escape a parameter from a REST route before using it in a SQL statement, allowing unauthenticated users to perform SQL injection attacks



- [https://github.com/truonghuuphuc/CVE-2024-5522-Poc](https://github.com/truonghuuphuc/CVE-2024-5522-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-5522-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-5522-Poc.svg)

## CVE-2024-5476
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/nscan9/CVE-2024-54761-BigAnt-Office-Messenger-5.6.06-RCE-via-SQL-Injection](https://github.com/nscan9/CVE-2024-54761-BigAnt-Office-Messenger-5.6.06-RCE-via-SQL-Injection) :  ![starts](https://img.shields.io/github/stars/nscan9/CVE-2024-54761-BigAnt-Office-Messenger-5.6.06-RCE-via-SQL-Injection.svg) ![forks](https://img.shields.io/github/forks/nscan9/CVE-2024-54761-BigAnt-Office-Messenger-5.6.06-RCE-via-SQL-Injection.svg)

## CVE-2024-5452
 A remote code execution (RCE) vulnerability exists in the lightning-ai/pytorch-lightning library version 2.2.1 due to improper handling of deserialized user input and mismanagement of dunder attributes by the `deepdiff` library. The library uses `deepdiff.Delta` objects to modify application state based on frontend actions. However, it is possible to bypass the intended restrictions on modifying dunder attributes, allowing an attacker to construct a serialized delta that passes the deserializer whitelist and contains dunder attributes. When processed, this can be exploited to access other modules, classes, and instances, leading to arbitrary attribute write and total RCE on any self-hosted pytorch-lightning application in its default configuration, as the delta endpoint is enabled by default.



- [https://github.com/XiaomingX/cve-2024-5452-poc](https://github.com/XiaomingX/cve-2024-5452-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-5452-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-5452-poc.svg)

## CVE-2024-5326
 The Post Grid Gutenberg Blocks and WordPress Blog Plugin – PostX plugin for WordPress is vulnerable to unauthorized modification of data due to a missing capability check on the 'postx_presets_callback' function in all versions up to, and including, 4.1.2. This makes it possible for authenticated attackers, with Contributor-level access and above, to change arbitrary options on affected sites. This can be used to enable new user registration and set the default role for new users to Administrator.



- [https://github.com/truonghuuphuc/CVE-2024-5326-Poc](https://github.com/truonghuuphuc/CVE-2024-5326-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-5326-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-5326-Poc.svg)

- [https://github.com/cve-2024/CVE-2024-5326-Poc](https://github.com/cve-2024/CVE-2024-5326-Poc) :  ![starts](https://img.shields.io/github/stars/cve-2024/CVE-2024-5326-Poc.svg) ![forks](https://img.shields.io/github/forks/cve-2024/CVE-2024-5326-Poc.svg)

## CVE-2024-5324
 The Login/Signup Popup ( Inline Form + Woocommerce ) plugin for WordPress is vulnerable to unauthorized modification of data due to a missing capability check on the 'import_settings' function in versions 2.7.1 to 2.7.2. This makes it possible for authenticated attackers, with Subscriber-level access and above, to change arbitrary options on affected sites. This can be used to enable new user registration and set the default role for new users to Administrator.



- [https://github.com/RandomRobbieBF/CVE-2024-5324](https://github.com/RandomRobbieBF/CVE-2024-5324) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-5324.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-5324.svg)

## CVE-2024-5274
 Type Confusion in V8 in Google Chrome prior to 125.0.6422.112 allowed a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/Alchemist3dot14/CVE-2024-5274-Detection](https://github.com/Alchemist3dot14/CVE-2024-5274-Detection) :  ![starts](https://img.shields.io/github/stars/Alchemist3dot14/CVE-2024-5274-Detection.svg) ![forks](https://img.shields.io/github/forks/Alchemist3dot14/CVE-2024-5274-Detection.svg)

## CVE-2024-5246
 NETGEAR ProSAFE Network Management System Tomcat Remote Code Execution Vulnerability. This vulnerability allows remote attackers to execute arbitrary code on affected installations of NETGEAR ProSAFE Network Management System. Authentication is required to exploit this vulnerability.

The specific flaw exists within the product installer. The issue results from the use of a vulnerable version of Apache Tomcat. An attacker can leverage this vulnerability to execute code in the context of SYSTEM. Was ZDI-CAN-22868.



- [https://github.com/Abdurahmon3236/CVE-2024-5246](https://github.com/Abdurahmon3236/CVE-2024-5246) :  ![starts](https://img.shields.io/github/stars/Abdurahmon3236/CVE-2024-5246.svg) ![forks](https://img.shields.io/github/forks/Abdurahmon3236/CVE-2024-5246.svg)

## CVE-2024-5243
 TP-Link Omada ER605 Buffer Overflow Remote Code Execution Vulnerability. This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link Omada ER605 routers. Authentication is not required to exploit this vulnerability. However, devices are vulnerable only if configured to use the Comexe DDNS service.

The specific flaw exists within the handling of DNS names. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to execute code in the context of root. Was ZDI-CAN-22523.



- [https://github.com/dilagluc/CVE_2024_5243](https://github.com/dilagluc/CVE_2024_5243) :  ![starts](https://img.shields.io/github/stars/dilagluc/CVE_2024_5243.svg) ![forks](https://img.shields.io/github/forks/dilagluc/CVE_2024_5243.svg)

## CVE-2024-5217
 ServiceNow has addressed an input validation vulnerability that was identified in the Washington DC, Vancouver, and earlier Now Platform releases. This vulnerability could enable an unauthenticated user to remotely execute code within the context of the Now Platform. The vulnerability is addressed in the listed patches and hot fixes below, which were released during the June 2024 patching cycle. If you have not done so already, we recommend applying security patches relevant to your instance as soon as possible.



- [https://github.com/NoTsPepino/CVE-2024-4879-CVE-2024-5217-ServiceNow-RCE-Scanning](https://github.com/NoTsPepino/CVE-2024-4879-CVE-2024-5217-ServiceNow-RCE-Scanning) :  ![starts](https://img.shields.io/github/stars/NoTsPepino/CVE-2024-4879-CVE-2024-5217-ServiceNow-RCE-Scanning.svg) ![forks](https://img.shields.io/github/forks/NoTsPepino/CVE-2024-4879-CVE-2024-5217-ServiceNow-RCE-Scanning.svg)

## CVE-2024-5124
 A timing attack vulnerability exists in the gaizhenbiao/chuanhuchatgpt repository, specifically within the password comparison logic. The vulnerability is present in version 20240310 of the software, where passwords are compared using the '=' operator in Python. This method of comparison allows an attacker to guess passwords based on the timing of each character's comparison. The issue arises from the code segment that checks a password for a particular username, which can lead to the exposure of sensitive information to an unauthorized actor. An attacker exploiting this vulnerability could potentially guess user passwords, compromising the security of the system.



- [https://github.com/XiaomingX/cve-2024-5124-poc](https://github.com/XiaomingX/cve-2024-5124-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-5124-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-5124-poc.svg)

## CVE-2024-5096
 A vulnerability classified as problematic was found in Hipcam Device up to 20240511. This vulnerability affects unknown code of the file /log/wifi.mac of the component MAC Address Handler. The manipulation leads to information disclosure. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. VDB-265078 is the identifier assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/fdzdev/CVE-2024-50962](https://github.com/fdzdev/CVE-2024-50962) :  ![starts](https://img.shields.io/github/stars/fdzdev/CVE-2024-50962.svg) ![forks](https://img.shields.io/github/forks/fdzdev/CVE-2024-50962.svg)

- [https://github.com/fdzdev/CVE-2024-50961](https://github.com/fdzdev/CVE-2024-50961) :  ![starts](https://img.shields.io/github/stars/fdzdev/CVE-2024-50961.svg) ![forks](https://img.shields.io/github/forks/fdzdev/CVE-2024-50961.svg)

- [https://github.com/fdzdev/CVE-2024-50964](https://github.com/fdzdev/CVE-2024-50964) :  ![starts](https://img.shields.io/github/stars/fdzdev/CVE-2024-50964.svg) ![forks](https://img.shields.io/github/forks/fdzdev/CVE-2024-50964.svg)

## CVE-2024-5084
 The Hash Form – Drag & Drop Form Builder plugin for WordPress is vulnerable to arbitrary file uploads due to missing file type validation in the 'file_upload_action' function in all versions up to, and including, 1.1.0. This makes it possible for unauthenticated attackers to upload arbitrary files on the affected site's server which may make remote code execution possible.



- [https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance](https://github.com/peiqiF4ck/WebFrameworkTools-5.5-enhance) :  ![starts](https://img.shields.io/github/stars/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg) ![forks](https://img.shields.io/github/forks/peiqiF4ck/WebFrameworkTools-5.5-enhance.svg)

- [https://github.com/Chocapikk/CVE-2024-5084](https://github.com/Chocapikk/CVE-2024-5084) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-5084.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-5084.svg)

- [https://github.com/WOOOOONG/CVE-2024-5084](https://github.com/WOOOOONG/CVE-2024-5084) :  ![starts](https://img.shields.io/github/stars/WOOOOONG/CVE-2024-5084.svg) ![forks](https://img.shields.io/github/forks/WOOOOONG/CVE-2024-5084.svg)

- [https://github.com/NanoWraith/CVE-2024-5084](https://github.com/NanoWraith/CVE-2024-5084) :  ![starts](https://img.shields.io/github/stars/NanoWraith/CVE-2024-5084.svg) ![forks](https://img.shields.io/github/forks/NanoWraith/CVE-2024-5084.svg)

- [https://github.com/Raeezrbr/CVE-2024-5084](https://github.com/Raeezrbr/CVE-2024-5084) :  ![starts](https://img.shields.io/github/stars/Raeezrbr/CVE-2024-5084.svg) ![forks](https://img.shields.io/github/forks/Raeezrbr/CVE-2024-5084.svg)

- [https://github.com/KTN1990/CVE-2024-5084](https://github.com/KTN1990/CVE-2024-5084) :  ![starts](https://img.shields.io/github/stars/KTN1990/CVE-2024-5084.svg) ![forks](https://img.shields.io/github/forks/KTN1990/CVE-2024-5084.svg)

## CVE-2024-5009
 In WhatsUp Gold versions released before 2023.1.3, an Improper Access Control vulnerability in Wug.UI.Controllers.InstallController.SetAdminPassword allows local attackers to modify admin's password.



- [https://github.com/sinsinology/CVE-2024-5009](https://github.com/sinsinology/CVE-2024-5009) :  ![starts](https://img.shields.io/github/stars/sinsinology/CVE-2024-5009.svg) ![forks](https://img.shields.io/github/forks/sinsinology/CVE-2024-5009.svg)

- [https://github.com/th3gokul/CVE-2024-5009](https://github.com/th3gokul/CVE-2024-5009) :  ![starts](https://img.shields.io/github/stars/th3gokul/CVE-2024-5009.svg) ![forks](https://img.shields.io/github/forks/th3gokul/CVE-2024-5009.svg)

## CVE-2024-4956
 Path Traversal in Sonatype Nexus Repository 3 allows an unauthenticated attacker to read system files. Fixed in version 3.68.1.



- [https://github.com/verylazytech/CVE-2024-4956](https://github.com/verylazytech/CVE-2024-4956) :  ![starts](https://img.shields.io/github/stars/verylazytech/CVE-2024-4956.svg) ![forks](https://img.shields.io/github/forks/verylazytech/CVE-2024-4956.svg)

- [https://github.com/ifconfig-me/CVE-2024-4956-Bulk-Scanner](https://github.com/ifconfig-me/CVE-2024-4956-Bulk-Scanner) :  ![starts](https://img.shields.io/github/stars/ifconfig-me/CVE-2024-4956-Bulk-Scanner.svg) ![forks](https://img.shields.io/github/forks/ifconfig-me/CVE-2024-4956-Bulk-Scanner.svg)

- [https://github.com/fin3ss3g0d/CVE-2024-4956](https://github.com/fin3ss3g0d/CVE-2024-4956) :  ![starts](https://img.shields.io/github/stars/fin3ss3g0d/CVE-2024-4956.svg) ![forks](https://img.shields.io/github/forks/fin3ss3g0d/CVE-2024-4956.svg)

- [https://github.com/XiaomingX/cve-2024-4956](https://github.com/XiaomingX/cve-2024-4956) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-4956.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-4956.svg)

- [https://github.com/GoatSecurity/CVE-2024-4956](https://github.com/GoatSecurity/CVE-2024-4956) :  ![starts](https://img.shields.io/github/stars/GoatSecurity/CVE-2024-4956.svg) ![forks](https://img.shields.io/github/forks/GoatSecurity/CVE-2024-4956.svg)

- [https://github.com/xungzzz/CVE-2024-4956](https://github.com/xungzzz/CVE-2024-4956) :  ![starts](https://img.shields.io/github/stars/xungzzz/CVE-2024-4956.svg) ![forks](https://img.shields.io/github/forks/xungzzz/CVE-2024-4956.svg)

- [https://github.com/erickfernandox/CVE-2024-4956](https://github.com/erickfernandox/CVE-2024-4956) :  ![starts](https://img.shields.io/github/stars/erickfernandox/CVE-2024-4956.svg) ![forks](https://img.shields.io/github/forks/erickfernandox/CVE-2024-4956.svg)

- [https://github.com/gmh5225/CVE-2024-4956](https://github.com/gmh5225/CVE-2024-4956) :  ![starts](https://img.shields.io/github/stars/gmh5225/CVE-2024-4956.svg) ![forks](https://img.shields.io/github/forks/gmh5225/CVE-2024-4956.svg)

- [https://github.com/Cappricio-Securities/CVE-2024-4956](https://github.com/Cappricio-Securities/CVE-2024-4956) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2024-4956.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2024-4956.svg)

- [https://github.com/banditzCyber0x/CVE-2024-4956](https://github.com/banditzCyber0x/CVE-2024-4956) :  ![starts](https://img.shields.io/github/stars/banditzCyber0x/CVE-2024-4956.svg) ![forks](https://img.shields.io/github/forks/banditzCyber0x/CVE-2024-4956.svg)

- [https://github.com/thinhap/CVE-2024-4956-PoC](https://github.com/thinhap/CVE-2024-4956-PoC) :  ![starts](https://img.shields.io/github/stars/thinhap/CVE-2024-4956-PoC.svg) ![forks](https://img.shields.io/github/forks/thinhap/CVE-2024-4956-PoC.svg)

- [https://github.com/Praison001/CVE-2024-4956-Sonatype-Nexus-Repository-Manager](https://github.com/Praison001/CVE-2024-4956-Sonatype-Nexus-Repository-Manager) :  ![starts](https://img.shields.io/github/stars/Praison001/CVE-2024-4956-Sonatype-Nexus-Repository-Manager.svg) ![forks](https://img.shields.io/github/forks/Praison001/CVE-2024-4956-Sonatype-Nexus-Repository-Manager.svg)

## CVE-2024-4947
 Type Confusion in V8 in Google Chrome prior to 125.0.6422.60 allowed a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/bjrjk/CVE-2024-4947](https://github.com/bjrjk/CVE-2024-4947) :  ![starts](https://img.shields.io/github/stars/bjrjk/CVE-2024-4947.svg) ![forks](https://img.shields.io/github/forks/bjrjk/CVE-2024-4947.svg)

## CVE-2024-4937
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/OHDUDEOKNICE/CVE-2024-49379](https://github.com/OHDUDEOKNICE/CVE-2024-49379) :  ![starts](https://img.shields.io/github/stars/OHDUDEOKNICE/CVE-2024-49379.svg) ![forks](https://img.shields.io/github/forks/OHDUDEOKNICE/CVE-2024-49379.svg)

## CVE-2024-4898
 The InstaWP Connect – 1-click WP Staging & Migration plugin for WordPress is vulnerable to arbitrary option updates due to a missing authorization checks on the REST API calls in all versions up to, and including, 0.1.0.38. This makes it possible for unauthenticated attackers to connect the site to InstaWP API, edit arbitrary site options and create administrator accounts.



- [https://github.com/truonghuuphuc/CVE-2024-4898-Poc](https://github.com/truonghuuphuc/CVE-2024-4898-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-4898-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-4898-Poc.svg)

- [https://github.com/cve-2024/CVE-2024-4898-Poc](https://github.com/cve-2024/CVE-2024-4898-Poc) :  ![starts](https://img.shields.io/github/stars/cve-2024/CVE-2024-4898-Poc.svg) ![forks](https://img.shields.io/github/forks/cve-2024/CVE-2024-4898-Poc.svg)

## CVE-2024-4885
 In WhatsUp Gold versions released before 2023.1.3, an unauthenticated Remote Code Execution vulnerability in Progress WhatsUpGold.  The 

WhatsUp.ExportUtilities.Export.GetFileWithoutZip



 allows execution of commands with iisapppool\nmconsole privileges.



- [https://github.com/sinsinology/CVE-2024-4885](https://github.com/sinsinology/CVE-2024-4885) :  ![starts](https://img.shields.io/github/stars/sinsinology/CVE-2024-4885.svg) ![forks](https://img.shields.io/github/forks/sinsinology/CVE-2024-4885.svg)

## CVE-2024-4883
 In WhatsUp Gold versions released before 2023.1.3, a Remote Code Execution issue exists in Progress WhatsUp Gold. This vulnerability allows an unauthenticated attacker to achieve the RCE as a service account through NmApi.exe.



- [https://github.com/sinsinology/CVE-2024-4883](https://github.com/sinsinology/CVE-2024-4883) :  ![starts](https://img.shields.io/github/stars/sinsinology/CVE-2024-4883.svg) ![forks](https://img.shields.io/github/forks/sinsinology/CVE-2024-4883.svg)

## CVE-2024-4879
 ServiceNow has addressed an input validation vulnerability that was identified in Vancouver and Washington DC Now Platform releases. This vulnerability could enable an unauthenticated user to remotely execute code within the context of the Now Platform. ServiceNow applied an update to hosted instances, and ServiceNow released the update to our partners and self-hosted customers. Listed below are the patches and hot fixes that address the vulnerability. If you have not done so already, we recommend applying security patches relevant to your instance as soon as possible.



- [https://github.com/Brut-Security/CVE-2024-4879](https://github.com/Brut-Security/CVE-2024-4879) :  ![starts](https://img.shields.io/github/stars/Brut-Security/CVE-2024-4879.svg) ![forks](https://img.shields.io/github/forks/Brut-Security/CVE-2024-4879.svg)

- [https://github.com/bigb0x/CVE-2024-4879](https://github.com/bigb0x/CVE-2024-4879) :  ![starts](https://img.shields.io/github/stars/bigb0x/CVE-2024-4879.svg) ![forks](https://img.shields.io/github/forks/bigb0x/CVE-2024-4879.svg)

- [https://github.com/NoTsPepino/CVE-2024-4879-CVE-2024-5217-ServiceNow-RCE-Scanning](https://github.com/NoTsPepino/CVE-2024-4879-CVE-2024-5217-ServiceNow-RCE-Scanning) :  ![starts](https://img.shields.io/github/stars/NoTsPepino/CVE-2024-4879-CVE-2024-5217-ServiceNow-RCE-Scanning.svg) ![forks](https://img.shields.io/github/forks/NoTsPepino/CVE-2024-4879-CVE-2024-5217-ServiceNow-RCE-Scanning.svg)

- [https://github.com/Mr-r00t11/CVE-2024-4879](https://github.com/Mr-r00t11/CVE-2024-4879) :  ![starts](https://img.shields.io/github/stars/Mr-r00t11/CVE-2024-4879.svg) ![forks](https://img.shields.io/github/forks/Mr-r00t11/CVE-2024-4879.svg)

- [https://github.com/Praison001/CVE-2024-4879-ServiceNow](https://github.com/Praison001/CVE-2024-4879-ServiceNow) :  ![starts](https://img.shields.io/github/stars/Praison001/CVE-2024-4879-ServiceNow.svg) ![forks](https://img.shields.io/github/forks/Praison001/CVE-2024-4879-ServiceNow.svg)

- [https://github.com/ShadowByte1/CVE-2024-4879](https://github.com/ShadowByte1/CVE-2024-4879) :  ![starts](https://img.shields.io/github/stars/ShadowByte1/CVE-2024-4879.svg) ![forks](https://img.shields.io/github/forks/ShadowByte1/CVE-2024-4879.svg)

- [https://github.com/tequilasunsh1ne/CVE_2024_4879](https://github.com/tequilasunsh1ne/CVE_2024_4879) :  ![starts](https://img.shields.io/github/stars/tequilasunsh1ne/CVE_2024_4879.svg) ![forks](https://img.shields.io/github/forks/tequilasunsh1ne/CVE_2024_4879.svg)

## CVE-2024-4875
 The HT Mega – Absolute Addons For Elementor plugin for WordPress is vulnerable to unauthorized modification of data|loss of data due to a missing capability check on the 'ajax_dismiss' function in versions up to, and including, 2.5.2. This makes it possible for authenticated attackers, with subscriber-level permissions and above, to update options such as users_can_register, which can lead to unauthorized user registration.



- [https://github.com/RandomRobbieBF/CVE-2024-4875](https://github.com/RandomRobbieBF/CVE-2024-4875) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-4875.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-4875.svg)

## CVE-2024-4864
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/rosembergpro/CVE-2024-48644](https://github.com/rosembergpro/CVE-2024-48644) :  ![starts](https://img.shields.io/github/stars/rosembergpro/CVE-2024-48644.svg) ![forks](https://img.shields.io/github/forks/rosembergpro/CVE-2024-48644.svg)

## CVE-2024-4832
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/trqt/CVE-2024-48322](https://github.com/trqt/CVE-2024-48322) :  ![starts](https://img.shields.io/github/stars/trqt/CVE-2024-48322.svg) ![forks](https://img.shields.io/github/forks/trqt/CVE-2024-48322.svg)

- [https://github.com/osvaldotenorio/cve-2024-48325](https://github.com/osvaldotenorio/cve-2024-48325) :  ![starts](https://img.shields.io/github/stars/osvaldotenorio/cve-2024-48325.svg) ![forks](https://img.shields.io/github/forks/osvaldotenorio/cve-2024-48325.svg)

- [https://github.com/fabiobsj/CVE-2024-48326](https://github.com/fabiobsj/CVE-2024-48326) :  ![starts](https://img.shields.io/github/stars/fabiobsj/CVE-2024-48326.svg) ![forks](https://img.shields.io/github/forks/fabiobsj/CVE-2024-48326.svg)

## CVE-2024-4761
 Out of bounds write in V8 in Google Chrome prior to 124.0.6367.207 allowed a remote attacker to perform an out of bounds memory write via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/michredteam/CVE-2024-4761](https://github.com/michredteam/CVE-2024-4761) :  ![starts](https://img.shields.io/github/stars/michredteam/CVE-2024-4761.svg) ![forks](https://img.shields.io/github/forks/michredteam/CVE-2024-4761.svg)

## CVE-2024-4701
 A path traversal issue potentially leading to remote code execution in Genie for all versions prior to 4.3.18



- [https://github.com/JoeBeeton/CVE-2024-4701-POC](https://github.com/JoeBeeton/CVE-2024-4701-POC) :  ![starts](https://img.shields.io/github/stars/JoeBeeton/CVE-2024-4701-POC.svg) ![forks](https://img.shields.io/github/forks/JoeBeeton/CVE-2024-4701-POC.svg)

## CVE-2024-4577
 In PHP versions 8.1.* before 8.1.29, 8.2.* before 8.2.20, 8.3.* before 8.3.8, when using Apache and PHP-CGI on Windows, if the system is set up to use certain code pages, Windows may use "Best-Fit" behavior to replace characters in command line given to Win32 API functions. PHP CGI module may misinterpret those characters as PHP options, which may allow a malicious user to pass options to PHP binary being run, and thus reveal the source code of scripts, run arbitrary PHP code on the server, etc.



- [https://github.com/watchtowrlabs/CVE-2024-4577](https://github.com/watchtowrlabs/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/watchtowrlabs/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/watchtowrlabs/CVE-2024-4577.svg)

- [https://github.com/xcanwin/CVE-2024-4577-PHP-RCE](https://github.com/xcanwin/CVE-2024-4577-PHP-RCE) :  ![starts](https://img.shields.io/github/stars/xcanwin/CVE-2024-4577-PHP-RCE.svg) ![forks](https://img.shields.io/github/forks/xcanwin/CVE-2024-4577-PHP-RCE.svg)

- [https://github.com/TAM-K592/CVE-2024-4577](https://github.com/TAM-K592/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/TAM-K592/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/TAM-K592/CVE-2024-4577.svg)

- [https://github.com/11whoami99/CVE-2024-4577](https://github.com/11whoami99/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/11whoami99/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/11whoami99/CVE-2024-4577.svg)

- [https://github.com/Chocapikk/CVE-2024-4577](https://github.com/Chocapikk/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-4577.svg)

- [https://github.com/ZephrFish/CVE-2024-4577-PHP-RCE](https://github.com/ZephrFish/CVE-2024-4577-PHP-RCE) :  ![starts](https://img.shields.io/github/stars/ZephrFish/CVE-2024-4577-PHP-RCE.svg) ![forks](https://img.shields.io/github/forks/ZephrFish/CVE-2024-4577-PHP-RCE.svg)

- [https://github.com/BTtea/CVE-2024-4577-RCE-PoC](https://github.com/BTtea/CVE-2024-4577-RCE-PoC) :  ![starts](https://img.shields.io/github/stars/BTtea/CVE-2024-4577-RCE-PoC.svg) ![forks](https://img.shields.io/github/forks/BTtea/CVE-2024-4577-RCE-PoC.svg)

- [https://github.com/huseyinstif/CVE-2024-4577-Nuclei-Template](https://github.com/huseyinstif/CVE-2024-4577-Nuclei-Template) :  ![starts](https://img.shields.io/github/stars/huseyinstif/CVE-2024-4577-Nuclei-Template.svg) ![forks](https://img.shields.io/github/forks/huseyinstif/CVE-2024-4577-Nuclei-Template.svg)

- [https://github.com/gotr00t0day/CVE-2024-4577](https://github.com/gotr00t0day/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/gotr00t0day/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/gotr00t0day/CVE-2024-4577.svg)

- [https://github.com/K3ysTr0K3R/CVE-2024-4577-EXPLOIT](https://github.com/K3ysTr0K3R/CVE-2024-4577-EXPLOIT) :  ![starts](https://img.shields.io/github/stars/K3ysTr0K3R/CVE-2024-4577-EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/K3ysTr0K3R/CVE-2024-4577-EXPLOIT.svg)

- [https://github.com/manuelinfosec/CVE-2024-4577](https://github.com/manuelinfosec/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/manuelinfosec/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/manuelinfosec/CVE-2024-4577.svg)

- [https://github.com/l0n3m4n/CVE-2024-4577-RCE](https://github.com/l0n3m4n/CVE-2024-4577-RCE) :  ![starts](https://img.shields.io/github/stars/l0n3m4n/CVE-2024-4577-RCE.svg) ![forks](https://img.shields.io/github/forks/l0n3m4n/CVE-2024-4577-RCE.svg)

- [https://github.com/Sh0ckFR/CVE-2024-4577](https://github.com/Sh0ckFR/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/Sh0ckFR/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/Sh0ckFR/CVE-2024-4577.svg)

- [https://github.com/bibo318/CVE-2024-4577-RCE-ATTACK](https://github.com/bibo318/CVE-2024-4577-RCE-ATTACK) :  ![starts](https://img.shields.io/github/stars/bibo318/CVE-2024-4577-RCE-ATTACK.svg) ![forks](https://img.shields.io/github/forks/bibo318/CVE-2024-4577-RCE-ATTACK.svg)

- [https://github.com/zomasec/CVE-2024-4577](https://github.com/zomasec/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/zomasec/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/zomasec/CVE-2024-4577.svg)

- [https://github.com/0x20c/CVE-2024-4577-nuclei](https://github.com/0x20c/CVE-2024-4577-nuclei) :  ![starts](https://img.shields.io/github/stars/0x20c/CVE-2024-4577-nuclei.svg) ![forks](https://img.shields.io/github/forks/0x20c/CVE-2024-4577-nuclei.svg)

- [https://github.com/Junp0/CVE-2024-4577](https://github.com/Junp0/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/Junp0/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/Junp0/CVE-2024-4577.svg)

- [https://github.com/aaddmin1122345/cve-2024-4577](https://github.com/aaddmin1122345/cve-2024-4577) :  ![starts](https://img.shields.io/github/stars/aaddmin1122345/cve-2024-4577.svg) ![forks](https://img.shields.io/github/forks/aaddmin1122345/cve-2024-4577.svg)

- [https://github.com/VictorShem/CVE-2024-4577](https://github.com/VictorShem/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/VictorShem/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/VictorShem/CVE-2024-4577.svg)

- [https://github.com/AlperenY-cs/CVE-2024-4577](https://github.com/AlperenY-cs/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/AlperenY-cs/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/AlperenY-cs/CVE-2024-4577.svg)

- [https://github.com/d3ck4/Shodan-CVE-2024-4577](https://github.com/d3ck4/Shodan-CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/d3ck4/Shodan-CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/d3ck4/Shodan-CVE-2024-4577.svg)

- [https://github.com/ggfzx/CVE-2024-4577](https://github.com/ggfzx/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/ggfzx/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/ggfzx/CVE-2024-4577.svg)

- [https://github.com/sug4r-wr41th/CVE-2024-4577](https://github.com/sug4r-wr41th/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/sug4r-wr41th/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/sug4r-wr41th/CVE-2024-4577.svg)

- [https://github.com/taida957789/CVE-2024-4577](https://github.com/taida957789/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/taida957789/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/taida957789/CVE-2024-4577.svg)

- [https://github.com/Wh02m1/CVE-2024-4577](https://github.com/Wh02m1/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/Wh02m1/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/Wh02m1/CVE-2024-4577.svg)

- [https://github.com/nemu1k5ma/CVE-2024-4577](https://github.com/nemu1k5ma/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/nemu1k5ma/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/nemu1k5ma/CVE-2024-4577.svg)

- [https://github.com/CirqueiraDev/MassExploit-CVE-2024-4577](https://github.com/CirqueiraDev/MassExploit-CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/CirqueiraDev/MassExploit-CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/CirqueiraDev/MassExploit-CVE-2024-4577.svg)

- [https://github.com/PhinehasNarh/CVE-2024-4577-LetsDefend-walkthrough](https://github.com/PhinehasNarh/CVE-2024-4577-LetsDefend-walkthrough) :  ![starts](https://img.shields.io/github/stars/PhinehasNarh/CVE-2024-4577-LetsDefend-walkthrough.svg) ![forks](https://img.shields.io/github/forks/PhinehasNarh/CVE-2024-4577-LetsDefend-walkthrough.svg)

- [https://github.com/XiangDongCJC/CVE-2024-4577-PHP-CGI-RCE](https://github.com/XiangDongCJC/CVE-2024-4577-PHP-CGI-RCE) :  ![starts](https://img.shields.io/github/stars/XiangDongCJC/CVE-2024-4577-PHP-CGI-RCE.svg) ![forks](https://img.shields.io/github/forks/XiangDongCJC/CVE-2024-4577-PHP-CGI-RCE.svg)

- [https://github.com/WanLiChangChengWanLiChang/CVE-2024-4577-RCE-EXP](https://github.com/WanLiChangChengWanLiChang/CVE-2024-4577-RCE-EXP) :  ![starts](https://img.shields.io/github/stars/WanLiChangChengWanLiChang/CVE-2024-4577-RCE-EXP.svg) ![forks](https://img.shields.io/github/forks/WanLiChangChengWanLiChang/CVE-2024-4577-RCE-EXP.svg)

- [https://github.com/Ra1n-60W/CVE-2024-4577](https://github.com/Ra1n-60W/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/Ra1n-60W/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/Ra1n-60W/CVE-2024-4577.svg)

- [https://github.com/zjhzjhhh/CVE-2024-4577](https://github.com/zjhzjhhh/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/zjhzjhhh/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/zjhzjhhh/CVE-2024-4577.svg)

- [https://github.com/olebris/CVE-2024-4577](https://github.com/olebris/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/olebris/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/olebris/CVE-2024-4577.svg)

- [https://github.com/Dejavu666/CVE-2024-4577](https://github.com/Dejavu666/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/Dejavu666/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/Dejavu666/CVE-2024-4577.svg)

- [https://github.com/charis3306/CVE-2024-4577](https://github.com/charis3306/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/charis3306/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/charis3306/CVE-2024-4577.svg)

- [https://github.com/Sysc4ll3r/CVE-2024-4577](https://github.com/Sysc4ll3r/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/Sysc4ll3r/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/Sysc4ll3r/CVE-2024-4577.svg)

- [https://github.com/bl4cksku11/CVE-2024-4577](https://github.com/bl4cksku11/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/bl4cksku11/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/bl4cksku11/CVE-2024-4577.svg)

- [https://github.com/dbyMelina/CVE-2024-4577](https://github.com/dbyMelina/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/dbyMelina/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/dbyMelina/CVE-2024-4577.svg)

- [https://github.com/r0otk3r/CVE-2024-4577](https://github.com/r0otk3r/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/r0otk3r/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/r0otk3r/CVE-2024-4577.svg)

- [https://github.com/Skycritch/CVE-2024-4577](https://github.com/Skycritch/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/Skycritch/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/Skycritch/CVE-2024-4577.svg)

- [https://github.com/hexedbyte/cve-2024-4577](https://github.com/hexedbyte/cve-2024-4577) :  ![starts](https://img.shields.io/github/stars/hexedbyte/cve-2024-4577.svg) ![forks](https://img.shields.io/github/forks/hexedbyte/cve-2024-4577.svg)

- [https://github.com/a-roshbaik/CVE-2024-4577](https://github.com/a-roshbaik/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/a-roshbaik/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/a-roshbaik/CVE-2024-4577.svg)

- [https://github.com/ahmetramazank/CVE-2024-4577](https://github.com/ahmetramazank/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/ahmetramazank/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/ahmetramazank/CVE-2024-4577.svg)

- [https://github.com/KimJuhyeong95/cve-2024-4577](https://github.com/KimJuhyeong95/cve-2024-4577) :  ![starts](https://img.shields.io/github/stars/KimJuhyeong95/cve-2024-4577.svg) ![forks](https://img.shields.io/github/forks/KimJuhyeong95/cve-2024-4577.svg)

- [https://github.com/Jcccccx/CVE-2024-4577](https://github.com/Jcccccx/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/Jcccccx/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/Jcccccx/CVE-2024-4577.svg)

- [https://github.com/princew88/CVE-2024-4577](https://github.com/princew88/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/princew88/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/princew88/CVE-2024-4577.svg)

- [https://github.com/BitMEXResearch/CVE-2024-4577](https://github.com/BitMEXResearch/CVE-2024-4577) :  ![starts](https://img.shields.io/github/stars/BitMEXResearch/CVE-2024-4577.svg) ![forks](https://img.shields.io/github/forks/BitMEXResearch/CVE-2024-4577.svg)

- [https://github.com/Gill-Singh-A/CVE-2024-4577-Exploit](https://github.com/Gill-Singh-A/CVE-2024-4577-Exploit) :  ![starts](https://img.shields.io/github/stars/Gill-Singh-A/CVE-2024-4577-Exploit.svg) ![forks](https://img.shields.io/github/forks/Gill-Singh-A/CVE-2024-4577-Exploit.svg)

- [https://github.com/Entropt/CVE-2024-4577_Analysis](https://github.com/Entropt/CVE-2024-4577_Analysis) :  ![starts](https://img.shields.io/github/stars/Entropt/CVE-2024-4577_Analysis.svg) ![forks](https://img.shields.io/github/forks/Entropt/CVE-2024-4577_Analysis.svg)

- [https://github.com/gmh5225/CVE-2024-4577-PHP-RCE](https://github.com/gmh5225/CVE-2024-4577-PHP-RCE) :  ![starts](https://img.shields.io/github/stars/gmh5225/CVE-2024-4577-PHP-RCE.svg) ![forks](https://img.shields.io/github/forks/gmh5225/CVE-2024-4577-PHP-RCE.svg)

- [https://github.com/a-roshbaik/CVE-2024-4577-PHP-RCE](https://github.com/a-roshbaik/CVE-2024-4577-PHP-RCE) :  ![starts](https://img.shields.io/github/stars/a-roshbaik/CVE-2024-4577-PHP-RCE.svg) ![forks](https://img.shields.io/github/forks/a-roshbaik/CVE-2024-4577-PHP-RCE.svg)

- [https://github.com/tntrock/CVE-2024-4577_PowerShell](https://github.com/tntrock/CVE-2024-4577_PowerShell) :  ![starts](https://img.shields.io/github/stars/tntrock/CVE-2024-4577_PowerShell.svg) ![forks](https://img.shields.io/github/forks/tntrock/CVE-2024-4577_PowerShell.svg)

- [https://github.com/jakabakos/CVE-2024-4577-PHP-CGI-argument-injection-RCE](https://github.com/jakabakos/CVE-2024-4577-PHP-CGI-argument-injection-RCE) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2024-4577-PHP-CGI-argument-injection-RCE.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2024-4577-PHP-CGI-argument-injection-RCE.svg)

- [https://github.com/mananjain61/PHP-CGI-INTERNAL-RCE](https://github.com/mananjain61/PHP-CGI-INTERNAL-RCE) :  ![starts](https://img.shields.io/github/stars/mananjain61/PHP-CGI-INTERNAL-RCE.svg) ![forks](https://img.shields.io/github/forks/mananjain61/PHP-CGI-INTERNAL-RCE.svg)

## CVE-2024-4573
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Castro-Ian/CVE-2024-4573-Mitigation-Script](https://github.com/Castro-Ian/CVE-2024-4573-Mitigation-Script) :  ![starts](https://img.shields.io/github/stars/Castro-Ian/CVE-2024-4573-Mitigation-Script.svg) ![forks](https://img.shields.io/github/forks/Castro-Ian/CVE-2024-4573-Mitigation-Script.svg)

## CVE-2024-4476
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/josephgodwinkimani/cloudpanel-2.4.2-CVE-2024-44765-recovery](https://github.com/josephgodwinkimani/cloudpanel-2.4.2-CVE-2024-44765-recovery) :  ![starts](https://img.shields.io/github/stars/josephgodwinkimani/cloudpanel-2.4.2-CVE-2024-44765-recovery.svg) ![forks](https://img.shields.io/github/forks/josephgodwinkimani/cloudpanel-2.4.2-CVE-2024-44765-recovery.svg)

## CVE-2024-4443
 The Business Directory Plugin – Easy Listing Directories for WordPress plugin for WordPress is vulnerable to time-based SQL Injection via the ‘listingfields’ parameter in all versions up to, and including, 6.4.2 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/truonghuuphuc/CVE-2024-4443-Poc](https://github.com/truonghuuphuc/CVE-2024-4443-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-4443-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-4443-Poc.svg)

## CVE-2024-4439
 WordPress Core is vulnerable to Stored Cross-Site Scripting via user display names in the Avatar block in various versions up to 6.5.2 due to insufficient output escaping on the display name. This makes it possible for authenticated attackers, with contributor-level access and above, to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page. In addition, it also makes it possible for unauthenticated attackers to inject arbitrary web scripts in pages that have the comment block present and display the comment author's avatar.



- [https://github.com/d0rb/CVE-2024-4439](https://github.com/d0rb/CVE-2024-4439) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2024-4439.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2024-4439.svg)

- [https://github.com/MielPopsssssss/CVE-2024-4439](https://github.com/MielPopsssssss/CVE-2024-4439) :  ![starts](https://img.shields.io/github/stars/MielPopsssssss/CVE-2024-4439.svg) ![forks](https://img.shields.io/github/forks/MielPopsssssss/CVE-2024-4439.svg)

- [https://github.com/w0r1i0g1ht/CVE-2024-4439](https://github.com/w0r1i0g1ht/CVE-2024-4439) :  ![starts](https://img.shields.io/github/stars/w0r1i0g1ht/CVE-2024-4439.svg) ![forks](https://img.shields.io/github/forks/w0r1i0g1ht/CVE-2024-4439.svg)

- [https://github.com/xssor-dz/-CVE-2024-4439](https://github.com/xssor-dz/-CVE-2024-4439) :  ![starts](https://img.shields.io/github/stars/xssor-dz/-CVE-2024-4439.svg) ![forks](https://img.shields.io/github/forks/xssor-dz/-CVE-2024-4439.svg)

## CVE-2024-4408
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Azvanzed/CVE-2024-44083](https://github.com/Azvanzed/CVE-2024-44083) :  ![starts](https://img.shields.io/github/stars/Azvanzed/CVE-2024-44083.svg) ![forks](https://img.shields.io/github/forks/Azvanzed/CVE-2024-44083.svg)

## CVE-2024-4396
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/RandomRobbieBF/CVE-2024-43965](https://github.com/RandomRobbieBF/CVE-2024-43965) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-43965.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-43965.svg)

## CVE-2024-4367
 A type check was missing when handling fonts in PDF.js, which would allow arbitrary JavaScript execution in the PDF.js context. This vulnerability affects Firefox  126, Firefox ESR  115.11, and Thunderbird  115.11.



- [https://github.com/LOURC0D3/CVE-2024-4367-PoC](https://github.com/LOURC0D3/CVE-2024-4367-PoC) :  ![starts](https://img.shields.io/github/stars/LOURC0D3/CVE-2024-4367-PoC.svg) ![forks](https://img.shields.io/github/forks/LOURC0D3/CVE-2024-4367-PoC.svg)

- [https://github.com/s4vvysec/CVE-2024-4367-POC](https://github.com/s4vvysec/CVE-2024-4367-POC) :  ![starts](https://img.shields.io/github/stars/s4vvysec/CVE-2024-4367-POC.svg) ![forks](https://img.shields.io/github/forks/s4vvysec/CVE-2024-4367-POC.svg)

- [https://github.com/Zombie-Kaiser/cve-2024-4367-PoC-fixed](https://github.com/Zombie-Kaiser/cve-2024-4367-PoC-fixed) :  ![starts](https://img.shields.io/github/stars/Zombie-Kaiser/cve-2024-4367-PoC-fixed.svg) ![forks](https://img.shields.io/github/forks/Zombie-Kaiser/cve-2024-4367-PoC-fixed.svg)

- [https://github.com/spaceraccoon/detect-cve-2024-4367](https://github.com/spaceraccoon/detect-cve-2024-4367) :  ![starts](https://img.shields.io/github/stars/spaceraccoon/detect-cve-2024-4367.svg) ![forks](https://img.shields.io/github/forks/spaceraccoon/detect-cve-2024-4367.svg)

- [https://github.com/snyk-labs/pdfjs-vuln-demo](https://github.com/snyk-labs/pdfjs-vuln-demo) :  ![starts](https://img.shields.io/github/stars/snyk-labs/pdfjs-vuln-demo.svg) ![forks](https://img.shields.io/github/forks/snyk-labs/pdfjs-vuln-demo.svg)

- [https://github.com/UnHackerEnCapital/PDFernetRemotelo](https://github.com/UnHackerEnCapital/PDFernetRemotelo) :  ![starts](https://img.shields.io/github/stars/UnHackerEnCapital/PDFernetRemotelo.svg) ![forks](https://img.shields.io/github/forks/UnHackerEnCapital/PDFernetRemotelo.svg)

- [https://github.com/clarkio/pdfjs-vuln-demo](https://github.com/clarkio/pdfjs-vuln-demo) :  ![starts](https://img.shields.io/github/stars/clarkio/pdfjs-vuln-demo.svg) ![forks](https://img.shields.io/github/forks/clarkio/pdfjs-vuln-demo.svg)

- [https://github.com/pS3ud0RAnD0m/cve-2024-4367-poc](https://github.com/pS3ud0RAnD0m/cve-2024-4367-poc) :  ![starts](https://img.shields.io/github/stars/pS3ud0RAnD0m/cve-2024-4367-poc.svg) ![forks](https://img.shields.io/github/forks/pS3ud0RAnD0m/cve-2024-4367-poc.svg)

- [https://github.com/exfil0/WEAPONIZING-CVE-2024-4367](https://github.com/exfil0/WEAPONIZING-CVE-2024-4367) :  ![starts](https://img.shields.io/github/stars/exfil0/WEAPONIZING-CVE-2024-4367.svg) ![forks](https://img.shields.io/github/forks/exfil0/WEAPONIZING-CVE-2024-4367.svg)

- [https://github.com/Bhavyakcwestern/Hacking-pdf.js-vulnerability](https://github.com/Bhavyakcwestern/Hacking-pdf.js-vulnerability) :  ![starts](https://img.shields.io/github/stars/Bhavyakcwestern/Hacking-pdf.js-vulnerability.svg) ![forks](https://img.shields.io/github/forks/Bhavyakcwestern/Hacking-pdf.js-vulnerability.svg)

- [https://github.com/Scivous/CVE-2024-4367-npm](https://github.com/Scivous/CVE-2024-4367-npm) :  ![starts](https://img.shields.io/github/stars/Scivous/CVE-2024-4367-npm.svg) ![forks](https://img.shields.io/github/forks/Scivous/CVE-2024-4367-npm.svg)

- [https://github.com/BektiHandoyo/cve-pdf-host](https://github.com/BektiHandoyo/cve-pdf-host) :  ![starts](https://img.shields.io/github/stars/BektiHandoyo/cve-pdf-host.svg) ![forks](https://img.shields.io/github/forks/BektiHandoyo/cve-pdf-host.svg)

- [https://github.com/MihranGIT/CVE-2024-4367](https://github.com/MihranGIT/CVE-2024-4367) :  ![starts](https://img.shields.io/github/stars/MihranGIT/CVE-2024-4367.svg) ![forks](https://img.shields.io/github/forks/MihranGIT/CVE-2024-4367.svg)

- [https://github.com/VVeakee/CVE-2024-4367](https://github.com/VVeakee/CVE-2024-4367) :  ![starts](https://img.shields.io/github/stars/VVeakee/CVE-2024-4367.svg) ![forks](https://img.shields.io/github/forks/VVeakee/CVE-2024-4367.svg)

- [https://github.com/MihranGIT/POC_CVE-2024-4367](https://github.com/MihranGIT/POC_CVE-2024-4367) :  ![starts](https://img.shields.io/github/stars/MihranGIT/POC_CVE-2024-4367.svg) ![forks](https://img.shields.io/github/forks/MihranGIT/POC_CVE-2024-4367.svg)

- [https://github.com/avalahEE/pdfjs_disable_eval](https://github.com/avalahEE/pdfjs_disable_eval) :  ![starts](https://img.shields.io/github/stars/avalahEE/pdfjs_disable_eval.svg) ![forks](https://img.shields.io/github/forks/avalahEE/pdfjs_disable_eval.svg)

- [https://github.com/PenguinCabinet/CVE-2024-4367-hands-on](https://github.com/PenguinCabinet/CVE-2024-4367-hands-on) :  ![starts](https://img.shields.io/github/stars/PenguinCabinet/CVE-2024-4367-hands-on.svg) ![forks](https://img.shields.io/github/forks/PenguinCabinet/CVE-2024-4367-hands-on.svg)

- [https://github.com/pedrochalegre7/CVE-2024-4367-pdf-sample](https://github.com/pedrochalegre7/CVE-2024-4367-pdf-sample) :  ![starts](https://img.shields.io/github/stars/pedrochalegre7/CVE-2024-4367-pdf-sample.svg) ![forks](https://img.shields.io/github/forks/pedrochalegre7/CVE-2024-4367-pdf-sample.svg)

## CVE-2024-4358
 In Progress Telerik Report Server, version 2024 Q1 (10.0.24.305) or earlier, on IIS, an unauthenticated attacker can gain access to Telerik Report Server restricted functionality via an authentication bypass vulnerability.



- [https://github.com/sinsinology/CVE-2024-4358](https://github.com/sinsinology/CVE-2024-4358) :  ![starts](https://img.shields.io/github/stars/sinsinology/CVE-2024-4358.svg) ![forks](https://img.shields.io/github/forks/sinsinology/CVE-2024-4358.svg)

- [https://github.com/Sk1dr0wz/CVE-2024-4358_Mass_Exploit](https://github.com/Sk1dr0wz/CVE-2024-4358_Mass_Exploit) :  ![starts](https://img.shields.io/github/stars/Sk1dr0wz/CVE-2024-4358_Mass_Exploit.svg) ![forks](https://img.shields.io/github/forks/Sk1dr0wz/CVE-2024-4358_Mass_Exploit.svg)

- [https://github.com/verylazytech/CVE-2024-4358](https://github.com/verylazytech/CVE-2024-4358) :  ![starts](https://img.shields.io/github/stars/verylazytech/CVE-2024-4358.svg) ![forks](https://img.shields.io/github/forks/verylazytech/CVE-2024-4358.svg)

- [https://github.com/RevoltSecurities/CVE-2024-4358](https://github.com/RevoltSecurities/CVE-2024-4358) :  ![starts](https://img.shields.io/github/stars/RevoltSecurities/CVE-2024-4358.svg) ![forks](https://img.shields.io/github/forks/RevoltSecurities/CVE-2024-4358.svg)

- [https://github.com/Harydhk7/CVE-2024-4358](https://github.com/Harydhk7/CVE-2024-4358) :  ![starts](https://img.shields.io/github/stars/Harydhk7/CVE-2024-4358.svg) ![forks](https://img.shields.io/github/forks/Harydhk7/CVE-2024-4358.svg)

## CVE-2024-4352
 The Tutor LMS Pro plugin for WordPress is vulnerable to unauthorized access of data, modification of data, loss of data due to a missing capability check on the 'get_calendar_materials' function. The plugin is also vulnerable to SQL Injection via the ‘year’ parameter of that function due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for authenticated attackers, with subscriber-level permissions and above, to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/truonghuuphuc/CVE-2024-4352-Poc](https://github.com/truonghuuphuc/CVE-2024-4352-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-4352-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-4352-Poc.svg)

## CVE-2024-4351
 The Tutor LMS Pro plugin for WordPress is vulnerable to unauthorized access of data, modification of data, loss of data due to a missing capability check on the 'authenticate' function in all versions up to, and including, 2.7.0. This makes it possible for authenticated attackers, with subscriber-level permissions and above, to gain control of an existing administrator account.



- [https://github.com/ZSECURE/CVE-2024-4351](https://github.com/ZSECURE/CVE-2024-4351) :  ![starts](https://img.shields.io/github/stars/ZSECURE/CVE-2024-4351.svg) ![forks](https://img.shields.io/github/forks/ZSECURE/CVE-2024-4351.svg)

## CVE-2024-4323
 A memory corruption vulnerability in Fluent Bit versions 2.0.7 thru 3.0.3. This issue lies in the embedded http server’s parsing of trace requests and may result in denial of service conditions, information disclosure, or remote code execution.



- [https://github.com/skilfoy/CVE-2024-4323-Exploit-POC](https://github.com/skilfoy/CVE-2024-4323-Exploit-POC) :  ![starts](https://img.shields.io/github/stars/skilfoy/CVE-2024-4323-Exploit-POC.svg) ![forks](https://img.shields.io/github/forks/skilfoy/CVE-2024-4323-Exploit-POC.svg)

- [https://github.com/d0rb/CVE-2024-4323](https://github.com/d0rb/CVE-2024-4323) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2024-4323.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2024-4323.svg)

- [https://github.com/yuansec/CVE-2024-4323-dos_poc](https://github.com/yuansec/CVE-2024-4323-dos_poc) :  ![starts](https://img.shields.io/github/stars/yuansec/CVE-2024-4323-dos_poc.svg) ![forks](https://img.shields.io/github/forks/yuansec/CVE-2024-4323-dos_poc.svg)

## CVE-2024-4320
 A remote code execution (RCE) vulnerability exists in the '/install_extension' endpoint of the parisneo/lollms-webui application, specifically within the `@router.post("/install_extension")` route handler. The vulnerability arises due to improper handling of the `name` parameter in the `ExtensionBuilder().build_extension()` method, which allows for local file inclusion (LFI) leading to arbitrary code execution. An attacker can exploit this vulnerability by crafting a malicious `name` parameter that causes the server to load and execute a `__init__.py` file from an arbitrary location, such as the upload directory for discussions. This vulnerability affects the latest version of parisneo/lollms-webui and can lead to remote code execution without requiring user interaction, especially when the application is exposed to an external endpoint or operated in headless mode.



- [https://github.com/bolkv/CVE-2024-4320](https://github.com/bolkv/CVE-2024-4320) :  ![starts](https://img.shields.io/github/stars/bolkv/CVE-2024-4320.svg) ![forks](https://img.shields.io/github/forks/bolkv/CVE-2024-4320.svg)

## CVE-2024-4295
 The Email Subscribers by Icegram Express plugin for WordPress is vulnerable to SQL Injection via the ‘hash’ parameter in all versions up to, and including, 5.7.20 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/truonghuuphuc/CVE-2024-4295-Poc](https://github.com/truonghuuphuc/CVE-2024-4295-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-4295-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-4295-Poc.svg)

- [https://github.com/cve-2024/CVE-2024-4295-Poc](https://github.com/cve-2024/CVE-2024-4295-Poc) :  ![starts](https://img.shields.io/github/stars/cve-2024/CVE-2024-4295-Poc.svg) ![forks](https://img.shields.io/github/forks/cve-2024/CVE-2024-4295-Poc.svg)

## CVE-2024-4232
 This vulnerability exists in Digisol Router (DG-GR1321: Hardware version 3.7L;  Firmware version : v3.2.02) due to lack of encryption or hashing in storing of passwords within the router's firmware/ database. An attacker with physical access could exploit this by extracting the firmware and reverse engineer the binary data to access the plaintext passwords on the vulnerable system.

Successful exploitation of this vulnerability could allow the attacker to gain unauthorized access to the targeted system.



- [https://github.com/Redfox-Security/Digisol-DG--GR1321-s-Password-Storage-in-Plaintext--CVE-2024-4232](https://github.com/Redfox-Security/Digisol-DG--GR1321-s-Password-Storage-in-Plaintext--CVE-2024-4232) :  ![starts](https://img.shields.io/github/stars/Redfox-Security/Digisol-DG--GR1321-s-Password-Storage-in-Plaintext--CVE-2024-4232.svg) ![forks](https://img.shields.io/github/forks/Redfox-Security/Digisol-DG--GR1321-s-Password-Storage-in-Plaintext--CVE-2024-4232.svg)

- [https://github.com/Redfox-Security/Digisol-DG-GR1321-s-Password-Storage-in-Plaintext-CVE-2024-4232](https://github.com/Redfox-Security/Digisol-DG-GR1321-s-Password-Storage-in-Plaintext-CVE-2024-4232) :  ![starts](https://img.shields.io/github/stars/Redfox-Security/Digisol-DG-GR1321-s-Password-Storage-in-Plaintext-CVE-2024-4232.svg) ![forks](https://img.shields.io/github/forks/Redfox-Security/Digisol-DG-GR1321-s-Password-Storage-in-Plaintext-CVE-2024-4232.svg)

## CVE-2024-4231
 This vulnerability exists in Digisol Router (DG-GR1321: Hardware version 3.7L;  Firmware version : v3.2.02) due to presence of root terminal access on a serial interface without proper access control. An attacker with physical access could exploit this by identifying UART pins and accessing the root shell on the vulnerable system.

Successful exploitation of this vulnerability could allow the attacker to access the sensitive information on the targeted system.



- [https://github.com/Redfox-Security/Digisol-DG-GR1321-s-Improper-Access-Control-CVE-2024-4231](https://github.com/Redfox-Security/Digisol-DG-GR1321-s-Improper-Access-Control-CVE-2024-4231) :  ![starts](https://img.shields.io/github/stars/Redfox-Security/Digisol-DG-GR1321-s-Improper-Access-Control-CVE-2024-4231.svg) ![forks](https://img.shields.io/github/forks/Redfox-Security/Digisol-DG-GR1321-s-Improper-Access-Control-CVE-2024-4231.svg)

- [https://github.com/Redfox-Security/Digisol-DG-GR1321-s-Improper-Access-Control--CVE-2024--4231](https://github.com/Redfox-Security/Digisol-DG-GR1321-s-Improper-Access-Control--CVE-2024--4231) :  ![starts](https://img.shields.io/github/stars/Redfox-Security/Digisol-DG-GR1321-s-Improper-Access-Control--CVE-2024--4231.svg) ![forks](https://img.shields.io/github/forks/Redfox-Security/Digisol-DG-GR1321-s-Improper-Access-Control--CVE-2024--4231.svg)

## CVE-2024-4130
 A DLL hijack vulnerability was reported in Lenovo App Store that could allow a local attacker to execute code with elevated privileges.



- [https://github.com/patrickdeanramos/CVE-2024-41302-Bookea-tu-Mesa-is-vulnerable-to-SQL-Injection](https://github.com/patrickdeanramos/CVE-2024-41302-Bookea-tu-Mesa-is-vulnerable-to-SQL-Injection) :  ![starts](https://img.shields.io/github/stars/patrickdeanramos/CVE-2024-41302-Bookea-tu-Mesa-is-vulnerable-to-SQL-Injection.svg) ![forks](https://img.shields.io/github/forks/patrickdeanramos/CVE-2024-41302-Bookea-tu-Mesa-is-vulnerable-to-SQL-Injection.svg)

- [https://github.com/patrickdeanramos/CVE-2024-41301-Bookea-tu-Mesa-is-vulnerable-to-Stored-Cross-Site-Scripting](https://github.com/patrickdeanramos/CVE-2024-41301-Bookea-tu-Mesa-is-vulnerable-to-Stored-Cross-Site-Scripting) :  ![starts](https://img.shields.io/github/stars/patrickdeanramos/CVE-2024-41301-Bookea-tu-Mesa-is-vulnerable-to-Stored-Cross-Site-Scripting.svg) ![forks](https://img.shields.io/github/forks/patrickdeanramos/CVE-2024-41301-Bookea-tu-Mesa-is-vulnerable-to-Stored-Cross-Site-Scripting.svg)

## CVE-2024-4110
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/d0rb/CVE-2024-41107](https://github.com/d0rb/CVE-2024-41107) :  ![starts](https://img.shields.io/github/stars/d0rb/CVE-2024-41107.svg) ![forks](https://img.shields.io/github/forks/d0rb/CVE-2024-41107.svg)

## CVE-2024-4051
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Jansen-C-Moreira/CVE-2024-40510](https://github.com/Jansen-C-Moreira/CVE-2024-40510) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40510.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40510.svg)

- [https://github.com/Jansen-C-Moreira/CVE-2024-40511](https://github.com/Jansen-C-Moreira/CVE-2024-40511) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40511.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40511.svg)

- [https://github.com/Jansen-C-Moreira/CVE-2024-40512](https://github.com/Jansen-C-Moreira/CVE-2024-40512) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40512.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40512.svg)

## CVE-2024-4050
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Jansen-C-Moreira/CVE-2024-40507](https://github.com/Jansen-C-Moreira/CVE-2024-40507) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40507.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40507.svg)

- [https://github.com/Jansen-C-Moreira/CVE-2024-40508](https://github.com/Jansen-C-Moreira/CVE-2024-40508) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40508.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40508.svg)

- [https://github.com/Jansen-C-Moreira/CVE-2024-40506](https://github.com/Jansen-C-Moreira/CVE-2024-40506) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40506.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40506.svg)

- [https://github.com/Jansen-C-Moreira/CVE-2024-40509](https://github.com/Jansen-C-Moreira/CVE-2024-40509) :  ![starts](https://img.shields.io/github/stars/Jansen-C-Moreira/CVE-2024-40509.svg) ![forks](https://img.shields.io/github/forks/Jansen-C-Moreira/CVE-2024-40509.svg)

- [https://github.com/nitipoom-jar/CVE-2024-40500](https://github.com/nitipoom-jar/CVE-2024-40500) :  ![starts](https://img.shields.io/github/stars/nitipoom-jar/CVE-2024-40500.svg) ![forks](https://img.shields.io/github/forks/nitipoom-jar/CVE-2024-40500.svg)

## CVE-2024-4049
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/Dirac231/CVE-2024-40498](https://github.com/Dirac231/CVE-2024-40498) :  ![starts](https://img.shields.io/github/stars/Dirac231/CVE-2024-40498.svg) ![forks](https://img.shields.io/github/forks/Dirac231/CVE-2024-40498.svg)

- [https://github.com/minendie/POC_CVE-2024-40492](https://github.com/minendie/POC_CVE-2024-40492) :  ![starts](https://img.shields.io/github/stars/minendie/POC_CVE-2024-40492.svg) ![forks](https://img.shields.io/github/forks/minendie/POC_CVE-2024-40492.svg)

## CVE-2024-4040
 A server side template injection vulnerability in CrushFTP in all versions before 10.7.1 and 11.1.0 on all platforms allows unauthenticated remote attackers to read files from the filesystem outside of the VFS Sandbox, bypass authentication to gain administrative access, and perform remote code execution on the server.




- [https://github.com/Stuub/CVE-2024-4040-SSTI-LFI-PoC](https://github.com/Stuub/CVE-2024-4040-SSTI-LFI-PoC) :  ![starts](https://img.shields.io/github/stars/Stuub/CVE-2024-4040-SSTI-LFI-PoC.svg) ![forks](https://img.shields.io/github/forks/Stuub/CVE-2024-4040-SSTI-LFI-PoC.svg)

- [https://github.com/airbus-cert/CVE-2024-4040](https://github.com/airbus-cert/CVE-2024-4040) :  ![starts](https://img.shields.io/github/stars/airbus-cert/CVE-2024-4040.svg) ![forks](https://img.shields.io/github/forks/airbus-cert/CVE-2024-4040.svg)

- [https://github.com/rbih-boulanouar/CVE-2024-4040](https://github.com/rbih-boulanouar/CVE-2024-4040) :  ![starts](https://img.shields.io/github/stars/rbih-boulanouar/CVE-2024-4040.svg) ![forks](https://img.shields.io/github/forks/rbih-boulanouar/CVE-2024-4040.svg)

- [https://github.com/gotr00t0day/CVE-2024-4040](https://github.com/gotr00t0day/CVE-2024-4040) :  ![starts](https://img.shields.io/github/stars/gotr00t0day/CVE-2024-4040.svg) ![forks](https://img.shields.io/github/forks/gotr00t0day/CVE-2024-4040.svg)

- [https://github.com/Mohammaddvd/CVE-2024-4040](https://github.com/Mohammaddvd/CVE-2024-4040) :  ![starts](https://img.shields.io/github/stars/Mohammaddvd/CVE-2024-4040.svg) ![forks](https://img.shields.io/github/forks/Mohammaddvd/CVE-2024-4040.svg)

- [https://github.com/entroychang/CVE-2024-4040](https://github.com/entroychang/CVE-2024-4040) :  ![starts](https://img.shields.io/github/stars/entroychang/CVE-2024-4040.svg) ![forks](https://img.shields.io/github/forks/entroychang/CVE-2024-4040.svg)

- [https://github.com/jakabakos/CVE-2024-4040-CrushFTP-File-Read-vulnerability](https://github.com/jakabakos/CVE-2024-4040-CrushFTP-File-Read-vulnerability) :  ![starts](https://img.shields.io/github/stars/jakabakos/CVE-2024-4040-CrushFTP-File-Read-vulnerability.svg) ![forks](https://img.shields.io/github/forks/jakabakos/CVE-2024-4040-CrushFTP-File-Read-vulnerability.svg)

- [https://github.com/tucommenceapousser/CVE-2024-4040-Scanner](https://github.com/tucommenceapousser/CVE-2024-4040-Scanner) :  ![starts](https://img.shields.io/github/stars/tucommenceapousser/CVE-2024-4040-Scanner.svg) ![forks](https://img.shields.io/github/forks/tucommenceapousser/CVE-2024-4040-Scanner.svg)

- [https://github.com/olebris/CVE-2024-4040](https://github.com/olebris/CVE-2024-4040) :  ![starts](https://img.shields.io/github/stars/olebris/CVE-2024-4040.svg) ![forks](https://img.shields.io/github/forks/olebris/CVE-2024-4040.svg)

- [https://github.com/0xN7y/CVE-2024-4040](https://github.com/0xN7y/CVE-2024-4040) :  ![starts](https://img.shields.io/github/stars/0xN7y/CVE-2024-4040.svg) ![forks](https://img.shields.io/github/forks/0xN7y/CVE-2024-4040.svg)

- [https://github.com/Mufti22/CVE-2024-4040](https://github.com/Mufti22/CVE-2024-4040) :  ![starts](https://img.shields.io/github/stars/Mufti22/CVE-2024-4040.svg) ![forks](https://img.shields.io/github/forks/Mufti22/CVE-2024-4040.svg)

- [https://github.com/1ncendium/CVE-2024-4040](https://github.com/1ncendium/CVE-2024-4040) :  ![starts](https://img.shields.io/github/stars/1ncendium/CVE-2024-4040.svg) ![forks](https://img.shields.io/github/forks/1ncendium/CVE-2024-4040.svg)

- [https://github.com/Praison001/CVE-2024-4040-CrushFTP-server](https://github.com/Praison001/CVE-2024-4040-CrushFTP-server) :  ![starts](https://img.shields.io/github/stars/Praison001/CVE-2024-4040-CrushFTP-server.svg) ![forks](https://img.shields.io/github/forks/Praison001/CVE-2024-4040-CrushFTP-server.svg)

- [https://github.com/ill-deed/CrushFTP-CVE-2024-4040-illdeed](https://github.com/ill-deed/CrushFTP-CVE-2024-4040-illdeed) :  ![starts](https://img.shields.io/github/stars/ill-deed/CrushFTP-CVE-2024-4040-illdeed.svg) ![forks](https://img.shields.io/github/forks/ill-deed/CrushFTP-CVE-2024-4040-illdeed.svg)

## CVE-2024-4008
 FDSK Leak in ABB, Busch-Jaeger, FTS Display (version 1.00) and BCU (version 1.3.0.33) allows attacker to take control via access to local KNX Bus-System



- [https://github.com/perras/CVE-2024-40080](https://github.com/perras/CVE-2024-40080) :  ![starts](https://img.shields.io/github/stars/perras/CVE-2024-40080.svg) ![forks](https://img.shields.io/github/forks/perras/CVE-2024-40080.svg)

## CVE-2024-3922
 The Dokan Pro plugin for WordPress is vulnerable to SQL Injection via the 'code' parameter in all versions up to, and including, 3.10.3 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/truonghuuphuc/CVE-2024-3922-Poc](https://github.com/truonghuuphuc/CVE-2024-3922-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-3922-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-3922-Poc.svg)

## CVE-2024-3919
 The OpenPGP Form Encryption for WordPress plugin before 1.5.1 does not validate and escape some of its shortcode attributes before outputting them back in a page/post where the shortcode is embed, which could allow users with the contributor role and above to perform Stored Cross-Site Scripting attacks.



- [https://github.com/phtcloud-dev/CVE-2024-39199](https://github.com/phtcloud-dev/CVE-2024-39199) :  ![starts](https://img.shields.io/github/stars/phtcloud-dev/CVE-2024-39199.svg) ![forks](https://img.shields.io/github/forks/phtcloud-dev/CVE-2024-39199.svg)

## CVE-2024-3867
 The archive-tainacan-collection theme for WordPress is vulnerable to Reflected Cross-Site Scripting due to the use of add_query_arg without appropriate escaping on the URL in version 2.7.2. This makes it possible for unauthenticated attackers to inject arbitrary web scripts in pages that execute if they can successfully trick a user into performing an action such as clicking on a link.



- [https://github.com/c4cnm/CVE-2024-3867](https://github.com/c4cnm/CVE-2024-3867) :  ![starts](https://img.shields.io/github/stars/c4cnm/CVE-2024-3867.svg) ![forks](https://img.shields.io/github/forks/c4cnm/CVE-2024-3867.svg)

## CVE-2024-3807
 The Porto theme for WordPress is vulnerable to Local File Inclusion in all versions up to, and including, 7.1.0 via 'porto_page_header_shortcode_type', 'slideshow_type' and 'post_layout' post meta. This makes it possible for authenticated attackers, with contributor-level and above permissions, to include and execute arbitrary files on the server, allowing the execution of any PHP code in those files. This can be used to bypass access controls, obtain sensitive data, or achieve code execution in cases where php file type can be uploaded and included. This was partially patched in version 7.1.0 and fully patched in version 7.1.1.



- [https://github.com/truonghuuphuc/CVE-2024-3806-AND-CVE-2024-3807-Poc](https://github.com/truonghuuphuc/CVE-2024-3806-AND-CVE-2024-3807-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-3806-AND-CVE-2024-3807-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-3806-AND-CVE-2024-3807-Poc.svg)

## CVE-2024-3806
 The Porto theme for WordPress is vulnerable to Local File Inclusion in all versions up to, and including, 7.1.0 via the 'porto_ajax_posts' function. This makes it possible for unauthenticated attackers to include and execute arbitrary files on the server, allowing the execution of any PHP code in those files. This can be used to bypass access controls, obtain sensitive data, or achieve code execution in cases where php file type can be uploaded and included.



- [https://github.com/truonghuuphuc/CVE-2024-3806-AND-CVE-2024-3807-Poc](https://github.com/truonghuuphuc/CVE-2024-3806-AND-CVE-2024-3807-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-3806-AND-CVE-2024-3807-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-3806-AND-CVE-2024-3807-Poc.svg)

- [https://github.com/RandomRobbieBF/CVE-2024-3806](https://github.com/RandomRobbieBF/CVE-2024-3806) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-3806.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-3806.svg)

## CVE-2024-3701
 The system application (com.transsion.kolun.aiservice) component does not perform an authentication check, which allows attackers to perform malicious exploitations and affect system services.



- [https://github.com/SarpantKeltiek/CVE-2024-37010](https://github.com/SarpantKeltiek/CVE-2024-37010) :  ![starts](https://img.shields.io/github/stars/SarpantKeltiek/CVE-2024-37010.svg) ![forks](https://img.shields.io/github/forks/SarpantKeltiek/CVE-2024-37010.svg)

## CVE-2024-3690
 A vulnerability classified as critical was found in PHPGurukul Small CRM 3.0. Affected by this vulnerability is an unknown functionality of the component Change Password Handler. The manipulation leads to sql injection. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-260479.



- [https://github.com/taeseongk/CVE-2024-3690](https://github.com/taeseongk/CVE-2024-3690) :  ![starts](https://img.shields.io/github/stars/taeseongk/CVE-2024-3690.svg) ![forks](https://img.shields.io/github/forks/taeseongk/CVE-2024-3690.svg)

## CVE-2024-3661
 DHCP can add routes to a client’s routing table via the classless static route option (121). VPN-based security solutions that rely on routes to redirect traffic can be forced to leak traffic over the physical interface. An attacker on the same local network can read, disrupt, or possibly modify network traffic that was expected to be protected by the VPN.



- [https://github.com/Roundthe-clock/CVE-2024-3661VPN](https://github.com/Roundthe-clock/CVE-2024-3661VPN) :  ![starts](https://img.shields.io/github/stars/Roundthe-clock/CVE-2024-3661VPN.svg) ![forks](https://img.shields.io/github/forks/Roundthe-clock/CVE-2024-3661VPN.svg)

## CVE-2024-3640
 An unquoted executable path exists in the Rockwell Automation FactoryTalk® Remote Access™ possibly resulting in remote code execution if exploited. While running the FTRA installer package, the executable path is not properly quoted, which could allow a threat actor to enter a malicious executable and run it as a System user. A threat actor needs admin privileges to exploit this vulnerability.



- [https://github.com/H1ng007/CVE-2024-3640_WafBypass](https://github.com/H1ng007/CVE-2024-3640_WafBypass) :  ![starts](https://img.shields.io/github/stars/H1ng007/CVE-2024-3640_WafBypass.svg) ![forks](https://img.shields.io/github/forks/H1ng007/CVE-2024-3640_WafBypass.svg)

## CVE-2024-3605
 The WP Hotel Booking plugin for WordPress is vulnerable to SQL Injection via the 'room_type' parameter of the /wphb/v1/rooms/search-rooms REST API endpoint in all versions up to, and including, 2.1.0 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/RandomRobbieBF/CVE-2024-3605](https://github.com/RandomRobbieBF/CVE-2024-3605) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-3605.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-3605.svg)

## CVE-2024-3596
 RADIUS Protocol under RFC 2865 is susceptible to forgery attacks by a local attacker who can modify any valid Response (Access-Accept, Access-Reject, or Access-Challenge) to any other response using a chosen-prefix collision attack against MD5 Response Authenticator signature.



- [https://github.com/alperenugurlu/CVE-2024-3596-Detector](https://github.com/alperenugurlu/CVE-2024-3596-Detector) :  ![starts](https://img.shields.io/github/stars/alperenugurlu/CVE-2024-3596-Detector.svg) ![forks](https://img.shields.io/github/forks/alperenugurlu/CVE-2024-3596-Detector.svg)

## CVE-2024-3568
 The huggingface/transformers library is vulnerable to arbitrary code execution through deserialization of untrusted data within the `load_repo_checkpoint()` function of the `TFPreTrainedModel()` class. Attackers can execute arbitrary code and commands by crafting a malicious serialized payload, exploiting the use of `pickle.load()` on data from potentially untrusted sources. This vulnerability allows for remote code execution (RCE) by deceiving victims into loading a seemingly harmless checkpoint during a normal training process, thereby enabling attackers to execute arbitrary code on the targeted machine.



- [https://github.com/rooobeam/Pickle-Deserialization-Exploit-in-Transformers](https://github.com/rooobeam/Pickle-Deserialization-Exploit-in-Transformers) :  ![starts](https://img.shields.io/github/stars/rooobeam/Pickle-Deserialization-Exploit-in-Transformers.svg) ![forks](https://img.shields.io/github/forks/rooobeam/Pickle-Deserialization-Exploit-in-Transformers.svg)

## CVE-2024-3552
 The Web Directory Free WordPress plugin before 1.7.0 does not sanitise and escape a parameter before using it in a SQL statement via an AJAX action available to unauthenticated users, leading to a SQL injection with different techniques like UNION, Time-Based and Error-Based.



- [https://github.com/truonghuuphuc/CVE-2024-3552-Poc](https://github.com/truonghuuphuc/CVE-2024-3552-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-3552-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-3552-Poc.svg)

- [https://github.com/KiPhuong/cve-2024-3552](https://github.com/KiPhuong/cve-2024-3552) :  ![starts](https://img.shields.io/github/stars/KiPhuong/cve-2024-3552.svg) ![forks](https://img.shields.io/github/forks/KiPhuong/cve-2024-3552.svg)

- [https://github.com/KiPhuong/challenge-cve-2024-3552](https://github.com/KiPhuong/challenge-cve-2024-3552) :  ![starts](https://img.shields.io/github/stars/KiPhuong/challenge-cve-2024-3552.svg) ![forks](https://img.shields.io/github/forks/KiPhuong/challenge-cve-2024-3552.svg)

## CVE-2024-3495
 The Country State City Dropdown CF7 plugin for WordPress is vulnerable to SQL Injection via the ‘cnt’ and 'sid' parameters in versions up to, and including, 2.7.2 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/truonghuuphuc/CVE-2024-3495-Poc](https://github.com/truonghuuphuc/CVE-2024-3495-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-3495-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-3495-Poc.svg)

- [https://github.com/issamjr/CVE-2024-2876](https://github.com/issamjr/CVE-2024-2876) :  ![starts](https://img.shields.io/github/stars/issamjr/CVE-2024-2876.svg) ![forks](https://img.shields.io/github/forks/issamjr/CVE-2024-2876.svg)

- [https://github.com/zomasec/CVE-2024-3495-POC](https://github.com/zomasec/CVE-2024-3495-POC) :  ![starts](https://img.shields.io/github/stars/zomasec/CVE-2024-3495-POC.svg) ![forks](https://img.shields.io/github/forks/zomasec/CVE-2024-3495-POC.svg)

## CVE-2024-3435
 A path traversal vulnerability exists in the 'save_settings' endpoint of the parisneo/lollms-webui application, affecting versions up to the latest release before 9.5. The vulnerability arises due to insufficient sanitization of the 'config' parameter in the 'apply_settings' function, allowing an attacker to manipulate the application's configuration by sending specially crafted JSON payloads. This could lead to remote code execution (RCE) by bypassing existing patches designed to mitigate such vulnerabilities.



- [https://github.com/ymuraki-csc/cve-2024-3435](https://github.com/ymuraki-csc/cve-2024-3435) :  ![starts](https://img.shields.io/github/stars/ymuraki-csc/cve-2024-3435.svg) ![forks](https://img.shields.io/github/forks/ymuraki-csc/cve-2024-3435.svg)

## CVE-2024-3400
 A command injection as a result of arbitrary file creation vulnerability in the GlobalProtect feature of Palo Alto Networks PAN-OS software for specific PAN-OS versions and distinct feature configurations may enable an unauthenticated attacker to execute arbitrary code with root privileges on the firewall.

Cloud NGFW, Panorama appliances, and Prisma Access are not impacted by this vulnerability.



- [https://github.com/h4x0r-dz/CVE-2024-3400](https://github.com/h4x0r-dz/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/h4x0r-dz/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/h4x0r-dz/CVE-2024-3400.svg)

- [https://github.com/W01fh4cker/CVE-2024-3400-RCE-Scan](https://github.com/W01fh4cker/CVE-2024-3400-RCE-Scan) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/CVE-2024-3400-RCE-Scan.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/CVE-2024-3400-RCE-Scan.svg)

- [https://github.com/0x0d3ad/CVE-2024-3400](https://github.com/0x0d3ad/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/0x0d3ad/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/0x0d3ad/CVE-2024-3400.svg)

- [https://github.com/ihebski/CVE-2024-3400](https://github.com/ihebski/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/ihebski/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/ihebski/CVE-2024-3400.svg)

- [https://github.com/momika233/CVE-2024-3400](https://github.com/momika233/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/momika233/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/momika233/CVE-2024-3400.svg)

- [https://github.com/Chocapikk/CVE-2024-3400](https://github.com/Chocapikk/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-3400.svg)

- [https://github.com/Yuvvi01/CVE-2024-3400](https://github.com/Yuvvi01/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/Yuvvi01/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/Yuvvi01/CVE-2024-3400.svg)

- [https://github.com/ak1t4/CVE-2024-3400](https://github.com/ak1t4/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/ak1t4/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/ak1t4/CVE-2024-3400.svg)

- [https://github.com/AdaniKamal/CVE-2024-3400](https://github.com/AdaniKamal/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/AdaniKamal/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/AdaniKamal/CVE-2024-3400.svg)

- [https://github.com/XiaomingX/CVE-2024-3400-poc](https://github.com/XiaomingX/CVE-2024-3400-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/CVE-2024-3400-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/CVE-2024-3400-poc.svg)

- [https://github.com/zam89/CVE-2024-3400-pot](https://github.com/zam89/CVE-2024-3400-pot) :  ![starts](https://img.shields.io/github/stars/zam89/CVE-2024-3400-pot.svg) ![forks](https://img.shields.io/github/forks/zam89/CVE-2024-3400-pot.svg)

- [https://github.com/schooldropout1337/CVE-2024-3400](https://github.com/schooldropout1337/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/schooldropout1337/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/schooldropout1337/CVE-2024-3400.svg)

- [https://github.com/0xr2r/CVE-2024-3400-Palo-Alto-OS-Command-Injection](https://github.com/0xr2r/CVE-2024-3400-Palo-Alto-OS-Command-Injection) :  ![starts](https://img.shields.io/github/stars/0xr2r/CVE-2024-3400-Palo-Alto-OS-Command-Injection.svg) ![forks](https://img.shields.io/github/forks/0xr2r/CVE-2024-3400-Palo-Alto-OS-Command-Injection.svg)

- [https://github.com/HackingLZ/panrapidcheck](https://github.com/HackingLZ/panrapidcheck) :  ![starts](https://img.shields.io/github/stars/HackingLZ/panrapidcheck.svg) ![forks](https://img.shields.io/github/forks/HackingLZ/panrapidcheck.svg)

- [https://github.com/marconesler/CVE-2024-3400](https://github.com/marconesler/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/marconesler/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/marconesler/CVE-2024-3400.svg)

- [https://github.com/retkoussa/CVE-2024-3400](https://github.com/retkoussa/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/retkoussa/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/retkoussa/CVE-2024-3400.svg)

- [https://github.com/swaybs/CVE-2024-3400](https://github.com/swaybs/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/swaybs/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/swaybs/CVE-2024-3400.svg)

- [https://github.com/ZephrFish/CVE-2024-3400-Canary](https://github.com/ZephrFish/CVE-2024-3400-Canary) :  ![starts](https://img.shields.io/github/stars/ZephrFish/CVE-2024-3400-Canary.svg) ![forks](https://img.shields.io/github/forks/ZephrFish/CVE-2024-3400-Canary.svg)

- [https://github.com/CerTusHack/CVE-2024-3400-PoC](https://github.com/CerTusHack/CVE-2024-3400-PoC) :  ![starts](https://img.shields.io/github/stars/CerTusHack/CVE-2024-3400-PoC.svg) ![forks](https://img.shields.io/github/forks/CerTusHack/CVE-2024-3400-PoC.svg)

- [https://github.com/CONDITIONBLACK/CVE-2024-3400-POC](https://github.com/CONDITIONBLACK/CVE-2024-3400-POC) :  ![starts](https://img.shields.io/github/stars/CONDITIONBLACK/CVE-2024-3400-POC.svg) ![forks](https://img.shields.io/github/forks/CONDITIONBLACK/CVE-2024-3400-POC.svg)

- [https://github.com/CyprianAtsyor/letsdefend-cve2024-3400-case-study](https://github.com/CyprianAtsyor/letsdefend-cve2024-3400-case-study) :  ![starts](https://img.shields.io/github/stars/CyprianAtsyor/letsdefend-cve2024-3400-case-study.svg) ![forks](https://img.shields.io/github/forks/CyprianAtsyor/letsdefend-cve2024-3400-case-study.svg)

- [https://github.com/tfrederick74656/cve-2024-3400-poc](https://github.com/tfrederick74656/cve-2024-3400-poc) :  ![starts](https://img.shields.io/github/stars/tfrederick74656/cve-2024-3400-poc.svg) ![forks](https://img.shields.io/github/forks/tfrederick74656/cve-2024-3400-poc.svg)

- [https://github.com/workshop748/CVE-2024-3400](https://github.com/workshop748/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/workshop748/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/workshop748/CVE-2024-3400.svg)

- [https://github.com/LoanVitor/CVE-2024-3400-](https://github.com/LoanVitor/CVE-2024-3400-) :  ![starts](https://img.shields.io/github/stars/LoanVitor/CVE-2024-3400-.svg) ![forks](https://img.shields.io/github/forks/LoanVitor/CVE-2024-3400-.svg)

- [https://github.com/Kr0ff/cve-2024-3400](https://github.com/Kr0ff/cve-2024-3400) :  ![starts](https://img.shields.io/github/stars/Kr0ff/cve-2024-3400.svg) ![forks](https://img.shields.io/github/forks/Kr0ff/cve-2024-3400.svg)

- [https://github.com/nanwinata/CVE-2024-3400](https://github.com/nanwinata/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/nanwinata/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/nanwinata/CVE-2024-3400.svg)

- [https://github.com/FoxyProxys/CVE-2024-3400](https://github.com/FoxyProxys/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/FoxyProxys/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/FoxyProxys/CVE-2024-3400.svg)

- [https://github.com/Ravaan21/CVE-2024-3400](https://github.com/Ravaan21/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/Ravaan21/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/Ravaan21/CVE-2024-3400.svg)

- [https://github.com/codeblueprint/CVE-2024-3400](https://github.com/codeblueprint/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/codeblueprint/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/codeblueprint/CVE-2024-3400.svg)

- [https://github.com/pwnj0hn/CVE-2024-3400](https://github.com/pwnj0hn/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/pwnj0hn/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/pwnj0hn/CVE-2024-3400.svg)

- [https://github.com/MrR0b0t19/CVE-2024-3400](https://github.com/MrR0b0t19/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/MrR0b0t19/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/MrR0b0t19/CVE-2024-3400.svg)

- [https://github.com/hahasagined/CVE-2024-3400](https://github.com/hahasagined/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/hahasagined/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/hahasagined/CVE-2024-3400.svg)

- [https://github.com/iwallarm/cve-2024-3400](https://github.com/iwallarm/cve-2024-3400) :  ![starts](https://img.shields.io/github/stars/iwallarm/cve-2024-3400.svg) ![forks](https://img.shields.io/github/forks/iwallarm/cve-2024-3400.svg)

- [https://github.com/andrelia-hacks/CVE-2024-3400](https://github.com/andrelia-hacks/CVE-2024-3400) :  ![starts](https://img.shields.io/github/stars/andrelia-hacks/CVE-2024-3400.svg) ![forks](https://img.shields.io/github/forks/andrelia-hacks/CVE-2024-3400.svg)

- [https://github.com/sxyrxyy/CVE-2024-3400-Check](https://github.com/sxyrxyy/CVE-2024-3400-Check) :  ![starts](https://img.shields.io/github/stars/sxyrxyy/CVE-2024-3400-Check.svg) ![forks](https://img.shields.io/github/forks/sxyrxyy/CVE-2024-3400-Check.svg)

- [https://github.com/index2014/CVE-2024-3400-Checker](https://github.com/index2014/CVE-2024-3400-Checker) :  ![starts](https://img.shields.io/github/stars/index2014/CVE-2024-3400-Checker.svg) ![forks](https://img.shields.io/github/forks/index2014/CVE-2024-3400-Checker.svg)

- [https://github.com/terminalJunki3/CVE-2024-3400-Checker](https://github.com/terminalJunki3/CVE-2024-3400-Checker) :  ![starts](https://img.shields.io/github/stars/terminalJunki3/CVE-2024-3400-Checker.svg) ![forks](https://img.shields.io/github/forks/terminalJunki3/CVE-2024-3400-Checker.svg)

- [https://github.com/MurrayR0123/CVE-2024-3400-Compromise-Checker](https://github.com/MurrayR0123/CVE-2024-3400-Compromise-Checker) :  ![starts](https://img.shields.io/github/stars/MurrayR0123/CVE-2024-3400-Compromise-Checker.svg) ![forks](https://img.shields.io/github/forks/MurrayR0123/CVE-2024-3400-Compromise-Checker.svg)

## CVE-2024-3393
 A Denial of Service vulnerability in the DNS Security feature of Palo Alto Networks PAN-OS software allows an unauthenticated attacker to send a malicious packet through the data plane of the firewall that reboots the firewall. Repeated attempts to trigger this condition will cause the firewall to enter maintenance mode.



- [https://github.com/FelixFoxf/-CVE-2024-3393](https://github.com/FelixFoxf/-CVE-2024-3393) :  ![starts](https://img.shields.io/github/stars/FelixFoxf/-CVE-2024-3393.svg) ![forks](https://img.shields.io/github/forks/FelixFoxf/-CVE-2024-3393.svg)

## CVE-2024-3367
 Argument injection in websphere_mq agent plugin in Checkmk 2.0.0, 2.1.0, 2.2.0p26 and 2.3.0b5 allows local attacker to inject one argument to runmqsc



- [https://github.com/dersecure/CVE-2024-33676](https://github.com/dersecure/CVE-2024-33676) :  ![starts](https://img.shields.io/github/stars/dersecure/CVE-2024-33676.svg) ![forks](https://img.shields.io/github/forks/dersecure/CVE-2024-33676.svg)

## CVE-2024-3293
 The rtMedia for WordPress, BuddyPress and bbPress plugin for WordPress is vulnerable to blind SQL Injection via the rtmedia_gallery shortcode in all versions up to, and including, 4.6.18 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for authenticated attackers, with contributor-level access and above, to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/truonghuuphuc/CVE-2024-3293-Poc](https://github.com/truonghuuphuc/CVE-2024-3293-Poc) :  ![starts](https://img.shields.io/github/stars/truonghuuphuc/CVE-2024-3293-Poc.svg) ![forks](https://img.shields.io/github/forks/truonghuuphuc/CVE-2024-3293-Poc.svg)

## CVE-2024-3273
 ** UNSUPPORTED WHEN ASSIGNED ** A vulnerability, which was classified as critical, was found in D-Link DNS-320L, DNS-325, DNS-327L and DNS-340L up to 20240403. Affected is an unknown function of the file /cgi-bin/nas_sharing.cgi of the component HTTP GET Request Handler. The manipulation of the argument system leads to command injection. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-259284. NOTE: This vulnerability only affects products that are no longer supported by the maintainer. NOTE: Vendor was contacted early and confirmed immediately that the product is end-of-life. It should be retired and replaced.



- [https://github.com/Chocapikk/CVE-2024-3273](https://github.com/Chocapikk/CVE-2024-3273) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-3273.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-3273.svg)

- [https://github.com/adhikara13/CVE-2024-3273](https://github.com/adhikara13/CVE-2024-3273) :  ![starts](https://img.shields.io/github/stars/adhikara13/CVE-2024-3273.svg) ![forks](https://img.shields.io/github/forks/adhikara13/CVE-2024-3273.svg)

- [https://github.com/ThatNotEasy/CVE-2024-3273](https://github.com/ThatNotEasy/CVE-2024-3273) :  ![starts](https://img.shields.io/github/stars/ThatNotEasy/CVE-2024-3273.svg) ![forks](https://img.shields.io/github/forks/ThatNotEasy/CVE-2024-3273.svg)

- [https://github.com/K3ysTr0K3R/CVE-2024-3273-EXPLOIT](https://github.com/K3ysTr0K3R/CVE-2024-3273-EXPLOIT) :  ![starts](https://img.shields.io/github/stars/K3ysTr0K3R/CVE-2024-3273-EXPLOIT.svg) ![forks](https://img.shields.io/github/forks/K3ysTr0K3R/CVE-2024-3273-EXPLOIT.svg)

- [https://github.com/mrrobot0o/CVE-2024-3273-](https://github.com/mrrobot0o/CVE-2024-3273-) :  ![starts](https://img.shields.io/github/stars/mrrobot0o/CVE-2024-3273-.svg) ![forks](https://img.shields.io/github/forks/mrrobot0o/CVE-2024-3273-.svg)

- [https://github.com/LeopoldSkell/CVE-2024-3273](https://github.com/LeopoldSkell/CVE-2024-3273) :  ![starts](https://img.shields.io/github/stars/LeopoldSkell/CVE-2024-3273.svg) ![forks](https://img.shields.io/github/forks/LeopoldSkell/CVE-2024-3273.svg)

- [https://github.com/yarienkiva/honeypot-dlink-CVE-2024-3273](https://github.com/yarienkiva/honeypot-dlink-CVE-2024-3273) :  ![starts](https://img.shields.io/github/stars/yarienkiva/honeypot-dlink-CVE-2024-3273.svg) ![forks](https://img.shields.io/github/forks/yarienkiva/honeypot-dlink-CVE-2024-3273.svg)

- [https://github.com/OIivr/Turvan6rkus-CVE-2024-3273](https://github.com/OIivr/Turvan6rkus-CVE-2024-3273) :  ![starts](https://img.shields.io/github/stars/OIivr/Turvan6rkus-CVE-2024-3273.svg) ![forks](https://img.shields.io/github/forks/OIivr/Turvan6rkus-CVE-2024-3273.svg)

## CVE-2024-3272
 ** UNSUPPORTED WHEN ASSIGNED ** A vulnerability, which was classified as very critical, has been found in D-Link DNS-320L, DNS-325, DNS-327L and DNS-340L up to 20240403. This issue affects some unknown processing of the file /cgi-bin/nas_sharing.cgi of the component HTTP GET Request Handler. The manipulation of the argument user with the input messagebus leads to hard-coded credentials. The attack may be initiated remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-259283. NOTE: This vulnerability only affects products that are no longer supported by the maintainer. NOTE: Vendor was contacted early and confirmed immediately that the product is end-of-life. It should be retired and replaced.



- [https://github.com/aliask/dinkleberry](https://github.com/aliask/dinkleberry) :  ![starts](https://img.shields.io/github/stars/aliask/dinkleberry.svg) ![forks](https://img.shields.io/github/forks/aliask/dinkleberry.svg)

## CVE-2024-3217
 The WP Directory Kit plugin for WordPress is vulnerable to SQL Injection via the 'attribute_value' and 'attribute_id' parameters in all versions up to, and including, 1.3.0 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for authenticated attackers, with subscriber-level access and above, to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/BassamAssiri/CVE-2024-3217-POC](https://github.com/BassamAssiri/CVE-2024-3217-POC) :  ![starts](https://img.shields.io/github/stars/BassamAssiri/CVE-2024-3217-POC.svg) ![forks](https://img.shields.io/github/forks/BassamAssiri/CVE-2024-3217-POC.svg)

## CVE-2024-3196
 A vulnerability was found in MailCleaner up to 2023.03.14. It has been declared as critical. This vulnerability affects the function getStats/Services_silentDump/Services_stopStartMTA/Config_saveDateTime/Config_hostid/Logs_StartGetStat/dumpConfiguration of the component SOAP Service. The manipulation leads to os command injection. Local access is required to approach this attack. The exploit has been disclosed to the public and may be used. It is recommended to apply a patch to fix this issue. The identifier of this vulnerability is VDB-262312.



- [https://github.com/kingfakee7/CVE-2024-31969](https://github.com/kingfakee7/CVE-2024-31969) :  ![starts](https://img.shields.io/github/stars/kingfakee7/CVE-2024-31969.svg) ![forks](https://img.shields.io/github/forks/kingfakee7/CVE-2024-31969.svg)

## CVE-2024-3171
 Use after free in Accessibility in Google Chrome prior to 122.0.6261.57 allowed a remote attacker who convinced a user to engage in specific UI gestures to potentially exploit heap corruption via specific UI gestures. (Chromium security severity: Medium)



- [https://github.com/VoltaireYoung/CVE-2024-31719----AMI-Aptio-5-Vulnerability](https://github.com/VoltaireYoung/CVE-2024-31719----AMI-Aptio-5-Vulnerability) :  ![starts](https://img.shields.io/github/stars/VoltaireYoung/CVE-2024-31719----AMI-Aptio-5-Vulnerability.svg) ![forks](https://img.shields.io/github/forks/VoltaireYoung/CVE-2024-31719----AMI-Aptio-5-Vulnerability.svg)

## CVE-2024-3121
 A remote code execution vulnerability exists in the create_conda_env function of the parisneo/lollms repository, version 5.9.0. The vulnerability arises from the use of shell=True in the subprocess.Popen function, which allows an attacker to inject arbitrary commands by manipulating the env_name and python_version parameters. This issue could lead to a serious security breach as demonstrated by the ability to execute the 'whoami' command among potentially other harmful commands.



- [https://github.com/dark-ninja10/CVE-2024-3121](https://github.com/dark-ninja10/CVE-2024-3121) :  ![starts](https://img.shields.io/github/stars/dark-ninja10/CVE-2024-3121.svg) ![forks](https://img.shields.io/github/forks/dark-ninja10/CVE-2024-3121.svg)

## CVE-2024-3116
 pgAdmin = 8.4 is affected by a  Remote Code Execution (RCE) vulnerability through the validate binary path API. This vulnerability allows attackers to execute arbitrary code on the server hosting PGAdmin, posing a severe risk to the database management system's integrity and the security of the underlying data.



- [https://github.com/TechieNeurons/CVE-2024-3116_RCE_in_pgadmin_8.4](https://github.com/TechieNeurons/CVE-2024-3116_RCE_in_pgadmin_8.4) :  ![starts](https://img.shields.io/github/stars/TechieNeurons/CVE-2024-3116_RCE_in_pgadmin_8.4.svg) ![forks](https://img.shields.io/github/forks/TechieNeurons/CVE-2024-3116_RCE_in_pgadmin_8.4.svg)

## CVE-2024-3105
 The Woody code snippets – Insert Header Footer Code, AdSense Ads plugin for WordPress is vulnerable to Remote Code Execution in all versions up to, and including, 2.5.0 via the 'insert_php' shortcode. This is due to the plugin not restricting the usage of the functionality to high level authorized users. This makes it possible for authenticated attackers, with contributor-level access and above, to execute code on the server.



- [https://github.com/hunThubSpace/CVE-2024-3105-PoC](https://github.com/hunThubSpace/CVE-2024-3105-PoC) :  ![starts](https://img.shields.io/github/stars/hunThubSpace/CVE-2024-3105-PoC.svg) ![forks](https://img.shields.io/github/forks/hunThubSpace/CVE-2024-3105-PoC.svg)

## CVE-2024-3095
 A Server-Side Request Forgery (SSRF) vulnerability exists in the Web Research Retriever component of langchain-ai/langchain version 0.1.5. The vulnerability arises because the Web Research Retriever does not restrict requests to remote internet addresses, allowing it to reach local addresses. This flaw enables attackers to execute port scans, access local services, and in some scenarios, read instance metadata from cloud environments. The vulnerability is particularly concerning as it can be exploited to abuse the Web Explorer server as a proxy for web attacks on third parties and interact with servers in the local network, including reading their response data. This could potentially lead to arbitrary code execution, depending on the nature of the local services. The vulnerability is limited to GET requests, as POST requests are not possible, but the impact on confidentiality, integrity, and availability is significant due to the potential for stolen credentials and state-changing interactions with internal APIs.



- [https://github.com/leoCottret/CVE-2024-30956](https://github.com/leoCottret/CVE-2024-30956) :  ![starts](https://img.shields.io/github/stars/leoCottret/CVE-2024-30956.svg) ![forks](https://img.shields.io/github/forks/leoCottret/CVE-2024-30956.svg)

## CVE-2024-3094
 Malicious code was discovered in the upstream tarballs of xz, starting with version 5.6.0. 
Through a series of complex obfuscations, the liblzma build process extracts a prebuilt object file from a disguised test file existing in the source code, which is then used to modify specific functions in the liblzma code. This results in a modified liblzma library that can be used by any software linked against this library, intercepting and modifying the data interaction with this library.



- [https://github.com/amlweems/xzbot](https://github.com/amlweems/xzbot) :  ![starts](https://img.shields.io/github/stars/amlweems/xzbot.svg) ![forks](https://img.shields.io/github/forks/amlweems/xzbot.svg)

- [https://github.com/lockness-Ko/xz-vulnerable-honeypot](https://github.com/lockness-Ko/xz-vulnerable-honeypot) :  ![starts](https://img.shields.io/github/stars/lockness-Ko/xz-vulnerable-honeypot.svg) ![forks](https://img.shields.io/github/forks/lockness-Ko/xz-vulnerable-honeypot.svg)

- [https://github.com/FabioBaroni/CVE-2024-3094-checker](https://github.com/FabioBaroni/CVE-2024-3094-checker) :  ![starts](https://img.shields.io/github/stars/FabioBaroni/CVE-2024-3094-checker.svg) ![forks](https://img.shields.io/github/forks/FabioBaroni/CVE-2024-3094-checker.svg)

- [https://github.com/byinarie/CVE-2024-3094-info](https://github.com/byinarie/CVE-2024-3094-info) :  ![starts](https://img.shields.io/github/stars/byinarie/CVE-2024-3094-info.svg) ![forks](https://img.shields.io/github/forks/byinarie/CVE-2024-3094-info.svg)

- [https://github.com/jfrog/cve-2024-3094-tools](https://github.com/jfrog/cve-2024-3094-tools) :  ![starts](https://img.shields.io/github/stars/jfrog/cve-2024-3094-tools.svg) ![forks](https://img.shields.io/github/forks/jfrog/cve-2024-3094-tools.svg)

- [https://github.com/gensecaihq/CVE-2024-3094-Vulnerability-Checker-Fixer](https://github.com/gensecaihq/CVE-2024-3094-Vulnerability-Checker-Fixer) :  ![starts](https://img.shields.io/github/stars/gensecaihq/CVE-2024-3094-Vulnerability-Checker-Fixer.svg) ![forks](https://img.shields.io/github/forks/gensecaihq/CVE-2024-3094-Vulnerability-Checker-Fixer.svg)

- [https://github.com/0xlane/xz-cve-2024-3094](https://github.com/0xlane/xz-cve-2024-3094) :  ![starts](https://img.shields.io/github/stars/0xlane/xz-cve-2024-3094.svg) ![forks](https://img.shields.io/github/forks/0xlane/xz-cve-2024-3094.svg)

- [https://github.com/robertdfrench/ifuncd-up](https://github.com/robertdfrench/ifuncd-up) :  ![starts](https://img.shields.io/github/stars/robertdfrench/ifuncd-up.svg) ![forks](https://img.shields.io/github/forks/robertdfrench/ifuncd-up.svg)

- [https://github.com/r0binak/xzk8s](https://github.com/r0binak/xzk8s) :  ![starts](https://img.shields.io/github/stars/r0binak/xzk8s.svg) ![forks](https://img.shields.io/github/forks/r0binak/xzk8s.svg)

- [https://github.com/teyhouse/CVE-2024-3094](https://github.com/teyhouse/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/teyhouse/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/teyhouse/CVE-2024-3094.svg)

- [https://github.com/emirkmo/xz-backdoor-github](https://github.com/emirkmo/xz-backdoor-github) :  ![starts](https://img.shields.io/github/stars/emirkmo/xz-backdoor-github.svg) ![forks](https://img.shields.io/github/forks/emirkmo/xz-backdoor-github.svg)

- [https://github.com/Hacker-Hermanos/CVE-2024-3094_xz_check](https://github.com/Hacker-Hermanos/CVE-2024-3094_xz_check) :  ![starts](https://img.shields.io/github/stars/Hacker-Hermanos/CVE-2024-3094_xz_check.svg) ![forks](https://img.shields.io/github/forks/Hacker-Hermanos/CVE-2024-3094_xz_check.svg)

- [https://github.com/XiaomingX/cve-2024-3094-xz-backdoor-exploit](https://github.com/XiaomingX/cve-2024-3094-xz-backdoor-exploit) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-3094-xz-backdoor-exploit.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-3094-xz-backdoor-exploit.svg)

- [https://github.com/badsectorlabs/ludus_xz_backdoor](https://github.com/badsectorlabs/ludus_xz_backdoor) :  ![starts](https://img.shields.io/github/stars/badsectorlabs/ludus_xz_backdoor.svg) ![forks](https://img.shields.io/github/forks/badsectorlabs/ludus_xz_backdoor.svg)

- [https://github.com/wgetnz/CVE-2024-3094-check](https://github.com/wgetnz/CVE-2024-3094-check) :  ![starts](https://img.shields.io/github/stars/wgetnz/CVE-2024-3094-check.svg) ![forks](https://img.shields.io/github/forks/wgetnz/CVE-2024-3094-check.svg)

- [https://github.com/robertdebock/ansible-role-cve_2024_3094](https://github.com/robertdebock/ansible-role-cve_2024_3094) :  ![starts](https://img.shields.io/github/stars/robertdebock/ansible-role-cve_2024_3094.svg) ![forks](https://img.shields.io/github/forks/robertdebock/ansible-role-cve_2024_3094.svg)

- [https://github.com/Yuma-Tsushima07/CVE-2024-3094](https://github.com/Yuma-Tsushima07/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/Yuma-Tsushima07/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/Yuma-Tsushima07/CVE-2024-3094.svg)

- [https://github.com/KaminaDuck/ansible-CVE-2024-3094](https://github.com/KaminaDuck/ansible-CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/KaminaDuck/ansible-CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/KaminaDuck/ansible-CVE-2024-3094.svg)

- [https://github.com/lypd0/CVE-2024-3094-Vulnerabity-Checker](https://github.com/lypd0/CVE-2024-3094-Vulnerabity-Checker) :  ![starts](https://img.shields.io/github/stars/lypd0/CVE-2024-3094-Vulnerabity-Checker.svg) ![forks](https://img.shields.io/github/forks/lypd0/CVE-2024-3094-Vulnerabity-Checker.svg)

- [https://github.com/neuralinhibitor/xzwhy](https://github.com/neuralinhibitor/xzwhy) :  ![starts](https://img.shields.io/github/stars/neuralinhibitor/xzwhy.svg) ![forks](https://img.shields.io/github/forks/neuralinhibitor/xzwhy.svg)

- [https://github.com/gustavorobertux/CVE-2024-3094](https://github.com/gustavorobertux/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/gustavorobertux/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/gustavorobertux/CVE-2024-3094.svg)

- [https://github.com/pentestfunctions/CVE-2024-3094](https://github.com/pentestfunctions/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/pentestfunctions/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/pentestfunctions/CVE-2024-3094.svg)

- [https://github.com/felipecosta09/cve-2024-3094](https://github.com/felipecosta09/cve-2024-3094) :  ![starts](https://img.shields.io/github/stars/felipecosta09/cve-2024-3094.svg) ![forks](https://img.shields.io/github/forks/felipecosta09/cve-2024-3094.svg)

- [https://github.com/ScrimForever/CVE-2024-3094](https://github.com/ScrimForever/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/ScrimForever/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/ScrimForever/CVE-2024-3094.svg)

- [https://github.com/DANO-AMP/CVE-2024-3094](https://github.com/DANO-AMP/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/DANO-AMP/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/DANO-AMP/CVE-2024-3094.svg)

- [https://github.com/Horizon-Software-Development/CVE-2024-3094](https://github.com/Horizon-Software-Development/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/Horizon-Software-Development/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/Horizon-Software-Development/CVE-2024-3094.svg)

- [https://github.com/Bella-Bc/xz-backdoor-CVE-2024-3094-Check](https://github.com/Bella-Bc/xz-backdoor-CVE-2024-3094-Check) :  ![starts](https://img.shields.io/github/stars/Bella-Bc/xz-backdoor-CVE-2024-3094-Check.svg) ![forks](https://img.shields.io/github/forks/Bella-Bc/xz-backdoor-CVE-2024-3094-Check.svg)

- [https://github.com/przemoc/xz-backdoor-links](https://github.com/przemoc/xz-backdoor-links) :  ![starts](https://img.shields.io/github/stars/przemoc/xz-backdoor-links.svg) ![forks](https://img.shields.io/github/forks/przemoc/xz-backdoor-links.svg)

- [https://github.com/galacticquest/cve-2024-3094-detect](https://github.com/galacticquest/cve-2024-3094-detect) :  ![starts](https://img.shields.io/github/stars/galacticquest/cve-2024-3094-detect.svg) ![forks](https://img.shields.io/github/forks/galacticquest/cve-2024-3094-detect.svg)

- [https://github.com/Security-Phoenix-demo/CVE-2024-3094-fix-exploits](https://github.com/Security-Phoenix-demo/CVE-2024-3094-fix-exploits) :  ![starts](https://img.shields.io/github/stars/Security-Phoenix-demo/CVE-2024-3094-fix-exploits.svg) ![forks](https://img.shields.io/github/forks/Security-Phoenix-demo/CVE-2024-3094-fix-exploits.svg)

- [https://github.com/robertdebock/ansible-playbook-cve-2024-3094](https://github.com/robertdebock/ansible-playbook-cve-2024-3094) :  ![starts](https://img.shields.io/github/stars/robertdebock/ansible-playbook-cve-2024-3094.svg) ![forks](https://img.shields.io/github/forks/robertdebock/ansible-playbook-cve-2024-3094.svg)

- [https://github.com/brinhosa/CVE-2024-3094-One-Liner](https://github.com/brinhosa/CVE-2024-3094-One-Liner) :  ![starts](https://img.shields.io/github/stars/brinhosa/CVE-2024-3094-One-Liner.svg) ![forks](https://img.shields.io/github/forks/brinhosa/CVE-2024-3094-One-Liner.svg)

- [https://github.com/harekrishnarai/xz-utils-vuln-checker](https://github.com/harekrishnarai/xz-utils-vuln-checker) :  ![starts](https://img.shields.io/github/stars/harekrishnarai/xz-utils-vuln-checker.svg) ![forks](https://img.shields.io/github/forks/harekrishnarai/xz-utils-vuln-checker.svg)

- [https://github.com/bsekercioglu/cve2024-3094-Checker](https://github.com/bsekercioglu/cve2024-3094-Checker) :  ![starts](https://img.shields.io/github/stars/bsekercioglu/cve2024-3094-Checker.svg) ![forks](https://img.shields.io/github/forks/bsekercioglu/cve2024-3094-Checker.svg)

- [https://github.com/mesutgungor/xz-backdoor-vulnerability](https://github.com/mesutgungor/xz-backdoor-vulnerability) :  ![starts](https://img.shields.io/github/stars/mesutgungor/xz-backdoor-vulnerability.svg) ![forks](https://img.shields.io/github/forks/mesutgungor/xz-backdoor-vulnerability.svg)

- [https://github.com/isuruwa/CVE-2024-3094](https://github.com/isuruwa/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/isuruwa/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/isuruwa/CVE-2024-3094.svg)

- [https://github.com/Mustafa1986/CVE-2024-3094](https://github.com/Mustafa1986/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/Mustafa1986/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/Mustafa1986/CVE-2024-3094.svg)

- [https://github.com/reuteras/CVE-2024-3094](https://github.com/reuteras/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/reuteras/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/reuteras/CVE-2024-3094.svg)

- [https://github.com/bioless/xz_cve-2024-3094_detection](https://github.com/bioless/xz_cve-2024-3094_detection) :  ![starts](https://img.shields.io/github/stars/bioless/xz_cve-2024-3094_detection.svg) ![forks](https://img.shields.io/github/forks/bioless/xz_cve-2024-3094_detection.svg)

- [https://github.com/Fractal-Tess/CVE-2024-3094](https://github.com/Fractal-Tess/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/Fractal-Tess/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/Fractal-Tess/CVE-2024-3094.svg)

- [https://github.com/dah4k/CVE-2024-3094](https://github.com/dah4k/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/dah4k/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/dah4k/CVE-2024-3094.svg)

- [https://github.com/been22426/CVE-2024-3094](https://github.com/been22426/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/been22426/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/been22426/CVE-2024-3094.svg)

- [https://github.com/mightysai1997/CVE-2024-3094](https://github.com/mightysai1997/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/mightysai1997/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/mightysai1997/CVE-2024-3094.svg)

- [https://github.com/shefirot/CVE-2024-3094](https://github.com/shefirot/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/shefirot/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/shefirot/CVE-2024-3094.svg)

- [https://github.com/ashwani95/CVE-2024-3094](https://github.com/ashwani95/CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/ashwani95/CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/ashwani95/CVE-2024-3094.svg)

- [https://github.com/devjanger/CVE-2024-3094-XZ-Backdoor-Detector](https://github.com/devjanger/CVE-2024-3094-XZ-Backdoor-Detector) :  ![starts](https://img.shields.io/github/stars/devjanger/CVE-2024-3094-XZ-Backdoor-Detector.svg) ![forks](https://img.shields.io/github/forks/devjanger/CVE-2024-3094-XZ-Backdoor-Detector.svg)

- [https://github.com/valeriot30/cve-2024-3094](https://github.com/valeriot30/cve-2024-3094) :  ![starts](https://img.shields.io/github/stars/valeriot30/cve-2024-3094.svg) ![forks](https://img.shields.io/github/forks/valeriot30/cve-2024-3094.svg)

- [https://github.com/mightysai1997/CVE-2024-3094-info](https://github.com/mightysai1997/CVE-2024-3094-info) :  ![starts](https://img.shields.io/github/stars/mightysai1997/CVE-2024-3094-info.svg) ![forks](https://img.shields.io/github/forks/mightysai1997/CVE-2024-3094-info.svg)

- [https://github.com/TheTorjanCaptain/CVE-2024-3094-Checker](https://github.com/TheTorjanCaptain/CVE-2024-3094-Checker) :  ![starts](https://img.shields.io/github/stars/TheTorjanCaptain/CVE-2024-3094-Checker.svg) ![forks](https://img.shields.io/github/forks/TheTorjanCaptain/CVE-2024-3094-Checker.svg)

- [https://github.com/ackemed/detectar_cve-2024-3094](https://github.com/ackemed/detectar_cve-2024-3094) :  ![starts](https://img.shields.io/github/stars/ackemed/detectar_cve-2024-3094.svg) ![forks](https://img.shields.io/github/forks/ackemed/detectar_cve-2024-3094.svg)

- [https://github.com/hazemkya/CVE-2024-3094-checker](https://github.com/hazemkya/CVE-2024-3094-checker) :  ![starts](https://img.shields.io/github/stars/hazemkya/CVE-2024-3094-checker.svg) ![forks](https://img.shields.io/github/forks/hazemkya/CVE-2024-3094-checker.svg)

- [https://github.com/iheb2b/CVE-2024-3094-Checker](https://github.com/iheb2b/CVE-2024-3094-Checker) :  ![starts](https://img.shields.io/github/stars/iheb2b/CVE-2024-3094-Checker.svg) ![forks](https://img.shields.io/github/forks/iheb2b/CVE-2024-3094-Checker.svg)

- [https://github.com/Simplifi-ED/CVE-2024-3094-patcher](https://github.com/Simplifi-ED/CVE-2024-3094-patcher) :  ![starts](https://img.shields.io/github/stars/Simplifi-ED/CVE-2024-3094-patcher.svg) ![forks](https://img.shields.io/github/forks/Simplifi-ED/CVE-2024-3094-patcher.svg)

- [https://github.com/Ikram124/CVE-2024-3094-analysis](https://github.com/Ikram124/CVE-2024-3094-analysis) :  ![starts](https://img.shields.io/github/stars/Ikram124/CVE-2024-3094-analysis.svg) ![forks](https://img.shields.io/github/forks/Ikram124/CVE-2024-3094-analysis.svg)

- [https://github.com/OpensourceICTSolutions/xz_utils-CVE-2024-3094](https://github.com/OpensourceICTSolutions/xz_utils-CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/OpensourceICTSolutions/xz_utils-CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/OpensourceICTSolutions/xz_utils-CVE-2024-3094.svg)

- [https://github.com/buluma/ansible-role-cve_2024_3094](https://github.com/buluma/ansible-role-cve_2024_3094) :  ![starts](https://img.shields.io/github/stars/buluma/ansible-role-cve_2024_3094.svg) ![forks](https://img.shields.io/github/forks/buluma/ansible-role-cve_2024_3094.svg)

- [https://github.com/MrBUGLF/XZ-Utils_CVE-2024-3094](https://github.com/MrBUGLF/XZ-Utils_CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/MrBUGLF/XZ-Utils_CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/MrBUGLF/XZ-Utils_CVE-2024-3094.svg)

- [https://github.com/MagpieRYL/CVE-2024-3094-backdoor-env-container](https://github.com/MagpieRYL/CVE-2024-3094-backdoor-env-container) :  ![starts](https://img.shields.io/github/stars/MagpieRYL/CVE-2024-3094-backdoor-env-container.svg) ![forks](https://img.shields.io/github/forks/MagpieRYL/CVE-2024-3094-backdoor-env-container.svg)

- [https://github.com/gayatriracha/CVE-2024-3094-Nmap-NSE-script](https://github.com/gayatriracha/CVE-2024-3094-Nmap-NSE-script) :  ![starts](https://img.shields.io/github/stars/gayatriracha/CVE-2024-3094-Nmap-NSE-script.svg) ![forks](https://img.shields.io/github/forks/gayatriracha/CVE-2024-3094-Nmap-NSE-script.svg)

- [https://github.com/weltregie/liblzma-scan](https://github.com/weltregie/liblzma-scan) :  ![starts](https://img.shields.io/github/stars/weltregie/liblzma-scan.svg) ![forks](https://img.shields.io/github/forks/weltregie/liblzma-scan.svg)

- [https://github.com/laxmikumari615/Linux---Security---Detect-and-Mitigate-CVE-2024-3094](https://github.com/laxmikumari615/Linux---Security---Detect-and-Mitigate-CVE-2024-3094) :  ![starts](https://img.shields.io/github/stars/laxmikumari615/Linux---Security---Detect-and-Mitigate-CVE-2024-3094.svg) ![forks](https://img.shields.io/github/forks/laxmikumari615/Linux---Security---Detect-and-Mitigate-CVE-2024-3094.svg)

- [https://github.com/fevar54/Detectar-Backdoor-en-liblzma-de-XZ-utils-CVE-2024-3094-](https://github.com/fevar54/Detectar-Backdoor-en-liblzma-de-XZ-utils-CVE-2024-3094-) :  ![starts](https://img.shields.io/github/stars/fevar54/Detectar-Backdoor-en-liblzma-de-XZ-utils-CVE-2024-3094-.svg) ![forks](https://img.shields.io/github/forks/fevar54/Detectar-Backdoor-en-liblzma-de-XZ-utils-CVE-2024-3094-.svg)

- [https://github.com/AndreaCicca/Sicurezza-Informatica-Presentazione](https://github.com/AndreaCicca/Sicurezza-Informatica-Presentazione) :  ![starts](https://img.shields.io/github/stars/AndreaCicca/Sicurezza-Informatica-Presentazione.svg) ![forks](https://img.shields.io/github/forks/AndreaCicca/Sicurezza-Informatica-Presentazione.svg)

- [https://github.com/hackingetico21/revisaxzutils](https://github.com/hackingetico21/revisaxzutils) :  ![starts](https://img.shields.io/github/stars/hackingetico21/revisaxzutils.svg) ![forks](https://img.shields.io/github/forks/hackingetico21/revisaxzutils.svg)

- [https://github.com/Juul/xz-backdoor-scan](https://github.com/Juul/xz-backdoor-scan) :  ![starts](https://img.shields.io/github/stars/Juul/xz-backdoor-scan.svg) ![forks](https://img.shields.io/github/forks/Juul/xz-backdoor-scan.svg)

## CVE-2024-2997
 A vulnerability was found in Bdtask Multi-Store Inventory Management System up to 20240320. It has been declared as problematic. Affected by this vulnerability is an unknown functionality. The manipulation of the argument Category Name/Model Name/Brand Name/Unit Name leads to cross site scripting. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-258199. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/lfillaz/CVE-2024-2997](https://github.com/lfillaz/CVE-2024-2997) :  ![starts](https://img.shields.io/github/stars/lfillaz/CVE-2024-2997.svg) ![forks](https://img.shields.io/github/forks/lfillaz/CVE-2024-2997.svg)

## CVE-2024-2961
 The iconv() function in the GNU C Library versions 2.39 and older may overflow the output buffer passed to it by up to 4 bytes when converting strings to the ISO-2022-CN-EXT character set, which may be used to crash an application or overwrite a neighbouring variable.



- [https://github.com/ambionics/cnext-exploits](https://github.com/ambionics/cnext-exploits) :  ![starts](https://img.shields.io/github/stars/ambionics/cnext-exploits.svg) ![forks](https://img.shields.io/github/forks/ambionics/cnext-exploits.svg)

- [https://github.com/rvizx/CVE-2024-2961](https://github.com/rvizx/CVE-2024-2961) :  ![starts](https://img.shields.io/github/stars/rvizx/CVE-2024-2961.svg) ![forks](https://img.shields.io/github/forks/rvizx/CVE-2024-2961.svg)

- [https://github.com/kjdfklha/CVE-2024-2961_poc](https://github.com/kjdfklha/CVE-2024-2961_poc) :  ![starts](https://img.shields.io/github/stars/kjdfklha/CVE-2024-2961_poc.svg) ![forks](https://img.shields.io/github/forks/kjdfklha/CVE-2024-2961_poc.svg)

- [https://github.com/mattaperkins/FIX-CVE-2024-2961](https://github.com/mattaperkins/FIX-CVE-2024-2961) :  ![starts](https://img.shields.io/github/stars/mattaperkins/FIX-CVE-2024-2961.svg) ![forks](https://img.shields.io/github/forks/mattaperkins/FIX-CVE-2024-2961.svg)

- [https://github.com/tnishiox/cve-2024-2961](https://github.com/tnishiox/cve-2024-2961) :  ![starts](https://img.shields.io/github/stars/tnishiox/cve-2024-2961.svg) ![forks](https://img.shields.io/github/forks/tnishiox/cve-2024-2961.svg)

- [https://github.com/absolutedesignltd/iconvfix](https://github.com/absolutedesignltd/iconvfix) :  ![starts](https://img.shields.io/github/stars/absolutedesignltd/iconvfix.svg) ![forks](https://img.shields.io/github/forks/absolutedesignltd/iconvfix.svg)

- [https://github.com/exfil0/test_iconv](https://github.com/exfil0/test_iconv) :  ![starts](https://img.shields.io/github/stars/exfil0/test_iconv.svg) ![forks](https://img.shields.io/github/forks/exfil0/test_iconv.svg)

## CVE-2024-2928
 A Local File Inclusion (LFI) vulnerability was identified in mlflow/mlflow, specifically in version 2.9.2, which was fixed in version 2.11.3. This vulnerability arises from the application's failure to properly validate URI fragments for directory traversal sequences such as '../'. An attacker can exploit this flaw by manipulating the fragment part of the URI to read arbitrary files on the local file system, including sensitive files like '/etc/passwd'. The vulnerability is a bypass to a previous patch that only addressed similar manipulation within the URI's query string, highlighting the need for comprehensive validation of all parts of a URI to prevent LFI attacks.



- [https://github.com/nuridincersaygili/CVE-2024-2928](https://github.com/nuridincersaygili/CVE-2024-2928) :  ![starts](https://img.shields.io/github/stars/nuridincersaygili/CVE-2024-2928.svg) ![forks](https://img.shields.io/github/forks/nuridincersaygili/CVE-2024-2928.svg)

## CVE-2024-2887
 Type Confusion in WebAssembly in Google Chrome prior to 123.0.6312.86 allowed a remote attacker to execute arbitrary code via a crafted HTML page. (Chromium security severity: High)



- [https://github.com/jjyuorg/reproduce-cve-2024-2887](https://github.com/jjyuorg/reproduce-cve-2024-2887) :  ![starts](https://img.shields.io/github/stars/jjyuorg/reproduce-cve-2024-2887.svg) ![forks](https://img.shields.io/github/forks/jjyuorg/reproduce-cve-2024-2887.svg)

## CVE-2024-2879
 The LayerSlider plugin for WordPress is vulnerable to SQL Injection via the ls_get_popup_markup action in versions 7.9.11 and 7.10.0 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/herculeszxc/CVE-2024-2879](https://github.com/herculeszxc/CVE-2024-2879) :  ![starts](https://img.shields.io/github/stars/herculeszxc/CVE-2024-2879.svg) ![forks](https://img.shields.io/github/forks/herculeszxc/CVE-2024-2879.svg)

## CVE-2024-2876
 The Email Subscribers by Icegram Express – Email Marketing, Newsletters, Automation for WordPress & WooCommerce plugin for WordPress is vulnerable to SQL Injection via the 'run' function of the 'IG_ES_Subscribers_Query' class in all versions up to, and including, 5.7.14 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/c0d3zilla/CVE-2024-2876](https://github.com/c0d3zilla/CVE-2024-2876) :  ![starts](https://img.shields.io/github/stars/c0d3zilla/CVE-2024-2876.svg) ![forks](https://img.shields.io/github/forks/c0d3zilla/CVE-2024-2876.svg)

- [https://github.com/issamjr/CVE-2024-2876](https://github.com/issamjr/CVE-2024-2876) :  ![starts](https://img.shields.io/github/stars/issamjr/CVE-2024-2876.svg) ![forks](https://img.shields.io/github/forks/issamjr/CVE-2024-2876.svg)

## CVE-2024-2782
 The Contact Form Plugin by Fluent Forms for Quiz, Survey, and Drag & Drop WP Form Builder plugin for WordPress is vulnerable to unauthorized modification of data due to a missing capability check on the /wp-json/fluentform/v1/global-settings REST API endpoint in all versions up to, and including, 5.1.16. This makes it possible for unauthenticated attackers to modify all of the plugin's settings.



- [https://github.com/whale93/CVE-2024-2782-PoC](https://github.com/whale93/CVE-2024-2782-PoC) :  ![starts](https://img.shields.io/github/stars/whale93/CVE-2024-2782-PoC.svg) ![forks](https://img.shields.io/github/forks/whale93/CVE-2024-2782-PoC.svg)

## CVE-2024-2771
 The Contact Form Plugin by Fluent Forms for Quiz, Survey, and Drag & Drop WP Form Builder plugin for WordPress is vulnerable to privilege escalation due to a missing capability check on the /wp-json/fluentform/v1/managers REST API endpoint in all versions up to, and including, 5.1.16. This makes it possible for unauthenticated attackers to grant users with Fluent Form management permissions which gives them access to all of the plugin's settings and features. This also makes it possible for unauthenticated attackers to delete manager accounts.



- [https://github.com/whale93/CVE-2024-2771-PoC](https://github.com/whale93/CVE-2024-2771-PoC) :  ![starts](https://img.shields.io/github/stars/whale93/CVE-2024-2771-PoC.svg) ![forks](https://img.shields.io/github/forks/whale93/CVE-2024-2771-PoC.svg)

## CVE-2024-2769
 A vulnerability was found in Campcodes Complete Online Beauty Parlor Management System 1.0. It has been declared as critical. Affected by this vulnerability is an unknown functionality of the file /admin/admin-profile.php. The manipulation of the argument adminname leads to sql injection. The attack can be launched remotely. The exploit has been disclosed to the public and may be used. The identifier VDB-257605 was assigned to this vulnerability.



- [https://github.com/SanjinDedic/FuguHub-8.4-Authenticated-RCE-CVE-2024-27697](https://github.com/SanjinDedic/FuguHub-8.4-Authenticated-RCE-CVE-2024-27697) :  ![starts](https://img.shields.io/github/stars/SanjinDedic/FuguHub-8.4-Authenticated-RCE-CVE-2024-27697.svg) ![forks](https://img.shields.io/github/forks/SanjinDedic/FuguHub-8.4-Authenticated-RCE-CVE-2024-27697.svg)

## CVE-2024-2768
 A vulnerability was found in Campcodes Complete Online Beauty Parlor Management System 1.0. It has been classified as critical. Affected is an unknown function of the file /admin/edit-services.php. The manipulation of the argument editid leads to sql injection. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-257604.



- [https://github.com/ThemeHackers/CVE-2024-27686](https://github.com/ThemeHackers/CVE-2024-27686) :  ![starts](https://img.shields.io/github/stars/ThemeHackers/CVE-2024-27686.svg) ![forks](https://img.shields.io/github/forks/ThemeHackers/CVE-2024-27686.svg)

## CVE-2024-2667
 The InstaWP Connect – 1-click WP Staging & Migration plugin for WordPress is vulnerable to arbitrary file uploads due to  insufficient file validation in the /wp-json/instawp-connect/v1/config REST API endpoint in all versions up to, and including, 0.1.0.22. This makes it possible for unauthenticated attackers to upload arbitrary files.



- [https://github.com/Puvipavan/CVE-2024-2667](https://github.com/Puvipavan/CVE-2024-2667) :  ![starts](https://img.shields.io/github/stars/Puvipavan/CVE-2024-2667.svg) ![forks](https://img.shields.io/github/forks/Puvipavan/CVE-2024-2667.svg)

- [https://github.com/Nxploited/CVE-2024-2667-Poc](https://github.com/Nxploited/CVE-2024-2667-Poc) :  ![starts](https://img.shields.io/github/stars/Nxploited/CVE-2024-2667-Poc.svg) ![forks](https://img.shields.io/github/forks/Nxploited/CVE-2024-2667-Poc.svg)

## CVE-2024-2656
 The Email Subscribers by Icegram Express – Email Marketing, Newsletters, Automation for WordPress & WooCommerce plugin for WordPress is vulnerable to Stored Cross-Site Scripting via a CSV import in all versions up to, and including, 5.7.14 due to insufficient input sanitization and output escaping. This makes it possible for authenticated attackers, with administrator-level permissions and above, to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page. This only affects multi-site installations and installations where unfiltered_html has been disabled.



- [https://github.com/sajaljat/CVE-2024-26560](https://github.com/sajaljat/CVE-2024-26560) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-26560.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-26560.svg)

## CVE-2024-2653
 amphp/http will collect CONTINUATION frames in an unbounded buffer and will not check a limit until it has received the set END_HEADERS flag, resulting in an OOM crash.



- [https://github.com/lockness-Ko/CVE-2024-27316](https://github.com/lockness-Ko/CVE-2024-27316) :  ![starts](https://img.shields.io/github/stars/lockness-Ko/CVE-2024-27316.svg) ![forks](https://img.shields.io/github/forks/lockness-Ko/CVE-2024-27316.svg)

- [https://github.com/sajaljat/CVE-2024-26535](https://github.com/sajaljat/CVE-2024-26535) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-26535.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-26535.svg)

- [https://github.com/sajaljat/CVE-2024-26534](https://github.com/sajaljat/CVE-2024-26534) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-26534.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-26534.svg)

## CVE-2024-2580
 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in FunnelKit Automation By Autonami allows Stored XSS.This issue affects Automation By Autonami: from n/a through 2.8.2.





- [https://github.com/sajaljat/CVE-2024-25809](https://github.com/sajaljat/CVE-2024-25809) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-25809.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-25809.svg)

## CVE-2024-2528
 A vulnerability was found in MAGESH-K21 Online-College-Event-Hall-Reservation-System 1.0. It has been classified as critical. This affects an unknown part of the file /admin/update-rooms.php. The manipulation of the argument room_id leads to sql injection. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The identifier VDB-256965 was assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/sajaljat/CVE-2024-25281](https://github.com/sajaljat/CVE-2024-25281) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-25281.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-25281.svg)

- [https://github.com/sajaljat/CVE-2024-25280](https://github.com/sajaljat/CVE-2024-25280) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-25280.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-25280.svg)

## CVE-2024-2527
 A vulnerability was found in MAGESH-K21 Online-College-Event-Hall-Reservation-System 1.0 and classified as critical. Affected by this issue is some unknown functionality of the file /admin/rooms.php. The manipulation of the argument room_id leads to sql injection. The attack may be launched remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-256964. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/sajaljat/CVE-2024-25279](https://github.com/sajaljat/CVE-2024-25279) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-25279.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-25279.svg)

- [https://github.com/maen08/CVE-2024-25277](https://github.com/maen08/CVE-2024-25277) :  ![starts](https://img.shields.io/github/stars/maen08/CVE-2024-25277.svg) ![forks](https://img.shields.io/github/forks/maen08/CVE-2024-25277.svg)

- [https://github.com/sajaljat/CVE-2024-25278](https://github.com/sajaljat/CVE-2024-25278) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-25278.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-25278.svg)

## CVE-2024-2473
 The WPS Hide Login plugin for WordPress is vulnerable to Login Page Disclosure in all versions up to, and including, 1.9.15.2. This is due to a bypass that is created when the 'action=postpass' parameter is supplied. This makes it possible for attackers to easily discover any login page that may have been hidden by the plugin.



- [https://github.com/whattheslime/wps-show-login](https://github.com/whattheslime/wps-show-login) :  ![starts](https://img.shields.io/github/stars/whattheslime/wps-show-login.svg) ![forks](https://img.shields.io/github/forks/whattheslime/wps-show-login.svg)

## CVE-2024-2432
 A privilege escalation (PE) vulnerability in the Palo Alto Networks GlobalProtect app on Windows devices enables a local user to execute programs with elevated privileges. However, execution requires that the local user is able to successfully exploit a race condition.



- [https://github.com/Hagrid29/CVE-2024-2432-PaloAlto-GlobalProtect-EoP](https://github.com/Hagrid29/CVE-2024-2432-PaloAlto-GlobalProtect-EoP) :  ![starts](https://img.shields.io/github/stars/Hagrid29/CVE-2024-2432-PaloAlto-GlobalProtect-EoP.svg) ![forks](https://img.shields.io/github/forks/Hagrid29/CVE-2024-2432-PaloAlto-GlobalProtect-EoP.svg)

## CVE-2024-2420
 LenelS2 NetBox access control and event monitoring system was discovered to contain Hardcoded Credentials in versions prior to and including 5.6.1 which allows an attacker to bypass authentication requirements.



- [https://github.com/l00neyhacker/CVE-2024-24204](https://github.com/l00neyhacker/CVE-2024-24204) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-24204.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-24204.svg)

- [https://github.com/l00neyhacker/CVE-2024-24206](https://github.com/l00neyhacker/CVE-2024-24206) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-24206.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-24206.svg)

- [https://github.com/l00neyhacker/CVE-2024-24203](https://github.com/l00neyhacker/CVE-2024-24203) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-24203.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-24203.svg)

## CVE-2024-2413
 Intumit SmartRobot uses a fixed encryption key for authentication. Remote attackers can use this key to encrypt a string composed of the user's name and timestamp to generate an authentication code. With this authentication code, they can obtain administrator privileges and subsequently execute arbitrary code on the remote server using built-in system functionality.



- [https://github.com/BurakSevben/CVE-2024-24137](https://github.com/BurakSevben/CVE-2024-24137) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-24137.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-24137.svg)

- [https://github.com/BurakSevben/CVE-2024-24138](https://github.com/BurakSevben/CVE-2024-24138) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-24138.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-24138.svg)

## CVE-2024-2410
 The JsonToBinaryStream() function is part of the protocol buffers C++ implementation and is used to parse JSON from a stream. If the input is broken up into separate chunks in a certain way, the parser will attempt to read bytes from a chunk that has already been freed. 




- [https://github.com/ASR511-OO7/CVE-2024-24103](https://github.com/ASR511-OO7/CVE-2024-24103) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24103.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24103.svg)

- [https://github.com/ASR511-OO7/CVE-2024-24102](https://github.com/ASR511-OO7/CVE-2024-24102) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24102.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24102.svg)

- [https://github.com/ASR511-OO7/CVE-2024-24104](https://github.com/ASR511-OO7/CVE-2024-24104) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24104.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24104.svg)

- [https://github.com/ASR511-OO7/CVE-2024-24108](https://github.com/ASR511-OO7/CVE-2024-24108) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24108.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24108.svg)

## CVE-2024-2409
 The MasterStudy LMS plugin for WordPress is vulnerable to Privilege Escalation in all versions up to, and including, 3.3.1. This is due to insufficient validation checks within the _register_user() function called by the 'wp_ajax_nopriv_stm_lms_register' AJAX action. This makes it possible for unauthenticated attackers to register a user with administrator-level privileges when MasterStudy LMS Pro is installed and the LMS Forms Editor add-on is enabled.



- [https://github.com/ASR511-OO7/CVE-2024-24094](https://github.com/ASR511-OO7/CVE-2024-24094) :  ![starts](https://img.shields.io/github/stars/ASR511-OO7/CVE-2024-24094.svg) ![forks](https://img.shields.io/github/forks/ASR511-OO7/CVE-2024-24094.svg)

## CVE-2024-2389
 In Flowmon versions prior to 11.1.14 and 12.3.5, an operating system command injection vulnerability has been identified.  An unauthenticated user can gain entry to the system via the Flowmon management interface, allowing for the execution of arbitrary system commands.





- [https://github.com/adhikara13/CVE-2024-2389](https://github.com/adhikara13/CVE-2024-2389) :  ![starts](https://img.shields.io/github/stars/adhikara13/CVE-2024-2389.svg) ![forks](https://img.shields.io/github/forks/adhikara13/CVE-2024-2389.svg)

## CVE-2024-2378
 A vulnerability exists in the web-authentication component of the SDM600. If exploited an attacker could escalate privileges on af-fected installations.



- [https://github.com/HazardLab-IO/CVE-2024-23780](https://github.com/HazardLab-IO/CVE-2024-23780) :  ![starts](https://img.shields.io/github/stars/HazardLab-IO/CVE-2024-23780.svg) ![forks](https://img.shields.io/github/forks/HazardLab-IO/CVE-2024-23780.svg)

## CVE-2024-2319
 Cross-Site Scripting (XSS) vulnerability in the Django MarkdownX project, affecting version 4.0.2. An attacker could store a specially crafted JavaScript payload in the upload functionality due to lack of proper sanitisation of JavaScript elements.



- [https://github.com/l00neyhacker/CVE-2024-23199](https://github.com/l00neyhacker/CVE-2024-23199) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-23199.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-23199.svg)

## CVE-2024-2300
 HP Advance Mobile Applications for iOS and Android are potentially vulnerable to information disclosure when using an outdated version of the application via mobile devices.



- [https://github.com/xiaomaoxxx/CVE-2024-23002](https://github.com/xiaomaoxxx/CVE-2024-23002) :  ![starts](https://img.shields.io/github/stars/xiaomaoxxx/CVE-2024-23002.svg) ![forks](https://img.shields.io/github/forks/xiaomaoxxx/CVE-2024-23002.svg)

## CVE-2024-2290
 The Advanced Ads plugin for WordPress is vulnerable to PHP Object Injection in all versions up to, and including, 1.52.1 via deserialization of untrusted input in the 'placement_slug' parameter. This makes it possible for authenticated attackers to inject a PHP Object. No POP chain is present in the vulnerable plugin. If a POP chain is present via an additional plugin or theme installed on the target system, it could allow the attacker to delete arbitrary files, retrieve sensitive data, or execute code.



- [https://github.com/BurakSevben/CVE-2024-22909](https://github.com/BurakSevben/CVE-2024-22909) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-22909.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-22909.svg)

## CVE-2024-2289
 The PowerPack Lite for Beaver Builder plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the link in multiple elements in all versions up to, and including, 1.3.0 due to insufficient input sanitization and output escaping on user supplied attributes. This makes it possible for authenticated attackers with contributor-level and above permissions to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page.



- [https://github.com/BurakSevben/CVE-2024-22890](https://github.com/BurakSevben/CVE-2024-22890) :  ![starts](https://img.shields.io/github/stars/BurakSevben/CVE-2024-22890.svg) ![forks](https://img.shields.io/github/forks/BurakSevben/CVE-2024-22890.svg)

## CVE-2024-2286
 The Sky Addons for Elementor (Free Templates Library, Live Copy, Animations, Post Grid, Post Carousel, Particles, Sliders, Chart) plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the wrapper link URL value in all versions up to, and including, 2.4.0 due to insufficient input sanitization and output escaping on user supplied attributes. This makes it possible for authenticated attackers with contributor-level and above permissions to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page.



- [https://github.com/brandon-t-elliott/CVE-2024-22867](https://github.com/brandon-t-elliott/CVE-2024-22867) :  ![starts](https://img.shields.io/github/stars/brandon-t-elliott/CVE-2024-22867.svg) ![forks](https://img.shields.io/github/forks/brandon-t-elliott/CVE-2024-22867.svg)

## CVE-2024-2267
 A vulnerability was found in keerti1924 Online-Book-Store-Website 1.0 and classified as problematic. This issue affects some unknown processing of the file /shop.php. The manipulation of the argument product_price leads to business logic errors. The attack may be initiated remotely. The exploit has been disclosed to the public and may be used. The identifier VDB-256037 was assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/l00neyhacker/CVE-2024-22678](https://github.com/l00neyhacker/CVE-2024-22678) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-22678.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-22678.svg)

- [https://github.com/l00neyhacker/CVE-2024-22675](https://github.com/l00neyhacker/CVE-2024-22675) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-22675.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-22675.svg)

- [https://github.com/l00neyhacker/CVE-2024-22676](https://github.com/l00neyhacker/CVE-2024-22676) :  ![starts](https://img.shields.io/github/stars/l00neyhacker/CVE-2024-22676.svg) ![forks](https://img.shields.io/github/forks/l00neyhacker/CVE-2024-22676.svg)

## CVE-2024-2257
 This vulnerability exists in Digisol Router (DG-GR1321: Hardware version 3.7L;  Firmware version : v3.2.02) due to improper implementation of password policies. An attacker with physical access could exploit this by creating password that do not adhere to the defined security standards/policy on the vulnerable system.

Successful exploitation of this vulnerability could allow the attacker to expose the router to potential security threats.



- [https://github.com/Redfox-Security/Digisol-DG-GR1321-s-Password-Policy-Bypass-CVE-2024-2257](https://github.com/Redfox-Security/Digisol-DG-GR1321-s-Password-Policy-Bypass-CVE-2024-2257) :  ![starts](https://img.shields.io/github/stars/Redfox-Security/Digisol-DG-GR1321-s-Password-Policy-Bypass-CVE-2024-2257.svg) ![forks](https://img.shields.io/github/forks/Redfox-Security/Digisol-DG-GR1321-s-Password-Policy-Bypass-CVE-2024-2257.svg)

- [https://github.com/Redfox-Security/Digisol-DG--GR1321-s-Password-Policy-Bypass--CVE--2024-2257](https://github.com/Redfox-Security/Digisol-DG--GR1321-s-Password-Policy-Bypass--CVE--2024-2257) :  ![starts](https://img.shields.io/github/stars/Redfox-Security/Digisol-DG--GR1321-s-Password-Policy-Bypass--CVE--2024-2257.svg) ![forks](https://img.shields.io/github/forks/Redfox-Security/Digisol-DG--GR1321-s-Password-Policy-Bypass--CVE--2024-2257.svg)

## CVE-2024-2253
 The Testimonial Carousel For Elementor plugin for WordPress is vulnerable to Stored Cross-Site Scripting via URL values the plugin's carousel widgets in all versions up to, and including, 10.2.1 due to insufficient input sanitization and output escaping on user supplied attributes. This makes it possible for authenticated attackers with contributor-level and above permissions to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page.



- [https://github.com/austino2000/CVE-2024-22534](https://github.com/austino2000/CVE-2024-22534) :  ![starts](https://img.shields.io/github/stars/austino2000/CVE-2024-22534.svg) ![forks](https://img.shields.io/github/forks/austino2000/CVE-2024-22534.svg)

## CVE-2024-2242
 The Contact Form 7 plugin for WordPress is vulnerable to Reflected Cross-Site Scripting via the ‘active-tab’ parameter in all versions up to, and including, 5.9 due to insufficient input sanitization and output escaping. This makes it possible for unauthenticated attackers to inject arbitrary web scripts in pages that execute if they can successfully trick a user into performing an action such as clicking on a link.



- [https://github.com/RandomRobbieBF/CVE-2024-2242](https://github.com/RandomRobbieBF/CVE-2024-2242) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-2242.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-2242.svg)

## CVE-2024-2193
 A Speculative Race Condition (SRC) vulnerability that impacts modern CPU architectures supporting speculative execution (related to Spectre V1) has been disclosed. An unauthenticated attacker can exploit this vulnerability to disclose arbitrary data from the CPU using race conditions to access the speculative executable code paths.



- [https://github.com/uthrasri/CVE-2024-2193](https://github.com/uthrasri/CVE-2024-2193) :  ![starts](https://img.shields.io/github/stars/uthrasri/CVE-2024-2193.svg) ![forks](https://img.shields.io/github/forks/uthrasri/CVE-2024-2193.svg)

## CVE-2024-2169
 Implementations of UDP application protocol are vulnerable to network loops.   An unauthenticated attacker can use maliciously-crafted packets against a vulnerable implementation that can lead to Denial of Service (DOS) and/or abuse of resources.



- [https://github.com/renancesarr/G3-Loop-DoS](https://github.com/renancesarr/G3-Loop-DoS) :  ![starts](https://img.shields.io/github/stars/renancesarr/G3-Loop-DoS.svg) ![forks](https://img.shields.io/github/forks/renancesarr/G3-Loop-DoS.svg)

## CVE-2024-2074
 A vulnerability was found in Mini-Tmall up to 20231017 and classified as critical. This issue affects some unknown processing of the file ?r=tmall/admin/user/1/1. The manipulation of the argument orderBy leads to sql injection. The attack may be initiated remotely. The exploit has been disclosed to the public and may be used. The identifier VDB-255389 was assigned to this vulnerability.



- [https://github.com/yuziiiiiiiiii/CVE-2024-2074](https://github.com/yuziiiiiiiiii/CVE-2024-2074) :  ![starts](https://img.shields.io/github/stars/yuziiiiiiiiii/CVE-2024-2074.svg) ![forks](https://img.shields.io/github/forks/yuziiiiiiiiii/CVE-2024-2074.svg)

## CVE-2024-2054
 The Artica-Proxy administrative web application will deserialize arbitrary PHP objects supplied by unauthenticated users and subsequently enable code execution as the "www-data" user.



- [https://github.com/Madan301/CVE-2024-2054](https://github.com/Madan301/CVE-2024-2054) :  ![starts](https://img.shields.io/github/stars/Madan301/CVE-2024-2054.svg) ![forks](https://img.shields.io/github/forks/Madan301/CVE-2024-2054.svg)

## CVE-2024-2053
 The Artica Proxy administrative web application will deserialize arbitrary PHP objects supplied by unauthenticated users and subsequently enable code execution as the "www-data" user. This issue was demonstrated on version 4.50 of the The Artica-Proxy administrative web application attempts to prevent local file inclusion. These protections can be bypassed and arbitrary file requests supplied by unauthenticated users will be returned according to the privileges of the "www-data" user.



- [https://github.com/b-L-x/CVE-2024-2053](https://github.com/b-L-x/CVE-2024-2053) :  ![starts](https://img.shields.io/github/stars/b-L-x/CVE-2024-2053.svg) ![forks](https://img.shields.io/github/forks/b-L-x/CVE-2024-2053.svg)

## CVE-2024-1931
 NLnet Labs Unbound version 1.18.0 up to and including version 1.19.1 contain a vulnerability that can cause denial of service by a certain code path that can lead to an infinite loop. Unbound 1.18.0 introduced a feature that removes EDE records from responses with size higher than the client's advertised buffer size. Before removing all the EDE records however, it would try to see if trimming the extra text fields on those records would result in an acceptable size while still retaining the EDE codes. Due to an unchecked condition, the code that trims the text of the EDE records could loop indefinitely. This happens when Unbound would reply with attached EDE information on a positive reply and the client's buffer size is smaller than the needed space to include EDE records. The vulnerability can only be triggered when the 'ede: yes' option is used; non default configuration. From version 1.19.2 on, the code is fixed to avoid looping indefinitely.



- [https://github.com/passer12/CVE-2024-1931-reproduction](https://github.com/passer12/CVE-2024-1931-reproduction) :  ![starts](https://img.shields.io/github/stars/passer12/CVE-2024-1931-reproduction.svg) ![forks](https://img.shields.io/github/forks/passer12/CVE-2024-1931-reproduction.svg)

## CVE-2024-1900
 Improper session management in the identity provider authentication flow in Devolutions Server 2023.3.14.0 and earlier allows an authenticated user via an identity provider to stay authenticated after his user is disabled or deleted in the identity provider such as Okta or Microsoft O365. 

The user will stay authenticated until the Devolutions Server token expiration.



- [https://github.com/adminlove520/cve-2024-19002](https://github.com/adminlove520/cve-2024-19002) :  ![starts](https://img.shields.io/github/stars/adminlove520/cve-2024-19002.svg) ![forks](https://img.shields.io/github/forks/adminlove520/cve-2024-19002.svg)

## CVE-2024-1874
 In PHP versions 8.1.* before 8.1.28, 8.2.* before 8.2.18, 8.3.* before 8.3.5, when using proc_open() command with array syntax, due to insufficient escaping, if the arguments of the executed command are controlled by a malicious user, the user can supply arguments that would execute arbitrary commands in Windows shell.



- [https://github.com/Tgcohce/CVE-2024-1874](https://github.com/Tgcohce/CVE-2024-1874) :  ![starts](https://img.shields.io/github/stars/Tgcohce/CVE-2024-1874.svg) ![forks](https://img.shields.io/github/forks/Tgcohce/CVE-2024-1874.svg)

- [https://github.com/ox1111/-CVE-2024-1874-](https://github.com/ox1111/-CVE-2024-1874-) :  ![starts](https://img.shields.io/github/stars/ox1111/-CVE-2024-1874-.svg) ![forks](https://img.shields.io/github/forks/ox1111/-CVE-2024-1874-.svg)

## CVE-2024-1800
 
In Progress® Telerik® Report Server versions prior to 2024 Q1 (10.0.24.130), a remote code execution attack is possible through an insecure deserialization vulnerability.



- [https://github.com/sinsinology/CVE-2024-4358](https://github.com/sinsinology/CVE-2024-4358) :  ![starts](https://img.shields.io/github/stars/sinsinology/CVE-2024-4358.svg) ![forks](https://img.shields.io/github/forks/sinsinology/CVE-2024-4358.svg)

## CVE-2024-1781
 A vulnerability was found in Totolink X6000R AX3000 9.4.0cu.852_20230719. It has been rated as critical. This issue affects the function setWizardCfg of the file /cgi-bin/cstecgi.cgi of the component shttpd. The manipulation leads to command injection. The exploit has been disclosed to the public and may be used. The identifier VDB-254573 was assigned to this vulnerability. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/Icycu123/CVE-2024-1781](https://github.com/Icycu123/CVE-2024-1781) :  ![starts](https://img.shields.io/github/stars/Icycu123/CVE-2024-1781.svg) ![forks](https://img.shields.io/github/forks/Icycu123/CVE-2024-1781.svg)

## CVE-2024-1709
 ConnectWise ScreenConnect 23.9.7 and prior are affected by an Authentication Bypass Using an Alternate Path or Channel

 vulnerability, which may allow an attacker direct access to confidential information or 

critical systems.





- [https://github.com/W01fh4cker/ScreenConnect-AuthBypass-RCE](https://github.com/W01fh4cker/ScreenConnect-AuthBypass-RCE) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/ScreenConnect-AuthBypass-RCE.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/ScreenConnect-AuthBypass-RCE.svg)

- [https://github.com/HussainFathy/CVE-2024-1709](https://github.com/HussainFathy/CVE-2024-1709) :  ![starts](https://img.shields.io/github/stars/HussainFathy/CVE-2024-1709.svg) ![forks](https://img.shields.io/github/forks/HussainFathy/CVE-2024-1709.svg)

- [https://github.com/cjybao/CVE-2024-1709-and-CVE-2024-1708](https://github.com/cjybao/CVE-2024-1709-and-CVE-2024-1708) :  ![starts](https://img.shields.io/github/stars/cjybao/CVE-2024-1709-and-CVE-2024-1708.svg) ![forks](https://img.shields.io/github/forks/cjybao/CVE-2024-1709-and-CVE-2024-1708.svg)

- [https://github.com/sxyrxyy/CVE-2024-1709-ConnectWise-ScreenConnect-Authentication-Bypass](https://github.com/sxyrxyy/CVE-2024-1709-ConnectWise-ScreenConnect-Authentication-Bypass) :  ![starts](https://img.shields.io/github/stars/sxyrxyy/CVE-2024-1709-ConnectWise-ScreenConnect-Authentication-Bypass.svg) ![forks](https://img.shields.io/github/forks/sxyrxyy/CVE-2024-1709-ConnectWise-ScreenConnect-Authentication-Bypass.svg)

## CVE-2024-1708
 ConnectWise ScreenConnect 23.9.7 and prior are affected by path-traversal vulnerability, which may allow an attacker 

the ability to execute remote code or directly impact confidential data or critical systems.





- [https://github.com/W01fh4cker/ScreenConnect-AuthBypass-RCE](https://github.com/W01fh4cker/ScreenConnect-AuthBypass-RCE) :  ![starts](https://img.shields.io/github/stars/W01fh4cker/ScreenConnect-AuthBypass-RCE.svg) ![forks](https://img.shields.io/github/forks/W01fh4cker/ScreenConnect-AuthBypass-RCE.svg)

- [https://github.com/cjybao/CVE-2024-1709-and-CVE-2024-1708](https://github.com/cjybao/CVE-2024-1709-and-CVE-2024-1708) :  ![starts](https://img.shields.io/github/stars/cjybao/CVE-2024-1709-and-CVE-2024-1708.svg) ![forks](https://img.shields.io/github/forks/cjybao/CVE-2024-1709-and-CVE-2024-1708.svg)

## CVE-2024-1698
 The NotificationX – Best FOMO, Social Proof, WooCommerce Sales Popup & Notification Bar Plugin With Elementor plugin for WordPress is vulnerable to SQL Injection via the 'type' parameter in all versions up to, and including, 2.8.2 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/kamranhasan/CVE-2024-1698-Exploit](https://github.com/kamranhasan/CVE-2024-1698-Exploit) :  ![starts](https://img.shields.io/github/stars/kamranhasan/CVE-2024-1698-Exploit.svg) ![forks](https://img.shields.io/github/forks/kamranhasan/CVE-2024-1698-Exploit.svg)

- [https://github.com/jesicatjan/WordPress-NotificationX-CVE-2024-1698](https://github.com/jesicatjan/WordPress-NotificationX-CVE-2024-1698) :  ![starts](https://img.shields.io/github/stars/jesicatjan/WordPress-NotificationX-CVE-2024-1698.svg) ![forks](https://img.shields.io/github/forks/jesicatjan/WordPress-NotificationX-CVE-2024-1698.svg)

## CVE-2024-1655
 Certain ASUS WiFi routers models has an OS Command Injection vulnerability, allowing an authenticated remote attacker to execute arbitrary system commands by sending a specially crafted request.



- [https://github.com/lnversed/CVE-2024-1655](https://github.com/lnversed/CVE-2024-1655) :  ![starts](https://img.shields.io/github/stars/lnversed/CVE-2024-1655.svg) ![forks](https://img.shields.io/github/forks/lnversed/CVE-2024-1655.svg)

## CVE-2024-1651
 Torrentpier version 2.4.1 allows executing arbitrary commands on the server.

This is possible because the application is vulnerable to insecure deserialization.








- [https://github.com/sharpicx/CVE-2024-1651-PoC](https://github.com/sharpicx/CVE-2024-1651-PoC) :  ![starts](https://img.shields.io/github/stars/sharpicx/CVE-2024-1651-PoC.svg) ![forks](https://img.shields.io/github/forks/sharpicx/CVE-2024-1651-PoC.svg)

- [https://github.com/hy011121/CVE-2024-1651-exploit-RCE](https://github.com/hy011121/CVE-2024-1651-exploit-RCE) :  ![starts](https://img.shields.io/github/stars/hy011121/CVE-2024-1651-exploit-RCE.svg) ![forks](https://img.shields.io/github/forks/hy011121/CVE-2024-1651-exploit-RCE.svg)

- [https://github.com/Whiteh4tWolf/CVE-2024-1651-PoC](https://github.com/Whiteh4tWolf/CVE-2024-1651-PoC) :  ![starts](https://img.shields.io/github/stars/Whiteh4tWolf/CVE-2024-1651-PoC.svg) ![forks](https://img.shields.io/github/forks/Whiteh4tWolf/CVE-2024-1651-PoC.svg)

## CVE-2024-1642
 The MainWP Dashboard  – WordPress Manager for Multiple Websites Maintenance plugin for WordPress is vulnerable to Cross-Site Request Forgery in all versions up to, and including, 4.6.0.1. This is due to missing or incorrect nonce validation on the 'posting_bulk' function. This makes it possible for unauthenticated attackers to delete arbitrary posts via a forged request granted they can trick a site administrator into performing an action such as clicking on a link.



- [https://github.com/Symbolexe/CVE-2024-1642470](https://github.com/Symbolexe/CVE-2024-1642470) :  ![starts](https://img.shields.io/github/stars/Symbolexe/CVE-2024-1642470.svg) ![forks](https://img.shields.io/github/forks/Symbolexe/CVE-2024-1642470.svg)

## CVE-2024-1561
 An issue was discovered in gradio-app/gradio, where the `/component_server` endpoint improperly allows the invocation of any method on a `Component` class with attacker-controlled arguments. Specifically, by exploiting the `move_resource_to_block_cache()` method of the `Block` class, an attacker can copy any file on the filesystem to a temporary directory and subsequently retrieve it. This vulnerability enables unauthorized local file read access, posing a significant risk especially when the application is exposed to the internet via `launch(share=True)`, thereby allowing remote attackers to read files on the host machine. Furthermore, gradio apps hosted on `huggingface.co` are also affected, potentially leading to the exposure of sensitive information such as API keys and credentials stored in environment variables.



- [https://github.com/DiabloHTB/CVE-2024-1561](https://github.com/DiabloHTB/CVE-2024-1561) :  ![starts](https://img.shields.io/github/stars/DiabloHTB/CVE-2024-1561.svg) ![forks](https://img.shields.io/github/forks/DiabloHTB/CVE-2024-1561.svg)

- [https://github.com/DiabloHTB/Nuclei-Template-CVE-2024-1561](https://github.com/DiabloHTB/Nuclei-Template-CVE-2024-1561) :  ![starts](https://img.shields.io/github/stars/DiabloHTB/Nuclei-Template-CVE-2024-1561.svg) ![forks](https://img.shields.io/github/forks/DiabloHTB/Nuclei-Template-CVE-2024-1561.svg)

## CVE-2024-1512
 The MasterStudy LMS WordPress Plugin – for Online Courses and Education plugin for WordPress is vulnerable to union based SQL Injection via the 'user' parameter of the /lms/stm-lms/order/items REST route in all versions up to, and including, 3.2.5 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/rat-c/CVE-2024-1512](https://github.com/rat-c/CVE-2024-1512) :  ![starts](https://img.shields.io/github/stars/rat-c/CVE-2024-1512.svg) ![forks](https://img.shields.io/github/forks/rat-c/CVE-2024-1512.svg)

## CVE-2024-1441
 An off-by-one error flaw was found in the udevListInterfacesByStatus() function in libvirt when the number of interfaces exceeds the size of the `names` array. This issue can be reproduced by sending specially crafted data to the libvirt daemon, allowing an unprivileged client to perform a denial of service attack by causing the libvirt daemon to crash.



- [https://github.com/almkuznetsov/CVE-2024-1441](https://github.com/almkuznetsov/CVE-2024-1441) :  ![starts](https://img.shields.io/github/stars/almkuznetsov/CVE-2024-1441.svg) ![forks](https://img.shields.io/github/forks/almkuznetsov/CVE-2024-1441.svg)

## CVE-2024-1403
 In OpenEdge Authentication Gateway and AdminServer prior to 11.7.19, 12.2.14, 12.8.1 on all platforms supported by the OpenEdge product, an authentication bypass vulnerability has been identified.  The
vulnerability is a bypass to authentication based on a failure to properly
handle username and password.  Certain unexpected
content passed into the credentials can lead to unauthorized access without proper
authentication.    










- [https://github.com/horizon3ai/CVE-2024-1403](https://github.com/horizon3ai/CVE-2024-1403) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2024-1403.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2024-1403.svg)

## CVE-2024-1346
 Weak MySQL database root password in LaborOfficeFree affects version 19.10. This vulnerability allows an attacker to calculate the root password of the MySQL database used by LaborOfficeFree using two constants.



- [https://github.com/PeterGabaldon/CVE-2024-1346](https://github.com/PeterGabaldon/CVE-2024-1346) :  ![starts](https://img.shields.io/github/stars/PeterGabaldon/CVE-2024-1346.svg) ![forks](https://img.shields.io/github/forks/PeterGabaldon/CVE-2024-1346.svg)

## CVE-2024-1304
 Cross-site scripting vulnerability in Badger Meter Monitool that affects versions up to 4.6.3 and earlier. This vulnerability allows a remote attacker to send a specially crafted javascript payload to an authenticated user and partially hijack their browser session.



- [https://github.com/guillermogm4/CVE-2024-1304---Badgermeter-moni-tool-Reflected-Cross-Site-Scripting-XSS](https://github.com/guillermogm4/CVE-2024-1304---Badgermeter-moni-tool-Reflected-Cross-Site-Scripting-XSS) :  ![starts](https://img.shields.io/github/stars/guillermogm4/CVE-2024-1304---Badgermeter-moni-tool-Reflected-Cross-Site-Scripting-XSS.svg) ![forks](https://img.shields.io/github/forks/guillermogm4/CVE-2024-1304---Badgermeter-moni-tool-Reflected-Cross-Site-Scripting-XSS.svg)

## CVE-2024-1303
 Incorrectly limiting the path to a restricted directory vulnerability in Badger Meter Monitool that affects versions up to 4.6.3 and earlier. This vulnerability allows an authenticated attacker to retrieve any file from the device using the download-file functionality.



- [https://github.com/guillermogm4/CVE-2024-1303---Badgermeter-moni-tool-Path-Traversal](https://github.com/guillermogm4/CVE-2024-1303---Badgermeter-moni-tool-Path-Traversal) :  ![starts](https://img.shields.io/github/stars/guillermogm4/CVE-2024-1303---Badgermeter-moni-tool-Path-Traversal.svg) ![forks](https://img.shields.io/github/forks/guillermogm4/CVE-2024-1303---Badgermeter-moni-tool-Path-Traversal.svg)

## CVE-2024-1302
 Information exposure vulnerability in Badger Meter Monitool affecting versions up to 4.6.3 and earlier. A local attacker could change the application's file parameter to a log file obtaining all sensitive information such as database credentials.



- [https://github.com/guillermogm4/CVE-2024-1302---Badgermeter-moni-tool-Sensitive-information-exposure](https://github.com/guillermogm4/CVE-2024-1302---Badgermeter-moni-tool-Sensitive-information-exposure) :  ![starts](https://img.shields.io/github/stars/guillermogm4/CVE-2024-1302---Badgermeter-moni-tool-Sensitive-information-exposure.svg) ![forks](https://img.shields.io/github/forks/guillermogm4/CVE-2024-1302---Badgermeter-moni-tool-Sensitive-information-exposure.svg)

## CVE-2024-1301
 SQL injection vulnerability in Badger Meter Monitool affecting versions 4.6.3 and earlier. A remote attacker could send a specially crafted SQL query to the server via the j_username parameter and retrieve the information stored in the database.



- [https://github.com/guillermogm4/CVE-2024-1301---Badgermeter-moni-tool-SQL-Injection](https://github.com/guillermogm4/CVE-2024-1301---Badgermeter-moni-tool-SQL-Injection) :  ![starts](https://img.shields.io/github/stars/guillermogm4/CVE-2024-1301---Badgermeter-moni-tool-SQL-Injection.svg) ![forks](https://img.shields.io/github/forks/guillermogm4/CVE-2024-1301---Badgermeter-moni-tool-SQL-Injection.svg)

## CVE-2024-1269
 A vulnerability has been found in SourceCodester Product Management System 1.0 and classified as problematic. This vulnerability affects unknown code of the file /supplier.php. The manipulation of the argument supplier_name/supplier_contact leads to cross site scripting. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-253012.



- [https://github.com/sajaljat/CVE-2024-1269](https://github.com/sajaljat/CVE-2024-1269) :  ![starts](https://img.shields.io/github/stars/sajaljat/CVE-2024-1269.svg) ![forks](https://img.shields.io/github/forks/sajaljat/CVE-2024-1269.svg)

## CVE-2024-1248
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/LiChaser/CVE-2024-12484](https://github.com/LiChaser/CVE-2024-12484) :  ![starts](https://img.shields.io/github/stars/LiChaser/CVE-2024-12484.svg) ![forks](https://img.shields.io/github/forks/LiChaser/CVE-2024-12484.svg)

## CVE-2024-1212
 Unauthenticated remote attackers can access the system through the LoadMaster management interface, enabling arbitrary system command execution.






- [https://github.com/Chocapikk/CVE-2024-1212](https://github.com/Chocapikk/CVE-2024-1212) :  ![starts](https://img.shields.io/github/stars/Chocapikk/CVE-2024-1212.svg) ![forks](https://img.shields.io/github/forks/Chocapikk/CVE-2024-1212.svg)

- [https://github.com/Rehan07-Human/Exploiting-RCE-Cyber_Project_CVE-2024-1212](https://github.com/Rehan07-Human/Exploiting-RCE-Cyber_Project_CVE-2024-1212) :  ![starts](https://img.shields.io/github/stars/Rehan07-Human/Exploiting-RCE-Cyber_Project_CVE-2024-1212.svg) ![forks](https://img.shields.io/github/forks/Rehan07-Human/Exploiting-RCE-Cyber_Project_CVE-2024-1212.svg)

- [https://github.com/r0otk3r/CVE-2024-1212](https://github.com/r0otk3r/CVE-2024-1212) :  ![starts](https://img.shields.io/github/stars/r0otk3r/CVE-2024-1212.svg) ![forks](https://img.shields.io/github/forks/r0otk3r/CVE-2024-1212.svg)

## CVE-2024-1210
 The LearnDash LMS plugin for WordPress is vulnerable to Sensitive Information Exposure in all versions up to, and including, 4.10.1 via API. This makes it possible for unauthenticated attackers to obtain access to quizzes.



- [https://github.com/karlemilnikka/CVE-2024-1208-and-CVE-2024-1210](https://github.com/karlemilnikka/CVE-2024-1208-and-CVE-2024-1210) :  ![starts](https://img.shields.io/github/stars/karlemilnikka/CVE-2024-1208-and-CVE-2024-1210.svg) ![forks](https://img.shields.io/github/forks/karlemilnikka/CVE-2024-1208-and-CVE-2024-1210.svg)

## CVE-2024-1209
 The LearnDash LMS plugin for WordPress is vulnerable to Sensitive Information Exposure in all versions up to, and including, 4.10.1 via direct file access due to insufficient protection of uploaded assignments. This makes it possible for unauthenticated attackers to obtain those uploads.



- [https://github.com/karlemilnikka/CVE-2024-1209](https://github.com/karlemilnikka/CVE-2024-1209) :  ![starts](https://img.shields.io/github/stars/karlemilnikka/CVE-2024-1209.svg) ![forks](https://img.shields.io/github/forks/karlemilnikka/CVE-2024-1209.svg)

## CVE-2024-1208
 The LearnDash LMS plugin for WordPress is vulnerable to Sensitive Information Exposure in all versions up to, and including, 4.10.2 via API. This makes it possible for unauthenticated attackers to obtain access to quiz questions.



- [https://github.com/karlemilnikka/CVE-2024-1208-and-CVE-2024-1210](https://github.com/karlemilnikka/CVE-2024-1208-and-CVE-2024-1210) :  ![starts](https://img.shields.io/github/stars/karlemilnikka/CVE-2024-1208-and-CVE-2024-1210.svg) ![forks](https://img.shields.io/github/forks/karlemilnikka/CVE-2024-1208-and-CVE-2024-1210.svg)

- [https://github.com/Cappricio-Securities/CVE-2024-1208](https://github.com/Cappricio-Securities/CVE-2024-1208) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2024-1208.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2024-1208.svg)

- [https://github.com/Cappricio-Securities/.github](https://github.com/Cappricio-Securities/.github) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/.github.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/.github.svg)

## CVE-2024-1131
 ** RESERVED ** This candidate has been reserved by an organization or individual that will use it when announcing a new security problem. When the candidate has been publicized, the details for this candidate will be provided.



- [https://github.com/xthalach/CVE-2024-11318](https://github.com/xthalach/CVE-2024-11318) :  ![starts](https://img.shields.io/github/stars/xthalach/CVE-2024-11318.svg) ![forks](https://img.shields.io/github/forks/xthalach/CVE-2024-11318.svg)

## CVE-2024-1112
 Heap-based buffer overflow vulnerability in Resource Hacker, developed by Angus Johnson, affecting version 3.6.0.92. This vulnerability could allow an attacker to execute arbitrary code via a long filename argument.



- [https://github.com/enessakircolak/CVE-2024-1112](https://github.com/enessakircolak/CVE-2024-1112) :  ![starts](https://img.shields.io/github/stars/enessakircolak/CVE-2024-1112.svg) ![forks](https://img.shields.io/github/forks/enessakircolak/CVE-2024-1112.svg)

## CVE-2024-1086
 A use-after-free vulnerability in the Linux kernel's netfilter: nf_tables component can be exploited to achieve local privilege escalation.

The nft_verdict_init() function allows positive values as drop error within the hook verdict, and hence the nf_hook_slow() function can cause a double free vulnerability when NF_DROP is issued with a drop error which resembles NF_ACCEPT.

We recommend upgrading past commit f342de4e2f33e0e39165d8639387aa6c19dff660.



- [https://github.com/Notselwyn/CVE-2024-1086](https://github.com/Notselwyn/CVE-2024-1086) :  ![starts](https://img.shields.io/github/stars/Notselwyn/CVE-2024-1086.svg) ![forks](https://img.shields.io/github/forks/Notselwyn/CVE-2024-1086.svg)

- [https://github.com/andigandhi/bitpixie](https://github.com/andigandhi/bitpixie) :  ![starts](https://img.shields.io/github/stars/andigandhi/bitpixie.svg) ![forks](https://img.shields.io/github/forks/andigandhi/bitpixie.svg)

- [https://github.com/LLfam/CVE-2024-1086](https://github.com/LLfam/CVE-2024-1086) :  ![starts](https://img.shields.io/github/stars/LLfam/CVE-2024-1086.svg) ![forks](https://img.shields.io/github/forks/LLfam/CVE-2024-1086.svg)

- [https://github.com/Alicey0719/docker-POC_CVE-2024-1086](https://github.com/Alicey0719/docker-POC_CVE-2024-1086) :  ![starts](https://img.shields.io/github/stars/Alicey0719/docker-POC_CVE-2024-1086.svg) ![forks](https://img.shields.io/github/forks/Alicey0719/docker-POC_CVE-2024-1086.svg)

- [https://github.com/kevcooper/CVE-2024-1086-checker](https://github.com/kevcooper/CVE-2024-1086-checker) :  ![starts](https://img.shields.io/github/stars/kevcooper/CVE-2024-1086-checker.svg) ![forks](https://img.shields.io/github/forks/kevcooper/CVE-2024-1086-checker.svg)

- [https://github.com/CCIEVoice2009/CVE-2024-1086](https://github.com/CCIEVoice2009/CVE-2024-1086) :  ![starts](https://img.shields.io/github/stars/CCIEVoice2009/CVE-2024-1086.svg) ![forks](https://img.shields.io/github/forks/CCIEVoice2009/CVE-2024-1086.svg)

- [https://github.com/xzx482/CVE-2024-1086](https://github.com/xzx482/CVE-2024-1086) :  ![starts](https://img.shields.io/github/stars/xzx482/CVE-2024-1086.svg) ![forks](https://img.shields.io/github/forks/xzx482/CVE-2024-1086.svg)

- [https://github.com/feely666/CVE-2024-1086](https://github.com/feely666/CVE-2024-1086) :  ![starts](https://img.shields.io/github/stars/feely666/CVE-2024-1086.svg) ![forks](https://img.shields.io/github/forks/feely666/CVE-2024-1086.svg)

## CVE-2024-1071
 The Ultimate Member – User Profile, Registration, Login, Member Directory, Content Restriction & Membership Plugin plugin for WordPress is vulnerable to SQL Injection via the 'sorting' parameter in versions 2.1.3 to 2.8.2 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.



- [https://github.com/gbrsh/CVE-2024-1071](https://github.com/gbrsh/CVE-2024-1071) :  ![starts](https://img.shields.io/github/stars/gbrsh/CVE-2024-1071.svg) ![forks](https://img.shields.io/github/forks/gbrsh/CVE-2024-1071.svg)

- [https://github.com/Trackflaw/CVE-2024-1071-Docker](https://github.com/Trackflaw/CVE-2024-1071-Docker) :  ![starts](https://img.shields.io/github/stars/Trackflaw/CVE-2024-1071-Docker.svg) ![forks](https://img.shields.io/github/forks/Trackflaw/CVE-2024-1071-Docker.svg)

- [https://github.com/Matrexdz/CVE-2024-1071](https://github.com/Matrexdz/CVE-2024-1071) :  ![starts](https://img.shields.io/github/stars/Matrexdz/CVE-2024-1071.svg) ![forks](https://img.shields.io/github/forks/Matrexdz/CVE-2024-1071.svg)

- [https://github.com/Matrexdz/CVE-2024-1071-Docker](https://github.com/Matrexdz/CVE-2024-1071-Docker) :  ![starts](https://img.shields.io/github/stars/Matrexdz/CVE-2024-1071-Docker.svg) ![forks](https://img.shields.io/github/forks/Matrexdz/CVE-2024-1071-Docker.svg)

## CVE-2024-0986
 A vulnerability was found in Issabel PBX 4.0.0. It has been rated as critical. This issue affects some unknown processing of the file /index.php?menu=asterisk_cli of the component Asterisk-Cli. The manipulation of the argument Command leads to os command injection. The attack may be initiated remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-252251. NOTE: The vendor was contacted early about this disclosure but did not respond in any way.



- [https://github.com/gunzf0x/Issabel-PBX-4.0.0-RCE-Authenticated](https://github.com/gunzf0x/Issabel-PBX-4.0.0-RCE-Authenticated) :  ![starts](https://img.shields.io/github/stars/gunzf0x/Issabel-PBX-4.0.0-RCE-Authenticated.svg) ![forks](https://img.shields.io/github/forks/gunzf0x/Issabel-PBX-4.0.0-RCE-Authenticated.svg)

## CVE-2024-0783
 A vulnerability was found in Project Worlds Online Admission System 1.0 and classified as critical. This issue affects some unknown processing of the file documents.php. The manipulation leads to unrestricted upload. The attack may be initiated remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-251699.



- [https://github.com/pwnpwnpur1n/Online-Admission-System-RCE-PoC](https://github.com/pwnpwnpur1n/Online-Admission-System-RCE-PoC) :  ![starts](https://img.shields.io/github/stars/pwnpwnpur1n/Online-Admission-System-RCE-PoC.svg) ![forks](https://img.shields.io/github/forks/pwnpwnpur1n/Online-Admission-System-RCE-PoC.svg)

## CVE-2024-0757
 The Insert or Embed Articulate Content into WordPress plugin through 4.3000000023 is not properly filtering which file extensions are allowed to be imported on the server, allowing the uploading of malicious code within zip files



- [https://github.com/hunThubSpace/CVE-2024-0757-Exploit](https://github.com/hunThubSpace/CVE-2024-0757-Exploit) :  ![starts](https://img.shields.io/github/stars/hunThubSpace/CVE-2024-0757-Exploit.svg) ![forks](https://img.shields.io/github/forks/hunThubSpace/CVE-2024-0757-Exploit.svg)

## CVE-2024-0741
 An out of bounds write in ANGLE could have allowed an attacker to corrupt memory leading to a potentially exploitable crash. This vulnerability affects Firefox  122, Firefox ESR  115.7, and Thunderbird  115.7.



- [https://github.com/HyHy100/Firefox-ANGLE-CVE-2024-0741](https://github.com/HyHy100/Firefox-ANGLE-CVE-2024-0741) :  ![starts](https://img.shields.io/github/stars/HyHy100/Firefox-ANGLE-CVE-2024-0741.svg) ![forks](https://img.shields.io/github/forks/HyHy100/Firefox-ANGLE-CVE-2024-0741.svg)

## CVE-2024-0713
 ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. ConsultIDs: CVE-2020-28871. Reason: This candidate is a reservation duplicate of CVE-2020-28871. Notes: All CVE users should reference CVE-2020-28871 instead of this candidate. All references and descriptions in this candidate have been removed to prevent accidental usage.



- [https://github.com/kitodd/CVE-2024-0713](https://github.com/kitodd/CVE-2024-0713) :  ![starts](https://img.shields.io/github/stars/kitodd/CVE-2024-0713.svg) ![forks](https://img.shields.io/github/forks/kitodd/CVE-2024-0713.svg)

## CVE-2024-0710
 The GP Unique ID plugin for WordPress is vulnerable to Unique ID Modification in all versions up to, and including, 1.5.5. This is due to insufficient input validation. This makes it possible for unauthenticated attackers to tamper with the generation of a unique ID on a form submission and replace the generated unique ID with a user-controlled one, leading to a loss of integrity in cases where the ID's uniqueness is relied upon in a security-specific context.



- [https://github.com/karlemilnikka/CVE-2024-0710](https://github.com/karlemilnikka/CVE-2024-0710) :  ![starts](https://img.shields.io/github/stars/karlemilnikka/CVE-2024-0710.svg) ![forks](https://img.shields.io/github/forks/karlemilnikka/CVE-2024-0710.svg)

## CVE-2024-0684
 A flaw was found in the GNU coreutils "split" program. A heap overflow with user-controlled data of multiple hundred bytes in length could occur in the line_bytes_split() function, potentially leading to an application crash and denial of service.



- [https://github.com/Valentin-Metz/writeup_split](https://github.com/Valentin-Metz/writeup_split) :  ![starts](https://img.shields.io/github/stars/Valentin-Metz/writeup_split.svg) ![forks](https://img.shields.io/github/forks/Valentin-Metz/writeup_split.svg)

## CVE-2024-0683
 The Bulgarisation for WooCommerce plugin for WordPress is vulnerable to unauthorized access due to missing capability checks on several functions in all versions up to, and including, 3.0.14. This makes it possible for unauthenticated and authenticated attackers, with subscriber-level access and above, to generate and delete labels.



- [https://github.com/3474458191/CVE-2024-0683](https://github.com/3474458191/CVE-2024-0683) :  ![starts](https://img.shields.io/github/stars/3474458191/CVE-2024-0683.svg) ![forks](https://img.shields.io/github/forks/3474458191/CVE-2024-0683.svg)

## CVE-2024-0679
 The ColorMag theme for WordPress is vulnerable to unauthorized access due to a missing capability check on the plugin_action_callback() function in all versions up to, and including, 3.1.2. This makes it possible for authenticated attackers, with subscriber-level access and above, to install and activate arbitrary plugins.



- [https://github.com/RandomRobbieBF/CVE-2024-0679](https://github.com/RandomRobbieBF/CVE-2024-0679) :  ![starts](https://img.shields.io/github/stars/RandomRobbieBF/CVE-2024-0679.svg) ![forks](https://img.shields.io/github/forks/RandomRobbieBF/CVE-2024-0679.svg)

## CVE-2024-0582
 A memory leak flaw was found in the Linux kernel’s io_uring functionality in how a user registers a buffer ring with IORING_REGISTER_PBUF_RING, mmap() it, and then frees it. This flaw allows a local user to crash or potentially escalate their privileges on the system.



- [https://github.com/ysanatomic/io_uring_LPE-CVE-2024-0582](https://github.com/ysanatomic/io_uring_LPE-CVE-2024-0582) :  ![starts](https://img.shields.io/github/stars/ysanatomic/io_uring_LPE-CVE-2024-0582.svg) ![forks](https://img.shields.io/github/forks/ysanatomic/io_uring_LPE-CVE-2024-0582.svg)

- [https://github.com/kuzeyardabulut/CVE-2024-0582](https://github.com/kuzeyardabulut/CVE-2024-0582) :  ![starts](https://img.shields.io/github/stars/kuzeyardabulut/CVE-2024-0582.svg) ![forks](https://img.shields.io/github/forks/kuzeyardabulut/CVE-2024-0582.svg)

- [https://github.com/101010zyl/CVE-2024-0582-dataonly](https://github.com/101010zyl/CVE-2024-0582-dataonly) :  ![starts](https://img.shields.io/github/stars/101010zyl/CVE-2024-0582-dataonly.svg) ![forks](https://img.shields.io/github/forks/101010zyl/CVE-2024-0582-dataonly.svg)

- [https://github.com/0ptyx/cve-2024-0582](https://github.com/0ptyx/cve-2024-0582) :  ![starts](https://img.shields.io/github/stars/0ptyx/cve-2024-0582.svg) ![forks](https://img.shields.io/github/forks/0ptyx/cve-2024-0582.svg)

- [https://github.com/Forsaken0129/CVE-2024-0582](https://github.com/Forsaken0129/CVE-2024-0582) :  ![starts](https://img.shields.io/github/stars/Forsaken0129/CVE-2024-0582.svg) ![forks](https://img.shields.io/github/forks/Forsaken0129/CVE-2024-0582.svg)

## CVE-2024-0566
 The Smart Manager WordPress plugin before 8.28.0 does not properly sanitise and escape a parameter before using it in a SQL statement, leading to a SQL injection exploitable by high privilege users such as admin.



- [https://github.com/xbz0n/CVE-2024-0566](https://github.com/xbz0n/CVE-2024-0566) :  ![starts](https://img.shields.io/github/stars/xbz0n/CVE-2024-0566.svg) ![forks](https://img.shields.io/github/forks/xbz0n/CVE-2024-0566.svg)

## CVE-2024-0507
 An attacker with access to a Management Console user account with the editor role could escalate privileges through a command injection vulnerability in the Management Console. This vulnerability affected all versions of GitHub Enterprise Server and was fixed in versions 3.11.3, 3.10.5, 3.9.8, and 3.8.13 This vulnerability was reported via the GitHub Bug Bounty program.



- [https://github.com/convisolabs/CVE-2024-0507_CVE-2024-0200-github](https://github.com/convisolabs/CVE-2024-0507_CVE-2024-0200-github) :  ![starts](https://img.shields.io/github/stars/convisolabs/CVE-2024-0507_CVE-2024-0200-github.svg) ![forks](https://img.shields.io/github/forks/convisolabs/CVE-2024-0507_CVE-2024-0200-github.svg)

## CVE-2024-0399
 The WooCommerce Customers Manager WordPress plugin before 29.7 does not properly sanitise and escape a parameter before using it in a SQL statement, leading to an SQL injection exploitable by Subscriber+ role.



- [https://github.com/xbz0n/CVE-2024-0399](https://github.com/xbz0n/CVE-2024-0399) :  ![starts](https://img.shields.io/github/stars/xbz0n/CVE-2024-0399.svg) ![forks](https://img.shields.io/github/forks/xbz0n/CVE-2024-0399.svg)

## CVE-2024-0352
 A vulnerability classified as critical was found in Likeshop up to 2.5.7.20210311. This vulnerability affects the function FileServer::userFormImage of the file server/application/api/controller/File.php of the component HTTP POST Request Handler. The manipulation of the argument file leads to unrestricted upload. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-250120.



- [https://github.com/Cappricio-Securities/CVE-2024-0352](https://github.com/Cappricio-Securities/CVE-2024-0352) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2024-0352.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2024-0352.svg)

## CVE-2024-0324
 The User Profile Builder – Beautiful User Registration Forms, User Profiles & User Role Editor plugin for WordPress is vulnerable to unauthorized modification of data due to a missing capability check on the 'wppb_two_factor_authentication_settings_update' function in all versions up to, and including, 3.10.8. This makes it possible for unauthenticated attackers to enable or disable the 2FA functionality present in the Premium version of the plugin for arbitrary user roles.



- [https://github.com/kodaichodai/CVE-2024-0324](https://github.com/kodaichodai/CVE-2024-0324) :  ![starts](https://img.shields.io/github/stars/kodaichodai/CVE-2024-0324.svg) ![forks](https://img.shields.io/github/forks/kodaichodai/CVE-2024-0324.svg)

## CVE-2024-0305
 A vulnerability was found in Guangzhou Yingke Electronic Technology Ncast up to 2017 and classified as problematic. Affected by this issue is some unknown functionality of the file /manage/IPSetup.php of the component Guest Login. The manipulation leads to information disclosure. The attack may be launched remotely. The exploit has been disclosed to the public and may be used. The identifier of this vulnerability is VDB-249872.



- [https://github.com/jidle123/cve-2024-0305exp](https://github.com/jidle123/cve-2024-0305exp) :  ![starts](https://img.shields.io/github/stars/jidle123/cve-2024-0305exp.svg) ![forks](https://img.shields.io/github/forks/jidle123/cve-2024-0305exp.svg)

## CVE-2024-0235
 The EventON WordPress plugin before 4.5.5, EventON WordPress plugin before 2.2.7 do not have authorisation in an AJAX action, allowing unauthenticated users to retrieve email addresses of any users on the blog



- [https://github.com/Cappricio-Securities/CVE-2024-0235](https://github.com/Cappricio-Securities/CVE-2024-0235) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2024-0235.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2024-0235.svg)

## CVE-2024-0230
 A session management issue was addressed with improved checks. This issue is fixed in Magic Keyboard Firmware Update 2.0.6. An attacker with physical access to the accessory may be able to extract its Bluetooth pairing key and monitor Bluetooth traffic.



- [https://github.com/keldnorman/cve-2024-0230-blue](https://github.com/keldnorman/cve-2024-0230-blue) :  ![starts](https://img.shields.io/github/stars/keldnorman/cve-2024-0230-blue.svg) ![forks](https://img.shields.io/github/forks/keldnorman/cve-2024-0230-blue.svg)

## CVE-2024-0204
 Authentication bypass in Fortra's GoAnywhere MFT prior to 7.4.1 allows an unauthorized user to create an admin user via the administration portal.



- [https://github.com/gobysec/Goby](https://github.com/gobysec/Goby) :  ![starts](https://img.shields.io/github/stars/gobysec/Goby.svg) ![forks](https://img.shields.io/github/forks/gobysec/Goby.svg)

- [https://github.com/gobysec/GobyVuls](https://github.com/gobysec/GobyVuls) :  ![starts](https://img.shields.io/github/stars/gobysec/GobyVuls.svg) ![forks](https://img.shields.io/github/forks/gobysec/GobyVuls.svg)

- [https://github.com/horizon3ai/CVE-2024-0204](https://github.com/horizon3ai/CVE-2024-0204) :  ![starts](https://img.shields.io/github/stars/horizon3ai/CVE-2024-0204.svg) ![forks](https://img.shields.io/github/forks/horizon3ai/CVE-2024-0204.svg)

- [https://github.com/cbeek-r7/CVE-2024-0204](https://github.com/cbeek-r7/CVE-2024-0204) :  ![starts](https://img.shields.io/github/stars/cbeek-r7/CVE-2024-0204.svg) ![forks](https://img.shields.io/github/forks/cbeek-r7/CVE-2024-0204.svg)

- [https://github.com/m-cetin/CVE-2024-0204](https://github.com/m-cetin/CVE-2024-0204) :  ![starts](https://img.shields.io/github/stars/m-cetin/CVE-2024-0204.svg) ![forks](https://img.shields.io/github/forks/m-cetin/CVE-2024-0204.svg)

- [https://github.com/adminlove520/CVE-2024-0204](https://github.com/adminlove520/CVE-2024-0204) :  ![starts](https://img.shields.io/github/stars/adminlove520/CVE-2024-0204.svg) ![forks](https://img.shields.io/github/forks/adminlove520/CVE-2024-0204.svg)

## CVE-2024-0200
 An unsafe reflection vulnerability was identified in GitHub Enterprise Server that could lead to reflection injection. This vulnerability could lead to the execution of user-controlled methods and remote code execution. To exploit this bug, an actor would need to be logged into an account on the GHES instance with the organization owner role. This vulnerability affected all versions of GitHub Enterprise Server prior to 3.12 and was fixed in versions 3.8.13, 3.9.8, 3.10.5, and 3.11.3. This vulnerability was reported via the GitHub Bug Bounty program.





- [https://github.com/convisolabs/CVE-2024-0507_CVE-2024-0200-github](https://github.com/convisolabs/CVE-2024-0507_CVE-2024-0200-github) :  ![starts](https://img.shields.io/github/stars/convisolabs/CVE-2024-0507_CVE-2024-0200-github.svg) ![forks](https://img.shields.io/github/forks/convisolabs/CVE-2024-0507_CVE-2024-0200-github.svg)

## CVE-2024-0197
 A flaw in the installer for Thales SafeNet Sentinel HASP LDK prior to 9.16 on Windows allows an attacker to escalate their privilege level via local access.





- [https://github.com/ewilded/CVE-2024-0197-POC](https://github.com/ewilded/CVE-2024-0197-POC) :  ![starts](https://img.shields.io/github/stars/ewilded/CVE-2024-0197-POC.svg) ![forks](https://img.shields.io/github/forks/ewilded/CVE-2024-0197-POC.svg)

## CVE-2024-0195
 A vulnerability, which was classified as critical, was found in spider-flow 0.4.3. Affected is the function FunctionService.saveFunction of the file src/main/java/org/spiderflow/controller/FunctionController.java. The manipulation leads to code injection. It is possible to launch the attack remotely. The exploit has been disclosed to the public and may be used. VDB-249510 is the identifier assigned to this vulnerability.



- [https://github.com/Cappricio-Securities/CVE-2024-0195](https://github.com/Cappricio-Securities/CVE-2024-0195) :  ![starts](https://img.shields.io/github/stars/Cappricio-Securities/CVE-2024-0195.svg) ![forks](https://img.shields.io/github/forks/Cappricio-Securities/CVE-2024-0195.svg)

## CVE-2024-0132
 NVIDIA Container Toolkit 1.16.1 or earlier contains a Time-of-check Time-of-Use (TOCTOU) vulnerability when used with default configuration where a specifically crafted container image may gain access to the host file system. This does not impact use cases where CDI is used. A successful exploit of this vulnerability may lead to code execution, denial of service, escalation of privileges, information disclosure, and data tampering.



- [https://github.com/r0binak/CVE-2024-0132](https://github.com/r0binak/CVE-2024-0132) :  ![starts](https://img.shields.io/github/stars/r0binak/CVE-2024-0132.svg) ![forks](https://img.shields.io/github/forks/r0binak/CVE-2024-0132.svg)

## CVE-2024-0044
 In createSessionInternal of PackageInstallerService.java, there is a possible run-as any app due to improper input validation. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/0xbinder/CVE-2024-0044](https://github.com/0xbinder/CVE-2024-0044) :  ![starts](https://img.shields.io/github/stars/0xbinder/CVE-2024-0044.svg) ![forks](https://img.shields.io/github/forks/0xbinder/CVE-2024-0044.svg)

- [https://github.com/scs-labrat/android_autorooter](https://github.com/scs-labrat/android_autorooter) :  ![starts](https://img.shields.io/github/stars/scs-labrat/android_autorooter.svg) ![forks](https://img.shields.io/github/forks/scs-labrat/android_autorooter.svg)

- [https://github.com/Re13orn/CVE-2024-0044-EXP](https://github.com/Re13orn/CVE-2024-0044-EXP) :  ![starts](https://img.shields.io/github/stars/Re13orn/CVE-2024-0044-EXP.svg) ![forks](https://img.shields.io/github/forks/Re13orn/CVE-2024-0044-EXP.svg)

- [https://github.com/sridhar-sec/EvilDroid](https://github.com/sridhar-sec/EvilDroid) :  ![starts](https://img.shields.io/github/stars/sridhar-sec/EvilDroid.svg) ![forks](https://img.shields.io/github/forks/sridhar-sec/EvilDroid.svg)

- [https://github.com/nahid0x1/CVE-2024-0044](https://github.com/nahid0x1/CVE-2024-0044) :  ![starts](https://img.shields.io/github/stars/nahid0x1/CVE-2024-0044.svg) ![forks](https://img.shields.io/github/forks/nahid0x1/CVE-2024-0044.svg)

- [https://github.com/007CRIPTOGRAFIA/c-CVE-2024-0044](https://github.com/007CRIPTOGRAFIA/c-CVE-2024-0044) :  ![starts](https://img.shields.io/github/stars/007CRIPTOGRAFIA/c-CVE-2024-0044.svg) ![forks](https://img.shields.io/github/forks/007CRIPTOGRAFIA/c-CVE-2024-0044.svg)

- [https://github.com/hunter24x24/cve_2024_0044](https://github.com/hunter24x24/cve_2024_0044) :  ![starts](https://img.shields.io/github/stars/hunter24x24/cve_2024_0044.svg) ![forks](https://img.shields.io/github/forks/hunter24x24/cve_2024_0044.svg)

- [https://github.com/Dit-Developers/CVE-2024-0044-](https://github.com/Dit-Developers/CVE-2024-0044-) :  ![starts](https://img.shields.io/github/stars/Dit-Developers/CVE-2024-0044-.svg) ![forks](https://img.shields.io/github/forks/Dit-Developers/CVE-2024-0044-.svg)

- [https://github.com/Kai2er/CVE-2024-0044-EXP](https://github.com/Kai2er/CVE-2024-0044-EXP) :  ![starts](https://img.shields.io/github/stars/Kai2er/CVE-2024-0044-EXP.svg) ![forks](https://img.shields.io/github/forks/Kai2er/CVE-2024-0044-EXP.svg)

## CVE-2024-0040
 In setParameter of MtpPacket.cpp, there is a possible out of bounds read due to a heap buffer overflow. This could lead to remote information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/uthrasri/frameworks_av_CVE-2024-0040](https://github.com/uthrasri/frameworks_av_CVE-2024-0040) :  ![starts](https://img.shields.io/github/stars/uthrasri/frameworks_av_CVE-2024-0040.svg) ![forks](https://img.shields.io/github/forks/uthrasri/frameworks_av_CVE-2024-0040.svg)

## CVE-2024-0039
 In attp_build_value_cmd of att_protocol.cc, there is a possible out of bounds write due to a missing bounds check. This could lead to remote code execution with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/41yn14/CVE-2024-0039-Exploit](https://github.com/41yn14/CVE-2024-0039-Exploit) :  ![starts](https://img.shields.io/github/stars/41yn14/CVE-2024-0039-Exploit.svg) ![forks](https://img.shields.io/github/forks/41yn14/CVE-2024-0039-Exploit.svg)

## CVE-2024-0030
 In btif_to_bta_response of btif_gatt_util.cc, there is a possible out of bounds read due to an incorrect bounds check. This could lead to local information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/uthrasri/system_bt_CVE-2024-0030](https://github.com/uthrasri/system_bt_CVE-2024-0030) :  ![starts](https://img.shields.io/github/stars/uthrasri/system_bt_CVE-2024-0030.svg) ![forks](https://img.shields.io/github/forks/uthrasri/system_bt_CVE-2024-0030.svg)

## CVE-2024-0023
 In ConvertRGBToPlanarYUV of Codec2BufferUtils.cpp, there is a possible out of bounds write due to an incorrect bounds check. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/AbrarKhan/G3_Frameworks_av_CVE-2024-0023](https://github.com/AbrarKhan/G3_Frameworks_av_CVE-2024-0023) :  ![starts](https://img.shields.io/github/stars/AbrarKhan/G3_Frameworks_av_CVE-2024-0023.svg) ![forks](https://img.shields.io/github/forks/AbrarKhan/G3_Frameworks_av_CVE-2024-0023.svg)

## CVE-2024-0015
 In convertToComponentName of DreamService.java, there is a possible way to launch arbitrary protected activities due to intent redirection. This could lead to local escalation of privilege with User execution privileges needed. User interaction is not needed for exploitation.



- [https://github.com/UmVfX1BvaW50/CVE-2024-0015](https://github.com/UmVfX1BvaW50/CVE-2024-0015) :  ![starts](https://img.shields.io/github/stars/UmVfX1BvaW50/CVE-2024-0015.svg) ![forks](https://img.shields.io/github/forks/UmVfX1BvaW50/CVE-2024-0015.svg)

## CVE-2024-0012
 An authentication bypass in Palo Alto Networks PAN-OS software enables an unauthenticated attacker with network access to the management web interface to gain PAN-OS administrator privileges to perform administrative actions, tamper with the configuration, or exploit other authenticated privilege escalation vulnerabilities like  CVE-2024-9474 https://security.paloaltonetworks.com/CVE-2024-9474 .

The risk of this issue is greatly reduced if you secure access to the management web interface by restricting access to only trusted internal IP addresses according to our recommended  best practice deployment guidelines https://live.paloaltonetworks.com/t5/community-blogs/tips-amp-tricks-how-to-secure-the-management-access-of-your-palo/ba-p/464431 .

This issue is applicable only to PAN-OS 10.2, PAN-OS 11.0, PAN-OS 11.1, and PAN-OS 11.2 software.

Cloud NGFW and Prisma Access are not impacted by this vulnerability.



- [https://github.com/watchtowrlabs/palo-alto-panos-cve-2024-0012](https://github.com/watchtowrlabs/palo-alto-panos-cve-2024-0012) :  ![starts](https://img.shields.io/github/stars/watchtowrlabs/palo-alto-panos-cve-2024-0012.svg) ![forks](https://img.shields.io/github/forks/watchtowrlabs/palo-alto-panos-cve-2024-0012.svg)

- [https://github.com/Sachinart/CVE-2024-0012-POC](https://github.com/Sachinart/CVE-2024-0012-POC) :  ![starts](https://img.shields.io/github/stars/Sachinart/CVE-2024-0012-POC.svg) ![forks](https://img.shields.io/github/forks/Sachinart/CVE-2024-0012-POC.svg)

- [https://github.com/TalatumLabs/CVE-2024-0012_CVE-2024-9474_PoC](https://github.com/TalatumLabs/CVE-2024-0012_CVE-2024-9474_PoC) :  ![starts](https://img.shields.io/github/stars/TalatumLabs/CVE-2024-0012_CVE-2024-9474_PoC.svg) ![forks](https://img.shields.io/github/forks/TalatumLabs/CVE-2024-0012_CVE-2024-9474_PoC.svg)

- [https://github.com/0xjessie21/CVE-2024-0012](https://github.com/0xjessie21/CVE-2024-0012) :  ![starts](https://img.shields.io/github/stars/0xjessie21/CVE-2024-0012.svg) ![forks](https://img.shields.io/github/forks/0xjessie21/CVE-2024-0012.svg)

- [https://github.com/XiaomingX/cve-2024-0012-poc](https://github.com/XiaomingX/cve-2024-0012-poc) :  ![starts](https://img.shields.io/github/stars/XiaomingX/cve-2024-0012-poc.svg) ![forks](https://img.shields.io/github/forks/XiaomingX/cve-2024-0012-poc.svg)

- [https://github.com/iSee857/CVE-2024-0012-poc](https://github.com/iSee857/CVE-2024-0012-poc) :  ![starts](https://img.shields.io/github/stars/iSee857/CVE-2024-0012-poc.svg) ![forks](https://img.shields.io/github/forks/iSee857/CVE-2024-0012-poc.svg)

- [https://github.com/Regent8SH/PanOsExploitMultitool](https://github.com/Regent8SH/PanOsExploitMultitool) :  ![starts](https://img.shields.io/github/stars/Regent8SH/PanOsExploitMultitool.svg) ![forks](https://img.shields.io/github/forks/Regent8SH/PanOsExploitMultitool.svg)

- [https://github.com/greaselovely/CVE-2024-0012](https://github.com/greaselovely/CVE-2024-0012) :  ![starts](https://img.shields.io/github/stars/greaselovely/CVE-2024-0012.svg) ![forks](https://img.shields.io/github/forks/greaselovely/CVE-2024-0012.svg)

- [https://github.com/punitdarji/Paloalto-CVE-2024-0012](https://github.com/punitdarji/Paloalto-CVE-2024-0012) :  ![starts](https://img.shields.io/github/stars/punitdarji/Paloalto-CVE-2024-0012.svg) ![forks](https://img.shields.io/github/forks/punitdarji/Paloalto-CVE-2024-0012.svg)

## CVE-2024-0001
 A condition exists in FlashArray Purity whereby a local account intended for initial array configuration remains active potentially allowing a malicious actor to gain elevated privileges.



- [https://github.com/jiupta/CVE-2024-0001-EXP](https://github.com/jiupta/CVE-2024-0001-EXP) :  ![starts](https://img.shields.io/github/stars/jiupta/CVE-2024-0001-EXP.svg) ![forks](https://img.shields.io/github/forks/jiupta/CVE-2024-0001-EXP.svg)

- [https://github.com/RobloxSecurityResearcher/RobloxVulnerabilityCVE-2024-0001](https://github.com/RobloxSecurityResearcher/RobloxVulnerabilityCVE-2024-0001) :  ![starts](https://img.shields.io/github/stars/RobloxSecurityResearcher/RobloxVulnerabilityCVE-2024-0001.svg) ![forks](https://img.shields.io/github/forks/RobloxSecurityResearcher/RobloxVulnerabilityCVE-2024-0001.svg)

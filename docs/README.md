<h1 align="center">PocOrExp in Github</h1>

<p align="center">
  <img src="https://visitor-badge.glitch.me/badge?page_id=https://github.com/adminlove520/poc-Collector/README.md"/>
  <img src="https://img.shields.io/github/stars/adminlove520/poc-Collector"/>  
  <img src="https://img.shields.io/github/forks/adminlove520/poc-Collector"/> 
  <img src="https://img.shields.io/github/issues/adminlove520/poc-Collector"/> 
  <img src="https://img.shields.io/github/license/adminlove520/poc-Collector"/> 
</p>
<p align="center">
<img src="https://img.shields.io/github/commit-activity/m/adminlove520/poc-Collector"/>
<img src="https://img.shields.io/github/last-commit/adminlove520/poc-Collector"/>
<img src="https://img.shields.io/github/repo-size/adminlove520/poc-Collector"/>
</p>     

> Aggregating existing Poc or Exp on Github, CVE information comes from the official CVE website.
>
> Note: Aggregation is only done through general CVE numbers, so for vulnerabilities with Windows-specific numbers like MS17-010 and famous vulnerabilities with nicknames, it's better to search for them yourself.

## Usage
```
python3 exp.py -h
usage: exp.py [-h]
[-y {2020,2021,2022,2023,2024,2025,all}]
[-i {y,n}] [-w {y,n}]

CVE Details and Collect PocOrExp in Github

optional arguments:
-h, --help show this help message and exit
-y {2020,2021,2022,2023,2024,2025,all}, --year {2020,2021,2022,2023,2024,2025,all}
get Poc or CVE of certain year or all years
-i {y,n}, --init {y,n}
init or not
-w {y,n}, --watch {y,n}
keep an eye on them or not
```

Parameter description:
- -y specifies the year of CVEs to process
- -i indicates whether it is the first initialization, y means initial, and will not process already handled CVEs, n means no, and will process already handled CVEs
- -w monitors PoC changes: the current strategy is to update known CVEs with PoC from previous years, and all CVEs from the current year

Steps to use:
- STEP 1: Install dependencies
```
pip3 install -r requirements.txt
```

- STEP 2: Apply for a GitHub API token and write it into the TOKENS file in the project directory. The format is as follows, multiple tokens can be used:

```
token:your_token
```


- STEP 3: Process CVE information
```
python3 exp.py -y 2021 -i y
python3 exp.py -y all -i y
```

- If you want to speed up the process, you can use the asynchronous script exp_async.py

## PocOrExps
- [PocOrExp All](https://github.com/adminlove520/poc-Collector/blob/main/docs/PocOrExp.md)
- [2025](https://github.com/adminlove520/poc-Collector/tree/main/2025/README.md)
- [2024](https://github.com/adminlove520/poc-Collector/tree/main/2024/README.md)
- [2023](https://github.com/adminlove520/poc-Collector/tree/main/2023/README.md)
- [2022](https://github.com/adminlove520/poc-Collector/tree/main/2022/README.md)
- [2021](https://github.com/adminlove520/poc-Collector/tree/main/2021/README.md)
- [2020](https://github.com/adminlove520/poc-Collector/tree/main/2020/README.md)

## Log
- 2021-04-12: Fixed the issue of GitHub search returning results like CVE-2020-36184 when searching for CVE-2020-3618.
- 2021-04-13: Switched to CVE official data due to missing CVE numbers on the NVD website, released an asynchronous script.
- 2021-04-14: Completed the first round of PocOrExp crawling, now using 20 GitHub API tokens to poll all CVEs within 12 hours and update.
- 2021-04-16: Added -w parameter.
- 2021-04-17: Added a daily update script today.py. The update content can be seen in [Today](https://github.com/adminlove520/poc-Collector/tree/main/docs/Today.md). You can modify it, for example, to send the `get_today_update` results to yourself through services like Dingding or wxpusher.
- 2021-04-20: Found some non-PoC repos, removed them by adding a blacklist, and updated the asynchronous script to v2.
- 2021-04-23: Discovered that some results in today's update are not recently updated repos due to the following reasons:
- 1. The repo changed from private to public.
- 2. When querying through the API, the script strategy is to take the top 30 results by star count, so when the number of other repos with the same CVE increases, they enter the top 30 list, appearing as newly added today. Found that only CVE-2019-0708 has more than 100 search results, so pagination was not used to crawl all. Changed to taking the top 100 results by star count each time.
- 2021-04-30: [download](https://github.com/adminlove520/poc-Collector/tree/main/scripts/download.py) to download all PoC/Exp to prevent repo deletion by publishers. Please update git to the latest version to prevent attacks when cloning on Windows [CVE-2020-27955](https://github.com/yhsung/cve-2020-27955-po...
- 2021-05-19: Found some phishing attempts using CVE on GitHub, like [JamesGee](https://github.com/JamesGeee). No special handling, please be cautious.
- 2024-09-01: If you are unable to find the POC/EXP on GitHub, you can also check here: https://pocorexps.nsa.im/

## Star History
[![Star History Chart](https://api.star-history.com/svg?repos=adminlove520/poc-Collector&type=Date)](https://www.star-history.com/#adminlove520/poc-Collector&Date)

## Reference
- https://github.com/nomi-sec/PoC-in-GitHub

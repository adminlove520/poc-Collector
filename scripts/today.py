import os
import subprocess
import datetime

def render_today(update):
    string = []
    string.append("# Update %s"%datetime.datetime.now().strftime('%Y-%m-%d'))
    if(len(update)==0):
        string.append('No Update Today!')
    for item in update:
        string.append("## %s"%item['CVE_ID'])
        string.append("%s" % item['CVE_DESCRIPTION'])
        string.append("")
        for URL in item['PocOrExp']:
            AUTHOR = URL.split('/')[-2]
            PROJECT_NAME = URL.split('/')[-1]
            link = "- [%s](%s) : " % (URL,URL)
            stars = "![starts](https://img.shields.io/github/stars/%s/%s.svg)" %(AUTHOR,PROJECT_NAME)
            forks = "![forks](https://img.shields.io/github/forks/%s/%s.svg)" %(AUTHOR,PROJECT_NAME)
            string.append(" ".join([link,stars,forks]))
        string.append('\n')
    # 更新Today.md的路径，现在应该放在docs目录下
    with open("../docs/Today.md",'w') as f:
        f.write("\n".join(string))
    return string

def parse_readme(content):
    poc_or_exps = {}
    CVE_ID = ""
    cve_ids = []
    for line in content:
        if line.startswith('## CVE'):
            CVE_ID = "CVE"+line.split('CVE')[-1]
            cve_ids.append(CVE_ID)
            poc_or_exps[CVE_ID] = {}
            poc_or_exps[CVE_ID]['CVE_ID'] = CVE_ID
            poc_or_exps[CVE_ID]['CVE_DESCRIPTION'] = ""
            poc_or_exps[CVE_ID]['URL'] = []        
        elif line.startswith('- ['):
            url = line.split('[')[1].split(']')[0]
            poc_or_exps[CVE_ID]['URL'].append(url)
        elif line.startswith('##'):
            continue
        else:
            poc_or_exps[CVE_ID]['CVE_DESCRIPTION'] = line
    return poc_or_exps,cve_ids

def get_today_update():
    status,output = subprocess.getstatusoutput('rm -rf poc-Collector')
    status,output = subprocess.getstatusoutput('git clone git@github.com:adminlove520/poc-Collector.git poc-Collector')
    status,output = subprocess.getstatusoutput('cd poc-Collector && git tag --sort=committerdate')
    tags = output.split('\n')
    print(tags)
    if(tags and tags[-1]!=datetime.datetime.now().strftime('%Y%m%d')):
        print('date info error')
        exit(-1)
    old_poc_or_exps = []
    new_poc_or_exps = []
    if len(tags) > 1:
        status,output = subprocess.getstatusoutput('cd poc-Collector && git checkout %s' % tags[-2])
        with open('poc-Collector/PocOrExp.md') as f:
            content = f.read().split('\n')
        content = [line for line in content if line!='']
        old_poc_or_exps,old_cve_ids = parse_readme(content)
    else:
        old_cve_ids = []
    status,output = subprocess.getstatusoutput('cd poc-Collector && git checkout %s' % tags[-1])
    with open('poc-Collector/PocOrExp.md') as f:
        content = f.read().split('\n')
    content = [line for line in content if line!='']
    new_poc_or_exps,new_cve_ids = parse_readme(content)
    update = []
    for CVE_ID in new_cve_ids:
        if CVE_ID not in old_cve_ids:
            d = {}
            d['CVE_ID'] = CVE_ID
            d['CVE_DESCRIPTION'] = new_poc_or_exps[CVE_ID]['CVE_DESCRIPTION']
            d['PocOrExp'] = new_poc_or_exps[CVE_ID]['URL']
            update.append(d)
        else:
            old_urls = old_poc_or_exps[CVE_ID]['URL']
            new_urls = new_poc_or_exps[CVE_ID]['URL']
            diff = list(set(new_urls)-set(old_urls))
            if(len(diff)==0):
                continue
            d = {}
            d['CVE_ID'] = CVE_ID
            d['CVE_DESCRIPTION'] = new_poc_or_exps[CVE_ID]['CVE_DESCRIPTION']
            d['PocOrExp'] = []
            for url in new_urls:
                if url in diff:
                    d['PocOrExp'].append(url)
            update.append(d)
    return render_today(update)

if __name__=="__main__":
    update_today = get_today_update()

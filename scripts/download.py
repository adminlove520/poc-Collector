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

from tqdm import tqdm
import os
cwd = os.path.abspath(os.path.dirname(__file__))
repo_root = os.path.join(cwd,'repo')

def clone_repos(urls):
    urls = list(set(urls))
    for url in tqdm(urls):
        author = url.split('/')[-2]
        repo_name = url.split('/')[-1]
        author_path = os.path.join(repo_root,author)
        if not os.path.exists(author_path): 
            os.mkdir(author_path)
        repo_path = os.path.join(author_path,repo_name)
        if os.path.exists(repo_path):
            cmd = "cd %s && git pull" % repo_path
        else:
            cmd = "cd %s && git clone %s" % (author_path,url)
        os.system(cmd)
        

if __name__=="__main__":
    # 更新路径引用
    if os.path.exists(os.path.join(cwd,"..","poc-Collector")):
        cmd = "cd %s && git pull"%os.path.join(cwd,"..","poc-Collector")
    else:
        cmd = "cd %s && git clone %s" % (os.path.join(cwd,".."),"https://github.com/adminlove520/poc-Collector")
    os.system(cmd)
    if not os.path.exists(repo_root):
        os.mkdir(repo_root)
    with open(os.path.join(cwd,'..','docs','PocOrExp.md')) as f:
        content = f.read().split('\n')
    poc_or_exps,cve_ids = parse_readme(content)
    urls = []
    for cve_id in cve_ids:
        urls+=poc_or_exps[cve_id]['URL']
    # 更新urls文件路径，现在应该放在scripts目录下
    with open(os.path.join(cwd,'urls'),'w') as f:
        f.write('\n'.join(urls))
    clone_repos(urls)

import json
import os
import shutil
import argparse
import datetime
import time
from random import sample
from tqdm import tqdm
from loguru import logger
import asyncio
import requests
import warnings
import sys

# 导入异步兼容性模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from async_compat import async_compat, check_async_compatibility

# 检查异步兼容性
compatibility_result = check_async_compatibility()
if not compatibility_result['compatible']:
    warnings.warn(compatibility_result['recommendation'])
    warnings.warn("❌ 异步功能可能不可用，建议使用同步脚本exp.py")

try:
    # 尝试获取异步请求对象
    aio_requests = async_compat.get_requests()
    if not aio_requests:
        # 如果没有异步支持，使用requests替代
        aio_requests = None
        warnings.warn("⚠️ 无法获取异步请求对象，将使用同步请求")
except Exception as e:
    aio_requests = None
    warnings.warn(f"⚠️ 获取异步请求对象时出错: {str(e)}")

# 确保导入json模块
import json

# 使用绝对路径确保正确找到文件
import os
sCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(sCRIPTS_DIR, '..'))
DOWNLOAD_DIR = os.path.join(PROJECT_ROOT, 'download')
TOKEN_FILE = os.path.join(PROJECT_ROOT, 'config', 'TOKENS')
BLACKLIST_FILE = os.path.join(PROJECT_ROOT, 'config', 'blacklist.txt')
tokens = []
blacklist = []

def download_cve_xml(filename):
    base_url = "https://cve.mitre.org/data/downloads/"
    url = base_url + filename
    logger.info(url)
    try:
        xml_content = requests.get(url, timeout = 600,stream=True)
    except Exception as e:
        logger.error("get cve xml file error!")
        exit(-1)
    with open(os.path.join(DOWNLOAD_DIR, filename), 'wb') as f:
        for chunk in xml_content:
            f.write(chunk)

def download_cve_xml_all():
    filenames = ["allitems-cvrf-year-%d.xml"%year for year in range(2020,datetime.datetime.now().year+1)]
    for filename in filenames:
        download_cve_xml(filename)
   
def parse_cve_xml(filename):
    with open(os.path.join(DOWNLOAD_DIR, filename),'rb') as f:
        content = f.read().split(b'\n')
    cve_infos = []
    cve_ids = []
    cve_descriptions = []
    for line in content:
        line = line.strip()
        if line.startswith(b"<CVE>"):
            cve_ids.append(line[5:-6].decode(encoding='utf-8'))
        if line.startswith(b'<Note Ordinal="1" Type="Description">'):
            cve_descriptions.append(line[37:-7].decode('utf-8','ignore'))
    cve_infos = []
    if(len(cve_ids)!=len(cve_descriptions)):
        logger.error("xml of cve process error")
        exit(-1)
    else:
        for i in range(len(cve_ids)):
            cve_infos.append({'CVE_ID': cve_ids[i], 'CVE_DESCRIPTION': cve_descriptions[i]})
        return cve_infos
    
def generate_markdown_year(year):
    year = str(year)
    filenames = os.listdir(year)
    filenames = [filename for filename in filenames if filename.startswith('CVE')]
    cve_number = [[int(filename.split('.')[0].split('-')[-1]),filename] for filename in filenames]
    cve_number.sort( key=lambda e:e[0], reverse=True)
    string = []
    for number in cve_number:
        filename = os.path.join(year,number[1])
        # print(filename)
        with open(filename,'r') as f:
            cve_info = json.load(f)
            if(cve_info['PocOrExp_NUM']==0):
                continue
            else:
                string.append("## %s" % cve_info['CVE_ID'])
                string.append("> %s\n" % cve_info['CVE_DESCRIPTION'])
                string.append("\n")
                for PocOrExp in cve_info['PocOrExp']:
                    URL = PocOrExp['URL']
                    AUTHOR = URL.split('/')[-2]
                    PROJECT_NAME = URL.split('/')[-1]
                    link = "- [%s](%s) : " % (URL,URL)
                    stars = "![starts](https://img.shields.io/github/stars/%s/%s.svg)" %(AUTHOR,PROJECT_NAME)
                    forks = "![forks](https://img.shields.io/github/forks/%s/%s.svg)" %(AUTHOR,PROJECT_NAME)
                    string.append(" ".join([link,stars,forks])+'\n')
    with open(os.path.join(year,"README.md"),'w') as f:
        tmp = "\n".join(string)
        tmp = tmp.replace("<","")
        tmp = tmp.replace(">","")
        f.write(tmp)
    return string

def generate_markdown():
    PocOrExps = []
    for year in list(range(2020, datetime.datetime.now().year+1))[::-1]:
        string = generate_markdown_year(year)
        PocOrExps.append('## %d' % year)
        PocOrExps = PocOrExps + string
        PocOrExps.append('\n')
    # 更新PocOrExp.md的路径，现在应该放在docs目录下
    with open('../docs/PocOrExp.md','w') as f:
        tmp = '\n'.join(PocOrExps)
        tmp = tmp.replace("<","").replace(">","")
        f.write(tmp)

async def get_PocOrExp_in_github(CVE_ID,Other_ID = None,token=None):
    if(Other_ID == None):
        api = 'https://api.github.com/search/repositories?q="%s"&sort=stars&per_page=100' % CVE_ID
    else:
        api = 'https://api.github.com/search/repositories?q="%s" NOT "%s"&sort=stars&per_page=100' % (CVE_ID,Other_ID)
    
    windows = 0.3
    while(True):
        time.sleep(windows)
        headers = {"Authorization": "token "+token}
        
        try:
            if aio_requests:
                # 使用异步请求
                req = await aio_requests.get(api,headers = headers)
                req = await req.text()
            else:
                # 使用同步请求替代
                warnings.warn(f"⚠️ 使用同步请求替代异步请求: {CVE_ID}")
                req = requests.get(api, headers=headers, timeout=60)
                req = req.text
            
            req = json.loads(req)
            logger.info("CVE_ID: %s , token: %s"%(CVE_ID, token))
            if('items' in req):
                items = req['items']
                break
            else:
                token = sample(tokens,1)[0]
                windows += 0.1
        except Exception as e:
            logger.error(f"请求错误: {str(e)}")
            token = sample(tokens,1)[0]
            windows += 0.1
    PocOrExps = []
    for item in items:
        URL = item['html_url']
        flag = False
        for burl in blacklist:
            if URL.startswith(burl):
                flag = True
                break
        if flag:
            continue
        STARS_NUM = item['stargazers_count']
        FORKS_NUM = item['forks_count']
        DESCRIPTION = item['description']
        UPDATE_TIME = item['updated_at']
        PocOrExps.append({
            'URL': URL,
            'STARS_NUM': STARS_NUM,
            'FORKS_NUM': FORKS_NUM,
            'DESCRIPTION': DESCRIPTION,
            'UPDATE_TIME': UPDATE_TIME
        })
    return PocOrExps

def parse_arg():
    parser = argparse.ArgumentParser(
        description='CVE Details and Collect PocOrExp in Github')
    parser.add_argument('-y', '--year',required=False,default=None, choices=list(map(str,range(2020,datetime.datetime.now().year+1)))+['all'],
                        help="get Poc or CVE of certain year or all years")
    parser.add_argument('-i','--init',required=False,default='n',choices=['y','n'],help = "init or not")
    parser.add_argument('-w','--watch',required=False,default='n',choices = ['y','n'],help = "keep an eye on them or not")
    args = parser.parse_args()
    return args

def is_prefix(cve_ids,CVE_ID):
    for cve_id in cve_ids:
        if cve_id!= CVE_ID and cve_id.startswith(CVE_ID):
            return True
    return False

def get_all_startswith_CVE_ID(cve_ids,CVE_ID):
    result = []
    for cve_id in cve_ids:
        if cve_id!= CVE_ID and cve_id.startswith(CVE_ID):
            result.append(cve_id)
    return result

async def process_single_cve(cve_ids,item,token):
    CVE_ID = item['CVE_ID']
    year = item['CVE_ID'].split("-")[1]
    dump_file = os.path.join(year, CVE_ID + '.json')
    PocOrExps = []
    if(not is_prefix(cve_ids,CVE_ID)):
        PocOrExps = await get_PocOrExp_in_github(CVE_ID,None,token)
    else:
        PocOrExps = await get_PocOrExp_in_github(CVE_ID,None,token)
        if(len(PocOrExps)!=0):
            other_ids = get_all_startswith_CVE_ID(cve_ids,CVE_ID)
            PocOrExps = await get_PocOrExp_in_github(CVE_ID,None,token)
            for other_id in other_ids:
                tmp = await get_PocOrExp_in_github(CVE_ID,other_id,token)
                urls_CVE_ID = []
                urls_Other_ID = []
                for PocOrExp in PocOrExps:
                    urls_CVE_ID.append(PocOrExp['URL'])
                for PocOrExp in tmp:
                    urls_Other_ID.append(PocOrExp['URL'])
                urls_CVE_ID = list(set(urls_CVE_ID) & set(urls_Other_ID))
                tmp = PocOrExps
                PocOrExps = []
                for PocOrExp in tmp:
                    if(PocOrExp['URL'] in urls_CVE_ID):
                        PocOrExps.append(PocOrExp)
    cve_info = {}
    cve_info['CVE_ID'] = item['CVE_ID']
    cve_info['CVE_DESCRIPTION'] = item['CVE_DESCRIPTION']
    cve_info['PocOrExp_NUM'] = len(PocOrExps)
    cve_info['PocOrExp'] = PocOrExps
    with open(dump_file, 'w') as f:
        json.dump(cve_info, f)



async def process_single_cve_async(cve_ids,cve,token,sema):
    async with sema:
        await process_single_cve(cve_ids,cve,token)
    

def process_cve(cve_infos,cve_ids,init = True):
    tasks = []
    sema = asyncio.Semaphore(len(tokens))
    for i in range(len(cve_infos)):
        tasks.append(asyncio.ensure_future(process_single_cve_async(cve_ids,cve_infos[i],tokens[i % len(tokens)],sema)))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks)) 

def process_cve_year(year,init = True):
    filename = "allitems-cvrf-year-%d.xml"%year
    download_cve_xml(filename)
    cve_infos = parse_cve_xml(filename)
    cve_ids = []
    for item in cve_infos:
        cve_ids.append(item['CVE_ID'])
    tmp = []
    if(init):
        for item in cve_infos:
            CVE_ID = item['CVE_ID']
            year = item['CVE_ID'].split("-")[1]
            dump_file = os.path.join(year, CVE_ID + '.json')
            if(init and os.path.exists(dump_file)):
                continue
            else:
                tmp.append(item)
        cve_infos = tmp
    process_cve(cve_infos,cve_ids,init)
    generate_markdown()
    
def process_cve_all(init = True):
    for year in list(range(2020,datetime.datetime.now().year+1))[::-1]:
        process_cve_year(year,init)

def init():
    # 更新日志文件路径
    logger.add('../PocOrExps.log',format="{time} {level} {message}",rotation="1000 MB")
    if(not os.path.exists(DOWNLOAD_DIR)):
        os.mkdir(DOWNLOAD_DIR)
    for year in range(2020, datetime.datetime.now().year+1):
        if(not os.path.exists(str(year))):
            os.mkdir(str(year))
    if(not os.path.exists(TOKEN_FILE)):
        logger.error("TOKEN FILE NOT EXISTS!")
        exit(-1)
        
    global tokens
    with open(TOKEN_FILE) as f:
        content = f.readlines()
    for line in content:
        line = line.strip()
        if line.startswith("token:"):
            tokens.append(line.split(":")[-1])
    logger.info(tokens)
    if(len(tokens)==0):
        logger.error("NO TOKEN IN TOKEN FILE")
        exit(-1)
        
    global blacklist
    with open(BLACKLIST_FILE) as f:
        content = f.readlines()
    for line in content:
        line = line.strip()
        if(line!=""):
            blacklist.append(line)

def update_year(year):
    filenames = os.listdir('%d'%year)
    filenames = [filename for filename in filenames if filename.startswith('CVE')]
    cve_ids = []
    cve_infos = []
    for filename in filenames:
        with open(os.path.join(str(year),filename)) as f:
            cve_info = json.load(f)
        cve_ids.append(cve_info['CVE_ID'])
        if(cve_info['PocOrExp_NUM']!=0):
            cve_infos.append({'CVE_ID':cve_info['CVE_ID'],'CVE_DESCRIPTION':cve_info['CVE_DESCRIPTION']})
    process_cve(cve_infos,cve_ids,init)

def watch():
    '''
    对今年以前的有Exp的CVE进行更新
    对今年的CVE全部更新
    '''
    for year in list(range(2020,datetime.datetime.now().year+1))[::-1]:
        update_year(year)
        generate_markdown()
    process_cve_year(datetime.datetime.now().year,False)
    generate_markdown()



def main():
    args = parse_arg()
    init()
    print(args)
    if(args.year == "all"):
        if(args.init == "y"):
            process_cve_all()
        elif(args.init == "n"):
            process_cve_all(False)
    elif(args.year):
        if(args.init == "y"):
            process_cve_year(int(args.year))
        elif(args.init == "n"):
            process_cve_year(int(args.year),False)
    if(args.watch == "y"):
        watch()

if __name__=="__main__":
    main()

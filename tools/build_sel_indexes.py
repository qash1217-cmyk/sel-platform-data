import csv, json, os
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(BASE, 'SEL平台規劃')
SRC = os.path.join(PLAN, '07_第一批100筆資源.csv')

TYPE_MAP = {
    '評量': '評量工具與量表', '審查工具': '評量工具與量表',
    '教學活動': '教學活動與教案', '教學策略': '教學活動與教案', '方案與課程': '教學活動與教案',
    '研究與證據': '學術文獻與實證', '框架': '學術文獻與實證', '政策與系統': '學術文獻與實證',
    '文化與公平': '學術文獻與實證', '案例': '學術文獻與實證', '課綱對應': '學術文獻與實證',
    '教師專業': '研習模組與講師素材', '家庭合作': '研習模組與講師素材'
    , '反思工具': '評量工具與量表', '社區合作': '研習模組與講師素材'
}
DOMAIN_MAP = {'教師自我覺察':'自我覺察', '自我管理':'自我管理', '社會覺察':'社會覺察', '人際關係':'人際關係', '負責任決定':'負責任的決定', '負責任的決定':'負責任的決定'}
STAGE_MAP = {'幼兒／國小':'幼兒園;國小', '國小／國中':'國小;國中', '國中／高中':'國中;高中職', '國小／高中':'國小;高中職', '跨階段':'幼兒園;國小;國中;高中職;大專'}

def curriculum(row):
    title, cat = row['title'], row['category']
    issue = []
    if '家庭' in title or cat == '家庭合作': issue.append('家庭教育')
    if '品德' in title or '正向' in title: issue.append('品德教育')
    if '生命' in title or '決策' in title: issue.append('生命教育')
    if '性別' in title: issue.append('性別平等教育')
    if '人權' in title or '公平' in title: issue.append('人權教育')
    if not issue and ('關係' in title or '衝突' in title or '合作' in title): issue.append('品德教育')
    area = '綜合活動領域' if cat in ('教學活動','教師專業','家庭合作') else '跨領域'
    competency = 'A1;B1;C1' if cat in ('研究與證據','框架','政策與系統') else 'A2;B1;C2'
    return competency, area, ';'.join(issue) if issue else '跨領域議題融入', '依教育階段與學習領域進行課程融入；正式對應待審查。'

def domains(row):
    direct = DOMAIN_MAP.get(row['sel_domain'])
    if direct: return direct
    title = row['title']
    found = []
    for keyword, domain in [('情緒','自我覺察'),('覺察','自我覺察'),('壓力','自我管理'),('調節','自我管理'),('心理健康','自我管理'),('同理','社會覺察'),('公平','社會覺察'),('家庭','社會覺察'),('關係','人際關係'),('衝突','人際關係'),('溝通','人際關係'),('合作','人際關係'),('決策','負責任的決定'),('選擇','負責任的決定')]:
        if keyword in title and domain not in found: found.append(domain)
    return ';'.join(found) if found else '自我覺察;自我管理;社會覺察;人際關係;負責任的決定'

with open(SRC, encoding='utf-8-sig', newline='') as f: raw = list(csv.DictReader(f))
out = []
for r in raw:
    comp, area, issue, note = curriculum(r)
    out.append({'resource_id':r['id'], 'title':r['title'], 'resource_type':TYPE_MAP.get(r['category'],'待分類'), 'sel_core_competency':domains(r), 'education_stage':STAGE_MAP.get(r['education_stage'],r['education_stage']), 'curriculum_108_competency':comp, 'curriculum_108_area':area, 'curriculum_108_issue':issue, 'curriculum_108_performance':'待依教育階段與領域補填', 'curriculum_108_content':note, 'mapping_status':'建議對應／待審查', 'source':r['source'], 'source_url':r['url'], 'verification_status':r['verification_status'], 'license_or_access':r['license_or_access'], 'notes':r['notes']})

fields = list(out[0].keys())
def write_csv(path, rows):
    with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

write_csv(os.path.join(PLAN, '12_SEL主分類索引.csv'), out)
views = [('13_依資源類型索引.csv','resource_type'),('14_依SEL五大能力索引.csv','sel_core_competency'),('15_依教育階段索引.csv','education_stage'),('16_108課綱對應索引.csv','curriculum_108_issue')]
for filename, key in views: write_csv(os.path.join(PLAN, filename), sorted(out, key=lambda x:(x[key],x['resource_id'])))

tree = {'依資源類型':defaultdict(list),'依SEL五大核心能力':defaultdict(list),'依教育階段':defaultdict(list),'108課綱相關資訊':defaultdict(list)}
for r in out:
    for label,key in [('依資源類型','resource_type'),('依SEL五大核心能力','sel_core_competency'),('依教育階段','education_stage'),('108課綱相關資訊','curriculum_108_issue')]:
        for value in r[key].split(';'): tree[label][value].append(r['resource_id'])
with open(os.path.join(PLAN, '17_SEL分類索引.json'), 'w', encoding='utf-8') as f: json.dump({k:dict(v) for k,v in tree.items()}, f, ensure_ascii=False, indent=2)
print(f'generated {len(out)} indexed resources')


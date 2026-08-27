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

def summary(row, mapped):
    title = row['title']
    phrases = {'Framework':'整理社會情緒學習的核心概念、能力面向與學校實施脈絡，提供教師建立共同語言及規劃課程的基礎。','Systemic Implementation':'說明如何把社會情緒學習連結到教室、學校、家庭與社區，協助學校規劃一致而持續的推動策略。','Program Guide':'彙整不同社會情緒學習方案的內容與證據資訊，便於教育工作者比較方案特色、實施條件與研究支持。','SSES':'介紹 OECD 社會與情緒技能研究的測量架構、背景變項與結果解讀方向，供研究與政策規劃參考。','EASEL':'提供社會情緒學習相關術語、理論與研究索引，協助教師從概念理解延伸到課堂實踐。','RULER':'以情緒識讀、理解、命名、表達與調節為主軸，提供建立情緒語言與支持性班級文化的教學思路。','EEF':'整理社會情緒學習的教學與實施建議，聚焦明確教學、課堂實踐、成人學習及全校推動的條件。','UNESCO':'從教育福祉、心理健康、包容與公平的角度，說明學校如何建立安全且支持學習的環境。','US ED':'彙整學校社會情緒學習、心理健康與教育工作者支持的政策和實務方向，提供學校系統規劃參考。','教育部':'提供臺灣教育政策、學生輔導、友善校園、正向管教與教師專業發展相關資訊，協助連結 SEL 與本土教育脈絡。','國教院':'整理十二年國民基本教育課綱、核心素養、議題融入及教育研究資料，作為 SEL 課程對照與教學設計的基礎。','教師在職進修網':'提供教師研習與專業成長課程的查詢入口，可依課程主題、辦理單位與研習資訊進一步查核。'}
    for key, text in phrases.items():
        if key in title or key in row['source']: return text
    if '情緒' in title: return '聚焦情緒辨識、情緒語言或情緒調節的教學與實踐，提供教師理解學生反應及設計引導活動的參考。'
    if '衝突' in title or '關係' in title or '合作' in title: return '聚焦班級互動、同儕合作與衝突處理，提供教師引導對話、修復關係及建立班級共同規範的參考。'
    if '教師' in title or '研習' in title: return '聚焦教師專業學習與教學實踐，協助教育工作者將 SEL 概念轉化為可操作的課堂或學校行動。'
    if '案例' in row['category'] or '方案' in title: return '記錄教育現場的推動背景、實施方式與反思，提供教師與學校規劃 SEL 行動時參考與調整。'
    return '整理社會情緒學習相關的概念、研究或教學實踐，提供教師進行專業學習、課程設計與教學反思時參考。'

resource_cards = []
for r, mapped in zip(raw, out):
    resource_cards.append({'resource_id':mapped['resource_id'], 'title':mapped['title'], 'abstract_summary':summary(r,mapped), 'resource_type':mapped['resource_type'], 'sel_core_competency':mapped['sel_core_competency'], 'education_stage':mapped['education_stage'], 'curriculum_108_issue':mapped['curriculum_108_issue'], 'source':mapped['source'], 'source_url':mapped['source_url'], 'verification_status':mapped['verification_status'], 'license_or_access':mapped['license_or_access'], 'notes':mapped['notes']})
with open(os.path.join(PLAN, '18_SEL資源摘要索引.json'), 'w', encoding='utf-8') as f: json.dump(resource_cards, f, ensure_ascii=False, indent=2)
core_competencies = [
 {'id':'self-awareness','name':'自我覺察','definition':'辨識自己的情緒、想法、價值、優勢與限制，理解它們如何影響行為與選擇。','teacher_focus':'協助學生說出感受與需要，辨識個人優勢，並建立安全的自我表達方式。','classroom_entry':'情緒詞彙、情緒簽到、優勢卡與學習反思。'},
 {'id':'self-management','name':'自我管理','definition':'調節情緒、想法與行為，管理壓力、延宕滿足、設定目標並持續採取行動。','teacher_focus':'示範停看聽、呼吸、尋求協助與目標拆解，讓學生練習選擇合適的調節策略。','classroom_entry':'情緒調節工具箱、目標卡、冷靜區與壓力調節練習。'},
 {'id':'social-awareness','name':'社會覺察','definition':'理解他人的觀點與感受，展現同理，並理解家庭、學校與社會中的規範與資源。','teacher_focus':'引導學生觀點取替、尊重差異、辨識偏見，並學會尋找支持資源。','classroom_entry':'觀點交換、同理聆聽、多元文化討論與支持網絡地圖。'},
 {'id':'relationship-skills','name':'人際關係','definition':'建立與維持健康關係，包含溝通、傾聽、合作、協商、衝突處理與尋求或提供幫助。','teacher_focus':'教導具體的溝通句型、合作角色、修復式對話與衝突後的關係修復。','classroom_entry':'合作規範、角色扮演、班級會議與修復式對話圈。'},
 {'id':'responsible-decision-making','name':'負責任的決定','definition':'依據倫理、安全、社會規範與可能後果，做出兼顧自己與他人的建設性選擇。','teacher_focus':'讓學生辨識問題、比較選項、預測後果，並反思決定對自己與群體的影響。','classroom_entry':'問題解決步驟卡、情境判斷、選擇與後果及行動反思。'}]
with open(os.path.join(PLAN, '19_SEL五大核心能力說明.json'), 'w', encoding='utf-8') as f: json.dump(core_competencies, f, ensure_ascii=False, indent=2)
print(f'generated {len(out)} indexed resources')


import json,sys
W=json.load(open(sys.argv[1]))
A={a['id']:a for a in W['aufgaben']}
def show(i):
    a=A[i]; print("=====",i,a['titel'],"| S",a['stufe'],"|",a['kategorie'],a['fallen'])
    for b in a['inhalt']:
        if b['t'] in('text','hinweis'): print("TXT:",b['md'])
        elif b['t']=='code': print("CODE:\n"+b['code'])
        elif b['t']=='tabelle':
            print("TAB:",b['kopf']); [print("   ",z) for z in b['zeilen']]
        else: print(b['t'], json.dumps(b,ensure_ascii=False)[:300])
    print("IA:",json.dumps(a['interaktion'],ensure_ascii=False)[:400])
    print("LOE:",json.dumps(a['loesung'],ensure_ascii=False)[:600])
    print("TIPP:",a['tipps'])
    print("ERK:",a['erklaerung'][0]['md'])
for i in sys.argv[2:]: show(i)

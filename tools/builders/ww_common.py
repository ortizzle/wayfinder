# Builder for River's Wordly Wise units (Wayfinder).
import json, io, time

def card(C, term, d, sp=None, hint=None, frm='source'):
    c = {'id': 'c%d' % len(C), 'term': term, 'def': d}
    if sp: c['sp'] = sp
    if hint: c['hint'] = hint
    c['from'] = frm
    C.append(c)

def q(Q, lv, text, opts, ans, hint, steps, main, tip, frm='source', kind='mc', qid=None):
    Q.append({'id': qid or ('q%d' % len(Q)), 'lv': lv, 'from': frm, 'kind': kind, 'q': text,
              'opts': opts, 'ans': ans, 'hint': hint, 'steps': steps,
              'ex': {'main': main, 'tip': tip}})

def build(C, Q, uid, title, summary, why, objectives, parentNote, nextUp, path,
          srcName, source, offset_hours=6):
    errs = []
    for c in C:
        if not c['def'].startswith('**'): errs.append('%s: def not bold-first' % c['id'])
        if c.get('from') not in ('source','added'): errs.append('%s: bad from' % c['id'])
    seen = set()
    for x in Q:
        if x['id'] in seen: errs.append('%s: duplicate id' % x['id'])
        seen.add(x['id'])
        if x['kind'] == 'mc':
            if len(x['opts']) != 4: errs.append('%s: %d opts' % (x['id'], len(x['opts'])))
            if len(set(x['opts'])) != len(x['opts']): errs.append('%s: duplicate opts' % x['id'])
        if x['kind'] == 'spell':
            if len(x['opts']) != 1: errs.append('%s: spell needs exactly 1 opt' % x['id'])
            w = x['opts'][0]
            if w != w.lower().strip() or not w.isalpha():
                errs.append('%s: spell answer must be a bare lowercase word' % x['id'])
        if not (0 <= x['ans'] < len(x['opts'])): errs.append('%s: ans out of range' % x['id'])
        if not (3 <= len(x['steps']) <= 6): errs.append('%s: %d steps' % (x['id'], len(x['steps'])))
        if not x['ex']['main'].startswith('**'): errs.append('%s: ex.main not bold' % x['id'])
        if x['lv'] not in (1,2,3): errs.append('%s: bad lv' % x['id'])
    assert not errs, errs
    unit = {
        'id': uid, 'type': 'unit',
        'updatedAt': int(time.time()*1000) - int(offset_hours*3600*1000),
        'classId': 'english', 'quarter': 1, 'status': 'draft', 'title': title,
        'srcName': srcName, 'source': source,
        'summary': {'text': summary, 'from': 'source'},
        'why': {'text': why, 'from': 'added'},
        'objectives': [{'text': t, 'from': f} for t, f in objectives],
        'parentNote': {'text': parentNote, 'from': 'added'},
        'nextUp': {'text': nextUp[0], 'minutes': nextUp[1], 'from': 'added'},
        'cards': C, 'questions': Q,
    }
    io.open('/home/user/wayfinder/' + path, 'w', encoding='utf-8').write(
        json.dumps({'v': 4, 'records': {uid: unit}}, ensure_ascii=False, indent=1))
    lv = {1:0, 2:0, 3:0}
    for x in Q: lv[x['lv']] += 1
    print('%-26s %2d cards (%d with sp) · %2d questions %s · %d spell' % (
        path.split('/')[-1], len(C), sum(1 for c in C if c.get('sp')), len(Q), lv,
        sum(1 for x in Q if x['kind']=='spell')))

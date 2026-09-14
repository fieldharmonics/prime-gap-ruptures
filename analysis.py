"""Exact rupture/recovery audit. Run: python3 analysis.py. Standard library only.
Published priority is accepted only through B=10**20; local sieve through 10**8.
Distances count later gaps/records/ruptures completed by the recovery upper endpoint.
"""
import csv,json,math,time,platform,hashlib
from pathlib import Path
try:
    import resource
except ImportError:  # The standard resource module is unavailable on Windows.
    resource=None
ROOT=Path(__file__).resolve().parent
B=10**20
BASES=(2,3,5,7,11,13,17,19,23,29,31,37,41)
MR_LIMIT=3317044064679887385961981
def prime(n):
    if not 0<=n<MR_LIMIT: raise ValueError('Outside deterministic test range')
    if n<2:return False
    for a in BASES:
        if n%a==0:return n==a
    d=n-1;r=0
    while d%2==0:d//=2;r+=1
    for a in BASES:
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(r-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True
def primes(bound,block=1000000):
    """Segmented Eratosthenes; no floating point in sieve bounds."""
    root=math.isqrt(bound);a=bytearray(b'\1')*(root+1);a[:2]=b'\0\0'
    for p in range(2,math.isqrt(root)+1):
        if a[p]:a[p*p::p]=b'\0'*((root-p*p)//p+1)
    base=[p for p in range(2,root+1) if a[p]]
    for lo in range(2,bound+1,block):
        hi=min(lo+block,bound+1);s=bytearray(b'\1')*(hi-lo)
        for p in base:
            start=max(p*p,((lo+p-1)//p)*p)
            if start<hi:s[start-lo::p]=b'\0'*((hi-1-start)//p+1)
        for i,v in enumerate(s):
            if v:yield lo+i
def classify(s,m):return 'initial' if m is None else ('rupture' if s>m+1 else 'sequential' if s==m+1 else 'nonrecord')
def skipped(s,m):return list(range(m+1,s)) if classify(s,m)=='rupture' else []
def scan(bound):
    prev=None;m=None;records=[];first={};count=0
    for q in primes(bound):
        count+=1
        if prev is not None and prev!=2:
            s=(q-prev)//2;first.setdefault(s,(prev,q,count-1))
            if m is None or s>m:
                records.append(dict(p=prev,q=q,step=s,previous=m,index=count-1,kind=classify(s,m)));m=s
        prev=q
    return records,first,count,prev
def write(name,rows):
    if not rows:return
    with (ROOT/'output'/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
    start=time.perf_counter();(ROOT/'output').mkdir(exist_ok=True)
    low=[int(x.split()[1]) for x in (ROOT/'sources/oeis_lower.txt').read_text().splitlines()]
    high=[int(x.split()[1]) for x in (ROOT/'sources/oeis_upper.txt').read_text().splitlines()]
    data=list(csv.DictReader((ROOT/'sources/gap_snapshot.csv').open()))
    first={int(r['gap'])//2:(int(r['p']),int(r['p'])+int(r['gap'])) for r in data if int(r['gap'])%2==0 and r['first_status']=='F' and int(r['p'])+int(r['gap'])<=B}
    allfirst={int(r['gap']):int(r['p']) for r in data}
    records=[];events=[];m=None
    for k,(p,q) in enumerate(zip(low,high),1):
        g=q-p
        assert allfirst[g]==p
        assert prime(p) and prime(q) and all(not prime(x) for x in range(p+1,q))
        if p==2:continue
        s=g//2;kind=classify(s,m)
        r=dict(record=k,p=p,q=q,gap=g,step=s,previous=m,kind=kind)
        records.append(r)
        if kind=='rupture':
            events.append(dict(event=len(events)+1,record=k,p=p,q=q,gap=g,step=s,previous=m,jump=s-m,skipped_start=m+1,skipped_end=s-1,skipped_count=s-m-1,status='confirmed' if q<=B else 'outside_boundary_candidate'))
        m=s
    local,lf,count,last=scan(100000000)
    assert [(r['p'],r['q']) for r in local]==[(r['p'],r['q']) for r in records if r['q']<=100000000]
    for t,(p,q,i) in lf.items():assert first[t]==(p,q)
    order=[int(x.split()[1]) for x in (ROOT/'sources/oeis_order.txt').read_text().splitlines()]
    ordered=[t for t in sorted(first,key=lambda t:first[t][0])]
    assert ordered[:len(order)]==order
    for line in (ROOT/'sources/oeis_first.txt').read_text().splitlines():
        t,p=map(int,line.split())
        if t:assert first[t][0]==p
    localidx={r['p']:r['index'] for r in local}
    recoveries=[]
    for e in events:
        rr=[]
        for t in range(e['skipped_start'],e['skipped_end']+1):
            pair=first.get(t) if e['q']<=B else None
            if pair:
                p,q=pair;assert p>e['p'] and prime(p) and prime(q) and all(not prime(x) for x in range(p+1,q))
                d=lf[t][2]-localidx[e['p']] if t in lf and e['p'] in localidx else ''
                r=dict(event=e['event'],step=t,gap=2*t,p=p,q=q,status='recovered',order=0,gap_count_distance=d,prime_index_distance=d,numerical_distance=p-e['p'],ratio=p/e['p'],log_ratio=math.log(p/e['p']),later_records=sum(e['q']<z['q']<=q for z in records),later_ruptures=sum(e['q']<z['q']<=q for z in events))
            else:r=dict(event=e['event'],step=t,gap=2*t,p='',q='',status='right_censored' if e['q']<=B else 'outside_detection_boundary',order='',gap_count_distance='',prime_index_distance='',numerical_distance='',ratio='',log_ratio='',later_records='',later_ruptures='')
            rr.append(r)
        done=sorted([r for r in rr if r['status']=='recovered'],key=lambda r:r['p'])
        for i,r in enumerate(done,1):r['order']=i
        complete=len(done)==len(rr)
        e.update(recovered_count=len(done),recovery_status='complete' if complete else 'right_censored' if e['q']<=B else 'outside_detection_boundary',complete_p=done[-1]['p'] if complete else '',complete_q=done[-1]['q'] if complete else '',last_step=done[-1]['step'] if complete else '',delay_ruptures=done[-1]['later_ruptures'] if complete else '',recovery_order=';'.join(str(r['step']) for r in done))
        recoveries+=rr
    write('ruptures.csv',events);write('recoveries.csv',recoveries);write('records.csv',records)
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024 if resource else None
    summary=dict(boundary=B,direct_boundary=100000000,direct_prime_count=count,direct_last_prime=last,listed_events=len(events),confirmed=sum(e['q']<=B for e in events),complete=sum(e['recovery_status']=='complete' for e in events),first13_max=max(e['delay_ruptures'] for e in events[:13]),max_delay=max(e['delay_ruptures'] for e in events if e['recovery_status']=='complete'),max_events=[e['event'] for e in events if e['delay_ruptures']==8],seconds=time.perf_counter()-start,peak_MiB=peak,python=platform.python_version(),platform=platform.platform(),cpu=platform.processor())
    (ROOT/'output/summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
if __name__=='__main__':main()

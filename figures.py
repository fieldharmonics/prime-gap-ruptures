"""Publication figures: PDF and SVG vectors, 300 dpi PNG previews."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import csv,math
from pathlib import Path
from analysis import primes
OUT=Path('output/figures');OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'svg.fonttype':'none'})
E=list(csv.DictReader(open('output/ruptures.csv')));R=list(csv.DictReader(open('output/recoveries.csv')))
def save(fig,name):
 fig.tight_layout()
 for ext in ('pdf','svg','png'):fig.savefig(OUT/(name+'.'+ext),dpi=300,bbox_inches='tight')
 plt.close(fig)
def tree(ps,name,title,full=False):
 fig,ax=plt.subplots(figsize=(9,7 if full else 3.6));prev=1 if full else ps[0]
 for i,p in enumerate(ps):
  h=(p-1)//2;old=(prev-1)//2
  for x in range(-h,h+1):
   new=abs(x)>old
   ax.add_patch(Rectangle((x-.48,i-.35),.96,.7,facecolor='black' if x==0 else '#386779' if new else '#ddd',edgecolor='#777',lw=.15,hatch='///' if p==127 and new else None))
  ax.text(67,i,str(p),va='center',fontsize=9)
  if i>0 and p>=3 and prev>=3:ax.text(78,i,str((p-prev)//2),va='center',fontsize=9,fontweight='bold' if p==127 else 'normal')
  prev=p
 ax.text(67,-1.2,'Prime',fontsize=9);ax.text(76,-1.2,'Step',fontsize=9)
 ax.set_xlim(-68,86);ax.set_ylim(len(ps),-2);ax.axis('off');ax.set_title(title,pad=15)
 if full:fig.text(.13,.01,'1 is a construction seed, not a prime.  The exceptional prime 2 is shown separately.',fontsize=9)
 save(fig,name)
tree([1]+list(primes(127))[1:],'01_prime_step_tree','The prime-step tree: centred rows through 127',True)
tree([p for p in primes(127) if p>=89],'02_enlargement','Every prime row from 89 to 127')
fig,ax=plt.subplots(figsize=(7,2.7));ax.plot(range(5),[1,2,3,4,7],'ko-');ax.set_xticks(range(5),['3 to 5','7 to 11','23 to 29','89 to 97','113 to 127']);ax.set_yticks(range(1,8));ax.set_ylabel('Record step');ax.axhspan(4.5,6.5,color='#ddd');ax.text(2.0,5.5,'Skipped: 5 and 6');save(fig,'03_record_progression')
fig,ax=plt.subplots(figsize=(7,2.6));ax.axis('off')
for i,(label,v) in enumerate([('Previous record',4),('Skipped level',5),('Skipped level',6),('New record',7)]):
 ax.text(i,.8,str(v),ha='center',fontsize=30,fontweight='bold');ax.text(i,.4,label,ha='center',fontsize=10)
ax.text(1.5,0,'113 to 127: gap 14   |   step 7   |   jump 3   |   two skipped levels',ha='center');ax.set_xlim(-.6,3.6);ax.set_ylim(-.3,1.2);save(fig,'04_first_rupture')
fig,ax=plt.subplots(figsize=(9,2));ax.plot([113,127],[0,0],'k-',lw=1)
for n in range(113,128):ax.scatter(n,0,c='black' if n in (113,127) else 'white',edgecolor='black',s=70);ax.text(n,-.12,str(n),ha='center',fontsize=9)
ax.text(120,.25,'13 interior integers, all composite',ha='center');ax.set_ylim(-.3,.45);ax.axis('off');save(fig,'05_rupture_desert')
def factors(n):
 f=[];d=2
 while d*d<=n:
  k=0
  while n%d==0:n//=d;k+=1
  if k:f.append(str(d)+(f'^{k}' if k>1 else ''))
  d+=1
 if n>1:f.append(str(n))
 return r'\times'.join(f)
fig,ax=plt.subplots(figsize=(7,3.6));ax.axis('off')
for i,n in enumerate(range(114,127)):
 col=i//7;row=i%7;ax.text(col*.53,1-row*.135,f'${n} = {factors(n)}$',fontsize=12,transform=ax.transAxes)
save(fig,'06_factor_oasis')
fig,ax=plt.subplots(figsize=(8,3));ax.plot([math.log10(int(e['p'])) for e in E[:68]],range(1,69),'k.',ms=5);ax.plot(math.log10(int(E[68]['p'])),69,marker='D',mfc='white',mec='black');ax.axvline(20,color='grey',ls='--');ax.set(xlabel='log10(lower prime)',ylabel='Rupture number',title='68 confirmed events and one outside-boundary candidate');save(fig,'07_rupture_timeline')
fig,ax=plt.subplots(figsize=(8,5.8))
for e in E[:13]:
 i=int(e['event']);rr=[r for r in R if r['event']==str(i)];xs=[math.log10(int(r['q'])/int(e['q'])) for r in rr]
 ax.plot([0,max(xs)],[i,i],color='#aaa');ax.scatter(xs,[i]*len(xs),c='#386779',s=23);ax.scatter(max(xs),i,marker='s',c='black',s=24)
ax.set_yticks(range(1,14));ax.invert_yaxis();ax.set(xlabel='log10(recovery upper prime / rupture upper prime)',ylabel='Rupture number',title='Individual recoveries; black square marks complete recovery');save(fig,'08_first13_recovery')
fig,ax=plt.subplots(figsize=(8,3.5));ax.scatter(range(1,67),[int(e['delay_ruptures']) for e in E[:66]],color='black',s=20)
ax.scatter([67,68],[1,0],marker='^',facecolors='none',edgecolors='black',s=55,label='Censored: elapsed count at boundary')
ax.set(xlabel='Rupture number',ylabel='Subsequent ruptures',title='Complete-recovery delay: 66 completed, two censored');ax.set_yticks(range(9));ax.legend(fontsize=8);save(fig,'09_recovery_summary')
fig,axes=plt.subplots(2,1,figsize=(8,5),sharex=True)
for ax,key,label in zip(axes,['jump','skipped_count'],['Record-step jump J','Skipped levels |K|']):
 ax.scatter([math.log10(int(e['p'])) for e in E[:68]],[int(e[key]) for e in E[:68]],s=17,color='black');ax.scatter(math.log10(int(E[-1]['p'])),int(E[-1][key]),marker='D',facecolors='none',edgecolors='black');ax.axvline(20,ls='--',color='grey');ax.set_ylabel(label)
axes[-1].set_xlabel('log10(lower prime)');save(fig,'10_jump_sizes')

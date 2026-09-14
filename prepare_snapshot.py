"""Recreate compact CSV from supplied full SQL snapshot, without network access."""
import sqlite3,csv
from pathlib import Path
db=sqlite3.connect(':memory:')
db.executescript(Path('sources/allgaps.sql').read_text())
rows=[(g,int(p),f,c) for g,p,f,c in db.execute('select gapsize,startprime,isfirst,gapcert from gaps where gapsize<=1854') if str(p).isdigit()]
with open('sources/gap_snapshot.csv','w',newline='') as f:
 w=csv.writer(f);w.writerow(['gap','p','first_status','certificate']);w.writerows(rows)
print(len(rows),'source rows extracted')

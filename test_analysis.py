import unittest,csv
from unittest.mock import Mock
from analysis import *
class AuditTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.rec,cls.first,_,_=scan(1000)
  with (ROOT/'output/ruptures.csv').open() as f:cls.e=list(csv.DictReader(f))
  with (ROOT/'output/recoveries.csv').open() as f:cls.r=list(csv.DictReader(f))
 def test_01_primes(self):self.assertEqual(list(primes(31)),[2,3,5,7,11,13,17,19,23,29,31])
 def test_02_gap(self):self.assertEqual(127-113,14)
 def test_03_step(self):self.assertEqual((127-113)//2,7)
 def test_04_exception(self):self.assertEqual(self.rec[0]['p'],3)
 def test_05_record(self):self.assertEqual([r['step'] for r in self.rec[:5]],[1,2,3,4,7])
 def test_06_sequential(self):self.assertEqual(classify(2,1),'sequential')
 def test_07_rupture(self):self.assertEqual(classify(7,4),'rupture')
 def test_08_implies_record(self):
  for m in range(1,100):
   for s in range(1,100):
    if classify(s,m)=='rupture':self.assertGreater(s,m)
 def test_09_skipped(self):self.assertEqual(skipped(7,4),[5,6])
 def test_10_first_recoveries(self):self.assertEqual(self.first[5][:2],(139,149));self.assertEqual(self.first[6][:2],(199,211))
 def test_11_complete(self):self.assertEqual(self.e[0]['complete_q'],'211')
 def test_12_censoring(self):self.assertEqual([e['event'] for e in self.e if e['recovery_status']=='right_censored'],['67','68'])
 def test_13_progression(self):self.assertEqual([r['p'] for r in self.rec[:5]],[3,7,23,89,113])
 def test_14_seven_eleven(self):self.assertEqual(self.rec[1]['kind'],'sequential')
 def test_15_first_rupture(self):self.assertEqual((self.e[0]['p'],self.e[0]['q']),('113','127'))
 def test_16_gap14(self):self.assertEqual(self.e[0]['gap'],'14')
 def test_17_step7(self):self.assertEqual(self.e[0]['step'],'7')
 def test_18_previous4(self):self.assertEqual(self.e[0]['previous'],'4')
 def test_19_jump3(self):self.assertEqual(self.e[0]['jump'],'3')
 def test_20_set56(self):self.assertEqual((self.e[0]['skipped_start'],self.e[0]['skipped_end']),('5','6'))
 def test_21_composites(self):self.assertTrue(all(not prime(n) for n in range(114,127)))
 def test_22_original_table(self):
  expected=[(113,127,7,4),(523,541,9,7),(1327,1361,17,11),(15683,15727,22,18),(19609,19661,26,22),(31397,31469,36,26),(155921,156007,43,36),(360653,360749,48,43),(370261,370373,56,48),(1349533,1349651,59,57),(1357201,1357333,66,59),(2010733,2010881,74,66),(4652353,4652507,77,74)]
  self.assertEqual([tuple(int(e[k]) for k in ['p','q','step','previous']) for e in self.e[:13]],expected)
  self.assertEqual(sum(int(e['q'])<=5000000 for e in self.e),13)
 def test_23_expansion(self):
  self.assertEqual(len(self.e),69);self.assertEqual(sum(e['status']=='confirmed' for e in self.e),68)
  self.assertEqual(sum(e['recovery_status']=='complete' for e in self.e),66)
  self.assertTrue(all(e['recovery_status']=='complete' for e in self.e[:59]))
  self.assertEqual([int(e['event']) for e in self.e if e['delay_ruptures']=='8'],[27,59])
  self.assertEqual(max(int(e['delay_ruptures']) for e in self.e[:13]),3)
 def test_24_original_recovery(self):
  self.assertEqual([int(e['complete_p']) for e in self.e[:13]],[199,1831,5591,30593,81463,173359,542603,1100977,2238823,5845193,6752623,11981443,13626257])
 def test_25_boundary(self):
  self.assertTrue(all(int(r['q'])<=B for r in self.r if r['status']=='recovered'))
  self.assertEqual(self.e[-1]['status'],'outside_boundary_candidate')
 def test_26_initialisation(self):self.assertEqual(classify(1,None),'initial')
 def test_27_nonrecord(self):self.assertEqual(classify(5,7),'nonrecord');self.assertEqual(skipped(5,7),[])
 def test_28_primality(self):
  self.assertTrue(prime(101412319996363309069));self.assertFalse(prime(3215031751))
 def test_29_segment_edges(self):self.assertEqual(list(primes(1000,17)),list(primes(1000,1000)))
 def test_30_finite_censor(self):
  _,f,_,_=scan(149);self.assertIn(5,f);self.assertNotIn(6,f)
 def test_31_source_hashes(self):validate_sources()
 def test_32_first_occurrence_coverage(self):self.assertEqual(len(read_indexed(ROOT/'sources/oeis_first.txt',0,722)),722)
 def test_33_reject_bad_indices(self):
  for contents in ('0 1\n2 3\n','0 1\n0 3\n','0 1\n'):
   path=Mock();path.name='synthetic';path.read_text.return_value=contents
   with self.assertRaises(ValueError):read_indexed(path,0,2)
 def test_34_data_driven_maximum(self):
  events=[dict(event=1,recovery_status='complete',delay_ruptures=2),dict(event=2,recovery_status='complete',delay_ruptures=5),dict(event=3,recovery_status='right_censored',delay_ruptures='')]
  self.assertEqual(delay_maximum(events),(5,[2]));self.assertEqual(delay_maximum([]),(None,[]))
 def test_35_memory_units(self):
  self.assertEqual(peak_mib(1024,'Linux'),1);self.assertEqual(peak_mib(1048576,'Darwin'),1);self.assertIsNone(peak_mib(None,'Windows'))
 def test_36_summary_maximum(self):
  summary=json.loads((ROOT/'output/summary.json').read_text())
  maximum=max(int(e['delay_ruptures']) for e in self.e if e['recovery_status']=='complete')
  self.assertEqual(summary['max_delay'],maximum)
  self.assertEqual(summary['max_events'],[int(e['event']) for e in self.e if e['delay_ruptures']==str(maximum)])
if __name__=='__main__':unittest.main(verbosity=2)

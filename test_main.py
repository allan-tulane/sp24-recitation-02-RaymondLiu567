from main import simple_work_calc, work_calc, span_calc, compare_span, compare_work
from main import print_results

def test_simple_work():
  assert simple_work_calc(1, 2, 2) == 1
  assert simple_work_calc(2, 2, 2) == 4
  assert simple_work_calc(4, 2, 2) == 10


def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 19 
  assert work_calc(20, 1, 2, lambda n: n*n) == 400  
  assert work_calc(30, 3, 2, lambda n: n) == 435 



def test_compare_span():
  def span_fn1(n):
      return span_calc(n, 2, 2, lambda n: 1)

  def span_fn2(n):
      return span_calc(n, 2, 2, lambda n: n) 

  res = compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100])
  print_results(res)

	
def test_compare_work():
  def work_fn1(n):
      return work_calc(n, 2, 2, lambda n: n)
  def work_fn2(n):
      return work_calc(n, 2, 2, lambda n: n**2)
  res = compare_work(work_fn1, work_fn2, sizes=[10, 20])
  print_results(res)


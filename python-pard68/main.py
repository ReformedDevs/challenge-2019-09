from timeit import default_timer as timer
from collections import deque

def is_prime(n, t=5):
	'''
	miller-rabin test
	default to five tests
	'''

	from random import randint
	if n < 2:
		return False 
	for prime in [2,3,5,7,11,13,17,19,23,29]:
		if n % prime == 0:
			return n == prime
	s, d = 0, n-1
	while d % 2 == 0:
		s, d = int(s+1), int(d/2)
	for i in range(t):
		x = pow(randint(2, n-1), d, n)
		if x == 1 or x == n-1:
			continue
		for r in range(1, s):
			x = (x * x) % n
			if x == 1:
				return False
			if x == n-1:
				break
			else:
				return False
		return True

def fib(n):
	seq = deque()
	seq.extendleft([0,1])
	prv = 1
	cur = 1
	nxt = 0
	while cur < n:
		nxt = cur + prv
		prv = cur
		seq.appendleft(cur)
		cur = nxt
	return seq

def solution(limit, mask):
	start = timer()
	seq = [x for x in fib(limit) if is_prime(x)]
	for n in seq:
		r = n*n
		# if mask(r, mask_for):
		if r & 0xf == 0x9:
			end = timer()
			time = end - start
			print(f"pard68, Python 3, {n}, {time*1000}, y33t")
			break

if __name__ == "__main__":
	limit = 9000000000000000000
	mask_for = 0x9
	solution(limit, mask_for)

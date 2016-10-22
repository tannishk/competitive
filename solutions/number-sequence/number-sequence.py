import sys

info = sys.argv

def recurs(num, ognum, passed_middle):
	if num > ognum:
		print ''
		return
	elif num > 0 and not passed_middle:
		sys.stdout.write('%d  ' % num)
		if (num - 5) <= 0:
			passed_middle = True
		recurs(num - 5, ognum, passed_middle)
	else:
		sys.stdout.write('%d  ' % num)
		recurs(num + 5, ognum, passed_middle)

for num in info[2:]:
	recurs(int(num), int(num), False)

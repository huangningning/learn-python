import time
VERIFYMATRIX = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
VERIFYCODE = '10X98765432'


def IDverify(ID):
	if type(ID) != str:
		return False
	if len(ID) != 18:
		return False
	if 1900< int (ID[6:10]) < 2100:
		pass
	else:
		return False
	if ID[-1].isdigit() or ID[-1] =='X':
		pass
	try:
		time.strptime(ID[6:14], '%Y%m%d')
	except:
		return False
	data = [VERIFYMATRIX[i]*int(ID[i]) for i in range(17)]
	verify_code = sum(data) %11
	verify_code =VERIFYCODE[verify_code]
	if verify_code != ID[-1]:
		return False
	else:
		return True
id = raw_input("your ID:")


if IDverify(id):
		print 'Ture'
else:
		print 'False'
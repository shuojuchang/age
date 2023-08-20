driving = input('有沒有開過車?')
if driving != '有' and driving != '沒有':
    print('請輸入: 有 / 沒有')
    raise SystemExit

age = input('請輸入年齡: ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('恭喜通過測驗 !')
	else:
		print('你怎麼可以開車?')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了,怎不去考?')
	else:
		print('加油,再等幾年你就可以去考了')


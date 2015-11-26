# -*- coding: utf-8 -*-

#import path
# Sentence 1 (Team Name + Score + Result)
# Team Name
TeamNameS = ['넥센이', '두산이', 'NC가', '한화가', '삼성이', 'LG가', 'SK가', '롯데가', 'KIA가', 'KT가']
TeamNameO = ['넥센을', '두산을', 'NC를', '한화를', '삼성을', 'LG를', 'SK를', '롯데를', 'KIA를', 'KT를']

# Score
Score = ['으로', '로', '로', '으로', '로', '로', '으로', '로', '로', '로']

# Result
Sentence1_Result = ['승리했습니다','신승했습니다','대승을 거두었습니다','압승을 거두었습니다']
'''
A_pitcher_inning = 7
A_pitcher_k = 13
A_pitcher_lost = 0
A_pitcher_name = "윤석민"
A_name = "기아"
A_score = 8
A_bullpen_inning = 2
A_bullpen_lost = 3

B_name = "한화"
B_score = 3
B_pitcher_name = "류현진"
B_pitcher_lost = 2
B_pitcher_inning = 7
B_pitcher_k = 11
B_bullpen_inning = 2
B_bullpen_lost = 6

B_hitter_tasun = 4
B_hitter_name = "김태균"
B_hitter_tasu = 5
B_hitter_anta = 2
B_hitter_tajum = 2
B_hitter_homerun = 1
'''

#article = open("sample.txt", "r")
article = open("20150319SKKT0.txt", "r")
txtfile = open("output.txt", "w")
textline = article.readline()
line_num = 1
Apitcherflag = False
Bpitcherflag = False
A_name=''
A_pitcher_inning = 0
A_pitcher_lost = 0
A_pitcher_name = ''
A_pitcher_k = 0
A_bullpen_inning = 0
A_bullpen_lost = 0
B_name =''
B_pitcher_inning = 0
B_pitcher_lost = 0
B_pitcher_name = ''
B_pitcher_k = 0
B_bullpen_inning = 0
B_bullpen_lost = 0

A_attack = []
A_attack_list = []

B_best_attack_num = ''
B_best_attack_name = ''
B_best_attack_pos = ''
B_best_attack_tan = 0
B_best_attack_anta = 0
B_best_attack_ta = 0
B_best_attack_home = 0




def sentence1():	
	
	Sentence1_str = ''
	ace = 0
	if A_pitcher_inning >= 7 and A_pitcher_lost <= 2:
		ace = 1
#		print A_pitcher_name+'을 앞세운 '
		Sentence1_str +=  A_pitcher_name+'을 앞세운 '


	for i in range(0,10,1):
#		print A_name
		if A_name in TeamNameS[i]:
#			print TeamNameS[i]+' '
			Sentence1_str += TeamNameS[i]+' '
			break

	if ace == 1:	
#		print B_pitcher_name+'의 '
		Sentence1_str += B_pitcher_name+'의 '
	for i in range(0,10,1):
		#print B_name
		if B_name in TeamNameO[i]:
#			print TeamNameO[i]+' 상대로 '
			Sentence1_str += TeamNameO[i]+' 상대로 '
			break
	result_index = 0
	if int(A_score)-int(B_score) >= 8:
		if int(B_score) <= 1:
			result_index = 3
		else:
			result_index = 2
	elif int(A_score)-int(B_score) >= 3:
		result_index = 1
	else:
		result_index = 0
	
	#print A_score+'대 '+B_score+Score[int(B_score)%10]+' '+Sentence1_Result[result_index]+'.'
	Sentence1_str += A_score+'대 '+B_score+Score[int(B_score)%10]+' '+Sentence1_Result[result_index]+'.'
#	print Sentence1_str
	txtfile.write(Sentence1_str)
def sentence2():	
	Sentence2_str = ''
	#print '선발투수 '+A_pitcher_name+'은(는) '+str(A_pitcher_inning)+'이닝 '+str(A_pitcher_k)+'K '+str(A_pitcher_lost)+'실점' 
	Sentence2_str +='선발투수 '+A_pitcher_name+'은(는) '+str(A_pitcher_inning)+'이닝 '+str(A_pitcher_k)+'K '+str(A_pitcher_lost)+'실점'
	ace = 0
	if A_pitcher_inning == 9:
		ace = 1
		if A_pitcher_lost == 0:
			Sentence2_str +='의 괴력투로 완봉승을 거두었습니다.'
		else:
			Sentence2_str +='의 괴력투로 완투승을 거두었습니다.'
	elif A_pitcher_lost > A_pitcher_inning+2 :
		#print '으로 무너졌지만 '
		Sentence2_str +='으로 무너졌지만 '
	elif A_pitcher_lost >= A_pitcher_inning-2:
		#print '으로 버텼고 '
		Sentence2_str +='으로 버텼고 '
	elif A_pitcher_inning <= 6:
		#print '으로 마운드를 지켜냈고 '
		Sentence2_str +='으로 마운드를 지켜냈고 '
	else:
		if A_pitcher_lost <= 1 :
			if A_pitcher_inning+A_pitcher_k >= 17:
			#	print '으로 '+B_name+'의 타선을 압도했고 '
				Sentence2_str += '으로 '+B_name+'의 타선을 압도했고 '	
			else:
			#	print '의 훌륭한 투구로 '+B_name+'의 타선을 침묵시켰고 '
				Sentence2_str +='의 훌륭한 투구로 '+B_name+'의 타선을 침묵시켰고 '
		else:
				#print '으로 호투했고 '	
				Sentence2_str +='으로 호투했고 '	

	if ace == 0:
		if A_bullpen_lost == 0:
		#	print '불펜이 나머지 '+str(A_bullpen_inning)+'이닝 무실점으로 막아냈습니다.'
			Sentence2_str += '불펜이 나머지 '+str(A_bullpen_inning)+'이닝 무실점으로 막아냈습니다.'
		elif A_bullpen_inning/A_bullpen_lost >= 2 :
			#print '불펜이 나머지 '+str(A_bullpen_inning)+'이닝 '+str(A_bullpen_lost)+'실점으로 지켜냈습니다.'
			Sentence2_str +='불펜이 나머지 '+str(A_bullpen_inning)+'이닝 '+str(A_bullpen_lost)+'실점으로 지켜냈습니다.'
		else:
			#print '불펜이 '+str(A_bullpen_inning)+'이닝 '+str(A_bullpen_lost)+'실점으로 무너졌지만, 타선에 힘입어 승리했습니다.'
			Sentence2_str +='불펜이 '+str(A_bullpen_inning)+'이닝 '+str(A_bullpen_lost)+'실점으로 무너졌지만, 타선에 힘입어 승리했습니다.'
#	print Sentence2_str	
	txtfile.write(Sentence2_str)
def sentence3():
	#이긴팀 타자정보 추가	
	Sentence3_str = ''
	total_tasu=0
	total_anta=0
	total_tayool=0
	best_anta=0
	best_name=""
	best_tasun=0
	best_pos=""
	best_tasu=0
	best_tajum=0
	best_homerun=0


	for eleme in A_attack_list:
		total_tasu += int(eleme[3])
		total_anta += int(eleme[4])
		if best_tajum < int(eleme[5]):
			best_name = eleme[0]
			best_tasun = int(eleme[1])
			best_pos = eleme[2]
			best_tasu = int(eleme[3])
			best_anta = int(eleme[4])
			best_tajum = int(eleme[5])
			best_homerun = int(eleme[6])		
	total_tayool = float(total_anta)/float(total_tasu)
#	print total_tasu
#	print total_anta
#	print total_tayool
	if best_tasun >= 3 and best_tasun<= 5:
		#print '중심 타자 '
		Sentence3_str += '중심 타자 '
	else:
		#print best_tasun+'번 타자 '
		Sentence3_str +=str(best_tasun)+'번 타자 '
	#print best_name+'은(는) ' + str(best_tasu)+'타수 ' 
	Sentence3_str +=best_name+'은(는) ' + str(best_tasu)+'타수 '
	if best_tajum <= 2:
		#print str(best_anta)+'안타 '
		Sentence3_str +=str(best_anta)+'안타 '
		if best_homerun >= 1:
	#		print str(best_homerun)+'홈런 '
			Sentence3_str += str(best_homerun)+'홈런 '
		#print str(best_tajum)+'타점으로 선전했고 '
		Sentence3_str +=str(best_tajum)+'타점으로 선전했고 '
	else :
		#print str(best_anta)+'안타 '
		Sentence3_str +=str(best_anta)+'안타 '
		if best_homerun >= 1:
#			print str(best_homerun)+'홈런 '
			Sentence3_str +=str(best_homerun)+'홈런 '
#		print str(best_tajum)+'타점으로 폭발하여 '
		Sentence3_str +=str(best_tajum)+'타점으로 폭발하여 '
	if total_tayool < 0.2:
#		print '부진했단 타선을 이끌고 팀을 승리로 이끌었습니다.'
		Sentence3_str +='부진했단 타선을 이끌고 팀을 승리로 이끌었습니다.'
	elif total_tayool > 0.26:
#		print '활발했던 타선과 함께 팀에게 승리를 안겼습니다.'
		Sentence3_str +='활발했던 타선과 함께 팀에게 승리를 안겼습니다.'
	else:
#		print '타선을 이끌고 팀을 승리로 이끌었습니다.'
		Sentence3_str +='타선을 이끌고 팀을 승리로 이끌었습니다.'
#	print Sentence3_str	
	txtfile.write(Sentence3_str)
#이름, 타순, 포지션, 타수, 안타, 타점 홈런
#0		1		2		3	4	  5	6
def sentence4():
	Sentence4_str = ''
#	print B_name+'의 선발투수 '+B_pitcher_name+'은(는) '+ str(B_pitcher_inning)+'이닝 '+str(B_pitcher_k)+'K '+str(B_pitcher_lost)+'실점'
	Sentence4_str +=B_name+'의 선발투수 '+B_pitcher_name+'은(는) '+ str(B_pitcher_inning)+'이닝 '+str(B_pitcher_k)+'K '+str(B_pitcher_lost)+'실점'
	if B_pitcher_inning == 9:
#		print '의 위력투를 펼쳤지만, 팀 타선의 침묵으로 완투패를 당했습니다.'
		Sentence4_str +='의 위력투를 펼쳤지만, 팀 타선의 침묵으로 완투패를 당했습니다.'
	elif B_pitcher_lost > B_pitcher_inning+2 :
#		print '으로 무너져 팀의 패배를 막지 못했습니다.'
		Sentence4_str +='으로 무너져 팀의 패배를 막지 못했습니다.'
	elif B_pitcher_lost >= B_pitcher_inning-2:
#		print '으로 버텼지만, '
		Sentence4_str +='으로 버텼지만, '
#		loopbysentence4_pitcher(Sentence4_str)
		if int(B_score) <= 5:		
			'''5점은 리그 평균득점'''
#			print '타선의 부진으로, 팀의 패배를 허용할 수 밖에 없었습니다.'
			Sentence4_str +='타선의 부진으로, 팀의 패배를 허용할 수 밖에 없었습니다.'
		elif int(A_score) - int(B_score) >= int(A_score) - B_pitcher_lost + 3:
#			print str(B_bullpen_inning)+'이닝 '+str(B_bullpen_lost)+'실점의 불펜의 붕괴를 이겨내지 못하고, 패배를 허용했습니다.'
			Sentence4_str +=str(B_bullpen_inning)+'이닝 '+str(B_bullpen_lost)+'실점의 불펜의 붕괴를 이겨내지 못하고, 패배를 허용했습니다.'
		else:
#			print '팀의 전반적인 투타밸런스가 좋지않아, 패배를 허용했습니다.'
			Sentence4_str +='팀의 전반적인 투타밸런스가 좋지않아, 패배를 허용했습니다.'
	elif B_pitcher_inning <= 6:
#		print '으로 마운드를 지켜냈지만, '
		Sentence4_str +='으로 마운드를 지켜냈지만, '
		if int(B_score) <= 5:		
			'''5점은 리그 평균득점'''
#			print '타선의 부진으로, 팀의 패배를 허용할 수 밖에 없었습니다.'
			Sentence4_str +='타선의 부진으로, 팀의 패배를 허용할 수 밖에 없었습니다.'
		elif int(A_score) - int(B_score) >= int(A_score) - B_pitcher_lost + 3:
#			print str(B_bullpen_inning)+'이닝 '+str(B_bullpen_lost)+'실점의 불펜의 붕괴를 이겨내지 못하고, 패배를 허용했습니다.'
			Sentence4_str +=str(B_bullpen_inning)+'이닝 '+str(B_bullpen_lost)+'실점의 불펜의 붕괴를 이겨내지 못하고, 패배를 허용했습니다.'
		else:
#			print '팀의 전반적인 투타밸런스가 좋지않아, 패배를 허용했습니다.'
			Sentence4_str +='팀의 전반적인 투타밸런스가 좋지않아, 패배를 허용했습니다.'
		#loopbysentence4_pitcher(Sentence4_str)
	else:
#		print '의 훌륭한 투구를 펼쳤지만, ' 	
		Sentence4_str +='의 훌륭한 투구를 펼쳤지만, '
		if int(B_score) <= 5:		
			'''5점은 리그 평균득점'''
#			print '타선의 부진으로, 팀의 패배를 허용할 수 밖에 없었습니다.'
			Sentence4_str +='타선의 부진으로, 팀의 패배를 허용할 수 밖에 없었습니다.'
		elif int(A_score) - int(B_score) >= int(A_score) - B_pitcher_lost + 3:
#			print str(B_bullpen_inning)+'이닝 '+str(B_bullpen_lost)+'실점의 불펜의 붕괴를 이겨내지 못하고, 패배를 허용했습니다.'
			Sentence4_str +=str(B_bullpen_inning)+'이닝 '+str(B_bullpen_lost)+'실점의 불펜의 붕괴를 이겨내지 못하고, 패배를 허용했습니다.'
		else:
#			print '팀의 전반적인 투타밸런스가 좋지않아, 패배를 허용했습니다.'
			Sentence4_str +='팀의 전반적인 투타밸런스가 좋지않아, 패배를 허용했습니다.'
#		loopbysentence4_pitcher(Sentence4_str)
	
#	print B_name+'의 '
	Sentence4_str +=B_name+'의 '
	if int(B_best_attack_num) >= 3 and int(B_best_attack_num)<= 5:
#		print '중심 타자 '
		Sentence4_str +='중심 타자 '
	else:
#		print B_best_attack_tan+'번 타자 '
		Sentence4_str +=B_best_attack_tan+'번 타자 '
#	print B_best_attack_name+'은(는) ' + str(B_best_attack_tan)+'타수 '
	Sentence4_str +=B_best_attack_name+'은(는) ' + str(B_best_attack_tan)+'타수 '
	if B_best_attack_anta <= 1:
#		print str(B_best_attack_anta)+'안타의 부진으로 팀을 위기에서 구해내지 못했습니다.'
		Sentence4_str +=str(B_best_attack_anta)+'안타의 부진으로 팀을 위기에서 구해내지 못했습니다.'
	else:
		if B_best_attack_ta <= 2:
#			print str(B_best_attack_anta)+'안타 '
			Sentence4_str +=str(B_best_attack_anta)+'안타 '
			if int(B_best_attack_home) >= 1:
#				print str(B_best_attack_home)+'홈런 '
				Sentence4_str +=str(B_best_attack_home)+'홈런 '
#			print str(B_best_attack_ta)+'타점으로 선전했지만, 팀 패배로 빛이 바랬습니다.'
			Sentence4_str +=str(B_best_attack_ta)+'타점으로 선전했지만, 팀 패배로 빛이 바랬습니다.'
		else :
#			print str(B_best_attack_anta)+'안타 '
			Sentence4_str +=str(B_best_attack_anta)+'안타 '
			if int(B_best_attack_home) >= 1:
#				print str(B_best_attack_home)+'홈런 '
				Sentence4_str +=str(B_best_attack_home)+'홈런 '
#			print str(B_best_attack_ta)+'타점으로 폭발했지만, 팀 패배로 빛이 바랬습니다.'
			Sentence4_str += str(B_best_attack_ta)+'타점으로 폭발했지만, 팀 패배로 빛이 바랬습니다.'
#	print Sentence4_str
	txtfile.write(Sentence4_str)
'''def loopbysentence4_pitcher(Sentence4_str):
	if int(B_score) <= 5:		
#		print '타선의 부진으로, 팀의 패배를 허용할 수 밖에 없었습니다.'
		Sentence4_str +='타선의 부진으로, 팀의 패배를 허용할 수 밖에 없었습니다.'
	elif int(A_score) - int(B_score) >= int(A_score) - B_pitcher_lost + 3:
#		print str(B_bullpen_inning)+'이닝 '+str(B_bullpen_lost)+'실점의 불펜의 붕괴를 이겨내지 못하고, 패배를 허용했습니다.'
		Sentence4_str +=str(B_bullpen_inning)+'이닝 '+str(B_bullpen_lost)+'실점의 불펜의 붕괴를 이겨내지 못하고, 패배를 허용했습니다.'
	else:
#		print '팀의 전반적인 투타밸런스가 좋지않아, 패배를 허용했습니다.'
		Sentence4_str +='팀의 전반적인 투타밸런스가 좋지않아, 패배를 허용했습니다.'
'''
def sentence5():
	Sentence5_str = ''
#	print '지금까지 프로야구 오토봇 Voidness였습니다.'
	Sentence5_str +='지금까지 프로야구 오토봇 Voidness였습니다.'
#	print Sentence5_str	
	txtfile.write(Sentence5_str)
	txtfile.write('\n')

ABflag = False

while textline:
	if line_num == 1:
		if int(textline.split()[4]) > int(textline.split()[5]):
			A_name = textline.split()[1]
			B_name = textline.split()[3]
			A_score = textline.split()[4]
			B_score = textline.split()[5]
		else:
			A_name = textline.split()[3]
			B_name = textline.split()[1]
			A_score = textline.split()[5]
			B_score = textline.split()[4]
			ABflag = True

	if '투구수' in textline and Apitcherflag == False:		
		line_num = line_num + 1
		textline = article.readline()
		if ABflag == True:
			B_pitcher_inning = float(textline.split()[1])
			B_pitcher_lost = int(textline.split()[7])
			B_pitcher_name = textline.split()[0]
			B_pitcher_k = int(textline.split()[6])
		else:
			A_pitcher_inning = float(textline.split()[1])
			A_pitcher_lost = int(textline.split()[7])
			A_pitcher_name = textline.split()[0]
			A_pitcher_k = int(textline.split()[6])

		line_num = line_num + 1
		textline = article.readline()
		while 1:
			if '타순' not in textline:
				if ABflag == True:
					B_bullpen_inning = B_bullpen_inning + float(textline.split()[1])
					temp = B_bullpen_inning*10
					temp = temp%10;
					if temp >= 3 :
						B_bullpen_inning += 1;
						B_bullpen_inning -=0.3;
					B_bullpen_lost = B_bullpen_lost + int(textline.split()[7])
				else:
					A_bullpen_inning = A_bullpen_inning + float(textline.split()[1])
					temp = A_bullpen_inning*10
					temp = temp%10;
					if temp >= 3 :
						A_bullpen_inning += 1;
						A_bullpen_inning -=0.3;
					A_bullpen_lost = A_bullpen_lost + int(textline.split()[7])
				line_num = line_num + 1
				textline = article.readline()
			else:
				break

		line_num = line_num + 1
		textline = article.readline()
		while 1:
			if '이닝' not in textline:
				if ABflag == True:
					if float(textline.split()[6]) > float(B_best_attack_ta):
						B_best_attack_num = textline.split()[0]
						B_best_attack_name = textline.split()[1]
						B_best_attack_pos = textline.split()[2]
						B_best_attack_tan = textline.split()[3]
						B_best_attack_anta = textline.split()[5]
						B_best_attack_ta = textline.split()[6]
						B_best_attack_home = textline.split()[7]
					elif float(textline.split()[6]) == float(B_best_attack_ta):
						if float(textline.split()[6]) == 0:
							pass
						elif float(textline.split()[5])/float(textline.split()[6]) > float(B_best_attack_anta)/float(B_best_attack_anta):
							B_best_attack_num = textline.split()[0]
							B_best_attack_name = textline.split()[1]
							B_best_attack_pos = textline.split()[2]
							B_best_attack_tan = textline.split()[3]
							B_best_attack_anta = textline.split()[5]
							B_best_attack_ta = textline.split()[6]
							B_best_attack_home = textline.split()[7]
				else:
					A_attack.append(textline.split()[1])
					A_attack.append(textline.split()[0])
					A_attack.append(textline.split()[2])
					A_attack.append(textline.split()[3])
					A_attack.append(textline.split()[5])
					A_attack.append(textline.split()[6])
					A_attack.append(textline.split()[7])
					A_attack_list.append(tuple(A_attack))
					A_attack = []
				line_num = line_num + 1
				textline = article.readline()
			else:
				break
		"""
		for eleme in A_attack_list:
			print eleme[0]
		"""
		Apitcherflag = True

	elif Bpitcherflag == False and Apitcherflag == True:
		if ABflag == True:
			A_pitcher_inning = float(textline.split()[1])
			A_pitcher_lost = int(textline.split()[7])
			A_pitcher_name = textline.split()[0]
			A_pitcher_k = int(textline.split()[6])
		else:
			B_pitcher_inning = float(textline.split()[1])
			B_pitcher_lost = int(textline.split()[7])
			B_pitcher_name = textline.split()[0]
			B_pitcher_k = int(textline.split()[6])

		line_num = line_num + 1
		textline = article.readline()
		while 1:
			if '타순' not in textline:
				if ABflag == True:
					A_bullpen_inning = A_bullpen_inning + float(textline.split()[1])
					A_bullpen_lost = A_bullpen_lost + int(textline.split()[7])
					temp = A_bullpen_inning*10
					temp = temp%10;
					if temp >= 3:
						A_bullpen_inning += 1;
						A_bullpen_inning -=0.3;
				else:
					B_bullpen_inning = B_bullpen_inning + float(textline.split()[1])
					B_bullpen_lost = B_bullpen_lost + int(textline.split()[7])
					temp = B_bullpen_inning*10
					temp = temp%10;
					if temp >= 3:
						B_bullpen_inning += 1;
						B_bullpen_inning -=0.3;

				line_num = line_num + 1
				textline = article.readline()
			else:
				break


		line_num = line_num + 1
		textline = article.readline()
		
		while 1:
			if 'LineUp' not in textline:
				if ABflag == True:
					A_attack.append(textline.split()[1])
					A_attack.append(textline.split()[0])
					A_attack.append(textline.split()[2])
					A_attack.append(textline.split()[3])
					A_attack.append(textline.split()[5])
					A_attack.append(textline.split()[6])
					A_attack.append(textline.split()[7])
					A_attack_list.append(tuple(A_attack))
					A_attack = []
				else:
					if float(textline.split()[6]) > float(B_best_attack_ta):
						B_best_attack_num = textline.split()[0]
						B_best_attack_name = textline.split()[1]
						B_best_attack_pos = textline.split()[2]
						B_best_attack_tan = textline.split()[3]
						B_best_attack_anta = textline.split()[5]
						B_best_attack_ta = textline.split()[6]
						B_best_attack_home = textline.split()[7]
					elif float(textline.split()[6]) == float(B_best_attack_ta):
						if textline.split()[6] == 0:
							pass
						elif float(textline.split()[5])/float(textline.split()[6]) > float(B_best_attack_anta)/float(B_best_attack_anta):
							B_best_attack_num = textline.split()[0]
							B_best_attack_name = textline.split()[1]
							B_best_attack_pos = textline.split()[2]
							B_best_attack_tan = textline.split()[3]
							B_best_attack_anta = textline.split()[5]
							B_best_attack_ta = textline.split()[6]
							B_best_attack_home = textline.split()[7]

				line_num = line_num + 1
				textline = article.readline()
			else:
				break
		Bpitcherflag = True

	line_num = line_num + 1
	textline = article.readline()





#----------------------------
		
sentence1()

sentence2()
sentence3()
sentence4()
sentence5()

txtfile.close()

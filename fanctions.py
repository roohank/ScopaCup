import playsound
#import  semidbm
#import pickle
from saved_lists import *



## تابع پخش افکت صوتی
def play_sound(Address):
	try:
		playsound.playsound(Address)
	except:
		pass

# تابع انتقال امتیازها و اسکوپاها از لیست تودرتو به لیست ها
def score_to_list_mizban(bazi_mizban_1, group_1_list, score_list__1, natijeh_bazi_mizban_1, get_score_list__1,
						 los_score_list__1, scopa_list__1, scopa_mizban_1, get_scopa_list__1, los_scopa_list__1,
						 natijeh_bazi_mihman_1, scopa_mihman_1):
	e = 0
	for team in bazi_mizban_1:
		team_indx = group_1_list.index(team)
		score_list__1[team_indx].append(natijeh_bazi_mizban_1[e])
		get_score_list__1[team_indx].append(natijeh_bazi_mizban_1[e])
		los_score_list__1[team_indx].append(natijeh_bazi_mihman_1[e])
		scopa_list__1[team_indx].append(scopa_mizban_1[e])
		get_scopa_list__1[team_indx].append(scopa_mizban_1[e])
		los_scopa_list__1[team_indx].append(scopa_mihman_1[e])

		e += 1

# تابع انتقال امتیازها و اسکوپاها از لیست تودرتو به لیست ها+
# بخش میهمان
def score_to_list_mihman(bazi_mihman_1, group_1_list, score_list__1, natijeh_bazi_mizban_1, get_score_list__1,
						 los_score_list__1, scopa_list__1, scopa_mizban_1, get_scopa_list__1, los_scopa_list__1,
						 natijeh_bazi_mihman_1, scopa_mihman_1):
	e = 0
	for team in bazi_mihman_1:
		team_indx = group_1_list.index(team)
		score_list__1[team_indx].append(natijeh_bazi_mihman_1[e])
		get_score_list__1[team_indx].append(natijeh_bazi_mihman_1[e])
		los_score_list__1[team_indx].append(natijeh_bazi_mizban_1[e])
		scopa_list__1[team_indx].append(scopa_mihman_1[e])
		get_scopa_list__1[team_indx].append(scopa_mihman_1[e])
		los_scopa_list__1[team_indx].append(scopa_mizban_1[e])
		e += 1

#تابع اضافه کردن امتیاز بازی و تعداد اسکوپای تیمها به لیست ها
def input_score_to_list(bazi_mizban_1, natijeh_bazi_mizban_1, scopa_mizban_1, group_1_list, bazi_mihman_1,
						natijeh_bazi_mihman_1, scopa_mihman_1, game_team_grupe_1, input_player1, input_scor1, input_scopa1, input_player2, input_scor2, input_scopa2):
	bazi_mizban_1.append(input_player1)

	natijeh_bazi_mizban_1.append(input_scor1)

	scopa_mizban_1.append(input_scopa1)
	door1 = 0
	while not door1 == len(group_1_list):
		if input_player1 == group_1_list[door1]:
			game_team_grupe_1.append(input_player1)
		door1 += 1

	bazi_mihman_1.append(input_player2)

	natijeh_bazi_mihman_1.append(input_scor2)

	scopa_mihman_1.append(input_scopa2)
	for i in range(0, len(group_1_list)):
		if input_player2 == group_1_list[i]:
			# اضافه کردن به لیست بازی ها
			game_team_grupe_1.append(input_player2)

#تابع ویرایش امتیاز و اسکوپا
def editor_score_and_scopa(group_1_list, bazi_mizban_1, natijeh_bazi_mizban_1, scopa_mizban_1, bazi_mihman_1,
						   natijeh_bazi_mihman_1, scopa_mihman_1):

	play_sound("./sounds/focusMode.mp3")
	mizban_name = input("نام تیم میزبان را وارد کنید!")
	if mizban_name in group_1_list:
		play_sound("./sounds/focusMode.mp3")
		mihman_name = input("نام تیم میهمان را وارد کنید!")
		if mihman_name in group_1_list:
			print("امتیاز و تعداد اسکوپای تیم میزبان و تیم میهمان را از ابتدا وارد کنید!")
			for i in range(0, len(bazi_mizban_1)):
				if mizban_name == bazi_mizban_1[i]:
					pass
					if mihman_name == bazi_mihman_1[i]:
						print("امتیاز وارد شده تیم {}: {}  است!".format(bazi_mizban_1[i],
																		natijeh_bazi_mizban_1[i]))
						try:
							play_sound("./sounds/focusMode.mp3")
							right_emtiyaz_mizban_0 = input("امتیاز صحیح تیم میزبان را وارد کنید!")
							right_emtiyaz_mizban = int(right_emtiyaz_mizban_0)
							if right_emtiyaz_mizban < 0:
								play_sound("./sounds/rpause.mp3")
								print("شما نمیتوانید عددی کوچکتر از صفر وارد کنید!")
								continue
							print("تعداد اسکوپای  وارد شده تیم {}: {}  است!".format(bazi_mizban_1[i],
																					scopa_mizban_1[i]))
							play_sound("./sounds/focusMode.mp3")
							right_scopa_mizban_0 = input("تعداد اسکوپای میزبان را وارد کنید!")
							right_scopa_mizban = int(right_scopa_mizban_0)
							if right_scopa_mizban < 0:
								play_sound("./sounds/rpause.mp3")
								print("شما نمیتوانید عددی کوچکتر از صفر وارد کنید!")
								continue
							print("امتیاز وارد شده تیم {}: {}  است!".format(bazi_mihman_1[i],
																			natijeh_bazi_mihman_1[i]))
							play_sound("./sounds/focusMode.mp3")
							right_emtiyaz_mihman_0 = input("امتیاز صحیح تیم میهمان را وارد کنید!")
							right_emtiyaz_mihman = int(right_emtiyaz_mihman_0)
							if right_emtiyaz_mihman < 0:
								play_sound("./sounds/rpause.mp3")
								print("شما نمیتوانید عددی کوچکتر از صفر وارد کنید!")
								continue
							print("تعداد اسکوپای  وارد شده تیم {}: {}  است!".format(bazi_mihman_1[i],
																					scopa_mihman_1[i]))
							play_sound("./sounds/focusMode.mp3")
							right_scopa_mihman_0 = input("تعداد اسکوپای تیم میهمان را وارد کنید!")
							right_scopa_mihman = int(right_scopa_mihman_0)
							if right_scopa_mihman < 0:
								play_sound("./sounds/rpause.mp3")
								print("شما نمیتوانید عددی کوچکتر از صفر وارد کنید!")
								continue
							natijeh_bazi_mizban_1.pop(i)
							natijeh_bazi_mizban_1.insert(i, right_emtiyaz_mizban)
							scopa_mizban_1.pop(i)
							scopa_mizban_1.insert(i, right_scopa_mizban)
							natijeh_bazi_mihman_1.pop(i)
							natijeh_bazi_mihman_1.insert(i, right_emtiyaz_mihman)
							scopa_mihman_1.pop(i)
							scopa_mihman_1.insert(i, right_scopa_mihman)
						except:
							play_sound("./sounds/runpause.mp3")
							print("نوع ورودی اشتباه! ورودی را بصورت عدد صحیح وارد کنید.")
							continue
		else:
			play_sound("./sounds/runpause.mp3")
			print("تیم {} در این گروه وجود ندارد!".format(mihman_name))
	else:
		play_sound("./sounds/runpause.mp3")
		print("تیم {} در این گروه وجود ندارد!".format(mizban_name))

#تابع ویرایش جدول نام گروه
def editor_group_name_table(group_1_list, copy_group_1_list, game_team_grupe_1, all_teamss, bazi_mizban_1, bazi_mihman_1, group_1_lottery):
	play_sound("./sounds/focusMode.mp3")
	last_team_name = input("نام تیمی را که می خواهید از این گروه حذف شود را وارد کنید!")
	if last_team_name in group_1_list:
		play_sound("./sounds/focusMode.mp3")
		new_team_name = input("نام تیمی را که می خواهید جایگزین تیم قبلی شود را وارد کنید!")
		name_indx = group_1_list.index(last_team_name)
		group_1_list.pop(name_indx)
		group_1_list.insert(name_indx, new_team_name)
		copy_group_1_list.pop(name_indx)
		copy_group_1_list.insert(name_indx, new_team_name)
		c = 0
		for name in group_1_lottery:
			if name == last_team_name:
				group_1_lottery.pop(c)
				group_1_lottery.insert(c, new_team_name)
			c += 1

		c = 0
		for name in game_team_grupe_1:
			if name == last_team_name:
				game_team_grupe_1.pop(c)
				game_team_grupe_1.insert(c, new_team_name)
			c += 1
		for name in range(0, len(all_teamss)):
			if all_teamss[name] == last_team_name:
				all_teamss.pop(name)
				all_teamss.insert(name, new_team_name)
		c = 0
		for name in bazi_mizban_1:
			if name == last_team_name:
				bazi_mizban_1.pop(c)
				bazi_mizban_1.insert(c, new_team_name)
			c += 1
		c2 = 0
		for name in bazi_mihman_1:
			if name == last_team_name:
				bazi_mihman_1.pop(c2)
				bazi_mihman_1.insert(c2, new_team_name)
			c2 += 1
	else:
		play_sound("./sounds/runpause.mp3")
		print("تیم {}  در این گروه وجود ندارد!".format(last_team_name))

#تابع محاسبه امتیاز هر تیم از هر بازی
def score_calculator_mizban(natijeh_mizban, natijeh_mihman):
	# در صورت بُرد
	if natijeh_mizban > 20:
		pass
		if natijeh_mihman < 20:
			scor = 3
			return (scor)
	if natijeh_mizban > natijeh_mihman:
		pass
		if natijeh_mihman == 20:
			scor = 2
			return (scor)
	if natijeh_mizban > natijeh_mihman:
		pass
		if natijeh_mihman > 20:
			scor = 2
			return (scor)
	# در صورت باخت
	if natijeh_mizban < 20:
		scor = 0
		return (scor)
	if natijeh_mizban < natijeh_mihman:
		pass
		if natijeh_mizban == 20:
			scor = 1
			return (scor)
	if natijeh_mizban < natijeh_mihman:
		pass
		if natijeh_mizban > 20:
			scor = 1
			return (scor)


# بخش محاسبه امتیاز هر تیم از هر بازی تیم میهمان
def scor_calculator_mihman(natijeh_mihman, natijeh_mizban):
	# در صورت برد
	if natijeh_mihman > 20:
		pass
		if natijeh_mizban < 20:
			scor = 3
			return (scor)
	if natijeh_mihman > natijeh_mizban:
		pass
		if natijeh_mizban == 20:
			scor = 2
			return (scor)
	if natijeh_mihman > natijeh_mizban:
		pass
		if natijeh_mizban > 20:
			scor = 2
			return (scor)
	# در صورت باخت
	if natijeh_mihman < 20:
		scor = 0
		return (scor)
	if natijeh_mihman < natijeh_mizban:
		pass
		if natijeh_mihman == 20:
			scor = 1
			return (scor)
	if natijeh_mihman < natijeh_mizban:
		pass
		if natijeh_mihman > 20:
			scor = 1
			return (scor)

#تابع خروجی جدول امتیاز
def output_score_table(group_1_list, A, sort_name_team_1, sort_number_of_game_grupe_1, sort_emtiyaz_team_1, sort_majmoaa_scopa_1, sort_majmoa_bord_bakht_1, sort_tafazol_emtiyaz_list_1, sort_tafazol_scopa_list__1, list_team_info, db1, groups_number, mr_scopa_grope_1, mr):
	for n in range(0, groups_number):
		nameGroupeInfo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
		ng =nameGroupeInfo[n]
		for copy in range(0, len(group_1_list)):

			db1.write("{} گروه {} \n".format(list_team_info[copy], ng))
			db1.write("نام تیم: \t {} \n".format(sort_name_team_1[copy]))
			db1.write("تعداد بازی: \t {} \n".format(sort_number_of_game_grupe_1[copy]))
			db1.write("امتیاز تیم: \t {} \n".format(sort_emtiyaz_team_1[copy]))
			db1.write("تعداد اسکوپا: \t {} \n".format(sort_majmoaa_scopa_1[copy]))
			db1.write("تعداد بُرد: \t {} \n".format(sort_majmoa_bord_bakht_1[copy]))
			db1.write("تفاضل امتیاز: \t {} \n".format(sort_tafazol_emtiyaz_list_1[copy]))
			db1.write("تفاضل اسکوپا: \t {} \n".format(sort_tafazol_scopa_list__1[copy]))
			db1.write("\n")
		db1.write(
			"آقای اسکوپای گروه {} : تیم {}  با {} اسکوپای زده. \n".format(ng, mr_scopa_grope_1[0], mr))


#تابع محاسبه تعداد بازی های هر تیم
def number_play(group_1_list, score_list__1, number_of_game_grupe_1):
	for i in range(0, len(group_1_list)):
		len_list = len(score_list__1[i])
		number_of_game_grupe_1.append(len_list)


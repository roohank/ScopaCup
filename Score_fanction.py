import  semidbm
import pickle
from fanctions import *
from saved_lists import *
from list_scopa import *

#def ScoreScopa():
# فراخوانی لیست های ذخیره شدعه از دیتابیس
db = semidbm.open('DataBase', 'c')
group_dict = pickle.loads(db['group_dict'])
db.close()

cup_name = group_dict['cup_name']
	



play_sound("./sounds/mute_all.mp3")

number_of_groups = group_dict['groups_number']
play_sound("./sounds/replay.wav")

# یک فایل متنی برای خروجی گرفتن از جدول امتیاز بازیها ایجاد میکنیم
db1 = open('./DataBase/score_table.txt', 'w', encoding='utf-8')
db1.write("جدول امتیاز گروه های جام {} : \n".format(cup_name))

# یک فایل متنی برای خروجی گرفتن از آقای اسکوپای جام به ترتیب ایجاد میکنیم
db2 = open('./DataBase/mr scopa table.txt', 'w', encoding='utf-8')
db2.write(" ")
db2.close()
# بخش دسته بندی امتیاز ها و اسکوپاها در لیست مربوط به خود
# بخش امتیاز بازی میزبان
baziMizban = ['bazi_mizban_1', 'bazi_mizban_2', 'bazi_mizban_3', 'bazi_mizban_4', 'bazi_mizban_5',
			  'bazi_mizban_6', 'bazi_mizban_7', 'bazi_mizban_8', 'bazi_mizban_9', 'bazi_mizban_10', 'bazi_mizban_11', 'bazi_mizban_12', 'bazi_mizban_13', 'bazi_mizban_14', 'bazi_mizban_15', 'bazi_mizban_16']
baziMihman = ['bazi_mihman_1', 'bazi_mihman_2', 'bazi_mihman_3', 'bazi_mihman_4', 'bazi_mihman_5',
			  'bazi_mihman_6', 'bazi_mihman_7', 'bazi_mihman_8', 'bazi_mihman_9', 'bazi_mihman_10', 'bazi_mihman_11', 'bazi_mihman_12', 'bazi_mihman_13', 'bazi_mihman_14', 'bazi_mihman_15', 'bazi_mihman_16']
natijehMizban = ['natijeh_bazi_mizban_1', 'natijeh_bazi_mizban_2', 'natijeh_bazi_mizban_3',
				 'natijeh_bazi_mizban_4', 'natijeh_bazi_mizban_5', 'natijeh_bazi_mizban_6',
				 'natijeh_bazi_mizban_7', 'natijeh_bazi_mizban_8', 'natijeh_bazi_mizban_9', 'natijeh_bazi_mizban_10', 'natijeh_bazi_mizban_11', 'natijeh_bazi_mizban_12', 'natijeh_bazi_mizban_13', 'natijeh_bazi_mizban_14', 'natijeh_bazi_mizban_15', 'natijeh_bazi_mizban_16']
natijehMihman = ['natijeh_bazi_mihman_1', 'natijeh_bazi_mihman_2', 'natijeh_bazi_mihman_3',
				 'natijeh_bazi_mihman_4', 'natijeh_bazi_mihman_5', 'natijeh_bazi_mihman_6',
				 'natijeh_bazi_mihman_7', 'natijeh_bazi_mihman_8', 'natijeh_bazi_mihman_9', 'natijeh_bazi_mihman_10', 'natijeh_bazi_mihman_11', 'natijeh_bazi_mihman_12', 'natijeh_bazi_mihman_13', 'natijeh_bazi_mihman_14', 'natijeh_bazi_mihman_15', 'natijeh_bazi_mihman_16']
listGroupe = ['group_1_list', 'group_2_list', 'group_3_list', 'group_4_list', 'group_5_list',
			  'group_6_list', 'group_7_list', 'group_8_list', 'group_9_list', 'group_10_list', 'group_11_list', 'group_12_list', 'group_13_list', 'group_14_list', 'group_15_list', 'group_16_list']
scopaMizban = ['scopa_mizban_1', 'scopa_mizban_2', 'scopa_mizban_3', 'scopa_mizban_4', 'scopa_mizban_5',
			   'scopa_mizban_6', 'scopa_mizban_7', 'scopa_mizban_8', 'scopa_mizban_9', 'scopa_mizban_10', 'scopa_mizban_11', 'scopa_mizban_12', 'scopa_mizban_13', 'scopa_mizban_14', 'scopa_mizban_15', 'scopa_mizban_16']
scopamihman = ['scopa_mihman_1', 'scopa_mihman_2', 'scopa_mihman_3', 'scopa_mihman_4', 'scopa_mihman_5',
			   'scopa_mihman_6', 'scopa_mihman_7', 'scopa_mihman_8', 'scopa_mihman_9', 'scopa_mihman_10', 'scopa_mihman_11', 'scopa_mihman_12', 'scopa_mihman_13', 'scopa_mihman_14', 'scopa_mihman_15', 'scopa_mihman_16']
scoreList = ['score_list__1', 'score_list__2', 'score_list__3', 'score_list__4', 'score_list__5',
			 'score_list__6', 'score_list__7', 'score_list__8', 'score_list__9', 'score_list__10', 'score_list__11', 'score_list__12', 'score_list__13', 'score_list__14', 'score_list__15', 'score_list__16']
bord_bakht = ['bord_bakht_1', 'bord_bakht_2', 'bord_bakht_3', 'bord_bakht_4', 'bord_bakht_5', 'bord_bakht_6',
			  'bord_bakht_7', 'bord_bakht_8', 'bord_bakht_9', 'bord_bakht_10', 'bord_bakht_11', 'bord_bakht_12', 'bord_bakht_13', 'bord_bakht_14', 'bord_bakht_15', 'bord_bakht_16']
ejazeh = ['ejazeh_1', 'ejazeh_2', 'ejazeh_3', 'ejazeh_4', 'ejazeh_5', 'ejazeh_6', 'ejazeh_7', 'ejazeh_8', 'ejazeh_9', 'ejazeh_10', 'ejazeh_11', 'ejazeh_12', 'ejazeh_13', 'ejazeh_14', 'ejazeh_15', 'ejazeh_16']


xx = 1
for t in range(0, number_of_groups):
	nameGroupeInfo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

	grooh = nameGroupeInfo[t]
	db1.write(f"گروه {grooh}")
	db1.write("\n")	

	ng = nameGroupeInfo[t]
	b_miz = baziMizban[t]
	b_mizban = group_dict[b_miz]
	b_mih = baziMihman[t]
	b_mihman = group_dict[b_mih]
	s_miz = scopaMizban[t]
	s_mizban = group_dict[s_miz]
	s_mih = scopamihman[t]
	s_mihman = group_dict[s_mih]
	lg = listGroupe[t]
	gName = group_dict[lg]
	lenGroupe = len(gName)
	score_l = scoreList[t]
	e_ejazeh = ejazeh[t]
	e_j = group_dict[e_ejazeh]
	n_miz = natijehMizban[t]
	n_mizban = group_dict[n_miz]
	n_mih = natijehMihman[t]
	n_mihman = group_dict[n_mih]
	g_d = group_dict['groh_dasteh']


	#اگر امتیاز گروهی وارد نشده باشد حلقه ادامه پیدا نکند
	if not e_j == 'ok':
		xx += 1
		continue

	score_list__1 = [[], [], [], [], [], [], [], [], [], [], [], []]
	get_score_list__1 = [[], [], [], [], [], [], [], [], [], [], [], []]
	los_score_list__1 = [[], [], [], [], [], [], [], [], [], [], [], []]
	scopa_list__1 = [[], [], [], [], [], [], [], [], [], [], [], []]
	get_scopa_list__1 = [[], [], [], [], [], [], [], [], [], [], [], []]
	los_scopa_list__1 = [[], [], [], [], [], [], [], [], [], [], [], []]
	emtiyaz_list_1 = [[], [], [], [], [], [], [], [], [], [], [], []]
	sort_tafazol_emtiyaz_list_1 = []
	sort_tafazol_scopa_list__1 = []
	number_of_game_grupe_1 = []
	sort_number_of_game_grupe_1 = []
	majmoa_emtiyaz_1 = []
	sort_majmoa_emtiyaz_1 = []
	emtiyaz_team_list_1 = [[], [], [], [], [], [], [], [], [], [], [], []]
	sum_tafazol_emtiyaz_1 = []
	sum_tafazol_scopa_1 = []
	majmoaa_scopa_1 = []
	copy_majmoaa_scopa_1 = []
	sort_majmoaa_scopa_1 = []
	sum_emtiyaz_team_1 = []
	indx_sum_emtiyaz_team_1 = []
	sort_emtiyaz_team_1 = []
	sort_name_team_1 = []
	mr_scopa_grope_1 = []
	scopa_name_group = []
	sort_scopa_name_group = []
	bord_bakht_1 = [[], [], [], [], [], [], [], [], [], [], [], []]
	majmoa_bord_bakht_1 = []
	sort_majmoa_bord_bakht_1 = []
	sort_bord_bakht_1 = []

	e = 0
	for team in b_mizban:
		teamMizban_indx = gName.index(team)

		score_list__1[teamMizban_indx].append(n_mizban[e])
		get_score_list__1[teamMizban_indx].append(n_mizban[e])
		los_score_list__1[teamMizban_indx].append(n_mihman[e])
		scopa_list__1[teamMizban_indx].append(s_mizban[e])
		get_scopa_list__1[teamMizban_indx].append(s_mizban[e])
		los_scopa_list__1[teamMizban_indx].append(s_mihman[e])
		e += 1

	e = 0
	for team in b_mihman:
		teamMihman_indx = gName.index(team)

		score_list__1[teamMihman_indx].append(n_mihman[e])
		get_score_list__1[teamMihman_indx].append(n_mihman[e])
		los_score_list__1[teamMihman_indx].append(n_mizban[e])
		scopa_list__1[teamMihman_indx].append(s_mihman[e])
		get_scopa_list__1[teamMihman_indx].append(s_mihman[e])
		los_scopa_list__1[teamMihman_indx].append(s_mizban[e])
		e += 1



	#تعداد بازی هر تیم
	for i in range(0, len(group_dict['group_1_list'])):
		len_list = len(score_list__1[i])

		number_of_game_grupe_1.append(len_list)

	# بخش محاسبه امتیاز هر تیم از هر بازی
	e = 0
	for i in b_mizban:
		indx_a = gName.index(i)
		natijeh_mizban = n_mizban[e]
		natijeh_mihman = n_mihman[e]
		if natijeh_mizban > natijeh_mihman:
			t_b = 1
		else:
			t_b = 0

		score_mizban = score_calculator_mizban(natijeh_mizban, natijeh_mihman)
		emtiyaz_team_list_1[indx_a].append(score_mizban)
		bord_bakht_1[indx_a].append(t_b)
		e += 1

	#امتیاز تیم میهمان
	e = 0
	for i in b_mihman:
		indx_b = gName.index(i)
		natijeh_mizban = n_mizban[e]
		natijeh_mihman = n_mihman[e]
		if natijeh_mihman > natijeh_mizban:
			t_b = 1
		else:
			t_b = 0


		score_mihman = scor_calculator_mihman(natijeh_mihman, natijeh_mizban)
		emtiyaz_team_list_1[indx_b].append(score_mihman)
		bord_bakht_1[indx_b].append(t_b)
		e += 1
	# جمع کردن لیست امتیاز ها و اضافه کردن به لیست مجموع
	for i in range(0, len(group_dict['group_1_list'])):
		#sum_emtiyaz = sum(score_list__1[i])
		sum_bord = sum(bord_bakht_1[i])
		#majmoa_emtiyaz_1.append(sum_emtiyaz)
		majmoa_bord_bakht_1.append(sum_bord)

	# جمع امتیاز هر تیم از هر بازی
	for i in range(0, len(group_dict['group_1_list'])):
		sum_scor = sum(emtiyaz_team_list_1[i])
		sort_emtiyaz_team_1.append(sum_scor)
		sum_emtiyaz_team_1.append(sum_scor)

	# مرتب کردن لیست امتیاز ها از بزرگ به کوچک
	#sort_emtiyaz_team_1.sort()
	#sort_emtiyaz_team_1.reverse()
	# پیدا کردن اندیس امتیاز ها
	for i in sort_emtiyaz_team_1:
		b = sum_emtiyaz_team_1
		indx_a = b.index(i)

		sort_name_team_1.append(gName[indx_a])
		# حذف امتیاز پیدا شده بر اساس اندیس برای جلوگیری از تکرار نام تیم با امتیازهای مشابه
		b.pop(indx_a)
		b.insert(indx_a, "x")

	# بخش محاسبه تفاضل امتیاز و اسکوپا
	for i in range(0, len(gName)):
		sum_get_emtiyaz = sum(get_score_list__1[i])
		sum_los_emtiyaz = sum(los_score_list__1[i])
		result_tafazol_emtiyaz = (sum_get_emtiyaz - sum_los_emtiyaz)
		sum_tafazol_emtiyaz_1.append(result_tafazol_emtiyaz)
		# محاسبه مجموع تفاضضل اسکوپا
		sum_get_scopa = sum(get_scopa_list__1[i])
		sum_los_scopa = sum(los_scopa_list__1[i])
		result_tafazol_scopa = (sum_get_scopa - sum_los_scopa)
		sum_tafazol_scopa_1.append(result_tafazol_scopa)
	# مجموع اسکوپا گروه
	for i in range(0, len(gName)):
		sum_scopa = sum(scopa_list__1[i])
		majmoaa_scopa_1.append(sum_scopa)
		copy_majmoaa_scopa_1.append(sum_scopa)

	# تابع مرتب کردن لیست امتیازها و اسکوپاها
	# پیدا کردن اندیس لیست امتیاز نامرتب
	for i in sort_name_team_1:
		c = gName
		indx_a = c.index(i)
		indx_sum_emtiyaz_team_1.append(indx_a)
		# مرتب کردن لیست  تعداد بازی ها
		sort_number_of_game_grupe_1.append(number_of_game_grupe_1[indx_a])
		# مرتب کردن مجموع امتیازها
		#sort_majmoa_emtiyaz_1.append(majmoa_emtiyaz_1[indx_a])
		sort_majmoa_bord_bakht_1.append(majmoa_bord_bakht_1[indx_a])
		# مرتب کردن جمع اسکوپاها
		sort_majmoaa_scopa_1.append(majmoaa_scopa_1[indx_a])
		# مرتب کردن لیست تفاضل امتیاز ها و تفاضل اسکوپاها
		sort_tafazol_emtiyaz_list_1.append(sum_tafazol_emtiyaz_1[indx_a])
		sort_tafazol_scopa_list__1.append(sum_tafazol_scopa_1[indx_a])

	# مشخص کردن آقای اسکوپای گروه
	mr = max(majmoaa_scopa_1)
	mr_indx = copy_majmoaa_scopa_1.index(mr)
	mr_scopa_grope_1.append(gName[mr_indx])

	# وارد کردن همه اسکوپاها به لیست گروه
	for i in range(0, len(gName)):
		mr_scopa_cup_name.append(gName[i])
		mr_scopa_cup_teadad.append(majmoaa_scopa_1[i])
		copy_mr_scopa_cup_teadad.append(majmoaa_scopa_1[i])

	#مرتب کردن جدول با اولویت امتیاز تیم و تفاضل امتیاز
	lenList = len(sort_name_team_1)
	tuple_list = []

	for i in range(0, lenList):
		list0 = []
		list0.append(sort_emtiyaz_team_1[i])
		list0.append(sort_tafazol_emtiyaz_list_1[i])
		list0.append(sort_majmoaa_scopa_1[i])		
		list0.append(sort_tafazol_scopa_list__1[i])
		list0.append(sort_majmoa_bord_bakht_1[i])
		list0.append(sort_number_of_game_grupe_1[i])
		tp0 = tuple(list0)
		list1 = []
		list1.append(tp0)
		list1.append(sort_name_team_1[i])
		tp1 = tuple(list1)
		tuple_list.append(tp1)
		list0.clear()
		list1.clear()
	tuple_list.sort()
	tuple_list.reverse()
	lenTuple = len(tuple_list)

	emtiyaz = []
	tafazol_e = []
	tafazol_s = []
	teadad_s = []
	bord = []
	bazi = []
	team_n = []

	for i in range(0, lenTuple):
		emtiyaz.append(tuple_list[i][0][0])
		tafazol_e.append(tuple_list[i][0][1])
		teadad_s.append(tuple_list[i][0][2])
		tafazol_s.append(tuple_list[i][0][3])
		
		bord.append(tuple_list[i][0][4])
		bazi.append(tuple_list[i][0][5])
		team_n.append(tuple_list[i][1])


	# khoroji score

	db1 = open('./DataBase/score_table.txt', 'a', encoding='utf-8')
	# بخش خروجی گروه یک
	groups_number = group_dict['groups_number']

	
	for copy in range(0, lenGroupe):
		db1.write("{} گروه {} \n".format(list_team_info[copy], ng))
		db1.write("نام تیم: \t {} \n".format(team_n[copy]))
		db1.write("تعداد بازی: \t {} \n".format(bazi[copy]))
		db1.write("امتیاز تیم: \t {} \n".format(emtiyaz[copy]))
		db1.write("تعداد اسکوپا: \t {} \n".format(teadad_s[copy]))
		db1.write("تعداد بُرد: \t {} \n".format(bord[copy]))
		db1.write("تفاضل امتیاز: \t {} \n".format(tafazol_e[copy]))
		db1.write("تفاضل اسکوپا: \t {} \n".format(tafazol_s[copy]))
		db1.write("\n")
		
	db1.write(
	"آقای اسکوپای گروه {} : تیم {}  با {} اسکوپای زده. \n".format(ng, mr_scopa_grope_1[0], mr))

	db1.write("####################\n")
	db1.write("\n")

	xx += 1
db1.close()
# part_4 f

# مرتب کردن لیست آقای اسکوپای جام
copy_mr_scopa_cup_teadad.sort()
copy_mr_scopa_cup_teadad.reverse()
# پیدا کردن اندیس آقای اسکوپای جام
for i in copy_mr_scopa_cup_teadad:
	indx_number = mr_scopa_cup_teadad.index(i)

	n_c = mr_scopa_cup_name[indx_number]
	sort_mr_scopa_cup_name.append(n_c)
	mr_scopa_cup_teadad.pop(indx_number)
	mr_scopa_cup_teadad.insert(indx_number, "x")

all_teamss = group_dict['all_teamss']
for i in sort_mr_scopa_cup_name:
	team_index = all_teamss.index(i)
	groupe = g_d[team_index]
	sort_scopa_name_group.append(groupe)


# khoroji scopa
# خروجی گرفتن از آقای اسکوپای جام
db2 = open('./DataBase/mr scopa table.txt', 'w', encoding='utf-8')
db2.write("آقای اسکوپای جام {} به ترتیب:".format(cup_name))
db2.write("\n")

x = 1

for c in range(0, len(mr_scopa_cup_name)):
	db2.write(
		str(x) + "." + " " + "تیم {} از گروه {} با {} اسکوپای زده".format(sort_mr_scopa_cup_name[c],
																			sort_scopa_name_group[c],
																			copy_mr_scopa_cup_teadad[c]))
	db2.write("\n")
	x += 1
db2.close()



import  semidbm
import pickle
from fanctions import *
from saved_lists import *

# فراخوانی لیست های ذخیره شدعه از دیتابیس
db = semidbm.open('DataBase', 'c')
group_dict = pickle.loads(db['group_dict'])
db.close()

group_1_lottery = group_dict['group_1_lottery']
group_2_lottery = group_dict['group_2_lottery']
group_3_lottery = group_dict['group_3_lottery']
group_4_lottery = group_dict['group_4_lottery']
group_5_lottery = group_dict['group_5_lottery']
group_6_lottery = group_dict['group_6_lottery']
group_7_lottery = group_dict['group_7_lottery']
group_8_lottery = group_dict['group_8_lottery']
group_9_lottery = group_dict['group_9_lottery']
group_10_lottery = group_dict['group_10_lottery']
group_11_lottery = group_dict['group_11_lottery']
group_12_lottery = group_dict['group_12_lottery']
group_13_lottery = group_dict['group_13_lottery']
group_14_lottery = group_dict['group_14_lottery']
group_15_lottery = group_dict['group_15_lottery']
group_16_lottery = group_dict['group_16_lottery']
groups_number = group_dict['groups_number']
cup_name = group_dict['cup_name']
group_1_list = group_dict['group_1_list']


all_groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'p']



def output_lattery_4_12(group_1_lottery, dbm_name):
			len_dovr = len(group_1_lottery) / 2
			len_dovr = int(len_dovr)
			if not len(group_1_lottery) % 2 == 0:
				len_dovr = len_dovr + 1

			if len(group_1_lottery) == 12 or len(group_1_lottery) == 11:
				yekom1, dovom1, sevom1, chaarom1, panjom1, sheshom1, haftom1, hashtom1, nohom1, dahom1, yazdahom1 = lattery_for_grooups(
					group_1_lottery)
				if groups_number > 1:
					yekom2, dovom2, sevom2, chaarom2, panjom2, sheshom2, haftom2, hashtom2, nohom2, dahom2, yazdahom2 = lattery_for_grooups(
					group_2_lottery)
				if groups_number > 2:
					yekom3, dovom3, sevom3, chaarom3, panjom3, sheshom3, haftom3, hashtom3, nohom3, dahom3, yazdahom3 = lattery_for_grooups(
						group_3_lottery)
				if groups_number > 3:
					yekom4, dovom4, sevom4, chaarom4, panjom4, sheshom4, haftom4, hashtom4, nohom4, dahom4, yazdahom4 = lattery_for_grooups(
						group_4_lottery)
				if groups_number > 4:
					yekom5, dovom5, sevom5, chaarom5, panjom5, sheshom5, haftom5, hashtom5, nohom5, dahom5, yazdahom5 = lattery_for_grooups(
						group_5_lottery)
				if groups_number > 5:
					yekom6, dovom6, sevom6, chaarom6, panjom6, sheshom6, haftom6, hashtom6, nohom6, dahom6, yazdahom6 = lattery_for_grooups(
						group_6_lottery)
				if groups_number > 6:
					yekom7, dovom7, sevom7, chaarom7, panjom7, sheshom7, haftom7, hashtom7, nohom7, dahom7, yazdahom7 = lattery_for_grooups(
						group_7_lottery)
				if groups_number > 7:
					yekom8, dovom8, sevom8, chaarom8, panjom8, sheshom8, haftom8, hashtom8, nohom8, dahom8, yazdahom8 = lattery_for_grooups(
						group_8_lottery)
				if groups_number > 8:
					yekom9, dovom9, sevom9, chaarom9, panjom9, sheshom9, haftom9, hashtom9, nohom9, dahom9, yazdahom9 = lattery_for_grooups(
						group_9_lottery)
				if groups_number > 9:
					yekom10, dovom10, sevom10, chaarom10, panjom10, sheshom10, haftom10, hashtom10, nohom10, dahom10, yazdahom10 = lattery_for_grooups(
						group_10_lottery)
				if groups_number > 10:
					yekom11, dovom11, sevom11, chaarom11, panjom11, sheshom11, haftom11, hashtom11, nohom11, dahom11, yazdahom11 = lattery_for_grooups(
						group_11_lottery)
				if groups_number > 11:
					yekom12, dovom12, sevom12, chaarom12, panjom12, sheshom12, haftom12, hashtom12, nohom12, dahom12, yazdahom12 = lattery_for_grooups(
						group_12_lottery)
				if groups_number > 12:
					yekom13, dovom13, sevom13, chaarom13, panjom13, sheshom13, haftom13, hashtom13, nohom13, dahom13, yazdahom13 = lattery_for_grooups(
						group_13_lottery)
				if groups_number > 13:
					yekom14, dovom14, sevom14, chaarom14, panjom14, sheshom14, haftom14, hashtom14, nohom14, dahom14, yazdahom14 = lattery_for_grooups(
						group_14_lottery)
				if groups_number > 14:
					yekom15, dovom15, sevom15, chaarom15, panjom15, sheshom15, haftom15, hashtom15, nohom15, dahom15, yazdahom15 = lattery_for_grooups(
						group_15_lottery)
				if groups_number > 15:
					yekom16, dovom16, sevom16, chaarom16, panjom16, sheshom16, haftom16, hashtom16, nohom16, dahom16, yazdahom16 = lattery_for_grooups(
						group_16_lottery)
			# اگر تعداد تیم هر گروه ده تا باشد
			if len(group_1_lottery) == 10 or len(group_1_lottery) == 9:
				yekom1, dovom1, sevom1, chaarom1, panjom1, sheshom1, haftom1, hashtom1, nohom1 = lattery_for_grooups(
					group_1_lottery)
				if groups_number > 1:
					yekom2, dovom2, sevom2, chaarom2, panjom2, sheshom2, haftom2, hashtom2, nohom2 = lattery_for_grooups(
					group_2_lottery)
				if groups_number > 2:
					yekom3, dovom3, sevom3, chaarom3, panjom3, sheshom3, haftom3, hashtom3, nohom3 = lattery_for_grooups(
						group_3_lottery)
				if groups_number > 3:
					yekom4, dovom4, sevom4, chaarom4, panjom4, sheshom4, haftom4, hashtom4, nohom4 = lattery_for_grooups(
						group_4_lottery)
				if groups_number > 4:
					yekom5, dovom5, sevom5, chaarom5, panjom5, sheshom5, haftom5, hashtom5, nohom5 = lattery_for_grooups(
						group_5_lottery)
				if groups_number > 5:
					yekom6, dovom6, sevom6, chaarom6, panjom6, sheshom6, haftom6, hashtom6, nohom6 = lattery_for_grooups(
						group_6_lottery)
				if groups_number > 6:
					yekom7, dovom7, sevom7, chaarom7, panjom7, sheshom7, haftom7, hashtom7, nohom7 = lattery_for_grooups(
						group_7_lottery)
				if groups_number > 7:
					yekom8, dovom8, sevom8, chaarom8, panjom8, sheshom8, haftom8, hashtom8, nohom8 = lattery_for_grooups(
						group_8_lottery)
				if groups_number > 8:
					yekom9, dovom9, sevom9, chaarom9, panjom9, sheshom9, haftom9, hashtom9, nohom9 = lattery_for_grooups(
						group_9_lottery)
				if groups_number > 9:
					yekom10, dovom10, sevom10, chaarom10, panjom10, sheshom10, haftom10, hashtom10, nohom10 = lattery_for_grooups(
						group_10_lottery)
				if groups_number > 10:
					yekom11, dovom11, sevom11, chaarom11, panjom11, sheshom11, haftom11, hashtom11, nohom11 = lattery_for_grooups(
						group_11_lottery)
				if groups_number > 11:
					yekom12, dovom12, sevom12, chaarom12, panjom12, sheshom12, haftom12, hashtom12, nohom12 = lattery_for_grooups(
						group_12_lottery)
				if groups_number > 12:
					yekom13, dovom13, sevom13, chaarom13, panjom13, sheshom13, haftom13, hashtom13, nohom13 = lattery_for_grooups(
						group_13_lottery)
				if groups_number > 13:
					yekom14, dovom14, sevom14, chaarom14, panjom14, sheshom14, haftom14, hashtom14, nohom14 = lattery_for_grooups(
						group_14_lottery)
				if groups_number > 14:
					yekom15, dovom15, sevom15, chaarom15, panjom15, sheshom15, haftom15, hashtom15, nohom15 = lattery_for_grooups(
						group_15_lottery)
				if groups_number > 15:
					yekom16, dovom16, sevom16, chaarom16, panjom16, sheshom16, haftom16, hashtom16, nohom16 = lattery_for_grooups(
						group_16_lottery)
			# اگر تعداد تیم در هر گروه 8 تا باشد
			if len(group_1_lottery) == 8 or len(group_1_lottery) == 7:
				yekom1, dovom1, sevom1, chaarom1, panjom1, sheshom1, haftom1 = lattery_for_grooups(
					group_1_lottery)
				if groups_number > 1:
					yekom2, dovom2, sevom2, chaarom2, panjom2, sheshom2, haftom2 = lattery_for_grooups(
					group_2_lottery)
				if groups_number > 2:
					yekom3, dovom3, sevom3, chaarom3, panjom3, sheshom3, haftom3 = lattery_for_grooups(
						group_3_lottery)
				if groups_number > 3:
					yekom4, dovom4, sevom4, chaarom4, panjom4, sheshom4, haftom4 = lattery_for_grooups(
						group_4_lottery)
				if groups_number > 4:
					yekom5, dovom5, sevom5, chaarom5, panjom5, sheshom5, haftom5 = lattery_for_grooups(
						group_5_lottery)
				if groups_number > 5:
					yekom6, dovom6, sevom6, chaarom6, panjom6, sheshom6, haftom6 = lattery_for_grooups(
						group_6_lottery)
				if groups_number > 6:
					yekom7, dovom7, sevom7, chaarom7, panjom7, sheshom7, haftom7 = lattery_for_grooups(
						group_7_lottery)
				if groups_number > 7:
					yekom8, dovom8, sevom8, chaarom8, panjom8, sheshom8, haftom8 = lattery_for_grooups(
						group_8_lottery)
				if groups_number > 8:
					yekom9, dovom9, sevom9, chaarom9, panjom9, sheshom9, haftom9 = lattery_for_grooups(
						group_9_lottery)
				if groups_number > 9:
					yekom10, dovom10, sevom10, chaarom10, panjom10, sheshom10, haftom10 = lattery_for_grooups(
						group_10_lottery)
				if groups_number > 10:
					yekom11, dovom11, sevom11, chaarom11, panjom11, sheshom11, haftom11 = lattery_for_grooups(
						group_11_lottery)
				if groups_number > 11:
					yekom12, dovom12, sevom12, chaarom12, panjom12, sheshom12, haftom12 = lattery_for_grooups(
						group_12_lottery)
				if groups_number > 12:
					yekom13, dovom13, sevom13, chaarom13, panjom13, sheshom13, haftom13 = lattery_for_grooups(
						group_13_lottery)
				if groups_number > 13:
					yekom14, dovom14, sevom14, chaarom14, panjom14, sheshom14, haftom14 = lattery_for_grooups(
						group_14_lottery)
				if groups_number > 14:
					yekom15, dovom15, sevom15, chaarom15, panjom15, sheshom15, haftom15 = lattery_for_grooups(
						group_15_lottery)
				if groups_number > 15:
					yekom16, dovom16, sevom16, chaarom16, panjom16, sheshom16, haftom16 = lattery_for_grooups(
						group_16_lottery)
			# اگه تعداد تیم هر گروه 6 تا باشد
			if len(group_1_lottery) == 6 or len(group_1_lottery) == 5:
				yekom1, dovom1, sevom1, chaarom1, panjom1 = lattery_for_grooups(
					group_1_lottery)
				if groups_number > 1:
					yekom2, dovom2, sevom2, chaarom2, panjom2 = lattery_for_grooups(
					group_2_lottery)
				if groups_number > 2:
					yekom3, dovom3, sevom3, chaarom3, panjom3 = lattery_for_grooups(
						group_3_lottery)
				if groups_number > 3:
					yekom4, dovom4, sevom4, chaarom4, panjom4 = lattery_for_grooups(
						group_4_lottery)
				if groups_number > 4:
					yekom5, dovom5, sevom5, chaarom5, panjom5 = lattery_for_grooups(
						group_5_lottery)
				if groups_number > 5:
					yekom6, dovom6, sevom6, chaarom6, panjom6 = lattery_for_grooups(
						group_6_lottery)
				if groups_number > 6:
					yekom7, dovom7, sevom7, chaarom7, panjom7 = lattery_for_grooups(
						group_7_lottery)
				if groups_number > 7:
					yekom8, dovom8, sevom8, chaarom8, panjom8 = lattery_for_grooups(
						group_8_lottery)
				if groups_number > 8:
					yekom9, dovom9, sevom9, chaarom9, panjom9 = lattery_for_grooups(
						group_9_lottery)
				if groups_number > 9:
					yekom10, dovom10, sevom10, chaarom10, panjom10 = lattery_for_grooups(
						group_10_lottery)
				if groups_number > 10:
					yekom11, dovom11, sevom11, chaarom11, panjom11 = lattery_for_grooups(
						group_11_lottery)
				if groups_number > 11:
					yekom12, dovom12, sevom12, chaarom12, panjom12 = lattery_for_grooups(
						group_12_lottery)
				if groups_number > 12:
					yekom13, dovom13, sevom13, chaarom13, panjom13 = lattery_for_grooups(
						group_13_lottery)
				if groups_number > 13:
					yekom14, dovom14, sevom14, chaarom14, panjom14 = lattery_for_grooups(
						group_14_lottery)
				if groups_number > 14:
					yekom15, dovom15, sevom15, chaarom15, panjom15 = lattery_for_grooups(
						group_15_lottery)
				if groups_number > 15:
					yekom16, dovom16, sevom16, chaarom16, panjom16 = lattery_for_grooups(
						group_16_lottery)
			# اگه تعداد تیم در هر گروه 4 تا باشد
			if len(group_1_lottery) == 4 or len(group_1_lottery) == 3:
				yekom1, dovom1, sevom1 = lattery_for_grooups(
					group_1_lottery)
				if groups_number > 1:
					yekom2, dovom2, sevom2 = lattery_for_grooups(
					group_2_lottery)
				if groups_number > 2:
					yekom3, dovom3, sevom3 = lattery_for_grooups(
						group_3_lottery)
				if groups_number > 3:
					yekom4, dovom4, sevom4 = lattery_for_grooups(
						group_4_lottery)
				if groups_number > 4:
					yekom5, dovom5, sevom5 = lattery_for_grooups(
						group_5_lottery)
				if groups_number > 5:
					yekom6, dovom6, sevom6 = lattery_for_grooups(
						group_6_lottery)
				if groups_number > 6:
					yekom7, dovom7, sevom7 = lattery_for_grooups(
						group_7_lottery)
				if groups_number > 7:
					yekom8, dovom8, sevom8 = lattery_for_grooups(
						group_8_lottery)
				if groups_number > 8:
					yekom9, dovom9, sevom9 = lattery_for_grooups(
						group_9_lottery)
				if groups_number > 9:
					yekom10, dovom10, sevom10 = lattery_for_grooups(
						group_10_lottery)
				if groups_number > 10:
					yekom11, dovom11, sevom11 = lattery_for_grooups(
						group_11_lottery)
				if groups_number > 11:
					yekom12, dovom12, sevom12 = lattery_for_grooups(
						group_12_lottery)
				if groups_number > 12:
					yekom13, dovom13, sevom13 = lattery_for_grooups(
						group_13_lottery)
				if groups_number > 13:
					yekom14, dovom14, sevom14 = lattery_for_grooups(
						group_14_lottery)
				if groups_number > 14:
					yekom15, dovom15, sevom15 = lattery_for_grooups(
						group_15_lottery)
				if groups_number > 15:
					yekom16, dovom16, sevom16 = lattery_for_grooups(
						group_16_lottery)
			# دور یکم
			dbm_name = open('./DataBase/lottery_groups.txt', 'w', encoding='utf-8')
			dbm_name.write("جدول قرعه بازیهای جام {} : \n".format(cup_name))
			dbm_name.write("تعداد گروه در این جام : {} : \n".format(groups_number))
			dbm_name.write("تعداد تیم در هر گروه: {} : \n".format(len(group_1_list)))
			dbm_name.write("تعداد دور بازی در این مرحله: {} : \n".format(len(group_1_lottery) - 1))
			dbm_name.write("تیم اول به عنوان تیم میزبان و تیم دوم به عنوان تیم میهمان: \n")
			dbm_name.write("قرعه دور یکم بازی ها: \n")
			dbm_name.write("گروه A \n")
			raddif = 1
			for i in range(0, len_dovr):
				dbm_name.write(f"{raddif}. {yekom1[i][0]}- {yekom1[i][1]} \n")
				raddif += 1
			# دور اول گروه دوم
			if groups_number > 1:
				dbm_name.write("گروه B \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {yekom2[i][0]}- {yekom2[i][1]} \n")
					raddif += 1
			# دور یکم گروه سه
			if groups_number > 2:
				dbm_name.write("گروه C \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {yekom3[i][0]}- {yekom3[i][1]} \n")
					raddif += 1
				# دور یکم گروه چهارم
				if groups_number > 3:
					dbm_name.write("گروه D \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {yekom4[i][0]}- {yekom4[i][1]} \n")
						raddif += 1
					# دور یکم گروه پنجم
					if groups_number > 4:
						dbm_name.write("گروه E \n")
						raddif = 1
						for i in range(0, len_dovr):
							dbm_name.write(f"{raddif}. {yekom5[i][0]}- {yekom5[i][1]} \n")
							raddif += 1
						# دور یکم گروه شش
						if groups_number > 5:
							dbm_name.write("گروه F \n")
							raddif = 1
							for i in range(0, len_dovr):
								dbm_name.write(f"{raddif}. {yekom6[i][0]}- {yekom6[i][1]} \n")
								raddif += 1
							# دور یکم گروه هفتم
							if groups_number > 6:
								dbm_name.write("گروه G \n")
								raddif = 1
								for i in range(0, len_dovr):
									dbm_name.write(f"{raddif}. {yekom7[i][0]}- {yekom7[i][1]} \n")
									raddif += 1
								# دور یکم گروه هشتم
								if groups_number > 7:
									dbm_name.write("گروه H \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {yekom8[i][0]}- {yekom8[i][1]} \n")
										raddif += 1
								if groups_number > 8:
									dbm_name.write("گروه I \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {yekom9[i][0]}- {yekom9[i][1]} \n")
										raddif += 1
								if groups_number > 9:
									dbm_name.write("گروه J \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {yekom10[i][0]}- {yekom10[i][1]} \n")
										raddif += 1
								if groups_number > 10:
									dbm_name.write("گروه K \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {yekom11[i][0]}- {yekom11[i][1]} \n")
										raddif += 1
								if groups_number > 11:
									dbm_name.write("گروه L \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {yekom12[i][0]}- {yekom12[i][1]} \n")
										raddif += 1
								if groups_number > 12:
									dbm_name.write("گروه M \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {yekom13[i][0]}- {yekom13[i][1]} \n")
										raddif += 1
								if groups_number > 13:
									dbm_name.write("گروه N \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {yekom14[i][0]}- {yekom14[i][1]} \n")
										raddif += 1
								if groups_number > 14:
									dbm_name.write("گروه O \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {yekom15[i][0]}- {yekom15[i][1]} \n")
										raddif += 1
								if groups_number > 15:
									dbm_name.write("گروه P \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {yekom16[i][0]}- {yekom16[i][1]} \n")
										raddif += 1
			# دور دوم بازی ها
			dbm_name.write("\n")
			dbm_name.write("قرعه دور دوم بازیها: \n")
			# دور دوم گروه یک
			dbm_name.write("گروه A \n")
			raddif = 1
			for i in range(0, len_dovr):
				dbm_name.write(f"{raddif}. {dovom1[i][0]}- {dovom1[i][1]} \n")
				raddif += 1
			# دور دوم گروه دو
			if groups_number > 1:
				dbm_name.write("گروه B \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {dovom2[i][0]}- {dovom2[i][1]} \n")
					raddif += 1
			# دور دوم گروه سه
			if groups_number > 2:
				dbm_name.write("گروه C \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {dovom3[i][0]}- {dovom3[i][1]} \n")
					raddif += 1
				# دور دوم گروه چهرا
				if groups_number > 3:
					dbm_name.write("گروه D \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {dovom4[i][0]}- {dovom4[i][1]} \n")
						raddif += 1
					# دور دوم گروه پنجم
					if groups_number > 4:
						dbm_name.write("گروه E \n")
						raddif = 1
						for i in range(0, len_dovr):
							dbm_name.write(f"{raddif}. {dovom5[i][0]}- {dovom5[i][1]} \n")
							raddif += 1
						# دور دوم گروه شش
						if groups_number > 5:
							dbm_name.write("گروه F \n")
							raddif = 1
							for i in range(0, len_dovr):
								dbm_name.write(f"{raddif}. {dovom6[i][0]}- {dovom6[i][1]} \n")
								raddif += 1
							# دور دوم گروه هفتم
							if groups_number > 6:
								dbm_name.write("گروه G \n")
								raddif = 1
								for i in range(0, len_dovr):
									dbm_name.write(f"{raddif}. {dovom7[i][0]}- {dovom7[i][1]} \n")
									raddif += 1
								# دور دوم گروه هشتم
								if groups_number > 7:
									dbm_name.write("گروه H \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {dovom8[i][0]}- {dovom8[i][1]} \n")
										raddif += 1
								if groups_number > 8:
									dbm_name.write("گروه I \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {dovom9[i][0]}- {dovom9[i][1]} \n")
										raddif += 1
								#دور دوم گروه 10
								if groups_number > 9:
									dbm_name.write("گروه J \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {dovom10[i][0]}- {dovom10[i][1]} \n")
										raddif += 1
								#دور دوم گروه 11
								if groups_number > 10:
									dbm_name.write("گروه K \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {dovom11[i][0]}- {dovom11[i][1]} \n")
										raddif += 1
								#دور دوم گروه 12
								if groups_number > 11:
									dbm_name.write("گروه L \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {dovom12[i][0]}- {dovom12[i][1]} \n")
										raddif += 1
								#دور دوم گروه 13
								if groups_number > 12:
									dbm_name.write("گروه M \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {dovom13[i][0]}- {dovom13[i][1]} \n")
										raddif += 1
								#دور دوم گروه 14
								if groups_number > 13:
									dbm_name.write("گروه N \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {dovom14[i][0]}- {dovom14[i][1]} \n")
										raddif += 1
								#دور دوم گروه 15
								if groups_number > 14:
									dbm_name.write("گروه O \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {dovom15[i][0]}- {dovom15[i][1]} \n")
										raddif += 1
								#دور دوم گروه 16
								if groups_number > 15:
									dbm_name.write("گروه P \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {dovom16[i][0]}- {dovom16[i][1]} \n")
										raddif += 1
			# دور سوم بازیها

			dbm_name.write("\n")
			dbm_name.write("قرعه دور سوم بازیها: \n")
			# دور سوم گروه یک
			dbm_name.write("گروه A \n")
			raddif = 1
			for i in range(0, len_dovr):
				dbm_name.write(f"{raddif}. {sevom1[i][0]}- {sevom1[i][1]} \n")
				raddif += 1
			# دور سوم گروه دو
			if groups_number > 1:
				dbm_name.write("گروه B \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {sevom2[i][0]}- {sevom2[i][1]} \n")
					raddif += 1
			# دور سوم گروه سه
			if groups_number > 2:
				dbm_name.write("گروه C \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {sevom3[i][0]}- {sevom3[i][1]} \n")
					raddif += 1
				# دور سوم گروه چهار
				if groups_number > 3:
					dbm_name.write("گروه D \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {sevom4[i][0]}- {sevom4[i][1]} \n")
						raddif += 1
					# دور سوم گروه پنجم
					if groups_number > 4:
						dbm_name.write("گروه E \n")
						raddif = 1
						for i in range(0, len_dovr):
							dbm_name.write(f"{raddif}. {sevom5[i][0]}- {sevom5[i][1]} \n")
							raddif += 1
						# دور سوم گروه ششم
						if groups_number > 5:
							dbm_name.write("گروه F \n")
							raddif = 1
							for i in range(0, len_dovr):
								dbm_name.write(f"{raddif}. {sevom6[i][0]}- {sevom6[i][1]} \n")
								raddif += 1
							# دور سوم گروه هفتم
							if groups_number > 6:
								dbm_name.write("گروه G \n")
								raddif = 1
								for i in range(0, len_dovr):
									dbm_name.write(f"{raddif}. {sevom7[i][0]}- {sevom7[i][1]} \n")
									raddif += 1
								# دور سوم گروه هشتم
								if groups_number > 7:
									dbm_name.write("گروه H \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {sevom8[i][0]}- {sevom8[i][1]} \n")
										raddif += 1
								#دور سوم گروه 9
								if groups_number > 8:
									dbm_name.write("گروه I \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {sevom9[i][0]}- {sevom9[i][1]} \n")
										raddif += 1
								#دور سوم گروه 10
								if groups_number > 9:
									dbm_name.write("گروه J \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {sevom10[i][0]}- {sevom10[i][1]} \n")
										raddif += 1
								#دور سوم گروه 11
								if groups_number > 10:
									dbm_name.write("گروه K \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {sevom11[i][0]}- {sevom11[i][1]} \n")
										raddif += 1
								#دور سوم گروه 12
								if groups_number > 11:
									dbm_name.write("گروه L \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {sevom12[i][0]}- {sevom12[i][1]} \n")
										raddif += 1
								#دور سوم گروه 13
								if groups_number > 12:
									dbm_name.write("گروه M \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {sevom13[i][0]}- {sevom13[i][1]} \n")
										raddif += 1
								#دور سوم گره 14
								if groups_number > 13:
									dbm_name.write("گروه N \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {sevom14[i][0]}- {sevom14[i][1]} \n")
										raddif += 1
								#دور سوم گروه 15
								if groups_number > 14:
									dbm_name.write("گروه O \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {sevom15[i][0]}- {sevom15[i][1]} \n")
										raddif += 1
								#دور سوم گروه 16
								if groups_number > 15:
									dbm_name.write("گروه P \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {sevom16[i][0]}- {sevom16[i][1]} \n")
										raddif += 1
			# دور چهارم بازیها
			if len(group_1_lottery) > 4:
				dbm_name.write("\n")
				dbm_name.write("قرعه دور چهارم بازیها: \n")
				# دور چهارم گروه یک
				dbm_name.write("گروه A \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {chaarom1[i][0]}- {chaarom1[i][1]} \n")
					raddif += 1
				# دور چهارم گروه دو
				if groups_number > 1:
					dbm_name.write("گروه B \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {chaarom2[i][0]}- {chaarom2[i][1]} \n")
						raddif += 1
				# دور چهارم گروه سه
				if groups_number > 2:
					dbm_name.write("گروه C \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {chaarom3[i][0]}- {chaarom3[i][1]} \n")
						raddif += 1
					# دور چهارم گروه چهار
					if groups_number > 3:
						dbm_name.write("گروه D \n")
						raddif = 1
						for i in range(0, len_dovr):
							dbm_name.write(f"{raddif}. {chaarom4[i][0]}- {chaarom4[i][1]} \n")
							raddif += 1
						# دور چهارم گروه پنجم
						if groups_number > 4:
							dbm_name.write("گروه E \n")
							raddif = 1
							for i in range(0, len_dovr):
								dbm_name.write(f"{raddif}. {chaarom5[i][0]}- {chaarom5[i][1]} \n")
								raddif += 1
							# دور چهارم گروه ششم
							if groups_number > 5:
								dbm_name.write("گروه F \n")
								raddif = 1
								for i in range(0, len_dovr):
									dbm_name.write(f"{raddif}. {chaarom6[i][0]}- {chaarom6[i][1]} \n")
									raddif += 1
								# دور چهارم گروه هفتم
								if groups_number > 6:
									dbm_name.write("گروه G \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {chaarom7[i][0]}- {chaarom7[i][1]} \n")
										raddif += 1
									# دور چهارم گروه هشتم
									if groups_number > 7:
										dbm_name.write("گروه H \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {chaarom8[i][0]}- {chaarom8[i][1]} \n")
											raddif += 1
									#دور چهارم گروه 9
									if groups_number > 8:
										dbm_name.write("گروه I \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {chaarom9[i][0]}- {chaarom9[i][1]} \n")
											raddif += 1
									#دور چهارم گروه 10
									if groups_number > 9:
										dbm_name.write("گروه J \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {chaarom10[i][0]}- {chaarom10[i][1]} \n")
											raddif += 1
									#دور چهارم گروه 11
									if groups_number > 10:
										dbm_name.write("گروه K \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {chaarom11[i][0]}- {chaarom11[i][1]} \n")
											raddif += 1
									#دور چهارم گروه 12
									if groups_number > 11:
										dbm_name.write("گروه L \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {chaarom12[i][0]}- {chaarom12[i][1]} \n")
											raddif += 1
									#دور چهارم 13
									if groups_number > 12:
										dbm_name.write("گروه M \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {chaarom13[i][0]}- {chaarom13[i][1]} \n")
											raddif += 1
									#دور چهارم گروه 14
									if groups_number > 13:
										dbm_name.write("گروه N \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {chaarom14[i][0]}- {chaarom14[i][1]} \n")
											raddif += 1
									#دور چهارم گروه 15
									if groups_number > 14:
										dbm_name.write("گروه O \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {chaarom15[i][0]}- {chaarom15[i][1]} \n")
											raddif += 1
									#دور چهارم گروه 16
									if groups_number > 15:
										dbm_name.write("گروه P \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {chaarom16[i][0]}- {chaarom16[i][1]} \n")
											raddif += 1
			#دور پنجم بازیها
			if len(group_1_lottery) > 5:
				dbm_name.write("\n")
				dbm_name.write("قرعه دور پنجم بازیها: \n")
				# دور پنجم گروه یک
				dbm_name.write("گروه A \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {panjom1[i][0]}- {panjom1[i][1]} \n")
					raddif += 1
				# دور پنجم گروه دوم
				if groups_number > 1:
					dbm_name.write("گروه B \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {panjom2[i][0]}- {panjom2[i][1]} \n")
						raddif += 1
				# دور پنجم گروه سوم
				if groups_number > 2:
					dbm_name.write("گروه C \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {panjom3[i][0]}- {panjom3[i][1]} \n")
						raddif += 1
					# دور پنجم گروه چهارم
					if groups_number > 3:
						dbm_name.write("گروه D \n")
						raddif = 1
						for i in range(0, len_dovr):
							dbm_name.write(f"{raddif}. {panjom4[i][0]}- {panjom4[i][1]} \n")
							raddif += 1
						# دور پنجم گروه پنجم
						if groups_number > 4:
							dbm_name.write("گروه E \n")
							raddif = 1
							for i in range(0, len_dovr):
								dbm_name.write(f"{raddif}. {panjom5[i][0]}- {panjom5[i][1]} \n")
								raddif += 1
							# دور پپنجم گروه ششم
							if groups_number > 5:
								dbm_name.write("گروه F \n")
								raddif = 1
								for i in range(0, len_dovr):
									dbm_name.write(f"{raddif}. {panjom6[i][0]}- {panjom6[i][1]} \n")
									raddif += 1
								# دور پنجم گگروه هفتم
								if groups_number > 6:
									dbm_name.write("گروه G \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {panjom7[i][0]}- {panjom7[i][1]} \n")
										raddif += 1
									# دور پنجم گروه هشتم
									if groups_number > 7:
										dbm_name.write("گروه H \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {panjom8[i][0]}- {panjom8[i][1]} \n")
											raddif += 1
									#دور پنجم گروه 9
									if groups_number > 8:
										dbm_name.write("گروه I \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {panjom9[i][0]}- {panjom9[i][1]} \n")
											raddif += 1
									#دور پنجم گروه 10
									if groups_number > 9:
										dbm_name.write("گروه J \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {panjom10[i][0]}- {panjom10[i][1]} \n")
											raddif += 1
									#دور پنجم گروه 11
									if groups_number > 10:
										dbm_name.write("گروه K \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {panjom11[i][0]}- {panjom11[i][1]} \n")
											raddif += 1
									#دور پنجم گروه 12
									if groups_number > 11:
										dbm_name.write("گروه L \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {panjom12[i][0]}- {panjom12[i][1]} \n")
											raddif += 1
									#دور پنجم گروه 13
									if groups_number > 12:
										dbm_name.write("گروه M \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {panjom13[i][0]}- {panjom13[i][1]} \n")
											raddif += 1
									#دور پنجم گروه 14
									if groups_number > 13:
										dbm_name.write("گروه N \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {panjom14[i][0]}- {panjom14[i][1]} \n")
											raddif += 1
									#دور پنجم گروه 15
									if groups_number > 14:
										dbm_name.write("گروه O \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {panjom15[i][0]}- {panjom15[i][1]} \n")
											raddif += 1
									#دور پنجم گروه 16
									if groups_number > 15:
										dbm_name.write("گروه P \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {panjom16[i][0]}- {panjom16[i][1]} \n")
											raddif += 1

			#دور ششم بازیها
			if len(group_1_lottery) > 6:
				# دور ششم بازیها
				dbm_name.write("\n")
				dbm_name.write("قرعه دور ششم بازیها: \n")
				# دور ششم گروه یک
				dbm_name.write("گروه A \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {sheshom1[i][0]}- {sheshom1[i][1]} \n")
					raddif += 1
				# دور ششم گروه دوم
				if groups_number > 1:
					dbm_name.write("گروه B \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {sheshom2[i][0]}- {sheshom2[i][1]} \n")
						raddif += 1
				# دور ششم گروه سوم
				if groups_number > 2:
					dbm_name.write("گروه C \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {sheshom3[i][0]}- {sheshom3[i][1]} \n")
						raddif += 1
					# دور ششم گروه چهارم
					if groups_number > 3:
						dbm_name.write("گروه D \n")
						raddif = 1
						for i in range(0, len_dovr):
							dbm_name.write(f"{raddif}. {sheshom4[i][0]}- {sheshom4[i][1]} \n")
							raddif += 1
						# دور ششم گروه پنجم
						if groups_number > 4:
							dbm_name.write("گروه E \n")
							raddif = 1
							for i in range(0, len_dovr):
								dbm_name.write(f"{raddif}. {sheshom5[i][0]}- {sheshom5[i][1]} \n")
								raddif += 1
							# دور ششم گروه ششم
							if groups_number > 5:
								dbm_name.write("گروه F \n")
								raddif = 1
								for i in range(0, len_dovr):
									dbm_name.write(f"{raddif}. {sheshom6[i][0]}- {sheshom6[i][1]} \n")
									raddif += 1
								# دور ششم گروه هفتم
								if groups_number > 6:
									dbm_name.write("گروه G \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {sheshom7[i][0]}- {sheshom7[i][1]} \n")
										raddif += 1
									# دور ششم گروه هشتم
									if groups_number > 7:
										dbm_name.write("گروه H \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {sheshom8[i][0]}- {sheshom8[i][1]} \n")
											raddif += 1
									#دور ششم گروه  9
									if groups_number > 8:
										dbm_name.write("گروه I \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {sheshom9[i][0]}- {sheshom9[i][1]} \n")
											raddif += 1
									#دور ششم گروه 10
									if groups_number > 9:
										dbm_name.write("گروه J \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {sheshom10[i][0]}- {sheshom10[i][1]} \n")
											raddif += 1
									#دور ششم گروه 11
									if groups_number > 10:
										dbm_name.write("گروه K \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {sheshom11[i][0]}- {sheshom11[i][1]} \n")
											raddif += 1
									#دور ششم گروه 12
									if groups_number > 11:
										dbm_name.write("گروه L \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {sheshom12[i][0]}- {sheshom12[i][1]} \n")
											raddif += 1
									#دور ششم گروه 13
									if groups_number > 12:
										dbm_name.write("گروه M \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {sheshom13[i][0]}- {sheshom13[i][1]} \n")
											raddif += 1
									#دور ششم گروه 14
									if groups_number > 13:
										dbm_name.write("گروه N \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {sheshom14[i][0]}- {sheshom14[i][1]} \n")
											raddif += 1
									#دور ششم گروه 15
									if groups_number > 14:
										dbm_name.write("گروه O \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {sheshom15[i][0]}- {sheshom15[i][1]} \n")
											raddif += 1
									#دور ششم گروه 16
									if groups_number > 15:
										dbm_name.write("گروه P \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {sheshom16[i][0]}- {sheshom16[i][1]} \n")
											raddif += 1
			
			if len(group_1_lottery) > 7:
				# دور هفتم بازیها
				dbm_name.write("\n")
				dbm_name.write("قرعه دور هفتم بازیها: \n")
				##دور هفتم گروه یک
				dbm_name.write("گروه A \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {haftom1[i][0]}- {haftom1[i][1]} \n")
					raddif += 1
				# دور هفتم گروه دوم
				if groups_number > 1:
					dbm_name.write("گروه B \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {haftom2[i][0]}- {haftom2[i][1]} \n")
						raddif += 1
				# دور هفتم گروه سوم
				if groups_number > 2:
					dbm_name.write("گروه C \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {haftom3[i][0]}- {haftom3[i][1]} \n")
						raddif += 1
					# دور هفتم گروه چهارم
					if groups_number > 3:
						dbm_name.write("گروه D \n")
						raddif = 1
						for i in range(0, len_dovr):
							dbm_name.write(f"{raddif}. {haftom4[i][0]}- {haftom4[i][1]} \n")
							raddif += 1
						# دور هفتم گروه پنجم
						if groups_number > 4:
							dbm_name.write("گروه E \n")
							raddif = 1
							for i in range(0, len_dovr):
								dbm_name.write(f"{raddif}. {haftom5[i][0]}- {haftom5[i][1]} \n")
								raddif += 1
							# دور هفتم گروه ششم
							if groups_number > 5:
								dbm_name.write("گروه F \n")
								raddif = 1
								for i in range(0, len_dovr):
									dbm_name.write(f"{raddif}. {haftom6[i][0]}- {haftom6[i][1]} \n")
									raddif += 1
								# دور هفتم گروه هفتم
								if groups_number > 6:
									dbm_name.write("گروه G \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {haftom7[i][0]}- {haftom7[i][1]} \n")
										raddif += 1
									# دور هفتم گروه هشتم
									if groups_number > 7:
										dbm_name.write("گروه H \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {haftom8[i][0]}- {haftom8[i][1]} \n")
											raddif += 1
									#دور هفتم گروه 9
									if groups_number > 8:
										dbm_name.write("گروه I \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {haftom9[i][0]}- {haftom9[i][1]} \n")
											raddif += 1
									#دور هفتم گروه 10
									if groups_number > 9:
										dbm_name.write("گروه J \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {haftom10[i][0]}- {haftom10[i][1]} \n")
											raddif += 1
									#دور هفتم گروه 11
									if groups_number > 10:
										dbm_name.write("گروه K \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {haftom11[i][0]}- {haftom11[i][1]} \n")
											raddif += 1
									#دور هفتم گروه 12
									if groups_number > 7:
										dbm_name.write("گروه L \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {haftom12[i][0]}- {haftom12[i][1]} \n")
											raddif += 1
									#دور هفتم گروه 13
									if groups_number > 12:
										dbm_name.write("گروه M \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {haftom13[i][0]}- {haftom13[i][1]} \n")
											raddif += 1
									#دور هفتم گروه 14
									if groups_number > 13:
										dbm_name.write("گروه N \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {haftom14[i][0]}- {haftom14[i][1]} \n")
											raddif += 1
									#دور هفتم گروه 15
									if groups_number > 14:
										dbm_name.write("گروه O \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {haftom15[i][0]}- {haftom15[i][1]} \n")
											raddif += 1
									#دور هفتم گروه 16
									if groups_number > 15:
										dbm_name.write("گروه P \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {haftom16[i][0]}- {haftom16[i][1]} \n")
											raddif += 1

			if len(group_1_lottery) > 8:
				# دور هشتم  بزیها
				dbm_name.write("\n")
				dbm_name.write("قرعه دور هشتم بازیها: \n")
				# دور هشتم گروه یکم
				dbm_name.write("گروه A \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {hashtom1[i][0]}- {hashtom1[i][1]} \n")
					raddif += 1
				# دور هشتم گروه دوم
				if groups_number > 1:
					dbm_name.write("گروه B \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {hashtom2[i][0]}- {hashtom2[i][1]} \n")
						raddif += 1
				# دور هشتم گروه سوم
				if groups_number > 2:
					dbm_name.write("گروه C \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {hashtom3[i][0]}- {hashtom3[i][1]} \n")
						raddif += 1
					# دور هشتم گروه چهارم
					if groups_number > 3:
						dbm_name.write("گروه D \n")
						raddif = 1
						for i in range(0, len_dovr):
							dbm_name.write(f"{raddif}. {hashtom4[i][0]}- {hashtom4[i][1]} \n")
							raddif += 1
						# دور هشتم پگروه پنجم
						if groups_number > 4:
							dbm_name.write("گروه E \n")
							raddif = 1
							for i in range(0, len_dovr):
								dbm_name.write(f"{raddif}. {hashtom5[i][0]}- {hashtom5[i][1]} \n")
								raddif += 1
							# دور هشتم گروه ششم
							if groups_number > 5:
								dbm_name.write("گروه F \n")
								raddif = 1
								for i in range(0, len_dovr):
									dbm_name.write(f"{raddif}. {hashtom6[i][0]}- {hashtom6[i][1]} \n")
									raddif += 1
								# دور هشتم گروه هفتم
								if groups_number > 6:
									dbm_name.write("گروه G \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {hashtom7[i][0]}- {hashtom7[i][1]} \n")
										raddif += 1
								# دور هشت گروه هشتم
								if groups_number > 7:
									dbm_name.write("گروه H \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {hashtom8[i][0]}- {hashtom8[i][1]} \n")
										raddif += 1
								#دور هشتم گروه 9
								if groups_number > 8:
									dbm_name.write("گروه I \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {hashtom9[i][0]}- {hashtom9[i][1]} \n")
										raddif += 1
								#دور هشتم گروه 10
								if groups_number > 9:
									dbm_name.write("گروه J \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {hashtom10[i][0]}- {hashtom10[i][1]} \n")
										raddif += 1
								#دور هشتم گروه 11
								if groups_number > 10:
									dbm_name.write("گروه K \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {hashtom11[i][0]}- {hashtom11[i][1]} \n")
										raddif += 1
								#دور هشتم گروه 12
								if groups_number > 11:
									dbm_name.write("گروه L \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {hashtom12[i][0]}- {hashtom12[i][1]} \n")
										raddif += 1
								#دور هشتم گروه 13
								if groups_number > 12:
									dbm_name.write("گروه M \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {hashtom13[i][0]}- {hashtom13[i][1]} \n")
										raddif += 1
								#دور هشتم گروه 14
								if groups_number > 13:
									dbm_name.write("گروه N \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {hashtom14[i][0]}- {hashtom14[i][1]} \n")
										raddif += 1
								#دور هشتم گروه 15
								if groups_number > 14:
									dbm_name.write("گروه O \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {hashtom15[i][0]}- {hashtom15[i][1]} \n")
										raddif += 1
								#دور هشتم گروه 16
								if groups_number > 15:
									dbm_name.write("گروه P \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {hashtom16[i][0]}- {hashtom16[i][1]} \n")
										raddif += 1
			if len(group_1_lottery) > 9:
				# دور نهم بازیها
				dbm_name.write("\n")
				dbm_name.write("قرعه دور نهم بازیها: \n")
				# دور نهم گروه یکم
				dbm_name.write("گروه A \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {nohom1[i][0]}- {nohom1[i][1]} \n")
					raddif += 1
				# دور نهم گروه دوم
				if groups_number > 1:
					dbm_name.write("گروه B \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {nohom2[i][0]}- {nohom2[i][1]} \n")
						raddif += 1
				# دور نهم گروه سوم
				if groups_number > 2:
					dbm_name.write("گروه C \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {nohom3[i][0]}- {nohom3[i][1]} \n")
						raddif += 1
					# دور نهم گروه چهارم
					if groups_number > 3:
						dbm_name.write("گروه D \n")
						raddif = 1
						for i in range(0, len_dovr):
							dbm_name.write(f"{raddif}. {nohom4[i][0]}- {nohom4[i][1]} \n")
							raddif += 1
						# دور نهم گروه پنجم
						if groups_number > 4:
							dbm_name.write("گروه E \n")
							raddif = 1
							for i in range(0, len_dovr):
								dbm_name.write(f"{raddif}. {nohom5[i][0]}- {nohom5[i][1]} \n")
								raddif += 1
							# دور نهم گروه ششم
							if groups_number > 5:
								dbm_name.write("گروه F \n")
								raddif = 1
								for i in range(0, len_dovr):
									dbm_name.write(f"{raddif}. {nohom6[i][0]}- {nohom6[i][1]} \n")
									raddif += 1
								# دور نهم گروه هفتم
								if groups_number > 6:
									dbm_name.write("گروه G \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {nohom7[i][0]}- {nohom7[i][1]} \n")
										raddif += 1
									# دور نهم گروه هشتم
									if groups_number > 7:
										dbm_name.write("گروه H \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {nohom8[i][0]}- {nohom8[i][1]} \n")
											raddif += 1
									#دور نهم گروه 9
									if groups_number > 8:
										dbm_name.write("گروه I \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {nohom9[i][0]}- {nohom9[i][1]} \n")
											raddif += 1
									#دور نهم گروه 10
									if groups_number > 9:
										dbm_name.write("گروه J \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {nohom10[i][0]}- {nohom10[i][1]} \n")
											raddif += 1
									#دور نهم گروه 11
									if groups_number > 10:
										dbm_name.write("گروه K \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {nohom11[i][0]}- {nohom11[i][1]} \n")
											raddif += 1
									#دور نهم گره 12
									if groups_number > 11:
										dbm_name.write("گروه K \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {nohom12[i][0]}- {nohom12[i][1]} \n")
											raddif += 1
									#دور نهم گروه 13
									if groups_number > 12:
										dbm_name.write("گروه M \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {nohom13[i][0]}- {nohom13[i][1]} \n")
											raddif += 1
									#دور نهم گروه 14
									if groups_number > 13:
										dbm_name.write("گروه N \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {nohom14[i][0]}- {nohom14[i][1]} \n")
											raddif += 1
									#دور نهم گروه 15
									if groups_number > 14:
										dbm_name.write("گروه O \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {nohom15[i][0]}- {nohom15[i][1]} \n")
											raddif += 1
									#دور نهم گروه 16
									if groups_number > 15:
										dbm_name.write("گروه P \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {nohom16[i][0]}- {nohom16[i][1]} \n")
											raddif += 1
			if len(group_1_lottery) > 10:
				# قرعه دور دهم بازیها
				dbm_name.write("\n")
				dbm_name.write("قرعه دور دهم بازیها: \n")
				##دور دهم گروه یکم
				dbm_name.write("گروه A \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {dahom1[i][0]}- {dahom1[i][1]} \n")
					raddif += 1
				# دور دهم گروه دوم
				if groups_number > 1:
					dbm_name.write("گروه B \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {dahom2[i][0]}- {dahom2[i][1]} \n")
						raddif += 1
				# دور دهم گروه سوم
				if groups_number > 2:
					dbm_name.write("گروه C \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {dahom3[i][0]}- {dahom3[i][1]} \n")
						raddif += 1
					##دور دهم گروه چهارم
					if groups_number > 3:
						dbm_name.write("گروه D \n")
						raddif = 1
						for i in range(0, len_dovr):
							dbm_name.write(f"{raddif}. {dahom4[i][0]}- {dahom4[i][1]} \n")
							raddif += 1
						# دور دهم گروه پنجم
						if groups_number > 4:
							dbm_name.write("گروه E \n")
							raddif = 1
							for i in range(0, len_dovr):
								dbm_name.write(f"{raddif}. {dahom5[i][0]}- {dahom5[i][1]} \n")
								raddif += 1
							# دور دهم گروه ششم
							if groups_number > 5:
								dbm_name.write("گروه F \n")
								raddif = 1
								for i in range(0, len_dovr):
									dbm_name.write(f"{raddif}. {dahom6[i][0]}- {dahom6[i][1]} \n")
									raddif += 1
								# دور دهم گروه هفتم
								if groups_number > 6:
									dbm_name.write("گروه G \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {dahom7[i][0]}- {dahom7[i][1]} \n")
										raddif += 1
									# دور دهم گروه هشتم
									if groups_number > 7:
										dbm_name.write("گروه H \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {dahom8[i][0]}- {dahom8[i][1]} \n")
											raddif += 1
									#دور دهم گروه 9
									if groups_number > 8:
										dbm_name.write("گروه I \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {dahom9[i][0]}- {dahom9[i][1]} \n")
											raddif += 1
									#دور دهم گروه 10
									if groups_number > 9:
										dbm_name.write("گروه J \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {dahom10[i][0]}- {dahom10[i][1]} \n")
											raddif += 1
									#دور دهم گروه 11
									if groups_number > 10:
										dbm_name.write("گروه K \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {dahom11[i][0]}- {dahom11[i][1]} \n")
											raddif += 1
									#دور دهم گروه 12
									if groups_number > 11:
										dbm_name.write("گروه L \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {dahom12[i][0]}- {dahom12[i][1]} \n")
											raddif += 1
									#دور دهم گروه 13
									if groups_number > 12:
										dbm_name.write("گروه M \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {dahom13[i][0]}- {dahom13[i][1]} \n")
											raddif += 1
									#دور دهم گروه 14
									if groups_number > 13:
										dbm_name.write("گروه N \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {dahom14[i][0]}- {dahom14[i][1]} \n")
											raddif += 1
									#دور دهم گروه 15
									if groups_number > 14:
										dbm_name.write("گروه O \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {dahom15[i][0]}- {dahom15[i][1]} \n")
											raddif += 1
									#دور دهم گروه 16
									if groups_number > 15:
										dbm_name.write("گروه P \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {dahom16[i][0]}- {dahom16[i][1]} \n")
											raddif += 1
			if len(group_1_lottery) > 11:
				# قرعه دور یازدهم بازیها
				dbm_name.write("\n")
				dbm_name.write("قرعه دور یازدهم بازیها: \n")
				# دور یازدهم گروه یکم
				dbm_name.write("گروه A \n")
				raddif = 1
				for i in range(0, len_dovr):
					dbm_name.write(f"{raddif}. {yazdahom1[i][0]}- {yazdahom1[i][1]} \n")
					raddif += 1
				# دور یازدهم گروه دوم
				if groups_number > 1:
					dbm_name.write("گروه B \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {yazdahom2[i][0]}- {yazdahom2[i][1]} \n")
						raddif += 1
				# دور یازدهم گروه سوم
				if groups_number > 2:
					dbm_name.write("گروه C \n")
					raddif = 1
					for i in range(0, len_dovr):
						dbm_name.write(f"{raddif}. {yazdahom3[i][0]}- {yazdahom3[i][1]} \n")
						raddif += 1
					# دور یازدهم گروه چهارم
					if groups_number > 3:
						dbm_name.write("گروه D \n")
						raddif = 1
						for i in range(0, len_dovr):
							dbm_name.write(f"{raddif}. {yazdahom4[i][0]}- {yazdahom4[i][1]} \n")
							raddif += 1
						# دور یازدهم گروه پنجم
						if groups_number > 4:
							dbm_name.write("گروه E \n")
							raddif = 1
							for i in range(0, len_dovr):
								dbm_name.write(f"{raddif}. {yazdahom5[i][0]}- {yazdahom5[i][1]} \n")
								raddif += 1
							# دور یازدهم گروه ششم
							if groups_number > 5:
								dbm_name.write("گروه F \n")
								raddif = 1
								for i in range(0, len_dovr):
									dbm_name.write(f"{raddif}. {yazdahom6[i][0]}- {yazdahom6[i][1]} \n")
									raddif += 1
								# دور یازدهم گروه هفتم
								if groups_number > 6:
									dbm_name.write("گروه G \n")
									raddif = 1
									for i in range(0, len_dovr):
										dbm_name.write(f"{raddif}. {yazdahom7[i][0]}- {yazdahom7[i][1]} \n")
										raddif += 1
									# دور یازدهم گروه هشتم
									if groups_number > 7:
										dbm_name.write("گروه H \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {yazdahom8[i][0]}- {yazdahom8[i][1]} \n")
											raddif += 1
									#دور یازدهم گروه 9
									if groups_number > 8:
										dbm_name.write("گروه I \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {yazdahom9[i][0]}- {yazdahom9[i][1]} \n")
											raddif += 1
									#دور یازدهم گروه 10
									if groups_number > 9:
										dbm_name.write("گروه J \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {yazdahom10[i][0]}- {yazdahom10[i][1]} \n")
											raddif += 1
									#دور یازدهم گروه 11
									if groups_number > 10:
										dbm_name.write("گروه K \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {yazdahom11[i][0]}- {yazdahom11[i][1]} \n")
											raddif += 1
									#دور یازدهم گروه 12
									if groups_number > 11:
										dbm_name.write("گروه L \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {yazdahom12[i][0]}- {yazdahom12[i][1]} \n")
											raddif += 1
									#دور یازدهم گروه 13
									if groups_number > 12:
										dbm_name.write("گروه M \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {yazdahom13[i][0]}- {yazdahom13[i][1]} \n")
											raddif += 1
									#دور یازدهم گروه 14
									if groups_number > 13:
										dbm_name.write("گروه N \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {yazdahom14[i][0]}- {yazdahom14[i][1]} \n")
											raddif += 1
									#دور یازدهم گروه 15
									if groups_number > 14:
										dbm_name.write("گروه O \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {yazdahom15[i][0]}- {yazdahom15[i][1]} \n")
											raddif += 1
									#دور یازدهم گروه 16
									if groups_number > 15:
										dbm_name.write("گروه P \n")
										raddif = 1
										for i in range(0, len_dovr):
											dbm_name.write(f"{raddif}. {yazdahom16[i][0]}- {yazdahom16[i][1]} \n")
											raddif += 1
			dbm_name.close()



def lattery_for_grooups(group_1_lottery):
	if not len(group_1_lottery) % 2 == 0:
		if groups_number > 0:
			group_1_lottery.append("B")
		if groups_number > 1:
			group_2_lottery.append("B")
		if groups_number > 2:
			group_3_lottery.append("B")
		if groups_number > 3:
			group_4_lottery.append("B")
			if groups_number > 4:
				group_5_lottery.append("B")
			if groups_number > 5:
				group_6_lottery.append("B")
			if groups_number > 6:
				group_7_lottery.append("B")
			if groups_number > 7:
				group_8_lottery.append("B")
			if groups_number > 8:
				group_9_lottery.append("B")
			if groups_number > 9:
				group_10_lottery.append("B")
			if groups_number > 10:
				group_11_lottery.append("B")
			if groups_number > 11:
				group_12_lottery.append("B")
			if groups_number > 12:
				group_13_lottery.append("B")
			if groups_number > 13:
				group_14_lottery.append("B")
			if groups_number > 14:
				group_15_lottery.append("B")
			if groups_number > 15:
				group_16_lottery.append("B")
	len_doovr = len(group_1_lottery) / 2
	len_doovr = int(len_doovr)
	if len(group_1_lottery) == 11 or len(group_1_lottery) == 12:
		period_1 = [[1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]]
		period_2 = [[11, 1], [10, 12], [2, 9], [8, 3], [4, 7], [6, 5]]
		period_3 = [[1, 10], [9, 11], [12, 8], [7, 2], [3, 6], [5, 4]]
		period_4 = [[9, 1], [8, 10], [6, 12], [11, 7], [2, 5], [4, 3]]
		period_5 = [[1, 8], [7, 9], [12, 4], [10, 6], [5, 11], [3, 2]]
		period_6 = [[7, 1], [6, 8], [9, 5], [2, 12], [4, 10], [11, 3]]
		period_7 = [[1, 6], [5, 7], [8, 4], [3, 9], [12, 11], [10, 2]]
		period_8 = [[5, 1], [6, 4], [7, 3], [2, 8], [9, 12], [11, 10]]
		period_9 = [[1, 4], [5, 3], [2, 6], [12, 7], [8, 11], [10, 9]]
		period_10 = [[3, 1], [4, 2], [5, 12], [11, 6], [7, 10], [9, 8]]
		period_11 = [[1, 2], [12, 3], [11, 4], [5, 10], [6, 9], [7, 8]]
	if len(group_1_lottery) == 9 or len(group_1_lottery) == 10:
		period_1 = [[1, 10], [2, 9], [3, 8], [7, 4], [5, 6]]
		period_2 = [[9, 1], [8, 10], [2, 7], [6, 3], [4, 5]]
		period_3 = [[1, 8], [7, 9], [10, 6], [5, 2], [3, 4]]
		period_4 = [[7, 1], [6, 8], [4, 10], [9, 5], [2, 3]]
		period_5 = [[1, 6], [5, 7], [10, 2], [8, 4], [3, 9]]
		period_6 = [[5, 1], [4, 6], [9, 10], [2, 8], [7, 3]]
		period_7 = [[1, 4], [3, 5], [6, 2], [10, 7], [8, 9]]
		period_8 = [[3, 1], [4, 2], [5, 10], [9, 6], [7, 8]]
		period_9 = [[1, 2], [10, 3], [9, 4], [8, 5], [6, 7]]
	if len(group_1_lottery) == 7 or len(group_1_lottery) == 8:
		period_1 = [[1, 8], [2, 7], [6, 3], [4, 5]]
		period_2 = [[7, 1], [6, 8], [5, 2], [3, 4]]
		period_3 = [[1, 6], [7, 5], [8, 4], [2, 3]]
		period_4 = [[5, 1], [4, 6], [3, 7], [8, 2]]
		period_5 = [[1, 4], [5, 3], [6, 2], [7, 8]]
		period_6 = [[3, 1], [2, 4], [8, 5], [7, 6]]
		period_7 = [[1, 2], [8, 3], [4, 7], [6, 5]]
	if len(group_1_lottery) == 5 or len(group_1_lottery) == 6:
		period_1 = [[1, 6], [2, 5], [3, 4]]
		period_2 = [[5, 1], [6, 4], [2, 3]]
		period_3 = [[4, 1], [3, 5], [6, 2]]
		period_4 = [[1, 3], [4, 2], [5, 6]]
		period_5 = [[2, 1], [6, 3], [5, 4]]
	if len(group_1_lottery) == 3 or len(group_1_lottery) == 4:
		period_1 = [[1, 4], [2, 3]]
		period_2 = [[3, 1], [4, 2]]
		period_3 = [[1, 2], [3, 4]]

	yekom = []
	dovom = []
	sevvom = []
	chaharom = []
	panjom = []
	shishom = []
	haftom = []
	hashtom = []
	nohom = []
	dahom = []
	yazdahom = []
	list_0 = []
	#list1 = []

	if len(group_1_lottery) >= 4:
		# دور یکم
		for i in range(0, len_doovr):
			a1 = period_1[i][0]
			b1 = period_1[i][1]
			team1 = group_1_lottery[a1 - 1]
			team2 = group_1_lottery[b1 - 1]
			list_0.append(team1)
			list_0.append(team2)
			tuple1 = tuple(list_0)
			yekom.append(tuple1)
			list_0.clear()
		# دور دوم
		for i in range(0, len_doovr):
			a2 = period_2[i][0]
			b2 = period_2[i][1]
			team1 = group_1_lottery[a2 - 1]
			team2 = group_1_lottery[b2 - 1]
			list_0.append(team1)
			list_0.append(team2)
			tuple1 = tuple(list_0)
			dovom.append(tuple1)
			list_0.clear()
			
			
		# دور سوم
		for i in range(0, len_doovr):
			a3 = period_3[i][0]
			b3 = period_3[i][1]
			team1 = group_1_lottery[a3 - 1]
			team2 = group_1_lottery[b3 - 1]
			list_0.append(team1)
			list_0.append(team2)
			tuple1 = tuple(list_0)
			sevvom.append(tuple1)
			list_0.clear()
			
		if len(group_1_lottery) >= 5:
			# دور چهاروم
			for i in range(0, len_doovr):
				a4 = period_4[i][0]
				b4 = period_4[i][1]
				team1 = group_1_lottery[a4 - 1]
				team2 = group_1_lottery[b4 - 1]
				list_0.append(team1)
				list_0.append(team2)
				tuple1 = tuple(list_0)
				chaarom.append(tuple1)
				list_0.clear()
				
			# دور پپنجم
			for i in range(0, len_doovr):
				a5 = period_5[i][0]
				b5 = period_5[i][1]
				team1 = group_1_lottery[a5 - 1]
				team2 = group_1_lottery[b5 - 1]
				list_0.append(team1)
				list_0.append(team2)
				tuple1 = tuple(list_0)
				panjom.append(tuple1)
				list_0.clear()
				
			if len(group_1_lottery) >= 7:
				# دور ششم
				for i in range(0, len_doovr):
					a6 = period_6[i][0]
					b6 = period_6[i][1]
					team1 = group_1_lottery[a6 - 1]
					team2 = group_1_lottery[b6 - 1]
					list_0.append(team1)
					list_0.append(team2)
					tuple1 = tuple(list_0)
					sheshom.append(tuple1)
					list_0.clear()
					
				# دور هفتم
				for i in range(0, len_doovr):
					a7 = period_7[i][0]
					b7 = period_7[i][1]
					team1 = group_1_lottery[a7 - 1]
					team2 = group_1_lottery[b7 - 1]
					list_0.append(team1)
					list_0.append(team2)
					tuple1 = tuple(list_0)
					haftom.append(tuple1)
					list_0.clear()
					
				if len(group_1_lottery) >= 9:
					# دور هشتم
					for i in range(0, len_doovr):
						a8 = period_8[i][0]
						b8 = period_8[i][1]
						team1 = group_1_lottery[a8 - 1]
						team2 = group_1_lottery[b8 - 1]
						list_0.append(team1)
						list_0.append(team2)
						tuple1 = tuple(list_0)
						hashtom.append(tuple1)
						list_0.clear()
					# دور نهم
					for i in range(0, len_doovr):
						a9 = period_9[i][0]
						b9 = period_9[i][1]
						team1 = group_1_lottery[a9 - 1]
						team2 = group_1_lottery[b9 - 1]
						list_0.append(team1)
						list_0.append(team2)
						tuple1 = tuple(list_0)
						nohom.append(tuple1)
						list_0.clear()
					if len(group_1_lottery) >= 11:
						for i in range(0, len_doovr):
							a10 = period_10[i][0]
							b10 = period_10[i][1]
							team1 = group_1_lottery[a10 - 1]
							team2 = group_1_lottery[b10 - 1]
							list_0.append(team1)
							list_0.append(team2)
							tuple1 = tuple(list_0)
							dahom.append(tuple1)
							list_0.clear()
						# دور یازدهم
						for i in range(0, len_doovr):
							a11 = period_11[i][0]
							b11 = period_11[i][1]
							team1 = group_1_lottery[a11 - 1]
							team2 = group_1_lottery[b11 - 1]
							list_0.append(team1)
							list_0.append(team2)
							tuple1 = tuple(list_0)
							yazdahom.append(tuple1)
							list_0.clear()

	if len(group_1_lottery) == 4:
		return (yekom, dovom, sevvom)
	if len(group_1_lottery) == 6:
		return (yekom, dovom, sevvom, chaharom, panjom)
	if len(group_1_lottery) == 8:
		return (yekom, dovom, sevvom, chaharom, panjom, shishom, haftom)
	if len(group_1_lottery) == 10:
		return (yekom, dovom, sevvom, chaharom, panjom, shishom, haftom, hashtom, nohom)
	if len(group_1_lottery) == 12:
		return (yekom, dovom, sevvom, chaharom, panjom, shishom, haftom, hashtom, nohom, dahom, yazdahom)

#part_5 c


lottery_dbm = open('./DataBase/lottery_groups.txt', 'w', encoding='utf-8')
lottery_dbm.close()

khoroji_lattery_12 = output_lattery_4_12(group_1_lottery, lottery_dbm)

play_sound("./sounds/shuffle.mp3")

play_sound("./sounds/mail.mp3")



import os, time, ctypes
#ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

from os import environ
environ['pygame_hide_support_prompt'] = 'hide'
from pygame import mixer

mixer.init()


from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import semidbm
import pickle
import shutil
import playsound
from list_scopa import *
from saved_lists import *
from fanctions import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


global group_dict
try:
	db = semidbm.open('DataBase', 'c')
	group_dict = pickle.loads(db['group_dict'])
	db.close()


except:
	db = semidbm.open('DataBase', 'c')
	db['group_dict'] = pickle.dumps(group_dict)
	db.close()

#window_3
class Edit_Tables(QWidget):

	def __init__(self, parent=None):
		"""Initializer."""
		super().__init__(parent)

		window.hide()
		self.m = None
		self.p3 = None
		self.setWindowTitle('بخش ویرایش اطلاعات جام')
		self.setAccessibleName('بخش ویرایش اطلاعات جام')
		self.setGeometry(100, 100, 550, 420)
		page_3 = QGridLayout()
		self.setLayout(page_3)

		db = semidbm.open('DataBase', 'c')
		group_dict = pickle.loads(db['group_dict'])
		db.close()
		play_sound("./sounds/intercept.mp3")

		self.listGroupe = ['group_1_list', 'group_2_list', 'group_3_list', 'group_4_list', 'group_5_list',
						   'group_6_list', 'group_7_list', 'group_8_list', 'group_9_list', 'group_10_list', 'group_11_list', 'group_12_list', 'group_13_list', 'group_14_list', 'group_15_list', 'group_16_list']
		self.copyListGroupe = ['copy_group_1_list', 'copy_group_2_list', 'copy_group_3_list', 'copy_group_4_list', 'copy_group_5_list', 'copy_group_6_list', 'copy_group_7_list', 'copy_group_8_list', 'copy_group_9_list', 'copy_group_10_list', 'copy_group_11_list', 'copy_group_12_list', 'copy_group_13_list', 'copy_group_14_list', 'copy_group_15_list', 'copy_group_16_list']
		self.latarryList = ['group_1_lottery', 'group_2_lottery', 'group_3_lottery', 'group_4_lottery', 'group_5_lottery', 'group_6_lottery', 'group_7_lottery', 'group_8_lottery', 'group_9_lottery', 'group_10_lottery', 'group_11_lottery', 'group_12_lottery', 'group_13_lottery', 'group_14_lottery', 'group_15_lottery', 'group_16_lottery']
		self.gameTeam = ['game_team_grupe_1', 'game_team_grupe_2', 'game_team_grupe_3', 'game_team_grupe_4', 'game_team_grupe_5', 'game_team_grupe_6', 'game_team_grupe_7', 'game_team_grupe_8', 'game_team_grupe_9', 'game_team_grupe_10', 'game_team_grupe_11', 'game_team_grupe_12', 'game_team_grupe_13', 'game_team_grupe_14', 'game_team_grupe_15', 'game_team_grupe_16']

		self.baziMizban = ['bazi_mizban_1', 'bazi_mizban_2', 'bazi_mizban_3', 'bazi_mizban_4', 'bazi_mizban_5',
						   'bazi_mizban_6', 'bazi_mizban_7', 'bazi_mizban_8', 'bazi_mizban_9', 'bazi_mizban_10', 'bazi_mizban_11', 'bazi_mizban_12', 'bazi_mizban_13', 'bazi_mizban_14', 'bazi_mizban_15', 'bazi_mizban_16']
		self.baziMihman = ['bazi_mihman_1', 'bazi_mihman_2', 'bazi_mihman_3', 'bazi_mihman_4', 'bazi_mihman_5',
						   'bazi_mihman_6', 'bazi_mihman_7', 'bazi_mihman_8', 'bazi_mihman_9', 'bazi_mihman_10', 'bazi_mihman_11', 'bazi_mihman_12', 'bazi_mihman_13', 'bazi_mihman_14', 'bazi_mihman_15', 'bazi_mihman_16']
		self.natijehMizban = ['natijeh_bazi_mizban_1', 'natijeh_bazi_mizban_2', 'natijeh_bazi_mizban_3',
							  'natijeh_bazi_mizban_4', 'natijeh_bazi_mizban_5', 'natijeh_bazi_mizban_6',
							  'natijeh_bazi_mizban_7', 'natijeh_bazi_mizban_8', 'natijeh_bazi_mizban_9', 'natijeh_bazi_mizban_10', 'natijeh_bazi_mizban_11', 'natijeh_bazi_mizban_12', 'natijeh_bazi_mizban_13', 'natijeh_bazi_mizban_14', 'natijeh_bazi_mizban_15', 'natijeh_bazi_mizban_16']
		self.natijehMihman = ['natijeh_bazi_mihman_1', 'natijeh_bazi_mihman_2', 'natijeh_bazi_mihman_3',
							  'natijeh_bazi_mihman_4', 'natijeh_bazi_mihman_5', 'natijeh_bazi_mihman_6',
							  'natijeh_bazi_mihman_7', 'natijeh_bazi_mihman_8', 'natijeh_bazi_mihman_9', 'natijeh_bazi_mihman_10', 'natijeh_bazi_mihman_11', 'natijeh_bazi_mihman_12', 'natijeh_bazi_mihman_13', 'natijeh_bazi_mihman_14', 'natijeh_bazi_mihman_15', 'natijeh_bazi_mihman_16']
		self.scopaMizban = ['scopa_mizban_1', 'scopa_mizban_2', 'scopa_mizban_3', 'scopa_mizban_4', 'scopa_mizban_5',
							'scopa_mizban_6', 'scopa_mizban_7', 'scopa_mizban_8', 'scopa_mizban_9', 'scopa_mizban_10', 'scopa_mizban_11', 'scopa_mizban_12', 'scopa_mizban_13', 'scopa_mizban_14', 'scopa_mizban_15', 'scopa_mizban_16']
		self.scopaMihman = ['scopa_mihman_1', 'scopa_mihman_2', 'scopa_mihman_3', 'scopa_mihman_4', 'scopa_mihman_5',
							'scopa_mihman_6', 'scopa_mihman_7', 'scopa_mihman_8', 'scopa_mihman_9', 'scopa_mihman_10', 'scopa_mihman_11', 'scopa_mihman_12', 'scopa_mihman_13', 'scopa_mihman_14', 'scopa_mihman_15', 'scopa_mihman_16']

		self.p3_lable_1 = QLabel('کدام بخش از جدول جام را میخواهید ویرایش کنید؟:')
		self.p3_lable_1.setGeometry(160, 50, 230, 21)
		page_3.addChildWidget(self.p3_lable_1)

		self.cb0_3 = QComboBox()
		self.cb0_3.setAccessibleName('کدام بخش از جدول جام را میخواهید ویرایش کنید؟')
		self.cb0_3.addItems(['ویرایش جدول گروه ها', 'ویرایش جدول امتیاز', 'ویرایش نام جام', 'حذف همه داده های جام'])
		self.cb0_3.activated.connect(self.Show)
		self.cb0_3.setGeometry(200, 80, 150, 20)
		page_3.addChildWidget(self.cb0_3)

		self.btn_continiue3 = QPushButton('ادامه')
		self.btn_continiue3.setAccessibleName('ادامه')
		self.btn_continiue3.setGeometry(180, 120, 80, 25)
		self.btn_continiue3.setDefault(True)
		self.btn_continiue3.clicked.connect(self.continiue_3)
		page_3.addChildWidget(self.btn_continiue3)

		self.p3_btn_cancel = QPushButton('انصراف')
		self.p3_btn_cancel.setAccessibleName('انصراف')
		self.p3_btn_cancel.setGeometry(270, 120, 80, 25)
		self.p3_btn_cancel.setDefault(True)
		self.p3_btn_cancel.clicked.connect(self.close_window3)
		page_3.addChildWidget(self.p3_btn_cancel)

		self.list_grope3 = group_dict['groups_name']
		if len(self.list_grope3) == 1:
			self.list_grope3 = ['گروه A', 'انتخاب گروه ']

		self.cb1_3 = QComboBox()
		self.cb1_3.setAccessibleName('انتخاب نام گروه')
		self.cb1_3.addItems(self.list_grope3)
		self.cb1_3.activated.connect(self.Showv1)
		self.cb1_3.setGeometry(200, 80, 150, 20)
		page_3.addChildWidget(self.cb1_3)
		self.cb1_3.hide()

		self.p3_lable_2 = QLabel('جدول کدام  گروه را میخواهید ویرایش کنید؟')
		self.p3_lable_2.setGeometry(175, 50, 200, 20)

		page_3.addChildWidget(self.p3_lable_2)
		self.p3_lable_2.hide()



		self.btn_co_3a = QPushButton('ادامه')
		self.btn_co_3a.setAccessibleName('ادامه')
		self.btn_co_3a.setGeometry(180, 120, 80, 25)
		self.btn_co_3a.setDefault(True)
		self.btn_co_3a.clicked.connect(self.continiue_3a)
		page_3.addChildWidget(self.btn_co_3a)
		self.btn_co_3a.hide()


		#edit a3
		self.p3_lable_3 = QLabel('نام تیم را جهت ویرایش انتخاب کنید')
		self.p3_lable_3.setGeometry(175, 50, 200, 20)
		page_3.addChildWidget(self.p3_lable_3)
		self.p3_lable_3.hide()



		self.cb2_3 = QComboBox()
		self.cb2_3.setAccessibleName('انتخاب نام تیم')
		self.cb2_3.activated.connect(self.Showv2)
		self.cb2_3.setGeometry(200, 80, 150, 20)
		page_3.addChildWidget(self.cb2_3)
		self.cb2_3.hide()

		self.btn_co_3b = QPushButton('ادامه')
		self.btn_co_3b.setAccessibleName('ادامه')
		self.btn_co_3b.setGeometry(180, 120, 80, 25)
		self.btn_co_3b.setDefault(True)
		self.btn_co_3b.clicked.connect(self.continiue_3b)
		page_3.addChildWidget(self.btn_co_3b)
		self.btn_co_3b.hide()

		self.p3_lable_4 = QLabel('نام صحیح تیم  را وارد کنید')
		self.p3_lable_4.setGeometry(175, 50, 200, 20)
		page_3.addChildWidget(self.p3_lable_4)
		self.p3_lable_4.hide()

		self.editName = QLineEdit()
		self.editName.setAccessibleName('نام صحیح تیم را وارد کنید')
		self.editName.setGeometry(200, 90, 150, 20)
		page_3.addChildWidget(self.editName)
		self.editName.hide()

		self.btn_co_3c = QPushButton('ثبت')
		self.btn_co_3c.setAccessibleName('ثبت')
		self.btn_co_3c.setGeometry(180, 120, 80, 25)
		self.btn_co_3c.setDefault(True)
		self.btn_co_3c.clicked.connect(self.continiue_3c)
		page_3.addChildWidget(self.btn_co_3c)
		self.btn_co_3c.hide()

		#ویرایش امتیاز 1
		self.p3_lable_b1 = QLabel('جدول کدام  گروه را میخواهید ویرایش کنید؟')
		self.p3_lable_b1.setGeometry(175, 50, 200, 20)
		page_3.addChildWidget(self.p3_lable_b1)
		self.p3_lable_b1.hide()

		self.cb1_emtiyaz = QComboBox()
		self.cb1_emtiyaz.setAccessibleName('انتخاب نام گروه')
		self.cb1_emtiyaz.addItems(self.list_grope3)
		self.cb1_emtiyaz.activated.connect(self.Showv1)
		self.cb1_emtiyaz.setGeometry(200, 80, 150, 20)
		page_3.addChildWidget(self.cb1_emtiyaz)
		self.cb1_emtiyaz.hide()


		#تغییر امتیاز 2
		self.p3_lable_b2 = QLabel('نام تیم را جهت ویرایش امتیاز انتخاب کنید')
		self.p3_lable_b2.setGeometry(175, 50, 200, 20)
		page_3.addChildWidget(self.p3_lable_b2)
		self.p3_lable_b2.hide()

		self.p3_lable_b3 = QLabel('تیم میزبان:')
		self.p3_lable_b3.setGeometry(390, 80, 60, 20)
		page_3.addChildWidget(self.p3_lable_b3)
		self.p3_lable_b3.hide()

		self.p3_lable_b4 = QLabel('تیم میهمان:')
		self.p3_lable_b4.setGeometry(200, 80, 60, 20)
		page_3.addChildWidget(self.p3_lable_b4)
		self.p3_lable_b4.hide()


		self.cb2_emtiyaz = QComboBox()
		self.cb2_emtiyaz.setAccessibleName('انتخاب تیم میزبان')
		self.cb2_emtiyaz.activated.connect(self.Showv2)
		self.cb2_emtiyaz.setGeometry(290, 80, 100, 20)
		page_3.addChildWidget(self.cb2_emtiyaz)
		self.cb2_emtiyaz.hide()


		self.cb3_emtyaz = QComboBox()
		self.cb3_emtyaz.setAccessibleName('انتخاب تیم میهمان')
		self.cb3_emtyaz.activated.connect(self.Showv2)
		self.cb3_emtyaz.setGeometry(100, 80, 100, 20)
		page_3.addChildWidget(self.cb3_emtyaz)
		self.cb3_emtyaz.hide()

		self.btn_emtiyaz2 = QPushButton('ادامه')
		self.btn_emtiyaz2.setAccessibleName('ادامه')
		self.btn_emtiyaz2.setGeometry(180, 120, 80, 25)
		self.btn_emtiyaz2.setDefault(True)
		self.btn_emtiyaz2.clicked.connect(self.btn_e2)
		page_3.addChildWidget(self.btn_emtiyaz2)
		self.btn_emtiyaz2.hide()

		#دکمه انتخاب گروه
		self.btn_emtiyaz1 = QPushButton('ادامه')
		self.btn_emtiyaz1.setAccessibleName('ادامه')
		self.btn_emtiyaz1.setGeometry(180, 120, 80, 25)
		self.btn_emtiyaz1.setDefault(True)
		self.btn_emtiyaz1.clicked.connect(self.btn_e1)
		page_3.addChildWidget(self.btn_emtiyaz1)
		self.btn_emtiyaz1.hide()


		#ویرایش 2b
		self.p3_lable_1c = QLabel('امتیاز و اسکوپای صحیح را وارد کنید')
		self.p3_lable_1c.setGeometry(175, 50, 200, 20)
		page_3.addChildWidget(self.p3_lable_1c)
		self.p3_lable_1c.hide()

		self.p3_lable_2c = QLabel()
		self.p3_lable_2c.setGeometry(300, 90, 200, 20)
		page_3.addChildWidget(self.p3_lable_2c)
		self.p3_lable_2c.hide()

		self.p3_lable_3c = QLabel()
		self.p3_lable_3c.setText('امتیاز تیم میزبان')
		self.p3_lable_3c.setGeometry(400, 115, 90, 20)
		page_3.addChildWidget(self.p3_lable_3c)
		self.p3_lable_3c.hide()

		self.right_e_mizban = QLineEdit()
		self.right_e_mizban.setGeometry(300, 115, 80, 20)
		page_3.addChildWidget(self.right_e_mizban)
		self.right_e_mizban.hide()

		self.p3_lable_4c = QLabel()
		self.p3_lable_4c.setGeometry(300, 150, 200, 20)
		page_3.addChildWidget(self.p3_lable_4c)
		self.p3_lable_4c.hide()

		self.p3_lable_5c = QLabel('اسکوپای تیم میزبان:')
		self.p3_lable_5c.setGeometry(420, 180, 100, 20)
		page_3.addChildWidget(self.p3_lable_5c)
		self.p3_lable_5c.hide()

		self.right_s_mizban = QLineEdit()
		self.right_s_mizban.setGeometry(300, 180, 80, 20)
		page_3.addChildWidget(self.right_s_mizban)
		self.right_s_mizban.hide()

		self.p3_lable_6c = QLabel()
		self.p3_lable_6c.setGeometry(50, 90, 200, 20)
		page_3.addChildWidget(self.p3_lable_6c)
		self.p3_lable_6c.hide()

		self.p3_lable_7c = QLabel('امتیاز تیم میهمان:')
		self.p3_lable_7c.setGeometry(170, 115, 90, 20)
		page_3.addChildWidget(self.p3_lable_7c)
		self.p3_lable_7c.hide()

		self.right_e_mihman = QLineEdit()
		self.right_e_mihman.setGeometry(80, 115, 80, 20)
		page_3.addChildWidget(self.right_e_mihman)
		self.right_e_mihman.hide()

		self.p3_lable_8c = QLabel()
		self.p3_lable_8c.setGeometry(50, 150, 200, 20)
		page_3.addChildWidget(self.p3_lable_8c)
		self.p3_lable_8c.hide()

		self.p3_lable_9c = QLabel('اسکوپای تیم میهمان:')
		self.p3_lable_9c.setGeometry(170, 180, 100, 20)
		page_3.addChildWidget(self.p3_lable_9c)
		self.p3_lable_9c.hide()

		self.right_s_mihman = QLineEdit()
		self.right_s_mihman.setGeometry(80, 180, 80, 20)
		page_3.addChildWidget(self.right_s_mihman)
		self.right_s_mihman.hide()

		self.btn_1c = QPushButton('ثبت')
		self.btn_1c.setAccessibleName('ثبت')
		self.btn_1c.setGeometry(175, 240, 80, 25)
		self.btn_1c.setDefault(True)
		self.btn_1c.clicked.connect(self.b_1c)
		page_3.addChildWidget(self.btn_1c)
		self.btn_1c.hide()

		#,d\\ویرایس نام جام
		self.editNamCup = QLineEdit()
		self.editNamCup.setAccessibleName('نام صحیح جام را وارد کنید!')
		self.editNamCup.setGeometry(200, 100, 150, 20)
		page_3.addChildWidget(self.editNamCup)
		self.editNamCup.hide()

		self.p3_lable_1d = QLabel('نام صحیح جام را وارد کنید!')
		self.p3_lable_1d.setGeometry(200, 50, 150, 20)
		page_3.addChildWidget(self.p3_lable_1d)
		self.p3_lable_1d.hide()

		self.btn_1d = QPushButton('ثبت')
		self.btn_1d.setAccessibleName('ثبت')
		self.btn_1d.setGeometry(210, 140, 60, 25)
		self.btn_1d.setDefault(True)
		self.btn_1d.clicked.connect(self.save_name)
		page_3.addChildWidget(self.btn_1d)
		self.btn_1d.hide()

		self.p3_btn_back = QPushButton('بازگشت')
		self.p3_btn_back.setAccessibleName('بازگشت به منوی قبل')
		self.p3_btn_back.setGeometry(270, 120, 80, 25)
		self.p3_btn_back.setDefault(True)
		self.p3_btn_back.clicked.connect(self.back_a)
		page_3.addChildWidget(self.p3_btn_back)
		self.p3_btn_back.hide()

	#part_3 def
	def ex3(self):
		play_sound("./sounds/disconnect.mp3")
		exit()



	def back_a(self):
		play_sound("./sounds/mail.mp3")
		self.p3 = Edit_Tables()
		self.p3.show()
		window.hide()
		self.close()

	def Showv2(self):
		self.indx_team = self.cb2_3.currentIndex()
		self.mizbanName = self.cb2_emtiyaz.currentText()
		self.mizbanIndx = self.cb2_emtiyaz.currentIndex()
		self.mihmanName = self.cb3_emtyaz.currentText()
		self.mihmanIndx = self.cb3_emtyaz.currentIndex()

	def Showv1(self):
		self.indx_groupe = self.cb1_3.currentIndex()
		self.editIndxGroup = self.cb1_emtiyaz .currentIndex()
		self.editNameGroup = self.cb1_emtiyaz.currentText()
	def Show(self):
		self.selectCb0_3 = self.cb0_3.currentText()

	def continiue_3(self):
		play_sound("./sounds/mail.mp3")
		self.p3_lable_1.hide()
		self.cb0_3.hide()
		self.p3_btn_cancel.hide()
		self.btn_continiue3.hide()
		delete_data = 0
		ext = 0
		try:
			if self.selectCb0_3 == 'ویرایش جدول گروه ها':
				if len(group_dict['cup_name']) == 0:
					play_sound("./sounds/questionmode.mp3")
					QMessageBox.about(self, "Warning!",
									  'اطلاعاتی برای ویرایش وجود ندارد. \n برای دسترسی به بخش ویرایش  ابتدا باید جدول امتیاز تکمیل شود!')
					play_sound("./sounds/mail.mp3")
					self.p3 = Edit_Tables()
					self.p3.show()
					window.hide()
					self.close()
				self.p3_lable_2.show()
				self.cb1_3.show()
				self.btn_co_3a.show()
				self.p3_btn_back.show()

			if self.selectCb0_3 == 'ویرایش جدول امتیاز':
				self.p3_lable_b1.show()
				self.cb1_emtiyaz.show()
				self.btn_emtiyaz1.show()
				self.p3_btn_cancel.hide()
				self.p3_btn_back.show()

			if self.selectCb0_3 == 'ویرایش نام جام':
				self.p3_lable_1.hide()
				self.cb0_3.hide()
				self.p3_btn_cancel.hide()
				self.btn_continiue3.hide()
				self.p3_btn_back.show()
				self.p3_btn_back.setGeometry(280, 140, 60, 25)
				self.editNamCup.show()
				self.p3_lable_1d.show()
				self.btn_1d.show()
			if self.selectCb0_3 == 'حذف همه داده های جام':
				delete_data = 1


				self.close
		except:
			play_sound("./sounds/questionmode.mp3")
			QMessageBox.about(self, "Warning!",
							  'از میان گزینه های موجود یکی را انتخاب کنید!')
			play_sound("./sounds/mail.mp3")
			return 

		if delete_data == 1:
			play_sound("./sounds/questionmode.mp3")

			self.msg = QMessageBox()
			self.msg.setWindowTitle('Warning!')

			self.msg.setText('با تایید شما تمام داده های جام حذف میشود. \n برای تایید دکمه Yes را کلیک کنید.')
			self.msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
			execute = self.msg.exec()
			if execute == QMessageBox.StandardButton.Yes:
				try:
					shutil.rmtree("./DataBase")
					play_sound("./sounds/filetx_complete.mp3")

					QMessageBox.about(self, 'about', 'فایل پایگاه داده با موفقیت حذف شد. برنامه را دوباره راه اندازی کنید.')
					ext = 1
				except:
					play_sound("./sounds/rpause.mp3")
					QMessageBox.about(self, 'about', 'فایل در حال اجراست. \n ابتدا پوشه DataBase را ببندید  یا برنامه را دوباره راه اندازی کنید و برای حذف داده های جام دوباره سعی کنید.')
					play_sound("./sounds/mute_all.mp3")
					self.p3 = Edit_Tables()
					self.p3.show()
					window.hide
					self.close

			if execute == QMessageBox.StandardButton.No:
				return

		if ext == 1:
			play_sound("./sounds/disconnect.mp3")
			exit()

	#part_3 def
	def close_window3(self):
		self.m = MainWindow()
		self.m.show()
		window.hide()
		self.close()

	def continiue_3a(self):
		play_sound("./sounds/mail.mp3")
		db = semidbm.open('DataBase', 'c')
		group_dict = pickle.loads(db['group_dict'])
		db.close()
		self.p3_lable_2.hide()
		self.cb1_3.hide()
		self.btn_co_3a.hide()
		self.p3_btn_back.hide()
		self.p3_lable_3.show()
		self.cb2_3.show()
		self.btn_co_3b.show()
		self.p3_btn_back.show()

		try:
			self.g_n = self.listGroupe[self.indx_groupe]
		except:
			play_sound("./sounds/rpause.mp3")
			QMessageBox.about(self, 'خطا!', 'ابتدا نام گروه را مشخص کنید.')
			play_sound("./sounds/mute_all.mp3")
			return
		self.list_g = group_dict[self.g_n]
		self.cb2_3.addItems(self.list_g)

	def continiue_3b(self):
		play_sound("./sounds/mail.mp3")
		self.p3_lable_3.hide()
		self.cb2_3.hide()
		self.btn_co_3b.hide()
		self.p3_btn_back.show()
		self.p3_lable_4.show()
		self.editName.show()
		self.btn_co_3c.show()

	def continiue_3c(self):
		play_sound("./sounds/mail.mp3")
		db = semidbm.open('DataBase', 'c')
		group_dict = pickle.loads(db['group_dict'])
		db.close()

		name = self.editName.text()
		try:
			self.indx_team = self.cb2_3.currentIndex()
		except:
			play_sound("./sounds/rpause.mp3")
			QMessageBox.about(self, 'خطا!', 'ابتدا نام تیم را مشخص کنید.')
			play_sound("./sounds/mute_all.mp3")
			return

		g_n = self.listGroupe[self.indx_groupe]
		copy_g_n = self.copyListGroupe[self.indx_groupe]
		latty = self.latarryList[self.indx_groupe]
		g_t = self.gameTeam[self.indx_groupe]


		list_g = group_dict[g_n]
		copylist_g = group_dict[copy_g_n]
		listL_t = group_dict[latty]
		listG_t = group_dict[g_t]

		deleted_team = list_g[self.indx_team]
		list_g.pop(self.indx_team)
		copylist_g.pop(self.indx_team)
		listL_t.pop(self.indx_team)
		list_g.insert(self.indx_team, name)
		copylist_g.insert(self.indx_team, name)
		listL_t.insert(self.indx_team, name)
		
		a = 0
		for i in group_dict['all_teamss']:
			if i == deleted_team:
				group_dict['all_teamss'].pop(a)
				group_dict['all_teamss'].insert(a, name)
			a += 1
		d = 0
		for i in listG_t:
			if i == deleted_team:
				listG_t.pop(d)
				listG_t.insert(d, name)
			d += 1

		group_dict[g_n] = list_g
		group_dict[copy_g_n] = copylist_g
		group_dict[latty] = listL_t
		group_dict[g_t] = listG_t

		db = semidbm.open('DataBase', 'c')
		db['group_dict'] = pickle.dumps(group_dict)
		db.close()

		db = semidbm.open('DataBase', 'c')
		group_dict = pickle.loads(db['group_dict'])
		db.close()
		play_sound("./sounds/videosession.mp3")
		QMessageBox.about(self, 'about', f'عملیات با موفقیت انجام شد. \n تیم {name} جایگزین تیم {deleted_team} شد.')
		play_sound("./sounds/mute_all.mp3")

		self.m = MainWindow()
		self.m.show()
		window.hide()
		self.close()


	def btn_e1(self):
		self.p3_lable_b1.hide()
		self.cb1_emtiyaz.hide()
		self.btn_emtiyaz1.hide()
		self.p3_lable_b2.show()
		self.cb2_emtiyaz.show()
		self.cb3_emtyaz.show()
		self.btn_emtiyaz2.show()
		self.p3_btn_cancel.show()
		self.p3_lable_b3.show()
		self.p3_lable_b4.show()

		try:
			g_n = self.listGroupe[self.editIndxGroup]
			if len(self.list_grope3) == 1:
				g_n = ['گروه A', 'انتخاب گروه ']
			addList = group_dict[g_n]
			self.cb2_emtiyaz.addItems(addList)
			self.cb3_emtyaz.addItems(addList)
		except:
			pass
			#QMessageBox.about(self, 'خطای ورودی!', ابتدا نام گروه را مشخص کنید!)


	def btn_e2(self):
		
		db = semidbm.open('DataBase', 'c')
		group_dict = pickle.loads(db['group_dict'])
		db.close()
		mizban_b = self.baziMizban[self.editIndxGroup]
		mizban_n = self.natijehMizban[self.editIndxGroup]
		mihman_b = self.baziMihman[self.editIndxGroup]
		mihman_n = self.natijehMihman[self.editIndxGroup]
		mizban_s = self.scopaMizban[self.indx_groupe]
		mihman_s = self.scopaMihman[self.indx_groupe]

		try:
			if self.mizbanName == self.mihmanName:
				play_sound("./sounds/rpause.mp3")
				QMessageBox.about(self, 'about', 'نام تیم میزبان و تیم میهمان نباید مشابه باشد!')
				play_sound("./sounds/mail.mp3")
				return
		except:
			play_sound("./sounds/rpause.mp3")
			QMessageBox.about(self, 'about', 'ابتدا تیم میزبان و تیم میهمان را مشخص کنید!')
			play_sound("./sounds/mail.mp3")
			return


		tool = len(group_dict['bazi_mizban_1'])

		mizbanName = self.mizbanName
		mihmanName = self.mihmanName
		self.mizbanBazi = group_dict[mizban_b]
		self.mihmanBazi = group_dict[mihman_b]
		doovr = 0
		for i in range(0, tool):
			if self.mizbanName in self.mizbanBazi[doovr]:
				if self.mihmanName in self.mihmanBazi[doovr]:
					self.mizban_e_n = group_dict[mizban_n][doovr]
					self.mihman_e_n = group_dict[mihman_n][doovr]

					self.mizban_s = group_dict[mizban_s][doovr]
					self.mihman_s = group_dict[mihman_s][doovr]
			doovr += 1

		try:
			# self.p3_lable_2c.setText(f'امتیاز تیم {self.mizban_e_n} ، {self.mizban_t} میباشد.')
			self.p3_lable_2c.setText(f'امتیاز تیم {self.mizbanName} ، {self.mizban_e_n} میباشد.')
			self.p3_lable_6c.setText(f'امتیاز تیم {self.mihmanName} ، {self.mihman_e_n} میباشد.')
			self.p3_lable_8c.setText(f'تعداد اسکوپای تیم {self.mihmanName} ، {self.mihman_s} میباشد.')
			self.p3_lable_4c.setText(f'تعداد اسکوپای تیم {mizbanName} ، self.{mizban_s} میباشد.')
			self.right_e_mizban.setAccessibleName(
				f'امتیاز تیم {self.mizbanName} ، {self.mizban_e_n} میباشد. امتیاز صحیح را وارد کنید.')
			self.right_e_mihman.setAccessibleName(
				f'امتیاز تیم {self.mihmanName} ، {self.mihman_e_n} میباشد. امتیاز صحیح را وارد کنید.')
			self.right_s_mihman.setAccessibleName(
				f'تعداد اسکوپای تیم {self.mihmanName} ، {self.mihman_s} میباشد. امتیاز صحیح را وارد کنید.')
			self.right_s_mizban.setAccessibleName(
				f'تعداد اسکوپای تیم {self.mizbanName} ، {self.mizban_s} میباشد. امتیاز صحیح را وارد کنید.')

			self.p3_lable_b2.hide()
			self.cb2_emtiyaz.hide()
			self.cb3_emtyaz.hide()
			self.btn_emtiyaz2.hide()
			self.p3_btn_cancel.hide()
			self.p3_btn_back.show()
			self.p3_btn_back.setGeometry(270, 240, 80, 25)
			self.p3_lable_b3.hide()
			self.p3_lable_b4.hide()
			self.p3_lable_1c.show()
			self.p3_lable_2c.show()
			self.p3_lable_3c.show()
			self.right_e_mizban.show()
			self.p3_lable_4c.show()
			self.p3_lable_5c.show()
			self.right_s_mizban.show()

			self.p3_lable_6c.show()
			self.p3_lable_7c.show()
			self.right_e_mihman.show()
			self.p3_lable_8c.show()
			self.p3_lable_9c.show()
			self.right_s_mihman.show()
			self.btn_1c.show()

		except:
			play_sound("./sounds/rpause.mp3")
			QMessageBox.about(self, 'خطای ورودی!', f' {self.mizbanName} بع عنوان تیم میزبان و   {self.mihmanName} بعنوان تیم میهمانتا کنون مسابقه ای انجام نداده اند!')
			play_sound("./sounds/mute_all.mp3")
			return

	def b_1c(self):
		try:
			emtyazMizban = int(self.right_e_mizban.text())
			scopaMizban = int(self.right_s_mizban.text())
			emtiyazMihman = int(self.right_e_mihman.text())
			scopaMihman = int(self.right_s_mihman.text())
		except:
			play_sound("./sounds/rpause.mp3")
			QMessageBox.about(self, 'خطای ورودی', 'مقادیر را بصورت عدد صحیح وارد کنید!')
			play_sound("./sounds/mute_all.mp3")
			return

		db = semidbm.open('DataBase', 'c')
		group_dict = pickle.loads(db['group_dict'])
		db.close()

		mizban_n = self.natijehMizban[self.editIndxGroup]
		mihman_n = self.natijehMihman[self.editIndxGroup]
		mizban_s = self.scopaMizban[self.indx_groupe]
		mihman_s = self.scopaMihman[self.indx_groupe]

		mizban_b = self.baziMizban[self.editIndxGroup]
		mihman_b = self.baziMihman[self.editIndxGroup]
		tool = len(group_dict['bazi_mizban_1'])
		doovr = 0
		for i in range(0, tool):
			if self.mizbanName in group_dict[mizban_b][doovr]:
				if self.mihmanName in group_dict[mihman_b][doovr]:
					group_dict[mizban_n].pop(doovr)
					group_dict[mizban_n].insert(doovr, emtyazMizban)
					group_dict[mihman_n].pop(doovr)
					group_dict[mihman_n].insert(doovr, emtiyazMihman)
					group_dict[mizban_s].pop(doovr)
					group_dict[mizban_s].insert(doovr, scopaMizban)
					group_dict[mihman_s].pop(doovr)
					group_dict[mihman_s].insert(doovr, scopaMihman)

			doovr += 1

		db = semidbm.open('DataBase', 'c')
		db['group_dict'] = pickle.dumps(group_dict)
		db.close()

		play_sound("./sounds/videosession.mp3")
		QMessageBox.about(self, 'about', 'ویرایش امتیاز و اسکوپا با موفقیت انجام شد.')
		play_sound("./sounds/mail.mp3")

		self.m = MainWindow()
		self.m.show()
		window.hide()
		self.close()

	def save_name(self):
		namejam = self.editNamCup.text()
		group_dict['cup_name'] = namejam
		db = semidbm.open('DataBase', 'c')
		db['group_dict'] = pickle.dumps(group_dict)
		db.close()

		play_sound("./sounds/videosession.mp3")
		QMessageBox.about(self, 'about', 'نام جام با موفقیت تغییر یافت!')
		play_sound("./sounds/mail.mp3")
		self.m = MainWindow()
		self.m.show()
		window.hide()
		self.close()

# part_2
# window_2
class Score_Table(QWidget):
	def __init__(self, parent=None):
		"""Initializer."""
		super().__init__(parent)
		window.hide()

		self.m2 = None
		self.p2 = None
		self.setWindowTitle('بخش ورود نتیجه بازیها')
		self.setAccessibleName('بخش ورود نتیجه بازیها به جدول امتیازها')
		self.setGeometry(100, 100, 550, 420)
		page_2 = QGridLayout()
		window.hide()
		self.setLayout(page_2)
		play_sound("./sounds/replay.wav")

		db = semidbm.open('DataBase', 'c')
		group_dict = pickle.loads(db['group_dict'])
		db.close()

		self.group_dict = group_dict

		self.list_g = group_dict['groups_name']
		if len(self.list_g) == 1:
			self.list_g = ['گروه A', 'انتخاب گروه']
		self.listGroupe = ['group_1_list', 'group_2_list', 'group_3_list', 'group_4_list', 'group_5_list',
						   'group_6_list', 'group_7_list', 'group_8_list', 'group_9_list', 'group_10_list', 'group_11_list', 'group_12_list', 'group_13_list', 'group_14_list', 'group_15_list', 'group_16_list']
		self.gameTeam = ['game_team_grupe_1', 'game_team_grupe_2', 'game_team_grupe_3', 'game_team_grupe_4', 'game_team_grupe_5', 'game_team_grupe_6', 'game_team_grupe_7', 'game_team_grupe_8', 'game_team_grupe_9', 'game_team_grupe_10', 'game_team_grupe_11', 'game_team_grupe_12', 'game_team_grupe_13', 'game_team_grupe_14', 'game_team_grupe_15', 'game_team_grupe_16']

		self.p2_lable_1 = QLabel('نام گروه را انتخاب کنید:')
		self.p2_lable_1.setGeometry(270, 50, 110, 20)
		page_2.addChildWidget(self.p2_lable_1)

		self.cb0 = QComboBox()
		self.cb0.setAccessibleName('انتخاب نام گروه')
		self.cb0.addItems(self.list_g)
		self.cb0.activated.connect(self.Show)
		self.cb0.setGeometry(160, 50, 100, 20)
		page_2.addChildWidget(self.cb0)

		# self.cb0.setStyleSheet('background-color: rgb(10, 10, 10);')

		self.p2_lable_2 = QLabel('تیم میزبان:')
		self.p2_lable_2.setGeometry(415, 90, 60, 20)
		self.p2_lable_2.hide()
		page_2.addChildWidget(self.p2_lable_2)

		self.cb2 = QComboBox()
		self.cb2.setAccessibleName('انتخاب تی میزبان')
		self.cb2.activated.connect(self.Show2)
		self.cb2.setGeometry(305, 90, 100, 20)
		page_2.addChildWidget(self.cb2)
		self.cb2.hide()

		self.p2_lable_3 = QLabel('تیم میهمان:')
		self.p2_lable_3.setGeometry(185, 90, 60, 20)
		self.p2_lable_3.hide()
		page_2.addChildWidget(self.p2_lable_3)

		self.cb3 = QComboBox()
		self.cb3.setAccessibleName('انتخاب تیم میهمان')
		self.cb3.activated.connect(self.Show3)
		self.cb3.setGeometry(75, 90, 100, 20)
		self.cb3.hide()
		page_2.addChildWidget(self.cb3)

		self.p2_lable_4 = QLabel('امتیاز تیم میزبان:')
		self.p2_lable_4.setGeometry(370, 160, 80, 20)
		self.p2_lable_4.hide()
		page_2.addChildWidget(self.p2_lable_4)

		self.scoreMizban = QLineEdit()
		self.scoreMizban.setAccessibleName('امتیاز تیم میزبان')
		self.scoreMizban.setGeometry(280, 160, 80, 20)
		self.scoreMizban.hide()
		page_2.addChildWidget(self.scoreMizban)

		self.p2_lable_5 = QLabel('تعداد اسکوپای تیم میزبان:')
		self.p2_lable_5.setGeometry(370, 190, 130, 20)
		self.p2_lable_5.hide()
		page_2.addChildWidget(self.p2_lable_5)

		self.scopaMizban = QLineEdit()
		self.scopaMizban.setAccessibleName('تعداد اسکوپای تیم میزبان')
		self.scopaMizban.setGeometry(280, 190, 80, 20)
		self.scopaMizban.hide()
		page_2.addChildWidget(self.scopaMizban)

		self.p2_lable_6 = QLabel('امتیاز تیم میهمان:')
		self.p2_lable_6.setGeometry(140, 160, 90, 20)
		self.p2_lable_6.hide()
		page_2.addChildWidget(self.p2_lable_6)

		self.emtiyazMihman = QLineEdit()
		self.emtiyazMihman.setAccessibleName('امتیاز تیم میهمان')
		self.emtiyazMihman.setGeometry(50, 160, 80, 20)
		self.emtiyazMihman.hide()
		page_2.addChildWidget(self.emtiyazMihman)

		self.p2_lable_7 = QLabel('تعداد اسکوپای تیم میهمان:')
		self.p2_lable_7.setGeometry(140, 190, 130, 20)
		self.p2_lable_7.hide()
		page_2.addChildWidget(self.p2_lable_7)

		self.scopaMihman = QLineEdit()
		self.scopaMihman.setAccessibleName('تعداد اسکوپای تیم میهمان')
		self.scopaMihman.setGeometry(50, 190, 80, 20)
		self.scopaMihman.hide()
		page_2.addChildWidget(self.scopaMihman)

		self.p2_btn_1 = QPushButton('ثبت و ادامه')
		self.p2_btn_1.setAccessibleName('ثبت و ادامه')
		self.p2_btn_1.setGeometry(50, 280, 80, 25)
		self.p2_btn_1.hide()
		self.p2_btn_1.setDefault(True)
		self.p2_btn_1.clicked.connect(self.clicked_1)
		self.p2_btn_1.clicked.connect(self.save)
		page_2.addChildWidget(self.p2_btn_1)

		self.p2_btn_2 = QPushButton('ثبت و بازگشت')
		self.p2_btn_2.setAccessibleName('ثبت و بازگشت به منوی اصلی')
		self.p2_btn_2.setGeometry(135, 280, 80, 25)
		self.p2_btn_2.hide()
		self.p2_btn_2.setDefault(True)
		self.p2_btn_2.clicked.connect(self.clicked_2)
		self.p2_btn_2.clicked.connect(self.save)
		page_2.addChildWidget(self.p2_btn_2)

		self.p2_btn_3 = QPushButton('انصراف')
		self.p2_btn_3.setAccessibleName('انصراف')
		self.p2_btn_3.setGeometry(220, 280, 80, 25)
		self.p2_btn_3.hide()
		self.p2_btn_3.setDefault(True)
		self.p2_btn_3.clicked.connect(self.close_window2)
		page_2.addChildWidget(self.p2_btn_3)

		self.btn_continiue = QPushButton('ادامه')
		self.btn_continiue.setAccessibleName('ادامه')
		self.btn_continiue.setGeometry(160, 90, 80, 25)
		self.btn_continiue.setDefault(True)
		self.btn_continiue.clicked.connect(self.continiue_btn)
		page_2.addChildWidget(self.btn_continiue)

		self.p2_btn_cancel = QPushButton('انصراف')
		self.p2_btn_cancel.setAccessibleName('انصراف')
		self.p2_btn_cancel.setGeometry(245, 90, 80, 25)
		self.p2_btn_cancel.setDefault(True)

		self.p2_btn_cancel.clicked.connect(self.close_window2)
		page_2.addChildWidget(self.p2_btn_cancel)

	def Show(self):
		self.selectCb0 = self.cb0.currentText()

	def clicked_1(self):
		self.clicked = 1

	def clicked_2(self):
		self.clicked = 2

	def continiue_btn(self):
		try:
			self.indx_0 = self.cb0.currentIndex()
			indx_1 = self.list_g.index(self.selectCb0)
		except:
			play_sound("./sounds/rpause.mp3")
			QMessageBox.about(self, 'خطا!', 'ابتدا نام گروه را انتخاب کنید!')
			return
		nameGrope = self.listGroupe[indx_1]
		self.addListCb2 = []
		self.addListCb2 = self.group_dict[nameGrope]

		self.cb2.addItems(self.addListCb2)
		self.cb3.addItems(self.addListCb2)

		self.p2_btn_cancel.hide()
		self.p2_lable_1.hide()
		self.cb0.hide()
		self.btn_continiue.hide()
		self.p2_lable_2.show()
		self.cb2.show()
		self.p2_lable_3.show()
		self.cb3.show()
		self.p2_lable_4.show()
		self.scoreMizban.show()
		self.p2_lable_5.show()
		self.scopaMizban.show()
		self.p2_lable_6.show()
		self.emtiyazMihman.show()
		self.p2_lable_7.show()
		self.scopaMihman.show()
		self.p2_btn_1.show()
		self.p2_btn_2.show()
		self.p2_btn_3.show()

	def Show2(self):
		self.selectCb2 = self.cb2.currentText()

	def Show3(self):
		self.selectCb3 = self.cb3.currentText()

	def save(self):
		db = semidbm.open('DataBase', 'c')
		group_dict = pickle.loads(db['group_dict'])
		db.close()
		group_dict['emtiyaz'].append('ok')

		indx_1 = self.list_g.index(self.selectCb0)
		try:
			cb_mizban = self.selectCb2
			cb_mihman = self.selectCb3
			if cb_mizban == cb_mihman:
				play_sound("./sounds/rpause.mp3")
				QMessageBox.about(self, 'خطای ورودی', 'نام تیم میزبان و تیم میهمان نمیتواند مشابه باشد!')
				return

			indx_mizban = self.cb2.currentIndex()
			indx_mihman = self.cb3.currentIndex()
		except:
			play_sound("./sounds/rpause.mp3")
			QMessageBox.about(self, 'خطای ورودی', 'تیم میزبان و تیم میهمان را مشخص کنید!')
			return

		mizbanList = ['bazi_mizban_1', 'bazi_mizban_2', 'bazi_mizban_3', 'bazi_mizban_4', 'bazi_mizban_5',
					  'bazi_mizban_6', 'bazi_mizban_7', 'bazi_mizban_8', 'bazi_mizban_9', 'bazi_mizban_10', 'bazi_mizban_11', 'bazi_mizban_12', 'bazi_mizban_13', 'bazi_mizban_14', 'bazi_mizban_15', 'bazi_mizban_16']
		mihmanList = ['bazi_mihman_1', 'bazi_mihman_2', 'bazi_mihman_3', 'bazi_mihman_4', 'bazi_mihman_5',
					  'bazi_mihman_6', 'bazi_mihman_7', 'bazi_mihman_8', 'bazi_mihman_9', 'bazi_mihman_10', 'bazi_mihman_11', 'bazi_mihman_12', 'bazi_mihman_13', 'bazi_mihman_14', 'bazi_mihman_15', 'bazi_mihman_16']
		natijehMizban = ['natijeh_bazi_mizban_1', 'natijeh_bazi_mizban_2', 'natijeh_bazi_mizban_3',
						 'natijeh_bazi_mizban_4', 'natijeh_bazi_mizban_5', 'natijeh_bazi_mizban_6',
						 'natijeh_bazi_mizban_7', 'natijeh_bazi_mizban_8', 'natijeh_bazi_mizban_9', 'natijeh_bazi_mizban_10', 'natijeh_bazi_mizban_11', 'natijeh_bazi_mizban_12', 'natijeh_bazi_mizban_13', 'natijeh_bazi_mizban_14', 'natijeh_bazi_mizban_15', 'natijeh_bazi_mizban_16']
		natijehMihman = ['natijeh_bazi_mihman_1', 'natijeh_bazi_mihman_2', 'natijeh_bazi_mihman_3',
						 'natijeh_bazi_mihman_4', 'natijeh_bazi_mihman_5', 'natijeh_bazi_mihman_6',
						 'natijeh_bazi_mihman_7', 'natijeh_bazi_mihman_8', 'natijeh_bazi_mihman_9', 'natijeh_bazi_mihman_10', 'natijeh_bazi_mihman_11', 'natijeh_bazi_mihman_12', 'natijeh_bazi_mihman_13', 'natijeh_bazi_mihman_14', 'natijeh_bazi_mihman_15', 'natijeh_bazi_mihman_16']
		scopaMizban = ['scopa_mizban_1', 'scopa_mizban_2', 'scopa_mizban_3', 'scopa_mizban_4', 'scopa_mizban_5',
					   'scopa_mizban_6', 'scopa_mizban_7', 'scopa_mizban_8', 'scopa_mizban_9', 'scopa_mizban_10', 'scopa_mizban_11', 'scopa_mizban_12', 'scopa_mizban_13', 'scopa_mizban_14', 'scopa_mizban_15', 'scopa_mizban_16']
		scopaMihman = ['scopa_mihman_1', 'scopa_mihman_2', 'scopa_mihman_3', 'scopa_mihman_4', 'scopa_mihman_5',
					   'scopa_mihman_6', 'scopa_mihman_7', 'scopa_mihman_8', 'scopa_mihman_9', 'scopa_mihman_10', 'scopa_mihman_11', 'scopa_mihman_12', 'scopa_mihman_13', 'scopa_mihman_14', 'scopa_mihman_15', 'scopa_mihman_16']
		gameTeam = ['game_team_grupe_1', 'game_team_grupe_2', 'game_team_grupe_3', 'game_team_grupe_4',
					'game_team_grupe_5', 'game_team_grupe_6', 'game_team_grupe_7', 'game_team_grupe_8', 'game_team_grupe_9', 'game_team_grupe_10', 'game_team_grupe_11', 'game_team_grupe_12', 'game_team_grupe_13', 'game_team_grupe_14', 'game_team_grupe_15', 'game_team_grupe_16']
		# bord_bakht = ['bord_bakht_1', 'bord_bakht_2', 'bord_bakht_3', 'bord_bakht_4', 'bord_bakht_5', 'bord_bakht_6', 'bord_bakht_7', 'bord_bakht_8', 'bord_bakht_9', 'bord_bakht_10', 'bord_bakht_11', 'bord_bakht_12', 'bord_bakht_13', 'bord_bakht_14', 'bord_bakht_15', 'bord_bakht_16']
		ejazeh = ['ejazeh_1', 'ejazeh_2', 'ejazeh_3', 'ejazeh_4', 'ejazeh_5', 'ejazeh_6', 'ejazeh_7', 'ejazeh_8', 'ejazeh_9', 'ejazeh_10', 'ejazeh_11', 'ejazeh_12', 'ejazeh_13', 'ejazeh_14', 'ejazeh_15', 'ejazeh_16']

		try:
			emtiyazMizban = int(self.scoreMizban.text())
			mizbanScopa = int(self.scopaMizban.text())
			emtiyazMihman = int(self.emtiyazMihman.text())
			mihmanScopa = int(self.scopaMihman.text())
		except:
			play_sound("./sounds/rpause.mp3")
			QMessageBox.about(self, 'خطای ورودی', 'مقادیر را بصورت عدد صحیح وارد کنید!')
			return
		gtm = self.gameTeam[indx_1]
		mizban_l = mizbanList[indx_1]
		group_dict[mizban_l].append(cb_mizban)
		mihman_l = mihmanList[indx_1]
		group_dict[mihman_l].append(cb_mihman)
		n_mizban = natijehMizban[indx_1]
		group_dict[n_mizban].append(emtiyazMizban)
		n_mihman = natijehMihman[indx_1]
		group_dict[n_mihman].append(emtiyazMihman)
		s_mizban = scopaMizban[indx_1]
		group_dict[s_mizban].append(mizbanScopa)
		s_mihman = scopaMihman[indx_1]
		group_dict[s_mihman].append(mihmanScopa)
		group_dict[gtm].append(cb_mizban)
		group_dict[gtm].append(cb_mihman)

		e_j = ejazeh[indx_1]
		group_dict[e_j] = 'ok'

		if self.clicked == 1:
			self.clicked = 0
			db = semidbm.open('DataBase', 'c')
			db['group_dict'] = pickle.dumps(group_dict)
			db.close()

			db = semidbm.open('DataBase', 'c')
			group_dict = pickle.loads(db['group_dict'])
			db.close()

			try:
				self.p2 = Score_Table()
				self.p2.show()
				window.hide()
				self.close()
			except:
				pass
		if self.clicked == 2:
			self.clicked = 0
			db = semidbm.open('DataBase', 'c')
			db['group_dict'] = pickle.dumps(group_dict)
			db.close()
			play_sound("./sounds/videosession.mp3")
			self.m = MainWindow()
			self.m.show()
			window.hide()
			self.close()

	def close_window2(self):
		if self.m2 == None:
			self.m2 = MainWindow()
			self.m2.show()
			window.hide()

			self.close()

# window_1
class Dialog(QDialog):

	"""Dialog."""

	def __init__(self, parent=None):
		"""Initializer."""
		super().__init__(parent)
		self.setWindowTitle('بخش جدول گروه ها')
		self.setGeometry(100, 100, 550, 420)
		self.page_1 = QGridLayout()
		self.setLayout(self.page_1)
		play_sound("./sounds/intercept.mp3")
		window.hide()
		self.p1 = None
		self.m = None
		self.p = None

		self.g_p1 = group_dict
		self.p_1_lable_1 = QLabel('اطلاعات جدول گروه ها را در یک مرحله و بصورت کامل وارد کنید.')
		self.page_1.addChildWidget(self.p_1_lable_1)
		self.p_1_lable_1.setGeometry(100, 20, 350, 30)

		self.p_1_lable_2 = QLabel('نام جام:')
		self.page_1.addChildWidget(self.p_1_lable_2)
		self.p_1_lable_2.setGeometry(230, 75, 60, 25)

		self.cup_name_input = QLineEdit()
		self.cup_name_input.setAccessibleName('نام جام را وارد کنید.')
		self.cup_name_input.setGeometry(110, 75, 110, 20)
		self.page_1.addChildWidget(self.cup_name_input)

		self.p_1_lable_3 = QLabel('تعداد گروه در این جام:')
		self.page_1.addChildWidget(self.p_1_lable_3)
		self.p_1_lable_3.setGeometry(230, 105, 120, 25)

		self.input_number_groups_0 = QLineEdit()
		self.input_number_groups_0.setAccessibleName('تعداد گروه در این جام را وارد کنید.')
		self.page_1.addChildWidget(self.input_number_groups_0)
		self.input_number_groups_0.setGeometry(110, 105, 110, 20)

		self.p_1_lable_4 = QLabel('تعداد تیم در هر گروه:')
		self.p_1_lable_4.setGeometry(230, 145, 120, 25)
		self.page_1.addChildWidget(self.p_1_lable_4)

		self.number_of_team_0 = QLineEdit()
		self.number_of_team_0.setAccessibleName('تعداد تیم در هر گروه؟')
		self.number_of_team_0.setGeometry(110, 145, 110, 20)
		self.page_1.addChildWidget(self.number_of_team_0)

		self.btn_1_page1 = QPushButton('ادامه')
		self.btn_1_page1.setAccessibleName('ادامه')
		self.btn_1_page1.setGeometry(115, 220, 60, 25)
		self.btn_1_page1.clicked.connect(self.p1_continiue)
		self.page_1.addChildWidget(self.btn_1_page1)

		self.btn_2_page1 = QPushButton('بازگشت')
		self.btn_2_page1.setAccessibleName('بازگشت')
		self.btn_2_page1.setGeometry(180, 220, 60, 25)
		self.btn_2_page1.clicked.connect(self.close_window)
		self.page_1.addChildWidget(self.btn_2_page1)

	def p1_continiue(self):
		db = semidbm.open('DataBase', 'c')
		group_dict = pickle.loads(db['group_dict'])
		db.close()
		if self.m == None:
			self.m = MainWindow()

		cup_name = self.cup_name_input.text()
		try:
			g_num = int(self.input_number_groups_0.text())
			t_num = int(self.number_of_team_0.text())
		except:
			play_sound("./sounds/rpause.mp3")
			QMessageBox.about(self, 'خطای ورودی !', 'ورودی را به عدد وارد کنید.')
			return
		if cup_name[0:3] == "جام":
			a = cup_name.split(" ")
			a.remove("جام")
			b = " ".join(a)
			cup_name = b

		group_dict['cup_name'] = cup_name
		if g_num > 16:
			play_sound("./sounds/rpause.mp3")
			QMessageBox.about(self, "اخطار!", "شما نمیتوانید بیشتر از 16 گروه تعریف کنید!")
			play_sound("./sounds/intercept.mp3")
			return

		group_dict['groups_number'] = g_num
		if t_num > 12:
			play_sound("./sounds/rpause.mp3")
			QMessageBox.about(self, "اخطار!", "شما نمیتوانید بیشتر از 12 تیم برای هر گروه تعریف کنید!")

			play_sound("./sounds/intercept.mp3")
			return
		group_dict['number_of_teams'] = t_num

		self.p_1_lable_1.hide()
		self.p_1_lable_3.hide()
		self.p_1_lable_4.hide()
		self.p_1_lable_2.hide()
		self.input_number_groups_0.hide()
		self.cup_name_input.hide()
		self.number_of_team_0.hide()
		self.btn_1_page1.hide()
		self.btn_2_page1.hide()
		if len(group_dict['cup_name']) > 0:
			g_name = ['گروه A', 'گروه B', 'گروه C', 'گروه D', 'گروه E', 'گروه F', 'گروه G', 'گروه H', 'گروه I', 'گروه J', 'گروه K', 'گروه L', 'گروه M', 'گروه N', 'گروه O', 'گروه P']

			t_name = [
				'تیم اول', 'تیم دوم', 'تیم سوم', 'تیم چهارم', 'تیم پنجم', 'تیم ششم', 'تیم هفتم', 'تیم هشتم',
				'تیم نهم',
				'تیم دهم', 'تیم یازدهم', 'تیم دوازدهم']

			s = 0
			doovr = 0
			for g in range(0, g_num):
				# g = 0
				if s == 2:
					break
				group_dict['all_groups'].append(g_name[g])
				group_dict['groups_name'].append(g_name[g])

				for t in range(0, t_num):
					# nameGroupeInfo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
					doovr += 1

					text, ok = QInputDialog.getText(self, '  اطلاعات  {} را وارد کنید.'.format(g_name[g]),
													t_name[t])

					if ok:
						play_sound("./sounds/key.mp3")
						txt_d = str(text)
						group_dict['all_teamss'].append(txt_d)
						which_group = g_name[g]
						if which_group == 'گروه A':
							group_dict['group_1_list'].append(txt_d)
							group_dict['copy_group_1_list'].append(txt_d)
							group_dict['group_1_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('A')
						if which_group == "گروه B":
							group_dict['group_2_list'].append(txt_d)
							group_dict['copy_group_2_list'].append(txt_d)
							group_dict['group_2_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('B')
						if which_group == 'گروه C':
							group_dict['group_3_list'].append(txt_d)
							group_dict['copy_group_3_list'].append(txt_d)
							group_dict['group_3_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('C')
						if which_group == 'گروه D':
							group_dict['group_4_list'].append(txt_d)
							group_dict['copy_group_4_list'].append(txt_d)
							group_dict['group_4_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('D')
						if which_group == 'گروه E':
							group_dict['group_5_list'].append(txt_d)
							group_dict['copy_group_5_list'].append(txt_d)
							group_dict['group_5_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('E')
						if which_group == "گروه F":
							group_dict['group_6_list'].append(txt_d)
							group_dict['copy_group_6_list'].append(txt_d)
							group_dict['group_6_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('F')
						if which_group == 'گروه G':
							group_dict['group_7_list'].append(txt_d)
							group_dict['copy_group_7_list'].append(txt_d)
							group_dict['group_7_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('G')
						if which_group == 'گروه H':
							group_dict['group_8_list'].append(txt_d)
							group_dict['copy_group_8_list'].append(txt_d)
							group_dict['group_8_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('H')
						if which_group == 'گروه I':
							group_dict['group_9_list'].append(txt_d)
							group_dict['copy_group_9_list'].append(txt_d)
							group_dict['group_9_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('I')
						if which_group == 'گروه J':
							group_dict['group_10_list'].append(txt_d)
							group_dict['copy_group_10_list'].append(txt_d)
							group_dict['group_10_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('J')
						if which_group == 'گروه K':
							group_dict['group_11_list'].append(txt_d)
							group_dict['copy_group_11_list'].append(txt_d)
							group_dict['group_11_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('K')
						if which_group == 'گروه L':
							group_dict['group_12_list'].append(txt_d)
							group_dict['copy_group_12_list'].append(txt_d)
							group_dict['group_12_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('L')
						if which_group == 'گروه M':
							group_dict['group_13_list'].append(txt_d)
							group_dict['copy_group_13_list'].append(txt_d)
							group_dict['group_13_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('M')
						if which_group == 'گروه N':
							group_dict['group_14_list'].append(txt_d)
							group_dict['copy_group_14_list'].append(txt_d)
							group_dict['group_14_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('N')
						if which_group == 'گروه O':
							group_dict['group_15_list'].append(txt_d)
							group_dict['copy_group_15_list'].append(txt_d)
							group_dict['group_15_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('O')
						if which_group == 'گروه P':
							group_dict['group_16_list'].append(txt_d)
							group_dict['copy_group_16_list'].append(txt_d)
							group_dict['group_16_lottery'].append(txt_d)
							group_dict['groh_dasteh'].append('P')


						if doovr == t_num * g_num:
							s = 1
					else:
						s = 2
						break
			if s == 1:
				db = semidbm.open('DataBase', 'c')
				db['group_dict'] = pickle.dumps(group_dict)
				db.close()
				play_sound("./sounds/questionmode.mp3")
				QMessageBox.about(self, "About", "جدول گروه ها با موفقیت ذخیره شد.")
				play_sound("./sounds/mail.mp3")

				self.m = MainWindow()
				self.m.show()
				window.hide()
				self.close()

	def close_window(self):
		# if self.m == None:
		self.p1 = MainWindow()
		self.p1.show()
		window.hide()
		self.close()

# window_home
class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.m = None
		self.p1 = None
		self.p2 = None
		self.p3 = None

		self.setAccessibleName('Scopa Cup v1.0. Programmed By Roohan')
		self.setWindowTitle('Scopa Cup')
		self.setGeometry(100, 100, 550, 420)
		# self.setStyleSheet('background-color: rgb(200, 150, 100);')

		# home = QGridLayout()
		self.home = QVBoxLayout()

		self.setLayout(self.home)
		self.w = None
		self.p2 = None
		self.d = None

		## فایل دیتابیس را برای ذخیره و فراخوانی داده  های قبل ایجاد میکنیم
		#db = semidbm.open('DataBase', 'c')
		#db.close()

		mixer.music.load("./sounds/rstart.mp3")
		mixer.music.play()

		# فراخوانی لیست های ذخیره شدعه از دیتابیس
		try:
			db = semidbm.open('DataBase', 'c')
			group_dict = pickle.loads(db['group_dict'])
			db.close()
		except:
			pass

		self.g_d = group_dict

		self.helloMsg = QLabel("Scopa Cup program v1.3\nprogrammed by Roohan", parent=self)
		self.home.addChildWidget(self.helloMsg)

		self.helloMsg.resize(150, 60)
		self.helloMsg.move(30, 5)

		self.main_btn1 = QPushButton('بخش جدول تیم ها و گروه ها')
		self.home.addChildWidget(self.main_btn1)
		self.main_btn1.clicked.connect(self.show_page_1)
		self.main_btn1.setDefault(True)
		self.main_btn1.setGeometry(100, 90, 350, 25)

		self.main_btn2 = QPushButton('بخش ورود نتایج مسابقات به جدول امتیازها')
		self.home.addChildWidget(self.main_btn2)
		self.main_btn2.clicked.connect(self.show_page_2)
		self.main_btn2.setDefault(True)
		self.main_btn2.setGeometry(100, 125, 350, 25)

		self.main_btn3 = QPushButton('بخش ویرایش جدول امتیازها و جدول گروه ها')
		self.home.addChildWidget(self.main_btn3)
		# self.main_btn3.clicked.connect(self.hideHomeWidget)
		self.main_btn3.setDefault(True)
		self.main_btn3.clicked.connect(self.show_page_3)
		self.main_btn3.setGeometry(100, 160, 350, 25)

		self.main_btn4 = QPushButton('به روز رسانی جدول امتیازها')
		self.home.addChildWidget(self.main_btn4)
		self.main_btn4.setDefault(True)
		self.main_btn4.clicked.connect(self.b_4_home)
		self.main_btn4.setGeometry(100, 195, 350, 25)

		self.main_btn5 = QPushButton('بخش قرعه بازیها')
		self.main_btn5.setDefault(True)
		self.main_btn5.clicked.connect(self.b_5_home)
		self.main_btn5.setGeometry(100, 230, 350, 25)
		self.home.addChildWidget(self.main_btn5)

		self.main_btn6 = QPushButton('مشاهده جدول امتیازها')
		self.home.addChildWidget(self.main_btn6)
		self.main_btn6.setDefault(True)
		self.main_btn6.clicked.connect(self.b_6_home)
		self.main_btn6.setGeometry(100, 265, 350, 25)

		self.main_btn7 = QPushButton('مشاهده جدول آقای اسکوپای جام')
		self.home.addChildWidget(self.main_btn7)
		self.main_btn7.setDefault(True)
		self.main_btn7.clicked.connect(self.b_7_home)
		self.main_btn7.setGeometry(100, 300, 350, 25)

		self.main_btn8 = QPushButton('مشاهده قرعه بازی ها')
		self.home.addChildWidget(self.main_btn8)
		self.main_btn8.setDefault(True)
		self.main_btn8.clicked.connect(self.b_8_home)
		self.main_btn8.setGeometry(100, 335, 350, 25)

		self.main_btn0 = QPushButton('خروج از برنامه')
		self.home.addChildWidget(self.main_btn0)
		self.main_btn0.setDefault(True)
		self.main_btn0.setGeometry(100, 370, 350, 25)
		self.main_btn0.clicked.connect(self.ex)

		self.msg1 = (f"""جدول گروه ها تکمیل شده است.
					اطلاعات جام:
					نام جام : {group_dict['cup_name']}.
					تعداد گروه در این جدول {group_dict['groups_number']}.
					تعداد تیم های حاضر در هر گروه {group_dict['number_of_teams']}.
					تعداد تیم های حاضر در جام {len(group_dict['all_teamss'])}.

					برای تغییر در جدول گروه به بخش ویرایش ، در منوی اصلی برنامه مراجعهکنید.
					""")

	def show_page_1(self, checked):

		if len(self.g_d['cup_name']) > 0:
			play_sound("./sounds/questionmode.mp3")
			QMessageBox.about(self, "Warning!", self.msg1)
			play_sound("./sounds/mail.mp3")
		# else:

		if len(self.g_d['cup_name']) == 0:
			self.p1 = Dialog()
			window.hide()
			self.close()
			self.p1.show()

	def show_page_2(self, checked):

		if len(self.g_d['cup_name']) == 0:
			play_sound("./sounds/questionmode.mp3")
			QMessageBox.about(self, "Warning!", 'برای ورود نتیجه بازیها ابتدا جدول گروه ها را تعریف کنید!')
			play_sound("./sounds/mail.mp3")
			return

		if True:
			self.p2 = Score_Table()
			self.p2.show()
			window.hide()
			self.close()

	def show_page_3(self, checked):

		if len(self.g_d['cup_name']) == 0:
			play_sound("./sounds/questionmode.mp3")
			QMessageBox.about(self, "Warning!",
							  'اطلاعاتی برای ویرایش وجود ندارد. \n برای دسترسی به بخش ویرایش ابتدا باید جدول گروه تکمیل شود!')
			play_sound("./sounds/mail.mp3")
			return

		if True:
			self.p3 = Edit_Tables()
			self.p3.show()
			window.hide()
			self.close()

	def ex(self):
		play_sound("./sounds/disconnect.mp3")
		exit()

	#def ex(self):
	#	mixer.music.load("./sounds/disconnect.mp3")
	#	mixer.music.play()
	#	exit()

	# def 4
	def b_4_home(self):
		# فراخوانی لیست های ذخیره شدعه از دیتابیس
		db = semidbm.open('DataBase', 'c')
		group_dict = pickle.loads(db['group_dict'])
		db.close()
		if len(group_dict['emtiyaz']) == 0:
			play_sound("./sounds/questionmode.mp3")
			QMessageBox.about(self, 'about',
							  'برای دسترسی به بخش به روز رسانی جدول امتیاز ابتدا باید جدول امتیاز تکمیل شود.')
			play_sound("./sounds/mute_all.mp3")
			return
		try:
			import Score_fanction
			play_sound("./sounds/questionmode.mp3")
			QMessageBox.about(self, 'about',
							  'به روز رسانی جدول امتیازها با موفقیت انجام شد. \n برای مشاهده جدول امتیاز هابه پوشه DataBase در محل اجرای فایل برنامه مراجعه کنید.')
			play_sound("./sounds/mail.mp3")
		except:
			play_sound("./sounds/questionmode.mp3")
			QMessageBox.about(self, 'about',
							  'به روز رسانی جدول امتیازها به درستی انجام نشد!]! \n برنامه را مجدد راه اندازی نمایید و دوباره برای به روز رسانی جدول تلاش کنید.')
			play_sound("./sounds/mail.mp3")
			return

	# part_5
	def b_5_home(self):
		play_sound("./sounds/mute_all.mp3")
		# فراخوانی لیست های ذخیره شدعه از دیتابیس
		db = semidbm.open('DataBase', 'c')
		group_dict = pickle.loads(db['group_dict'])
		db.close()
		if len(group_dict['cup_name']) == 0:
			play_sound("./sounds/questionmode.mp3")
			QMessageBox.about(self, 'about', 'برای دسترسی به بخش قرعه بازی ها ابتدا باید جدول گروه را تکمیل کنید!')

			play_sound("./sounds/mute_all.mp3")
			return

		import Lattarry_Fanctions

		play_sound("./sounds/questionmode.mp3")
		QMessageBox.about(self, 'about',
						  'قرعه بازیها با موفقیت انجام شد. \n برای مشاهده قرعه بازی ها به پوشه DataBase در محل اجرای فایل برنامه مراجعه کنید.')
		play_sound("./sounds/mail.mp3")
		return

	# Lattarry_Fanctions.khoroji_lattery_12
	def b_6_home(self):
		try:
			full = os.path.join(os.getcwd(), 'DataBase\\score_table.txt')
			full2 = '"' + full + '"'
			os.startfile(full2)
			play_sound("./sounds/node101508.mp3")
		except:
			play_sound("./sounds/questionmode.mp3")
			QMessageBox.about(self, 'about',
							  'اطلاعاتی برای نمایش وجود ندارد!')
			play_sound("./sounds/mail.mp3")
			return

	def b_7_home(self):
		try:
			full = os.path.join(os.getcwd(), 'DataBase\\mr scopa table.txt')
			full2 = '"' + full + '"'
			os.startfile(full2)
			play_sound("./sounds/node101508.mp3")
		except:
			play_sound("./sounds/questionmode.mp3")
			QMessageBox.about(self, 'about',
							  'اطلاعاتی برای نمایش وجود ندارد!')
			play_sound("./sounds/mail.mp3")
			return

	def b_8_home(self):
		try:
			full = os.path.join(os.getcwd(), 'DataBase\\lottery_groups.txt')
			full2 = '"' + full + '"'
			os.startfile(full2)
			play_sound("./sounds/node101508.mp3")
		except:
			play_sound("./sounds/questionmode.mp3")
			QMessageBox.about(self, 'about',
							  'اطلاعاتی برای نمایش وجود ندارد!')
			play_sound("./sounds/mail.mp3")
			return

app = QApplication(sys.argv)
window = MainWindow()
window.show()
mixer.music.queue("./sounds/connect.mp3")
sys.exit(app.exec())
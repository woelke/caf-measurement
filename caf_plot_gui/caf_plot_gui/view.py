# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1591, 898)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_label = QtWidgets.QVBoxLayout()
        self.verticalLayout_label.setObjectName("verticalLayout_label")
        self.edit_label_filter = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_label_filter.setObjectName("edit_label_filter")
        self.verticalLayout_label.addWidget(self.edit_label_filter)
        self.lst_label = QtWidgets.QListWidget(self.centralwidget)
        self.lst_label.setObjectName("lst_label")
        self.verticalLayout_label.addWidget(self.lst_label)
        self.gridLayout.addLayout(self.verticalLayout_label, 2, 2, 1, 1)
        self.horizontalLayout_Plots = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Plots.setObjectName("horizontalLayout_Plots")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cbox_plots = QtWidgets.QComboBox(self.centralwidget)
        self.cbox_plots.setObjectName("cbox_plots")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbox_plots)
        self.horizontalLayout_Plots.addLayout(self.formLayout_2)
        self.btn_new_plot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_new_plot.setObjectName("btn_new_plot")
        self.horizontalLayout_Plots.addWidget(self.btn_new_plot)
        self.btn_delete_plot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete_plot.setObjectName("btn_delete_plot")
        self.horizontalLayout_Plots.addWidget(self.btn_delete_plot)
        self.gridLayout.addLayout(self.horizontalLayout_Plots, 0, 2, 1, 3)
        self.verticalLayout_csv = QtWidgets.QVBoxLayout()
        self.verticalLayout_csv.setObjectName("verticalLayout_csv")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radiobtn_memory = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobtn_memory.setObjectName("radiobtn_memory")
        self.horizontalLayout.addWidget(self.radiobtn_memory)
        self.radiobtn_performance = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobtn_performance.setChecked(True)
        self.radiobtn_performance.setObjectName("radiobtn_performance")
        self.horizontalLayout.addWidget(self.radiobtn_performance)
        self.verticalLayout_csv.addLayout(self.horizontalLayout)
        self.lst_csv = QtWidgets.QListWidget(self.centralwidget)
        self.lst_csv.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.lst_csv.setObjectName("lst_csv")
        self.verticalLayout_csv.addWidget(self.lst_csv)
        self.gridLayout.addLayout(self.verticalLayout_csv, 0, 0, 3, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 2, 1, 3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 3, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 2, 3, 1, 1)
        self.verticalLayout_details = QtWidgets.QVBoxLayout()
        self.verticalLayout_details.setObjectName("verticalLayout_details")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.edit_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_filename.setObjectName("edit_filename")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_filename)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.edit_title = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_title.setObjectName("edit_title")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_title)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.edit_ylabel = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_ylabel.setObjectName("edit_ylabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edit_ylabel)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.edit_xlabel = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_xlabel.setObjectName("edit_xlabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.edit_xlabel)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.edit_ydivider = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_ydivider.setObjectName("edit_ydivider")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.edit_ydivider)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.edit_xmin = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_xmin.setObjectName("edit_xmin")
        self.horizontalLayout_6.addWidget(self.edit_xmin)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.edit_xmax = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_xmax.setObjectName("edit_xmax")
        self.horizontalLayout_6.addWidget(self.edit_xmax)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.edit_ymin = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_ymin.setObjectName("edit_ymin")
        self.horizontalLayout_7.addWidget(self.edit_ymin)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.edit_ymax = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_ymax.setObjectName("edit_ymax")
        self.horizontalLayout_7.addWidget(self.edit_ymax)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.verticalLayout_details.addLayout(self.formLayout)
        self.table_tlabel = QtWidgets.QTableWidget(self.centralwidget)
        self.table_tlabel.setObjectName("table_tlabel")
        self.table_tlabel.setColumnCount(0)
        self.table_tlabel.setRowCount(0)
        self.verticalLayout_details.addWidget(self.table_tlabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bnt_save_plot = QtWidgets.QPushButton(self.centralwidget)
        self.bnt_save_plot.setObjectName("bnt_save_plot")
        self.horizontalLayout_3.addWidget(self.bnt_save_plot)
        self.btn_preview_plot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_preview_plot.setObjectName("btn_preview_plot")
        self.horizontalLayout_3.addWidget(self.btn_preview_plot)
        self.verticalLayout_details.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_details, 2, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1591, 25))
        self.menubar.setObjectName("menubar")
        self.menuPlot_all = QtWidgets.QMenu(self.menubar)
        self.menuPlot_all.setObjectName("menuPlot_all")
        self.menuConfiguration = QtWidgets.QMenu(self.menubar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        MainWindow.setMenuBar(self.menubar)
        self.action_plot_all = QtWidgets.QAction(MainWindow)
        self.action_plot_all.setObjectName("action_plot_all")
        self.action_preview = QtWidgets.QAction(MainWindow)
        self.action_preview.setObjectName("action_preview")
        self.action_set_plot_script = QtWidgets.QAction(MainWindow)
        self.action_set_plot_script.setObjectName("action_set_plot_script")
        self.action_add_cvs_file = QtWidgets.QAction(MainWindow)
        self.action_add_cvs_file.setObjectName("action_add_cvs_file")
        self.action_add_cvs_folder = QtWidgets.QAction(MainWindow)
        self.action_add_cvs_folder.setObjectName("action_add_cvs_folder")
        self.action_set_pdf_program = QtWidgets.QAction(MainWindow)
        self.action_set_pdf_program.setObjectName("action_set_pdf_program")
        self.action_save_and_print_config = QtWidgets.QAction(MainWindow)
        self.action_save_and_print_config.setObjectName("action_save_and_print_config")
        self.menuPlot_all.addAction(self.action_plot_all)
        self.menuPlot_all.addAction(self.action_preview)
        self.menuConfiguration.addAction(self.action_save_and_print_config)
        self.menuConfiguration.addAction(self.action_set_plot_script)
        self.menuConfiguration.addAction(self.action_add_cvs_folder)
        self.menuConfiguration.addAction(self.action_set_pdf_program)
        self.menubar.addAction(self.menuPlot_all.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Plots:"))
        self.btn_new_plot.setText(_translate("MainWindow", "New"))
        self.btn_delete_plot.setText(_translate("MainWindow", "Delete"))
        self.radiobtn_memory.setText(_translate("MainWindow", "Memory"))
        self.radiobtn_performance.setText(_translate("MainWindow", "Performance"))
        self.label.setText(_translate("MainWindow", "File name:"))
        self.label_2.setText(_translate("MainWindow", "Title:"))
        self.label_3.setText(_translate("MainWindow", "Y-label:"))
        self.label_4.setText(_translate("MainWindow", "X-label:"))
        self.label_6.setText(_translate("MainWindow", "Y-divider:"))
        self.label_7.setText(_translate("MainWindow", "X-axis"))
        self.label_8.setText(_translate("MainWindow", "min:"))
        self.label_9.setText(_translate("MainWindow", "max:"))
        self.label_10.setText(_translate("MainWindow", "Y-axis"))
        self.label_11.setText(_translate("MainWindow", "min:"))
        self.label_12.setText(_translate("MainWindow", "max:"))
        self.bnt_save_plot.setText(_translate("MainWindow", "Save"))
        self.btn_preview_plot.setText(_translate("MainWindow", "Preview"))
        self.menuPlot_all.setTitle(_translate("MainWindow", "Run"))
        self.menuConfiguration.setTitle(_translate("MainWindow", "Configuration"))
        self.action_plot_all.setText(_translate("MainWindow", "Plot all"))
        self.action_preview.setText(_translate("MainWindow", "Preview"))
        self.action_set_plot_script.setText(_translate("MainWindow", "Set plot-script"))
        self.action_add_cvs_file.setText(_translate("MainWindow", "Add CVS file"))
        self.action_add_cvs_folder.setText(_translate("MainWindow", "Add CVS folder"))
        self.action_set_pdf_program.setText(_translate("MainWindow", "Set pdf program"))
        self.action_save_and_print_config.setText(_translate("MainWindow", "Save and print config"))


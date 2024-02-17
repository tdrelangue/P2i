# Form implementation generated from reading ui file 'GraphWindow2.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 781, 611))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frameGraph = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.frameGraph.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameGraph.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameGraph.setObjectName("frameGraph")
        self.layoutWidget = QtWidgets.QWidget(parent=self.frameGraph)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 351, 609))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SliderDelaiLivr = QtWidgets.QSlider(parent=self.layoutWidget)
        self.SliderDelaiLivr.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SliderDelaiLivr.setObjectName("SliderDelaiLivr")
        self.gridLayout_2.addWidget(self.SliderDelaiLivr, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelDelai = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelDelai.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDelai.setObjectName("labelDelai")
        self.horizontalLayout_5.addWidget(self.labelDelai)
        self.spinBoxDelai = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.spinBoxDelai.setObjectName("GraphSpinBoxDelai")
        self.horizontalLayout_5.addWidget(self.spinBoxDelai)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelQuarantaine = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelQuarantaine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelQuarantaine.setObjectName("labelQuarantaine")
        self.horizontalLayout_7.addWidget(self.labelQuarantaine)
        self.spinBoxQuarantaine = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.spinBoxQuarantaine.setObjectName("GraphSpinBoxQuarantaine")
        self.horizontalLayout_7.addWidget(self.spinBoxQuarantaine)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 5, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelFreqProd = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelFreqProd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelFreqProd.setObjectName("labelFreqProd")
        self.horizontalLayout_8.addWidget(self.labelFreqProd)
        self.spinBoxFreqProd = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.spinBoxFreqProd.setObjectName("GraphSpinBoxSuremballage")
        self.horizontalLayout_8.addWidget(self.spinBoxFreqProd)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 7, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelDLC = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelDLC.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDLC.setObjectName("labelDLC")
        self.horizontalLayout_9.addWidget(self.labelDLC)
        self.spinBoxDLC = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.spinBoxDLC.setObjectName("GraphSpinBoxDLC")
        self.horizontalLayout_9.addWidget(self.spinBoxDLC)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 9, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelContractDate = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelContractDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelContractDate.setObjectName("labelContractDate")
        self.horizontalLayout_6.addWidget(self.labelContractDate)
        self.spinBoxContractDate = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.spinBoxContractDate.setObjectName("GraphSpinBoxContractDate")
        self.horizontalLayout_6.addWidget(self.spinBoxContractDate)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.SliderContratDate = QtWidgets.QSlider(parent=self.layoutWidget)
        self.SliderContratDate.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SliderContratDate.setObjectName("SliderContratDate")
        self.gridLayout_2.addWidget(self.SliderContratDate, 4, 0, 1, 1)
        self.SliderQuarantaine = QtWidgets.QSlider(parent=self.layoutWidget)
        self.SliderQuarantaine.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SliderQuarantaine.setObjectName("SliderQuarantaine")
        self.gridLayout_2.addWidget(self.SliderQuarantaine, 6, 0, 1, 1)
        self.SliderFreqProd = QtWidgets.QSlider(parent=self.layoutWidget)
        self.SliderFreqProd.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SliderFreqProd.setObjectName("SliderFreqProd")
        self.gridLayout_2.addWidget(self.SliderFreqProd, 8, 0, 1, 1)
        self.SliderDLC = QtWidgets.QSlider(parent=self.layoutWidget)
        self.SliderDLC.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SliderDLC.setObjectName("SliderDLC")
        self.gridLayout_2.addWidget(self.SliderDLC, 10, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxSaL = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxSaL.setText("")
        self.checkBoxSaL.setObjectName("GraphCheckBoxSaL")
        self.gridLayout.addWidget(self.checkBoxSaL, 8, 1, 1, 1)
        self.checkBoxDiL = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxDiL.setText("")
        self.checkBoxDiL.setObjectName("GraphCheckBoxDiL")
        self.gridLayout.addWidget(self.checkBoxDiL, 9, 1, 1, 1)
        self.labelJe = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelJe.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelJe.setObjectName("labelJe")
        self.gridLayout.addWidget(self.labelJe, 6, 0, 1, 1)
        self.checkBoxMaL = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxMaL.setText("")
        self.checkBoxMaL.setObjectName("GraphCheckBoxMaL")
        self.gridLayout.addWidget(self.checkBoxMaL, 4, 1, 1, 1)
        self.checkBoxLuL = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxLuL.setText("")
        self.checkBoxLuL.setObjectName("GraphCheckBoxLuL")
        self.gridLayout.addWidget(self.checkBoxLuL, 3, 1, 1, 1)
        self.labelVe = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelVe.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelVe.setObjectName("labelVe")
        self.gridLayout.addWidget(self.labelVe, 7, 0, 1, 1)
        self.checkBoxVeL = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxVeL.setText("")
        self.checkBoxVeL.setObjectName("GraphCheckBoxVeL")
        self.gridLayout.addWidget(self.checkBoxVeL, 7, 1, 1, 1)
        self.checkBoxJeL = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxJeL.setText("")
        self.checkBoxJeL.setObjectName("GraphCheckBoxJeL")
        self.gridLayout.addWidget(self.checkBoxJeL, 6, 1, 1, 1)
        self.checkBoxLuP = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxLuP.setText("")
        self.checkBoxLuP.setObjectName("GraphCheckBoxLuP")
        self.gridLayout.addWidget(self.checkBoxLuP, 3, 2, 1, 1)
        self.labelDi = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelDi.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDi.setObjectName("labelDi")
        self.gridLayout.addWidget(self.labelDi, 9, 0, 1, 1)
        self.labelMa = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelMa.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelMa.setObjectName("labelMa")
        self.gridLayout.addWidget(self.labelMa, 4, 0, 1, 1)
        self.labelSa = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelSa.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelSa.setObjectName("labelSa")
        self.gridLayout.addWidget(self.labelSa, 8, 0, 1, 1)
        self.labelMe = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelMe.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelMe.setObjectName("labelMe")
        self.gridLayout.addWidget(self.labelMe, 5, 0, 1, 1)
        self.checkBoxDiP = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxDiP.setText("")
        self.checkBoxDiP.setObjectName("GraphCheckBoxDiP")
        self.gridLayout.addWidget(self.checkBoxDiP, 9, 2, 1, 1)
        self.checkBoxSaP = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxSaP.setText("")
        self.checkBoxSaP.setObjectName("GraphCheckBoxSaP")
        self.gridLayout.addWidget(self.checkBoxSaP, 8, 2, 1, 1)
        self.checkBoxJeP = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxJeP.setText("")
        self.checkBoxJeP.setObjectName("GraphCheckBoxJeP")
        self.gridLayout.addWidget(self.checkBoxJeP, 6, 2, 1, 1)
        self.checkBoxMaP = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxMaP.setText("")
        self.checkBoxMaP.setObjectName("GraphCheckBoxMaP")
        self.gridLayout.addWidget(self.checkBoxMaP, 4, 2, 1, 1)
        self.checkBoxVeP = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxVeP.setText("")
        self.checkBoxVeP.setObjectName("GraphCheckBoxVeP")
        self.gridLayout.addWidget(self.checkBoxVeP, 7, 2, 1, 1)
        self.checkBoxMeL = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxMeL.setText("")
        self.checkBoxMeL.setObjectName("GraphCheckBoxMeL")
        self.gridLayout.addWidget(self.checkBoxMeL, 5, 1, 1, 1)
        self.checkBoxMeP = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxMeP.setText("")
        self.checkBoxMeP.setObjectName("GraphCheckBoxMeP")
        self.gridLayout.addWidget(self.checkBoxMeP, 5, 2, 1, 1)
        self.labelLu = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelLu.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelLu.setObjectName("labelLu")
        self.gridLayout.addWidget(self.labelLu, 3, 0, 1, 1)
        self.labelLivr = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelLivr.setObjectName("labelLivr")
        self.gridLayout.addWidget(self.labelLivr, 2, 1, 1, 1)
        self.labelProd = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelProd.setObjectName("labelProd")
        self.gridLayout.addWidget(self.labelProd, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_4.addWidget(self.pushButtonClear)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addWidget(self.frameGraph)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 22))
        self.menubar.setObjectName("GraphMenubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("GraphMenuFile")
        self.menuFen_tre = QtWidgets.QMenu(parent=self.menubar)
        self.menuFen_tre.setObjectName("GraphMenuFen_tre")
        self.menuPolice = QtWidgets.QMenu(parent=self.menuFen_tre)
        self.menuPolice.setObjectName("GraphMenuPolice")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("GraphStatusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOuvrir = QtGui.QAction(parent=MainWindow)
        self.actionOuvrir.setObjectName("GraphActionOuvrir")
        self.actionNouveau = QtGui.QAction(parent=MainWindow)
        self.actionNouveau.setObjectName("GraphActionNouveau")
        self.actionSauvegarder = QtGui.QAction(parent=MainWindow)
        self.actionSauvegarder.setObjectName("GraphActionSauvegarder")
        self.actionMode_Sans_Serif = QtGui.QAction(parent=MainWindow)
        self.actionMode_Sans_Serif.setCheckable(True)
        self.actionMode_Sans_Serif.setEnabled(True)
        self.actionMode_Sans_Serif.setObjectName("GraphActionMode_Sans_Serif")
        self.action32 = QtGui.QAction(parent=MainWindow)
        self.action32.setCheckable(True)
        self.action32.setEnabled(True)
        self.action32.setObjectName("GraphAction32")
        self.action16 = QtGui.QAction(parent=MainWindow)
        self.action16.setCheckable(True)
        self.action16.setChecked(True)
        self.action16.setObjectName("GraphAction16")
        self.action8 = QtGui.QAction(parent=MainWindow)
        self.action8.setCheckable(True)
        self.action8.setEnabled(True)
        self.action8.setObjectName("GraphAction8")
        self.menuFile.addAction(self.actionOuvrir)
        self.menuFile.addAction(self.actionNouveau)
        self.menuFile.addAction(self.actionSauvegarder)
        self.menuPolice.addAction(self.action32)
        self.menuPolice.addAction(self.action16)
        self.menuPolice.addAction(self.action8)
        self.menuFen_tre.addAction(self.menuPolice.menuAction())
        self.menuFen_tre.addAction(self.actionMode_Sans_Serif)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFen_tre.menuAction())

        # Créer un canvas qui servira pour le graph
        self.figure = Figure()
        # self.ax = self.figure.add_subplot(111)
        self.GraphCanvas = FigureCanvas(self.figure )
        self.GraphCanvas.setObjectName("GraphCanvas")

        self.horizontalLayout_3.addWidget(self.GraphCanvas)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelDelai.setText(_translate("MainWindow", "Delai de livraison"))
        self.labelQuarantaine.setText(_translate("MainWindow", "Quarantaine"))
        self.labelFreqProd.setText(_translate("MainWindow", "Fréquence de prod"))
        self.labelDLC.setText(_translate("MainWindow", "DLC"))
        self.labelContractDate.setText(_translate("MainWindow", "Contract date"))
        self.labelJe.setText(_translate("MainWindow", "Jeudi"))
        self.labelVe.setText(_translate("MainWindow", "Vendredi"))
        self.labelDi.setText(_translate("MainWindow", "Dimanche"))
        self.labelMa.setText(_translate("MainWindow", "Mardi"))
        self.labelSa.setText(_translate("MainWindow", "Samedi"))
        self.labelMe.setText(_translate("MainWindow", "Mercredi"))
        self.labelLu.setText(_translate("MainWindow", "Lundi"))
        self.labelLivr.setText(_translate("MainWindow", "Livraison"))
        self.labelProd.setText(_translate("MainWindow", "Production"))
        self.pushButtonClear.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "Fichier"))
        self.menuFen_tre.setTitle(_translate("MainWindow", "Fenêtre"))
        self.menuPolice.setTitle(_translate("MainWindow", "Police"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir ..."))
        self.actionNouveau.setText(_translate("MainWindow", "Nouveau"))
        self.actionSauvegarder.setText(_translate("MainWindow", "Enregistrer sous ..."))
        self.actionMode_Sans_Serif.setText(_translate("MainWindow", "Mode Sans Serif"))
        self.action32.setText(_translate("MainWindow", "32"))
        self.action16.setText(_translate("MainWindow", "16"))
        self.action8.setText(_translate("MainWindow", "8"))
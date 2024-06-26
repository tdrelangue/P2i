# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class UiGraphWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("GraphCentral-widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 781, 611))
        self.horizontalLayoutWidget.setObjectName("GraphHorizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("GraphHorizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("GraphVerticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("GraphHorizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("GraphGridLayout_2")

        # Let's go add a slider to the spinboxes
        # First I add a vertical layout that will contain a slider, a spinbox and a label
        self.ParametersVerticalLayout = QtWidgets.QVBoxLayout()
        self.ParametersVerticalLayout.setObjectName("GraphParametersVerticalLayout")

        # Let's create our items
        self.spinBoxDelai = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxDelai.setObjectName("GraphSpinBoxDelai")
        self.labelDelai = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelDelai.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDelai.setObjectName("GraphLabelDelai")
        self.SliderDelai = QtWidgets.QSlider()
        self.SliderDelai.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SliderDelai.setObjectName("GraphSliderDelai")

        # same for ContractDate

        # Let's create our items
        self.spinBoxContractDate = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxContractDate.setObjectName("GraphSpinBoxContratDate")
        self.labelContractDate = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelContractDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelContractDate.setObjectName("GraphLabelContratDate")
        self.SliderContratDate = QtWidgets.QSlider()
        self.SliderContratDate.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SliderContratDate.setObjectName("GraphSliderContratDate")

        # same for Quarantaine
        # Let's create our items
        self.spinBoxQuarantaine = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxQuarantaine.setObjectName("GraphSpinBoxQuarantaine")
        self.labelQuarantaine = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelQuarantaine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelQuarantaine.setObjectName("GraphLabelQuarantaine")
        self.SliderQuarantaine = QtWidgets.QSlider()
        self.SliderQuarantaine.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SliderQuarantaine.setObjectName("GraphSliderQuarantaine")

        # same for Suremballage

        # Let's create our items
        self.labelDelaiSurembalage = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelDelaiSurembalage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDelaiSurembalage.setObjectName("GraphlabelDelaiSurembalage")
        self.spinBoxSuremballage = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxSuremballage.setObjectName("GraphSpinBoxSuremballage")
        self.SliderSuremballage = QtWidgets.QSlider()
        self.SliderSuremballage.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SliderSuremballage.setObjectName("GraphSliderSuremballage")

        # same for DLC

        # Let's create our items
        self.labelDLC = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelDLC.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDLC.setObjectName("GraphLabelDLC")
        self.spinBoxDLC = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxDLC.setObjectName("GraphSpinBoxDLC")
        self.SliderDLC = QtWidgets.QSlider()
        self.SliderDLC.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.SliderDLC.setObjectName("GraphSliderDLC")

        # Create a dictionary to store the widgets and their corresponding layouts
        widgets_and_layouts = {
            "Delai": (self.labelDelai, self.spinBoxDelai, self.SliderDelai),
            "ContractDate": (self.labelContractDate, self.spinBoxContractDate, self.SliderContratDate),
            "Quarantaine": (self.labelQuarantaine, self.spinBoxQuarantaine, self.SliderQuarantaine),
            "Suremballage": (self.labelDelaiSurembalage, self.spinBoxSuremballage, self.SliderSuremballage),
            "DLC": (self.labelDLC, self.spinBoxDLC, self.SliderDLC),
        }

        for widget_name, (label, spin_box, slider) in widgets_and_layouts.items():
            # Horizontal layout for each set of widgets
            horizontal_layout = QtWidgets.QHBoxLayout()
            horizontal_layout.setObjectName(f"Graph{widget_name}HorizontalLayout")

            # Align the label to the left
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            horizontal_layout.addWidget(label)

            # Align the spin box to the right
            spin_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            horizontal_layout.addWidget(spin_box)

            # Add the horizontal layout to the vertical layout
            self.ParametersVerticalLayout.addLayout(horizontal_layout)

            # Add the slider to the vertical layout
            self.ParametersVerticalLayout.addWidget(slider)

        self.horizontalLayout.addLayout(self.ParametersVerticalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("GraphHorizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("GraphGridLayout")
        self.checkBoxDiL = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxDiL.setText("")
        self.checkBoxDiL.setObjectName("GraphCheckBoxDiL")
        self.gridLayout.addWidget(self.checkBoxDiL, 7, 2, 1, 1)
        self.labelJe = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelJe.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelJe.setObjectName("GraphLabelJe")
        self.gridLayout.addWidget(self.labelJe, 4, 0, 1, 1)
        self.checkBoxSaL = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxSaL.setText("")
        self.checkBoxSaL.setObjectName("GraphCheckBoxSaL")
        self.gridLayout.addWidget(self.checkBoxSaL, 6, 2, 1, 1)
        self.labelLu = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelLu.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelLu.setObjectName("GraphLabelLu")
        self.gridLayout.addWidget(self.labelLu, 1, 0, 1, 1)
        self.checkBoxJeL = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxJeL.setText("")
        self.checkBoxJeL.setObjectName("GraphCheckBoxJeL")
        self.gridLayout.addWidget(self.checkBoxJeL, 4, 2, 1, 1)
        self.labelVe = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelVe.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelVe.setObjectName("GraphLabelVe")
        self.gridLayout.addWidget(self.labelVe, 5, 0, 1, 1)
        self.checkBoxLuL = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxLuL.setText("")
        self.checkBoxLuL.setObjectName("GraphCheckBoxLuL")
        self.gridLayout.addWidget(self.checkBoxLuL, 1, 2, 1, 1)
        self.checkBoxVeL = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxVeL.setText("")
        self.checkBoxVeL.setObjectName("GraphCheckBoxVeL")
        self.gridLayout.addWidget(self.checkBoxVeL, 5, 2, 1, 1)
        self.checkBoxMaL = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxMaL.setText("")
        self.checkBoxMaL.setObjectName("GraphCheckBoxMaL")
        self.gridLayout.addWidget(self.checkBoxMaL, 2, 2, 1, 1)
        self.labelDi = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelDi.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDi.setObjectName("GraphLabelDi")
        self.gridLayout.addWidget(self.labelDi, 7, 0, 1, 1)
        self.checkBoxLuP = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxLuP.setText("")
        self.checkBoxLuP.setObjectName("GraphCheckBoxLuP")
        self.gridLayout.addWidget(self.checkBoxLuP, 1, 1, 1, 1)
        self.labelSa = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelSa.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelSa.setObjectName("GraphLabelSa")
        self.gridLayout.addWidget(self.labelSa, 6, 0, 1, 1)
        self.labelMa = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelMa.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelMa.setObjectName("GraphLabelMa")
        self.gridLayout.addWidget(self.labelMa, 2, 0, 1, 1)
        self.labelMe = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelMe.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelMe.setObjectName("GraphLabelMe")
        self.gridLayout.addWidget(self.labelMe, 3, 0, 1, 1)
        self.checkBoxVeP = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxVeP.setText("")
        self.checkBoxVeP.setObjectName("GraphCheckBoxVeP")
        self.gridLayout.addWidget(self.checkBoxVeP, 5, 1, 1, 1)
        self.checkBoxSaP = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxSaP.setText("")
        self.checkBoxSaP.setObjectName("GraphCheckBoxSaP")
        self.gridLayout.addWidget(self.checkBoxSaP, 6, 1, 1, 1)
        self.checkBoxDiP = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxDiP.setText("")
        self.checkBoxDiP.setObjectName("GraphCheckBoxDiP")
        self.gridLayout.addWidget(self.checkBoxDiP, 7, 1, 1, 1)
        self.checkBoxMaP = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxMaP.setText("")
        self.checkBoxMaP.setObjectName("GraphCheckBoxMaP")
        self.gridLayout.addWidget(self.checkBoxMaP, 2, 1, 1, 1)
        self.checkBoxJeP = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxJeP.setText("")
        self.checkBoxJeP.setObjectName("GraphCheckBoxJeP")
        self.gridLayout.addWidget(self.checkBoxJeP, 4, 1, 1, 1)
        self.checkBoxMeP = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxMeP.setText("")
        self.checkBoxMeP.setObjectName("GraphCheckBoxMeP")
        self.gridLayout.addWidget(self.checkBoxMeP, 3, 1, 1, 1)
        self.checkBoxMeL = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBoxMeL.setText("")
        self.checkBoxMeL.setObjectName("GraphCheckBoxMeL")
        self.gridLayout.addWidget(self.checkBoxMeL, 3, 2, 1, 1)
        self.labelLivr = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelLivr.setObjectName("GraphLabelLivr")
        self.gridLayout.addWidget(self.labelLivr, 0, 2, 1, 1)
        # had to tweek the size policy
        self.labelLivr.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        self.labelProd = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelProd.setObjectName("GraphLabelProd")
        self.labelProd.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addWidget(self.labelProd, 0, 1, 1, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("GraphHorizontalLayout_4")
        self.pushButtonClear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonClear.setObjectName("GraphPushButtonClear")
        self.horizontalLayout_4.addWidget(self.pushButtonClear)
        self.pushButtonIA = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonIA.setObjectName("GraphPushButtonIA")
        self.horizontalLayout_4.addWidget(self.pushButtonIA)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        # Créer un canvas qui servira pour le graph
        self.figure = Figure()
        # self.ax = self.figure.add_subplot(111)
        self.GraphCanvas = FigureCanvas(self.figure)
        self.GraphCanvas.setObjectName("GraphCanvas")
        self.horizontalLayout_3.addWidget(self.GraphCanvas)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SecuStock", "SecuStock"))
        self.labelDLC.setText(_translate("SecuStock", "DLC"))
        self.labelQuarantaine.setText(_translate("SecuStock", "Quarantaine"))
        self.labelDelai.setText(_translate("SecuStock", "Delai de livraison"))
        self.labelContractDate.setText(_translate("SecuStock", "Contract date"))
        self.labelDelaiSurembalage.setText(_translate("SecuStock", "Delai de suremballage"))
        self.labelJe.setText(_translate("SecuStock", "Jeudi"))
        self.labelLu.setText(_translate("SecuStock", "Lundi"))
        self.labelVe.setText(_translate("SecuStock", "Vendredi"))
        self.labelDi.setText(_translate("SecuStock", "Dimanche"))
        self.labelSa.setText(_translate("SecuStock", "Samedi"))
        self.labelMa.setText(_translate("SecuStock", "Mardi"))
        self.labelMe.setText(_translate("SecuStock", "Mercredi"))
        self.labelLivr.setText(_translate("SecuStock", "Livraison"))
        self.labelProd.setText(_translate("SecuStock", "Production"))
        self.pushButtonClear.setText(_translate("SecuStock", "&Clear"))
        self.pushButtonIA.setText(_translate("SecuStock", "&IA"))


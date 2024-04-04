# Libraries
import os
import sys
# Import the sys module for handling system-specific parameters and functions
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
# Import the FigureCanvasQTAgg for creating a matplotlib figure canvas in a PyQt6 application
from mainWindow import UiMainWindow
# Import the UiMainWindow class from the mainWindow module
from GraphWindow import UiGraphWindow
# Import the UiGraphWindow class from the GraphWindow module
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QCheckBox, QSpinBox, QMessageBox, QSlider
# Import various classes from the PyQt6.QtWidgets module for creating graphical user interface elements

from PyQt6.QtGui import QIcon, QFont
# Import various classes from the Py6.QtGui module for handling graphical user interface elements    QIcon,

import numpy as np                          # Import the numpy module for numerical computations
from CalcSecuStock import *                 # Import the CalcSecuStock module, which contains functions for calculating stock-related values


class MyApp(QMainWindow):                   # Define a new class named MyApp that inherits from the QMainWindow class
    def __init__(self):                      # Define the constructor method for the MyApp class
        super().__init__()       # Call the constructor of the superclass (QMainWindow) to initialize the object
        self.setWindowTitle('SecuStock')      # Set the window title to 'SecuStock'
        self.setWindowIcon(QIcon(self.resource_path('assets\\stock.ico')))      # Set the window icon to the 'stock.ico' file
        # import open dyslexic font
        id_open_dys = QtGui.QFontDatabase.addApplicationFont(self.resource_path("assets\\OpenDyslexic-Regular.otf"))
        # get the exact system name to ensure no mistakes are made
        try :
            self.OpenDyslexic = QtGui.QFontDatabase.applicationFontFamilies(id_open_dys)[0]
        except :
            self.OpenDyslexic = "calibri"
        self.PrimaryFont = "calibri"

        # Creation of the menu bar
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFen_tre = QtWidgets.QMenu(parent=self.menubar)
        self.menuFen_tre.setObjectName("menuFen_tre")
        self.menuPolice = QtWidgets.QMenu(parent=self.menuFen_tre)
        self.menuPolice.setObjectName("menuPolice")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionOuvrir = QtGui.QAction()
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionNouveau = QtGui.QAction()
        self.actionNouveau.setObjectName("actionNouveau")
        self.actionSauvegarder = QtGui.QAction()
        self.actionSauvegarder.setObjectName("actionSauvegarder")
        self.actionMode_Dys = QtGui.QAction()
        self.actionMode_Dys.setCheckable(True)
        self.actionMode_Dys.setEnabled(True)
        self.actionMode_Dys.setObjectName("actionMode_Dys")
        self.actionMode_Dys.toggled.connect(self.ChangeFont)
        self.action32 = QtGui.QAction()
        self.action32.setCheckable(True)
        self.action32.setEnabled(True)
        self.action32.setObjectName("action32")
        self.action32.toggled.connect(lambda _: self.ChangeFontSize(changedValue=32))
        self.action16 = QtGui.QAction()
        self.action16.setCheckable(True)
        self.action16.setChecked(True)
        self.action16.toggled.connect(lambda _: self.ChangeFontSize(changedValue=16))
        self.action16.setObjectName("action16")
        self.action8 = QtGui.QAction()
        self.action8.setCheckable(True)
        self.action8.setEnabled(True)
        self.action8.setObjectName("action8")
        self.action8.toggled.connect(lambda _: self.ChangeFontSize(changedValue=8))
        self.menuFile.addAction(self.actionOuvrir)
        self.menuFile.addAction(self.actionNouveau)
        self.menuFile.addAction(self.actionSauvegarder)
        self.menuPolice.addAction(self.action32)
        self.menuPolice.addAction(self.action16)
        self.menuPolice.addAction(self.action8)
        self.menuFen_tre.addAction(self.menuPolice.menuAction())
        self.menuFen_tre.addAction(self.actionMode_Dys)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFen_tre.menuAction())

        _translate = QtCore.QCoreApplication.translate
        self.menuFile.setTitle(_translate("MainWindow", "Fichier"))
        self.menuFen_tre.setTitle(_translate("MainWindow", "Fenêtre"))
        self.menuPolice.setTitle(_translate("MainWindow", "Police"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir ..."))
        self.actionNouveau.setText(_translate("MainWindow", "Nouveau"))
        self.actionSauvegarder.setText(_translate("MainWindow", "Enregistrer sous ..."))
        self.actionMode_Dys.setText(_translate("MainWindow", "Mode dyslexique"))
        self.action32.setText(_translate("MainWindow", "32"))
        self.action16.setText(_translate("MainWindow", "16"))
        self.action8.setText(_translate("MainWindow", "8"))

        # Initialize base values
        self.DLC = 30                         # Shelf life
        self.DelaiLivraison = 1               # Delay in delivery
        self.Suremballage = 1                 # Overpackaging
        self.Quarantaine = 1                  # Quarantine
        self.ContratDate = 15                 # Contract date

        # Initialize value checkboxes
        self.LuProd = True                    # Monday production
        self.MaProd = True                    # Tuesday production
        self.MeProd = True                    # Wednesday production
        self.JeProd = True                    # Thursday production
        self.VeProd = True                    # Friday production
        self.SaProd = True                    # Saturday production
        self.DiProd = False                   # Sunday production
        self.LuLivr = True                    # Monday delivery
        self.MaLivr = True                    # Tuesday delivery
        self.MeLivr = True                    # Wednesday delivery
        self.JeLivr = True                    # Thursday delivery
        self.VeLivr = True                    # Friday delivery
        self.SaLivr = True                    # Saturday delivery
        self.DiLivr = False                   # Sunday delivery

        self.ui = UiMainWindow()              # Create an instance of the UiMainWindow class
        self.ui.setupUi(self)                 # Set up the user interface using the UiMainWindow instance

        # Connect the 'Enter' push button to the CreateGraphWindow method
        self.pushButtonEnter = self.findChild(QPushButton, "pushButtonEnter")
        self.pushButtonEnter.clicked.connect(self.CreateGraphWindow)

        # checkbox Lundi Prod
        self.checkBoxLuP = self.findChild(QCheckBox, "checkBoxLuP")
        self.checkBoxLuP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="LuProd"))
        # checkbox Mardi Prod
        self.checkBoxMaP = self.findChild(QCheckBox, "checkBoxMaP")
        self.checkBoxMaP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="MaProd"))
        # checkbox Mercredi Prod
        self.checkBoxMeP = self.findChild(QCheckBox, "checkBoxMeP")
        self.checkBoxMeP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="MeProd"))
        # checkbox Jeudi Prod
        self.checkBoxJeP = self.findChild(QCheckBox, "checkBoxJeP")
        self.checkBoxJeP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="JeProd"))
        # checkbox Vendredi Prod
        self.checkBoxVeP = self.findChild(QCheckBox, "checkBoxVeP")
        self.checkBoxVeP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="VeProd"))
        # checkbox Samedi Prod
        self.checkBoxSaP = self.findChild(QCheckBox, "checkBoxSaP")
        self.checkBoxSaP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="SaProd"))
        # checkbox Dimanche Prod
        self.checkBoxDiP = self.findChild(QCheckBox, "checkBoxDiP")
        self.checkBoxDiP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="DiProd"))
        # checkbox Lundi Livr
        self.checkBoxLuL = self.findChild(QCheckBox, "checkBoxLuL")
        self.checkBoxLuL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="LuLivr"))
        # checkbox Mardi Livr
        self.checkBoxMaL = self.findChild(QCheckBox, "checkBoxMaL")
        self.checkBoxMaL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="MaLivr"))
        # checkbox Mercredi Livr
        self.checkBoxMeL = self.findChild(QCheckBox, "checkBoxMeL")
        self.checkBoxMeL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="MeLivr"))
        # checkbox Jeudi Livr
        self.checkBoxJeL = self.findChild(QCheckBox, "checkBoxJeL")
        self.checkBoxJeL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="JeLivr"))
        # checkbox Vendredi Livr
        self.checkBoxVeL = self.findChild(QCheckBox, "checkBoxVeL")
        self.checkBoxVeL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="VeLivr"))
        # checkbox Samedi Livr
        self.checkBoxSaL = self.findChild(QCheckBox, "checkBoxSaL")
        self.checkBoxSaL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="SaLivr"))
        # checkbox Dimanche Livr
        self.checkBoxDiL = self.findChild(QCheckBox, "checkBoxDiL")
        self.checkBoxDiL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="DiLivr"))

        # spinBox DLC
        self.spinBoxDLC = self.findChild(QSpinBox, "spinBoxDLC")
        self.spinBoxDLC.valueChanged.connect(lambda _: self.SpinBoxIsChanged(changedValue="DLC"))
        # spinBox Delai
        self.spinBoxDelai = self.findChild(QSpinBox, "spinBoxDelai")
        self.spinBoxDelai.valueChanged.connect(lambda _: self.SpinBoxIsChanged(changedValue="Livr"))
        # spinBox Freq Prod
        self.spinBoxSuremballage = self.findChild(QSpinBox, "spinBoxSuremballage")
        self.spinBoxSuremballage.valueChanged.connect(lambda _: self.SpinBoxIsChanged(changedValue="Surr"))
        # spinBox Quarantaine
        self.spinBoxQuarantaine = self.findChild(QSpinBox, "spinBoxQuarantaine")
        self.spinBoxQuarantaine.valueChanged.connect(lambda _: self.SpinBoxIsChanged(changedValue="Quar"))
        # spinBox Contract Date
        self.spinBoxContractDate = self.findChild(QSpinBox, "spinBoxContratDate")
        self.spinBoxContractDate.valueChanged.connect(lambda _: self.SpinBoxIsChanged(changedValue="CD"))

        # Let's assign some base values so that people don't have to click 1000 times per use
        # checkBoxLuP
        self.checkBoxLuP.setChecked(self.LuProd)
        # checkBoxLuL
        self.checkBoxLuL.setChecked(self.LuLivr)
        # checkBoxMaP
        self.checkBoxMaP.setChecked(self.MaProd)
        # checkBoxMaL
        self.checkBoxMaL.setChecked(self.MaLivr)
        # checkBoxMeP
        self.checkBoxMeP.setChecked(self.MeProd)
        # checkBoxMeL
        self.checkBoxMeL.setChecked(self.MeLivr)
        # checkBoxJeP
        self.checkBoxJeP.setChecked(self.JeProd)
        # checkBoxJeL
        self.checkBoxJeL.setChecked(self.JeLivr)
        # checkBoxVeP
        self.checkBoxVeP.setChecked(self.VeProd)
        # checkBoxVeL
        self.checkBoxVeL.setChecked(self.VeLivr)
        # checkBoxSaP
        self.checkBoxSaP.setChecked(self.SaProd)
        # checkBoxSaL
        self.checkBoxSaL.setChecked(self.SaLivr)
        # checkBoxDiP
        self.checkBoxDiP.setChecked(self.DiProd)
        # checkBoxDiL
        self.checkBoxDiL.setChecked(self.DiLivr)

        # Same for spinboxes
        self.spinBoxContractDate.setValue(self.ContratDate)
        self.spinBoxQuarantaine.setValue(self.Quarantaine)
        self.spinBoxDelai.setValue(self.DelaiLivraison)
        self.spinBoxSuremballage.setValue(self.Suremballage)
        self.spinBoxDLC.setValue(self.DLC)

        self.ChangeFontSize(changedValue=16)
        width = 925
        height = 420
        # setting the width and height of window
        self.resize(width, height)

    def CreateGraphWindow(self):
        """Function responsible for creating a graph in the canvas"""
        self.ui = UiGraphWindow()
        self.ui.setupUi(self)

        self.Canvas = self.findChild(FigureCanvas, "GraphCanvas")
        self.ax = self.Canvas.figure.add_subplot(111)

        self.AssignGraphWindowWidgets()
        self.CreateGraph()
        # Set the window to full screen
        self.showMaximized()

    def SpinBoxIsChanged(self,  changedValue):
        """Function responsible for changing the parameter according to the spinBoxes in the main page"""
        match changedValue:
            case "DLC":
                self.DLC = self.spinBoxDLC.value()
            case "Livr":
                self.DelaiLivraison = self.spinBoxDelai.value()
            case "Surr":
                self.Suremballage = self.spinBoxSuremballage.value()
            case "Quar":
                self.Quarantaine = self.spinBoxQuarantaine.value()
            case "CD":
                self.ContratDate = self.spinBoxContractDate.value()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def GraphSliderIsChanged(self, changedValue):
        """Function responsible for changing the parameter according to the sliders in the graph page"""

        match changedValue:
            case "DLC":
                self.DLC = self.sliderDLC.value()
                self.spinBoxDLC.setValue(self.DLC)
            case "Livr":
                self.DelaiLivraison = self.sliderDelai.value()
                self.spinBoxDelai.setValue(self.DelaiLivraison)
            case "Surr":
                self.Suremballage = self.sliderSuremballage.value()
                self.spinBoxSuremballage.setValue(self.Suremballage)
            case "Quar":
                self.Quarantaine = self.sliderQuarantaine.value()
                self.spinBoxQuarantaine.setValue(self.Quarantaine)
            case "CD":
                self.ContratDate = self.sliderContractDate.value()
                self.spinBoxContractDate.setValue(self.ContratDate)
        self.CreateGraph()

    def GraphSpinBoxIsChanged(self, changedValue):
        """Function responsible for changing the parameter according to the spinBoxes in the graph page"""
        match changedValue:
            case "DLC":
                self.DLC = self.spinBoxDLC.value()
            case "Livr":
                self.DelaiLivraison = self.spinBoxDelai.value()
            case "Surr":
                self.Suremballage = self.spinBoxSuremballage.value()
            case "Quar":
                self.Quarantaine = self.spinBoxQuarantaine.value()
            case "CD":
                self.ContratDate = self.spinBoxContractDate.value()
        self.CreateGraph()

    def CheckBoxIsChecked(self, changedValue):
        """Function responsible for changing the parameter according to the checkboxes in the main page"""
        match changedValue:
            case "LuProd":
                self.LuProd = self.checkBoxLuP.isChecked()
            case "MaProd":
                self.MaProd = self.checkBoxMaP.isChecked()
            case "MeProd":
                self.MeProd = self.checkBoxMeP.isChecked()
            case "JeProd":
                self.JeProd = self.checkBoxJeP.isChecked()
            case "VeProd":
                self.VeProd = self.checkBoxVeP.isChecked()
            case "SaProd":
                self.SaProd = self.checkBoxSaP.isChecked()
            case "DiProd":
                self.DiProd = self.checkBoxDiP.isChecked()
            case "LuLivr":
                self.LuLivr = self.checkBoxLuL.isChecked()
            case "MaLivr":
                self.MaLivr = self.checkBoxMaL.isChecked()
            case "MeLivr":
                self.MeLivr = self.checkBoxMeL.isChecked()
            case "JeLivr":
                self.JeLivr = self.checkBoxJeL.isChecked()
            case "VeLivr":
                self.VeLivr = self.checkBoxVeL.isChecked()
            case "SaLivr":
                self.SaLivr = self.checkBoxSaL.isChecked()
            case "DiLivr":
                self.DiLivr = self.checkBoxDiL.isChecked()

    def GraphCheckBoxIsChecked(self, changedValue):
        """Function responsible for changing the parameter according to the checkboxes in the graph page"""
        match changedValue:
            case "LuProd":
                self.LuProd = self.checkBoxLuP.isChecked()
            case "MaProd":
                self.MaProd = self.checkBoxMaP.isChecked()
            case "MeProd":
                self.MeProd = self.checkBoxMeP.isChecked()
            case "JeProd":
                self.JeProd = self.checkBoxJeP.isChecked()
            case "VeProd":
                self.VeProd = self.checkBoxVeP.isChecked()
            case "SaProd":
                self.SaProd = self.checkBoxSaP.isChecked()
            case "DiProd":
                self.DiProd = self.checkBoxDiP.isChecked()
            case "LuLivr":
                self.LuLivr = self.checkBoxLuL.isChecked()
            case "MaLivr":
                self.MaLivr = self.checkBoxMaL.isChecked()
            case "MeLivr":
                self.MeLivr = self.checkBoxMeL.isChecked()
            case "JeLivr":
                self.JeLivr = self.checkBoxJeL.isChecked()
            case "VeLivr":
                self.VeLivr = self.checkBoxVeL.isChecked()
            case "SaLivr":
                self.SaLivr = self.checkBoxSaL.isChecked()
            case "DiLivr":
                self.DiLivr = self.checkBoxDiL.isChecked()
        self.CreateGraph()

    def AssignGraphWindowWidgets(self):
        """Recuperate the widgets when the new graph window is opened"""
        # Relicat de l'époque où le graph ne se mettait pas à jour en temps réel
        # Je fais la bascule entre V1 et V2 donc je le laisse pour l'instant
        try:
            # push button enter
            self.pushButtonEnter = self.findChild(QPushButton, "GraphPushButtonEnter")
            self.pushButtonEnter.clicked.connect(self.CreateGraph)
        except Exception:
            pass

        # checkbox Lundi Prod
        self.checkBoxLuP = self.findChild(QCheckBox, "GraphCheckBoxLuP")
        self.checkBoxLuP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="LuProd"))
        # checkbox Mardi Prod
        self.checkBoxMaP = self.findChild(QCheckBox, "GraphCheckBoxMaP")
        self.checkBoxMaP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="MaProd"))
        # checkbox Mercredi Prod
        self.checkBoxMeP = self.findChild(QCheckBox, "GraphCheckBoxMeP")
        self.checkBoxMeP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="MeProd"))
        # checkbox Jeudi Prod
        self.checkBoxJeP = self.findChild(QCheckBox, "GraphCheckBoxJeP")
        self.checkBoxJeP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="JeProd"))
        # checkbox Vendredi Prod
        self.checkBoxVeP = self.findChild(QCheckBox, "GraphCheckBoxVeP")
        self.checkBoxVeP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="VeProd"))
        # checkbox Samedi Prod
        self.checkBoxSaP = self.findChild(QCheckBox, "GraphCheckBoxSaP")
        self.checkBoxSaP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="SaProd"))
        # checkbox Dimanche Prod
        self.checkBoxDiP = self.findChild(QCheckBox, "GraphCheckBoxDiP")
        self.checkBoxDiP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="DiProd"))
        # checkbox Lundi Livr
        self.checkBoxLuL = self.findChild(QCheckBox, "GraphCheckBoxLuL")
        self.checkBoxLuL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="LuLivr"))
        # checkbox Mardi Livr
        self.checkBoxMaL = self.findChild(QCheckBox, "GraphCheckBoxMaL")
        self.checkBoxMaL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="MaLivr"))
        # checkbox Mercredi Livr
        self.checkBoxMeL = self.findChild(QCheckBox, "GraphCheckBoxMeL")
        self.checkBoxMeL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="MeLivr"))
        # checkbox Jeudi Livr
        self.checkBoxJeL = self.findChild(QCheckBox, "GraphCheckBoxJeL")
        self.checkBoxJeL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="JeLivr"))
        # checkbox Vendredi Livr
        self.checkBoxVeL = self.findChild(QCheckBox, "GraphCheckBoxVeL")
        self.checkBoxVeL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="VeLivr"))
        # checkbox Samedi Livr
        self.checkBoxSaL = self.findChild(QCheckBox, "GraphCheckBoxSaL")
        self.checkBoxSaL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="SaLivr"))
        # checkbox Dimanche Livr
        self.checkBoxDiL = self.findChild(QCheckBox, "GraphCheckBoxDiL")
        self.checkBoxDiL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="DiLivr"))

        # reassign old checkbox values to new checkboxes
        # checkBoxLuP
        self.checkBoxLuP.setChecked(self.LuProd)
        # checkBoxLuL
        self.checkBoxLuL.setChecked(self.LuLivr)
        # checkBoxMaP
        self.checkBoxMaP.setChecked(self.MaProd)
        # checkBoxMaL
        self.checkBoxMaL.setChecked(self.MaLivr)
        # checkBoxMeP
        self.checkBoxMeP.setChecked(self.MeProd)
        # checkBoxMeL
        self.checkBoxMeL.setChecked(self.MeLivr)
        # checkBoxJeP
        self.checkBoxJeP.setChecked(self.JeProd)
        # checkBoxJeL
        self.checkBoxJeL.setChecked(self.JeLivr)
        # checkBoxVeP
        self.checkBoxVeP.setChecked(self.VeProd)
        # checkBoxVeL
        self.checkBoxVeL.setChecked(self.VeLivr)
        # checkBoxSaP
        self.checkBoxSaP.setChecked(self.SaProd)
        # checkBoxSaL
        self.checkBoxSaL.setChecked(self.SaLivr)
        # checkBoxDiP
        self.checkBoxDiP.setChecked(self.DiProd)
        # checkBoxDiL
        self.checkBoxDiL.setChecked(self.DiLivr)

        # spinBox DLC
        self.spinBoxDLC = self.findChild(QSpinBox, "GraphSpinBoxDLC")
        self.spinBoxDLC.valueChanged.connect(lambda _: self.GraphSpinBoxIsChanged(changedValue="DLC"))
        # spinBox Delai
        self.spinBoxDelai = self.findChild(QSpinBox, "GraphSpinBoxDelai")
        self.spinBoxDelai.valueChanged.connect(lambda _: self.GraphSpinBoxIsChanged(changedValue="Livr"))
        # spinBox Freq Prod
        self.spinBoxSuremballage = self.findChild(QSpinBox, "GraphSpinBoxSuremballage")
        self.spinBoxSuremballage.valueChanged.connect(lambda _: self.GraphSpinBoxIsChanged(changedValue="Surr"))
        # spinBox Quarantaine
        self.spinBoxQuarantaine = self.findChild(QSpinBox, "GraphSpinBoxQuarantaine")
        self.spinBoxQuarantaine.valueChanged.connect(lambda _: self.GraphSpinBoxIsChanged(changedValue="Quar"))
        # spinBox Contract Date
        self.spinBoxContractDate = self.findChild(QSpinBox, "GraphSpinBoxContratDate")
        self.spinBoxContractDate.valueChanged.connect(lambda _: self.GraphSpinBoxIsChanged(changedValue="CD"))

        self.spinBoxContractDate.setValue(self.ContratDate)
        self.spinBoxQuarantaine.setValue(self.Quarantaine)
        self.spinBoxDelai.setValue(self.DelaiLivraison)
        self.spinBoxSuremballage.setValue(self.Suremballage)
        self.spinBoxDLC.setValue(self.DLC)

        # slider DLC
        self.sliderDLC = self.findChild(QSlider, "GraphSliderDLC")
        self.sliderDLC.valueChanged.connect(lambda _: self.GraphSliderIsChanged(changedValue="DLC"))
        # slider Delai
        self.sliderDelai = self.findChild(QSlider, "GraphSliderDelai")
        self.sliderDelai.valueChanged.connect(lambda _: self.GraphSliderIsChanged(changedValue="Livr"))
        # slider Freq Prod
        self.sliderSuremballage = self.findChild(QSlider, "GraphSliderSuremballage")
        self.sliderSuremballage.valueChanged.connect(lambda _: self.GraphSliderIsChanged(changedValue="Surr"))
        # slider Quarantaine
        self.sliderQuarantaine = self.findChild(QSlider, "GraphSliderQuarantaine")
        self.sliderQuarantaine.valueChanged.connect(lambda _: self.GraphSliderIsChanged(changedValue="Quar"))
        # slider Contract Date
        self.sliderContractDate = self.findChild(QSlider, "GraphSliderContratDate")
        self.sliderContractDate.valueChanged.connect(lambda _: self.GraphSliderIsChanged(changedValue="CD"))

        self.sliderContractDate.setValue(self.ContratDate)
        self.sliderQuarantaine.setValue(self.Quarantaine)
        self.sliderDelai.setValue(self.DelaiLivraison)
        self.sliderSuremballage.setValue(self.Suremballage)
        self.sliderDLC.setValue(self.DLC)

    def CreateGraph(self):
        """Creates or updates the graph"""
        try:
            planning = create_delivery_planning(
                quarantaine=self.Quarantaine + self.DelaiLivraison,
                suremballage=self.Suremballage,
                DLC=self.DLC,
                contractDate=self.ContratDate,
                MondayLivr=self.LuLivr,
                TuesdayLivr=self.MaLivr,
                WednesdayLivr=self.MeLivr,
                ThursdayLivr=self.JeLivr,
                FridayLivr=self.VeLivr,
                SaturdayLivr=self.SaLivr,
                SundayLivr=self.DiLivr,
                MondayProd=self.LuProd,
                TuesdayProd=self.MaProd,
                WednesdayProd=self.MeProd,
                ThursdayProd=self.JeProd,
                FridayProd=self.VeProd,
                SaturdayProd=self.SaProd,
                SundayProd=self.DiProd
            )
            a_rupture, b_rupture, rupture = calculate_rupture(planning)
            a_degagement, b_degagement, degagement = calculate_degagement(planning)

            def f(x, a, b):
                return a * x + b

            # Generate x values
            x_values = np.linspace(0, rupture - 1, rupture)

            # Calculate y values for each function
            y1_values = f(x_values, a_rupture, b_rupture)
            y2_values = f(x_values, a_degagement, b_degagement)

            # Plot the functions
            self.ax.plot(x_values, y1_values, label=f"{a_rupture}x + {b_rupture}")
            self.ax.cla()
            self.ax.plot(x_values, y1_values, label=f"Chances de rupture")
            self.ax.plot(x_values, y2_values, label=f"Chances de dégagement")
            # Add labels and a legend
            self.ax.set_xlabel('Nombre de jours de stock de sécurité')
            self.ax.set_ylabel("""Pourcentage d'écart de prévision maximal sans pertes""")
            self.ax.set_title('Graph of Two Linear Functions')
            self.ax.legend()
        except:
            # Standard popup with only OK button
            QMessageBox.critical(None, "Result", "Les paramêtres entrés ne permettent pas de calculer \n"
                                                 "le taux d'écart causant une rupture ou un dépassement")

        self.Canvas.draw()

    def ChangeFont(self):
        if self.action32:
            self.ChangeFontSize(changedValue=32)
        elif self.action16:
            self.ChangeFontSize(changedValue=16)
        else:
            self.ChangeFontSize(changedValue=8)

    def ChangeFontSize(self, changedValue):
        if changedValue == 32:
            self.action16.setChecked(False)
            self.action8.setChecked(False)
        elif changedValue == 16:
            self.action32.setChecked(False)
            self.action8.setChecked(False)
        elif changedValue == 8:
            self.action32.setChecked(False)
            self.action16.setChecked(False)
        else:
            self.action32.setChecked(False)
            self.action16.setChecked(False)
            self.action8.setChecked(False)
        if self.actionMode_Dys.isChecked():
            try :
                self.setFont(QFont(self.OpenDyslexic, changedValue))
            except :
                self.setFont(QFont(self.PrimaryFont, changedValue))
        else:
            self.setFont(QFont(self.PrimaryFont, changedValue))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())

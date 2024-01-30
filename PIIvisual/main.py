# Libraries
import sys
from mainWindow import UiMainWindow
from GraphWindow import UiGraphWindow
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QCheckBox, QSpinBox
from PyQt5.QtGui import QIcon, QFont
from icecream import ic


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SecuStock')
        self.setWindowIcon(QIcon('stock.ico'))
        self.resize(900, 500)
        self.PrimaryFont = QFont("verdana", 16)
        self.SecondaryFont = QFont("verdana", 8)

        # def base values
        self.DLC = 0
        self.DelaiLivraison = 0
        self.FreqProd = 0
        self.Quarantaine = 0
        self.ContractDate = 0

        # def value checkboxes
        self.LuProd = False
        self.MaProd = False
        self.MeProd = False
        self.JeProd = False
        self.VeProd = False
        self.SaProd = False
        self.DiProd = False
        self.LuLivr = False
        self.MaLivr = False
        self.MeLivr = False
        self.JeLivr = False
        self.VeLivr = False
        self.SaLivr = False
        self.DiLivr = False

        self.ui = UiMainWindow()
        self.ui.setupUi(self)

        # push button enter
        self.pushButtonEnter = self.findChild(QPushButton, "pushButtonEnter")
        self.pushButtonEnter.clicked.connect(self.CreateGraphWindow)

        # checkbox Lundi Prod
        self.checkBoxLuP = ic(self.findChild(QCheckBox, "checkBoxLuP"))
        self.checkBoxLuP.toggled.connect(self.LuProdIsChecked)
        # checkbox Mardi Prod
        self.checkBoxMaP = ic(self.findChild(QCheckBox, "checkBoxMaP"))
        self.checkBoxMaP.toggled.connect(self.MaProdIsChecked)
        # checkbox Mercredi Prod
        self.checkBoxMeP = ic(self.findChild(QCheckBox, "checkBoxMeP"))
        self.checkBoxMeP.toggled.connect(self.MeProdIsChecked)
        # checkbox Jeudi Prod
        self.checkBoxJeP = ic(self.findChild(QCheckBox, "checkBoxJeP"))
        self.checkBoxJeP.toggled.connect(self.JeProdIsChecked)
        # checkbox Vendredi Prod
        self.checkBoxVeP = ic(self.findChild(QCheckBox, "checkBoxVeP"))
        self.checkBoxVeP.toggled.connect(self.VeProdIsChecked)
        # checkbox Samedi Prod
        self.checkBoxSaP = ic(self.findChild(QCheckBox, "checkBoxSaP"))
        self.checkBoxSaP.toggled.connect(self.SaProdIsChecked)
        # checkbox Dimanche Prod
        self.checkBoxDiP = ic(self.findChild(QCheckBox, "checkBoxDiP"))
        self.checkBoxDiP.toggled.connect(self.DiProdIsChecked)
        # checkbox Lundi Livr
        self.checkBoxLuL = ic(self.findChild(QCheckBox, "checkBoxLuL"))
        self.checkBoxLuL.toggled.connect(self.LuLivrIsChecked)
        # checkbox Mardi Livr
        self.checkBoxMaL = ic(self.findChild(QCheckBox, "checkBoxMaL"))
        self.checkBoxMaL.toggled.connect(self.MaLivrIsChecked)
        # checkbox Mercredi Livr
        self.checkBoxMeL = ic(self.findChild(QCheckBox, "checkBoxMeL"))
        self.checkBoxMeL.toggled.connect(self.MeLivrIsChecked)
        # checkbox Jeudi Livr
        self.checkBoxJeL = ic(self.findChild(QCheckBox, "checkBoxJeL"))
        self.checkBoxJeL.toggled.connect(self.JeLivrIsChecked)
        # checkbox Vendredi Livr
        self.checkBoxVeL = ic(self.findChild(QCheckBox, "checkBoxVeL"))
        self.checkBoxVeL.toggled.connect(self.VeLivrIsChecked)
        # checkbox Samedi Livr
        self.checkBoxSaL = ic(self.findChild(QCheckBox, "checkBoxSaL"))
        self.checkBoxSaL.toggled.connect(self.SaLivrIsChecked)
        # checkbox Dimanche Livr
        self.checkBoxDiL = ic(self.findChild(QCheckBox, "checkBoxDiL"))
        self.checkBoxDiL.toggled.connect(self.DiLivrIsChecked)

        # spinBox DLC
        self.spinBoxDLC = ic(self.findChild(QSpinBox, "spinBoxDLC"))
        self.spinBoxDLC.valueChanged.connect(self.DlcIsChanged)
        # spinBox Delai
        self.spinBoxDelai = ic(self.findChild(QSpinBox, "spinBoxDelai"))
        self.spinBoxDelai.valueChanged.connect(self.DelaiIsChanged)
        # spinBox Freq Prod
        self.spinBoxFreqProd = ic(self.findChild(QSpinBox, "spinBoxFreqProd"))
        self.spinBoxFreqProd.valueChanged.connect(self.FreqProdIsChanged)
        # spinBox Quarantaine
        self.spinBoxQuarantaine = ic(self.findChild(QSpinBox, "spinBoxQuarantaine"))
        self.spinBoxQuarantaine.valueChanged.connect(self.QuarantaineIsChanged)
        # spinBox Contract Date
        self.spinBoxContractDate = ic(self.findChild(QSpinBox, "spinBoxContractDate"))
        self.spinBoxContractDate.valueChanged.connect(self.ContractDateIsChanged)

    def CreateGraphWindow(self):
        self.ui = UiGraphWindow()
        self.ui.setupUi(self)

    def DlcIsChanged(self):
        self.DLC = ic(self.spinBoxDLC.value())

    def DelaiIsChanged(self):
        self.DelaiLivraison = ic(self.spinBoxDelai.value())

    def FreqProdIsChanged(self):
        self.FreqProd = ic(self.spinBoxFreqProd.value())

    def QuarantaineIsChanged(self):
        self.Quarantaine = ic(self.spinBoxQuarantaine.value())

    def ContractDateIsChanged(self):
        self.ContractDate = ic(self.spinBoxContractDate.value())

    def LuProdIsChecked(self):
        self.LuProd = ic(self.checkBoxLuP.isChecked())

    def MaProdIsChecked(self):
        self.MaProd = ic(self.checkBoxMaP.isChecked())

    def MeProdIsChecked(self):
        self.MeProd = ic(self.checkBoxMeP.isChecked())

    def JeProdIsChecked(self):
        self.JeProd = ic(self.checkBoxJeP.isChecked())

    def VeProdIsChecked(self):
        self.VeProd = ic(self.checkBoxVeP.isChecked())

    def SaProdIsChecked(self):
        self.SaProd = ic(self.checkBoxSaP.isChecked())

    def DiProdIsChecked(self):
        self.DiProd = ic(self.checkBoxDiP.isChecked())

    def LuLivrIsChecked(self):
        self.LuLivr = ic(self.checkBoxLuL.isChecked())

    def MaLivrIsChecked(self):
        self.MaLivr = ic(self.checkBoxMaL.isChecked())

    def MeLivrIsChecked(self):
        self.MeLivr = ic(self.checkBoxMeL.isChecked())

    def JeLivrIsChecked(self):
        self.JeLivr = ic(self.checkBoxJeL.isChecked())

    def VeLivrIsChecked(self):
        self.VeLivr = ic(self.checkBoxVeL.isChecked())

    def SaLivrIsChecked(self):
        self.SaLivr = ic(self.checkBoxSaL.isChecked())

    def DiLivrIsChecked(self):
        self.DiLivr = ic(self.checkBoxDiL.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())

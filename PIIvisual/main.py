# Libraries
import sys                                 # Import the sys module for handling system-specific parameters and functions
import PyQt6
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas  # Import the FigureCanvasQTAgg for creating a matplotlib figure canvas in a PyQt5 application

from mainWindow import UiMainWindow          # Import the UiMainWindow class from the mainWindow module
from GraphWindow import UiGraphWindow        # Import the UiGraphWindow class from the GraphWindow module
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QCheckBox, QSpinBox, QMessageBox, QSlider
# Import various classes from the PyQt6.QtWidgets module for creating graphical user interface elements

from PyQt6.QtGui import QIcon, QFont
# Import various classes from the Py6.QtGui module for handling graphical user interface elements    QIcon,

import numpy as np                          # Import the numpy module for numerical computations
from CalcSecuStock import *                 # Import the CalcSecuStock module, which contains functions for calculating stock-related values


class MyApp(QMainWindow):                   # Define a new class named MyApp that inherits from the QMainWindow class
    def __init__(self):                      # Define the constructor method for the MyApp class
        super().__init__()                   # Call the constructor of the superclass (QMainWindow) to initialize the object
        self.setWindowTitle('SecuStock')      # Set the window title to 'SecuStock'
        self.setWindowIcon(QIcon('stock.ico')) # Set the window icon to the 'stock.ico' file
        # self.setSizePolicy(QSizePolicy.Policy, QSizePolicy.Policy.Maximum) # Set the size policy of the window
        self.resize(900, 550)                # Set the window size to 900x550 pixels
        self.PrimaryFont = QFont("verdana", 16) # Create a QFont object for the primary font
        self.SecondaryFont = QFont("verdana", 8) # Create a QFont object for the secondary font

        # Initialize base values
        self.DLC = 30                         # Days of lead time (DLC)
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
        self.checkBoxLuP = ic(self.findChild(QCheckBox, "checkBoxLuP"))
        self.checkBoxLuP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="LuProd"))
        # checkbox Mardi Prod
        self.checkBoxMaP = ic(self.findChild(QCheckBox, "checkBoxMaP"))
        self.checkBoxMaP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="MaProd"))
        # checkbox Mercredi Prod
        self.checkBoxMeP = ic(self.findChild(QCheckBox, "checkBoxMeP"))
        self.checkBoxMeP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="MeProd"))
        # checkbox Jeudi Prod
        self.checkBoxJeP = ic(self.findChild(QCheckBox, "checkBoxJeP"))
        self.checkBoxJeP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="JeProd"))
        # checkbox Vendredi Prod
        self.checkBoxVeP = ic(self.findChild(QCheckBox, "checkBoxVeP"))
        self.checkBoxVeP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="VeProd"))
        # checkbox Samedi Prod
        self.checkBoxSaP = ic(self.findChild(QCheckBox, "checkBoxSaP"))
        self.checkBoxSaP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="SaProd"))
        # checkbox Dimanche Prod
        self.checkBoxDiP = ic(self.findChild(QCheckBox, "checkBoxDiP"))
        self.checkBoxDiP.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="DiProd"))
        # checkbox Lundi Livr
        self.checkBoxLuL = ic(self.findChild(QCheckBox, "checkBoxLuL"))
        self.checkBoxLuL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="LuLivr"))
        # checkbox Mardi Livr
        self.checkBoxMaL = ic(self.findChild(QCheckBox, "checkBoxMaL"))
        self.checkBoxMaL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="MaLivr"))
        # checkbox Mercredi Livr
        self.checkBoxMeL = ic(self.findChild(QCheckBox, "checkBoxMeL"))
        self.checkBoxMeL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="MeLivr"))
        # checkbox Jeudi Livr
        self.checkBoxJeL = ic(self.findChild(QCheckBox, "checkBoxJeL"))
        self.checkBoxJeL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="JeLivr"))
        # checkbox Vendredi Livr
        self.checkBoxVeL = ic(self.findChild(QCheckBox, "checkBoxVeL"))
        self.checkBoxVeL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="VeLivr"))
        # checkbox Samedi Livr
        self.checkBoxSaL = ic(self.findChild(QCheckBox, "checkBoxSaL"))
        self.checkBoxSaL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="SaLivr"))
        # checkbox Dimanche Livr
        self.checkBoxDiL = ic(self.findChild(QCheckBox, "checkBoxDiL"))
        self.checkBoxDiL.toggled.connect(lambda _: self.CheckBoxIsChecked(changedValue="DiLivr"))

        # spinBox DLC
        self.spinBoxDLC = ic(self.findChild(QSpinBox, "spinBoxDLC"))
        self.spinBoxDLC.valueChanged.connect(lambda _: self.SpinBoxIsChanged(changedValue="DLC"))
        # spinBox Delai
        self.spinBoxDelai = ic(self.findChild(QSpinBox, "spinBoxDelai"))
        self.spinBoxDelai.valueChanged.connect(lambda _: self.SpinBoxIsChanged(changedValue="Livr"))
        # spinBox Freq Prod
        self.spinBoxSuremballage = ic(self.findChild(QSpinBox, "spinBoxSuremballage"))
        self.spinBoxSuremballage.valueChanged.connect(lambda _: self.SpinBoxIsChanged(changedValue="Surr"))
        # spinBox Quarantaine
        self.spinBoxQuarantaine = ic(self.findChild(QSpinBox, "spinBoxQuarantaine"))
        self.spinBoxQuarantaine.valueChanged.connect(lambda _: self.SpinBoxIsChanged(changedValue="Quar"))
        # spinBox Contract Date
        self.spinBoxContractDate = ic(self.findChild(QSpinBox, "spinBoxContratDate"))
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

    def CreateGraphWindow(self):
        """Function responsible for creating a graph in the canvas"""
        self.ui = UiGraphWindow()
        self.ui.setupUi(self)

        self.Canvas = ic(self.findChild(FigureCanvas, "GraphCanvas"))
        self.ax = self.Canvas.figure.add_subplot(111)

        # spinBox Delai
        self.spinBoxDelai = ic(self.findChild(QSpinBox, "GraphSpinBoxDelai"))
        self.spinBoxDelai.valueChanged.connect(lambda _: self.SpinBoxIsChanged(changedValue="Livr"))
        self.AssignGraphWindowWidgets()
        self.CreateGraph()

    def SpinBoxIsChanged(self,  changedValue):
        """Function responsible for changing the parameter according to the spinBoxes in the main page"""
        match changedValue:
            case "DLC":
                self.DLC = ic(self.spinBoxDLC.value())
            case "Livr":
                self.DelaiLivraison = ic(self.spinBoxDelai.value())
            case "Surr":
                self.Suremballage = ic(self.spinBoxSuremballage.value())
            case "Quar":
                self.Quarantaine = ic(self.spinBoxQuarantaine.value())
            case "CD":
                self.ContratDate = ic(self.spinBoxContractDate.value())

    def GraphSliderIsChanged(self, changedValue):
        """Function responsible for changing the parameter according to the sliders in the graph page"""

        match changedValue:
            case "DLC":
                self.DLC = ic(self.sliderDLC.value())
                self.spinBoxDLC.setValue(self.DLC)
            case "Livr":
                self.DelaiLivraison = ic(self.sliderDelai.value())
                self.spinBoxDelai.setValue(self.DelaiLivraison)
            case "Surr":
                self.Suremballage = ic(self.sliderSuremballage.value())
                self.spinBoxSuremballage.setValue(self.Suremballage)
            case "Quar":
                self.Quarantaine = ic(self.sliderQuarantaine.value())
                self.spinBoxQuarantaine.setValue(self.Quarantaine)
            case "CD":
                self.ContratDate = ic(self.sliderContractDate.value())
                self.spinBoxContractDate.setValue(self.ContratDate)
        self.CreateGraph()

    def GraphSpinBoxIsChanged(self, changedValue):
        """Function responsible for changing the parameter according to the spinBoxes in the graph page"""
        match changedValue:
            case "DLC":
                self.DLC = ic(self.spinBoxDLC.value())
            case "Livr":
                self.DelaiLivraison = ic(self.spinBoxDelai.value())
            case "Surr":
                self.Suremballage = ic(self.spinBoxSuremballage.value())
            case "Quar":
                self.Quarantaine = ic(self.spinBoxQuarantaine.value())
            case "CD":
                self.ContratDate = ic(self.spinBoxContractDate.value())
        self.CreateGraph()

    def CheckBoxIsChecked(self, changedValue):
        """Function responsible for changing the parameter according to the checkboxes in the main page"""
        match changedValue:
            case "LuProd":
                self.LuProd = ic(self.checkBoxLuP.isChecked())
            case "MaProd":
                self.MaProd = ic(self.checkBoxMaP.isChecked())
            case "MeProd":
                self.MeProd = ic(self.checkBoxMeP.isChecked())
            case "JeProd":
                self.JeProd = ic(self.checkBoxJeP.isChecked())
            case "VeProd":
                self.VeProd = ic(self.checkBoxVeP.isChecked())
            case "SaProd":
                self.SaProd = ic(self.checkBoxSaP.isChecked())
            case "DiProd":
                self.DiProd = ic(self.checkBoxDiP.isChecked())
            case "LuLivr":
                self.LuLivr = ic(self.checkBoxLuL.isChecked())
            case "MaLivr":
                self.MaLivr = ic(self.checkBoxMaL.isChecked())
            case "MeLivr":
                self.MeLivr = ic(self.checkBoxMeL.isChecked())
            case "JeLivr":
                self.JeLivr = ic(self.checkBoxJeL.isChecked())
            case "VeLivr":
                self.VeLivr = ic(self.checkBoxVeL.isChecked())
            case "SaLivr":
                self.SaLivr = ic(self.checkBoxSaL.isChecked())
            case "DiLivr":
                self.DiLivr = ic(self.checkBoxDiL.isChecked())

    def GraphCheckBoxIsChecked(self, changedValue):
        """Function responsible for changing the parameter according to the checkboxes in the graph page"""
        match changedValue:
            case "LuProd":
                self.LuProd = ic(self.checkBoxLuP.isChecked())
            case "MaProd":
                self.MaProd = ic(self.checkBoxMaP.isChecked())
            case "MeProd":
                self.MeProd = ic(self.checkBoxMeP.isChecked())
            case "JeProd":
                self.JeProd = ic(self.checkBoxJeP.isChecked())
            case "VeProd":
                self.VeProd = ic(self.checkBoxVeP.isChecked())
            case "SaProd":
                self.SaProd = ic(self.checkBoxSaP.isChecked())
            case "DiProd":
                self.DiProd = ic(self.checkBoxDiP.isChecked())
            case "LuLivr":
                self.LuLivr = ic(self.checkBoxLuL.isChecked())
            case "MaLivr":
                self.MaLivr = ic(self.checkBoxMaL.isChecked())
            case "MeLivr":
                self.MeLivr = ic(self.checkBoxMeL.isChecked())
            case "JeLivr":
                self.JeLivr = ic(self.checkBoxJeL.isChecked())
            case "VeLivr":
                self.VeLivr = ic(self.checkBoxVeL.isChecked())
            case "SaLivr":
                self.SaLivr = ic(self.checkBoxSaL.isChecked())
            case "DiLivr":
                self.DiLivr = ic(self.checkBoxDiL.isChecked())
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
        self.checkBoxLuP = ic(self.findChild(QCheckBox, "GraphCheckBoxLuP"))
        self.checkBoxLuP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="LuProd"))
        # checkbox Mardi Prod
        self.checkBoxMaP = ic(self.findChild(QCheckBox, "GraphCheckBoxMaP"))
        self.checkBoxMaP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="MaProd"))
        # checkbox Mercredi Prod
        self.checkBoxMeP = ic(self.findChild(QCheckBox, "GraphCheckBoxMeP"))
        self.checkBoxMeP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="MeProd"))
        # checkbox Jeudi Prod
        self.checkBoxJeP = ic(self.findChild(QCheckBox, "GraphCheckBoxJeP"))
        self.checkBoxJeP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="JeProd"))
        # checkbox Vendredi Prod
        self.checkBoxVeP = ic(self.findChild(QCheckBox, "GraphCheckBoxVeP"))
        self.checkBoxVeP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="VeProd"))
        # checkbox Samedi Prod
        self.checkBoxSaP = ic(self.findChild(QCheckBox, "GraphCheckBoxSaP"))
        self.checkBoxSaP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="SaProd"))
        # checkbox Dimanche Prod
        self.checkBoxDiP = ic(self.findChild(QCheckBox, "GraphCheckBoxDiP"))
        self.checkBoxDiP.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="DiProd"))
        # checkbox Lundi Livr
        self.checkBoxLuL = ic(self.findChild(QCheckBox, "GraphCheckBoxLuL"))
        self.checkBoxLuL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="LuLivr"))
        # checkbox Mardi Livr
        self.checkBoxMaL = ic(self.findChild(QCheckBox, "GraphCheckBoxMaL"))
        self.checkBoxMaL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="MaLivr"))
        # checkbox Mercredi Livr
        self.checkBoxMeL = ic(self.findChild(QCheckBox, "GraphCheckBoxMeL"))
        self.checkBoxMeL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="MeLivr"))
        # checkbox Jeudi Livr
        self.checkBoxJeL = ic(self.findChild(QCheckBox, "GraphCheckBoxJeL"))
        self.checkBoxJeL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="JeLivr"))
        # checkbox Vendredi Livr
        self.checkBoxVeL = ic(self.findChild(QCheckBox, "GraphCheckBoxVeL"))
        self.checkBoxVeL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="VeLivr"))
        # checkbox Samedi Livr
        self.checkBoxSaL = ic(self.findChild(QCheckBox, "GraphCheckBoxSaL"))
        self.checkBoxSaL.toggled.connect(lambda _: self.GraphCheckBoxIsChecked(changedValue="SaLivr"))
        # checkbox Dimanche Livr
        self.checkBoxDiL = ic(self.findChild(QCheckBox, "GraphCheckBoxDiL"))
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
        self.spinBoxDLC = ic(self.findChild(QSpinBox, "GraphSpinBoxDLC"))
        self.spinBoxDLC.valueChanged.connect(lambda _: self.GraphSpinBoxIsChanged(changedValue="DLC"))
        # spinBox Delai
        self.spinBoxDelai = ic(self.findChild(QSpinBox, "GraphSpinBoxDelai"))
        self.spinBoxDelai.valueChanged.connect(lambda _: self.GraphSpinBoxIsChanged(changedValue="Livr"))
        # spinBox Freq Prod
        self.spinBoxSuremballage = ic(self.findChild(QSpinBox, "GraphSpinBoxSuremballage"))
        self.spinBoxSuremballage.valueChanged.connect(lambda _: self.GraphSpinBoxIsChanged(changedValue="Surr"))
        # spinBox Quarantaine
        self.spinBoxQuarantaine = ic(self.findChild(QSpinBox, "GraphSpinBoxQuarantaine"))
        self.spinBoxQuarantaine.valueChanged.connect(lambda _: self.GraphSpinBoxIsChanged(changedValue="Quar"))
        # spinBox Contract Date
        self.spinBoxContractDate = ic(self.findChild(QSpinBox, "GraphSpinBoxContratDate"))
        self.spinBoxContractDate.valueChanged.connect(lambda _: self.GraphSpinBoxIsChanged(changedValue="CD"))

        self.spinBoxContractDate.setValue(self.ContratDate)
        self.spinBoxQuarantaine.setValue(self.Quarantaine)
        self.spinBoxDelai.setValue(self.DelaiLivraison)
        self.spinBoxSuremballage.setValue(self.Suremballage)
        self.spinBoxDLC.setValue(self.DLC)

        # slider DLC
        self.sliderDLC = ic(self.findChild(QSlider, "GraphSliderDLC"))
        self.sliderDLC.valueChanged.connect(lambda _: self.GraphSliderIsChanged(changedValue="DLC"))
        # slider Delai
        self.sliderDelai = ic(self.findChild(QSlider, "GraphSliderDelai"))
        self.sliderDelai.valueChanged.connect(lambda _: self.GraphSliderIsChanged(changedValue="Livr"))
        # slider Freq Prod
        self.sliderSuremballage = ic(self.findChild(QSlider, "GraphSliderSuremballage"))
        self.sliderSuremballage.valueChanged.connect(lambda _: self.GraphSliderIsChanged(changedValue="Surr"))
        # slider Quarantaine
        self.sliderQuarantaine = ic(self.findChild(QSlider, "GraphSliderQuarantaine"))
        self.sliderQuarantaine.valueChanged.connect(lambda _: self.GraphSliderIsChanged(changedValue="Quar"))
        # slider Contract Date
        self.sliderContractDate = ic(self.findChild(QSlider, "GraphSliderContratDate"))
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())

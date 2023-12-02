import sys
from PyQt6.QtWidgets import *

class Fenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chronomètre")
        self.setGeometry(100, 100, 400, 200)
        
        self.label_Compteur = QLabel("Compteur :")
        self.entry_Compteur = QLineEdit()
        self.entry_Compteur.setReadOnly(True)
        self.bouton_Start = QPushButton("Start")
        self.bouton_Reset = QPushButton("Reset")
        self.bouton_Stop = QPushButton("Stop")
        self.bouton_Connect = QPushButton("Connect")
        self.bouton_Quitter = QPushButton("Quitter")

        layout_principal = QGridLayout()
        
        layout_principal.addWidget(self.label_Compteur, 0 , 0)
        layout_principal.addWidget(self.entry_Compteur, 1 , 0, 1, 2)
        layout_principal.addWidget(self.bouton_Start, 2 , 0, 1, 2)
        layout_principal.addWidget(self.bouton_Reset, 3 , 0)
        layout_principal.addWidget(self.bouton_Stop, 3 , 1)
        layout_principal.addWidget(self.bouton_Connect, 4 , 0)
        layout_principal.addWidget(self.bouton_Quitter, 4 , 1)

        self.setLayout(layout_principal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre()
    fenetre.show()
    sys.exit(app.exec())
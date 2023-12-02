import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

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

        self.compteur = 0
        self.timer = QTimer(self)

        layout_principal.addWidget(self.label_Compteur, 0, 0)
        layout_principal.addWidget(self.entry_Compteur, 1, 0, 1, 2)
        layout_principal.addWidget(self.bouton_Start, 2, 0, 1, 2)
        layout_principal.addWidget(self.bouton_Reset, 3, 0)
        layout_principal.addWidget(self.bouton_Stop, 3, 1)
        layout_principal.addWidget(self.bouton_Connect, 4, 0)
        layout_principal.addWidget(self.bouton_Quitter, 4, 1)

        self.setLayout(layout_principal)

        self.bouton_Start.clicked.connect(self.start)
        self.bouton_Reset.clicked.connect(self.reset)
        self.bouton_Quitter.clicked.connect(self.quitter)
        self.bouton_Stop.clicked.connect(self.stop)

        self.timer.timeout.connect(self.compteur_plus_1)

    def start(self):
        self.arret_thread = False
        self.timer.start(1000)

    def compteur_plus_1(self):
        if not self.arret_thread:
            self.compteur += 1
            self.entry_Compteur.setText(str(self.compteur))

    def reset(self):
        self.timer.stop()
        if self.compteur != 0:
            self.compteur = 0
        self.entry_Compteur.clear()

    def quitter(self):
        self.stop()
        QCoreApplication.exit(0)

    def stop(self):
        self.arret_thread = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre()
    fenetre.show()
    sys.exit(app.exec())

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QFrame, QLineEdit
from PyQt5.QtGui import QFont, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint

import pandas as pd
import importSquadData

imported = False

class Player(QWidget):
    def __init__(self, name, window):
        super().__init__(window)
        self.name = name
        self.radius = 15
        self.setFixedSize(self.radius * 6, self.radius * 6) # means the circle will be contained within, adding extra space for name
        self._drag_active = False
        self._drag_position = QPoint() # tracks mouse position where clicked
        self.setAttribute(Qt.WA_TranslucentBackground) # makes background translucent so only circle is shown
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: # only care about left click
            self._drag_active = True
            self._drag_position = event.globalPos() - self.frameGeometry().topLeft() # if we don't consider this offset the top left corner will always snap to the mouse
            event.accept() # means event has been handled

    def mouseMoveEvent(self, event):
        if self._drag_active and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_active = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing) # smoothes out the edges of shapes

        diameter = self.radius * 2
        pen_width = 2

        # Calculate the center of the widget
        center_x = self.width() // 2
        center_y = self.height() // 2

        # Calculate top-left coords to draw ellipse so circle is centered horizontally
        top_left_x = center_x - self.radius
        top_left_y = center_y - self.radius - 5 # subtracted 5 to leave extra room for name below

        painter.setBrush(QBrush(Qt.blue)) # makes fill blue
        painter.setPen(QPen(Qt.black, pen_width)) # makes border black
        painter.drawEllipse(top_left_x, top_left_y, diameter - pen_width, diameter - pen_width)

        # Draw the name in the center
        painter.setPen(Qt.black)
        font = QFont("Arial", 5)
        painter.setFont(font)
        text_rect = self.rect()
        text_rect.setTop(self.radius * 2)  # start text below the circle
        painter.drawText(text_rect, Qt.AlignCenter, self.name)

    def move_to_position(self, pos):
        if pos == "GK":
            self.move(25, 225)
        elif pos == "WB (R)" or pos == "D (R)":
            self.move(200, 450)
        elif pos == "D (C)":
            self.move(180, 225)
        elif pos == "WB (L)" or pos == "D (L)":
            self.move(200, 0)
        elif pos == "DM":
            self.move(360, 225)
        elif pos == "M (R)":
            self.move(540, 450)
        elif pos == "M (C)":
            self.move(540, 225)
        elif pos == "M (L)":
            self.move(540, 0)
        elif pos == "AM (R)":
            self.move(720, 450)
        elif pos == "AM (C)":
            self.move(720, 225)
        elif pos == "AM (L)":
            self.move(720, 0)
        elif pos == "ST (C)" or pos == "ST (R)" or pos == "ST (L)":
            self.move(900, 225)
        

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(350, 200, 1200, 600)
    window.setFixedSize(1200, 600)
    window.setWindowTitle("Interactive Football Pitch")


    ### Creating and editing a label
    name_label = QLabel(window) # create label
    name_label.setText("Add Player Name:") # set text
    name_label.setFont(QFont("Times New Roman", 10)) # change font
    name_label.move(22, 540) # change location
    
    
    ### Creating and editing textbox
    name_textbox = QLineEdit(window) # create
    name_textbox.move(20, 565) # move
    
    
    ### Creating label for button that makes the players
    create_player_button_label = QLabel(window)
    create_player_button_label.setText("Press Button To Create Player (Add name to textbox on left first):")
    create_player_button_label.setFont(QFont("Times New Roman", 10))
    create_player_button_label.move(302, 540)
    
    
    ### Creating button that makes the players
    create_player_button = QPushButton(window)
    create_player_button.setText("Create Player")
    create_player_button.move(300, 562)
    
    
    ### Creating button that imports the players
    import_player_button = QPushButton(window)
    import_player_button.setText("Import Players")
    import_player_button.move(450, 562)
    
    
    ### Separate the textbox, labels, and buttons from rest of window
    line = QFrame(window)
    line.setFrameShape(QFrame.HLine)
    line.setGeometry(0, 530, 1000, 10)


    ### create a section of the screen for transfers, making that part red
    red_widget = QWidget(window)
    red_widget.setStyleSheet("background-color: red;")
    red_widget.setGeometry(1000, 0, 200, 600)
    
    
    # connect button to function --> creating lambda function that calls the on_create_player_button_clicked function
    # with the contents of the textbox as a parameter converted to plain text
    create_player_button.clicked.connect(lambda: on_create_player_button_clicked(name_textbox.text(), window))

    import_player_button.clicked.connect(lambda: on_import_player_button_clicked(window))
    
    
    window.show()
    app.exec()
    
def on_create_player_button_clicked(name, window):
    player = Player(name, window)
    player.move(100, 100)
    player.show()

def on_import_player_button_clicked(window):
    global imported

    if imported == False: # only want to import once
        imported = True
        player_df = importSquadData.create_player_df() # get player dataframe
        player_names = player_df["Name"].to_list() # get the player names
        best_positions = player_df["Best Pos"].to_list()
        for i in range(len(player_names)): # create a circle for each player
            player = Player(player_names[i], window)
            print(best_positions[i])
            player.move_to_position(best_positions[i].strip()) # move the player on the field based on their best position
            player.show()
        print(player_df)
    
if __name__ == '__main__':
    main()
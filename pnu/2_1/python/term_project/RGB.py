from PyQt5.QtGui import *

class RGB(QColor):
    def hex_format(self):
        return '#{:02X}{:02X}{:02X}'.format(self.red, self.green, self.blue)

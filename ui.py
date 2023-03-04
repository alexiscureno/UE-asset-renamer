import sys
import unreal
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QCheckBox
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QSize
from PyQt5.QtGui import QImage, QPixmap, QMouseEvent
from PyQt5 import uic, QtCore

def rename_assets(search_pattern, replace_pattern, use_case):
    # unreal classes instances

    system_lib = unreal.SystemLibrary()
    edit_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()


    # get the selected assets and number for displaying

    selected_assets = edit_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0

    unreal.log("Selected {} assets".format(num_assets))

    # this loops over each asset and renames it

    for asset in selected_assets:
        asset_name = system_lib.get_object_name(asset)

        # check if the asset name contains the given string and checks if its case-sensitive
        if string_lib.contains(asset_name, search_pattern, use_case=use_case):
            search_case = unreal.SearchCase.CASE_SENSITIVE if use_case else unreal.SearchCase.IGNORE_CASE
            replaced_name = string_lib.replace(asset_name, search_pattern, replace_pattern, search_case=search_case)
            edit_util.rename_asset(asset, replaced_name)

            replaced += 1
            unreal.log('Replaced {} with {}.'.format(asset_name, replaced_name))

        else:
            unreal.log("{} did not match the search pattern, was skipped".format(asset_name))

    unreal.log('replaced {} of {} assets'.format(replaced, num_assets))
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r"F:\PycharmProjects\UE\UE-asset-renamer\asset-renamer-ui.ui", self)

        # LineEdits
        self.replace_le = self.findChild(QLineEdit, "lineEdit")
        self.with_le = self.findChild(QLineEdit, "lineEdit_2")

        # Checkbox
        self.case_check = self.findChild(QCheckBox, "checkBox")

        # Buttons
        self.ok_bttn = self.findChild(QPushButton, "pushButton")
        self.ok_bttn.clicked.connect(self.rename)

    def rename(self):
        replace_text = self.replace_le.text()
        with_text = self.with_le.text()
        case_sens = self.case_check.isChecked()

        rename_assets(replace_text, with_text, case_sens)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

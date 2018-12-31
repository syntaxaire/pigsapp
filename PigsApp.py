import ctypes
from datetime import datetime, timedelta
import os
import sys
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon, QIntValidator

import pigs_ui

# execute and register the strategies
# this sys.path is used to load strategies.py from outside the executable after
# pyinstaller build
from tournament import run_tournament

sys.path.append(os.path.dirname(sys.executable))
from strategies import strategies

# this is necessary to set a taskbar icon in Windows
myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class PigsApp(QtWidgets.QApplication):
    def __init__(self, args):
        super(PigsApp, self).__init__(args)
        rounds = 10  # default number of games in tournament
        to_score = 100  # default score to play to
        self.MainWindow = QtWidgets.QMainWindow()
        self.icon = QIcon("pig_nose.ico")
        self.icon.addFile("pig-nose-16x16.png")
        self.icon.addFile("pig-nose-24x24.png")
        self.icon.addFile("pig-nose-32x32.png")
        self.icon.addFile("pig-nose-48x48.png")
        self.icon.addFile("pig-nose-256x256.png")
        self.setWindowIcon(self.icon)
        self.ui = pigs_ui.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.ui.rounds_lineEdit.setText(str(rounds))
        self.ui.rounds_lineEdit.setValidator(QIntValidator(1, 1_000_000, self))
        self.ui.score_lineEdit.setText(str(to_score))
        self.ui.score_lineEdit.setValidator(QIntValidator(1, 1_000_000, self))

        # dynamically add checkboxes for defined participant strategies
        self.stratboxes_and_strats = []
        for strategy in strategies:
            newbox = QtWidgets.QCheckBox(self.ui.centralwidget)
            newbox.setText(strategy.name)
            newbox.setToolTip(strategy.__doc__)
            newbox.setChecked(True)
            self.ui.participants_verticalLayout.addWidget(newbox)
            self.stratboxes_and_strats.append((newbox, strategy(0)))
        self.ui.startButton.clicked.connect(self.start_clicked)
        self.ui.checkall_pushButton.clicked.connect(self.check_all_strats)
        self.ui.uncheckall_pushButton.clicked.connect(self.uncheck_all_strats)
        self.exec_()

    def check_all_strats(self):
        for checkbox, _ in self.stratboxes_and_strats:
            checkbox.setChecked(True)

    def uncheck_all_strats(self):
        for checkbox, _ in self.stratboxes_and_strats:
            checkbox.setChecked(False)

    def start_clicked(self):
        checked_strategies = []
        for checkbox, player in self.stratboxes_and_strats:
            if checkbox.isChecked():
                checked_strategies.append(player)
        if len(checked_strategies) < 2:
            cur_text = self.ui.output_plainTextEdit.toPlainText()
            if len(cur_text) != 0:
                cur_text += "\n"
            cur_text += "Please select at least two strategies."
            self.ui.output_plainTextEdit.setPlainText(cur_text)
            return
        self.ui.startButton.setEnabled(False)
        rounds = int(self.ui.rounds_lineEdit.text())
        to_score = int(self.ui.score_lineEdit.text())
        pb = self.ui.progressBar
        outbox = self.ui.output_plainTextEdit

        tournament_start = datetime.now()
        last_updated = datetime.now()
        for progress, results in run_tournament(checked_strategies,
                                                rounds, to_score):
            pb.setValue(pb.maximum() * progress)
            # for long tournaments, give a text update if some time has passed
            # but not too often to avoid blurring numbers
            cur_timestamp = datetime.now()
            if (cur_timestamp - last_updated) > timedelta(seconds=0.5):
                outbox.setPlainText(prettify_results(results))
                last_updated = cur_timestamp
            self.processEvents()  # allow window moving, etc. while running
        outbox.setPlainText(prettify_results(results))
        tournament_end = datetime.now()
        winner = max(results, key=lambda x: results[x])
        winstr = f"Winning strategy: {winner}, {results[winner]}."
        outbox.appendPlainText(winstr)
        outbox.appendPlainText("Tournament complete in " +
                               str(tournament_end - tournament_start))
        self.ui.startButton.setEnabled(True)


def prettify_results(results):
    text = ""
    for player_name in results:
        text += f"{player_name}: {results[player_name]}\n"
    return text


if __name__ == '__main__':
    app = PigsApp(sys.argv)

from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QListView, QApplication, QMainWindow
from ui_form import Ui_MainWindow
import sys

# Create the application
app = QApplication(sys.argv)

mw = QMainWindow()
# Get a QListView
ui = Ui_MainWindow()
ui.setupUi(mw)
listView = ui.listView_2
# Create a QStandardItemModel
model = QStandardItemModel(listView)

# Add items to the model
for i in range(10):
    # Create a QStandardItem
    item = QStandardItem(f"Item {i}")
    # Add the item to the model
    model.appendRow(item)

# Set the model for the listView
listView.setModel(model)

# Show the listView
mw.show()

# Run the application
sys.exit(app.exec())

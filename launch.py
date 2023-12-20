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
listView1 = ui.listView
listView2 = ui.listView_2
listView3 = ui.listView_3
listView4 = ui.listView_4
# Create a QStandardItemModel
model = QStandardItemModel(listView1)
model2 = QStandardItemModel(listView2)
model3 = QStandardItemModel(listView3)
model4 = QStandardItemModel(listView4)

models = [model,model2, model3, model4]
listViews = [listView1, listView2, listView3, listView4]
# Add items to the model
for model in models:
    for i in range(10):
        # Create a QStandardItem
        item = QStandardItem(f"Item {i}")
        # Add the item to the model
        model.appendRow(item)

# Set the model for the listView
for i, lv in enumerate(listViews):
    lv.setModel(models[i])

# Show the listView
mw.show()

# Run the application
sys.exit(app.exec())

import sys
from PyQt5.QtWidgets import QApplication
from model.client_model import ClientModel
from controller.client_controller import ClientController
from view.client_view import ClientView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = ClientModel()
    controller = ClientController(model)
    view = ClientView()
    view.set_controller(controller)
    view.show()
    sys.exit(app.exec_())

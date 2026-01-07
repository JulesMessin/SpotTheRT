import sys
from PyQt5.QtWidgets import QApplication
from model.client_model import ClientModel
from controller.client_controller import ClientController
from view.login_view import LoginView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = ClientModel()
    view = LoginView()
    controller = ClientController(model,view)
    view.set_controller(controller)
    view.show()
    sys.exit(app.exec_())

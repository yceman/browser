import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self, parent = ..., flags = ...):
        super().__init__(parent, flags)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com.br"))
        self.setCentralWidget(self.browser)
        self.navbar = QToolBar()
        self.addToolBar("Navigation", self.navbar)

        back_btn = QPushButton("Voltar")
        back_btn.clicked.connect(self.browser.back)
        self.navbar.addWidget(back_btn)

        forward_btn = QPushButton("Avançar")
        forward_btn.clicked.connect(self.browser.forward)
        self.navbar.addWidget(forward_btn)

        reload_btn = QPushButton("Recarregar")
        reload_btn.clicked.connect(self.browser.reload)
        self.navbar.addWidget(reload_btn)

        home_btn = QPushButton("Home")
        home_btn.clicked.connect(lambda: self.browser.setUrl(QUrl("https://www.google.com.br")))
        self.navbar.addWidget(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

        def navigate_to_url(self):
            url = self.url_bar.text()
            if not url.startswith("http"):
                url = "http://" + url

            self.browser.setUrl(QUrl(url))

        def update_url(self, q):
            self.url_bar.setText(q.toString())

        app = QApplication(sys.argv)
        QApplication.setApplicationName("My Browser")
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
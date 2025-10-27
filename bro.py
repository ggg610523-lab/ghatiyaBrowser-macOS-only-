import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QLineEdit, QToolBar, QAction, QMenu, QMenuBar
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

HOME_URL = "https://www.google.com"

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Browser App")
        self.setGeometry(100, 100, 1200, 800)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        # Menu
        self.menu = QMenuBar()
        self.setMenuBar(self.menu)
        file_menu = self.menu.addMenu("File")
        new_tab_action = QAction("New Tab", self)
        new_tab_action.triggered.connect(lambda: self.add_new_tab(HOME_URL, "New Tab"))
        file_menu.addAction(new_tab_action)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Toolbar
        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        back_btn = QAction("←", self)
        back_btn.triggered.connect(lambda: self.current_tab().back())
        nav_bar.addAction(back_btn)

        forward_btn = QAction("→", self)
        forward_btn.triggered.connect(lambda: self.current_tab().forward())
        nav_bar.addAction(forward_btn)

        reload_btn = QAction("⟳", self)
        reload_btn.triggered.connect(lambda: self.current_tab().reload())
        nav_bar.addAction(reload_btn)

        home_btn = QAction("🏠", self)
        home_btn.triggered.connect(self.go_home)
        nav_bar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_bar.addWidget(self.url_bar)

        new_tab_btn = QAction("➕", self)
        new_tab_btn.triggered.connect(lambda _: self.add_new_tab(HOME_URL, "New Tab"))
        nav_bar.addAction(new_tab_btn)

        # Add initial tab
        self.add_new_tab(HOME_URL, "Home")

        self.show()

    # Tab management
    def current_tab(self):
        return self.tabs.currentWidget()

    def add_new_tab(self, url, label):
        browser = QWebEngineView()
        browser.setUrl(QUrl(url))
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda q, b=browser: self.update_url(q, b))
        browser.loadFinished.connect(lambda _, b=browser: self.tabs.setTabText(self.tabs.indexOf(b), b.page().title()))

    def close_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.removeTab(i)

    # Navigation
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.current_tab().setUrl(QUrl(url))

    def update_url(self, q, browser):
        if browser == self.current_tab():
            self.url_bar.setText(q.toString())

    def go_home(self):
        self.current_tab().setUrl(QUrl(HOME_URL))

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    sys.exit(app.exec_())


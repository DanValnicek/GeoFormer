# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QIcon)
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import (QMenu,
                               QMenuBar, QSizePolicy, QSplitter, QStatusBar,
                               QTabWidget, QToolBar, QVBoxLayout,
                               QWidget, QWidgetAction)

from src.VideoPresentationProcessingWidget import VideoPresentationProcessingWidget
from src.pdfviewer.videoOpener import VideoOpener


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon()
        iconThemeName = u"document-open"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/icons/images/document-open.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionOpen.setIcon(icon)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon1 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.actionQuit.setIcon(icon1)
        self.actionProcessVideoAndPresentation = QAction(MainWindow)
        self.actionProcessVideoAndPresentation.triggered.connect(MainWindow.open_video_presentation_processor)
        self.actionProcessVideoAndPresentation.setObjectName(u"Create video slide annotation")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon(QIcon.fromTheme(u"help-about"))
        self.actionAbout.setIcon(icon2)
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.actionZoom_In = QAction(MainWindow)
        self.actionZoom_In.setObjectName(u"actionZoom_In")
        icon3 = QIcon()
        iconThemeName = u"zoom-in"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u":/icons/images/zoom-in.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionZoom_In.setIcon(icon3)
        self.actionZoom_Out = QAction(MainWindow)
        self.actionZoom_Out.setObjectName(u"actionZoom_Out")
        icon4 = QIcon()
        iconThemeName = u"zoom-out"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u":/icons/images/zoom-out.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionZoom_Out.setIcon(icon4)
        self.actionPrevious_Page = QAction(MainWindow)
        self.actionPrevious_Page.setObjectName(u"actionPrevious_Page")
        icon5 = QIcon()
        iconThemeName = u"go-previous-view-page"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u":/icons/images/go-previous-view-page.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionPrevious_Page.setIcon(icon5)
        self.actionNext_Page = QAction(MainWindow)
        self.actionNext_Page.setObjectName(u"actionNext_Page")
        icon6 = QIcon()
        iconThemeName = u"go-next-view-page"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u":/icons/images/go-next-view-page.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionNext_Page.setIcon(icon6)
        self.actionContinuous = QAction(MainWindow)
        self.actionContinuous.setObjectName(u"actionContinuous")
        self.actionContinuous.setCheckable(True)
        self.actionBack = QAction(MainWindow)
        self.actionBack.setObjectName(u"actionBack")
        self.actionBack.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/go-previous-view.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionBack.setIcon(icon7)
        self.actionForward = QAction(MainWindow)
        self.actionForward.setObjectName(u"actionForward")
        self.actionForward.setEnabled(False)
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/go-next-view.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionForward.setIcon(icon8)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setDocumentMode(False)
        self.pdfView = QPdfView(self.splitter)
        self.pdfView.setPageMode(QPdfView.PageMode.MultiPage)
        self.pdfView.setObjectName(u"pdfView")
        self.splitter.addWidget(self.tabWidget)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pdfView.sizePolicy().hasHeightForWidth())
        self.pdfView.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.pdfView)

        self.verticalLayout_2.addWidget(self.splitter)

        self.mainToolBar = QToolBar(MainWindow)
        self.openVidBtn = VideoOpener(MainWindow.document_location_changed, self.pdfView)
        self.openVidBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.openVidBtn.setObjectName(u"openVidBtn")
        self.tabWidget.addTab(self.openVidBtn, "")

        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 700, 26))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar.setObjectName(u"mainToolBar")
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionProcessVideoAndPresentation)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addAction(self.actionPrevious_Page)
        self.menuView.addAction(self.actionNext_Page)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionContinuous)
        self.mainToolBar.addAction(self.actionOpen)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionZoom_Out)
        self.mainToolBar.addAction(self.actionZoom_In)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionBack)
        self.mainToolBar.addAction(self.actionForward)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PDF Viewer", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.actionProcessVideoAndPresentation.setText(
            QCoreApplication.translate("MainWindow", u"Annotate slides in video"))
        # if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
        # endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        # if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
        # endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.actionZoom_In.setText(QCoreApplication.translate("MainWindow", u"Zoom In", None))
        # if QT_CONFIG(shortcut)
        self.actionZoom_In.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl++", None))
        # endif // QT_CONFIG(shortcut)
        self.actionZoom_Out.setText(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
        # if QT_CONFIG(shortcut)
        self.actionZoom_Out.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+-", None))
        # endif // QT_CONFIG(shortcut)
        self.actionPrevious_Page.setText(QCoreApplication.translate("MainWindow", u"Previous Page", None))
        # if QT_CONFIG(shortcut)
        self.actionPrevious_Page.setShortcut(QCoreApplication.translate("MainWindow", u"PgUp", None))
        # endif // QT_CONFIG(shortcut)
        self.actionNext_Page.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        # if QT_CONFIG(shortcut)
        self.actionNext_Page.setShortcut(QCoreApplication.translate("MainWindow", u"PgDown", None))
        # endif // QT_CONFIG(shortcut)
        self.actionContinuous.setText(QCoreApplication.translate("MainWindow", u"Continuous", None))
        self.actionBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        # if QT_CONFIG(tooltip)
        self.actionBack.setToolTip(QCoreApplication.translate("MainWindow", u"back to previous view", None))
        # endif // QT_CONFIG(tooltip)
        self.actionForward.setText(QCoreApplication.translate("MainWindow", u"Forward", None))
        # if QT_CONFIG(tooltip)
        self.actionForward.setToolTip(QCoreApplication.translate("MainWindow", u"forward to next view", None))
        # endif // QT_CONFIG(tooltip)
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.bookmarkTab), QCoreApplication.translate("MainWindow", u"Bookmarks", None))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.pagesTab),
        #                           QCoreApplication.translate("MainWindow", u"Pages", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.openVidBtn),
                                  QCoreApplication.translate("MainWindow", u"Video Intervals", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

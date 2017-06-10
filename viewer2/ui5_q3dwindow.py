# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis3\python\developing_plugins\Qgis2threejs\viewer2\q3dwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Q3DWindow(object):
    def setupUi(self, Q3DWindow):
        Q3DWindow.setObjectName("Q3DWindow")
        Q3DWindow.resize(757, 580)
        Q3DWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(Q3DWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webView = Q3DView(self.centralwidget)
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        Q3DWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Q3DWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menubar.setObjectName("menubar")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        self.menuExport = QtWidgets.QMenu(self.menuProject)
        self.menuExport.setObjectName("menuExport")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuCamera = QtWidgets.QMenu(self.menuView)
        self.menuCamera.setObjectName("menuCamera")
        self.menuControls = QtWidgets.QMenu(self.menuView)
        self.menuControls.setObjectName("menuControls")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuPanels = QtWidgets.QMenu(self.menuWindow)
        self.menuPanels.setObjectName("menuPanels")
        Q3DWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Q3DWindow)
        self.statusbar.setObjectName("statusbar")
        Q3DWindow.setStatusBar(self.statusbar)
        self.dockWidgetProperties = QtWidgets.QDockWidget(Q3DWindow)
        self.dockWidgetProperties.setObjectName("dockWidgetProperties")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeView = Q3DTreeView(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setHeaderHidden(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.dockWidgetProperties.setWidget(self.dockWidgetContents)
        Q3DWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetProperties)
        self.toolBar = QtWidgets.QToolBar(Q3DWindow)
        self.toolBar.setObjectName("toolBar")
        Q3DWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidgetConsole = QtWidgets.QDockWidget(Q3DWindow)
        self.dockWidgetConsole.setFloating(False)
        self.dockWidgetConsole.setObjectName("dockWidgetConsole")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidgetDebugView = QtWidgets.QListWidget(self.dockWidgetContents_2)
        self.listWidgetDebugView.setObjectName("listWidgetDebugView")
        self.verticalLayout_3.addWidget(self.listWidgetDebugView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditInputBox = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.lineEditInputBox.setObjectName("lineEditInputBox")
        self.horizontalLayout.addWidget(self.lineEditInputBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.dockWidgetConsole.setWidget(self.dockWidgetContents_2)
        Q3DWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetConsole)
        self.actionSTL_format = QtWidgets.QAction(Q3DWindow)
        self.actionSTL_format.setEnabled(False)
        self.actionSTL_format.setObjectName("actionSTL_format")
        self.actionWorld_Settings = QtWidgets.QAction(Q3DWindow)
        self.actionWorld_Settings.setEnabled(False)
        self.actionWorld_Settings.setObjectName("actionWorld_Settings")
        self.actionPerspective = QtWidgets.QAction(Q3DWindow)
        self.actionPerspective.setCheckable(True)
        self.actionPerspective.setChecked(True)
        self.actionPerspective.setObjectName("actionPerspective")
        self.actionOrthogonal = QtWidgets.QAction(Q3DWindow)
        self.actionOrthogonal.setCheckable(True)
        self.actionOrthogonal.setEnabled(False)
        self.actionOrthogonal.setObjectName("actionOrthogonal")
        self.actionReload = QtWidgets.QAction(Q3DWindow)
        self.actionReload.setObjectName("actionReload")
        self.actionAlways_on_Top = QtWidgets.QAction(Q3DWindow)
        self.actionAlways_on_Top.setCheckable(True)
        self.actionAlways_on_Top.setChecked(False)
        self.actionAlways_on_Top.setObjectName("actionAlways_on_Top")
        self.actionExport_to_Web = QtWidgets.QAction(Q3DWindow)
        self.actionExport_to_Web.setEnabled(False)
        self.actionExport_to_Web.setObjectName("actionExport_to_Web")
        self.actionExport_as_Image = QtWidgets.QAction(Q3DWindow)
        self.actionExport_as_Image.setEnabled(False)
        self.actionExport_as_Image.setObjectName("actionExport_as_Image")
        self.actionReset_Camera_Position = QtWidgets.QAction(Q3DWindow)
        self.actionReset_Camera_Position.setObjectName("actionReset_Camera_Position")
        self.actionOrbit = QtWidgets.QAction(Q3DWindow)
        self.actionOrbit.setCheckable(True)
        self.actionOrbit.setChecked(True)
        self.actionOrbit.setObjectName("actionOrbit")
        self.actionTrackball = QtWidgets.QAction(Q3DWindow)
        self.actionTrackball.setCheckable(True)
        self.actionTrackball.setEnabled(False)
        self.actionTrackball.setObjectName("actionTrackball")
        self.actionLayer_Panel = QtWidgets.QAction(Q3DWindow)
        self.actionLayer_Panel.setCheckable(True)
        self.actionLayer_Panel.setChecked(True)
        self.actionLayer_Panel.setEnabled(False)
        self.actionLayer_Panel.setObjectName("actionLayer_Panel")
        self.menuExport.addAction(self.actionExport_to_Web)
        self.menuExport.addSeparator()
        self.menuExport.addAction(self.actionExport_as_Image)
        self.menuExport.addAction(self.actionSTL_format)
        self.menuProject.addAction(self.menuExport.menuAction())
        self.menuCamera.addAction(self.actionPerspective)
        self.menuCamera.addAction(self.actionOrthogonal)
        self.menuControls.addAction(self.actionOrbit)
        self.menuControls.addAction(self.actionTrackball)
        self.menuView.addAction(self.actionWorld_Settings)
        self.menuView.addAction(self.menuCamera.menuAction())
        self.menuView.addAction(self.menuControls.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionReset_Camera_Position)
        self.menuView.addAction(self.actionReload)
        self.menuWindow.addAction(self.menuPanels.menuAction())
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionAlways_on_Top)
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExport_to_Web)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionReset_Camera_Position)
        self.toolBar.addAction(self.actionReload)

        self.retranslateUi(Q3DWindow)
        QtCore.QMetaObject.connectSlotsByName(Q3DWindow)

    def retranslateUi(self, Q3DWindow):
        _translate = QtCore.QCoreApplication.translate
        Q3DWindow.setWindowTitle(_translate("Q3DWindow", "Live Exporter - Qgis2threejs"))
        self.menuProject.setTitle(_translate("Q3DWindow", "&Project"))
        self.menuExport.setTitle(_translate("Q3DWindow", "Export"))
        self.menuView.setTitle(_translate("Q3DWindow", "&View"))
        self.menuCamera.setTitle(_translate("Q3DWindow", "Camera"))
        self.menuControls.setTitle(_translate("Q3DWindow", "Controls"))
        self.menuWindow.setTitle(_translate("Q3DWindow", "&Window"))
        self.menuPanels.setTitle(_translate("Q3DWindow", "Panels"))
        self.dockWidgetProperties.setWindowTitle(_translate("Q3DWindow", "Properties"))
        self.toolBar.setWindowTitle(_translate("Q3DWindow", "toolBar"))
        self.dockWidgetConsole.setWindowTitle(_translate("Q3DWindow", "Console"))
        self.label.setText(_translate("Q3DWindow", ">>>"))
        self.actionSTL_format.setText(_translate("Q3DWindow", "Export as STL format"))
        self.actionWorld_Settings.setText(_translate("Q3DWindow", "World Settings..."))
        self.actionPerspective.setText(_translate("Q3DWindow", "Perspective"))
        self.actionOrthogonal.setText(_translate("Q3DWindow", "Orthographic"))
        self.actionReload.setText(_translate("Q3DWindow", "Reload"))
        self.actionReload.setShortcut(_translate("Q3DWindow", "F5"))
        self.actionAlways_on_Top.setText(_translate("Q3DWindow", "Always on Top"))
        self.actionExport_to_Web.setText(_translate("Q3DWindow", "Export to Web..."))
        self.actionExport_as_Image.setText(_translate("Q3DWindow", "Export as Image"))
        self.actionReset_Camera_Position.setText(_translate("Q3DWindow", "Reset Camera Position"))
        self.actionReset_Camera_Position.setShortcut(_translate("Q3DWindow", "Shift+R"))
        self.actionOrbit.setText(_translate("Q3DWindow", "Orbit"))
        self.actionTrackball.setText(_translate("Q3DWindow", "Trackball"))
        self.actionLayer_Panel.setText(_translate("Q3DWindow", "Layer Panel"))

from .q3dtreeview import Q3DTreeView
from .q3dview import Q3DView

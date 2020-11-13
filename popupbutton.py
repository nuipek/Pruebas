from PyQt5.QtWidgets import QWidget, QToolBar,QMenu,QToolButton,QPushButton,QSizePolicy

def addAction(widget, actionNameOrList,parent=None):
    try:
        if isinstance(actionNameOrList, str):
            tname = actionNameOrList.lower()
            if tname == "|":
                widget.addSeparator()
            else:
                action = iface.mainWindow().findChild(QAction,actionNameOrList)
                if action is not None:
                    widget.addAction(action)
                else:
                    widget.addWidget(QLabel(actionNameOrList,parent))
        elif isinstance(actionNameOrList, list):
            widget.addWidget(createToolButton(actionNameOrList,parent))
    except Exception as e:
        info(e)

def createToolButton( actionNamesList, parent=None):
    try:
        menu = QMenu(parent)
        for an in actionNamesList:
            addAction(menu,an,parent)
            actions = [a for a in menu.actions()]
        tb = QToolButton()
        tb.setDefaultAction(actions[0])
        tb.setMenu(menu)
        tb.setPopupMode(QToolButton.MenuButtonPopup)
        menu.triggered.connect(tb.setDefaultAction)
        return tb
    except Exception as e:
        info(e)

def info(*args):
    print(args)

try:
    tb_name = "mytb_test"
    tb = iface.mainWindow().findChild(QToolBar,tb_name)
    if tb is None:#create the toolbar
        tb = QToolBar(iface.mainWindow())
        tb.setObjectName(tb_name)
        tb.setWindowTitle("My Toolbar")
        iface.mainWindow().addToolBarBreak()#toolbar in new line
        iface.addToolBar(tb)
    else:
        tb.clear()
    #add actions to tb
    actionsList =["MyAPp:","mActionSaveProject","|","mActionZoomIn","mActionZoomOut",["mActionMeasure","mActionMeasureAngle","mActionMeasureArea"]]
    for a in actionsList:
        addAction(tb,a)
    #add a hide button
    btnObjectName = 'mClose_' + tb_name
    btn = tb.findChild(QPushButton, btnObjectName)
    if btn is None:
        btnHide = QPushButton()
        btnHide.setObjectName(btnObjectName)
        btnHide.setMaximumWidth(15)
        btnHide.setToolTip('close')
        btnHide.clicked.connect(lambda: tb.setHidden(True))
        #spacer
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tb.addWidget(spacer)
        tb.addWidget(btnHide)
    tb.show()
except Exception as e:
    info(e)

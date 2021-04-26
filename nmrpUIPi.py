## nmrpUi.py
## Author: Eddie Grabert

from PyQt5 import QtGui, QtWidgets
import sys
import os

class nmrpGUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(nmrpGUI, self).__init__()
        self.setGeometry(0,0,800,400)
        self.setWindowTitle("Network Management Raspberry Pi")
        self.setupUI()

    ## define structure
    def setupUI(self):

        self.window = QtWidgets.QWidget(self)
        self.window.setObjectName("window")
        self.setStyleSheet(" QToolTip{color: black ; font: 12pt}")

        font = QtGui.QFont()
        font.setPointSize(12)

        self.tabs = QtWidgets.QTabWidget(self.window)
        self.tabs.setGeometry(0, 0, 800, 400)
        self.tabs.setFont(font)

        # Network Scanner tab #####################################
        self.setupTab1(font)

        # Port Scanner tab ########################################
        self.setupTab2(font)

        # TraceRoute tab ##########################################
        self.setupTab3(font)

        # Speed Test tab ###########################################
        self.setupTab4(font)

        self.setCentralWidget(self.window)
        self.tabs.setCurrentIndex(0)

    ## Tab Methods
    def setupTab1(self, font): ####################################
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab1")
        self.tab_1.setFont(font)

        self.tab_1_Layout = QtWidgets.QHBoxLayout(self.tab_1)
        self.tab_1_Layout.setSpacing(0)
        self.tab_1_Layout.setObjectName("tab1_Layout")
        self.tab_1_Layout.setContentsMargins(0, 0, 0, 0)

        # Input Section
        self.input_Layout_NS = QtWidgets.QVBoxLayout()
        self.input_Layout_NS.setSpacing(9)
        self.input_Layout_NS.setObjectName("input_Layout_NS")
        self.input_Layout_NS.setContentsMargins(10, 10, 10, 10)

        self.label_Layout_NS = QtWidgets.QHBoxLayout()
        self.label_Layout_NS.setSpacing(0)
        self.label_Layout_NS.setObjectName("label_Layout_NS")

        self.label_NS = QtWidgets.QLabel(self.tab_1)
        self.label_NS.setObjectName("label_NS")
        self.label_NS.setMinimumSize(120, 31)
        self.label_NS.setText("Run to show the ")
        self.label_Layout_NS.addWidget(self.label_NS)

        self.device_label_NS = QtWidgets.QLabel(self.tab_1)
        self.device_label_NS.setObjectName("device_label_NS")
        self.device_label_NS.setMinimumSize(119, 31)
        self.device_label_NS.setText("network devices")
        self.device_label_NS.setToolTip("These are the devices that are \ncurrently connected to your network.")
        self.label_Layout_NS.addWidget(self.device_label_NS)

        self.input_Layout_NS.addLayout(self.label_Layout_NS)

        self.runNSButton = QtWidgets.QPushButton(self.tab_1)
        self.runNSButton.setObjectName("runNSButton")
        self.runNSButton.setMinimumSize(241, 31)
        self.runNSButton.setText("Run Network Scanner")
        self.runNSButton.clicked.connect(lambda: self.pressed_runNSButton())
        self.input_Layout_NS.addWidget(self.runNSButton)

        self.space_widget_NS = QtWidgets.QWidget(self.tab_1)
        self.space_widget_NS.setObjectName("space_widget_NS")
        self.space_widget_NS.setMinimumSize(241, 266)
        self.input_Layout_NS.addWidget(self.space_widget_NS)

        self.tab_1_Layout.addLayout(self.input_Layout_NS)

        # Output Section
        self.output_Layout_NS = QtWidgets.QVBoxLayout()
        self.output_Layout_NS.setSpacing(0)
        self.output_Layout_NS.setObjectName("output_Layout_NS")
        self.output_Layout_NS.setContentsMargins(10, 10, 10, 10)

        self.scroll_Area_NS = QtWidgets.QScrollArea(self.tab_1)
        self.scroll_Area_NS.setObjectName("scroll_Area_NS")
        self.scroll_Area_NS.setGeometry(0, 0, 513, 348)
        self.scroll_Area_NS.setWidgetResizable(True)

        self.scroll_Area_Contents_NS = QtWidgets.QWidget()
        self.scroll_Area_Contents_NS.setObjectName("scroll_Area_Contents_NS")
        self.scroll_Area_Contents_NS.setGeometry(0, 0, 513, 348)

        self.scroll_Layout_NS = QtWidgets.QVBoxLayout(self.scroll_Area_Contents_NS)
        self.scroll_Layout_NS.setObjectName("scroll_Layout_NS")
        self.scroll_Layout_NS.setContentsMargins(0, 0, 0, 0)

        self.table_results_NS = QtWidgets.QTableWidget()
        self.table_results_NS.setObjectName("table_results_NS")
        self.table_results_NS.setRowCount(0)
        self.table_results_NS.setColumnCount(0)
        self.table_results_NS.move(0,0)
        self.scroll_Layout_NS.addWidget(self.table_results_NS)
        self.macInfo = ""

        self.scroll_Area_NS.setWidget(self.scroll_Area_Contents_NS)
        self.output_Layout_NS.addWidget(self.scroll_Area_NS)

        self.tab_1_Layout.addLayout(self.output_Layout_NS)

        self.tabs.addTab(self.tab_1, "Network Scanner")

    def setupTab2(self, font): ####################################
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setFont(font)
        
        self.tab_2_Layout = QtWidgets.QHBoxLayout(self.tab_2)
        self.tab_2_Layout.setSpacing(0)
        self.tab_2_Layout.setObjectName("tab_2_Layout")
        self.tab_2_Layout.setContentsMargins(0, 0, 0, 0)

        # Input Section
        self.input_Layout_PS = QtWidgets.QVBoxLayout()
        self.input_Layout_PS.setSpacing(9)
        self.input_Layout_PS.setObjectName("input_Layout_PS")
        self.input_Layout_PS.setContentsMargins(10, 10, 10, 10)

        self.label_Layout_PS = QtWidgets.QHBoxLayout()
        self.label_Layout_PS.setSpacing(0)
        self.label_Layout_PS.setObjectName("label_Layout_PS")

        self.label_PS = QtWidgets.QLabel(self.tab_2)
        self.label_PS.setObjectName("label_PS")
        self.label_PS.setMinimumSize(120, 31)
        self.label_PS.setText("Run to show the ")
        self.label_Layout_PS.addWidget(self.label_PS)

        self.port_label_PS = QtWidgets.QLabel(self.tab_2)
        self.port_label_PS.setObjectName("port_label_PS")
        self.port_label_PS.setMinimumSize(119, 31)
        self.port_label_PS.setText("open ports")
        self.port_label_PS.setToolTip("A port is a path for internal or external \ncommunication. When the port is open, \nit means that the port is allowing traffic \nto flow through it.")
        self.label_Layout_PS.addWidget(self.port_label_PS)

        self.input_Layout_PS.addLayout(self.label_Layout_PS)

        self.runPSButton = QtWidgets.QPushButton(self.tab_2)
        self.runPSButton.setObjectName("runPSButton")
        self.runPSButton.setMinimumSize(241, 31)
        self.runPSButton.setText("Run Port Scanner")
        self.runPSButton.clicked.connect(lambda: self.pressed_runPSButton())
        self.input_Layout_PS.addWidget(self.runPSButton)

        self.space_widget_PS = QtWidgets.QWidget(self.tab_2)
        self.space_widget_PS.setObjectName("space_widget_PS")
        self.space_widget_PS.setMinimumSize(241, 266)

        self.input_Layout_PS.addWidget(self.space_widget_PS)

        self.tab_2_Layout.addLayout(self.input_Layout_PS)

        # Output Section
        self.output_Layout_PS = QtWidgets.QVBoxLayout()
        self.output_Layout_PS.setSpacing(0)
        self.output_Layout_PS.setObjectName("output_Layout_PS")
        self.output_Layout_PS.setContentsMargins(10, 10, 10, 10)

        self.scroll_Bounds_PS = QtWidgets.QWidget(self.tab_2)
        self.scroll_Bounds_PS.setObjectName("scroll_Bounds_PS")
        self.scroll_Bounds_PS.setMinimumSize(513, 348)

        self.scroll_Area_PS = QtWidgets.QScrollArea(self.scroll_Bounds_PS)
        self.scroll_Area_PS.setObjectName("scroll_Area_PS")
        self.scroll_Area_PS.setGeometry(0, 0, 513, 348)
        self.scroll_Area_PS.setWidgetResizable(True)

        self.scroll_Area_Contents_PS = QtWidgets.QWidget()
        self.scroll_Area_Contents_PS.setObjectName("scroll_Area_Contents_PS")
        self.scroll_Area_Contents_PS.setGeometry(0, 0, 511, 346)

        self.scroll_Layout_PS = QtWidgets.QVBoxLayout(self.scroll_Area_Contents_PS)
        self.scroll_Layout_PS.setObjectName("scroll_Layout_PS")
        self.scroll_Layout_PS.setContentsMargins(0, 0, 0, 0)

        self.portNames = {"21": "FTP - File Transfer Protocol", "22": "SSH - Secure Shell Protocol",
             "23": "Telnet", "25": "SMTP - Simple Mail Transfer Protocol",
             "53": "DNS - Domain Name System", "80": "HTTP - Hypertext Transfer Protocol",
             "135": "Microsoft DCOM - Distributed Component Object Model", "443": "HTTPS - Hypertext Transfer Protocol Secure",
             "1433": "Microsoft SQL - Structured Query Language", "3389": "RDP - Remote Desktop Protocol"}
        self.table_results_PS = QtWidgets.QTableWidget()
        self.table_results_PS.setObjectName("table_results_PS")
        self.table_results_PS.setRowCount(0)
        self.table_results_PS.setColumnCount(0)
        self.table_results_PS.move(0,0)
        self.scroll_Layout_PS.addWidget(self.table_results_PS)

        self.scroll_Area_PS.setWidget(self.scroll_Area_Contents_PS)
        self.output_Layout_PS.addWidget(self.scroll_Bounds_PS)
        self.tab_2_Layout.addLayout(self.output_Layout_PS)
        
        self.tabs.addTab(self.tab_2, "Port Scanner")

    def setupTab3(self, font): ####################################
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tab_3.setFont(font)

        self.tab_3_Layout = QtWidgets.QHBoxLayout(self.tab_3)
        self.tab_3_Layout.setSpacing(0)
        self.tab_3_Layout.setObjectName("tab_3_Layout")
        self.tab_3_Layout.setContentsMargins(0, 0, 0, 0)

        # Input Section
        self.input_Layout_TR = QtWidgets.QVBoxLayout()
        self.input_Layout_TR.setSpacing(9)
        self.input_Layout_TR.setObjectName("input_Layout_TR")
        self.input_Layout_TR.setContentsMargins(10, 10, 10, 10)

        self.label_Layout_TR_1 = QtWidgets.QHBoxLayout()
        self.label_Layout_TR_1.setSpacing(0)
        self.label_Layout_TR_1.setObjectName("label_Layout_TR_1")

        self.label_TR_1 = QtWidgets.QLabel(self.tab_2)
        self.label_TR_1.setObjectName("label_TR_1")
        self.label_TR_1.setMinimumSize(191, 31)
        self.label_TR_1.setText("Enter the URL you want to ")
        self.label_Layout_TR_1.addWidget(self.label_TR_1)

        self.trace_label_TR = QtWidgets.QLabel(self.tab_2)
        self.trace_label_TR.setObjectName("trace_label_TR")
        self.trace_label_TR.setMinimumSize(50, 31)
        self.trace_label_TR.setText("Trace: ")
        self.trace_label_TR.setToolTip("A trace route follows the path \nthat a packet would take on its \njourney from host to destination.")
        self.label_Layout_TR_1.addWidget(self.trace_label_TR)

        self.input_Layout_TR.addLayout(self.label_Layout_TR_1)

        self.input_Url = QtWidgets.QLineEdit(self.tab_3)
        self.input_Url.setObjectName("input_Url")
        self.input_Url.setMinimumSize(241, 31)
        self.input_Url.setText("")
        self.input_Layout_TR.addWidget(self.input_Url)

        self.label_Layout_TR_2 = QtWidgets.QHBoxLayout()
        self.label_Layout_TR_2.setSpacing(0)
        self.label_Layout_TR_2.setObjectName("label_Layout_TR_2")

        self.label_TR_2 = QtWidgets.QLabel(self.tab_2)
        self.label_TR_2.setObjectName("label_TR_2")
        self.label_TR_2.setMinimumSize(83, 31)
        self.label_TR_2.setText("Select your ")
        self.label_Layout_TR_2.addWidget(self.label_TR_2)

        self.ttl_label_TR = QtWidgets.QLabel(self.tab_2)
        self.ttl_label_TR.setObjectName("ttl_label_TR")
        self.ttl_label_TR.setMinimumSize(159, 31)
        self.ttl_label_TR.setText("Time to Live: ")
        self.ttl_label_TR.setToolTip("When a packet is sent from your computer \nto a destination, it has a predetermined \namount of time before it expires and is no \nlonger active. This is the packet's \"time to live\".")
        self.label_Layout_TR_2.addWidget(self.ttl_label_TR)

        self.input_Layout_TR.addLayout(self.label_Layout_TR_2)

        self.button_Layout_TR = QtWidgets.QHBoxLayout()
        self.button_Layout_TR.setSpacing(26)
        self.button_Layout_TR.setObjectName("button_Layout_TR")

        self.button_dTTL_TR = QtWidgets.QPushButton(self.tab_3)
        self.button_dTTL_TR.setObjectName("button_dTTL_TR")
        self.button_dTTL_TR.setMinimumSize(82, 31)
        self.button_dTTL_TR.setText("<<")
        self.button_dTTL_TR.clicked.connect(lambda: self.pressed_dTTL_TR())
        self.button_Layout_TR.addWidget(self.button_dTTL_TR)

        self.input_Ttl = QtWidgets.QLabel(self.tab_3)
        self.input_Ttl.setObjectName("input_Ttl")
        self.input_Ttl.setMinimumSize(21, 31)
        self.input_Ttl.setText("10")
        self.button_Layout_TR.addWidget(self.input_Ttl)

        self.button_iTTL_TR = QtWidgets.QPushButton(self.tab_3)
        self.button_iTTL_TR.setObjectName("button_iTTL_TR")
        self.button_iTTL_TR.setMinimumSize(82, 31)
        self.button_iTTL_TR.setText(">>")
        self.button_iTTL_TR.clicked.connect(lambda: self.pressed_iTTL_TR())
        self.button_Layout_TR.addWidget(self.button_iTTL_TR)

        self.input_Layout_TR.addLayout(self.button_Layout_TR)

        self.runTRButton = QtWidgets.QPushButton(self.tab_3)
        self.runTRButton.setObjectName("runTRButton")
        self.runTRButton.setMinimumSize(241, 31)
        self.runTRButton.setText("Run TraceRoute")
        self.runTRButton.clicked.connect(lambda: self.pressed_runTRButton())
        self.input_Layout_TR.addWidget(self.runTRButton)

        self.space_widget_TR = QtWidgets.QWidget(self.tab_3)
        self.space_widget_TR.setObjectName("space_widget_TR")
        self.space_widget_TR.setMinimumSize(241, 142)

        self.input_Layout_TR.addWidget(self.space_widget_TR)

        self.tab_3_Layout.addLayout(self.input_Layout_TR)

        # Output Section
        self.output_Layout_TR = QtWidgets.QVBoxLayout()
        self.output_Layout_TR.setSpacing(0)
        self.output_Layout_TR.setObjectName("output_Layout_TR")
        self.output_Layout_TR.setContentsMargins(10, 10, 10, 10)

        self.scroll_Bounds_TR = QtWidgets.QWidget(self.tab_3)
        self.scroll_Bounds_TR.setObjectName("scroll_Bounds_TR")
        self.scroll_Bounds_TR.setMinimumSize(513, 348)

        self.scroll_Area_TR = QtWidgets.QScrollArea(self.scroll_Bounds_TR)
        self.scroll_Area_TR.setObjectName("scroll_Area_TR")
        self.scroll_Area_TR.setGeometry(0, 0, 513, 348)
        self.scroll_Area_TR.setWidgetResizable(True)

        self.scroll_Area_Contents_TR = QtWidgets.QWidget()
        self.scroll_Area_Contents_TR.setObjectName("scroll_Area_Contents_TR")
        self.scroll_Area_Contents_TR.setGeometry(0, 0, 511, 346)

        self.scroll_Layout_TR = QtWidgets.QVBoxLayout(self.scroll_Area_Contents_TR)
        self.scroll_Layout_TR.setObjectName("scroll_Layout_TR")
        self.scroll_Layout_TR.setContentsMargins(0, 0, 0, 0)

        self.traceCodes = {"11": "progressing", "SA": "destination reached"}
        self.ipInfo = ""

        self.table_results_TR = QtWidgets.QTableWidget()
        self.table_results_TR.setObjectName("table_results_TR")
        self.table_results_TR.setRowCount(0)
        self.table_results_TR.setColumnCount(0)
        self.table_results_TR.move(0,0)
        self.scroll_Layout_TR.addWidget(self.table_results_TR)

        self.scroll_Area_TR.setWidget(self.scroll_Area_Contents_TR)
        self.output_Layout_TR.addWidget(self.scroll_Bounds_TR)
        self.tab_3_Layout.addLayout(self.output_Layout_TR)

        self.tabs.addTab(self.tab_3, "TraceRoute")

    def setupTab4(self, font): ####################################
        self.tab_4 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_4.setFont(font)
        
        self.tab_4_Layout = QtWidgets.QHBoxLayout(self.tab_4)
        self.tab_4_Layout.setSpacing(0)
        self.tab_4_Layout.setObjectName("tab_4_Layout")
        self.tab_4_Layout.setContentsMargins(0, 0, 0, 0)

        # Input Section
        self.input_Layout_ST = QtWidgets.QVBoxLayout()
        self.input_Layout_ST.setSpacing(9)
        self.input_Layout_ST.setObjectName("input_Layout_ST")
        self.input_Layout_ST.setContentsMargins(10, 10, 10, 10)

        self.label_Layout_ST = QtWidgets.QHBoxLayout()
        self.label_Layout_ST.setSpacing(0)
        self.label_Layout_ST.setObjectName("label_Layout_ST")

        self.label_ST = QtWidgets.QLabel(self.tab_2)
        self.label_ST.setObjectName("label_ST")
        self.label_ST.setMinimumSize(120, 31)
        self.label_ST.setText("Run to show the ")
        self.label_Layout_ST.addWidget(self.label_ST)

        self.speed_label_ST = QtWidgets.QLabel(self.tab_2)
        self.speed_label_ST.setObjectName("speed_label_ST")
        self.speed_label_ST.setMinimumSize(119, 31)
        self.speed_label_ST.setText("speed results")
        self.speed_label_ST.setToolTip("Download Speed - The speed at which data is received by \nyour computer from the Internet (given in Megabytes per second). \nUpload Speed - The speed at which data is sent by your \ncomputer from the Internet (given in Megabytes per second). \nPing - This is the time it takes for your device to send \ndata to a server and then back again (given in Milliseconds).")
        self.label_Layout_ST.addWidget(self.speed_label_ST)

        self.input_Layout_ST.addLayout(self.label_Layout_ST)

        self.runSTButton = QtWidgets.QPushButton(self.tab_2)
        self.runSTButton.setObjectName("runSTButton")
        self.runSTButton.setMinimumSize(241, 31)
        self.runSTButton.setText("Run Speed Test")
        self.runSTButton.clicked.connect(lambda: self.pressed_runSTButton())
        self.input_Layout_ST.addWidget(self.runSTButton)

        self.space_widget_ST = QtWidgets.QWidget(self.tab_4)
        self.space_widget_ST.setObjectName("space_widget_ST")
        self.space_widget_ST.setMinimumSize(241, 266)

        self.input_Layout_ST.addWidget(self.space_widget_ST)

        self.tab_4_Layout.addLayout(self.input_Layout_ST)

        # Output Section
        self.output_Layout_ST = QtWidgets.QVBoxLayout()
        self.output_Layout_ST.setSpacing(0)
        self.output_Layout_ST.setObjectName("output_Layout_ST")
        self.output_Layout_ST.setContentsMargins(10, 10, 10, 10)

        self.scroll_Bounds_ST = QtWidgets.QWidget(self.tab_4)
        self.scroll_Bounds_ST.setObjectName("scroll_Bounds_ST")
        self.scroll_Bounds_ST.setMinimumSize(513, 348)

        self.scroll_Area_ST = QtWidgets.QScrollArea(self.scroll_Bounds_ST)
        self.scroll_Area_ST.setObjectName("scroll_Area_ST")
        self.scroll_Area_ST.setGeometry(0, 0, 513, 348)
        self.scroll_Area_ST.setWidgetResizable(True)

        self.scroll_Area_Contents_ST = QtWidgets.QWidget()
        self.scroll_Area_Contents_ST.setObjectName("scroll_Area_Contents_ST")
        self.scroll_Area_Contents_ST.setGeometry(0, 0, 511, 346)

        self.scroll_Layout_ST = QtWidgets.QVBoxLayout(self.scroll_Area_Contents_ST)
        self.scroll_Layout_ST.setObjectName("scroll_Layout_ST")
        self.scroll_Layout_ST.setContentsMargins(0, 0, 0, 0)

        self.testInfo = 1
        self.testLabels = []

        self.table_results_ST = QtWidgets.QTableWidget()
        self.table_results_ST.setObjectName("table_results_ST")
        self.table_results_ST.setRowCount(0)
        self.table_results_ST.setColumnCount(0)
        self.table_results_ST.move(0,0)
        self.scroll_Layout_ST.addWidget(self.table_results_ST)

        self.scroll_Area_ST.setWidget(self.scroll_Area_Contents_ST)
        self.output_Layout_ST.addWidget(self.scroll_Bounds_ST)
        self.tab_4_Layout.addLayout(self.output_Layout_ST)
        
        self.tabs.addTab(self.tab_4, "Speed Test")


    # Button Methods
    # Tab 1
    def pressed_runNSButton(self):
        os.system("ifconfig > ip.txt")
        output = open("ip.txt")
        line = output.readline()
        while (line.find("eth1") == -1):
            line = output.readline()
        line = output.readline()
        list = line.split()
        ipList = list[1].split(".")
        ipString = ipList[0] + "." + ipList[1] + "." + ipList[2] + ".1/24"
        output.close()
        os.system("rm ip.txt")

        os.system("sudo python3 netScan.py " + ipString + " > out.txt")
        rowCount = len(open("out.txt").readlines()) - 3
        output = open("out.txt")
        TA = output.readline() #throwaway lines
        TA = output.readline() #throwaway lines
        index = 0
        devices = 0;
        macs = " "
        rowLabel = []
        self.table_results_NS.setRowCount(rowCount)
        self.table_results_NS.setColumnCount(3)
        self.table_results_NS.setHorizontalHeaderLabels(["IP Address", "MAC Address", "Device Vendor"])
        self.table_results_NS.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.table_results_NS.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.table_results_NS.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        addrLine = output.readline()
        while (addrLine.find("D") != 0):
            rowLabel.append("Device " + str(index + 1))
            addrList = addrLine.split()
            self.table_results_NS.setItem(index, 0, QtWidgets.QTableWidgetItem(addrList[0]))
            self.table_results_NS.setItem(index, 1, QtWidgets.QTableWidgetItem(addrList[1]))
            devices += 1
            macs += addrList[1] + " "
            addrLine = output.readline()
            index += 1
        self.table_results_NS.setVerticalHeaderLabels(rowLabel)
        self.macInfo = str(devices) + macs
        output.close()
        os.system("rm out.txt")
        index = 0
        os.system("python vendor.py " + self.macInfo + "> out.txt")
        output = open("out.txt")
        line = output.readline()
        while (line.find("Done") == -1):
            if (line.find("error") != -1):
                self.table_results_NS.setItem(index, 2, QtWidgets.QTableWidgetItem("No Result"))
                index +=1
            if (line.find("company") != -1):
                list = line.split("'")
                self.table_results_NS.setItem(index, 2, QtWidgets.QTableWidgetItem(list[3]))
                index += 1
            line = output.readline()
        output.close()
        os.system("rm out.txt")

    # Tab 2
    def pressed_runPSButton(self):
        os.system("ifconfig > ip.txt")
        output = open("ip.txt")
        line = output.readline()
        while (line.find("eth1") == -1):
            line = output.readline()
        line = output.readline()
        list = line.split()
        ipList = list[1].split(".")
        ipString = ipList[0] + "." + ipList[1] + "." + ipList[2] + ".1/24"
        output.close()
        os.system("rm ip.txt")
        
        os.system("sudo python3 pScan.py " + ipString + " > out.txt")
        rowCount = len(open("out.txt").readlines()) - 2
        output = open("out.txt")
        TA = output.readline() #throwaway lines
        first = True
        prevIp = ""
        index = 0
        device = 1
        rowLabel = []
        self.table_results_PS.setRowCount(rowCount)
        self.table_results_PS.setColumnCount(3)
        self.table_results_PS.setHorizontalHeaderLabels(["IP Address", "Port Number", "Port Description"])
        self.table_results_PS.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.table_results_PS.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.table_results_PS.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        addrLine = output.readline()
        while (addrLine.find("D") != 0):
            addrList = addrLine.split()
            if (first):
                first = False
                rowLabel.append("Device " + str(device))
                prevIp = addrList[0]
                self.table_results_PS.setItem(index, 0, QtWidgets.QTableWidgetItem(addrList[0]))
                self.table_results_PS.setItem(index, 1, QtWidgets.QTableWidgetItem(addrList[1]))
                self.table_results_PS.setItem(index, 2, QtWidgets.QTableWidgetItem(self.portNames[addrList[1]]))
            elif (prevIp == addrList[0]):
                rowLabel.append("Device " + str(device))
                self.table_results_PS.setItem(index, 0, QtWidgets.QTableWidgetItem(addrList[0]))
                self.table_results_PS.setItem(index, 1, QtWidgets.QTableWidgetItem(addrList[1]))
                self.table_results_PS.setItem(index, 2, QtWidgets.QTableWidgetItem(self.portNames[addrList[1]]))
            else:
                device += 1
                rowLabel.append("Device " + str(device))
                prevIp = addrList[0]
                self.table_results_PS.setItem(index, 0, QtWidgets.QTableWidgetItem(addrList[0]))
                self.table_results_PS.setItem(index, 1, QtWidgets.QTableWidgetItem(addrList[1]))
                self.table_results_PS.setItem(index, 2, QtWidgets.QTableWidgetItem(self.portNames[addrList[1]]))
            index += 1
            addrLine = output.readline()
        self.table_results_PS.setVerticalHeaderLabels(rowLabel)
        output.close()
        os.system("rm out.txt")


    # Tab 3
    def pressed_iTTL_TR(self):
        ttl = int(self.input_Ttl.text())
        if (ttl < 30):
            ttl += 5
            self.input_Ttl.setText(str(ttl))

    def pressed_dTTL_TR(self):
        ttl = int(self.input_Ttl.text())
        if (ttl > 5):
            ttl -= 5
            self.input_Ttl.setText(str(ttl))

    def pressed_runTRButton(self):
        os.system("sudo python3 traceFunc2.py " + self.input_Url.text() + " " + self.input_Ttl.text() + " > out.txt")
        rowCount = int(self.input_Ttl.text())
        output = open("out.txt")
        TA = output.readline() #throwaway lines
        TA = output.readline() #throwaway lines
        TA = output.readline() #throwaway lines
        TA = output.readline() #throwaway lines
        TA = output.readline() #throwaway lines
        addrLine = output.readline()
        index = 0
        ipNum = 0
        ips = " "
        ipSkip = []
        first = True
        rowLabel = []
        self.table_results_TR.setRowCount(rowCount)
        self.table_results_TR.setColumnCount(3)
        self.table_results_TR.setHorizontalHeaderLabels(["IP Address", "IP Information", "Packet Progress"])

        self.table_results_TR.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.table_results_TR.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.table_results_TR.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        while (addrLine.find("D") != 0):
            rowLabel.append("Hop " + str(index + 1))
            addrList = addrLine.split()
            hop = int(addrList[0])
            if (hop != index + 1):
                self.table_results_TR.setItem(index, 0, QtWidgets.QTableWidgetItem("Unanswered"))
                self.table_results_TR.setItem(index, 1, QtWidgets.QTableWidgetItem(" "))
                self.table_results_TR.setItem(index, 2, QtWidgets.QTableWidgetItem(" "))
                ipSkip.append(index)
                index += 1
            else:
                if (not first):
                    self.table_results_TR.setItem(index, 0, QtWidgets.QTableWidgetItem(addrList[1]))
                    self.table_results_TR.setItem(index, 2, QtWidgets.QTableWidgetItem(self.traceCodes[addrList[2]]))
                    ips += addrList[1] + " "
                    ipNum += 1
                    addrLine = output.readline()
                    index += 1
                else:
                    self.table_results_TR.setItem(index, 0, QtWidgets.QTableWidgetItem(addrList[1]))
                    self.table_results_TR.setItem(index, 1, QtWidgets.QTableWidgetItem("Internal Router IP"))
                    self.table_results_TR.setItem(index, 2, QtWidgets.QTableWidgetItem(self.traceCodes[addrList[2]]))
                    addrLine = output.readline()
                    index += 1
                    first = False
        while (rowCount > index):
            rowLabel.append("Hop " + str(index + 1))
            self.table_results_TR.setItem(index, 0, QtWidgets.QTableWidgetItem("Unanswered"))
            self.table_results_TR.setItem(index, 1, QtWidgets.QTableWidgetItem(" "))
            self.table_results_TR.setItem(index, 2, QtWidgets.QTableWidgetItem(" "))
            index += 1
        ipInfo = str(ipNum) + ips
        output.close()
        os.system("rm out.txt")
        index = 1;
        os.system("sudo python3 location.py " + ipInfo + " > out.txt")
        output = open("out.txt")
        line = output.readline()
        line = line.strip()
        while (line.find("Done") == -1):
            if index not in ipSkip:
                self.table_results_TR.setItem(index, 1, QtWidgets.QTableWidgetItem(line))
                line = output.readline()
                line = line.strip()
            index += 1
        output.close()
        os.system("rm out.txt")
        self.table_results_TR.setVerticalHeaderLabels(rowLabel)

    # Tab 4

    def pressed_runSTButton(self):
        os.system("sudo python speed.py > out.txt")
        output = open("out.txt")

        self.table_results_ST.setRowCount(self.testInfo)
        self.table_results_ST.setColumnCount(3)
        self.table_results_ST.setHorizontalHeaderLabels(["Download Speed", "Upload Speed", "Ping Speed"])
        self.table_results_ST.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.table_results_ST.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.table_results_ST.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        index = 0;
        line = output.readline()
        while (line.find("Done") == -1):
            list = line.split()
            line = list[1] + " " + list[2]
            self.table_results_ST.setItem(self.testInfo - 1, index, QtWidgets.QTableWidgetItem(line))
            index += 1
            line = output.readline()
        output.close()
        os.system("rm out.txt")
        self.testLabels.append("Test " + str(self.testInfo))
        self.testInfo += 1
        self.table_results_ST.setVerticalHeaderLabels(self.testLabels)



def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = nmrpGUI()
    ui.show()
    sys.exit(app.exec_())
main()

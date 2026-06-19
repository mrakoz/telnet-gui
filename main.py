import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QSplitter, QListWidget, QPushButton, 
                             QLineEdit, QTextEdit, QLabel, QInputDialog, QMessageBox,
                             QFormLayout, QDialog, QDialogButtonBox, QCheckBox)
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QColor, QTextCursor, QTextCharFormat, QFont

from storage import load_profiles, save_profiles, add_profile, edit_profile, delete_profile
from telnet_worker import TelnetWorker

# Dark Theme Stylesheet
STYLESHEET = """
QMainWindow, QDialog {
    background-color: #282c34;
    color: #abb2bf;
}
QWidget {
    font-family: 'Inter', 'Segoe UI', sans-serif;
    font-size: 14px;
}
QListWidget {
    background-color: #21252b;
    color: #abb2bf;
    border: 1px solid #181a1f;
    border-radius: 4px;
    padding: 5px;
}
QListWidget::item:selected {
    background-color: #3e4451;
    color: #ffffff;
}
QTextEdit {
    background-color: #1e2227;
    color: #abb2bf;
    border: 1px solid #181a1f;
    border-radius: 4px;
    padding: 5px;
    font-family: 'Consolas', 'Monospace';
}
QLineEdit {
    background-color: #21252b;
    color: #abb2bf;
    border: 1px solid #181a1f;
    border-radius: 4px;
    padding: 6px;
}
QPushButton {
    background-color: #3e4451;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    padding: 8px 12px;
}
QPushButton:hover {
    background-color: #4b5363;
}
QPushButton:pressed {
    background-color: #2c313a;
}
QLabel {
    color: #abb2bf;
}
"""

class ProfileDialog(QDialog):
    def __init__(self, parent=None, name="", ip="", port="23"):
        super().__init__(parent)
        self.setWindowTitle("Edit Profile")
        self.layout = QVBoxLayout(self)
        
        self.form_layout = QFormLayout()
        
        self.name_input = QLineEdit(name)
        self.ip_input = QLineEdit(ip)
        self.port_input = QLineEdit(str(port))
        
        self.form_layout.addRow("Name:", self.name_input)
        self.form_layout.addRow("IP Address:", self.ip_input)
        self.form_layout.addRow("Port:", self.port_input)
        
        self.layout.addLayout(self.form_layout)
        
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        self.layout.addWidget(self.button_box)
        
    def get_data(self):
        return self.name_input.text(), self.ip_input.text(), self.port_input.text()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ubuntu Telnet Client")
        self.resize(1000, 600)
        
        self.worker = None
        self.profiles = []
        self.profile_logs = {}
        self.current_profile_index = -1
        
        self.init_ui()
        self.refresh_profile_list()
        
    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        layout = QVBoxLayout(main_widget)
        
        # Splitter for 1/3 and 2/3 layout
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)
        
        # --- LEFT PANEL (1/3) ---
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        
        self.profile_list = QListWidget()
        self.profile_list.itemSelectionChanged.connect(self.on_profile_selected)
        left_layout.addWidget(QLabel("Saved Servers:"))
        left_layout.addWidget(self.profile_list)
        
        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Add")
        self.btn_edit = QPushButton("Edit")
        self.btn_del = QPushButton("Delete")
        
        self.btn_add.clicked.connect(self.add_new_profile)
        self.btn_edit.clicked.connect(self.edit_selected_profile)
        self.btn_del.clicked.connect(self.delete_selected_profile)
        
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_edit)
        btn_layout.addWidget(self.btn_del)
        
        left_layout.addLayout(btn_layout)
        
        # --- RIGHT PANEL (2/3) ---
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        
        # Connection Controls
        conn_layout = QHBoxLayout()
        
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("IP Address")
        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("Port")
        self.port_input.setFixedWidth(80)
        
        self.btn_connect = QPushButton("Connect")
        self.btn_connect.setStyleSheet("background-color: #98c379; color: #282c34; font-weight: bold;")
        self.btn_connect.clicked.connect(self.toggle_connection)
        
        self.btn_clear = QPushButton("Clear Log")
        self.btn_clear.clicked.connect(self.clear_current_log)
        
        self.interactive_checkbox = QCheckBox("Interactive Mode")
        self.interactive_checkbox.setStyleSheet("color: #abb2bf;")
        
        conn_layout.addWidget(QLabel("Host:"))
        conn_layout.addWidget(self.ip_input)
        conn_layout.addWidget(QLabel("Port:"))
        conn_layout.addWidget(self.port_input)
        conn_layout.addWidget(self.btn_connect)
        conn_layout.addWidget(self.btn_clear)
        conn_layout.addWidget(self.interactive_checkbox)
        
        right_layout.addLayout(conn_layout)
        
        # Output Area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        # Use a nice monospaced font
        font = QFont("Consolas", 11)
        font.setStyleHint(QFont.Monospace)
        self.output_area.setFont(font)
        self.output_area.installEventFilter(self)
        right_layout.addWidget(self.output_area)
        
        # Input Area
        self.cmd_input = QLineEdit()
        self.cmd_input.setPlaceholderText("Type command and press Enter...")
        self.cmd_input.returnPressed.connect(self.send_command)
        self.cmd_input.setEnabled(False)
        right_layout.addWidget(self.cmd_input)
        
        # Add to splitter and set initial sizes (1/3 and 2/3)
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([333, 666])
        
    def refresh_profile_list(self):
        self.profile_list.clear()
        self.profiles = load_profiles()
        for p in self.profiles:
            self.profile_list.addItem(f"{p['name']} ({p['ip']}:{p['port']})")
            
    def on_profile_selected(self):
        selected_items = self.profile_list.selectedItems()
        if selected_items:
            new_index = self.profile_list.row(selected_items[0])
            
            # Save current log before switching
            if self.current_profile_index != -1:
                self.profile_logs[self.current_profile_index] = self.output_area.toHtml()
                
            self.current_profile_index = new_index
            
            # Restore new log
            if new_index in self.profile_logs:
                self.output_area.setHtml(self.profile_logs[new_index])
            else:
                self.output_area.clear()
            
            if 0 <= new_index < len(self.profiles):
                p = self.profiles[new_index]
                self.ip_input.setText(p['ip'])
                self.port_input.setText(str(p['port']))
                
    def clear_current_log(self):
        self.output_area.clear()
        if self.current_profile_index != -1:
            self.profile_logs[self.current_profile_index] = ""
                
    def add_new_profile(self):
        dialog = ProfileDialog(self)
        if dialog.exec_():
            name, ip, port = dialog.get_data()
            if name and ip and port:
                add_profile(name, ip, port)
                self.refresh_profile_list()
                
    def edit_selected_profile(self):
        selected_items = self.profile_list.selectedItems()
        if not selected_items:
            return
            
        index = self.profile_list.row(selected_items[0])
        p = self.profiles[index]
        
        dialog = ProfileDialog(self, p['name'], p['ip'], p['port'])
        if dialog.exec_():
            name, ip, port = dialog.get_data()
            if name and ip and port:
                edit_profile(index, name, ip, port)
                self.refresh_profile_list()
                
    def delete_selected_profile(self):
        selected_items = self.profile_list.selectedItems()
        if not selected_items:
            return
            
        index = self.profile_list.row(selected_items[0])
        reply = QMessageBox.question(self, 'Delete Profile', 
                                     'Are you sure you want to delete this profile?',
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
                                     
        if reply == QMessageBox.Yes:
            delete_profile(index)
            self.refresh_profile_list()

    def toggle_connection(self):
        if self.worker and self.worker.running:
            self.disconnect_server()
        else:
            self.connect_server()
            
    def connect_server(self):
        ip = self.ip_input.text().strip()
        port_str = self.port_input.text().strip()
        
        if not ip or not port_str:
            self.append_output("Please enter IP address and Port.", "error")
            return
            
        try:
            port = int(port_str)
        except ValueError:
            self.append_output("Invalid port number.", "error")
            return
            
        self.btn_connect.setText("Disconnect")
        self.btn_connect.setStyleSheet("background-color: #e06c75; color: #282c34; font-weight: bold;")
        self.ip_input.setEnabled(False)
        self.port_input.setEnabled(False)
        self.profile_list.setEnabled(False)
        self.cmd_input.setEnabled(True)
        self.cmd_input.setFocus()
        
        self.worker = TelnetWorker(ip, port)
        self.worker.data_received.connect(self.on_data_received)
        self.worker.connection_closed.connect(self.on_connection_closed)
        self.worker.connection_error.connect(self.on_connection_error)
        self.worker.start()
        
    def disconnect_server(self):
        if self.worker:
            self.worker.stop()
            self.worker = None
            
    def on_connection_closed(self):
        self.append_output("\nConnection closed.", "info")
        self.reset_ui_after_disconnect()
        
    def on_connection_error(self, err_msg):
        self.append_output(f"\n{err_msg}", "error")
        self.reset_ui_after_disconnect()
        
    def reset_ui_after_disconnect(self):
        self.btn_connect.setText("Connect")
        self.btn_connect.setStyleSheet("background-color: #98c379; color: #282c34; font-weight: bold;")
        self.ip_input.setEnabled(True)
        self.port_input.setEnabled(True)
        self.profile_list.setEnabled(True)
        self.cmd_input.setEnabled(False)
        self.cmd_input.clear()
        
    def on_data_received(self, data):
        self.append_output(data, "server")
        
    def send_command(self):
        cmd = self.cmd_input.text()
        if self.worker and self.worker.running:
            self.append_output(f"> {cmd}\n", "client")
            self.worker.send_command(cmd)
            self.cmd_input.clear()

    def append_output(self, text, msg_type="server"):
        cursor = self.output_area.textCursor()
        cursor.movePosition(QTextCursor.End)
        
        format = QTextCharFormat()
        
        # Apply modern colors
        if msg_type == "client":
            format.setForeground(QColor("#61afef")) # Blue
        elif msg_type == "server":
            format.setForeground(QColor("#abb2bf")) # Light gray
        elif msg_type == "error":
            format.setForeground(QColor("#e06c75")) # Red
        elif msg_type == "info":
            format.setForeground(QColor("#98c379")) # Green
            
        cursor.setCharFormat(format)
        cursor.insertText(text)
        
        self.output_area.setTextCursor(cursor)
        self.output_area.ensureCursorVisible()
        
    def closeEvent(self, event):
        if self.worker:
            self.worker.stop()
        event.accept()

    def eventFilter(self, obj, event):
        if obj == self.output_area and event.type() == QEvent.KeyPress:
            if self.interactive_checkbox.isChecked() and self.worker and self.worker.running:
                char = event.text()
                if char:
                    # Echo the character locally if needed? Telnet usually relies on server echo.
                    # But for now we just send it.
                    self.worker.send_raw(char)
                    return True # Prevent text edit from handling it
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLESHEET)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                              QPushButton, QFileDialog, QListWidget, QLineEdit, QLabel,
                              QMessageBox, QInputDialog, QErrorMessage)
from PyQt6.QtCore import Qt
from mutagen.flac import FLAC
from mutagen.id3 import ID3

class FlacMetadataManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enhanced FLAC Metadata Manager")
        self.setGeometry(100, 100, 900, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # File/Folder selection
        file_layout = QHBoxLayout()
        self.path_input = QLineEdit()
        file_button = QPushButton("Select File")
        file_button.clicked.connect(self.select_file)
        folder_button = QPushButton("Select Folder")
        folder_button.clicked.connect(self.select_folder)
        file_layout.addWidget(self.path_input)
        file_layout.addWidget(file_button)
        file_layout.addWidget(folder_button)
        layout.addLayout(file_layout)

        # Metadata list
        self.metadata_list = QListWidget()
        self.metadata_list.itemDoubleClicked.connect(self.edit_metadata_item)
        layout.addWidget(self.metadata_list)

        # CRUD buttons
        button_layout = QHBoxLayout()
        create_button = QPushButton("Create")
        create_button.clicked.connect(self.create_metadata)
        update_button = QPushButton("Update")
        update_button.clicked.connect(self.update_metadata)
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete_metadata)
        apply_all_button = QPushButton("Apply to All")
        apply_all_button.clicked.connect(self.apply_to_all)
        button_layout.addWidget(create_button)
        button_layout.addWidget(update_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(apply_all_button)
        layout.addLayout(button_layout)

        self.current_path = None
        self.files = []

        # Error message dialog
        self.error_dialog = QErrorMessage(self)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select FLAC file", "", "FLAC Files (*.flac)")
        if file_path:
            self.path_input.setText(file_path)
            self.current_path = file_path
            self.files = [file_path]
            self.read_metadata()

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.path_input.setText(folder_path)
            self.current_path = folder_path
            self.files = [os.path.join(root, file) for root, _, files in os.walk(folder_path)
                          for file in files if file.endswith('.flac')]
            self.read_metadata()

    def read_metadata(self):
        self.metadata_list.clear()
        for file_path in self.files:
            try:
                audio = FLAC(file_path)
                self.metadata_list.addItem(f"File: {file_path}")
                for key, value in audio.tags.items():
                    self.metadata_list.addItem(f"{key}: {value[0]}")
                self.metadata_list.addItem("")  # Add a blank line between files
            except Exception as e:
                self.metadata_list.addItem(f"Error processing {file_path}: {str(e)}")

    def process_file(self, file_path):
        try:
            audio = FLAC(file_path)
            self.metadata_list.addItem(f"File: {file_path}")
            for key, value in audio.tags.items():
                self.metadata_list.addItem(f"{key}: {value[0]}")
            self.metadata_list.addItem("")  # Add a blank line between files
        except Exception as e:
            self.metadata_list.addItem(f"Error processing {file_path}: {str(e)}")

    def create_metadata(self):
        key, ok = QInputDialog.getText(self, "Create Metadata", "Enter metadata key:")
        if ok and key:
            value, ok = QInputDialog.getText(self, "Create Metadata", "Enter metadata value:")
            if ok:
                self.apply_metadata(key, value, create=True)

    def update_metadata(self):
        current_item = self.metadata_list.currentItem()
        if current_item and ':' in current_item.text():
            key, old_value = current_item.text().split(':', 1)
            new_value, ok = QInputDialog.getText(self, "Update Metadata",
                                                 f"Update value for {key}:",
                                                 text=old_value.strip())
            if ok:
                self.apply_metadata(key, new_value)

    def delete_metadata(self):
        current_item = self.metadata_list.currentItem()
        if current_item and ':' in current_item.text():
            key = current_item.text().split(':', 1)[0]
            reply = QMessageBox.question(self, "Delete Metadata",
                                          f"Are you sure you want to delete '{key}'?",
                                          QMessageBox.StandardButton.Yes |
                                          QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.apply_metadata(key, None, delete=True)

    def apply_metadata(self, key, value, create=False, delete=False):
        for file_path in self.files:
            try:
                audio = FLAC(file_path)
                if delete:
                    if key in audio:
                        del audio[key]
                elif create or key in audio:
                    audio[key] = value
                audio.save()
            except Exception as e:
                self.error_dialog.showMessage(f"Error processing {file_path}: {str(e)}")
        self.read_metadata()

    def apply_to_all(self):
        key, ok = QInputDialog.getText(self, "Apply to All", "Enter metadata key:")
        if ok and key:
            value, ok = QInputDialog.getText(self, "Apply to All", "Enter metadata value:")
            if ok:
                self.apply_metadata(key, value, create=True)

    def edit_metadata_item(self, item):
        if ':' in item.text():
            key, old_value = item.text().split(':', 1)
            new_value, ok = QInputDialog.getText(self, "Edit Metadata",
                                                 f"Edit value for {key}:",
                                                 text=old_value.strip())
            if ok:
                self.apply_metadata(key, new_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlacMetadataManager()
    window.show()
    sys.exit(app.exec())

**Enhanced FLAC Metadata Manager**
=====================================

**Overview**
------------

This is a PyQt6-based application designed to manage metadata for FLAC audio files. It allows users to create, update, delete, and apply metadata to individual files or entire folders.

**Features**
------------

* **File/Folder Selection**: Select individual FLAC files or entire folders containing FLAC files for metadata management.
* **Metadata List**: Display metadata for selected files/folders in a list view, allowing users to easily navigate and edit metadata.
* **CRUD Operations**: Create new metadata items using `Create`, update existing items using `Update`, delete items using `Delete`, or apply changes to all selected files/folders using `Apply to All`.
* **Error Handling**: Display error messages when encountering issues during metadata processing.
* **Metadata Editing**: Edit individual metadata items by double-clicking on them in the list view.

**Usage**
---------

### Running the Application

To run the application, execute the following command:

```bash
python main.py
```

### Selecting Files/Folders

1. Click `Select File` to choose an individual FLAC file or `Select Folder` to choose an entire folder containing FLAC files.
2. The selected path will be displayed in the input field at the top of the window.

### Creating New Metadata Items

1. Click `Create` to open a dialog box where you can enter a new metadata key-value pair.
2. Enter the desired metadata key (e.g., `artist`) followed by its corresponding value (e.g., `John Doe`).
3. Click `OK` to add the new metadata item.

### Updating Existing Metadata Items

1. Select an existing metadata item from the list view by clicking on it.
2. Click `Update` to open a dialog box where you can edit the selected metadata item.
3. Enter the new value for the selected metadata key (or leave it blank to delete the item).
4. Click `OK` to apply changes.

### Deleting Metadata Items

1. Select an existing metadata item from the list view by clicking on it.
2. Click `Delete` to confirm deletion.

### Applying Changes to All Files/Folders

1. Click `Apply to All` to open a dialog box where you can enter a new metadata key-value pair.
2. Enter the desired metadata key (e.g., `artist`) followed by its corresponding value (e.g., `John Doe`).
3. Click `OK` to apply changes to all selected files/folders.

**Technical Details**
--------------------

This application uses:

* PyQt6 for building the graphical user interface (GUI)
* Mutagen library for handling FLAC audio files' metadata

**Known Issues**
-----------------

* Error handling may not cover all edge cases; please report any issues encountered during use.

**Contributing**
--------------

Feel free to contribute by reporting bugs or suggesting new features. To do so:

1. Fork this repository.
2. Create a new branch for your changes.
3. Make changes to the code.
4. Commit your changes with a descriptive message.
5. Create a pull request for review.

**License**
----------

This application is released under the MIT License.

**Acknowledgments**
------------------

Special thanks to:

* The PyQt6 community for providing an excellent GUI framework
* The Mutagen library developers for creating an efficient metadata handling library

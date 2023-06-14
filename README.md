# txt2md
This Python script converts any file that ends in .txt to .md but also converts any file that ends in .md from html format to markdown format

You need to run this script in the folder you have your files. The idea of this script was to use [Notes Exporter App](http://writeapp.net/notesexporter/) to export all notes created in Apple Notes App to a folder. Once the files were all exported, I realized the files all ended in `.txt` filename extensions but also prepended with `Notes` for every file name. Also, anything in Notes that uses rich text formatting seems to use HTML formatting behind the scenes. So I need to do the following:

* Export files using [Notes Exporter App](http://writeapp.net/notesexporter/)
* Rename all files that start with `Notes` and end in `.txt` to just the filename and end it with `.md` (eg - NotesFilename.txt to Filename.md)
* All converted files that end in `.md` should be scanned and if the file contains any .html formatting, convert it to markdown and keeping the same filename

Of course, you'll have to tweak the script to fit your needs. This was a quick hack and a good start. The script can be condensed. It's just longer here because as I made progress, I had to append additional steps.

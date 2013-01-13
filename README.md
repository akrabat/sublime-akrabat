#sublime-akrabat

This repository contains useful Sublime Text 2 stuff.


##PHP Getter & Setter snippet

Type `gs` followed by `tab` and then your underscore_separated property name to create a getter and setter method.

Alternatively, select some text and press `shift+cmd+p` and then type `gs` to automatically replace the selected text with the getter and setter methods completed for the text that was selected.

As an example, typing `gs {tab} date_last_updated` will produce:

        public function getDateLastUpdated()
        {
            return $this->date_last_updated;
        }
        
        public function setDateLastUpdated($dateLastUpdated)
        {
            $this->date_last_updated = $dateLastUpdated;
            return $this;
        }


##Tidy:

Three commands to tidy HTML, XML and JSON:

From Command Palette:

* Tidy XML  (ctrl+shift+x)
* Tidy HTML (ctrl+shift+h)
* Tidy JSON (ctrl+shift+j)


## Some useful commands (accessed via cmd+shift+p)

* `Open Containing Folder` to open a Finder window.
* `Open Terminal Here` to open a Terminal at the directory where this file is.
* `Open Terminal at Project Folder` to open a Terminal at the directory where the project is.

[Terminal](http://wbond.net/sublime_packages/terminal) from Will Bond is required.



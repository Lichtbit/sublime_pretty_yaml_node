Pretty YAML Node
================

Prettify YAML Node plugin for Sublime Text 3 (Based on [Pretty
YAML](<https://github.com/aukaost/SublimePrettyYAML>))



Installation 
-------------

Install this sublime text package via [Package
Control](<http://wbond.net/sublime_packages/package_control>)

You have to install node on your machine and put the path in the plugin's preferences.



Usage To prettify YAML, make selection of YAML and press keys:
--------------------------------------------------------------

-   Linux: <kbd>ctrl+alt+y</kbd>

-   Windows: <kbd>ctrl+alt+y</kbd>

-   OS X: <kbd>cmd+ctrl+y</kbd>

If selection is empty and configuration entry
**use_entire_file_if_no_selection** is true, tries to prettify whole file.


Default configuration
---------------------

This plugin uses js-yaml as node module to process YAML files. You can specify the options for [safeDump](<https://github.com/nodeca/js-yaml#safedump-object---options->) in the plugin's preferences.

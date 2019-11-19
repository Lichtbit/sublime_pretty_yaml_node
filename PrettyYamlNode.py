import sublime
import sublime_plugin
import decimal
import sys
import tempfile
import subprocess
import os
import shutil
import json

s = sublime.load_settings("Pretty YAML Node.sublime-settings")

class PrettyyamlnodeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        """ Pretty print YAML """
        for region in self.view.sel():

            selected_entire_file = False

            # If no selection, use the entire file as the selection
            if region.empty() and s.get("use_entire_file_if_no_selection", True):
                selection = sublime.Region(0, self.view.size())
                selected_entire_file = True
            else:
                selection = region

            temp_path = tempfile.mkdtemp("prettyyaml")
            with open(temp_path + "/in.yml" ,"w") as file:
              file.write(self.view.substr(selection))

            with open(temp_path + "/config.json", 'w') as file:
              json.dump(s.get('dumper_args'), file) 

            subprocess.call([s.get("node_path"), os.path.dirname(os.path.abspath(__file__)) + "/pretty_json.js", temp_path])
            
            with open(temp_path + "/out.yml" ,"r") as file:
              self.view.replace(edit, selection, file.read())

            shutil.rmtree(temp_path)

            if selected_entire_file:
                self.change_syntax()

    def change_syntax(self):        
        if "Plain text" in self.view.settings().get('syntax'):
            self.view.set_syntax_file("Packages/YAML/YAML.tmLanguage")


def plugin_loaded():
    global s
    s = sublime.load_settings("Pretty YAML Node.sublime-settings")

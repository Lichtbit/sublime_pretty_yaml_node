import sublime
import sublime_plugin
import decimal
import sys
import tempfile
import subprocess
import os
import shutil
import json

STATUS_ID = 'pretty_yaml_node'
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

            output = subprocess.check_output([s.get("node_path"), os.path.dirname(os.path.abspath(__file__)) + "/pretty_json.js", temp_path])
            self.set_short_status(self.view, output.decode("utf-8").replace("\n", ""))
            with open(temp_path + "/out.yml" ,"r") as file:
              self.view.replace(edit, selection, file.read())

            shutil.rmtree(temp_path)

            if selected_entire_file:
                self.change_syntax()

    def change_syntax(self):
        if "Plain text" in self.view.settings().get('syntax'):
            self.view.set_syntax_file("Packages/YAML/YAML.tmLanguage")

    def set_short_status(self, active_view, text):
        def erase_status():
            active_view.erase_status(STATUS_ID)
        active_view.set_status(STATUS_ID, text)
        sublime.set_timeout_async(erase_status, 2000)

def plugin_loaded():
    global s
    s = sublime.load_settings("Pretty YAML Node.sublime-settings")

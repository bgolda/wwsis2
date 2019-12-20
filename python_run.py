#this is a simple package to make sublime text open code snippets in command line instead of sublime parser
#since sublime text does not support inputs in its command line, osme programs has to be executed in cmd

import sublime
import sublime_plugin
import subprocess

class PythonRunCommand(sublime_plugin.WindowCommand):
    def run(self):
        command = 'cmd /k "C:\Python27\python.exe" %s' % sublime.active_window().active_view().file_name()
        subprocess.Popen(command)
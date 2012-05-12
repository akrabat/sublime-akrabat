# Based on https://gist.github.com/1138554
#
# See http://tidy.sourceforge.net/docs/quickref.html for tidy options

import sublime, sublime_plugin, subprocess, re

class TidyHtmlCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    command = 'tidy --indent auto -utf8 -w -q --tidy-mark no --indent-spaces 4 --show-body-only yes --show-warnings no --vertical-space no'
    command += ' --new-blocklevel-tags section,header,footer,hgroup,nav,dialog,datalist,details,figcaption,figure,meter,output,progress'
    command += ' --new-pre-tags article,aside,summary,mark'
    command += ' --new-inline-tags video,audio,canvas,source,embed,ruby,rt,rp,keygen,menu,command,time'
    command += ' --fix-uri no --literal-attributes yes'

    # help from http://www.sublimetext.com/forum/viewtopic.php?f=2&p=12451
    p = subprocess.Popen(command, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    result, err = p.communicate(self.view.substr(self.view.sel()[0]).encode('utf-8'))

    print result

    if err != "":
      self.view.set_status('tidyxml', "tidyxml: "+err)
      sublime.set_timeout(self.clear,10000)
    else:
      out = re.sub('</li>\n\n', '</li>\n', result)
      self.view.replace(edit, self.view.sel()[0], out.decode('utf-8'))
      sublime.set_timeout(self.clear,0)
    

  def clear(self):
    self.view.erase_status('tidyxml')


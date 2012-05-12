# Note that as SublimeText 2's bundled Python is version 2.6, we need to use
# our own orderddict and simplejson modules in order to keep the order of the 
# keys the same
# See http://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict-in-python
#
import sublime, sublime_plugin, subprocess, ordereddict, simplejson as json

class TidyJsonCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    try:
      # json.encoder.c_make_encoder = None
      # data = json.loads(self.view.substr(self.view.sel()[0]).encode('utf-8'))
      json_str = self.view.substr(self.view.sel()[0]).encode('utf-8')
      data = json.loads(json_str, object_pairs_hook=ordereddict.OrderedDict)
      result = json.dumps(data, sort_keys=False, indent=4)

      self.view.replace(edit, self.view.sel()[0], result.decode('utf-8'))
      sublime.set_timeout(self.clear,0)
    except Exception as inst:
      print inst
      self.view.set_status('tidyjson', "tidyjson: " + str(inst))
      sublime.set_timeout(self.clear, 5000)


  def clear(self):
    self.view.erase_status('tidyjson')


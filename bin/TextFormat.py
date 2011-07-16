
import subprocess

class TextFormatter:
    def __init__(self,lynx='/usr/bin/lynx'):
        self.lynx = lynx

    def html2text(self, html_source):
        "Expects unicode; returns unicode"
        return subprocess.Popen([self.lynx,
                      '-dump',
                      '-stdin',
                      '-nolist'],
                      stdin=subprocess.PIPE,
                      stdout=subprocess.PIPE).communicate(input=html_source)


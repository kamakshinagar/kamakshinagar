
 import subprocess

class Slug(object):
      def __init__(self, number, value):
        self.number = number
        self.value = value

def main_function(app_name,size):
    response= Done
    val = subprocess.check_call("./script.sh %s %s'" % str(app_name),str(size), shell=True)
    print("the output from script is" val)
    return response

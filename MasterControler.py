__author__ = 'hut-dell'
import subprocess

def stopvmall():

    rs = subprocess.check_output(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", "StopVMALL"])
import os
import subprocess
import sys

try:
    os.mkdir("1-iris", 777)
except:
    pass

try:
    os.mkdir("2-iris", 777)
except:
    pass

try:
    os.mkdir("3-iris", 777)
except:
    pass

try:
    os.mkdir("1-wisconsin", 777)
except:
    pass

try:
    os.mkdir("2-wisconsin", 777)
except:
    pass

try:
    os.mkdir("3-wisconsin", 777)
except:
    pass

os.chdir("1-iris")
subprocess.call([sys.argv[1], "12", "4", "20", sys.argv[2], "../data/iris-1.csv"])
os.chdir("../2-iris")
subprocess.call([sys.argv[1], "12", "4", "20", sys.argv[2], "../data/iris-1.csv"])
os.chdir("../3-iris")
subprocess.call([sys.argv[1], "12", "4", "20", sys.argv[2], "../data/iris-1.csv"])

try:
    os.chdir("../1-wisconsin")
    subprocess.call([sys.argv[1], "12", "9", "50", sys.argv[2], "../data/breast-cancer-wisconsin.csv"])
except:
    pass

try:
    os.chdir("../2-wisconsin")
    subprocess.call([sys.argv[1], "12", "9", "50", sys.argv[2], "../data/breast-cancer-wisconsin.csv"])
except:
    pass

try:
    os.chdir("../3-wisconsin")
    subprocess.call([sys.argv[1], "12", "9", "50", sys.argv[2], "../data/breast-cancer-wisconsin.csv"])
except:
    pass
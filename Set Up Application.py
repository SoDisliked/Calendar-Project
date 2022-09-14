import os 
import sys 
from configuration import 

from greenlock.version import _currentversion_

if sys.argv[-1] == 'publier date':
    os.system("Le programme actuel en Python est configuré sur votre PC")
    sys.exit()

VERSION = "1ére version configuré[]";

def long_description():
    """Description dans la partie haut de l'application"""
    return open(os.path.join(sys.path[0], "Description")).read()

setup(
    name="Logiciel Horraire Auto Ecole",
    packages=['LogicielHorraire'],
    version = VERSION,
    description = "Logiciel qui permet de configurer au préalable les rdv de l'auto école"
    license= "MITLicense",
    long_description = long_description(),
    long_description_content_type="text/x-rst",
    author = "Luca Frumuselu",
    download_url = "https:://github.com/sodisliked/configurateur/" + VERSION,
    
)
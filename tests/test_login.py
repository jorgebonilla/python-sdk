import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
from aviatrix import Aviatrix

def test_login():
    controller_ip=os.environ.get("CONTROLLER")
    username=os.environ.get("CONTROLLER_USERNAME")
    password=os.environ.get("CONTROLLER_PASSWORD")
    controller = Aviatrix(controller_ip)
    controller.login(username,password)
    assert controller.results.find("authorized successfully") != -1

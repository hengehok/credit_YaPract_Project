import pytest


from tests import actualResult

@pytest.fixture()
def before_and_after_tests():
   #Setup


   yield

   #Teardown
   print("test stop")
   actualResult.clear()

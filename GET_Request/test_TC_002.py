import pytest

@pytest.mark.usefixtures("dataload")
class Test_User:
    def test_openprofile(self,dataload):
        print(dataload)
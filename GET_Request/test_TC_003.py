import pytest



def test_login_logout10(start_exec):
    print ("a")

@pytest.mark.Smoke
@pytest.mark.Regression
def test_login_logout20(start_exec):
    print ("b")

@pytest.mark.skip("Skipping as this is not working, issue raised")
def test_login_logout4():
    print ("c")
# def test_crossbrowser(crossBrowser):
#     print (crossBrowser)

# def test_crossbrowser1(crossBrowser):
#     print (crossBrowser[1])





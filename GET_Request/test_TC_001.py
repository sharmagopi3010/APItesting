import pytest

# @pytest.mark.usefixtures("start_exec")
# class Test_Login_Logout:

#     def test_login_logout1111(self):
#         print ("HJI333")

#     def test_login_logout2222(self):
#         print ("HJIwww")


# obj=Login_Logout();
# obj.test_login_logout1111()

expected_value = 10

def test_login_logout1():
    print ("test case start")
    actual_value = 5
    assert expected_value == actual_value, "These two values should be same"

def test_login_logout3():
    print ("d")
# @pytest.mark.Smoke
# @pytest.mark.Regression
# def test_login_logout2(start_exec):
#     print ("HJIwww")

# @pytest.mark.Smoke
# def test_login_logout3():
#     print ("HJIwbbb")
    
# @pytest.mark.xfail #will not skip the case but avoid showing error
# def test_login_logout5():
#     print ("HJIwbbb")



    


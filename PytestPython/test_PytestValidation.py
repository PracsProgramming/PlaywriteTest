# from builtins import function

import pytest


#Fixtures provides a way to create
# Reusable code
@pytest.mark.smoke
def test_initial_check(pre_work,pre_work2,pre_work3):
    print("This is first Test")
    assert pre_work == "Pass"

# @pytest.mark.skip
def test_second_check(pre_work,pre_work2,pre_work3):
    print("This is Second test")

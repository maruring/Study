from decision_table import DecisionTable

def test_case1():
    assert DecisionTable(175,70,30).is_pass() == True

def test_case2():
    """身長が条件不合格
    """
    assert DecisionTable(150,70,30).is_pass() == False

def test_case3():
    """体重が条件不合格
    """
    assert DecisionTable(175,20,30).is_pass() == False

def test_case4():
    """BMIが条件不合格
    """
    assert DecisionTable(175,70,10).is_pass() == False

def test_case5():
    """身長と体重が条件不合格
    """
    assert DecisionTable(150,20,30).is_pass() == False

def test_case6():
    """身長とBMIが条件不合格
    """
    assert DecisionTable(150,70,10).is_pass() == False

def test_case7():
    """BMIと体重が条件不合格
    """
    assert DecisionTable(175,20,10).is_pass() == False

def test_case8():
    """すべての条件が不合格
    """
    assert DecisionTable(110,20,10).is_pass() == False

"""
判定条件と判定順番が一定であればテストの条件を圧縮することができる
身長 ⇒ 体重 ⇒ BMI の順で判定する
"""
def test_order_case1():
    assert DecisionTable(180,80,45).is_pass_by_order() == True

def test_order_case2():
    """身長が条件不合格
    """
    assert DecisionTable(150,80,45).is_pass_by_order() == False

def test_order_case3():
    """体重が条件不合格
    """
    assert DecisionTable(180,20,45).is_pass_by_order() == False

def test_order_case4():
    """BMIが条件不合格
    """
    assert DecisionTable(180,80,10).is_pass_by_order() == False
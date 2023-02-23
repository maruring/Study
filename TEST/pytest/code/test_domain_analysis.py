from domain_analysis import DomainAnalysis

def case1():
    assert DomainAnalysis(20,30).calc_total_score() == 50

def case2():
    """self.aがon point, self.bがin point
    """
    assert DomainAnalysis(60,40).is_pass() == True

def case3():
    """self.aがoff point, self.bがin point
    """
    assert DomainAnalysis(59,40).is_pass() == False

def case4():
    """self.aがin point, self.bがon point
    """
    assert DomainAnalysis(70,20).is_pass() == True

def case5():
    """self.aがin point, self.bがoff point
    """
    assert DomainAnalysis(70,19).is_pass() == False

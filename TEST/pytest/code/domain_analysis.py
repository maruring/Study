class DomainAnalysis:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def calc_total_score(self):
        return self.a + self.b
    
    def is_pass(self):
        if self.a >= 60 and self.calc_total_score() >= 90:
            return True
        else:
            return False
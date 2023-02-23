class DecisionTable:
    def __init__(self, height, weight, BMI):
        self.height = height
        self.weight = weight
        self.BMI = BMI
    
    def is_pass(self):
        if self.height >= 170 and self.weight >= 65 and self.BMI >= 25:
            return True
        else:
            return False
    
    def is_pass_by_order(self):
        """判定条件の順番の一定の場合
        身長 ⇒ 体重 ⇒ BMI の順で判定する
        """
        if self.height < 170:
            return False
        if self.weight < 65:
            return False
        if self.BMI < 25:
            return False
        
        return True
import numpy as np
from scipy.optimize import minimize

class MinimizePoint:
    def __init__(self, expression, constraints):
        self.expression = expression
        self.constraints = []
        for constraint_str in constraints:
            constraint = {'type': 'ineq', 'fun': lambda x: eval(constraint_str.replace('x', 'x[0]').replace('y', 'x[1]'))}
            self.constraints.append(constraint)
        if 'y' in expression:
            self.x0 = np.array([0, 0])
        else:
            self.x0 = 0
    def objective(self, x, *args):
        return eval(self.expression.replace('x', 'x[0]').replace('y', 'x[1]'))
    def MinimizeResult(self):
        print(self.expression)
        print(self.constraints)
        result = minimize(self.objective, self.x0, constraints=self.constraints)
        return result.x, result.fun
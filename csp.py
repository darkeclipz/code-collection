# For more information, see:
# https://github.com/darkeclipz/or/blob/master/csp/CSP%20(Constraint%20Satisfaction%20Problem).ipynb
import copy
import operator

class Variable():
    def __init__(self, name, D): 
        self.name = name; 
        self.domain = D; 
        self.value = D[0]
    def __hash__(self): return int(''.join([str(ord(x)) for x in self.name]))
    def __eq__(self, v): return v.name == self.name
    def __repr__(self): return '{}={}'.format(self.name, self.value, self.domain)
        
class Constraint():
    def __init__(self, expr, scope): self.expression = expr; self.scope = scope
    def __repr__(self): return self.expression
    def eval(self, V): return eval(self.replace_all(self.expression, {v.name:v.value for v in V}))
    def replace_all(self, text, dic):
        for k, v in dic.items():
            text = text.replace(k, str(v))
        return text
    
class AllDiff(Constraint):
    def __init__(self, scope): self.scope = scope
    def __repr__(self): return 'AllDiff({})'.format(','.join([v.name for v in self.scope]))
    def count_name(self,V): return {v:len(v.name) for v in V}
    def largest_variable_name(self,V): return sorted(self.count_name(V).items(), key=operator.itemgetter(1))
    def eval(self, V): 
        V = [k for k,v in self.largest_variable_name(V)[::-1]]
        return eval(self.replace_all('alldiff([{}])'.format(','.join([v.name for v in V if v in self.scope])), 
                                     {v.name:v.value for v in V}))
    
# Heuristical scope searching algorithm with solution pruning. It starts
# to check if a solution is valid as soon as the scope of a constraint
# is a subset of the solution set. Before solving, by inference, it will sort
# the variables based on in how many constraints they are. With this heuristic
# it will fail as early as possible (which should improve the speed).
class HGSSolver():
    
    # C : scope of the constraint
    # S : solution set
    def all_scope(self, C, S): return all([s in C for s in S]) # c is a subset of S
    def any_scope(self, C, S): return any([s in C for s in S]) # any c is in S
    def k_scope(self, C, S, k): return sum([1 for s in S if s in C]) >= k # c is in S atleast k times
    def count_constraints(self,V,C): return {v:sum([1 for c in C if v in c.scope]) for v in V}
    def most_constrained_order(self,V,C): return sorted(self.count_constraints(V,C).items(), key=operator.itemgetter(1))
    def pre_sort(self,V,C): return [k for k,v in self.most_constrained_order(V,C)]
    
    def __init__(self, variables, constraints):
        self.variables = variables
        self.constraints = constraints
        self.stop_on_first = False
        
    def solve(self):
        self.solution = []
        self.hgs_solve([], self.pre_sort([v for v in self.variables], self.constraints))
        return self.solution[::-1]
    
    def hgs_solve(self, S, V):
        if len(V) == 0: 
            return all([c.eval(S) for c in self.constraints]) 
        elif len(S) > 0:
            for c in self.constraints:
                if isinstance(c, AllDiff) and self.k_scope(S, c.scope, 2): 
                    if not c.eval(S): return
                else:
                    if self.all_scope(S, c.scope) and not c.eval(S): return
        v = V.pop()
        S.append(v)
        for d in v.domain:
            if self.solution and self.stop_on_first: return
            v.value = d
            if self.hgs_solve(copy.deepcopy(S), copy.deepcopy(V)):
                self.solution.append(copy.deepcopy(S))
        return False
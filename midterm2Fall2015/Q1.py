# For each of the expressions in the table below, write the output displayed by the interactive Python interpreter
# when the expression is evaluated. The output may have multiple lines. If more than 3 lines are displayed, just
# write the first 3. If an error occurs, write “Error”. If evaulation would run forever, write “Forever”.
# The first two rows have been provided as examples.
# Assume that you have started python3 and executed the following statements (which do not cause errors):

class Ok:
    py = [3.14]
    
    def __init__(self, py):
        self.ok = self.py
        Ok.py.append(3 * py)
    
    def my(self, eye):
        print(self.my(eye))
        return self.ok.pop()
    
    def __str__(self):
        return str(self.ok)[:4]
    
# 11. Create a class `Logger` with a method `log(message)`. 
# Implement method overloading to log different message types
#  (`error`, `warning`, `info`).
class Logger:
    def log(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(f"{a} {b} {c}")  
        elif a!=None and b!=None:
            print(f"{a} {b}")
        else:
            print(a)
                
            
logger=Logger()
logger.log("error")
logger.log("warning")
logger.log("info")
logger.log("error", "warning", "info")
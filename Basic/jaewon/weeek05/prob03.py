def solution(s):
    
    ss = {"a" : s.count("P") + s.count("p") , "b" : s.count( "Y" ) + s.count( "y" ) }
    if ss["a"]==ss["b"]:
        return True
    else:
        return False
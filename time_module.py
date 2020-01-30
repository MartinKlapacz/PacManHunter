import window_var as var

seconds_since_start = 0 #Zeitpunkt zu Beginn der Runde

def run():
    global seconds_since_start
    seconds_since_start += 1/(var.FPS*4)
    return seconds_since_start #sollen ungefähr eine Sekunde sein 




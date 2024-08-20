import time 

wait_time =1
max_return =5
attempet =0
while attempet <max_return:
    print("ATTEMPET",attempet + 1 ,"-wait time" ,wait_time ,"Second")
    time.sleep(wait_time)
    wait_time*=2
    attempet+=1
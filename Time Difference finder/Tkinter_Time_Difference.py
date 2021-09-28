class Time:
    def __init__(self, current_time ,duration):
        self.current_time = current_time
        self.duration = duration
        for time in current_time:
            sh, sm = [int(i) for i in time.split(":")]
        for tim in duration:
            dh, dm = [int(j) for j in tim.split(":")]
    def ftime(self):
        end_time = []
        eh , em = 00, 00
        if sh + dh> 23:
            eh = 00
        else:
            eh = sh + dh
        if sm + dm>59:
            eh += 1
            em = 00
        else:
            em = sm + dm
        end_time.append(eh)
        end_time.append(em)
        print(f"The class started at {sh}:{sm}. It went on for {dh}:{dm} hours.")
        print(f"Now the time is {eh}:{em}")

ct = input("Enter the starting time in HH:MM in 24 hour format: ").split()
dur = input("Enter the duration of the class in HH:MM in 24 hour format: ").split()
Time(ct,dur)


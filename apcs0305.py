import sys 
for line in sys.stdin: 
    a=int(line) 
    if a != 0: 
        stuScores = []
        students = int(input())
        for i in range (0, students):
            stuScores.append(input())

        stuScores = sorted(stuScores)

        for i in range (0,students):
            print(stuScores[i], end = ' ')
            if (i == students-1) :
                print()
        if (int(stuScores[students-1]) < 60):
            print ("worst case")
        elif (int(stuScores[0]) >= 60) :
            print("best case")
        else :
            for i in range (students-1,-1,-1):
                if (int(stuScores[i]) < 60):
                    print(stuScores[i])
                    break
    
            for i in range (0,students):
                if (int(stuScores[i]) >= 60):
                    print(stuScores[i])
                    break



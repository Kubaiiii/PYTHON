# student marks scenario
marks = 69

if( marks >=0 and marks <= 30) :
    print("BELOW AVERAGE")
elif(marks >= 31 and marks <= 40) :
    print("AVERAGE")
elif(marks >= 41 and marks <= 70) :
    print("ABOVE AVERAGE")
elif(marks > 70 and marks <= 100) :
    print("EXCELLENT")
else:
    print("INVALID MARKS")
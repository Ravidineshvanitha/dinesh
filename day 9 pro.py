time=int(input())
entry=list(map(int,input().split()))
exit=list(map(int,input().split()))
Present=0
Total_guests=0
for i in range(time):
    Present+=entry[i]-exit[i]
    if Total_guests<Presents:
        Total_guests=Present
print(Total_guests,end="")        

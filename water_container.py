max=0
height=list(map(int,input("Height: ").split()))
print(height)

for i in range(0,len(height)):
    for j in range(i+1,len(height)):
      volume=abs((min(height[i],height[j]))*(j-i))
      print(volume)
      if volume>=max:
         max=volume

print(max)
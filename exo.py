a = 5
b = 7.07106781187 
c = 5
# b= 4


if a == b and b == c:
    print("triangle équilatéral")

elif a == b or a == c or b == c:
    
    hypotenuse = max(a, b, c)
    
    print("triangle isocèle", end="")
    
    if hypotenuse == a:
        if abs(b*b + c*c - a*a) < 0.0001:
            print(" rectangle")
        else:
            print()
    elif hypotenuse == b:
        if abs(a*a + c*c - b*b) < 0.0001:
            print(" rectangle")
        else:
            print()
    else:  
        if abs(a*a + b*b - c*c) < 0.0001:
            print("rectangle")
        

#  l'écart entre les deux côtés de l'équation est tellement petit qu'on considère qu'ils sont égaux (pour regler le probl de floats) en maths ce serait 0
elif abs(a*a + b*b - c*c) < 0.0001 or abs(a*a + c*c - b*b) < 0.0001 or abs(b*b + c*c - a*a) < 0.0001:
    print("triangle rectangle")

else:
    print("triangle quelconque")

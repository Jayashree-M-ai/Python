class manyfunctions():
    def subfields():
        print("Sub-fields of AI are: ")
        print("Machine Learning ")
        print("Neural Networks ")
        print("Vision ")
        print("Robotics ")
        print("Speech Processing ")
        print("Natural Language Processing ")
    
    def oddeven(num):
        if(num%2==0):
            a="Even Number"
        else:
            a="Odd Number"
        return a

    def eligible(gen,age):
        if(gen=="male" and age>20):
            msg="Eligible"
        elif(gen=="female" and age>17):
            msg="Eligible"
        else:
            msg="Not Eligible"
        return msg

    def per():
        s1=int(input("Enter the Subject 1"))
        s2=int(input("Enter the Subject 2"))
        s3=int(input("Enter the Subject 3"))
        s4=int(input("Enter the Subject 4"))
        s5=int(input("Enter the Subject 5"))
        tot=s1+s2+s3+s4+s5
        per=tot/5
        return tot,per

    def area():
        h=int(input("Enter Height"))
        b=int(input("Enter Breadth"))
        print("Area Formala:(Height*Breadth)/2")
        a=(h*b)/2
        return a

    def peri():
        h1=int(input("Enter Height1"))
        h2=int(input("Enetr Height2"))
        b=int(input("Enter Breadth"))
        print("Perimeter formula: Height1 + Height2 + Breadth")
        p=h1+h2+b
        return p
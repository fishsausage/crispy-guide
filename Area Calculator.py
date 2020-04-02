print(" ---Area Calculator--=Area Calculator English Mode v1.1 =--rotaluclaC aerA---")
print("                      This program by FishSausage Tech Otaku")
print("                 FishSausage Tech Otaku All rights reserved.")
print("                          There is a funny egg in it!")
print("     Plan to launch more calculation function,for example Sao Hua(Cross out)")
print('''
      ______ _     _        _____                                  
     |  ____(_)   | |      / ____|                                 
     | |__   _ ___| |__   | (___   __ _ _   _ ___  __ _  __ _  ___ 
     |  __| | / __| '_ \   \___ \ / _` | | | / __|/ _` |/ _` |/ _ 
\
     | |    | \__ \ | | |  ____) | (_| | |_| \__ \ (_| | (_| |  __/
     |_|    |_|___/_| |_| |_____/ \__,_|\__,_|___/\__,_|\__, |\___|
                                                        __/ |     
Tencent QQ:2441435962(PRC) GitHub:Fish Sausage         |___/
________________________________________________________________________________                                                        
''')
while 3>2:
    chose = (input('Rectangle(1) Square(2) Triangle(3) Trapezoidal(4) Circle(5)（Input the serial number to select,press "Enter" key to be continue.）' ))                                                                                                                                                                                                                                                                                                                                                        
    if chose=="5":
        radiusordiameter = (input('Do you have a radius(r) or a diameter(d)?：'))
        if radiusordiameter == "r":
            def circle():
                radius = int(input('Please input radius.:'))
                result = 3.14*(radius*radius)
                print(f'Area of a circle is: {result}')
            circle()
        else:
            def circle():
                diameter = int(input('Please input diameter.:'))
                result = 3.14*((diameter/2)*(diameter/2))
                print(f'Area of a circle is: {result}')

            circle()       
    else:
        if chose == "2":
                def square():
                    side = int(input('Please enter side length.:'))
                    result = side*side
                    print(f'Area of a square is: {result}')

                square()
        else:
            if chose == "1":
                def rectangle():
                    length = int(input("Please enter height.:"))
                    wide = int(input("Please enter width.:"))
                    result = length*wide
                    print(f'Area of a rectangle is: {result}')

                rectangle()
            else:
                if chose == "3":
                    def Triangle():
                        Bottomlength = int(input('Please enter bottom length：'))
                        height = int(input('Pleath enter height：'))
                        result = Bottomlength*height/2
                        print(f'Area of a triangle is: {result}')

                    Triangle()
                if chose == "f":
                    def Egg():
                        mom = int(input('Please enter your mother’s age：'))
                        dad = int(input('Please enter your father’s age'))
                        grd = int(input('Please enter your grandfather’s age：'))
                        grm = int(input('Please enter your grandmother’s age：'))
                        fen = int(input('Please enter score for this software!!!：'))
                        result = (grd * grm) + 5 / (mom + dad)
                        print(f'Your grandfather’s age × your grandmother’s age add 5 and be divided by sum of your mother,father’s age= {result}')
                        print('You enter 5.Full marks 5.(Funny)')

                    Egg()
                else:
                    if chose == "4":
                        def echelon():
                            Upperbottom = int(input('Please enter upperbottom：'))
                            lowerbottom = int(input('Please enter lowerbottom：'))
                            hight = int(input('Please enter hight：'))
                            result = (Upperbottom + lowerbottom)*hight/2
                            print(f'Area of a trapezoidal is: {result}')

                        echelon()
                    else:
                        print("You have entered an unsupported main.You must re-enter,otherwise, within three days your ashes were all winnow away!")

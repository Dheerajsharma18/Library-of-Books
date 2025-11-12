import webbrowser
print("WELCOME")
def run():
        print("press 1 for continue")
        print("press 2 for Exit")

a=int(input("Continue or exit"))
if a==1:
    print("Continue")
elif a==2:
    print("Thankyou for visiting")


def book():
    print("press 1 for book1")
    print("press 2 for book2")
    print("press 3 for book3")
    print("press 4 for book4")
book()


b=int(input("Enter book number to continue"))
if b==1:
    print("Philosophy book-The Prine")
    webbrowser.open("https://www.pdfbooksworld.com/bibi/pre.html?book=112.epub")

    run()

    
elif b==2:
    print("java books")
    webbrowser.open("https://www.iitk.ac.in/esc101/share/downloads/javanotes5.pdf")


    run()

elif b==3:
    print("Python books")
    webbrowser.open("https://greenteapress.com/wp/think-python-2e/")


    run()

elif b==4:
    print("C+ programming language books")
    webbrowser.open("https://archive.org/details/c-in-depth-2nd-ed.-srivastava.pdf")


    run()

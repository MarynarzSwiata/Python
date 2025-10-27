def Note(note):
    with open('100daysChallenge/mini-projects/welcome.txt', 'w') as f:
        f.write(f"\n {note}")
        
def open_File():
    with open('100daysChallenge/mini-projects/welcome.txt', 'r') as f:
        f.read()

Note(str(input("Napisz swoja notatkę: \n")))
open_File()
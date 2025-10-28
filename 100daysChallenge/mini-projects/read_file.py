file_scr = "100daysChallenge/mini-projects/notes_journal.txt"

def save_note(note):
    with open(file_scr, 'a') as f:
        f.write(f"{note}\n")
        
def read_journal():
    with open(file_scr, 'r') as f:
        notes_lines = f.readlines()
        for i, note in enumerate(notes_lines, start=1):
            print(f"{i}. {note.strip()}")

#save_note(str(input("Napisz swoja notatkę: \n")))
read_journal()
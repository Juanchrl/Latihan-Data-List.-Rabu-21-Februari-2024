notes = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti"]
notes2 = ["Mi", "Do", "Fa", "So", "La", "Ti", "Re"]

def custom_sort(note):
    return notes2.index(note)

notes.sort(key=custom_sort)
print(', '.join([f'"{note}"' for note in notes]))

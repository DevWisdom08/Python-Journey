from django.shortcuts import render

def caesar(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'
    if not encrypt:
        shift = -shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(),
                                      shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def index(request):
    result = ''
    if request.method == 'POST':
        text = request.POST.get('text', '')
        shift = int(request.POST.get('shift', 3))
        action = request.POST.get('action', 'Encrypt')
        if action == 'Encrypt':
            result = caesar(text, shift)
        else:
            result = caesar(text, shift, encrypt=False)
    return render(request, 'cipher/index.html', {'result': result})


def create_character(name, strength, intelligence, charisma):
    """Create an RPG character with stat validation."""
    # Validate name type
    if not isinstance(name, str):
        return "The character name should be a string"
    # Validate name length
    if len(name) > 10:
        return "The character name is too long"
    # Validate name spaces
    if " " in name:
        return "The character name should not contain spaces"
    # Validate stats integers
    stats = [strength, intelligence, charisma]
    if not all(isinstance(s, int) for s in stats):
        return "All stats should be integers"
    # Validate minimum
    if any(s < 1 for s in stats):
        return "All stats should be no less than 1"
    # Validate maximum
    if any(s > 4 for s in stats):
        return "All stats should be no more than 4"
    # Validate total
    if sum(stats) != 7:
        return "The character should start with 7 points"
    # Dot builder
    def build_line(label, value):
        full_dots = "●" * value
        empty_dots = "○" * (10 - value)
        return f"{label} {full_dots}{empty_dots}"
    
    return "\n".join([
        name,
        build_line("STR", strength),
        build_line("INT", intelligence),
        build_line("CHA", charisma),
    ])


def character_creator(request):
    result = ''
    error = ''
    if request.method == 'POST':
        name = request.POST.get('name', '')
        try:
            strength = int(request.POST.get('strength', 0))
            intelligence = int(request.POST.get('intelligence', 0))
            charisma = int(request.POST.get('charisma', 0))
        except ValueError:
            strength = 0
            intelligence = 0
            charisma = 0
        
        result = create_character(name, strength, intelligence, charisma)
    
    return render(request, 'cipher/character.html', {'result': result})
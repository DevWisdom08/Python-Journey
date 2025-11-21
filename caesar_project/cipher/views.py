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

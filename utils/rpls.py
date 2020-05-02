def multi_replace(target, value):
    # Удаление недопустимых символов
    for wrong, correct in value.items():
        target = target.replace(wrong, correct)
    return target


values = {
    '/': '',
    ':': '',
    '*': '',
    '?': '',
    '"': '',
    '<': '',
    '>': '',
    '|': ''
}

madlib_word_choices = {
    "proper_noun_1": "",
    "proper_noun_2": "",
    "noun": "",
    "verb_past": "",
    "adjective": ""
}

madlib_word_choices["adjective"] = input("Enter a adjective: ")
madlib_word_choices["proper_noun_1"] = input("Enter a proper_noun_1: ")
madlib_word_choices["proper_noun_2"] = input("Enter a proper_noun_2: ")
madlib_word_choices["noun"] = input("Enter a noun: ")
madlib_word_choices["verb_past"] = input("Enter a verb_past: ")


print("One fine morning, a %s fellow by the name of %s visited the town of %s. Then he tripped over a %s and %s." % (madlib_word_choices['adjective'], madlib_word_choices['proper_noun_1'], madlib_word_choices['proper_noun_2'], madlib_word_choices['noun'], madlib_word_choices['verb_past']))
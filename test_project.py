import pytest
import project

def test_is_valid():
    # tests al rules for accepted strings
    assert project.is_valid("This is an accepted string") == True
    assert project.is_valid("This is An accepted string  ") == True
    assert project.is_valid("This is ** NOT ** accepted string") == False
    assert project.is_valid(" ") == False
    assert project.is_valid("This is a number 898") == False
    assert project.is_valid("This is very long accepted string, this is very long accepted string") == False

def test_check_spaces_letters():
    # tests REGEX - if the string passed contains only letters and spaces
    assert project.check_spaces_letters("50") == False
    assert project.check_spaces_letters(" This is accepted ") == True
    assert project.check_spaces_letters("Not valid.") == False
    assert project.check_spaces_letters("Are you valid?") == False
    assert project.check_spaces_letters("And .... not valid") == False
    assert project.check_spaces_letters("Okay I am  valid") == True

def test_is_valid_dic():
    #test is the response from API call comes in a format that be converted to JSON
    assert project.is_valid_dic("50") == False
    assert project.is_valid_dic("this is a string, not a dict") == False

    students = '''{"Hermione": "Gryffindor",
                "Harry": "Gryffindor",
                "Rony": "Gryffindor",
                "Draco": "Slytherin" }'''

    assert project.is_valid_dic(students) == False #lacks key meaning

    dictionary = '''{"meaning": "NOT_FOUND",
                "Harry": "Gryffindor",
                "Rony": "Gryffindor",
                "Draco": "Slytherin" }'''

    assert project.is_valid_dic(dictionary) == False #meaning key has value NOT_FOUND

    kat = '''{
    "word": "kat",
    "meaning": "Een huisdier dat behoort tot de familie van de katachtigen en bekend staat om zijn onafhankelijke karakter en het vermogen om muizen en andere kleine dieren te vangen.",
    "type": "zelfstandig naamwoord",
    "synoniem": "poes, kater, huiskat",
    "antoniem": "hond",
    "sentence_01": "Mijn kat houdt ervan om op mijn schoot te liggen terwijl ik tv kijk.",
    "sentence_02": "De kat van mijn buurman is altijd buiten aan het rondzwerven.",
    "sentence_03": "Ik heb een allergie voor kattenhaar, dus ik kan geen kat als huisdier hebben.",
    "present": "kat",
    "perfectum": "gekat",
    "imperfectum": "katte",
    "article": "de"
    }'''

    assert project.is_valid_dic(kat) == True #IMPORTANT: passing string keys and values need to be encapusulated by double-quotes
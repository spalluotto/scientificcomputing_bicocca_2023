import re
import os
from plot_frequency_func import plot_freq

def test_word_count():
    test_file = "test.txt"
    with open(test_file, "w") as f:
        f.write("cane gatto pera\n")
        f.write("topo gatto pera\n")
        f.write("cane gatto mela\n")

    result = plot_freq(test_file,plot=False)
    
    expected = {"cane": 2, "gatto":3,"topo":1,"pera":2,"mela":1}
    assert result == expected
    os.remove(test_file)
    
def test_regression():
    test_file = "test.txt"
    with open(test_file, 'w') as f:
        f.write("penna gomma penna\n")
        f.write("presa gomma presa\n")
        f.write("scarpa gomma penna\n")

    result = plot_freq(test_file, plot=False)
    expected = {"penna": 3, "gomma":3 , "presa":2, "scarpa":1}

    assert result == expected
    os.remove(test_file)
    
def test_top_word():
    test_file = "test.txt"
    with open(test_file, 'w') as f:
        f.write("cane gatto pera\n")
        f.write("topo gatto pera\n")
        f.write("cane gatto mela\n")
        f.write("cane gatto pera\n")
        f.write("topo gatto pera\n")
        f.write("cane gatto mela\n")

    result = plot_freq(test_file, plot=False)

    top_word = list(result.keys())[0]
    assert top_word == 'gatto'
    os.remove(test_file)

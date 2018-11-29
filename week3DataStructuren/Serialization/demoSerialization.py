import pickle

def main():
    naam = "studenten.dat"
    bepaalBi(naam)


def bepaalBi(bestandsnaam):
    meer = 'j'
    try:
        input_file = open(bestandsnaam, 'rb')
        bi1 = pickle.load (input_file)
        input_file.close()
    except IOError:
        bi1 = set()
    while meer.lower() == 'j':
        print ("Studenten in Bi1: ",bi1)
        student = input('Student: ')
        bi1.add (student)
        meer = input ("Doorgaan (j/n)")
    output_file = open(bestandsnaam, 'wb')
    pickle.dump(bi1, output_file)
    output_file.close()

main()

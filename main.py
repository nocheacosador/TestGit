from Printing import Printer, GetPrinter

def Main():
    printer = GetPrinter('html')

    printer.Header('Kopūstas')
    printer.Paragraph(  'Kopūstas (Brassica oleracea) – bastutinių (Brassicaceae) '
                        'šeimos augalų rūšis. Tai dvimetis (kai kurie varietetai '
                        'vienmečiai) žydintis augalas, kurio žiedai gausiažiedėje '
                        'kekėje. Vainiklapiai geltoni, kartais balti. Ankštaros labai '
                        'stambios. Stiebas lapuotas, apatiniai lapai stambūs, mėsingi. '
                        'Visas augalas pilkai žalias.')

    printer.Print()

if __name__ == '__main__':
    Main()
    # Some change that should not be allowed
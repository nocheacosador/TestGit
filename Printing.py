from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def Header(self, header: str) -> None:
        pass
    
    @abstractmethod
    def Paragraph(self, paragraph: str) -> None:
        pass

    @abstractmethod
    def Print(self) -> None:
        pass

class StdoutPrinter(Printer):
    def Header(self, header: str) -> None:
        header_capitalized = header.upper()
        print()
        print('    ' + header_capitalized)
        print()
    
    def Paragraph(self, paragraph: str) -> None:
        char_count = 0
        print(' ', end='')
        for word in paragraph.replace('\n', ' ').split(' '):
            if char_count >= 50:
                print()
                char_count = 0
            print(word, end=' ')
            char_count += len(word) + 1
        print()

    def Print(self) -> None:
        pass


def GetPrinter(printer: str) -> Printer:
    match printer:
        case 'Stdout':
            return StdoutPrinter()
        case _:
            raise RuntimeError(f"There is no printer '{printer}'")
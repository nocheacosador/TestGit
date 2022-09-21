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


class HtmlPrinter(Printer):
    def __init__(self) -> None:
        super().__init__()
        self.content = '<!DOCTYPE html><html><head><title>Title</title></head><body>'


    def Header(self, header: str, level: int = 3) -> None:
        if level > 3: level = 3
        self.content += f'<h{level}>{header}</h{level}>'
    
    def Paragraph(self, paragraph: str) -> None:
        self.content += f'<p>{paragraph}</p>'

    def Print(self) -> None:
        self.content += '</body></html>'
        with open('out.html', 'w', encoding='utf-8') as file:
            file.write(self.content)
        
def GetPrinter(printer: str) -> Printer:
    match printer:
        case 'stdout':
            return StdoutPrinter()
        case 'html':
            return HtmlPrinter()
        case _:
            raise RuntimeError(f"There is no printer '{printer}'")

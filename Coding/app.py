import random

class Code:
    def __init__(self, file_name:str, language : str, file_type:str, typing: str, ide_used: str) -> None:
        self.file_name = file_name
        self.language = language
        self.file_type = file_type
        self.typing  = typing
        self.ide_used = ide_used
        self.has_errors = True

    def error_found(self) -> None:
        if self.has_errors:
            print(f'The {self.language} file {self.file_name}.{self.file_type} has an error in line {random.randint(1,193)}')
        else:
            self.has_errors = False
            print("No errors were found")

    def error_fixed(self) -> None:
        if self.has_errors:
            self.has_errors = False
            print("No errors were found")
        else:
            print(f'The {self.language} file {self.file_name} has an error in line {random.randint(1,193)}')

    def run_code(self) -> None:
        if self.has_errors == False:
            print("Process finished with exit code 0")
        else:
            print(f'Unable to run {self.language} file {self.file_name}.{self.file_type}')

    def __str__(self) -> str:
        return f'{self.file_name}.{self.file_type} is a {self.typing}ly typed {self.language} file written in the {self.ide_used} IDE'

code1: Code = Code("app", "Python", "py", "dynamic", "Pycharm")
code2: Code = Code("store_analysis","R", "R","dynamic", "RStudio")
code3: Code = Code("wound_assay","C++", "cpp","static", "VSCode")

code3.error_found()
code3.run_code()
code3.error_fixed()
code3.run_code()
print(code3)
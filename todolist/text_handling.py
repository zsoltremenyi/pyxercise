


class TextHandler():
    def __init__(self, prompt, text_file):
        self.prompt = prompt
        self.text_file = text_file

    def read_text(self):
        with open(self.text_file, "r") as f:
            data = f.read()
            return data

    def adding_tasks(self):
        with open(self.text_file, "r") as file:
            data = file.readlines()

        with open(self.text_file, 'a') as file:
            for i in self.prompt:
                if i+"\n" not in data:
                    file.write(f"{i}\n")

    def del_task(self):
        with open(self.text_file, "r") as file:
            data = file.readlines()
        with open(self.text_file, "w") as file:
            for line in data:
                if line.strip("\n") not in self.prompt:
                    file.write(line)
class Text:
    def __init__(self, file):
        self.file = file
    
    def stats(self):
        with open(self.file, 'r') as file:
            line = file.readline()
            num_lines = len(line)
            
            content = file.read()
            word_ = content.split()
            num_words = len(word_)

            num_characters = len(content)
        output = f"=== STATS ===\nLines: {num_lines}\nWords: {num_words}\nCharacters: {num_characters}"
        return output
    
    def top(self, r):
        top_ = dict()
        with open(self.file, 'r') as file:
            for line in file:
                line = line.strip().lower()
                words = line.split(" ")
                
                for word in words:
                    top_[word] = top_.get(word, 0) + 1


        sorted_top = sorted(top_.items(), key = lambda x: x[1], reverse=True)
        output = '\n=== TOP WORDS ===\n'
        for word, count in sorted_top[:r]:
                output += f"{word}\t- {count}\n"

        return output
    

    def match(self, pattern):
        top_ = dict()
        with open(self.file, 'r') as file:
            for i, line in  enumerate(file, start=1):
                l_line = line.split()
                if pattern in l_line:
                    top_[f"Line {i}"] = line.strip()
        
        output = '\n=== MATCH ===\n'
        for name, value in top_.items():
            output += f"{name}: {value}\n"
            
        return output



            
                

            

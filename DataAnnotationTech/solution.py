class Solution():
    def decode(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()

        data = []
        for line in lines:
            number, word = line.split()
            data.append((int(number), word))

        data.sort()

        output = []
        line_index_end = 0
        while line_index_end < len(data):
            line_len = len(output) + 1
            line_index_end += line_len
            if line_index_end - 1 < len(data):
                output.append(data[line_index_end - 1][1])

        return ' '.join(output)
    
decoder = Solution()
file = "coding_qual_input.txt"

print(decoder.decode(file))

# prints: young system present student lot experiment strong crease sun company hurry remember milk us repeat clothe against meant history indicate pitch print bread would
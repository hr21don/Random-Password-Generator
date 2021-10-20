import secrets

def generate_pass(num_words):
    with open('dicewarewordlist.txt', 'r') as file: #opens the diceware wordlist with the context manager 
        lines = file.readlines()[2:7778] #uses the readlines function to give a list of each line in the file
        words_list = [line.split()[1] for line in lines]#split method to build a list containing just words
    words = [secrets.choice(words_list) for i in range(num_words)] #building a list using the desired number of random words using the secret choice function
    return ' '.join(words)#combine the random words into a single string with spaces between them


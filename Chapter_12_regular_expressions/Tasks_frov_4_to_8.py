import re

# Task 4:
mammoth = """
            We have seen the Queen of cheese,
            Laying quietly at your ease,
            Gently fanned by evening breeze --
            Thy fair form no flies dare seize.
            
            All gaily dressed soon you'll go
            To the great Provincial Show,
            To be admired by many a beau
            In the city of Toronto.
            
            Cows numerous as a swarm of bees --
            Or as the leaves upon the trees --
            It did require to make thee please,
            And stand unrivalled Queen of Cheese.
            
            May you not receive a scar as
            We have heard that Mr. Harris
            Intends to send you off as far as
            The great World's show at Paris.
            
            Of the youth -- beware of these --
            For some of them might rudely squeeze
            And bite your cheek; then songs or glees
            We could not sing o' Queen of Cheese.
            
            We'rt thou suspended from baloon,
            You'd cast a shade, even at noon;
            Folks would think it was the moon
            About to fall and crush them soon. 
          """

# Task 5:
result = re.findall(r'\bc\w*\b', mammoth)  # найти все слова, начинающиеся на "c".
print(result)

# Task 6:
result = re.findall(r'\bc\w{3}\b', mammoth)  # найти все слова, состоящие из 4 букв и начинающиеся на "c"
print(result)

# Task 7:
result = re.findall(r'\b\w*r\b', mammoth)  # найти все слова, заканчивающиеся на "r".
print(result)

# Task 8:
result = re.findall(r'\b\w*[aeuio]{3}\w*\b', mammoth)  # найти все слова, содержащие три гласных подряд
print(result)

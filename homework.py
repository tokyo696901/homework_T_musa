def main():

    print(" translates words to morse code\n")

    words = input("write here to be encoded: ")
    words = words.upper()

    codeDict = createDict()

    i = 0

    try:
        while (i < len(words)):
            if (words[i] != " "):
                print(codeDict[words[i]], end = " ")
            else:
                print("/", end = " ")
            i += 1
    except:
        print("\nInvalid characters found - refer to morse code alphabet")


def createDict():
    code = {'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----'}

    return code


main()
=+=+=+=+=+=+=+=+=+=+=+=+=+=+==+=+=+=+=+=+==+=+=+=+=+=+==+=+=+=+=+==+=+=+=+==+=+=+==+=+=+==+=+=+=+=+==+=+=+=+==+=+=+==+=+=+==+=+=+=+==+=+=+==+=+=+=+==+=+==+=+=+==+=+=+=+==+==+=+=+=+==+=+=+=+=+=+=+==+=+=+=+=+=+==+=+=+=+==+=+=+=+=+=+=+=+=+==+=+=+==+=+=+==+=+=+==+==+=+=+==+



  f = open("train.csv", "r")
  tokyo = f.readlines()
  f.close()
   
  count = 0
  all_male = 0
  all_female = 0

  t = []
  for i in range(1, len(tokyo)):
      t = a[i].strip().split(',')
      if t[1] == '1' and t[5] == 'male':
          male += 1
      if t[1] and t[5] == 'female':
          female += 1
   
  count = all_male + all_female
  print ("total number of survivors:",  count)
  print ("number of surviving men:",  all_male)
  print ("number of surviving women:",  all_female)


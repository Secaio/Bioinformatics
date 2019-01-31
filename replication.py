# Input:  A string Text and an integer k
# Output: A list containing all most frequent words in Text	
def FrequentWords(Text, k):
    words = [] # output variable
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq: # add each key to words whose corresponding frequency value is equal to m
        if freq[key] == m:
            words.append(key)
    words.sort()
    return words	
	
def FrequentWords1(Text, k):
    FrequentPatterns = [] # output variable
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m: # add each key to words whose corresponding frequency value is equal to m
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    return freq
	
def FrequencyMap1(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        for chave in freq:
            if (chave == Pattern):
                freq[chave]+=1;
    return freq
		
# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
def CountDict(Text, k):
    Count = {} # output variable
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

def remove_duplicates(Items):
    ItemsNoDuplicates = [] # output variable
    for i in Items:
        if i not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(i)
    return ItemsNoDuplicates
	
# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    tmp = []
    for char in Pattern:
        tmp.insert(0,char)
    return "".join(map(str, tmp))	

# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = '' # output variable
    i = len(Pattern) - 1
    while i >= 0:
        revComp = revComp + complement(Pattern[i])
        i -= 1
    return revComp
	
# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement1(Pattern):   
    # your code here
    return Complement(Reverse(Pattern))
	
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    if Nucleotide == 'A':
        comp = 'T'
    if Nucleotide == 'T':
        comp = 'A'
    if Nucleotide == 'C':
        comp = 'G'
    if Nucleotide == 'G':
        comp = 'C'
    return comp

def inversComplement(input):
    output = ''
    for letter in input:
        letter = letter.upper()
        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        else:
            output += 'G'
    return output

# Input:  Two strings, Pattern and Genome
# Output: A list containing all starting positions where Pattern appears as a substring of Genome
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions
	
# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    # look at the first half of Genome to compute first array value	
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n): # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:# the current array value can differ from the previous array value by at most 1
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

# Input:  A String Genome
# Output: Skew(Genome)
def Skew(Genome):
    skew = {} #initializing the dictionary
    skew[0] = 0
    for i in range(1,len(Genome)+1):
        if Genome[i-1] == "G":
            skew[i] = skew[i-1]+1
        elif Genome[i-1] == "C":
            skew[i] = skew[i-1]-1
        else:
            skew[i] = skew[i-1]
    return skew
	
def Skew1(Genome):
    skew = [] #initializing the list
    skew.append(0)
    for i in range(1,len(Genome)+1):
        if Genome[i-1] == "G":
            skew.append(skew[i-1]+1)
        elif Genome[i-1] == "C":
            skew.append(skew[i-1]-1)
        else:
            skew.append(skew[i-1])
    return skew
	
# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    SkewGenome = Skew(Genome)
    minimum = min(SkewGenome.values())
    for i in range(1,len(SkewGenome)):
        if SkewGenome[i] == minimum:
            positions.append(i)
    return positions

# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance = distance + 1
    return distance

# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            positions.append(i)
    return positions

# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            count = count+1
    return count

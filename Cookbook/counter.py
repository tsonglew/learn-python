words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)

top_three = word_counts.most_common(3)
print top_three

print word_counts['not']
print word_counts['eyes']

# add count by yourself
word_counts['not'] += 1
print word_counts['not']
# or function update()
word_counts.update(['not'])
print word_counts['not']

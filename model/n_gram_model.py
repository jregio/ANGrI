import random
from collections import defaultdict

class NgramModel:
    def __init__(self, n):
        self.n = n
        self.ngram_counts = defaultdict(int)
        self.total_ngrams = 0
        
    def train(self, sentences):
        """Train the n-gram model on a list of sentences."""
        for sentence in sentences:
            chars = list(sentence)
            # Add padding for beginning and end of sentence
                
            for i in range(len(chars)-self.n+1):
                # Get n-gram
                ngram = tuple(chars[i:i+self.n])
                
                # Update counts
                self.ngram_counts[ngram] += 1
                self.total_ngrams += 1

    def calculate_probabilities(self):
        """Calculate probabilities for each n-gram."""
        probabilities = {}
        for ngram, count in self.ngram_counts.items():
            probabilities[ngram] = count / self.total_ngrams
        return probabilities
    
    def sample_ngram(self):
        """Sample a single n-gram based on their probabilities."""
        if not self.ngram_counts:
            return None
            
        # Calculate probabilities
        probs = self.calculate_probabilities()
        
        # Get list of n-grams and their probabilities
        ngrams = list(probs.keys())
        probabilities = list(probs.values())
        
        # Sample one n-gram using the probabilities
        sampled_ngram = random.choices(ngrams, weights=probabilities, k=1)[0]
        return ''.join(sampled_ngram)

    
import PyPDF2
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest
import nltk



nltk.download('punkt')
nltk.download('stopwords')
def summarize_pdf(file_path, num_sentences):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Extract the text from each page
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Tokenize the text into sentences
        sentences = sent_tokenize(text)

        # Tokenize the text into words and remove stop words
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text.lower())
        word_freq = {}
        for word in words:
            if word not in stop_words:
                if word not in word_freq.keys():
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1
                sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word_freq.keys():
                    if len(sentence.split(' ')) < 30:
                        if sentence not in sentence_scores.keys():
                            sentence_scores[sentence] = word_freq[word]
                        else:
                            sentence_scores[sentence] += word_freq[word]

        # Get the top N sentences with the highest scores
        summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

        # Join the summary sentences into a single string
        summary = ' '.join(summary_sentences)

        return summary

# Example usage
file_path = r'C:\Users\Lenovo\OneDrive\Desktop\TEST\BJP.pdf'

num_sentences = 10  # Number of sentences in the summary
summary = summarize_pdf(file_path, num_sentences)
print(summary)
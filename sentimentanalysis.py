from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def analyze(filename):
    analyzer = SentimentIntensityAnalyzer()
    total_lines = 0
    positive = 0
    negative = 0

    with open(filename, 'r') as file:
        for line in file.read().split('\n'):
            total_lines += 1
            vs = analyzer.polarity_scores(line)
            if vs['pos'] > 0.51:
                positive += 1
            if vs['neg'] > 0.51:
                negative += 1
    result = f'Positive {round((positive / total_lines) * 100, 2)}% Negative {round((negative / total_lines) * 100, 2)}%'
    return str(result)






















if __name__ == '__main__':
    filename = 'placeholder'
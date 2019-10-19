import nltk
from nltk.translate.bleu_score import SmoothingFunction
class NotBleuException(Exception):
    pass
class NotMeteorException(Exception):
    pass
def BleuFunction(order=4):
    cc = SmoothingFunction()
    if (4 == order):
        sf = cc.method4
    elif (3 == order):
        sf = cc.method3
    elif (2 == order):
        sf = cc.method2
    elif (1 == order):
        sf = cc.method1
    else:
        raise NotBleuException
    return sf

def nltk_sentence_bleu(hypothesis, reference, order=4):
    try:
        sf = BleuFunction(order)
        return nltk.translate.bleu([reference], hypothesis, smoothing_function=sf)
    except:
        raise NotBleuException

def nltk_corpus_bleu(hypotheses, references, order=4):
    refs = []
    count = 0
    total_score = 0.0

    try:
        sf = BleuFunction(order)
    except:
        raise NotBleuException

    for hyp, ref in zip(hypotheses, references):
        hyp = hyp.split()
        ref = ref.split()
        refs.append([ref])

        score = nltk.translate.bleu([ref], hyp, smoothing_function=sf)
        total_score += score
        count += 1

    avg_score = total_score / count
    corpus_bleu = nltk.translate.bleu_score.corpus_bleu(refs, hypotheses)
    print('corpus_bleu: %.4f avg_score: %.4f' % (corpus_bleu, avg_score))
    return corpus_bleu, avg_score


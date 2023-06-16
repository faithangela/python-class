import lmproof
def proofread(text):
    proofread = improoof.load("en")
    correction = proofread.proofread(text)
    print("original: {}".format())
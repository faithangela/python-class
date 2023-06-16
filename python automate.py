import lmproof
def proofread(text):
    proofread = improoof.load("en")
    correction = proofread.proofread(text)
    print("original: {}".format(text))
    print("correction: {}".format(correction))
proofread("Your Text")    
    
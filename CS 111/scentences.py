"""
Write a Python program named sentences.py that 
generates simple English sentences. 
During this prove milestone, you will 
write functions that generate sentences with three parts:

a determiner (sometimes known as an article)
a noun
a verb
In other words, your program will build and 
output sentences in this form:

Sentence = [Determiner] + [noun] + [verb] + .
For example:

A cat laughed.
Some girls thought.
One man eats.
Many dogs run.
The woman will think.
Many men will write.
For this milestone, your program must include 
at least these five functions:

main
make_sentence
get_determiner
get_noun
get_verb
You may add other functions if you want. 
The functions get_determiner, get_noun, and get_verb 
must randomly choose a word from a list of words 
and return the randomly chosen word. 
All the functions that you must write for this milestone 
assignment are described in the Steps section below.
"""
determiners_plural_list = ["many", "some","a group of","those", "few","several","various","numerous","multiple","a lot of","thousands of", "both the"]
determiners_single_list = ["every","another","one","a","this","that","each","the"]
nouns_single_list = ["robot", "engine","river","clown","reflection","lantern","person","man","woman","child","boy","girl","dog","cat","bat","bug","giraffe","tiger","mokey","fish"]
nouns_plural_list = ["robots","engines","rivers","clowns", "reflections","lanterns","people","men","women","children","boys","girls","dogs","cats","bats","bugs","giraffes","tigers","monkeys","fish"]
verbs_plural_prsnt_future = ["eat","go","run","talk","laugh","jump","speak","write","read","think","sleep","fly","cook","study","cry","sing","grow","watch"]
verb_single_prsnt = ["eats","goes","runs","talks","laughs","jumps","speaks","writes","reads","thinks","sleeps","flies","cooks","studies","cries","sings","grows","watches"]
verb_past = ["ate","went","ran","talked","laughed","jumped","spoke","wrote","read","thought","slept","flew","cooked","studied","cried","sang","grew","watched"]
import random

def main():
    plural = bool(random.randint(0,1))
    tense = random.randint(0,3)
    negative = random.randint(0,1)

    make_sentence(plural, tense, negative)

def get_determiner(single_plural):
    if single_plural == True:
        return random.choice(determiners_plural_list)
    else:
        return random.choice(determiners_single_list)

def get_noun(single_plural):
    if single_plural == True:
        return random.choice(nouns_plural_list)
    else:
        return random.choice(nouns_single_list)


def get_verb(single_plural, past_prsnt_ftr, pstv_ngtv):
    verb =""
    if past_prsnt_ftr == 0:
        if pstv_ngtv == 0:
            verb = random.choice(verb_past)
        else:
            verb = "did not " + random.choice(verbs_plural_prsnt_future)
    elif past_prsnt_ftr == 1:
        if single_plural==1:
            if pstv_ngtv == 0:
                verb = random.choice(verbs_plural_prsnt_future)
            else:
                verb = "do not " + random.choice(verbs_plural_prsnt_future)
        else:
            if pstv_ngtv == 0:
                verb = random.choice(verb_single_prsnt)
            else: 
                verb = "does not " + random.choice(verbs_plural_prsnt_future)
    else:
        if pstv_ngtv == 0:
            verb = "will " + random.choice(verbs_plural_prsnt_future)
        else:
            verb = "will not " + random.choice(verbs_plural_prsnt_future)
    return verb
    

def make_sentence(plural, past_prsnt_ftr, ngtv):
    sentence =  "\n"+get_determiner(plural).capitalize() + " "+ get_noun(plural) + " "+ get_verb(plural, past_prsnt_ftr, ngtv) + "."
    print(f"{sentence}")
        
input("Click enter to generate a random sentence. ")

main()
more = "y"
while more == "y" or more == "Y":
    more = input("\ntype 'y' for another phrase, type anything else to stop. ")
    main()
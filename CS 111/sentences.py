"""
I didn't realize that it was supposed to make just six sentences

enjoy your 'almost' infinite random sentence generator
"""

# here I define determiners(single and plural), nouns(single and plural), and verbs(single, plural, past, present, future)
determiners_plural_list = ["many", "some","a group of","those", "few","several","various","numerous","multiple","a lot of","thousands of", "both the"]
determiners_single_list = ["every","another","one","a","this","that","each","the"]
nouns_single_list = ["robot", "engine","river","clown","reflection","lantern","person","man","woman","child","boy","girl","dog","cat","bat","bug","giraffe","tiger","mokey","fish"]
nouns_plural_list = ["robots","engines","rivers","clowns", "reflections","lanterns","people","men","women","children","boys","girls","dogs","cats","bats","bugs","giraffes","tigers","monkeys","fish"]
verbs_plural_prsnt_future = ["eat","go","run","talk","laugh","jump","speak","write","read","think","sleep","fly","cook","study","cry","sing","grow","watch"]
verb_single_prsnt = ["eats","goes","runs","talks","laughs","jumps","speaks","writes","reads","thinks","sleeps","flies","cooks","studies","cries","sings","grows","watches"]
verb_past = ["ate","went","ran","talked","laughed","jumped","spoke","wrote","read","thought","slept","flew","cooked","studied","cried","sang","grew","watched"]
prepositions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
import random

# main will decide if phrase will be plural, in the past present or furture tense, in the phrase is positive or negative
def main():
    plural = bool(random.randint(0,1))
    tense = random.randint(0,2)
    negative = random.randint(0,1)

    make_sentence(plural, tense, negative)

#see if single or plural and get corresponding determiner
def get_determiner(single_plural):
    if single_plural == True:
        return random.choice(determiners_plural_list)
    else:
        return random.choice(determiners_single_list)

#see if single or plural and get corresponding noun
def get_noun(single_plural):
    if single_plural == True:
        return random.choice(nouns_plural_list)
    else:
        return random.choice(nouns_single_list)

#get random verb
def get_verb(single_plural, past_prsnt_ftr, pstv_ngtv):
    verb =""
    #first layer checks which tense the phrase will be in
    if past_prsnt_ftr == 0:
        if pstv_ngtv == 0:                                                  #if past tense check if is positive or negative
            verb = random.choice(verb_past)                                     #positive past tense takes from simple past verbs
        else:
            verb = "did not " + random.choice(verbs_plural_prsnt_future)        #negative past will add to phrase and take form plural verbs
    elif past_prsnt_ftr == 1:                                               #if present, check if single or plural
        if single_plural==1:
            if pstv_ngtv == 0:
                verb = random.choice(verbs_plural_prsnt_future)                 #if plural and positive take from plural present verbs
            else:
                verb = "do not " + random.choice(verbs_plural_prsnt_future)     #if negative and pural, add 'do not' and take from plural present
        else:
            if pstv_ngtv == 0:
                verb = random.choice(verb_single_prsnt)                         #if single positve, take from single present verbs
            else: 
                verb = "does not " + random.choice(verbs_plural_prsnt_future)   #if single negative, add take from plural present verbs
    else:                                                                   #if future tense, check positive or negative
        if pstv_ngtv == 0:
            verb = "will " + random.choice(verbs_plural_prsnt_future)           # if positive add 'will' and take future verb
        else:
            verb = "will not " + random.choice(verbs_plural_prsnt_future)       # if negative, 'will not' and future verb
    return verb
    
# make_sentence inputs conditions and combines into one sentence
def make_sentence(plural, past_prsnt_ftr, ngtv):
    sentence =  "\n" + get_determiner(plural).capitalize() + " " + get_noun(plural) + " " + get_verb(plural, past_prsnt_ftr, ngtv) + " " + get_prepositional_phrase(plural) + "."
    print(f"{sentence}")

#get a random preposition
def get_preposition():
    preposition = random.choice(prepositions)
    return preposition

#creates prepositional phrase in correct tense
def get_prepositional_phrase(single_plural):
    if single_plural == True:
        prepositinal_phrase = get_preposition() +" "+ get_determiner(single_plural) +" "+ get_noun(single_plural)
        return prepositinal_phrase
    else:
        prepositinal_phrase = get_preposition() +" "+ get_determiner(single_plural) +" "+ get_noun(single_plural)
        return prepositinal_phrase

input("Click enter to generate a random sentence. ")        #start condition

main()

#can keep generating until done
more = "y"
while more == "y" or more == "Y":
    more = input("\ntype 'y' for another phrase, type anything else to stop. ")
    main()
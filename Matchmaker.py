
def ask_question(text, q_type="scale", options=["little", "lots"]):
    """Ask question - shows a (multiple choice) question and returns the answer.
    
    - q_type: "scale" = range of values for a scale / rank, 1 to 100
    - q_type: "bool" = Yes / No question, Boolean true / false value
    - q_type: "choose" = select an option from numbered statements (e.g. actions taken)
    - options (list items): the descriptions for "choose" statement options,
    which go after a number), or text for the start and end points of the range
    in q_type: "scale" - e.g. to show the question "...? (1=little, 100=lots)".
    """
    pass #...[remove this line after adding the function code here]...

# All the boolean variables that were here have been moved to key:value pairs
# in this dictionary and use of them updated to this using find and replace.
# Spelling and grammar errors have been corrected in Grammarly editor.
you = {"perception":50, "understanding":False, "patient":False, "impatient":False,
    "cannot_relate":False, "picky_friend":False, "gullible":False, "crowd_follower":False,
    "drone":False, "stable":False, "haphazard":False, "unstable":False, "emotionless":False,
    "loyal":False, "reliable":False, "cool_one":False, "hurtful":False, "caringness":False,
    "privacy":False, "robot":False, "no_morals":False, "regret":False, "outburst":False,
    "light_humor":False, "dark_humor":False, "sense_of_humor":False, "no_humor":False,
    "dark":False, "hurtful_humor":False, "haphazard_hero":False, "emotional_struggle":False}
# Help with dictionary variables: https://docs.python.org/3.5/tutorial/datastructures.html#dictionaries

#=== Start of main program ===#

print("Welcome to the people matcher, this program intends to match people\n"+
    "with their ideal partner. Though a pinch of salt may be required.")
print("This program will ask you questions about yourself. Finally making "+
    "suggestions as to the type of person that you would most likely be interested in")

print("On a scale of 0 (introverted) to 100 (extroverted) where would you rank yourself?")
introversion=input()
print("Given the choice, how many people would you meet and have as your friends?\n"+
      " (1) I would go for lots of people and try all of them.\n"+
      " (2) I would go for lots of people and have only the best as friends.\n"+
      " (3) I would go for few people and have a few friends.\n"+
      " (4) Rather go without meeting people or friends.")
depth=input()
if depth == "1":
    depth=33
elif depth == "2":
    depth=66
elif depth == "3":
    depth=99
elif depth == "4":
    depth=0
    
print("How good would you say your friends are to you? 100=terrible, 1=Wonderful")
# Inverse scale used to normal expectations of "how good". 1=worst, 100=best
tolerance=int(input())
depth=depth+(50-tolerance)/2
print("Are you a messy person? (Y/N)")
mess=input()
if mess == "Y":
    organisation=25
    print("Do you mind others' who are untidy? (Y/N)")
    spicy=input()
    if spicy == "Y":
        tolerance-10
    elif spicy == "N":
        tolerance+10
elif mess=="N":
    organisation=75
    print("Do you mind others' messiness/not being organised? (Y/N)")
    spicy=input()
    if spicy == "Y":
        tolerance-10
    elif spicy == "N":
        tolerance+10

print("How much do you care about others' affairs? (1=little, 100=lots)")
you["caringness"]=int(input())
print("How much do you care about the emotions of your friends? (1=little, 100=lots)")
you["caringness"]=(you["caringness"]+int(input()))/2

print("When a friend is sad, which action do you take?")
print(" (1) I don't ask them about their issues - they can deal with it.")
print(" (2) I stay out of their way, wondering what is wrong.")
print(" (3) I already know the problem, based on the way they are acting.")
print(" (4) Ask them what is wrong.")
response=input()
if response == "1":
    you["caringness"]=you["caringness"]/2
elif response == "2":
    tolerance=tolerance/2
elif response == "3":
    you["perception"]+25
elif response == "4":
    you["caringness"]=you["caringness"]+(100-you["caringness"])/2

print("How well do you get on with your teachers? (1=terribly, 100=brilliantly)")
respect=int(input())
tolerance=(tolerance-50)+respect
print("Do you post your opinions on social media? (Y/N)")
media=input()
if media == "Y":
    depth=depth/2
elif media == "N":
    depth=depth+(100-depth)/2
print("Do you swear? (Y/N)")
swear=input()
if swear == "Y":
    respect=respect/2
elif swear == "N":
    respect=respect+(100-respect)/2

print("Do you often notice when others are sad or not themselves? (Y/N)")
insightful=input()
if insightful == "Y":
    you["perception"]=you["perception"]+(100-you["perception"])/2
    print("Do you wonder why they are like that? (Y/N)")
    longing=input()
    if longing == "Y":
        you["caringness"]=you["caringness"]+(100-you["caringness"])/2
    elif longing == "N":
        you["caringness"]-you["caringness"]/2
elif insightful == "N":
    you["perception"]=you["perception"]/2
    print("Do you want to be able to tell? (Y/N)")
    longing=input()
    if longing == "Y":
        you["caringness"]=you["caringness"]+(100-you["caringness"])/2
    elif longing == "N":
        you["caringness"]=you["caringness"]/2
print("Do you often get into trouble for having not done things? (Y/N)")
plan=input()
if plan == "Y":
    organisation=organisation/2
elif plan == "N":
    orgainisation=organisation+(100-organisation)/2

print("You understand how you feel and why you feel the way you do? (1=not at all, 100=completely)")
self_understanding=int(input())
print("You often reflect on things that have happened in the day\n"+
    "and on your feelings before going to sleep at night? (Y/N)")
response=input()
if response == "Y":
    self_understanding=self_understanding+(100-self_understanding)/2
elif response == "N":
    self_understanding=self_understanding/2
print("Do you talk to others about how you are feeling? (Y/N)")
response=input()
if response == "Y":
    you["privacy"]=False
    self_understanding=self_understanding+(100-self_understanding)/2
elif response == "N":
    you["privacy"]=True
    self_understanding=self_understanding/2
print("Do you ever suddenly consider that you could've hurt\n"+
    "someone's feelings and feel slightly ashamed? (Y/N)")
you["regret"]=input()
if you["regret"] == "Y":
    you["regret"]=True
    you["perception"]=you["perception"]+(100-you["perception"])/2
    you["caringness"]=you["caringness"]+(100-you["caringness"])/2
elif you["regret"] == "N":
    you["regret"]=False
    you["perception"]=you["perception"]/2
    you["caringness"]=you["caringness"]/2
print("Do you suffer from emotional outbursts? (Y/N)")
response=input()
if response == "Y":
    tolerance=tolerance/2
    self_understanding=self_understanding/2
    
elif response == "N":
    tolerance=tolerance+(100-tolerance)/2
    self_understanding=self_understanding+(100-self_understanding)/2

print("How effective are your jokes, according to you? (1=terrible, 100=perfect)")
humor=int(input())
print("A friend cracks a bit of tasteful, but hurtful banter to one of your other friends, what do you do?")
print("1.Laugh, you just can't help it, it is too damn funny.")
print("2.Laugh internally, since your not quite sure how the recipent feels about it.")
print("3.You usually don't get the joke till the moment has passed.")
print("4.You don't really find hurtful jokes funny.")
response=input()
if response == "1":
    humor=humor+(100-humor)/2
    you["caringness"]=you["caringness"]/2
elif response == "2":
    humor=humor+(100-humor)/2
    you["caringness"]=you["caringness"]+(100-you["caringness"])/2
elif response == "3":
    humor=humor/2
elif response == "4":
    you["caringness"]=you["caringness"]+(100-you["caringness"])/2
print("I often tell jokes. (Y/N)")
responce=input()
if responce == "Y":
    humor=humor+(100-humor)/2
elif responce == "N":
    humor=humor/2
print("But I don't take part in the slightly hurtful banter\n"+
    "so that I don't hurt peoples' feelings? (Y/N)")
responce=input()
if responce == "Y":
    you["caringness"]=you["caringness"]+(100-you["caringness"])/2
elif responce == "N":
    you["caringness"]=you["caringness"]/2
print("How do you like your humor? (1=dark, 100=light-hearted)")
darkness=int(input())
print("Are you sarcastic often? (Y/N)")
responce=input()
if responce == "Y":
    darkness=darkness+(darkness-100)/2
    humor=humor+(100-humor)/2
elif responce == "N":
    humor=humor/2
    darkness=darkness/2

print("Do you know what it is that you would like to do,\n"+
    "for employment when you leave school? (Y/N)")
responce=input()
if responce == "Y":
    self_understanding=self_understanding+(100-self_understanding)/2
elif responce == "N":
    self_understanding=self_understanding/2
print("Do you know what your best friend wants to do when they leave school? (Y/N)")
responce=input()
if responce == "Y":
    depth=depth+(100-depth)/2
elif responce == "N":
    depth=depth/2
print("Do your friends talk to you about how they feel? (Y/N)")
responce=input()
if responce == "Y":
    depth=depth+(100-depth)/2
elif responce == "N":
    depth=depth/2


print(depth,tolerance,you["caringness"],respect,you["perception"],organisation,self_understanding,humor)
print("Depth,tolerance,caringness,respect,perception,organisation,self understanding,humor")

print("--------------------------------------")
print("--------------------------------------")
if tolerance>=50 and you["perception"]>=50:
    you["understanding"]=True
elif tolerance>50 and you["perception"]<50:
    you["patient"]=True
elif tolerance<50 and you["perception"]>50:
    you["impatient"]=True
elif tolerance<50 and you["perception"]<50:
    you["cannot_relate"]=True

if depth>=50 and you["perception"]>=50:
    you["picky_friend"]=True
elif depth>50 and you["perception"]<50:
    you["gullible"]=True
elif depth<50 and you["perception"]>50:
    you["crowd_follower"]=True    
elif depth<50 and you["perception"]<50:
    you["drone"]=True

if respect>=50 and self_understanding>=50:
    you["stable"]=True
elif respect<50 and self_understanding>50:
    you["haphazard"]=True
elif respect>50 and self_understanding<50:
    you["robot"]=True
elif respect<50 and self_understanding<50:
    you["unstable"]=True

if humor>=50 and darkness>=50:
    you["dark_humor"]=True
elif humor<50 and darkness>50:
    you["dark"]=True
elif humor>50 and darkness<50:
    you["light_humor"]=True
elif humor<50 and darkness<50:
    you["no_humor"]=True

if you["patient"]==True and you["robot"]==True:
    you["emotionless"]=True

if you["impatient"]==True and you["robot"]==True:
    you["emotional_struggle"]=True

if you["understanding"]==True and you["picky_friend"]==True:
    you["loyal"]=True

if you["stable"]==True and you["picky_friend"]==True:
    you["reliable"]=True

if you["impatient"]==True and you["haphazard"]==True:
    you["haphazard_hero"]=True

if you["stable"]==True and you["gullible"]==True:
    you["cool_one"]=True

if you["unstable"]==True and you["cannot_relate"]==True:
    you["hurtful"]=True

if you["unstable"]==True and you["impatient"]==True:
    you["outburst"]=True

if you["drone"]==True and you["unstable"]==True:
    you["no_morals"]=True

if you["hurtful"]==True or you["no_morals"]==True:
    negative=True

if you["dark"]==True and you["perception"]<50:
    you["hurtful_humor"]=True

if you["dark_humor"]==True and you["perception"]<50:
    you["hurtful_humor"]=True

if you["light_humor"]==True or you["dark_humor"]==True:
    you["sense_of_humor"]=True

if you["caringness"]>50:
    you["caringness"]=True


print("Your understanding and way you feel about people is best described as this...")

if you["understanding"]==True:
    print("You understand people and because of this you are very patient with people that you know have reasons to act the way that they should.")
elif you["patient"]==True:
    print("You don’t always understand why people do the things that they do, nevertheless you do not get angry with them rather you try to understand why they are acting in such a way.")
elif you["impatient"]==True:
    print("You usually understand why people do the things that they do, or usually have an inkling as to why. Yet you do not let them get away with it, you make sure that you tell them that they have done wrongdoings.")
elif you["cannot_relate"]==True:
    print("You struggle to understand people’s motives especially when they do mean or unexpected things, you are easy to annoy if people don’t make it clear why they are acting the way they area and because of this you often get into arguments.")

print()
print("The way you value friendship is best described as this")

if you["picky_friend"]==True:
    print("When it comes to friends you are careful, you like to meet people and usually you can tell their intentions from a mile away. You still try to be friends with everyone but some people you just no are up to no good.")
elif you["gullible"]==True:
    print("When it comes to friends you do prefer loyalty however you sometimes find it hard to distinguish the good from the bad and due to this often feel as if you are taken advantage of.")
elif you["crowd_follower"]==True:
    print("When it comes to friends you are somewhat in the middle, you like having friends around due to the social status but also aren't just friends with anyone. You do have boundaries and people that you wouldn't befriend despite the popularity you may gain. You can also usually tell who the bad ones are.")
elif you["drone"]==True:
    print("When it comes to friends you prefer the social status of the people themselves, you’re not too picky and will happily befriend an irritating person (well one that’s not too bad) as long as you are able to gain something from them such as status.")

print()
print("Your general attitude is best described as this")

if you["stable"]==True:
    print("You respect authority and try not to break rules often. You really understand yourself meaning that people often see you as a very stable, righteous person.")
elif you["haphazard"]==True:
    print("You’re in touch with your emotions, and know right from wrong. However, when pointless rules are enforced by pointless figureheads you often find yourself arguing with or breaking the rules. This does sometimes win you a cheer but sometimes a tut.")
elif you["robot"]== True:
    print("You follow the rules pretty much all the time but not because you want to more the fact that you don't really have a better alternative and don't really know what else you would do.")
elif you["unstable"]==True:
    print("You don’t understand the rules and also do not distinguish right from wrong as much as others, also you don't care much for the rules you might not necessarily go out of your way to break them but you don't like their existence.")

print()
print()
print("Overall, however, this is the sort of personality you behold")
    
if you["emotionless"]==True:
    print("You have trouble understanding emotions sometimes. You can't read people too well sometimes surprised by peoples cruelness, but you struggle to understand yourself even more so. You might find some calm in trying to understand others' emotions or the world around you. To others' you seem perhaps withdrawn sometimes, but in reality you are just trying to understand things sometimes the people around you and sometimes yourself. Nevertheless, you try not to get angry with people, you don't always understand them, but you usually don't snap. Usually...")
    if you["sense_of_humor"]==False:
        print("This is especially notable when you have trouble telling and receiving jokes, sometimes you don't quite get them, but that's ok.")
if you["emotional_struggle"]==True and you["caringness"]<50:
    print("You have trouble understanding emotions sometimes. Both your own and the peoples' around you. Though you do have a better understanding of others Sometimes this can seem a grace, since you don't often find yourself caught in the issues that surround you. However, sometimes it seems the issues find you since you don't like it when people are not nice you tend not to have a very long fuse when things like this happen, you let them know what it is that you think of them. Sometimes this can be good, but other times you upset the person. Whether or not they deserved it is up for debate, I'm only a program after all")
    if you["regret"]==True:
        print("Sometimes you feel that you take things too far, but can't help yourself since people can be some damn mean at times. You sometimes wonder if you are the mean one...Stay true to what you believe and surely you will not be anything but moral")
if you["emotional_struggle"]==True and you["caringness"]>50:
    print("You have trouble understanding emotions sometimes both your own and those of the people around you, though you do have a better understanding of others, however unlike many that share your traits you care having a large sympathy for people. Which causes some real moral dilemmas at times. Most of the time you find yourself bitting your tongue when people start being mean to you, you mostly shut it out as the rage boils silently inside of you, not speaking out for fear of being the bad person yourself. Only when others are the victim do you find yourself unable not to speak out, usually telling the bully what for. Meanness you can take it, but when others are the victim you won't stand by simply watching.")
    if you["regret"]==True:
        print("This doesn't mean you feel no sympathy for the bullies though, no, sometimes you try to understand why they do the things they do and wonder if you are too mean during your counter attacks...Still, you don't doubt that you needed to do something.")
if you["loyal"]==True:
    print("You are the one that everyone one says is a good friend. Though you might not always actually believe it yourself. You like to keep your friendship group quite small but to those friends, you are a great listener and feel the things that they do. You try to help them and be a good person. Even sometimes forgetting yourself along the way.")
    if you["sense_of_humor"]==True:
        print("You also can usually also crack good jokes, though not always the funniest you jokes are unlikely to hurt peoples' feelings since you think about the effects beforehand")
        
if you["reliable"]==True:
    print("You are the rock of the group. No not Dwayne “the rock” Johnson, but the one that your friends rely on in a bad situation, you are usually in control of your mood and because of this people believe that you are the one to go to when they are not. Sometimes you might feel tired of helping others, but other times you enjoy it.")
    if you["sense_of_humor"]==True:
        print("You can usually crack a joke to get your friends back smiling again since you seem to be naturally quite good at being able to judge the hurtfulness of your humour but occasionally you do mess up with it.")
if you["cool_one"]==True:
    print("You are the cool and calm one in a relatively big group of friends, you don’t know all of them that well, but the ones they know you best see you as a person that could walk through anything and not skip a beat. Though secretly sometimes you panic you don’t often let it show and people love you for this.")
if you["haphazard_hero"]==True:
    print("You know what's right and wrong, however while your morals are solid your emotions are not as well grounded, they are unstable and fluctuate, it isn't uncommon for you to suffer from mood swings however you differ from more hurtful people because you know right from wrong, you do not hurt people that are nice, but the people that deserve it, you rarely hold back.")

if you["hurtful"]==True:
    print("You may come across as unintentionally hurtful at times. This isn't so much that you want to hurt peoples' feelings, just that people's reactions are hard for you to gauge, your moral compass might be a bit skewed at times but you try to be civil with most that are to you, unless they are enforcing the rules, then it's their fault.")
    if you["hurtful_humor"]==True:
        print("This may be partially attributed to your humor since you seem to be the sort that may accidentally hurt someone's feelings with an ill-judged joke, or finding hurtful things funny.")    
if you["outburst"]==True:
    print("You seem to have quite a short fuse and also have trouble differentiating right from wrong. Because of this when people test your patience it isn't unknown for you to have angry outbursts at people.")
if you["no_morals"]==True:
    print("As much as I hate to say it, it looks as if your morality may be a bit lacking, it is likely that you mostly use people, not understanding the reasons why this is wrong. It most likely isn't unheard of for you to have outbursts at people that threaten your social standing or to kick others down for your own gain.") 
    if you["hurtful_humor"]==True:
        print("This may be partially due to your more dark sense of humour, which others might find disconcerting at times, or even hurtful when you misjudge what is funny.")
if you["outburst"]==True and you["regret"]==True and you["hurtful"]==False:
    print("But despite the fact that sometimes you can be driven to say hurtful things you yourself an not mean. Your actions play on your mind and you do regret it when your temper makes you go too far")
if you["hurtful"]==True and you["regret"]==True and you["outburst"]==False:
    print("But despite the fact that you struggle to understand what it is that you do that others find upsetting, you still regret the upset that you cause. You strive not to hurt people, but always find that you do")
if you["hurtful"]==True and you["regret"]==True and you["outburst"]==True:
    print("You really hurt people sometimes your tendency to lose your temper along with the fact that you don't always know what exactly it is that you have said to cause upset is sometimes to you the most upsetting thing of all. You try not to upset people, but find that you sometimes do, you can't help it and that's what hurts the most.")

print()
if you["caringness"]==True:
    print("In addition to or perhaps contrasting your overall personality")
    print("You are sympathetic even empathetic at times, other peoples' pain really gets to you. You want to help people with their problems and it infuriates you when you can’t")
if you["privacy"]==True:
    print("In addition to or perhaps contrasting your overall personality you are also...")
    print("Quite a secretive person, you keep things from others, some things even from your friends. Not always out of spite simply because you don’t quite trust everyone with your deepest darkest secrets.")

input()

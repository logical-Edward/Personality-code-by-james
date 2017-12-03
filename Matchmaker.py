# All the individual boolean variables at the start have been moved to key:value pairs in a dictionary.
you = {"perception":50, "understanding":False, "pacient":False, "impacient":False, "cant_relate":False,
       "picky_friend":False, "gulible":False, "crowd_follower":False, "gulible":False, "haphazrd":False,
       "drone":False, "stable":False, "haphazard":False, "unstable":False, "emotionless":False, "loyal":False,
       "reliable":False, "cool_one":False, "hurtful":False, "caringness":False, "privacy":False, "robot":False,
       "no_morals":False, "regret":False, "outburst":False, "light_humor":False, "dark_humor":False,
       "sense_of_humor":False, "no_humor":False, "dark":False, "hurtful_humor":False, "haphazard_hero":False,
       "emotional_struggle":False}
# Help with dictionary variables: https://docs.python.org/3.5/tutorial/datastructures.html#dictionaries
# you["robot"] = value

perception=50

understanding=False
pacient=False
impacient=False
cant_relate=False
picky_friend=False
gulible=False
crowd_follower=False
gulible=False
haphazrd=False
drone=False
stable=False
haphazard=False
unstable=False
emotionless=False
loyal=False
reliable=False
cool_one=False
hurtful=False
caringness=False
privacy=False
robot=False
no_morals=False
regret=False
outburst=False
light_humor=False
dark_humor=False
sense_of_humor=False
no_humor=False
dark=False
hurtful_humor=False
haphazard_hero=False
emotional_struggle=False

#=== Start of main program - after module import, function creating and option variables. ===

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
caringness=int(input())
print("How much do you care about the emotions of your friends? (1=little, 100=lots)")
caringness=(caringness+int(input()))/2

print("When a friend is sad, which action do you take?")
print(" (1) I don't ask them about their issues - they can deal with it.")
print(" (2) I stay out of their way, wondering what is wrong.")
print(" (3) I already know the problem, based on the the way they act.")
print(" (4) Ask them what is wrong.")
response=input()
if response == "1":
    caringness=caringness/2
elif response == "2":
    tolerance=tolerance/2
elif response == "3":
    perception+25
elif response == "4":
    caringness=caringness+(100-caringness)/2

print("How well do you get on with your teachers? 1==Terribly 100=Brilliantly")
respect=int(input())
tolerance=tolerance-50+respect
print("Do you post you opinions on soical media? Y/N")
media=input()
if media=="Y":
    depth=depth/2
elif media=="N":
    depth=depth+(100-depth)/2
print("Do you swear? Y/N")
swear=input()
if swear=="Y":
    respect=respect/2
elif swear=="N":
    respect=respect+(100-respect)/2
print("Do you notice when others are sad or not themeselves often? Y/N")
insightful=input()
if insightful=="Y":
    perception=perception+(100-perception)/2
    print("Do you wonder why they are like that? Y/N")
    longing=input()
    if longing=="Y":
        caringness=caringness+(100-caringness)/2
    elif longing=="N":
        caringness-caringness/2
elif insightful=="N":
    perception=perception/2
    print("Do you want to be able to be able to tell? Y/N")
    longing=input()
    if longing=="Y":
        caringness=caringness+(100-caringness)/2
    elif longing=="N":
        caringness=caringness/2
print("Do you often get into trouble for not having done things? Y/N")
plan=input()
if plan=="Y":
    organisation=organisation/2
elif plan=="N":
    orgainisation=organisation+(100-organisation)/2
print("You understand how you feel and why you feel the way you do. 1=Not at all  100=Completely")
self_understanding=int(input())
print("You often reflect on things that have happened in the day and on your feelings before going to sleep at night? Y/N")
response=input()
if response=="Y":
    self_understanding=self_understanding+(100-self_understanding)/2
elif response=="N":
    self_understanding=self_understanding/2
print("Do you talk to others about how you are feeling? Y/N")
response=input()
if response=="Y":
    privacy=False
    self_understanding=self_understanding+(100-self_understanding)/2
elif response=="N":
    privacy=True
    self_understanding=self_understanding/2
print("Do you ever suddenly consider that you could've hurt someones feelings and feel slighltly ashamed? Y/N")
regret=input()
if regret=="Y":
    regret=True
    perception=perception+(100-perception)/2
    caringness=caringness+(100-caringness)/2
elif regret=="N":
    regret=False
    perception=perception/2
    caringness=caringness/2
print("Do you suffer from emotional outbursts? Y/N")
responce=input()
if responce=="Y":
    tolerance=tolerance/2
    self_understanding=self_understanding/2
    
elif responce=="N":
    tolerance=tolerance+(100-tolerance)/2
    self_understanding=self_understanding+(100-self_understanding)/2
print("How effective are your jokes, according to you? 1=Terrible 100=Perfect")
humor=int(input())
print("A friend cracks a bit of tasteful, but hurtful banter to one of your other friends, what do you do?")
print("1.Laugh, you just can't help it, it is too damn funny.")
print("2.Laugh internally, since your not quite sure how the recipent feels about it.")
print("3.You usually don't get the joke till the moment has passed.")
print("4.You don't really find hurtful jokes funny.")
responce=input()
if responce=="1":
    humor=humor+(100-humor)/2
    caringness=caringness/2
elif responce=="2":
    humor=humor+(100-humor)/2
    caringness=caringness+(100-caringness)/2
elif responce=="3":
    humor=humor/2
elif responce=="4":
    caringness=caringness+(100-caringness)/2
print("I often tell jokes. Y/N")
responce=input()
if responce=="Y":
    humor=humor+(100-humor)/2
    print(" But I don't take part in the slightly hurtful banter so that I don't hurt peoples' feelings? Y/N")
    responce=input()
    if responce=="Y":
        caringness=caringness+(100-caringness)/2
    elif responce=="N":
        caringness=caringness/2
elif responce=="N":
    humor=humor/2
    print("I don't take part in the slightly hurtful banter so that I don't hurt peoples' feelings? Y/N")
    responce=input()
    if responce=="Y":
        caringness=caringness+(100-caringness)/2
    elif responce=="N":
        caringness=caringness/2
print("How do you like your humor? 1=Dark 100=Lighthearted")
darkness=int(input())
print("Are you sarcasitc often? Y/N")
responce=input()
if responce=="Y":
    darkness=darkness+(darkness-100)/2
    humor=humor+(100-humor)/2
elif responce=="N":
    humor=humor/2
    darkness=darkness/2
print("Do you know what it is that you would like to do, for employment when you leave school? Y/N")
responce=input()
if responce=="Y":
    self_understanding=self_understanding+(100-self_understanding)/2
elif responce=="N":
    self_understanding=self_understanding/2
print("Do you know what your best friend wants to do when they leave school? Y/N")
responce=input()
if responce=="Y":
    depth=depth+(100-depth)/2
elif responce=="N":
    depth=depth/2
print("Do your friends talk to you about how they feel? Y/N")
responce=input()
if responce=="Y":
    depth=depth+(100-depth)/2
elif responce=="N":
    depth=depth/2
    


        
        
    
    

print(depth,tolerance,caringness,respect,perception,organisation,self_understanding,humor)
print("Depth,tolerance,caringness,respect,perception,organisation,self understanding,humor")


print("--------------------------------------")
print("--------------------------------------")
if tolerance>=50 and perception>=50:
    understanding=True
elif tolerance>50 and perception<50:
    pacient=True
elif tolerance<50 and perception>50:
    impacient=True
elif tolerance<50 and perception<50:
    cant_relate=True

if depth>=50 and perception>=50:
    picky_friend=True
elif depth>50 and perception<50:
    gulible=True
elif depth<50 and perception>50:
    crowd_follower=True    
elif depth<50 and perception<50:
    drone=True

if respect>=50 and self_understanding>=50:
    stable=True
elif respect<50 and self_understanding>50:
    haphazard=True
elif respect>50 and self_understanding<50:
    robot=True
elif respect<50 and self_understanding<50:
    unstable=True

if humor>=50 and darkness>=50:
    dark_humor=True
elif humor<50 and darkness>50:
    dark=True
elif humor>50 and darkness<50:
    light_humor=True
elif humor<50 and darkness<50:
    no_humor=True


if pacient==True and robot==True:
    emotionless=True

if impacient==True and robot==True:
    emotional_struggle=True

if understanding==True and picky_friend==True:
    loyal=True

if stable==True and picky_friend==True:
    reliable=True

if impacient==True and haphazard==True:
    haphazard_hero=True

if stable==True and gulible==True:
    cool_one=True

if unstable==True and cant_relate==True:
    hurtful=True

if unstable==True and impacient==True:
    outburst=True

if drone==True and unstable==True:
    no_morals=True

if hurtful==True or no_morals==True:
    negative=True

if dark==True and perception<50:
    hurtful_humor=True

if dark_humor==True and perception<50:
    hurtful_humor=True

if light_humor==True or dark_humor==True:
    sense_of_humor=True

if caringness>50:
    caringness=True

print("Your understanding and way you feel about people is best described as this...")


if understanding==True:
    print("You understand people and because of this you are very patient with people that you know have reasons to act the way that they should.")
elif pacient==True:
    print("You don’t always understand why people do the things that they do, nevertheless you do not get angry with them rather you try to understand why they are acting in such a way.")
elif impacient==True:
    print("You usually understand why people do the things that they do, or usually have an inkling as to why. Yet you do not let them get away with it, you make sure that you tell them that they have done wrongdoings.")
elif cant_relate==True:
    print("You struggle to understand people’s motives especially when they do mean or unexpected things, you are easy to annoy if people don’t make it clear why they are acting the way they area and because of this you often get into arguments.")

print()
print("The way you value friendship is best described as this")

if picky_friend==True:
    print("When it comes to friends you are careful, you like to meet people and usually you can tell their intentions from a mile away. You still try to be friends with everyone but some people you just no are up to no good.")
elif gulible==True:
    print("When it comes to friends you do prefer loyalty however you sometimes find it hard to distinguish the good from the bad and due to this often feel as if you are taken advantage of.")
elif crowd_follower==True:
    print("When it comes to friends you are somewhat in the middle, you like having friends around due to the social status, but also aren't just friends with anyone. You do have boundaries and people that you wouldn't befriend despite the popularity you may gain. You can also usually tell who the bad ones are.")
elif drone==True:
    print("When it comes to friends you prefer the social status of the people themselves, you’re not too picky and will happily befriend an irritating person (well one that’s not too bad) as long as you are able to gain something from them such as status.")
print()
print("Your general attitude is best described as this")

if stable==True:
    print("You respect authority and try not to break rules often. You really understand yourself meaning that people often see you as a very stable, righteous person.")
elif haphazard==True:
    print("You’re in touch with your emotions, and know right from wrong. However when pointless rules are enforced by pointless figureheads you often find yourself arguing with or breaking the rules. This does sometimes win you a cheer but sometimes a tut.")
elif robot== True:
    print("You follow the rules pretty much all the time but not because you want to more the fact that you dont really have a better alternative and don't really know what else you would do.")
elif unstable==True:
    print("You don’t understand the rules and also do not distinguish right from wrong as much as others, also you don't care much for the rules you might not nessicarily go out of your way to break them but you don't like their exisitance.")

print()
print()

print ("Overall however this is the sort of personality you behold")
    
if emotionless==True:
    print("You have trouble understanding emotions sometimes. You can't read people too well sometimes supirsed by peoples cruelness, but you struggle to understand yourself even more so. You might find some calm in trying to understand others' emotions or the world around you. To others' you seem perhaps withdrawn sometimes, but in reality you are just trying to understand things sometimes the people around you and sometimes yourself. Nevertheless you try not to get angry with people, you don't always understand them, but you usualy don't snap. Usually...")
    if sense_of_humor==False:
        print("This is espeailly notable when you have trouble telling and reciving jokes, sometimes you don't quite get them, but thats ok.")
if emotional_struggle==True and caringness<50:
    print("You have trouble understanding emotions sometimes. Both your own and the peoples' around you. Though you do have a better understanding of others Sometimes this can seem a grace, since you dont often find yourself caught in the issues that surrond you. However sometimes it seems the issues find you, since you don't like it when people are not nice you tend not to have a very long fuse when things like this happen, you let them know what it is that you think of them. Sometimes this can be good, but othertimes you upset the person. Whether or not they deserved it is up for debate, im only a program after all")
    if regret==True:
        print("Sometimes you feel that you take things too far, but can't help yourself since people can be some damn mean at times. You sometimes wonder if you are the mean one...Stay true to what you belive and surely you will not be anything but moral")
if emotional_struggle==True and caringness>50:
    print("You have trouble understading emotions sometimes both your own and those of the people around you, though you do have a better understanding of others, however unlike many that share your traits you care having a large sympathy for people. Which causes some real moral dilemas at times. Most of the time you find yourself bitting your tongue when people start being mean to you, you mostly shut it out as the rage boils silently inside of you, not speaking out for fear of being the bad person yourself. Only when others are the victim do you find yourself unable not to speak out, usually telling the bully what for. Meaness you can take it, but when others are the vicitm you wont stand by simply watching.")
    if regret==True:
        print("This doesnt mean you feel no sympathy for the bullies though, no, sometimes you try to understand why they do the things they do and wonder if you are too mean during you counter attacks...Still you dont doubt that you needed to do something.")
if loyal==True:
    print("You are the one that everyone one says is a good friend. Though you might not always actually believe it yourself. You like to keep your friendship group quite small but to those friends you are a great listener and feel the things that they do. You try to help them, and be a good person. Even sometimes forgetting yourself along the way.")
    if sense_of_humor==True:
        print("You also can usually also crack good jokes, though not always the funniest you jokes are unlikely to hurt peoples' feelings since you think about the effects before hand")
        
if reliable==True:
    print("You are the rock of the group. No not Dwayne “the rock” Johnson, but the one that your friends rely on in a bad situation, you are usually in control of your mood and because of this people believe that you are the one to go to when they are not. Sometimes you might feel tired of helping others, but other times you enjoy it.")
    if sense_of_humor==True:
        print("You can usually crack a joke to get your freinds back similing again, since you seem to be natually quite good at being able to judge the hurtfulness of your humor but occasinally you do mess up with it.")
if cool_one==True:
    print("You are the cool and calm one in a relatively big group of friends, you don’t know all of them that well, but the ones the know you best see you as a person that could walk through anything and not skip a beat. Though secretly sometimes you panic you don’t often let it show and people love you for this.")
if haphazard_hero==True:
    print("You know what's right and wrong, however while your morals are solid your emotions are not as well grounded, they are unstable and fluctuate, it isn't uncommon for you to suffer from mood swings however you differ from more hurtful people because you know right from wrong, you do not hurt people that are nice, but the people that deserve it, you rarely hold back.")

if hurtful==True:
    print("You may come across as unitentionally hurtful at times. This isn't so much that you want to hurt peoples' feelings, just that people's reactions are hard for you to gauge, your moral compass might be a bit skewed at times but you try to be civil with most that are to you, unless they are enforcing the rules, then it's their fault.")
    if hurtful_humor==True:
        print("This may be partially attributed to your humor, since you seem to be the sort that may accientally hurt someones feelings with an i'll jugded joke, or finding hurtful things funny.")    
if outburst==True:
    print("You seem to have quite a short fuse and also have trouble differencating right from wrong. Because of this when people test your pacience it isn't unknown for you to have angry outbursts at people.")
if no_morals==True:
    print("As much as I hate to say it, it looks as if your morality may be a bit lacking, it is likely that you mosty use people, not understanding the reasons why this is wrong. It most likley isn't unheard of for you to have outbursts at people that threaten your social standing or to kick others down for your own gain.") 
    if hurtful_humor==True:
        print("This may be partially due to your more dark sense of humor, which others might find disconserting at times, or even hurtful when you misjudge what is funny.")
if outburst==True and regret==True and hurtful==False:
    print("But despite the fact that sometimes you can be driven to say hurtful things you yourself an not mean. Your actions play on your mind and you do regret it when your temper makes you go too far")
if hurtful==True and regret==True and outburst==False:
    print("But despite the fact that you struggle to understand what it is that you do that others find upsetting, you still regret the upset that you cause. You strive not to hurt people, but always find that you do")
if hurtful==True and regret==True and outburst==True:
    print("You really hurt people sometimes your tendency to lose your temper along with the fact that you don't always know what exactly it is that you have said to cause upset is sometimes to you the most upsetting thing of all. You try not to upset people, but find that you sometimes do, you can't help it and that's what hurts the most.")



print()
if caringness==True:
    print("In addition to or perhaps contrasting your overall personality")
    print("You are sympathic even empathetic at times, other peoples pain really gets to you. You want to help people with their problems and it infuriates you when you can’t")
if privacy==True:
    print("In addition to or perhaps contrasting your overall personality you are also...")
    print("Quite a secretive person, you keep things from others, somethings even from your friends. Not always out of spite simply because you don’t quite trust everyone with your deepest darkest secrets.")
    
    






input()




    


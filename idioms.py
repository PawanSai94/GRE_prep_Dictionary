import random
import time
prompt = "   >"
recollect = {}
d1 = {
'to eat humble pie': 'admit to defeat' ,
'a pig in a poke': 'a poor purchase' ,
'a flash in the pan': 'a star today a flop tomorrow' ,
'to pour oil on troubled waters': 'to try to make peace' ,

'the sword of Damocles': 'any threating danger' ,
'Pyrrhic victory': 'an expensive conquest' ,
'a wet blanket': 'spoilsport' ,
'to beard the lion': 'defy an opponent in his home' ,

'crocodile tears': 'hypocritical sympathy' ,
'to carry the day': 'to win the honors' ,
'Skid Row': 'run down district' ,
'to go up in smoke': 'end fruitlessly' ,

'to throw down the gauntlet': 'to offer a challenge' ,
'feeling no pain': 'under the influence of alcohol' ,
'Hobsons choice': 'to have no say in the matter' ,
'to rule the roost': 'be the boss' ,

'stock in trade': 'the necessary equipment' ,
'to take down a peg': 'to humiliate' ,
'pass the buck': 'to refuse to take responsibility' ,
'to lionize a person': 'to idolize' ,

}

d2 = {

'Im from Missouri': 'I have to be convinced' ,
'red-letter day': 'occasion for rejoicing' ,
'let sleeping dogs lie': 'don’t rake up old grievances' ,
'thumbs down': 'to signal rejection' ,

'cause celebre': 'famous law case' ,
'one swallow doesnt make summer': 'dont jump to conclusions' ,
'bitter pill to swallow': 'a humiliating defeat' ,
'an ax to grind': 'having a selfish motive in background' ,

'sour grapes': 'claiming to despise what you cannot have' ,
'swap horses in midstream': 'to change ones mind' ,
'to cool ones heels': 'to be kept waiting' ,
'a red herring': 'a diversion' ,

'to spill the beans': 'give away a secret' ,
'stiff upper lip': 'courage in face of trouble' ,
'cold feet': 'hesitation because of fear' ,
'look a gift horse in mouth': 'to be critical of a present' ,

'to pay the piper': 'to bear the consequences' ,
'on the carpet': 'being scolded' ,
'to show ones hand': 'to reveal ones emotions' ,
'to tilt at windmills': 'fight imaginary enemies' ,

}

d3 = {

'to feather ones nest': 'provide for oneself at expense of others' ,
'fair-weather friends': 'unreliable acquaintances' ,
'to sow wild oats': 'to lead a wild life' ,
'windfall': 'unexpected financial gain' ,

'wear ones heart on ones sleeve': 'make ones feelings evident' ,
'wash dirty linen in public': 'openly discuss private affairs' ,
'save face': 'to avoid disgrace' ,
'Indian summer': 'warm autumn weather' ,

'take the bull by the horns': 'to face a problem directly' ,
'the lions share': 'the major portion' ,
'out of the frying pan into the fire': 'from bad to worse' ,
'keep the pot boiling': 'to maintain interest' ,

'bury the hatchet': 'make peace' ,
'Philadelphia lawyer': 'outstandingly able' ,
'gild the lily': 'to praise extravagantly' ,
'steal ones thunder': 'to beat someone to the punch' ,

'woolgathering': 'absentmindedness' ,
'to whitewash': 'to conceal defects' ,
'break the ice': 'make a start' ,
'the grapevine': 'a means of spreading information' ,

}

d4 = {

'in a bee line': 'directly' ,
'the world the flesh and the devil': 'temptations' ,
'make bricks without straw': 'attempt something without necessary materials' ,
'have the upper hand': 'gain control' ,

'to draw in ones horns': 'to check ones anger' ,
'to put the cart before the horse': 'to do things backwards' ,
'to turn the tables': 'to turn the situation in ones favour' ,
'a chip off the old block': 'a son who is like his father' ,

'under the wire': 'just in time' ,
'to be at large': 'not confined or in jail' ,
'to go against the grain': 'to irritate' ,
'to wink at': 'to pretend not to see' ,

'to play possum': 'to try yo fool someone' ,
'its an ill wind that blows nobody good': 'someone usually benefits from another persons misfortune' ,
'to know the ropes': 'to be fully acquainted with the procedures' ,
'behind the eight ball': 'in trouble' ,

'left holding the bag': 'to be left to suffer the blame' ,
'a lick and a promise': 'to do something in hasty and superficial manner' ,
'tongue in cheek': 'insincerely' ,
'to take the wind out of ones sails': 'to remove someones advantage' ,

}

d5 = {

'two strings to ones bow': 'two means of achieveing ones aim' ,
'on tenter hooks': 'in a state of anxiety' ,
'the fat is in the fire': 'the mischief is done' ,
'like Caesars wife': 'above suspicion' ,

'plea bargain': 'to agree to plead guilty for lesser charge to avoid serious one' ,
'in apple pie order': 'in near order - good condition' ,
'apple polishing': 'trying to gain favor by gifts or flattery' ,
'the Draconian code': 'a very severe set of rules' ,

'the distaff side': 'women' ,
'on the qui vive': 'on the alert' ,
'to get ones back up': 'to become angry' ,
'to bring home the bacon': 'to earn a living - to succeed' ,

'to get down off a high horse': 'to act like an ordinary person' ,
'the first water': 'of the best quality - the greatest' ,
'dyed in the wool': 'set in ones ways' ,
'blue chip': 'a highly valuable asset' ,

'as broad as is it long': 'it makes very little difference' ,
'blow hot and cold': 'swing for and against something' ,
'in the doldrums': 'in a bored or depressed state' ,
'burn the midnight oil': 'study or work late into the night' ,

}

d6 = {

'to strike while the iron is hot': 'take action at the right moment' ,
'to split hairs': 'to make a fine decision' ,
'sleep on it': 'postpone a decision' ,
'once in a blue moon': 'on a very rare occasion' ,

'to break the ice': 'to make a beginning' ,
'loaded for bear': 'to be well prepared' ,
'to bring down the house': 'to cause great enthusiasm' ,
'to pull ones weight': 'to do a fair share of the work' ,

'a white elephant': 'a costly and useless possession' ,
'lock stock and barrel': 'entirely - completely' ,
'a feather in ones cap': 'something to be proud of' ,
'out on a limb': 'in a dangerous or exposed position' ,

'on the spur of the moment': 'on impulse - without thinking' ,
'a fly in the ointment': 'some small thing that spoils the enjoyment' ,
'to take French leave': 'to go away without permission' ,
'in the arms of Morpheus': 'asleep' ,

'forty winks': 'a short nap' ,
'from pillar to post': 'from one place to another' ,
'in the lap of the gods': 'out of ones own hands' ,
'Achilles heel': 'weak spot' ,

}

d7 = {

'cold shoulder': 'to disregard or ignore' ,
'without rhyme or reason': 'makes no sense' ,
'swan song': 'final or last' ,
'to get the sack': 'to be discharged or fired' ,

'ivory tower': 'isolated from life or lifes problems' ,
'to feather ones nest': 'to enrich oneself at every opportunity' ,
'the writing on the wall': 'an incident or event that shows what will happen in the future' ,
'on the bandwagon': 'joinging the majority - going along with the trend' ,

'to hit the nail on the head': 'to guess something correctly' ,
'on the dot': 'exactly on time' ,
'to take under ones wing': 'to become responsible for' ,
'out of ones depth': 'in a situation that is too difficult to handle' ,

'to take a leaf out of someones book': 'to imitate or follow the example' ,
'brass tacks': 'the real problem or situation' ,
'hook line and sinker': 'completely fall to a trick' ,
'lily livered': 'cowardly' ,

'to pull up stakes': 'to quit a place' ,
'to raise Cain': 'to cause trouble - make a fuss' ,
'to leave no stone unturned': 'to try ones best - to make every effort' ,
'tongue in ones cheek': 'not to be sincere' ,

'keep a stiff upper lip': 'keep up courage - stand up to trouble' ,
'to throw the book at someone': 'to give the maximum punishment' ,
'terra firma': 'solid - firm land' ,
'in seventh heaven': 'the highest happiness or delight' ,

}



def func():
	count=0
	items = list(block.items())  # List of tuples of (key,values)
	random.shuffle(items)
	for key, value in items:
	    print("\n   " + key)#, ":", value)
	    print ("\n   ?\n")
	    condition = input(prompt)
	    count=count+1
	    if condition=="y":
	    	recollect[key]=value
	    	print ("   " + value)
	    	print("\n")
	    	print ("The remaining idioms are: ",len(items)-count)
	    	time.sleep(1)
	#    	print (len(items))
	#   	print (count)
	#
	print ("\n    RECOLLECTING STARTS....")
	#for key in recollect:
	#    print("    ", key, ' : ', recollect[key])
	items = list(recollect.items())  # List of tuples of (key,values)
	random.shuffle(items)
	for key, value in items:
	    print("\n   " + key)#, ":", value)
	    print ("\n   ?\n")
	    condition = input(prompt)
	    if condition=="y":
	    	print ("   " + value)
	    	print("\n")
	    	time.sleep(1)
	    	
print (" Which block of idioms do you want to revise?\n    1\t    2\t    3\t    4\t    5\t    6\t    7\t")
num_block = input(prompt)
if num_block=='1':
	block=d1
	func()
	for keys,values in recollect.items():
		print (keys, " : ", values)
elif num_block=='2':
	block = d2
	func()
	for keys,values in recollect.items():
		print (keys, " : ", values)
elif num_block=='3':
	block=d3
	func()
	for keys,values in recollect.items():
		print (keys, " : ", values)	
elif num_block=='4':
	block=d4
	func()
	for keys,values in recollect.items():
		print (keys, " : ", values)
#		print(values)
elif num_block=='5':
	block=d5
	func()
	for keys,values in recollect.items():
		print (keys, " : ", values)
elif num_block=='6':
	block=d6
	func()
	for keys,values in recollect.items():
		print (keys, " : ", values)
elif num_block=='7':
	block=d7
	func()
	for keys,values in recollect.items():
		print (keys, " : ", values)
else:
	block=d1
	func()
	time.sleep(1)
	block=d2
	func()
	time.sleep(1)
	block=d3
	func()
	time.sleep(1)
	block=d4
	func()
	time.sleep(1)
	block=d5
	func()
	block=d6
	func()
	time.sleep(1)
	block=d7
	func()
	time.sleep(1)
#	print (block)

import random
import time
prompt = "   >"
recollect = {}
d1 = {
	'voracious': 'desiring huge amount' ,
'indiscriminate': 'carelessly chosen' ,
'steeped': 'to be completely soaked or involved in something' ,
'eminent': 'of outstanding reputation' ,
'replete': 'completely filled with' ,

'abound': 'existing in great number' ,
'technology': 'related to science of engineering' ,
'matron': 'a mature woman' ,
'automaton': 'robot' ,
'prognosticate': 'predict future' ,
'scouring': 'scraping ' ,
'grime': 'dirt' ,

'paradox': 'self contradictory but true' ,
'tinge': 'small amount of' ,
'annals': 'historical records' ,
'realm': 'someones special field' ,
'compound': 'to add to' ,

'drudgery': 'dull difficult work' ,
'implore': 'beg for assistance' ,
'badgered': 'to continually nag' ,
'interminably': 'unending' ,
'perceive': 'to come to have an understanding' ,
'perpetrated': 'to do something illegal, theiving' ,
'chagrin': 'distressed with humiliation' ,

'laconic': 'concise - brief - pithy' ,
'intrepid': 'brave - courageous' ,
'reticent': 'uncommunicative and secluded' ,
'accost': 'to greet first aggressively' ,
'throng': 'great number of people' ,

'hapless': 'luckless' ,
'felon': 'criminal' ,
'furtive': 'sly - secretive' ,
'plethora': 'overabundance' ,
'irate': 'angry' ,

'pretext': 'an excuse' ,
'fabricate': 'to make up a lie' ,
'adroit': 'clever and skillful' ,
'gesticulate': 'to use lively gestures' ,
'vigilant': 'alert' ,

'nuance': 'every tiny bit of difference' ,
'cajoled': 'coax - wheedle - persuade' ,
'rudimentary': 'elementary - basic' ,
'avid': 'enthusiastic' ,
'enhance': 'to make greater' ,
'penitentiary': 'prison' ,

'loathe': 'despise - hate' ,
'reprimand': 'to scold severely' ,
'lackluster': 'poor performance' ,
'wrest': 'seize - take back' ,
'caustic': 'sarcastic - stinging' ,

'incipient': 'beginning to develop' ,
'inadvertent': 'negligent' ,
'confederate': 'accomplice in illegal' ,
'jostle': 'to push' ,
'dupe': 'an easily fooled person' ,
'infamous': 'evil known for bad reputation' ,

'repudiate': 'reject' ,
'bristle': 'to have ones hair stand up fear and anger' ,
'ominous': 'threatening' ,
'cessation': 'a pause' ,
'tremulous': 'trembling' ,

'undertaker': 'who digs coffin' ,
'gubernatorial': 'governor office' ,
'mundane': 'earthly' ,
'incongruous': 'having inconsistent elements' ,
'euphemism': 'saying something indirectly' ,
'condolence': 'expression of sympathy' ,
'stipulate': 'make specific demand' ,

'alacrity': 'swift - briskiness' ,
'disdain': 'scorn - show disregard - disrespect - unworthy' ,
'belligerent': 'warlike' ,
'intimidate': 'to overawe' ,
'feint': 'a false attack' ,

'promulgate': 'to make it known officially' ,
'scoff': 'mock' ,
'pugnacious': 'quarrelsome' ,
'belittle': 'speak of as unimportant' ,
'brash': 'rude - insolent' ,

'laceration': 'jagged wound' ,
'tangible': 'touch or actual form' ,
'castigate': 'punish - chastise' ,
'octogenarian': 'person in eighties' ,
'sordid': 'dirty filthy ignoble' ,

'aspirant': 'candidate for better job' ,
'dregs': 'most worthless part' ,
'scurrilous': 'scandalous - vulgar remarks' ,
'frenzy': 'wild fit or frantic outburst' ,
'solace': 'easing of grief - make peace' ,

'scorn': 'disdain' ,
'mudslinging': 'make scandalous allegations' ,
'caucus': 'a community meeting political' ,
'masochist': 'take joy of own pain' ,
'vilification': 'abusively disparaging speech' ,
'disparage': 'of little worth' ,
'malcontent': 'a person who is dissatisfied' ,

'rampant': 'flourishing or spreading unchecked' ,
'concur': 'agree' ,
'inane': 'foolish' ,
'clandestine': 'secretly illicit' ,
'ethics': 'code of principles' ,

'flagrant': 'outrageous' ,
'admonish': 'to warn' ,
'duress': 'compulsion or force or coercion' ,
'sleuths': 'detective' ,
'inexorable': 'unrelenting inflexible' ,
'proctor': 'invigilator' ,
'conceit': 'excessive pride' ,
'braggart': 'one who boasts about himself' ,

'egregious': 'remarkably bad' ,
'acrimonious': 'bitter - caustic' ,
'duplicity': 'cunning double dealing' ,
'paucity': 'scarcity' ,
'distraught': 'mentally confused' ,
'furlough': 'leave of absence' ,

'elicit': 'to draw forth reaction from someone - extract' ,
'pernicious': 'harmful' ,
'construe': 'to infer or to deduce or to interpret' ,
'impunity': 'go without punishment' ,
'salvage': 'rescue or save' ,
'diligence': 'careful and persistent effort' ,
'coercion': 'duress - to make do something by force' ,

'railed': 'to express objection abusive' ,
'crusade': 'vigorous campaingn or movement' ,

'discern': 'perceive' ,
'consternation': 'dismay' ,
'sally': 'to rush forth' ,
'feasible': 'possible' ,
'affluent': 'rich' ,

}

d2 = {

'precocious': 'reaching maturity early' ,
'perfunctory': 'without paying attention  - superficial' ,
'deride': 'to scoff ones efforts' ,
'chagrin': 'humiliation' ,
'perverse': 'to persist with error - contrary' ,

'disparage': 'discredit or make it less worth' ,
'laudable': 'praiseworthy' ,
'eschew': 'avoid' ,
'fiasco': 'complete failure' ,
'masticate': 'to chew up' ,

'dubious': 'doubtful or suspicious' ,
'quell': 'to put an end to' ,
'voluble': 'talkative' ,
'obsolescence': 'process of wearing out' ,
'confidant': 'one whom you confide secrets' ,

'chastened': 'humbled  or punished archaic' ,

'ado': 'fuss' ,
'paroxysm': 'sudden outburst' ,
'reprehensible': 'worthy of blame - needs censure' ,
'skirmish': 'small fight' ,
'jurisdiction': 'range of authority' ,
'implacable': 'relentless - unforgiving - inexorable' ,
'nonconformists': 'person who doesn’t comply with rules' ,

'fray': 'a fight' ,
'monolithic': 'massively solid' ,
'harass': 'trouble or torment' ,
'indigent': 'poor needy' ,
'arbitrary': 'based on whim - dictatorial' ,
'placate': 'make less angry or hostile' ,

'stymie': 'prevent or hinder progress - impede' ,
'turbulent': 'unruly - agitated' ,
'cognizant': 'aware' ,
'flout': 'show contempt - scoff' ,
'effigy': 'hated person likeness' ,

'terminate': 'end' ,
'forthwith': 'immediately' ,
'exacerbate': 'to irritate - make worse' ,
'revert': 'return' ,
'oust': 'to drive out' ,

'alimony': 'financial assistance to spouse after divorce' ,
'delinquent': 'offender or wrongdoer' ,
'hoods': 'violent criminals' ,

'emaciated': 'abnormally thin - wasted away' ,
'surge': 'to rush suddenly' ,
'tranquil': 'quiet' ,
'sanctuary': 'shelter' ,
'ascend': 'to rise' ,

'malnutrition': 'inadequate diet' ,
'beseiged': 'to surround - hem in' ,
'afflict': 'to trouble greatly - in distress' ,
'privation': 'lack of necessities' ,
'sinister': 'evil - ominous' ,

'ubiquitous': 'being everywhere at same time' ,
'malignant': 'likely to cause death' ,
'thwart': 'to hinder - defeat' ,
'remote': 'distant hidden away' ,
'harbinger': 'a forerunner - advance notice' ,
'moat': 'deep wide ditch' ,

'excruciating': 'agonizing- torturing' ,
'respite': 'an interval of relief - delay' ,
'fretful': 'worrisome - irritable' ,
'succumb': 'to give way - yield' ,
'reverberate': 'reechoing - resounding' ,
'graft': 'corrupt records' ,

'lest': 'in case - for fear that' ,

'impresario': 'organizer of cultural events' ,
'bigot': 'narrow minded person - prejudiced person' ,
'adverse': 'unfavorable harmful' ,
'asset': 'valuable thing to have' ,
'extortion': 'getting money by threat' ,
'rabble rousers': 'who instigates mob' ,

'blatant': 'very showy - diagreeably loud' ,
'entourage': 'group of attendants' ,
'virulent': 'full of hate - harmful' ,
'venom': 'poison - spite - malice' ,
'spew': 'throw up - spit out' ,

'loath': 'unwilling - reluctant' ,
'solicit': 'to beg' ,
'astute': 'keen - shrewd' ,
'advocate': 'to be in favor of' ,
'ineffectual': 'not effective' ,

'scrutinize': 'examine closely' ,
'vexatious': 'annoying' ,
'nefarious': 'villianous - vicious' ,
'amicable': 'friendly - peaceful' ,
'malady': 'disease' ,

'inclement': 'bad stormy weather' ,
'peruse': 'examine or study carefully' ,
'desist': 'cease or stop' ,
'premonition': 'forewarning' ,
'recoil': 'draw back' ,
'picket': 'group of protesters' ,

'wan': 'sickly pale' ,
'doleful': 'sad melancholy' ,
'pertinent': 'to the point' ,
'mastiff': 'a large dog' ,
'ruddy': 'healthy red face' ,
'obsess': 'to haunt = preoccupy' ,

'histrionics': 'display of emotions' ,
'elusive': 'hard to grasp' ,
'frustrate': 'counteract - foil - thwart' ,
'symptomatic': 'indicative' ,
'interject': 'interrupt - insert' ,

'inert': 'without power to move' ,
'salient': 'prominent' ,
'imminent': 'likely to happen - threatening' ,
'squeamish': 'over sensitive - easily shocked' ,
'engrossed': 'absorbed' ,
'convulsions': 'uncontrollable muscle contractions' ,
'schlock': 'low quality' ,
'patron': 'sponsorer - customer' ,

'hysterical': 'uncontrollable emotion' ,

'inundate': 'to flood' ,
'fruitless': 'useless' ,
'poignant': 'moving - painful to the feelings' ,
'garbled': 'mixed up' ,
'sanguine': 'optimistic' ,

'phlegmatic': 'calm and collected - usually a person' ,
'corroborate': 'confirm or support' ,
'comprehensive': 'thorough' ,
'zealous': 'enthusiastic' ,
'coerce': 'to force' ,
'alibi': 'a  perpetrator claiming he was somewhere else' ,
'swindler': 'person who uses deception to rob' ,

'elapse': 'to slip by' ,
'meticulous': 'careful' ,
'domicile': 'home' ,
'lax': 'careless or negligent' ,
'sporadic': 'occasional' ,

'rash': 'reckless' ,
'conjecture': 'guess' ,
'obviate': 'to do away with - eliminate' ,
'lurid': 'sensational' ,
'quip': 'joke' ,
'longshoreman': 'docker - who loads and unloads ships' ,
'lusty': 'joyous archaic - passionate' ,

'allegiance': 'loyalty - pledge  allegiance' ,
'rote': 'mechanical or habitual repetition' ,
'porpoise': 'a dolphin fish' ,

}

d3 = {

'diatribe': 'bitter criticism' ,
'inhibition': 'restraint feeling of ones self concious - holding back oneself' ,
'fortuitous': 'accidental - happening by lucky chance' ,
'incoherent': 'disjointed - unclear' ,
'ilk': 'of a particular kind or sort' ,

'prestigious': 'illustrious' ,
'placard': 'poster' ,
'integral': 'essential ' ,
'remuneration': 'reward - pay' ,
'nominal': 'slight' ,

'expunge': 'erase' ,
'flamboyant': 'showy - colorful' ,
'anathema': 'something greatly detested' ,
'schism': 'split' ,
'utopia': 'place of perfection' ,

'timorous': 'fearful' ,
'truncated': 'cut short' ,
'jaunty': 'sprightly full of energy - gay' ,
'fractious': 'quarrelsome' ,
'ostentatious': 'showy  - to impress' ,

'incontrovertible': 'undeniable' ,
'surreptitiously': 'stealthily - accomplished by secret' ,
'importune': 'ask urgently' ,
'haven': 'safe place' ,
'subjugate': 'conquer' ,

'eventuate': 'to result finally' ,
'emit': 'to give off' ,
'ultimate': 'result' ,
'viable': 'pracitcable' ,
'subterranean': 'underground' ,

'premise': 'grounds for a conclusion - If the premise is true then the conclusion must be true' ,
'jeopardize': 'endanger' ,
'incredulous': 'skeptical' ,
'permeate': 'to spread through' ,
'propitious': 'favorable' ,

'surmise': 'guess' ,
'curtail': 'to cut short' ,
'repress': 'to put down' ,
'cryptic': 'puzzling' ,
'inchoate': 'in an early stage' ,

'aspire': 'to strice for' ,
'inveigh': 'attack verbally' ,
'nettle': 'irritate' ,
'overt': 'open' ,
'relegate': 'assign to an inferior position' ,

'supine': 'lying on back' ,
'mammoth': 'huge' ,
'repulse': 'drive back' ,
'havoc': 'ruin' ,
'raze': 'destroy' ,

'lethal': 'deadly' ,
'scurry': 'run hastily' ,
'incisive': 'acute - sharp' ,
'precipitate ': 'hasten - cause to do something quickly' ,
'stereotype': 'unvarying pattern - cliché - typecast' ,
'gild': 'cover thinly with gold' ,

'singular': 'extraordinary - remarkable' ,
'stentorian': 'loud and powerful' ,
'valor': 'courage' ,
'bias': 'prejudice' ,
'sinecure': 'soft job with status or financial benefit' ,

'slugger': 'who throws hard punches' ,
'hoodlum': 'gangster' ,
'conscientious': 'willing to do ones work thoroughly' ,

'complicity': 'partner in wrongdoing' ,
'liquidation': 'disposal of, killing' ,
'accomplice': 'an associate in crime' ,
'recant': 'withdraw previous statements' ,
'culpable': 'deserving blame' ,

'abrogate': 'abolish - repeal to do away with - repudiate' ,
'preclude': 'prevent' ,
'alleged': 'supposed - reported' ,
'invalidate': 'to deprive of legal force - to nullify' ,
'access': 'admittance' ,

'extrinsic': 'foreign - coming from outside' ,
'landmark': 'historic - turning point' ,
'persevere': 'persist' ,
'declaim': 'speak loudly - rhetoric - oratorial' ,
'fetter': 'to hamper' ,

'nomadic': 'wandering' ,
'paragon': 'model of excellence' ,
'controversial': 'debatable' ,
'asperity': 'harshness of temper' ,
'epithets': 'descriptive name - tagline Charles the Bald' ,

'hairnets': 'net cap worn by cooks' ,
'straitjacket': 'hands tied up inside jacket' ,
'bandito': 'a Mexican bandit' ,

'indigenous': 'native' ,
'gregarious': 'sociable' ,
'habitat': 'natural environment' ,
'cursory': 'hasty - not thorough' ,
'interloper': 'an unauthorized person' ,

'prolific': 'producing abundantly - fertile' ,
'bulwark': 'protection' ,
'sedentary': 'largely inactive - sitting lifestyle' ,
'frugal': 'thrifty' ,
'antithesis': 'exact opposite' ,

'altruistic': 'unselfish' ,
'embellish': 'adorn - touch up' ,
'cache': 'secret hiding place' ,
'coterie': 'small group having something in common' ,
'cupidity': 'greed' ,

'virtuosity': 'great technical skill' ,
'temerity': 'foolish boldness' ,
'amorous': 'full of love' ,
'progeny': 'descendants' ,
'saturate': 'soak - fill up completely' ,

'beatniks': '1950s 60s person who likes beats - classicists opp' ,
'mugged': 'attacked in public' ,
'lucre': 'filthy money gained in dishonorable way' ,
'starch': 'stiffness of manner or character' ,

}

d4 = {

'ruse': 'trick' ,
'perpetrate': 'commit' ,
'consummate': 'complete  - of the highest degree' ,
'subterfuge': 'ruse - trick' ,
'concoct': 'devise' ,
'fallacious': 'misleading' ,

'manifold': 'complex - many' ,
'assiduous': 'devoted - attentive' ,
'impeccable': 'faultless - perfect' ,
'fraught': 'filled' ,
'resourceful': 'able to meet any situation' ,

'murky': 'dark - obscure' ,
'components': 'elements' ,
'hoax': 'deception' ,
'labyrinth': 'maze - winding passages' ,
'evaluate': 'appraise - find the value for' ,

'exult': 'rejoice greatly' ,
'attest': 'to certify' ,
'gullible': 'easily cheated or fooled' ,
'deploy': 'to position forces with plan' ,
'enigma': 'riddle' ,

'abortive': 'fruitless - useless - failing' ,
'modify': 'to change' ,
'accommodate': 'to make fit - adjust' ,
'spontaneous': 'without preparation' ,
'innate': 'natural' ,

'veneer': 'thin covering' ,
'myriad': 'countless number' ,
'urbane': 'polished - witty - civilized' ,
'crave': 'to desire' ,
'irrelevant': 'not related to the subject' ,

'deem': 'believe - to judge' ,
'inherent': 'inborn' ,
'buff': 'a fan - follower' ,
'romp': 'to move in a lively manner' ,
'latent': 'lying hidden' ,

'tortuous': 'winding' ,
'itinerant': 'wandering' ,
'peregrination': 'travel' ,
'conjugal': 'relating to marriage - connubial' ,
'barometer': 'instrument for measuring change' ,

'megalomania': 'abnormal desire for wealth and power' ,
'profligate': 'wasteful' ,
'strife': 'discord - disagreement' ,
'legion': 'a large number' ,
'coup': 'revolution' ,

'amnesty': 'a general pardon' ,
'expatriate': 'an exile' ,
'exonerate': 'to free from guilt' ,
'fiat': 'an offical order - a decree' ,
'mendacious': 'lying - untrue' ,

'parsimonious': 'miserly' ,
'pecuniary': 'financial' ,
'dismantle': 'take apart' ,
'sumptuous': 'lavish' ,
'underwrite': 'agree to finance' ,

'restrictive': 'harsh - confining' ,
'balk': 'to refuse to move' ,
'blunt': 'plain spoken' ,
'nostalgia': 'yearning for the past' ,
'rife': 'widespread' ,

'sturgeon': 'type of fish' ,
'earwig': 'type of insect' ,

'reviled': 'scolded' ,
'derogatory': 'belittle - disparage' ,
'indict': 'accuse' ,
'nebulous': 'unclear - vague' ,
'pesky': 'annoying' ,

'disposition': 'temperament - character' ,

'repose': 'state of rest' ,
'redolent': 'fragrant' ,
'omnivorous': 'eating any kind of food' ,
'disparate': 'different' ,
'abstemious': 'moderate in eating or drinking' ,

'frigid': 'very cold weather' ,

'extant': 'still exisiting' ,
'vicissitudes': 'difficulties' ,
'edifice': 'a building' ,
'sultry': 'extremely hot and humid - torrid weather' ,
'trenchant': 'keen - inicisive' ,

'rebuttal': 'denial' ,

'puissant': 'powerful' ,
'unabated': 'without subsiding' ,
'maudlin': 'sentimental' ,
'levity': 'lightness of disposition - humor' ,
'lugubrious': 'very sad' ,

'sundry': 'several' ,

'scion': 'child - descendant' ,
'indoctrinate': 'to teach certain principles' ,
'opulence': 'wealth - riches' ,
'obsequious': 'seeking favor - fawning' ,
'fulsome': 'excessive - insincere' ,

'lush': 'luxurious - elaborate' ,
'destitution': 'extreme poverty' ,
'ponder': 'to consider carefully' ,
'supplication': 'earnest prayer' ,
'decadence': 'decay' ,

'penance': 'atonement for sin' ,
'ascetic': 'one who practices self denial and devotion' ,
'desultory': 'occuring ny change - disconnected' ,
'disciple': 'follower' ,
'metamorphosis': 'change' ,

'bona fide': 'genuine' ,
'salvation': 'deliverance from ruin' ,
'materialism': 'attention to wordly things neglecting spirituality' ,
'nurture': 'to nourish - support' ,
'nirvana': 'freedom from care and pain - Buddhist heaven' ,

'indelible': 'making mark that cannot be removed' ,
'fervent': 'ardent - passionate followers' ,
'gallantry': 'courageous act' ,
'martyrdom': 'death - suffering' ,

'juxtapose': 'to place side by side' ,
'plight': 'predicament - dangerous situation' ,
'covert': 'secret - hidden' ,
'cope': 'to be able to handle' ,
'incompatibility': 'quality of being mismated' ,

'incapacitated': 'disabled - made unfit' ,
'fabricate': 'to lie - concoct' ,
'connubial': 'related to marriage - conjugal' ,
'demur': 'to object' ,
'appellation': 'a name' ,

'escalation': 'an increase - intensification' ,
'indifference': 'lack of concern' ,
'potential': 'possible' ,
'cumulative': 'accumulated' ,
'recondite': 'secret - hidden - obscure' ,

'acknowledge': 'admit' ,
'delude': 'fool' ,
'prelude': 'introduction' ,
'chimerical': 'imaginary - visionary - fantastic' ,
'palliate': 'aleeviate - relieve without curing' ,
'predicament': 'difficult situation' ,

'heterogeneous': 'dissimilar' ,
'gamut': 'range' ,
'perspicacious': 'acutely perceptive - shrewd' ,
'analogous': 'comparable - similar' ,
'maladjusted': 'poorly adjusted - disturbed' ,

'acrimony': 'bitterness or ill feeling' ,
'querulous': 'complaining in a rather petulant or whining manner' ,
'petulant': 'childishly sulky or bad tempered' ,

'phenomenon': 'unusual occurrence' ,
'mortality': 'death' ,
'decade': 'ten years' ,
'susceptible': 'easily affected' ,
'nuerotic': 'suffereing from nervous disorder' ,

'pedagogue': 'teacher' ,
'enunciate': 'to utter - proclaim' ,
'inordinate': 'excessive' ,
'irascible': 'irritable' ,
'introspective': 'looking into ones own feelings' ,

'perpetuate': 'to cause to continue' ,
'mandate': 'an authoritative order or command' ,
'compensatory': 'serving to pay back' ,
'neutralize': 'to counteract' ,
'catastrophic': 'disastrous' ,

'aardvark': 'an animal' ,
'zymurgy': 'distillery of fermentation of winemaking' ,
'redress': 'seek remedy or set right - rectify' ,
}

d5 ={
'anthropologist': 'an expert in study of races beliefs customs of mankind' ,
'artifact': 'an object made by had rather than nature' ,
'bizarre': 'odd peculiar strange weird' ,
'fetish': 'an object that is thought to have magical powers' ,
'inanimate': 'lifeless' ,

'imperative': 'compulsory - necessary - urgent' ,
'imprudent': 'unwise - not careful' ,
'prohibition': 'the act of forbidding certain behavior' ,
'taboo': 'forbidden by custom or religious practice' ,
'taint': 'contamination - one that spoils' ,

'abhor': 'to detest - to despise' ,
'absurd': 'ridiculous' ,
'bigot': 'a person who is intolerant of other peoples views' ,
'contemptuous': 'expressing a feeling that something is worthless' ,
'universal': 'present everywhere' ,

'vulnerable': 'capable of being injured' ,
'entreaty': 'appeal or plea' ,
'tradition': 'custom that has been handed down' ,
'originate': 'begin - arise' ,
'inviolable': 'safe from destruction' ,
'gesundheit': 'sneeze bless you in german' ,
'abreast': 'alongside - side by side - be in level' ,
'cartographer': 'map makers' ,

'dispersed': 'scatteres - spread - broken up' ,
'awesome': 'inspiring terror -weird' ,
'puny': 'weak - unimportant' ,
'debris': 'ruins - fragments' ,
'eruption': 'bursting out' ,

'obliterate': 'erase - wipe out' ,
'deplorable': 'sad - pitiable' ,
'initiate': 'start - set going' ,
'conflagration': 'great fire' ,
'rue': 'regret' ,

'hoard': 'hide - store - accumulate' ,
'congenial': 'sympathetic - agreeable' ,
'sage': 'wise man - philosopher' ,
'aegis': 'shield - protection - sponsorship' ,
'detriment': 'injury - damage - hurt' ,

'hardy': 'sturdy - capable of enduring difficult situation' ,
'longevity': 'long duration of life' ,
'imbibe': 'drink' ,
'virile': 'masterful - manly' ,
'senile': 'infirm - weak from old age' ,
'doddering': 'trembling - shaking' ,

'lethargic': 'lazy - indifferent' ,
'prevalent': 'prevailing -common - general' ,
'paramount': 'supreme - foremost' ,
'remiss': 'careless - negligent' ,
'hostile': 'antagonistic - angry' ,

'aversion': 'strong dislike - opposition' ,
'rebuke': 'criticize - reproach - reprimand' ,
'evince': 'show plainly - exhibit' ,
'vogue': 'fashion' ,
'superficial': 'on the surface - slight' ,

'jettison': 'throw overboard - discard' ,
'inevitable': 'unavoidable -sure -certain' ,
'lucrative': 'profitable' ,
'tussle': 'a rough struggle' ,
'intrinsic': 'essential - natural - inborn' ,

'acute': 'severe - keen -sharp' ,
'gist': 'essence - main point' ,
'transient': 'passing - short lived - fleeting' ,
'terse': 'concise - brief - compact' ,
'cogent': 'forceful - convincing - persuasive' ,

'pinnacle': 'summit -peak - top -crown' ,
'array': 'arrangement - system' ,
'obscure': 'unknown - lowly' ,
'ardent': 'passionate -eager' ,
'culminate': 'reach the highest point' ,

'constrict': 'limit - bind - squeeze' ,
'prodigy': 'marvel - phenomenon' ,
'bereft': 'deprived of' ,
'falter': 'stumble- hesitate' ,
'exultation': 'triumphant joy' ,

'vitriolic': 'biting - burning' ,
'invective': 'insulting - abusive' ,
'besmirch': 'soil - stain - dim the reputation' ,
'voluminous': 'bulky - large' ,
'retrospect': 'looking backwards' ,

'egotist': 'a vain - conceited person' ,
'humility': 'humbleness - modesty' ,
'pungent': 'sharply stimulating - biting' ,
'inveterate': 'habitual - firmly established' ,
'adamant': 'unyielding - inflexible' ,

'vulnerable': 'open to attack - susceptible' ,
'bedlam': 'confusion - uproar' ,
'cacophony': 'discord - harsh sound - dissonance' ,
'exploit': 'profit by - utilize' ,
'propinquinty': 'sudden - nearness in time or place' ,

'crocus': 'a flower in Spring' ,
'disgruntled': 'unhappy - displeased' ,
'infallible': 'exempt from error - right' ,
'panacea': 'cure  all - remedy' ,
'eradicate': 'wipe out' ,
'impede': 'interfere - block - hinder' ,

'sedate': 'quiet - still - undisturbed - sober' ,
'equanimity': 'eveness of mind - composure' ,
'compatible': 'harmonious - well matched' ,
'serenity': 'peaceful repose' ,
'revere': 'honor - respect - admire' ,

'irrational': 'unreasonable - absurd' ,
'avarice': 'greed - passion for riches' ,
'insatiable': 'cannot be satisfied' ,
'nadir': 'lowest point' ,
'moribund': 'dying - at the point of death' ,

'lithe': 'graceful' ,
'obese': 'very fat' ,
'adherent': 'supporter - backer' ,
'bliss': 'happiness - pleasure' ,
'pathetic': 'sad - pitiful - distressing' ,

'exhort': 'urge strongly - advise' ,
'apathy': 'lack of interest - unconcern' ,
'fracas': 'noisy fight - brawl' ,
'inebriated': 'drunk - intoxicated' ,
'adversary': 'opponent - enemy - foe' ,

'indolent': 'lazy' ,
'gusto': 'enthusiasm - enjoyment -zest' ,
'garrulous': 'talkative - wordy' ,
'banal': 'trivial - meaningless from overuse' ,
'platitude': 'commonplace or trite saying' ,

'pique': 'fit of resentment' ,
'dilettante': 'one who has great interest but little knowledge' ,
'atypical': 'nonconforming' ,
'nondescript': 'undistinguished - difficult to describe' ,
'wane': 'decrease - decline' ,
'enervating': 'causing one to feel drained out of energy' ,
'trite': 'lacking originality' ,

'extinct': 'no longer existing' ,
'idyllic': 'simple - peaceful' ,
'galvanize': 'excite or arouse to activity' ,
'encumbrance': 'burden - handicap - load' ,
'gaudy': 'showy - flashy' ,

'condescend': 'stoop - lower oneself' ,
'candor': 'frankness - honesty' ,
'mortify': 'embarrass - humiliate' ,
'jocose': 'humorous - merry' ,
'malign': 'abuse - slander' ,

'abjure': 'forgo - let go' ,
'quorum': 'minimum number of members political' ,
'omnipotent': 'almighty - unlimited in power' ,
'zenith': 'summit - top - prime' ,
'fledgling': 'little known - newly developed' ,
'peremptory': 'absolute - compulsory - binding' ,
'precedent': 'custom - model' ,

'uncouth': 'lacking good manners' ,
'wheedle': 'coax - persuade - cajole' ,
'rustic': 'countrified  - unpolished' ,
'jubilant': 'joyful in high spirits' ,
'decorum': 'politeness - correct behavior' ,
'charlatan': 'pretender - fraud' ,

}

d6 ={
'propaganda': 'information that is misleading politics' ,
'specious': 'superficially plausible but actually misleading' ,
'fervid': 'enthusiastic - intense - passionate' ,
'prudent': 'wise - cautious' ,
'ostensible': 'seeming - pretended - outward' ,
'heresy': 'lack of faith - dissent' ,
'spurious': 'false - specious - counterfeit' ,

'propagate': 'produce - spread - multiply' ,
'anomaly': 'abnormality - irregularity' ,
'innocuous': 'innocent - harmless - mild' ,
'surfeit': 'excess - superabundance' ,
'milieu': 'environment - setting' ,

'strident': 'harsh - shrill - rough' ,
'concomitant': 'accompanying - attending' ,
'lassitude': 'tired - weariness - fatigue' ,
'deleterious': 'harmful - bad' ,
'efficacy': 'power to produce an effect' ,

'dissent': 'protest - differ - disagree' ,
'ferment': 'agitiation - uproar - turmoil' ,
'attenuated': 'weaked - thinned - decreased' ,
'arbiter': 'judge' ,
'incumbent': 'morally required' ,

'profound': 'deep - intense' ,
'alleviate': 'make easier - lighten' ,
'prodigious': 'extraordinary - enormous' ,
'expedite': 'carry out promptly' ,
'celerity': 'speed - rapidity' ,

'antiquated': 'old fashioned or outdated' ,
'usurp': 'seize - annex - grab' ,
'paltry': 'of little importane - insignificant' ,
'condone': 'pardon - excuse' ,
'trivial': 'petty - worthless' ,
'bizarre': 'fantastic - odd' ,

'shibboleth': 'custom or belief distinguishing a particular class of people' ,
'menial': 'humble - degrading' ,
'venerable': 'respected - worshipped' ,
'extraneous': 'foreign - not belonging' ,
'ambiguous': 'vague - undefined - not specific or clear - more than one interpretation' ,
'succint': 'brief - concise' ,

'archaic': 'out of date' ,
'emulate': 'strive to equal' ,
'facetious': 'comical - humorous - witty' ,
'rabid': 'fanatical - furious - mad' ,
'salubrious': 'healthful - wholesome' ,
'acme': 'zenith' ,

'complacent': 'self satisfied' ,
'somber': 'gloomy - sad' ,
'debilitate': 'weaken' ,
'impetuous': 'impulsive' ,
'occult': 'secret - mysterious - supernatural' ,

'discreet': 'careful - cautious - prudent' ,
'foment': 'stir up - instigate' ,
'glean': 'gather - collect' ,
'quarry': 'something hunted or pursued' ,
'slovenly': 'disorderly - carelessly' ,

'contrite': 'remorseful - regretful' ,
'penitent': 'regretful - confessing guilt' ,
'abjure': 'abstain from - renounce' ,
'reproach': 'reprimand - rebuke' ,
'evanescent': 'momentary - passing - fleeting' ,
'tantamount': 'equivalent - identical' ,

'swarthy': 'dark complexioned' ,
'propensity': 'disposition - inclination - bent' ,
'wary': 'watchful - shrewd' ,
'allay': 'calm - soothe' ,
'deter': 'hinder - discourage' ,
'connoisseur': 'expert' ,

'rancor': 'bitterness or resentfulness longstanding' ,
'incarcerate': 'imprison or confine' ,

'site': 'location' ,
'vigil': 'wakeful watching' ,
'cumbersome': 'unweildy - burdensome' ,
'interrogate': 'question' ,
'divulge': 'disclose - reveal' ,

'commodious': 'large - spacious' ,
'fluctuate': 'shift - alternate' ,
'unmitigated': 'unrelieved - as bad as can be' ,
'disheveled': 'disorderly clothing or hair' ,
'antiquated': 'old fashioned or outdated' ,

'expurgate': 'unsuitable matter removed' ,
'vituperative': 'invective - bitter and abusive' ,

'tenacious': 'tough - stubborn' ,
'façade': 'front - superficial appearance' ,
'asinine': 'silly - stupid' ,
'grimace': 'facial expression of disgust' ,
'calumny': 'false accusation - slander' ,

'pittance': 'small amount' ,
'au courant': 'up to date' ,
'fastidious': 'particular - choosy - OCD' ,
'noisome': 'foul - unwholesome' ,
'unkempt': 'untidy - neglected' ,

'parable': 'a moralistic story' ,
'whimsical': 'humorous - witty' ,
'lampoon': 'ridicule' ,
'countenance': 'tolerate - approve' ,
'sanctimonious': 'hypocritically religious' ,

'supercilious': 'acting to be superior to others - arrogant- haughty' ,
'capricious': 'fickle - mercurial - sudden mood changes' ,

'equanimity': 'calmness - self control' ,
'effrontery': 'boldness' ,
'nonentity': 'one of no importance' ,
'flabbergasted': 'astounded' ,
'debacle': 'ruin - collapse' ,

'vivacious': 'lively - gay' ,
'gaunt': 'thin - haggard' ,
'mien': 'appearance - bearing' ,
'hirsute': 'hairy' ,
'refute': 'proving wrong or false' ,

'pensive': 'thoughful - reflective' ,
'whet': 'stimulate - stir up' ,
'stupor': 'daze - insensible condition' ,
'wince': 'draw back - flinch' ,
'cliché': 'a commonplace saying' ,

'genre': 'a certain form or style in painting or literature' ,
'candid': 'frank - open - honest' ,
'unsavory': 'disagreeable - offensive - morally bad' ,
'degrade': 'make contemptible - lower' ,
'venial': 'pardonable - forgivable' ,

'adulation': 'excessive admiration or praise' ,
'epitome': 'person or thing that embodies the best' ,
'dexterity': 'mental or physical skill' ,
'grotesque': 'strange - bizarre - fantastic' ,
'compassion': 'sympathetic feeling - kindness' ,
'repugnant': 'distasteful - repulsive' ,

'acme': 'zenith -peak - pinnacle' ,
'copious': 'ample - abundant - plentiful' ,
'vehemently': 'violently - eagerly - apssionately' ,
'depict': 'describe clearly - picture - portray' ,
'naïve': 'unworldly - unsophisticated' ,

'perfidious': 'treacherous - false' ,
'covet': 'want - envy - wish' ,
'ingratiate': 'win confidence - charm' ,
'penury': 'poverty' ,
'ignominious': 'humiliaitng - disgraceful' ,

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
	    	print ("The remaining words are: ",len(items)-count)
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
	    	
print (" Which block of words do you want to revise?\n    1\t    2\t    3\t    4\t    5\t    6\t")
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
	time.sleep(1)
	block=d6
	func()
	time.sleep(1)
#	print (block)
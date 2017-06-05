import sys

telikes=['anagnoristikotk','arithmstatheratk','sintk','miontk','epitk','diatk','isontk','mikrisotk','diaforotk','mikroterotk','megalisotk','megaliterotk','ekxwrisitk','lathostk','komatk','erwtimtk','deksiapartk','aristeripartk','eoftk','deksiatetragwnhpartk','aristeritetragonipartk','deksiaaggtk','aristeroaggtk','anwkatwtk']

pinakas=[
['katastash1','katastash2','sintk','miontk','epitk','diatk','katastash4','katastash3','isontk','katastash5','katastash6','aristeroaggtk','deksiaaggtk','aristeripartk','deksiapartk','aristeritetragonipartk','deksiatetragwnhpartk','erwtimtk','komatk','eoftk','katastash0','lathostk'],
['katastash1','katastash1','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk','anagnoristikotk'],
['arithmstatheratk','katastash2','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk','arithmstatheratk'],
['mikroterotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk','diaforotk','mikroterotk','mikrisotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk','mikroterotk'],
['megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megalisotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk','megaliterotk'],
['anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','ekxwrisitk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk','anwkatwtk'],
['lathostk','lathostk','lathostk','lathostk','katastash7','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk','lathostk'],
['katastash7','katastash7','katastash7','katastash7','katastash8','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','lathostk','katastash7','katastash7'],
['katastash7','katastash7','katastash7','katastash7','katastash8','katastash7','katastash7','katastash7','katastash7','katastash7','katastash0','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7','katastash7']
]


arxeio = open(sys.argv[1])
onoma = sys.argv[1]

arxeioInt = open(onoma[0:len(onoma)-3]+'.int','w')
arxeioC = open(onoma[0:len(onoma)-1],'w')
arxeioFinal = open(onoma[0:len(onoma)-3]+'.asm','w')

grammes=1
tetrades=[]
proswrino=0
onomaProgramma=''
metavlhtes = []
exitList = []
pinakasSymvolwn = []
offset = 12

def lektikos():
        global grammes
        leksi=""
        katastash = 'katastash0'
        while katastash not in telikes:
            c=arxeio.read(1)
            if (c>='A' and c<='Z') or (c>='a' and c<='z'):
                stili=0
            elif (c>='0' and c<='9'):
                stili=1
            elif (c=='+'):
                stili=2
            elif (c=='-'):
                stili=3
            elif (c=='*'):
                stili=4
            elif (c=='/'):
                stili=5
            elif (c=='>'):
                stili=6
            elif (c=='<'):
                stili=7
            elif (c=='='):
                stili=8
            elif (c==':'):
                stili=9
            elif (c=='\\'):
                stili=10
            elif (c=='{'):
                stili=11
            elif (c=='}'):
                stili=12
            elif (c=='('):
                stili=13
            elif (c==')'):
                stili=14
            elif (c=='['):

                stili=15
            elif (c==']'):
                stili=16
            elif (c==';'):
                stili=17
            elif (c==','):
                stili=18
            elif (c==''):
                stili=19
            elif (c==' ' or c=='\t' or c=='\n'):
                if c=='\n':
                    grammes = grammes + 1;
                stili=20
            else:
                stili=21
                
            grammi = int(katastash[len(katastash)-1])
            katastash = pinakas[grammi][stili]
            if katastash!='katastash0' and katastash!='katastash6' and katastash!='katastash7' and katastash!='katastash8' and len(leksi)<30:
                leksi=leksi+str(c);

        if katastash=='lathostk':
            if c=='':
               print 'EOF mesa sta sxolia'
               exit(0)
            elif stili==21:
                print 'Lathos xaraktiras'
                exit(0)
            else:
                print 'Perimena *'
                exit(0)
                
        if katastash=='mikroterotk' or katastash=='megaliterotk' or katastash=='arithmstatheratk' or katastash=='anagnoristikotk' or katastash=='anwkatwtk':
            arxeio.seek(-1,1)
            leksi=leksi[0:len(leksi)-1]
        if katastash=='eoftk':
            leksi='EOF'

        if katastash=='anagnoristikotk':
            if leksi=='and':
                katastash='andtk'
            elif leksi=='program':
                katastash='programtk'
            elif leksi=='in':
                katastash='intk'
            elif leksi=='inout':
                katastash='inouttk'
            elif leksi=='and':
                katastash='andtk'
            elif leksi=='or':
                katastash='ortk'
            elif leksi=='not':
                katastash='nottk'
            elif leksi=='if':
                katastash='iftk'
            elif leksi=='exit':
                katastash='exittk'
            elif leksi=='declare':
                katastash='declaretk'
            elif leksi=='procedure':
                katastash='proceduretk'
            elif leksi=='do':
                katastash='dotk'
            elif leksi=='function':
                katastash='functiontk'
            elif leksi=='return':
                katastash='returntk'
            elif leksi=='else':
                katastash='elsetk'
            elif leksi=='print':
                katastash='printtk'
            elif leksi=='while':
                katastash='whiletk'
            elif leksi=='enddeclare':
                katastash='enddeclaretk'
            elif leksi=='call':
                katastash='calltk'
            elif leksi=='select':
                katastash='selecttk'
            elif leksi=='default':
                katastash='defaulttk'
                
        return leksi, katastash

def synt():
    global onomaProgramma
    leksi, katastash = lektikos()
    if katastash == 'programtk':
        leksi, katastash =lektikos()
        if katastash=='anagnoristikotk':
            onomaProgramma=leksi
            
            eisagwghScope(onomaProgramma)
            
            leksi, katastash = lektikos()
            leksi, katastash=block(leksi, katastash, onomaProgramma,'programtk')
            if katastash!='eoftk':
                print grammes, ' Perimena eof'
                exit(0)
        else:
            print grammes, ' Perimena onoma programmatos'
            exit(0)
    else:
        print grammes, ' Perimena program'
        exit(0)
        
def block(leksi, katastash, onomaBlock, typosBlock):
	global returnFlag
	if katastash=='aristeroaggtk':
		leksi, katastash = lektikos()
		
		leksi, katastash = declarations(leksi, katastash)
		leksi, katastash = subprograms(leksi, katastash)
		
		#gia to  startQuad
		if onomaBlock!=onomaProgramma:
			listaEntities = pinakasSymvolwn[1][2]
			entity = listaEntities[len(listaEntities)-1]
			entity[2] = nextquad()
		
		genquad('begin block', onomaBlock, '_', '_')
		returnFlag=False
		leksi, katastash = sequence(leksi, katastash)
		
		if onomaBlock==onomaProgramma:
			genquad('halt', '_', '_', '_')
		
		frameLength = offset
		if onomaBlock!=onomaProgramma:
			listaEntities = pinakasSymvolwn[1][2]
			entity = listaEntities[len(listaEntities)-1]
			entity[3] = frameLength
		
		makeFiles()
		intFinal()
		diagrafhScope()
		genquad('end block', onomaBlock, '_', '_')
		
		if returnFlag==True and (typosBlock=='programtk' or typosBlock=='proceduretk'):
			print grammes, ' Exw dei return mesa sto porgramma h se diadikasia'
			exit(0)
		if returnFlag==False and typosBlock=='functiontk' :
			print grammes, ' Den exw dei return mesa sthn synarthsh'
			exit(0)	
			
		if katastash=='deksiaaggtk':
			leksi, katastash = lektikos()
		else:
			print grammes, 'Perimena }'
			exit(0)
	else:
		print grammes, 'Perimena {'
		exit(0)
	return leksi, katastash

def declarations(leksi, katastash):
    if katastash=='declaretk':
        leksi, katastash = lektikos()
        leksi, katastash = varlist(leksi, katastash)
        if katastash == 'enddeclaretk':
            leksi, katastash = lektikos()
            return leksi, katastash
        else:
            print grammes, 'Perimena enddeclare'
            exit(0)
    return leksi, katastash

def varlist(leksi, katastash):
	global metavlhtes
	if katastash == 'anagnoristikotk':
		metavlhtes=metavlhtes+[leksi]
		
		eisagwghEntityMetavliti(leksi)
		
		leksi, katastash = lektikos()
		while katastash=='komatk':
			leksi, katastash = lektikos()
			if katastash=='anagnoristikotk':
				metavlhtes=metavlhtes+[leksi]
				eisagwghEntityMetavliti(leksi)
		
				leksi, katastash = lektikos()
			else:
				print grammes, 'Perimena onoma metavlhths stis dilwseis'
				exit(0)
	return leksi, katastash


def subprograms(leksi, katastash):
    while katastash=='functiontk' or katastash=='proceduretk':
        leksi, katastash=func(leksi, katastash)
    return leksi, katastash


def func(leksi, katastash):
    if katastash=='proceduretk':
        leksi, katastash = lektikos()
        if katastash=='anagnoristikotk':
            onomaBlock=leksi
            
            eisagwghEntitySynarthshs(onomaBlock,'proceduretk')
            
            eisagwghScope(onomaBlock)
            leksi, katastash = lektikos()
            leksi, katastash = funcbody(leksi, katastash, onomaBlock, 'proceduretk')
        else:
            print grammes, 'Perimena onoma diadikasias'
    elif katastash=='functiontk':
        leksi, katastash = lektikos()
        if katastash=='anagnoristikotk':
            onomaBlock=leksi
            
            eisagwghEntitySynarthshs(onomaBlock,'functiontk')
            
            eisagwghScope(onomaBlock)
            
            leksi, katastash = lektikos()
            leksi, katastash = funcbody(leksi, katastash, onomaBlock,'functiontk')
        else:
            print grammes, 'Perimena onoma synarthshs'
    return leksi, katastash

def funcbody(leksi, katastash, onomaBlock, typosBlock):
    leksi, katastash = formalpars(leksi, katastash)
    leksi, katastash = block(leksi, katastash, onomaBlock,typosBlock)
    return leksi, katastash

def formalpars(leksi, katastash):
    if katastash=='aristeripartk':
        leksi, katastash = lektikos()
        if katastash!='deksiapartk':
            leksi, katastash = formalparlist(leksi, katastash)
        
        if katastash=='deksiapartk':
            leksi, katastash = lektikos()
            return leksi, katastash
        else:
            print grammes, ' Perimena )'
            exit(0)
    else:
        print grammes, ' Perimena ('
        exit(0)

def formalparlist(leksi, katastash):
    leksi, katastash = formalparitem(leksi, katastash)
    while katastash=='komatk':
        leksi, katastash = lektikos()
        leksi, katastash = formalparitem(leksi, katastash)
    return leksi, katastash

def formalparitem(leksi, katastash):
    
    if katastash=='intk':
        leksi, katastash = lektikos()
        if katastash == 'anagnoristikotk':
			eisagwghEntityParametros(leksi,'intk')
			leksi, katastash = lektikos()
        else:
            print grammes, ' Perimena onoma parametrou'
            exit(0)
    elif katastash=='inouttk':
        leksi, katastash = lektikos()
        if katastash == 'anagnoristikotk':
			
			eisagwghEntityParametros(leksi,'inouttk')
			leksi, katastash = lektikos()
        else:
            print grammes, ' Perimena onoma parametrou'
            exit(0)
    else:
        print grammes, ' Perimena typo parametrou (in,inout)'
        exit(0)
    return leksi, katastash

def sequence(leksi, katastash):
    leksi, katastash = statement(leksi, katastash)
    
    while katastash == 'erwtimtk':
        leksi, katastash = lektikos()
        leksi, katastash = statement(leksi, katastash)
    return leksi, katastash

def bracketseq(leksi, katastash):
    if katastash=='aristeroaggtk':
        leksi, katastash = lektikos()
        leksi, katastash = sequence(leksi, katastash)
        if katastash=='deksiaaggtk':
            leksi, katastash = lektikos()
        else:
            print grammes, 'Perimena }'
            exit(0)
    else:
        print grammes, 'Perimena {'
        exit(0)
    return leksi, katastash

def brackorstat(leksi, katastash):
    if katastash=='aristeroaggtk':
        leksi, katastash = bracketseq(leksi, katastash)
    else:
	
        leksi, katastash = statement(leksi, katastash)
        if katastash=='erwtimtk':
            leksi, katastash = lektikos()
        else:
            print grammes, 'Perimena ;'
            exit(0)
    return leksi, katastash

def statement(leksi, katastash):
	if katastash=='anagnoristikotk':
		leksi, katastash = assignmentstat(leksi, katastash)
		return leksi, katastash 
	elif katastash=='iftk':
		leksi, katastash = ifstat(leksi, katastash)
		return leksi, katastash
	elif katastash=='dotk':
		leksi, katastash = dowhilestat(leksi, katastash)
		return leksi, katastash
	elif katastash=='whiletk':
		leksi, katastash = whilestat(leksi, katastash)
		return leksi, katastash
	elif katastash=='selecttk':
		leksi, katastash = selectstat(leksi, katastash)
		return leksi, katastash
	elif katastash=='exittk':
		leksi, katastash = exitstat(leksi, katastash)
		return leksi, katastash
	elif katastash=='returntk':
		leksi, katastash = returnstat(leksi, katastash)
		return leksi, katastash
	elif katastash=='printtk':
		leksi, katastash = printstat(leksi, katastash)
		return leksi, katastash
	elif katastash=='calltk':
		leksi, katastash = callstat(leksi, katastash)
		return leksi, katastash
	else:
		return leksi, katastash
		
def assignmentstat(leksi, katastash):
	
	anagnoristiko = leksi
	leksi, katastash = lektikos()
	if katastash=='ekxwrisitk':
		leksi, katastash = lektikos()
		leksi, katastash, place = expression(leksi, katastash)
		genquad(':=', place, '_', anagnoristiko)
		return leksi, katastash
	else:
		print grammes, 'Perimena :='
		exit(0)
		
def ifstat(leksi, katastash):
	leksi, katastash = lektikos()
	if katastash=='aristeripartk':
		leksi, katastash = lektikos()
		leksi, katastash, CTrue, CFalse = condition(leksi, katastash)
		if katastash=='deksiapartk':
			leksi, katastash = lektikos()
			
			z = nextquad()
			backpatch(CTrue, z)
			
			leksi, katastash = brackorstat(leksi, katastash)
			
			x=nextquad()
			jumplist=makelist(x)
			genquad('jump','_','_','_')
			
			z=nextquad()
			backpatch(CFalse, z)
			leksi, katastash = elsepart(leksi, katastash)
			
			
			z=nextquad()
			backpatch(jumplist,z)
			
			return leksi, katastash
		else:
			print grammes, 'Perimena )'
			exit(0)
	else:
		print grammes, 'Perimena ('
		exit(0)
		
def elsepart(leksi, katastash):
	if katastash=='elsetk':
		leksi, katastash = lektikos()
		leksi, katastash = brackorstat(leksi, katastash)
	return leksi, katastash
	
def whilestat(leksi, katastash):
	leksi, katastash = lektikos()
	if katastash=='aristeripartk':
		leksi, katastash = lektikos()
		
		startWhile=nextquad()
		
		leksi, katastash, CTrue, CFalse = condition(leksi, katastash)
		if katastash=='deksiapartk':
			leksi, katastash = lektikos()
			
			z = nextquad()
			backpatch(CTrue, z)
			
			leksi, katastash = brackorstat(leksi, katastash)
			
			genquad('jump','_','_',startWhile)
			z = nextquad()
			backpatch(CFalse, z)
			return leksi, katastash
		else:
			print grammes, 'Perimena )'
			exit(0)
	else:
		print grammes, 'Perimena ('
		exit(0)	
		
def selectstat(leksi, katastash):
	jumpL = emptylist()
	
	leksi, katastash = lektikos()
	if katastash=='aristeripartk':
		leksi, katastash = lektikos()
		if katastash=='anagnoristikotk':
			anagnoristiko = leksi
			leksi, katastash = lektikos()
			if katastash=='deksiapartk':
				leksi, katastash = lektikos()
				
				num=1
				while katastash=='arithmstatheratk':
					const=int(leksi)
					if num==const:
						
						list1=makelist(nextquad())
						genquad('<>',anagnoristiko,const,'_')
						num=num+1
						leksi, katastash = lektikos()
						if katastash=='anwkatwtk':
							leksi, katastash = lektikos()
							leksi, katastash = brackorstat(leksi, katastash)
							
							jump=makelist(nextquad())
							genquad('jump','_','_','_')
							backpatch(list1,nextquad())
							jumpL=merge(jumpL,jump)
							
						else:
							print grammes, 'Perimena :'
							exit(0)
					else:
						print grammes, 'Perimena ',num
						exit(0)
				if katastash=='defaulttk':
					leksi, katastash = lektikos()
					if katastash=='anwkatwtk':
						leksi, katastash = lektikos()
						leksi, katastash = brackorstat(leksi, katastash)
						
						backpatch(jumpL,nextquad())
						return leksi, katastash
					else:
						print grammes, 'Perimena :'
						exit(0)
				else:
					print grammes, 'Perimena default'
					exit(0)
			else:
				print grammes, 'Perimena )'
				exit(0)
		else:
			print grammes, 'Perimena anagnoristiko'
			exit(0)		
	else:
		print grammes, 'Perimena ('
		exit(0)
		
def dowhilestat(leksi, katastash):
	global exitList
	leksi, katastash = lektikos()
	
	arxikiExitList =  exitList
	
	exitList = emptylist()
	
	startDo=nextquad()
	
	leksi, katastash = brackorstat(leksi, katastash)
	
	
	if katastash=='whiletk':
		leksi, katastash = lektikos()
		if katastash=='aristeripartk':
			leksi, katastash = lektikos()
			leksi, katastash, CTrue, CFalse = condition(leksi, katastash)
			
			backpatch(CTrue, startDo)
			z = nextquad()
			backpatch(CFalse, z)
			backpatch(exitList, z)
			
			exitList = arxikiExitList
			
			if katastash=='deksiapartk':
				leksi, katastash = lektikos()

				return leksi, katastash
			else:
				print grammes, 'Perimena )'
				exit(0)
		else:
			print grammes, 'Perimena ('
			exit(0)	
	else:
		print grammes, 'Perimena while'
		exit(0)	
		
def exitstat(leksi, katastash):
	global exitList
	
	x=nextquad()
	lista = makelist(x)
	exitList = merge(exitList,lista)
	genquad('jump','_','_','_')
	
	leksi, katastash = lektikos()
	return leksi, katastash
	
def returnstat(leksi, katastash):
	global returnFlag
	
	returnFlag=True
	leksi, katastash = lektikos()
	if katastash=='aristeripartk':
		leksi, katastash = lektikos()
		leksi, katastash, place = expression(leksi, katastash)
		genquad('ret', place, '_', '_')
		if katastash=='deksiapartk':
			leksi, katastash = lektikos()
			return leksi, katastash
		else:
			print grammes, 'Perimena )'
			exit(0)
	else:
		print grammes, 'Perimena ('
		exit(0)
		
def printstat(leksi, katastash):
	leksi, katastash = lektikos()
	if katastash=='aristeripartk':
		leksi, katastash = lektikos()
		leksi, katastash, place = expression(leksi, katastash)
		genquad('out', place, '_', '_')
		if katastash=='deksiapartk':
			leksi, katastash = lektikos()
			return leksi, katastash
		else:
			print grammes, 'Perimena )'
			exit(0)
	else:
		print grammes, 'Perimena ('
		exit(0)
		
def callstat(leksi, katastash):
	leksi, katastash = lektikos()
	if katastash=='anagnoristikotk':
		onoma=leksi
		leksi, katastash = lektikos()
		leksi, katastash = actualpars(leksi, katastash)
		
		genquad('call',onoma,'_','_')
		return leksi, katastash
	else:
		print grammes, 'Perimena anagnoristiko'
		exit(0)
		
def actualpars(leksi, katastash):
    if katastash=='aristeripartk':
        leksi, katastash = lektikos()
        if katastash!='deksiapartk':
            leksi, katastash = actualparlist(leksi, katastash)
        
        if katastash=='deksiapartk':
            leksi, katastash = lektikos()
            return leksi, katastash
        else:
            print grammes, ' Perimena )'
            exit(0)
    else:
        print grammes, ' Perimena ('
        exit(0)

def actualparlist(leksi, katastash):
    leksi, katastash = actualparitem(leksi, katastash)
    while katastash=='komatk':
        leksi, katastash = lektikos()
        leksi, katastash = actualparitem(leksi, katastash)
    return leksi, katastash

def actualparitem(leksi, katastash):
    
    if katastash=='intk':
        leksi, katastash = lektikos()
        leksi, katastash, place = expression(leksi, katastash)
        
        
        genquad('par',place,'CV','_')
    elif katastash=='inouttk':
        leksi, katastash = lektikos()
        if katastash == 'anagnoristikotk':
			
			genquad('par',leksi,'REF','_')
			leksi, katastash = lektikos()
        else:
            print grammes, ' Perimena onoma parametrou'
            exit(0)
    else:
        print grammes, ' Perimena typo parametrou (in,inout)'
        exit(0)
    return leksi, katastash
    
def condition(leksi, katastash):
	leksi, katastash,BT1true,BT1false = boolterm(leksi, katastash)
	
	while katastash=='ortk':
		
		z=nextquad()
		backpatch(BT1false,z)
		
		leksi, katastash = lektikos()
		leksi, katastash,BT2true,BT2false = boolterm(leksi, katastash)
	
		BT1true = merge(BT1true,BT2true)
		BT1false = BT2false
		
	CTrue=BT1true
	CFalse=BT1false
	
	return leksi, katastash,CTrue,CFalse
	
def boolterm(leksi, katastash):
	leksi, katastash,BF1true,BF1false = boolfactor(leksi, katastash)
	
	while katastash=='andtk':
		leksi, katastash = lektikos()
		
		z=nextquad()
		backpatch(BF1true,z)
		
		leksi, katastash,BF2true,BF2false = boolfactor(leksi, katastash)
		
		BF1false=merge(BF1false,BF2false)
		BF1true=BF2true
		
	BTtrue=BF1true
	BTfalse=BF1false
	return leksi, katastash,BTtrue,BTfalse	

	
def boolfactor(leksi, katastash):	
	
	if katastash=='nottk':
		leksi, katastash = lektikos()
		if katastash=='aristeritetragonipartk':
			leksi, katastash = lektikos()
			leksi, katastash,CTrue, CFalse = condition(leksi, katastash)
			if katastash=='deksiatetragwnhpartk':
				leksi, katastash = lektikos()
				return leksi, katastash,CFalse,CTrue
			else:
				print grammes, ' Perimena ]'
				exit(0)
		else:
			print grammes, ' Perimena ['
			exit(0)
	elif katastash=='aristeritetragonipartk':
		leksi, katastash = lektikos()
		leksi, katastash,CTrue, CFalse = condition(leksi, katastash)
		if katastash=='deksiatetragwnhpartk':
			leksi, katastash = lektikos()
			return leksi, katastash, CTrue, CFalse
		else:
			print grammes, ' Perimena ]'
			exit(0)
	else:
		leksi, katastash, E1place = expression(leksi, katastash)
		if katastash=='isontk' or katastash=='mikroterotk' or katastash=='mikrisotk' or katastash=='diaforotk' or katastash=='megalisotk' or katastash=='megaliterotk':
			relop = leksi
			leksi, katastash = lektikos()
			leksi, katastash, E2place = expression(leksi, katastash)
			
			x=nextquad()
			BFtrue = makelist(x)
			genquad(relop, E1place, E2place,'_')
			
			x=nextquad()
			BFfalse=makelist(x)
			genquad('jump','_','_','_')
			
			
			return leksi, katastash, BFtrue, BFfalse
		else:
			print grammes, ' Perimena =,<,<=,<>,>=,>'
			exit(0)
			
def expression(leksi, katastash):
	if katastash=='sintk' or katastash=='miontk':
		leksi, katastash = lektikos()
	
	leksi, katastash, T1place = term(leksi, katastash)
	
	while katastash=='sintk' or katastash=='miontk':
                sinMion = leksi
                
		leksi, katastash = lektikos()
		leksi, katastash, T2place = term(leksi, katastash)
		
		w = newtemp()
		genquad(sinMion, T1place, T2place, w)
		T1place = w
		
	return leksi, katastash, T1place


def term(leksi, katastash):
	leksi, katastash, F1place = factor(leksi, katastash)
	while katastash=='epitk' or katastash=='diatk':
                epiDia = leksi
		leksi, katastash = lektikos()
		leksi, katastash, F2place = factor(leksi, katastash)
		
		w = newtemp()
		genquad(epiDia, F1place, F2place, w)
		F1place=w
		
	return leksi, katastash, F1place

def factor(leksi, katastash):
	if katastash=='arithmstatheratk':
                place = leksi
		leksi, katastash = lektikos()
		return leksi, katastash, place
	elif katastash=='aristeripartk':
		leksi, katastash = lektikos()
		leksi, katastash, place = expression(leksi, katastash)
		if katastash=='deksiapartk':
			leksi, katastash = lektikos()
			return leksi, katastash, place
		else:
			print grammes, 'Perimena )'
			exit(0)
	elif katastash=='anagnoristikotk':
		place = leksi
		leksi, katastash = lektikos()
		if katastash=='aristeripartk':
			leksi, katastash = idtail(leksi, katastash)
			onoma=place
			w=newtemp()
			genquad('par',w,'RET','_')
			genquad('call',onoma,'_','_')
			place=w
		return leksi, katastash, place
	else:
		print grammes, 'Perimena arithmhtikh stathera, ( h anagnoristiko'
		exit(0)
		
def idtail(leksi, katastash):
	if katastash=='aristeripartk':
		leksi, katastash = actualpars(leksi, katastash)
	return leksi, katastash


def nextquad():
    global tetrades
    return len(tetrades)+0
def newtemp():
	global proswrino
	global metavlhtes
	proswrino=proswrino+1
    
	leksi='T_'+str(proswrino)
	metavlhtes=metavlhtes+[leksi]
	eisagwghEntityMetavliti(leksi)
	return leksi

def genquad(op,x,y,z):
    global tetrades
    tetrades=tetrades + [[nextquad(),op,x,y,z]]

def emptylist():
    return []

def makelist(x):
    return [x]

def merge(l1,l2):
    return l1+l2

def backpatch(l1,z):
    global tetrades
    
    for i in range(len(l1)):
        for j  in range(len(tetrades)):
            if l1[i]==tetrades[j][0]:
                tetrades[j][4]=z
                break

def makeFiles():
	global metavlhtes
	for i in range(len(tetrades)):
		arxeioInt.write(str(tetrades[i])+'\n')

	arxeioC.write('#include <stdio.h>\n')	
	arxeioC.write('int main(){\n')
	
	for i in range(len(metavlhtes)):
		arxeioC.write('\tint '+metavlhtes[i]+';\n')
	for i in range(len(tetrades)):
		arxeioC.write('\tL_'+str(tetrades[i][0]) +': ')
		if tetrades[i][1]==':=':
			arxeioC.write(str(tetrades[i][4])+'='+str(tetrades[i][2]))
		if tetrades[i][1]=='+' or tetrades[i][1]=='/' or tetrades[i][1]=='*' or tetrades[i][1]=='-':
			arxeioC.write(str(tetrades[i][4])+'='+str(tetrades[i][2])+tetrades[i][1]+str(tetrades[i][3]))
		if tetrades[i][1]=='jump':
			arxeioC.write('goto L_'+str(tetrades[i][4]))
		if tetrades[i][1]=='<' or tetrades[i][1]=='<=' or tetrades[i][1]=='>=' or tetrades[i][1]=='>':
			arxeioC.write('if('+str(tetrades[i][2])+tetrades[i][1]+str(tetrades[i][3])+') goto L_'+str(tetrades[i][4]))
		if tetrades[i][1]=='<>':
			arxeioC.write('if('+str(tetrades[i][2])+'!='+str(tetrades[i][3])+') goto L_'+str(tetrades[i][4]))
		if tetrades[i][1]=='=':
			arxeioC.write('if('+str(tetrades[i][2])+'=='+str(tetrades[i][3])+') goto L_'+str(tetrades[i][4]))
		if tetrades[i][1]=='out':	
			arxeioC.write('printf("%d\\n",'+str(tetrades[i][2])+')')
		arxeioC.write(';\n')
	arxeioC.write('}\n')
	
def eisagwghScope(onoma):
	global pinakasSymvolwn
	global offset
	offset = 12 
	vathos = len(pinakasSymvolwn)
	pinakasSymvolwn = [[onoma,vathos,[]]]+pinakasSymvolwn
	
def diagrafhScope():
	global pinakasSymvolwn
	global offset
	printPinakaSymvolwn()
	
	pinakasSymvolwn = pinakasSymvolwn[1:len(pinakasSymvolwn)]
	
	if len(pinakasSymvolwn)>0:
		offset = 12
		listaEntities = pinakasSymvolwn[0][2]
		for i in range(len(listaEntities)):
			if len(listaEntities[i])<4:
				offset = offset + 4
			
		
def printPinakaSymvolwn():
	print 
	for i in range(len(pinakasSymvolwn)):
		print pinakasSymvolwn[i]
	print 
	
def eisagwghEntityMetavliti(onoma):
		global offset
		global pinakasSymvolwn
		
		pinakasSymvolwn[0][2] = pinakasSymvolwn[0][2]+[[onoma,offset]]
		offset=offset+4
		
def eisagwghEntityParametros(onoma,typos):
		global offset
		global pinakasSymvolwn
		
		pinakasSymvolwn[0][2] = pinakasSymvolwn[0][2]+[[onoma,offset,typos]]
		offset=offset+4
		
def eisagwghEntitySynarthshs(onoma,typos):
		global offset
		global pinakasSymvolwn
		
		pinakasSymvolwn[0][2] = pinakasSymvolwn[0][2]+[[onoma,typos,'_','_']]

def plhroforiaMetavlhths(onoma):
	global pinakasSymvolwn
	
	vathosTrexousas = len(pinakasSymvolwn)-1

	for i in range(len(pinakasSymvolwn)):
		for j in range(len(pinakasSymvolwn[i][2])):
				if pinakasSymvolwn[i][2][j][0]==onoma:
					if len(pinakasSymvolwn[i][2][j])==2:
						return i,pinakasSymvolwn[i][2][j][1],''
					elif len(pinakasSymvolwn[i][2])==3:
						return i,pinakasSymvolwn[i][2][j][1],pinakasSymvolwn[i][2][j][2]
					else:
						print 'H ' ,onoma, ' den einai metavlhth h parametros'
						exit(0)
				
	print 'Den vrethike h metavlhth ',onoma
	exit(0)
	
def gnlvcode(onoma):
	global pinakasSymvolwn
	
	vathosTrexousas = len(pinakasSymvolwn)-1
	
	for i in range(len(pinakasSymvolwn)):
		for j in range(len(pinakasSymvolwn[i][2])):
				if pinakasSymvolwn[i][2][0]==onoma:
					arxeioFinal.write('li $t0, -4($t0)\n')
					for k in range(vathosTrexousas-1-i):
						arxeioFinal.write('lw $t0, -4($t0)\n')
					offset = pinakasSymvolwn[i][2][1]
					arxeioFinal.write('add $t0, $t0, -'+str(offset)+'\n')
					return

def loadvr(v,r):
	v=str(v)
	r=str(r)
	vathosTrexousas = len(pinakasSymvolwn)-1
	if v[0]>='0' and v[0]<='9':
		arxeioFinal.write('li $t'+r+','+v+'\n')
	else:
		vathos,offset, typos = plhroforiaMetavlhths(v)
		offset = str(offset)
		if vathos == 0:
			arxeioFinal.write('lw $t'+r+',-'+offset+'($s0)\n')
		elif vathos == vathosTrexousas:
			if typos=='' or typos=='intk':
				arxeioFinal.write('lw $t'+r+',-'+offset+'($sp)\n')
			elif typos=='inouttk':
				arxeioFinal.write('lw $t0,-'+offset+'($sp)\n')
				arxeioFinal.write('lw $t'+r+',($t0)\n')
		elif vathos < vathosTrexousas:
			if typos=='' or typos=='intk':
				gnlvcode()
				arxeioFinal.write('lw $t'+r+',($t0)\n')
			elif typos=='inouttk':
				gnlvcode()
				arxeioFinal.write('lw $t0, ($t0)\n') 
				arxeioFinal.write('lw $t'+r+',($t0)\n')

def storerv(r,v):
	v=str(v)
	r=str(r)
	vathosTrexousas = len(pinakasSymvolwn)-1
	
	vathos,offset, typos = plhroforiaMetavlhths(v)
	offset = str(offset)
	if vathos == 0:
		arxeioFinal.write('sw $t'+r+',-'+offset+'($s0)\n')
	elif vathos == vathosTrexousas:
		if typos=='' or typos=='intk':
			arxeioFinal.write('sw $t'+r+',-'+offset+'($sp)\n')
		elif typos=='inouttk':
			arxeioFinal.write('lw $t0,-'+offset+'($sp)\n')
			arxeioFinal.write('sw $t'+r+',($t0)\n')
	elif vathos < vathosTrexousas:
		if typos=='' or typos=='intk':
			gnlvcode()
			arxeioFinal.write('sw $t'+r+',($t0)\n')
		elif typos=='inouttk':
			gnlvcode()
			arxeioFinal.write('lw $t0, ($t0)\n') 
			arxeioFinal.write('sw $t'+r+',($t0)\n')
			
def intFinal():
	
	global tetrades
	
	for i in range(len(tetrades)):
		arxeioFinal.write('\tL_'+str(tetrades[i][0]) +': ')
		if tetrades[i][1]==':=':
			loadvr(tetrades[i][2],1)
			storerv(1,tetrades[i][4])
		if tetrades[i][1]=='+' or tetrades[i][1]=='/' or tetrades[i][1]=='*' or tetrades[i][1]=='-':
			loadvr(tetrades[i][2],1)
			loadvr(tetrades[i][3],2)
			if tetrades[i][1]=='+':
				op='add'
			elif tetrades[i][1]=='/':
				op='div'
			elif tetrades[i][1]=='*':
				op='mul'
			else:
				op='sub'
			arxeioFinal.write(op+' $t1, $t1, $t2\n')
			storerv(1,tetrades[i][4])
			
		if tetrades[i][1]=='jump':
			arxeioFinal.write('j L_'+str(tetrades[i][4]))
		if tetrades[i][1]=='<' or tetrades[i][1]=='<=' or tetrades[i][1]=='>=' or tetrades[i][1]=='>' or tetrades[i][1]=='<>' or tetrades[i][1]=='=':
			loadvr(tetrades[i][2],1)
			loadvr(tetrades[i][3],2)
			if tetrades[i][1]=='<':
				op='blt'
			elif tetrades[i][1]=='<=':
				op='ble'
			elif tetrades[i][1]=='=':
				op='beq'
			elif tetrades[i][1]=='>':
				op='bgt'
			elif tetrades[i][1]=='>=':
				op='bge'
			else:
				op='bne'
			arxeioFinal.write(op+' $t1, $t1, L'+str(tetrades[i][4])+'\n')
		if tetrades[i][1]=='out':	
			arxeioFinal.write('printf("%d\\n",'+str(tetrades[i][2])+')')
		arxeioC.write('\n')

	tetrades=[]
	
synt()

for i in range(len(tetrades)):
    print tetrades[i]
print metavlhtes

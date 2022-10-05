import datetime
from django.contrib import messages
from django.shortcuts import redirect, render
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.yui import BarChart
from . import model


def home(request):
        return render(request,'home.html')

def createPA(request):

    if request.method == 'POST' and request.POST.get('secteurs',False):
        nomPA = request.POST["secteurs"]
        lastNbPA = model.PA.Find_Last_nbPA(nomPA)
        try:
            lastNbPA=lastNbPA[0]+1
        except:
            lastNbPA =1
        parts = model.User.Find_All()
        return render(request,'addNewPA.html',{"sect":nomPA,"lastNbPA":lastNbPA,"parts":parts})
    elif request.method == 'POST':
        sects = model.Secteur.Find_All()
        return render(request,'addNewPA.html',{"sects":sects})
    else:
        return redirect('home')

def PAE(request):
    if request.method == 'POST':
        p=model.PA()
        p.nomPA = request.POST["sects"]
        p.nbPA = request.POST["nbPA"]
        p.piloteImm = request.session["user"]["Immatricule"]
        p.secteurPA = request.POST["sects"]
        #For appending participants
        for i in model.User.Find_All_id():
            if request.POST.get("part"+str(i),False):
                p.participants.append(int(request.POST["part"+str(i)]))
        #For appending checkers
        for i in model.User.Find_All_id():
            if request.POST.get("C"+str(i),False):
                p.C.append(int(request.POST["C"+str(i)]))
        #For appending actors
        for i in model.User.Find_All_id():
            if request.POST.get("A"+str(i),False):
                p.A.append(int(request.POST["A"+str(i)]))
        model.PA.Insert(p)
        p.idPA=model.PA.Find_id(p.nomPA,p.nbPA,p.pagePA)
        return render(request,'created.html',{"idPA":p.idPA})
    else:
        return redirect('home')

def createProblem(request):
    if request.method=='POST' and not(request.POST.get("cr",False)):
        idAxe = request.POST["idAxe"]
        idPA = request.POST["idPA"]
        criticity=[1,2,3]
        try:
           nbprob=model.Problem.Count_By_idAxe(idAxe)+1
        except:
            nbprob=1
        return render(request,'addNewProblem.html',{"idAxe":idAxe,"idPA":idPA,"crList":criticity,"nbProb":nbprob})
    elif request.method=='POST': 
        p=model.Problem()               
        p.idAxe = request.POST["idAxe"]
        idPA = request.POST["idPA"]
        p.nbProb = request.POST["nbProb"]
        p.descriptionProb = inputReformat(request.POST["descriptionProb"])
        p.cr = request.POST["cr"]
        model.Problem.Insert(p)
        return render(request,'created.html',{"idPA":idPA})
    else:
        return redirect('home')

def createAxe(request):
    if request.method=='POST' and not(request.POST.get("indicateur",False)):
        idPA = request.POST["idPA"]
        try:
           nbAxe=model.Axe.Count_By_idPA(idPA)+1
        except:
            nbAxe=1
        return render(request,'addNewAxe.html',{"idPA":idPA,"nbAxe":nbAxe})
    elif request.method=='POST': 
        p=model.Axe()               
        p.idPA = request.POST["idPA"]
        p.nbAxe = request.POST["nbAxe"]
        p.indicateur = inputReformat(request.POST["indicateur"])
        model.Axe.Insert(p)
        return render(request,'created.html',{"idPA":p.idPA})
    else:
        return redirect('home')

def createAction(request):
    if request.method=='POST' and not(request.POST.get("actionAct",False)):
        idProb = request.POST["idProb"]
        idPA = request.POST["idPA"]
        try:
            nbAct=model.Action.Count_By_idProb(idProb)+1
        except:
            nbAct=1
        resps = model.User.Find_All()
        return render(request,'addNewAction.html',{"idProb":idProb,"idPA":idPA,"nbAct":nbAct,"resps":resps})
    elif request.method=='POST': 
        p=model.Action()    
        idPA=request.POST["idPA"]           
        p.idProb = request.POST["idProb"]
        p.nbAct = request.POST["nbAct"]
        p.cause = inputReformat(request.POST["causeAct"])
        p.action = inputReformat(request.POST["actionAct"])
        p.resp=[]
        for i in model.User.Find_All_id():
            if request.POST.get("resp"+str(i)):
                p.resp.append(int(request.POST["resp"+str(i)]))
        p.datePrevue=request.POST["datePrevue"]
        print(p.datePrevue)
        if request.POST.get('P',False):
            p.P=True
        else:
            p.P=False
        p.D,p.C,p.A=False,False,False
        if len(p.resp)==0:
            planified=p.P  
            resps = model.User.Find_All()
            messages.error(request,'Vous devez sélectionner au minimum 1 personne pour être responsable d\'action!')
            return render(request,'addNewAction.html',{"idProb":p.idProb,"idPA":idPA,"nbAct":p.nbAct,"selectedResps":p.resp,"cause":p.cause,"action":p.action,"planified":planified,"resps":resps,"dtpr":p.datePrevue})
        
        if len(p.resp)>2:
            planified=p.P  
            resps = model.User.Find_All()
            messages.error(request,'Vous devez sélectionner au maximum 2 personnes pour responsable d\'action!')
            return render(request,'addNewAction.html',{"idProb":p.idProb,"idPA":idPA,"nbAct":p.nbAct,"selectedResps":p.resp,"cause":p.cause,"action":p.action,"planified":planified,"resps":resps,"dtpr":p.datePrevue})
        
        if datetime.datetime.strptime(p.datePrevue, '%Y-%m-%d').date() <= datetime.date.today():
            planified=p.P  
            resps = model.User.Find_All()
            messages.error(request,'La date prévue doit être supérieur à la date actuelle!')
            return render(request,'addNewAction.html',{"idProb":p.idProb,"idPA":idPA,"nbAct":p.nbAct,"selectedResps":p.resp,"cause":p.cause,"action":p.action,"planified":planified,"resps":resps,"dtpr":p.datePrevue})
        
        model.Action.Insert(p)
        return render(request,'created.html',{"idPA":idPA})
    else:
        return redirect('home')

def consult(request):
    if request.method == 'POST' and (request.POST.get("idPA",False)):
        idPA=request.POST["idPA"]
        respFilter="tous"
        pa=model.PA.Find_By_idPA(str(idPA))
        parts=""
        if pa.participants is not None:
            for i in pa.participants:
                try:
                    parts+=model.User.FindById(i)+','
                except:
                    parts=parts
            parts = parts[:-1]
        Cs=""
        if pa.C is not None:
            for i in pa.C:
                try:
                    Cs+=model.User.FindById(i)+','
                except:
                    Cs=Cs
            Cs = Cs[:-1]
        As=""
        if pa.A is not None:
            for i in pa.A:
                try:
                    As+=model.User.FindById(i)+','
                except:
                    As=As
            As = As[:-1]
        pilote=model.User.FindById(pa.piloteImm)
        axes = model.Axe.Find_All_By_idPA(pa.idPA)
        axeAndProbAndActions=[]
        for axe in axes:
            probs=model.Problem.Find_All_By_idAxe(axe.idAxe)
            probAndActions=[]
            sums=0
            for prob in probs:
                actions=model.Action.Find_All_By_idProb(prob.idProb)
                sums+=len(actions)
                probAndActions.append([prob,len(actions)+2,len(actions)+1,actions])
            axeAndProbAndActions.append([axe,len(probs)+sums+2,probAndActions])
        dict={"pa":pa,"parts":parts,"pilote":pilote,"axeAndProbAndActions":axeAndProbAndActions,"Cs":Cs,"As":As,"respFilter":respFilter}
        return render(request,'PAE.html',dict)
    elif request.method == 'POST' and ((request.POST.get("pagePA",False)) and (request.POST.get("nbPA",False))) and request.POST.get("respFilter",False):
        nomPA = request.POST["sects"]
        nbPA = request.POST["nbPA"]
        page= request.POST["pagePA"]
        respFilter=request.POST["respFilter"]
        userImm=request.session["user"]["Immatricule"]
        idPA=model.PA.Find_id(nomPA,nbPA,page)
        pa=model.PA.Find_By_idPA(str(idPA))
        parts=""
        if pa.participants is not None:
            for i in pa.participants:
                parts+=model.User.FindById(i)+','
            parts = parts[:-1]
        Cs=""
        if pa.C is not None:
            for i in pa.C:
                try:
                    Cs+=model.User.FindById(i)+','
                except:
                    Cs=Cs
            Cs = Cs[:-1]
        As=""
        if pa.A is not None:
            for i in pa.A:
                try:
                    As+=model.User.FindById(i)+','
                except:
                    As=As
            As = As[:-1]
        pilote=model.User.FindById(pa.piloteImm)
        axes = model.Axe.Find_All_By_idPA(pa.idPA)
        axeAndProbAndActions=[]
        for axe in axes:
            probs=model.Problem.Find_All_By_idAxe(axe.idAxe)
            probAndActions=[]
            sums=0
            for prob in probs:
                if respFilter=="miennes":
                    actions=model.Action.Find_All_By_idProb_and_userImm(prob.idProb,userImm)
                    if len(actions)!=0:
                        sums+=len(actions)
                        probAndActions.append([prob,len(actions)+2,len(actions)+1,actions])
                else:
                    actions=model.Action.Find_All_By_idProb(prob.idProb)
                    sums+=len(actions)
                    probAndActions.append([prob,len(actions)+2,len(actions)+1,actions])
            if len(probAndActions)!=0 or respFilter=="tous":
                axeAndProbAndActions.append([axe,len(probs)+sums+2,probAndActions])
        dict={"pa":pa,"parts":parts,"pilote":pilote,"axeAndProbAndActions":axeAndProbAndActions,"Cs":Cs,"As":As,"respFilter":respFilter}
        return render(request,'PAE.html',dict)
    elif request.method == 'POST' and (request.POST.get("nbPA",False)):
        nomPA = request.POST["sects"]
        nbPA = request.POST["nbPA"]
        page=model.PA.Find_Last_pagePA(nomPA,nbPA)+1
        pagePA=[]
        for i in range(1,page):
            pagePA.append(i)
        return render(request,'ConsultForm.html',{"sect":nomPA,"nb":nbPA,"pagePA":pagePA})
    elif request.method == 'POST' and request.POST.get("secteurs",False):
        nomPA = request.POST["secteurs"]
        lastNbPA = model.PA.Find_Last_nbPA(nomPA)
        try:
            lastNbPA=lastNbPA[0]+1
        except:
            err="Pas de PA dans ce secteur! Sélectionner un autre secteur ou créer un PA"
            sects = model.PA.Find_All_Sects()
            return render(request,'ConsultForm.html',{"sects":sects,"error":err})
        NbPA=[]
        for i in range(1,lastNbPA):
            NbPA.append(i)
        return render(request,'ConsultForm.html',{"sect":nomPA,"NbPA":NbPA})
    elif request.method == 'POST':
        sects = model.PA.Find_All_Sects()
        return render(request,'ConsultForm.html',{"sects":sects})
    else:
        return redirect('home')

def addPage(request):
    if request.method == 'POST':
        p=model.PA.Find_By_idPA(str(request.POST["idPA"]))
        p.pagePA=int(p.pagePA)+1
        p.piloteImm=int(p.piloteImm)
        p.nbRev=int(p.nbRev)
        p.nbPA=int(p.nbPA)
        model.PA.Insert(p)
        p.idPA=model.PA.Find_id(p.nomPA,p.nbPA,p.pagePA)
        return render(request,'created.html',{"idPA":p.idPA})
    else:
        return redirect('home')

def updateP(request):
    if request.method == 'POST':
        idAct = request.POST["idAct"]
        idPA = request.POST["idPA"]
        if request.POST.get('P',False):
            P=True
        else:
            P=False
        act=model.Action.Find_By_id(idAct)
        if act.D==True and P==False:
            messages.error(request,'Can\'t displanified a done action')
            dict={"idPA":idPA}
            return render(request,"created.html",dict)
        elif act.D==False and P==False:
            model.Action.Update_P(idAct,P)
            messages.success(request,'Action unplanified successfully!')
            dict={"idPA":idPA}
            return render(request,"created.html",dict)
        else:
            model.Action.Update_P(idAct,P)
            messages.success(request,'Action planified successfully!')
            dict={"idPA":idPA}
            return render(request,"created.html",dict)
    else:
        return redirect('home')

def updateD(request):
    if request.method == 'POST':
        if request.POST.get("idPA",False):
            idAct = request.POST["idAct"]
            idPA = request.POST["idPA"]
            if request.POST.get('D',False):
                D=True
            else:
                D=False
            act=model.Action.Find_By_id(idAct)
            if act.P==False and D==True:
                messages.error(request,'Can\'t do not planified action!')
                dict={"idPA":idPA}
                return render(request,"created.html",dict)
            if act.C==True and D==False and act.P==True:
                messages.error(request,'Can\'t undone a checked action')
                dict={"idPA":idPA}
                return render(request,"created.html",dict)
            elif act.C==False and D==False and act.P==True:
                model.Action.Update_D(idAct,D)
                messages.success(request,'Action undone successfully!')
                dateDone=None
                model.Action.Update_dateDone(dateDone,idAct)
                dict={"idPA":idPA}
                return render(request,"created.html",dict)
            else:
                model.Action.Update_D(idAct,D)
                messages.success(request,'Action done successfully!')
                dateDone=datetime.date.today()
                model.Action.Update_dateDone(dateDone,idAct)
                dict={"idPA":idPA}
                return render(request,"created.html",dict)
        elif request.POST.get("AllAct",False):
            idAct = request.POST["idAct"]
            if request.POST.get('D',False):
                D=True
            else:
                D=False
            act=model.Action.Find_By_id(idAct)
            if act.P==False and D==True:
                messages.error(request,'Can\'t do not planified action!')
                return render(request,'UpdatedRedirectToConsultAll.html')
            if act.C==True and D==False and act.P==True:
                messages.error(request,'Can\'t undone a checked action')
                return render(request,'UpdatedRedirectToConsultAll.html')
            elif act.C==False and D==False and act.P==True:
                model.Action.Update_D(idAct,D)
                messages.success(request,'Action undone successfully!')
                dateDone=None
                model.Action.Update_dateDone(dateDone,idAct)
                return render(request,'UpdatedRedirectToConsultAll.html')
            else:
                model.Action.Update_D(idAct,D)
                messages.success(request,'Action done successfully!')
                dateDone=datetime.date.today()
                model.Action.Update_dateDone(dateDone,idAct)
                return render(request,'UpdatedRedirectToConsultAll.html')
    else:
        return redirect('home')

def updateC(request):
    if request.method == 'POST':
        if request.POST.get("idPA",False):
            idAct = request.POST["idAct"]
            idPA = request.POST["idPA"]
            if request.POST.get('C',False):
                C=True
            else:
                C=False
            act=model.Action.Find_By_id(idAct)
            if act.D==False and C==True:
                messages.error(request,'Can\'t check not done action!')
                dict={"idPA":idPA}
                return render(request,"created.html",dict)
            if act.A==True and C==False and act.D==True:
                messages.error(request,'Can\'t uncheck an acted action')
                dict={"idPA":idPA}
                return render(request,"created.html",dict)
            elif act.A==False and C==False and act.D==True:
                model.Action.Update_C(idAct,C)
                messages.success(request,'Action unchecked successfully!')
                dateCloture=None
                model.Action.Update_dateCloture(dateCloture,idAct)
                dict={"idPA":idPA}
                return render(request,"created.html",dict)
            else:
                model.Action.Update_C(idAct,C)
                messages.success(request,'Action checked successfully!')
                dateCloture=datetime.date.today()
                model.Action.Update_dateCloture(dateCloture,idAct)
                dict={"idPA":idPA}
                return render(request,"created.html",dict)
        elif request.POST.get("AllAct",False):
            idAct = request.POST["idAct"]
            if request.POST.get('C',False):
                C=True
            else:
                C=False
            act=model.Action.Find_By_id(idAct)
            if act.D==False and C==True:
                messages.error(request,'Can\'t check not done action!')
                return render(request,'UpdatedRedirectToConsultAll.html')
            if act.A==True and C==False and act.D==True:
                messages.error(request,'Can\'t uncheck an acted action')
                return render(request,'UpdatedRedirectToConsultAll.html')
            elif act.A==False and C==False and act.D==True:
                model.Action.Update_C(idAct,C)
                messages.success(request,'Action unchecked successfully!')
                dateCloture=None
                model.Action.Update_dateCloture(dateCloture,idAct)
                return render(request,'UpdatedRedirectToConsultAll.html')
            else:
                model.Action.Update_C(idAct,C)
                messages.success(request,'Action checked successfully!')
                dateCloture=datetime.date.today()
                model.Action.Update_dateCloture(dateCloture,idAct)
                return render(request,'UpdatedRedirectToConsultAll.html')

    else:
        return redirect('home')

def updateA(request):
    if request.method == 'POST':
        if request.POST.get("idPA",False):
            idAct = request.POST["idAct"]
            idPA = request.POST["idPA"]
            if request.POST.get('A',False):
                A=True
            else:
                A=False
            act=model.Action.Find_By_id(idAct)
            if act.C==False and A==True:
                messages.error(request,'Can\'t Act not checked action!')
                dict={"idPA":idPA}
                return render(request,"created.html",dict)
            elif act.C==True and A==True:
                model.Action.Update_A(idAct,A)
                messages.success(request,'Action acted successfully!')
                dict={"idPA":idPA}
                return render(request,"created.html",dict)
            else:
                messages.success(request,'Action unacted successfully!')
                model.Action.Update_A(idAct,A)
                dict={"idPA":idPA}
                return render(request,"created.html",dict)
        elif request.POST.get("AllAct",False):
            idAct = request.POST["idAct"]
            if request.POST.get('A',False):
                A=True
            else:
                A=False
            act=model.Action.Find_By_id(idAct)
            if act.C==False and A==True:
                messages.error(request,'Can\'t Act not checked action!')
                return render(request,'UpdatedRedirectToConsultAll.html')
            elif act.C==True and A==True:
                messages.success(request,'Action unacted successfully!')
                return render(request,'UpdatedRedirectToConsultAll.html')
            else:
                model.Action.Update_A(idAct,A)
                messages.success(request,'Action acted successfully!')                
                return render(request,'UpdatedRedirectToConsultAll.html')
    else:
        return redirect('home')

def login(request):
    if request.method == 'POST':
        imm=request.POST['immatricule']
        pwd=str(request.POST['pwd'])
        user=model.User()
        user.Immatricule=int(imm)
        user.pwd=pwd
        
        if not user.Check_Imm():
            messages.error(request,'Invalid Immaricule!')
            dict={}
            return render(request,'login.html',dict)
        
        if not user.Check_Password():
            messages.error(request,'Invalid Password!')
            dict={}
            return render(request,'login.html',dict)
        messages.success(request,'Logged in successfully!')
        user=user.getUser()
        request.session['user']=user.serialize()
        result=model.PA.Find_All()
        if result==[]:
            noPA = True
        else:
            noPA = False
        request.session['noPA']=noPA
        return redirect('home')
            
    else:
        dict={}
        return render(request,'login.html',dict)

def logout(request):
    try:
        del request.session['user']
    except:
        messages.error(request,'Logged out unsuccessfully!')
        return redirect('home')
    messages.error(request,'Logged out successfully!')
    return redirect('home')

def rev(request):
    if request.method == 'POST':
        if request.POST.get('rev1'):
            idPA=request.POST['idPA']
            messages.success(request,str(model.PA.percentage(idPA))+'%')
            model.PA.update_rev(1,idPA)
            dict={"idPA":idPA}
            return render(request,"created.html",dict)       
        elif request.POST.get('rev2'):
            idPA=request.POST['idPA']
            messages.success(request,str(model.PA.percentage(idPA))+'%')
            model.PA.update_rev(2,idPA)
            dict={"idPA":idPA}
            return render(request,"created.html",dict) 
        elif request.POST.get('rev3'):
            idPA=request.POST['idPA']
            messages.success(request,str(model.PA.percentage(idPA))+'%')
            model.PA.update_rev(3,idPA)
            dict={"idPA":idPA}
            return render(request,"created.html",dict) 
        elif request.POST.get('rev4'):
            idPA=request.POST['idPA']
            messages.success(request,str(model.PA.percentage(idPA))+'%')
            model.PA.update_rev(4,idPA)
            dict={"idPA":idPA}
            return render(request,"created.html",dict) 
    else:
        return redirect('home')

def modificateParticipants(request):
        #this if to get the post request from the modificateParticpants.html
    if request.method == 'POST' and request.POST.get("idPA1",False):
        idPA=request.POST["idPA1"]
        pa=model.PA.Find_By_idPA(idPA)
        parts=[]
        for i in model.User.Find_All_id():
            if request.POST.get("part"+str(i)):
                parts.append(int(request.POST["part"+str(i)]))
        pa.participants=parts
        model.PA.UpdateParticipants(pa)
        return render(request,'created.html',{"idPA":pa.idPA})
        #this elif to get the post request from the PAE.html
    elif request.method == 'POST' and request.POST.get("idPA",False):
        idPA=request.POST["idPA"]
        pa=model.PA.Find_By_idPA(idPA)
        users=model.User.Find_All_id()
        dict={"pa":pa,"users":users}
        return render(request,'modificateParticipants.html',dict)
    else:
        return redirect('home')

def modificateAxe(request):
      #this if to get the post request from the modificateAxe.html
    if request.method == 'POST' and request.POST.get("idPA1",False):
        idPA=request.POST["idPA1"]
        idAxe=request.POST["idAxe"]
        indicateur=inputReformat(request.POST["indicateur"])
        axe=model.Axe.Find_By_idAxe(idAxe)
        axe.indicateur=indicateur
        model.Axe.UpdateAxe(axe)
        return render(request,'created.html',{"idPA":idPA})
        #this elif to get the post request from the PAE.html
    elif request.method == 'POST' and request.POST.get("idPA",False):
        idPA=request.POST["idPA"]
        idAxe=request.POST["idAxe"]
        axe=model.Axe.Find_By_idAxe(idAxe)
        axe.indicateur=outputReformat(axe.indicateur)
        dict={"axe":axe,"idPA":idPA}
        return render(request,'modificateAXe.html',dict)
    else:
        return redirect('home')

def modificateProblem(request):
      #this if to get the post request from the modificateProblem.html
    if request.method == 'POST' and request.POST.get("idPA1",False):
        idPA=request.POST["idPA1"]
        idProb=request.POST["idProb"]
        desc=inputReformat(request.POST["probDesc"])
        cr=int(request.POST["cr"])
        prob=model.Problem.Find_By_idProb(idProb)
        prob.descriptionProb=desc
        prob.cr=cr
        model.Problem.UpdateProblem(prob)
        return render(request,'created.html',{"idPA":idPA})
        #this elif to get the post request from the PAE.html
    elif request.method == 'POST' and request.POST.get("idPA",False):
        idPA=request.POST["idPA"]
        idProb=request.POST["idProb"]
        l=[1,2,3]
        prob=model.Problem.Find_By_idProb(idProb)
        prob.descriptionProb=outputReformat(prob.descriptionProb)
        dict={"prob":prob,"idPA":idPA,"crList":l}
        return render(request,'modificateProblem.html',dict)
    else:
        return redirect('home')

def modificateAction(request):
      #this if to get the post request from the modificateProblem.html
    if request.method == 'POST' and request.POST.get("idPA1",False):
        idPA=request.POST["idPA1"]
        idAct=request.POST["idAct"]
        act=model.Action.Find_By_idAct(idAct)
        act.cause=inputReformat(request.POST["cause"])
        act.action=inputReformat(request.POST["action"])
        act.resp=[]
        for i in model.User.Find_All_id():
            if request.POST.get("resp"+str(i)):
                act.resp.append(int(request.POST["resp"+str(i)]))
        if len(act.resp)==0:
            users = model.User.Find_All_id()
            act.datePrevue=str(act.datePrevue)
            messages.error(request,'Vous devez sélectionner au minimum 1 personne pour être responsable d\'action!')
            act.cause=outputReformat(act.cause)
            act.action=outputReformat(act.action)
            dict={"act":act,"idPA":idPA,"users":users}
            return render(request,'modificateAction.html',dict)
        if len(act.resp)>2:
            users = model.User.Find_All_id()
            act.datePrevue=str(act.datePrevue)
            messages.error(request,'Vous devez sélectionner au maximum 2 personnes pour responsable d\'action!')
            act.cause=outputReformat(act.cause)
            act.action=outputReformat(act.action)
            dict={"act":act,"idPA":idPA,"users":users}
            return render(request,'modificateAction.html',dict)
        datePrevue=request.POST["datePrevue"]
        if datetime.datetime.strptime(datePrevue, '%Y-%m-%d').date() <= datetime.date.today():
            users = model.User.Find_All_id()
            act.datePrevue=str(act.datePrevue)
            messages.error(request,'La date prévue doit être supérieur à la date actuelle!')
            act.cause=outputReformat(act.cause)
            act.action=outputReformat(act.action)
            dict={"act":act,"idPA":idPA,"users":users}
            return render(request,'modificateAction.html',dict)
        act.datePrevue=datePrevue
        model.Action.UpdateAction(act)
        return render(request,'created.html',{"idPA":idPA})
        #this elif to get the post request from the PAE.html
    elif request.method == 'POST' and request.POST.get("idPA",False):
        idPA=request.POST["idPA"]
        idAct=request.POST["idAct"]
        act=model.Action.Find_By_idAct(idAct)
        users=model.User.Find_All_id()
        act.datePrevue=str(act.datePrevue)
        act.cause=outputReformat(act.cause)
        act.action=outputReformat(act.action)
        dict={"act":act,"idPA":idPA,"users":users}
        return render(request,'modificateAction.html',dict)
    else:
        return redirect('home')

def consultUsers(request):
    if request.method == 'POST':
        users=model.User.Find_All()
        dict={"users":users}
        return render(request,'users.html',dict)
    else:
        return redirect('home')

def deleteUser(request):
    if request.method == 'POST':
        imm=int(request.POST["Immatricule"])
        model.User.DeleteUser(imm)
        messages.success(request,'Utilisateur supprimée avec succès!')
        return render(request,'createdUser.html')
    else:
        return redirect('home')

def createUser(request):
    if request.method == 'POST' and request.POST.get("immatricule",False):
        user=model.User()
        user.Immatricule=int(request.POST["immatricule"])
        user.FirstName=inputReformat(request.POST["FirstName"])
        user.LastName=inputReformat(request.POST["LastName"])
        user.pwd=request.POST["pwd"]
        if user.Immatricule in model.User.Find_All_id():
            messages.error(request,'Cet Immatricule existe déjà!')
            dict={"user":user}
            return render(request,'createUser.html',dict)
        model.User.createUser(user)
        messages.success(request,'Utilisateur crée avec succès!')
        return render(request,'createdUser.html')
    elif request.method == 'POST':
        dict={}
        return render(request,'createUser.html',dict)
    else:
        return redirect('home')

def modificateUser(request):
    if request.method == 'POST' and request.POST.get("FirstName",False):
        lastImm=request.POST["lastImmatricule"]
        imm=request.POST["immatricule"]
        if int(imm) != int(lastImm) :
            if int(imm) in model.User.Find_All_id():
                messages.error(request,'Cet Immatricule existe déjà!')
                user=model.User.FindByIdImm(lastImm)
                dict={"user":user}
                return render(request,'modificateUser.html',dict)
            else:
                user=model.User.FindByIdImm(lastImm)
                user.Immatricule=imm
                user.FirstName=inputReformat(request.POST["FirstName"])
                user.LastName=inputReformat(request.POST["LastName"])
                user.pwd=request.POST["pwd"]
                model.User.createUser(user)
                model.User.UpdateUserInPA_Axe_Prob_Act(lastImm,imm)
                model.User.DeleteUser(lastImm)
                return render(request,'createdUser.html')
        else:
            user=model.User.FindByIdImm(lastImm)
            user.Immatricule=imm
            user.FirstName=inputReformat(request.POST["FirstName"])
            user.LastName=inputReformat(request.POST["LastName"])
            user.pwd=request.POST["pwd"]
            model.User.UpdateUser(user,lastImm)
            return render(request,'createdUser.html')
    elif request.method == 'POST':
        imm=request.POST["Immatricule"]
        user=model.User.FindByIdImm(imm)
        dict={"user":user}
        return render(request,'modificateUser.html',dict)
    else:
        return redirect('home')

def consultSecters(request):
    if request.method == 'POST':
        sects=model.Secteur.Find_All_Sects()
        dict={"sects":sects}
        return render(request,'secters.html',dict)
    else:
        return redirect('home')

def modificateSecter(request):
    if request.method == 'POST' and request.POST.get("nameSecLast",False):
        sec=inputReformat(request.POST["nameSec"])
        lastSec=inputReformat(request.POST["nameSecLast"])
        model.Secteur.Update(sec,lastSec)
        messages.success(request,'Secteur modifié avec succès!')
        return render(request,'createdSecter.html')
    elif request.method == 'POST':
        sec=request.POST["nameSec"]
        dict={"sect":sec}
        return render(request,'modificateSecter.html',dict)
    else:
        return redirect('home')

def deleteSecter(request):
    if request.method == 'POST':
        nameSec=request.POST["nameSec"]
        try:
            model.Secteur.delete(inputReformat(nameSec))
        except:
            messages.error(request,'Secteur ne peut pas être supprimé! Ce secteur est utilisé dans un ou plusieurs Plan d\'action(s)!')
            sects=model.Secteur.Find_All_Sects()
            dict={"sects":sects}
            return render(request,'secters.html',dict)
        messages.success(request,'Secteur supprimée avec succès!')
        return render(request,'createdSecter.html')
    else:
        return redirect('home')

def createSecter(request):
    if request.method == 'POST' and request.POST.get("nameSec",False):
        nameSec=request.POST["nameSec"]
        try:
           model.Secteur.insert(inputReformat(nameSec))
        except:
            messages.error(request,'Secteur existe déjà!')
            sects=model.Secteur.Find_All_Sects()
            dict={"sects":sects}
            return render(request,'secters.html',dict)
        messages.success(request,'Secteur crée avec succès!')
        return render(request,'createdSecter.html')
    elif request.method == 'POST':
        return render(request,'createSecter.html')
    else:
        return redirect('home')

def modificateCheckers(request):
        #this if to get the post request from the modificateParticpants.html
    if request.method == 'POST' and request.POST.get("idPA1",False):
        idPA=request.POST["idPA1"]
        pa=model.PA.Find_By_idPA(idPA)
        C=[]
        for i in model.User.Find_All_id():
            if request.POST.get("C"+str(i)):
                C.append(int(request.POST["C"+str(i)]))
        pa.C=C
        model.PA.UpdateCheckers(pa)
        return render(request,'created.html',{"idPA":pa.idPA})
        #this elif to get the post request from the PAE.html
    elif request.method == 'POST' and request.POST.get("idPA",False):
        idPA=request.POST["idPA"]
        pa=model.PA.Find_By_idPA(idPA)
        users=model.User.Find_All_id()
        dict={"pa":pa,"users":users}
        return render(request,'modificateCheckers.html',dict)
    else:
        return redirect('home')

def modificateActors(request):
        #this if to get the post request from the modificateParticpants.html
    if request.method == 'POST' and request.POST.get("idPA1",False):
        idPA=request.POST["idPA1"]
        pa=model.PA.Find_By_idPA(idPA)
        A=[]
        for i in model.User.Find_All_id():
            if request.POST.get("A"+str(i)):
                A.append(int(request.POST["A"+str(i)]))
        pa.A=A
        model.PA.UpdateActors(pa)
        return render(request,'created.html',{"idPA":pa.idPA})
        #this elif to get the post request from the PAE.html
    elif request.method == 'POST' and request.POST.get("idPA",False):
        idPA=request.POST["idPA"]
        pa=model.PA.Find_By_idPA(idPA)
        users=model.User.Find_All_id()
        dict={"pa":pa,"users":users}
        return render(request,'modificateActors.html',dict)
    else:
        return redirect('home')

def dashboard(request):
    if request.method == 'POST':
        sect=request.POST["secteurs"]
        period=request.POST.get("periode",False)
        allResp=request.POST.get("tousResp",False)
        #setting start and end of period
        if period:
            dateDeb=request.POST["dateDebut"]
            dateFin=request.POST["dateFin"]
        #setting start and end of current year
        else:
            year=datetime.date.today().year
            dateDeb=str(year)+'-1-1'
            dateFin=str(year)+'-12-31'
        #all Responsables
        if allResp :
            #All Sectors
            if sect=="tous":
                #get TRA , TRAT and TCA filtred on current year
                nbAP=model.Action.getAllPlanified(dateDeb,dateFin)
                nbAR=model.Action.getAllDone(dateDeb,dateFin)
                nbART=model.Action.getAllDoneAtTime(dateDeb,dateFin)
                nbAC=model.Action.getAllClustered(dateDeb,dateFin)
                sects=model.Secteur.Find_All_Secters()
                nbAllPA=model.PA.getAllPA(dateDeb,dateFin)
                nbCompletedPA=model.PA.getCompletedPA(dateDeb,dateFin)
                nbUncompletedPA=model.PA.getUncompletedPA(dateDeb,dateFin)
                resps=False
            #Some Secters
            else:
                #get TRA , TRAT and TCA filtred on current year
                nbAP=model.Action.getAllPlanifiedBySecter(dateDeb,dateFin,sect)
                nbAR=model.Action.getAllDoneBySecter(dateDeb,dateFin,sect)
                nbART=model.Action.getAllDoneAtTimeBySecter(dateDeb,dateFin,sect)
                nbAC=model.Action.getAllClusteredBySecter(dateDeb,dateFin,sect)
                sects=[sect]
                nbAllPA=model.PA.getAllPABySecter(dateDeb,dateFin,sect)
                nbCompletedPA=model.PA.getCompletedPABySecter(dateDeb,dateFin,sect)
                nbUncompletedPA=model.PA.getUncompletedPABySecter(dateDeb,dateFin,sect)
                resps=False
        #some Responsables
        else:
            resp=[]
            resps=[]
            for i in model.User.Find_All_id():
                if request.POST.get("resp"+str(i)):
                    resp.append(int(request.POST["resp"+str(i)]))
                    resps.append(model.User.FindById(int(request.POST["resp"+str(i)])))
            #All Sectors
            if sect=="tous":
                #get TRA , TRAT and TCA filtred on current year
                nbAP=model.Action.getAllPlanifiedByResps(dateDeb,dateFin,resp)
                nbAR=model.Action.getAllDoneByResps(dateDeb,dateFin,resp)
                nbART=model.Action.getAllDoneAtTimeByResps(dateDeb,dateFin,resp)
                nbAC=model.Action.getAllClusteredByResps(dateDeb,dateFin,resp)
                nbAllPA=model.PA.getAllPAByResps(dateDeb,dateFin,resp)
                nbCompletedPA=model.PA.getCompletedPAByResps(dateDeb,dateFin,resp)
                nbUncompletedPA=model.PA.getUncompletedPAByResps(dateDeb,dateFin,resp)
                sects=model.Secteur.Find_All_Secters()
            #Some Secters
            else:
                #get TRA , TRAT and TCA filtred on current year
                nbAP=model.Action.getAllPlanifiedBySecterByResps(dateDeb,dateFin,sect,resp)
                nbAR=model.Action.getAllDoneBySecterByResps(dateDeb,dateFin,sect,resp)
                nbART=model.Action.getAllDoneAtTimeBySecterByResps(dateDeb,dateFin,sect,resp)
                nbAC=model.Action.getAllClusteredBySecterByResps(dateDeb,dateFin,sect,resp)
                nbAllPA=model.PA.getAllPABySecterByResps(dateDeb,dateFin,sect,resp)
                nbCompletedPA=model.PA.getCompletedPABySecterByResps(dateDeb,dateFin,sect,resp)
                nbUncompletedPA=model.PA.getUncompletedPABySecterByResps(dateDeb,dateFin,sect,resp)
                sects=[sect]
        #Taux de réalisation d'action
        TRA=[]
        TRAall=[] 
        allAR=0
        allAP=0
        t1ac,t1ap,t2ac,t2ap,t3ac,t3ap,t4ac,t4ap=0,0,0,0,0,0,0,0    
        tt=[[t1ac,t1ap],[t2ac,t2ap],[t3ac,t3ap],[t4ac,t4ap]]   
        for nbar,nbap in zip(nbAR,nbAP):
                    sum=0
                    count=0
                    allar=0
                    allap=0
                    T=[]
                    for ar,ap,t in zip(nbar,nbap,tt):
                        if(ap==None):
                            T.append("En dehors de la période donnée!")
                        elif (ap==0):
                            T.append("Pas d'actions planifiées dans cette période!")
                        else:
                            if ar!=None:
                                t[0]+=ar
                                t[1]+=ap
                                allar+=ar
                                allAR+=ar
                                allap+=ap
                                allAP+=ap
                                sum+=(ar/ap)*100
                                count+=1
                                T.append(str(round((ar/ap)*100,2))+'%')
                    if allap!=0:
                        TRAall.append((allar/allap)*100)
                    else:
                        TRAall.append(0)
                    if count==0:
                        T.append("Pas de moyenne!")
                    else:
                        T.append(str(round(sum/count,2))+'%')
                    TRA.append(T)
        if allAP!=0:
            TRAMoyen=str(round((allAR/allAP)*100,2))+'%'
        else:
            TRAMoyen=str(round(0,2))+'%'
        
        TRATrim=[]
        allART=0
        allAP=0
        for t in tt:
            allAR+=t[0]
            allAP+=t[1]
            if t[1]!=0:
                TRATrim.append((t[0]/t[1])*100)
            else:
                TRATrim.append(0)
        som=0
        for t in TRATrim:
            som+=t
        TRATrimMoyen=str(round((som/4),2))+'%'

        #Taux de réalisation d'action à temps
        TRAT=[]
        TRATall=[] 
        allART=0
        allAP=0
        t1ac,t1ap,t2ac,t2ap,t3ac,t3ap,t4ac,t4ap=0,0,0,0,0,0,0,0    
        tt=[[t1ac,t1ap],[t2ac,t2ap],[t3ac,t3ap],[t4ac,t4ap]]
        for nbart,nbap in zip(nbART,nbAP):
                    sum=0
                    count=0
                    allart=0
                    allap=0
                    T=[]
                    for art,ap,t in zip(nbart,nbap,tt):
                        if(ap==None):
                            T.append("En dehors de la période donnée!")
                        elif (ap==0):
                            T.append("Pas d'actions planifiées dans cette période!")
                        else:
                            if art!=None:
                                t[0]+=art
                                t[1]+=ap
                                allart+=art
                                allART+=art
                                allap+=ap
                                allAP+=ap
                                sum+=(art/ap)*100
                                count+=1
                                T.append(str(round((art/ap)*100,2))+'%')
                    if allap!=0:
                        TRATall.append((allart/allap)*100)
                    else:
                        TRATall.append(0)
                    if count==0:
                        T.append("Pas de moyenne!")
                    else:
                        T.append(str(round(sum/count,2))+'%')
                    TRAT.append(T)
        if allAP!=0:
            TRATMoyen=str(round((allART/allAP)*100,2))+'%'
        else:
            TRATMoyen=str(round(0,2))+'%'

        TRATTrim=[]
        allART=0
        allAP=0
        for t in tt:
            allART+=t[0]
            allAP+=t[1]
            if t[1]!=0:
                TRATTrim.append((t[0]/t[1])*100)
            else:
                TRATTrim.append(0)
        som=0
        for t in TRATTrim:
            som+=t
        TRATTrimMoyen=str(round((som/4),2))+'%'

        #Taux de cloturation d'action
        TCA=[]  
        TCAall=[]
        allAC=0
        allAP=0
        t1ac,t1ap,t2ac,t2ap,t3ac,t3ap,t4ac,t4ap=0,0,0,0,0,0,0,0    
        tt=[[t1ac,t1ap],[t2ac,t2ap],[t3ac,t3ap],[t4ac,t4ap]]  
        
        for nbac,nbap in zip(nbAC,nbAP):
                    sum=0
                    count=0
                    allac=0
                    allap=0
                    T=[]
                    for ac,ap,t in zip(nbac,nbap,tt):
                        if(ap==None):
                            T.append("En dehors de la période donnée!")
                        elif (ap==0):
                            T.append("Pas d'actions planifiées dans cette période!")
                        else:
                            if ac!=None:
                                t[0]+=ac
                                t[1]+=ap
                                allAC+=ac
                                allAP+=ap
                                allac+=ac
                                allap+=ap
                                sum+=(ac/ap)*100
                                count+=1
                                T.append(str(round((ac/ap)*100,2))+'%')
                    if allap!=0:
                        TCAall.append((allac/allap)*100)
                    else:
                        TCAall.append(0)
                    if count==0:
                        T.append("Pas de moyenne!")
                    else:
                        T.append(str(round(sum/count,2))+'%')
                    TCA.append(T)
        if allAP!=0:
            TCAMoyen=str(round((allAC/allAP)*100,2))+'%'
        else:
            TCAMoyen=str(round(0,2))+'%'

        TCATrim=[]
        allAC=0
        allAP=0
        for t in tt:
            allAC+=t[0]
            allAP+=t[1]
            if t[1]!=0:
                TCATrim.append((t[0]/t[1])*100)
            else:
                TCATrim.append(0)
        som=0
        for t in TCATrim:
            som+=t
        TCATrimMoyen=str(round((som/4),2))+'%'

        nbAllPAM=[]
        for n in nbAllPA:
            nbAllPAM.append([n[0],n[1],n[2],n[3],'-'])
        
        nbAllPA=nbAllPAM

        nbCompletedPAM=[]
        for n in nbCompletedPA:
            nbCompletedPAM.append([n[0],n[1],n[2],n[3],'-'])

        nbCompletedPA=nbCompletedPAM

        nbUncompletedPAM=[]
        for n in nbCompletedPA:
            nbUncompletedPAM.append([n[0],n[1],n[2],n[3],'-'])

        nbUncompletedPA=nbUncompletedPAM

        tab=[]
        for i,j,k,l,m,n,o in zip(sects,TRA,TRAT,TCA,nbAllPA,nbCompletedPA,nbUncompletedPA):
            tab.append([i,zip(j,k,l,m,n,o)])
       

        data = [['PA','TRA','TRAT','TCA']]
        for x,y,z,i in  zip(sects,TRAall,TRATall,TCAall):
            data.append([x,y,z,i])
        # DataSource object
        data_source = SimpleDataSource(data=data)
        # Chart object
        i1i2 = BarChart(data_source)
        data = [['Trim','TRA','TRAT','TCA']]
        trim=['T1','T2','T3','T4']
        for x,y,z,t in  zip(trim,TRATrim,TRATTrim,TCATrim):
            data.append([x,y,z,t])
        # DataSource object
        data_source = SimpleDataSource(data=data)
        chart= BarChart(data_source)
        dict={"TRA":tab,"sects":sects,"resps":resps,"chart":chart,"chart1":i1i2,"TRAMoyen":TRAMoyen,"TRATMoyen":TRATMoyen,"TCAMoyen":TCAMoyen,"TCATrimMoyen":TCATrimMoyen,"TRATTrimMoyen":TRATTrimMoyen,"TRATrimMoyen":TRATrimMoyen}
        return render(request,'dashboard.html',dict)
    else:
        return redirect('home')

def dashboardForm(request):
    if request.method == 'POST':
        sects=model.Secteur.Find_All()
        resps=model.User.Find_All()
        dict={"sects":sects,"resps":resps}
        return render(request,'dashboardForm.html',dict)
    else:
        return redirect('home')

def consultAllMyActions(request):
    if request.method == 'POST':
        myActs=model.Action.getAllMyActs(request.session["user"]["Immatricule"])
        myCheckerActs=model.Action.getAllMyCheckerActs(request.session["user"]["Immatricule"])
        myActorActs=model.Action.getAllMyActorActs(request.session["user"]["Immatricule"])
        dict={"myActs":myActs,"myCheckerActs":myCheckerActs,"myActorActs":myActorActs}
        return render(request,'consultAllMyActions.html',dict)
    else:
        return redirect('home')

def inputReformat(text):
    text=text.split('\r\n')
    text='<br />'.join(text)
    text=text.split("'")
    text="''".join(text)
    return text

def outputReformat(text):
    text=text.split('<br />')
    text='\r\n'.join(text)
    text=text.split("''")
    text="'".join(text)
    return text

def consultAllMyPA(request):
    if request.method == 'POST':
        myPAs=model.PA.getAllMyPA(request.session["user"]["Immatricule"])
        dict={"myPAs":myPAs}
        return render(request,'consultAllMyPA.html',dict)
    else:
        return redirect('home')

def historic(request):
    if request.method == 'POST':
        completedPA=model.PA.getAllCompletedPA()
        uncompletedPA=model.PA.getAllUncompletedPA()
        dict={"completedPA":completedPA,"uncompletedPA":uncompletedPA}
        return render(request,'Historic.html',dict)
    else:
        return redirect('home')

def printPA(request):
    if request.method == 'POST' and (request.POST.get("idPA",False)):
        idPA=request.POST["idPA"]
        respFilter="tous"
        pa=model.PA.Find_By_idPA(str(idPA))
        parts=""
        if pa.participants is not None:
            for i in pa.participants:
                try:
                    parts+=model.User.FindById(i)+','
                except:
                    parts=parts
            parts = parts[:-1]
        Cs=""
        if pa.C is not None:
            for i in pa.C:
                try:
                    Cs+=model.User.FindById(i)+','
                except:
                    Cs=Cs
            Cs = Cs[:-1]
        As=""
        if pa.A is not None:
            for i in pa.A:
                try:
                    As+=model.User.FindById(i)+','
                except:
                    As=As
            As = As[:-1]
        pilote=model.User.FindById(pa.piloteImm)
        axes = model.Axe.Find_All_By_idPA(pa.idPA)
        axeAndProbAndActions=[]
        for axe in axes:
            probs=model.Problem.Find_All_By_idAxe(axe.idAxe)
            probAndActions=[]
            sums=0
            for prob in probs:
                actions=model.Action.Find_All_By_idProb(prob.idProb)
                sums+=len(actions)
                probAndActions.append([prob,len(actions)+2,len(actions)+1,actions])
            axeAndProbAndActions.append([axe,len(probs)+sums+2,probAndActions])
        dict={"pa":pa,"parts":parts,"pilote":pilote,"axeAndProbAndActions":axeAndProbAndActions,"Cs":Cs,"As":As,"respFilter":respFilter}
        return render(request,'printPA.html',dict)
    else:
        return redirect('home')
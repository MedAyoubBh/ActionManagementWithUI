import datetime
from django.db import models
import psycopg2


class Secteur():
    nameSec = models.CharField(max_length=250)

    def Find_All_Sects():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='SELECT * from public."Secteur" order by "nameSec" asc;'
        cursor.execute(str)
        result = cursor.fetchall()
        conn.close()
        all = []
        for name in result:
            all.append(name)
        return all

    def insert(new):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='''insert into public."Secteur" values(\''''+new+'''\');commit;'''
        cursor.execute(str)
        conn.close()

    def delete(old):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='''delete from public."Secteur" where "nameSec"=\''''+old+'''\';commit;'''
        cursor.execute(str)
        conn.close()

    def Update(new,old):
        Secteur.insert(new)
        #modificate old secter values in PA with the new one
        idPAs=PA.Find_By_Secter(old)
        for idPA in idPAs:
            PA.UpdateSecter(idPA,new)
        Secteur.delete(old)

    def Find_All():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='SELECT * from public."Secteur" order by "nameSec" ASC;'
        cursor.execute(str)
        result = cursor.fetchall()
        conn.close()
        all = []
        for name in result:
            s = Secteur()
            s.nameSec=name
            all.append(s)
        return all

    def Find_All_Secters():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='SELECT * from public."Secteur" order by "nameSec" ASC;'
        cursor.execute(str)
        result = cursor.fetchall()
        conn.close()
        all = []
        for name in result:
            all.append(name[0])
        return all

    def __str__(self) :
        return self.nameSec

    def __str__(self) :
        return self.nameSec


class PA():
    idPA = models.IntegerField()
    nomPA = models.CharField(max_length=250)
    nbPA = models.IntegerField()
    pagePA = 1
    datePA = datetime.date.today()
    piloteImm = models.IntegerField()
    secteurPA = models.CharField(max_length=250)
    participants = []
    dateRev = datePA
    nbRev = 0
    C = []
    A = []

    def getAllCompletedPA():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        st='''SELECT pa."idPA",pa."nomPA",pa."nbPA",pa."pagePA",pa."datePA",pa."piloteImm",pa."secteurPA",pa."participants",pa."dateRev",pa."nbRev",pa."C",pa."A" from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and act."A" = \''''+str(True)+'''\' ;'''
        cursor.execute(st)
        result = cursor.fetchall()
        completedPA=[]
        for res in result:
            s = PA()
            s.idPA=res[0]
            s.nomPA=res[1]
            s.nbPA=res[2]
            s.pagePA=res[3]
            s.datePA=res[4]
            s.piloteImm=res[5]
            s.secteurPA=res[6]
            s.participants=res[7]
            q=""
            for r in s.participants:
                try:
                    q+=User.FindById(r)+', '
                except:
                    q=q
            s.participants=q[:-2]
            s.dateRev=res[8]
            s.nbRev=res[9]
            s.C=res[10]
            q=""
            if s.C!=None:
                for r in s.C:
                    try:
                        q+=User.FindById(r)+', '
                    except:
                        q=q
                s.C=q[:-2]
            s.A=res[11]
            q=""
            if s.A!=None:
                for r in s.A:
                    try:
                        q+=User.FindById(r)+', '
                    except:
                        q=q
                s.A=q[:-2]
            completedPA.append(s)
        conn.close()
        return completedPA
    
    def getAllCompletedPA():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        st='''SELECT pa."idPA",pa."nomPA",pa."nbPA",pa."pagePA",pa."datePA",pa."piloteImm",pa."secteurPA",pa."participants",pa."dateRev",pa."nbRev",pa."C",pa."A" from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and act."A" = \''''+str(True)+'''\' order By pa."idPA" asc;'''
        cursor.execute(st)
        result = cursor.fetchall()
        completedPA=[]
        for res in result:
            s = PA()
            s.idPA=res[0]
            s.nomPA=res[1]
            s.nbPA=res[2]
            s.pagePA=res[3]
            s.datePA=res[4]
            s.piloteImm=res[5]
            s.secteurPA=res[6]
            s.participants=res[7]
            q=""
            for r in s.participants:
                try:
                    q+=User.FindById(r)+', '
                except:
                    q=q
            s.participants=q[:-2]
            s.dateRev=res[8]
            s.nbRev=res[9]
            s.C=res[10]
            q=""
            if s.C!=None:
                for r in s.C:
                    try:
                        q+=User.FindById(r)+', '
                    except:
                        q=q
                s.C=q[:-2]
            s.A=res[11]
            q=""
            if s.A!=None:
                for r in s.A:
                    try:
                        q+=User.FindById(r)+', '
                    except:
                        q=q
                s.A=q[:-2]
            completedPA.append(s)
        conn.close()
        return completedPA
    
    def getAllUncompletedPA():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        st='''SELECT pa."idPA",pa."nomPA",pa."nbPA",pa."pagePA",pa."datePA",pa."piloteImm",pa."secteurPA",pa."participants",pa."dateRev",pa."nbRev",pa."C",pa."A" from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and act."A" = \''''+str(False)+'''\' order By pa."idPA" asc;'''
        cursor.execute(st)
        result = cursor.fetchall()
        uncompletedPA=[]
        for res in result:
            s = PA()
            s.idPA=res[0]
            s.nomPA=res[1]
            s.nbPA=res[2]
            s.pagePA=res[3]
            s.datePA=res[4]
            s.piloteImm=res[5]
            s.secteurPA=res[6]
            s.participants=res[7]
            q=""
            for r in s.participants:
                try:
                    q+=User.FindById(r)+', '
                except:
                    q=q
            s.participants=q[:-2]
            s.dateRev=res[8]
            s.nbRev=res[9]
            s.C=res[10]
            q=""
            if s.C!=None:
                for r in s.C:
                    try:
                        q+=User.FindById(r)+', '
                    except:
                        q=q
                s.C=q[:-2]
            s.A=res[11]
            q=""
            if s.A!=None:
                for r in s.A:
                    try:
                        q+=User.FindById(r)+', '
                    except:
                        q=q
                s.A=q[:-2]
            uncompletedPA.append(s)
        conn.close()
        return uncompletedPA

    def Find_All_Sects():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='SELECT distinct("secteurPA") from public."PA" order by "secteurPA" asc;'
        cursor.execute(str)
        result = cursor.fetchall()
        conn.close()
        all = []
        for name in result:
            all.append(name)
        print(all)
        return all

    def getAllPA(dateDeb,dateFin):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(idPA) from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' and act."P" = \''''+str(True)+'''\' ;'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(idPA) from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' and act."P" = \''''+str(True)+'''\';'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\';'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

            finalResult.append(result)
        conn.close()
        return finalResult

    def getCompletedPA(dateDeb,dateFin):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\';'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

            finalResult.append(result)
        conn.close()
        return finalResult

    def getUncompletedPA(dateDeb,dateFin):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\';'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

            finalResult.append(result)
        conn.close()
        return finalResult

    def getAllPABySecter(dateDeb,dateFin,sect):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
            #st='''SELECT count(idPA) from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' and act."P" = \''''+str(True)+'''\' ;'''
        result=[]
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\';'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count("idPA") from public."PA" pa WHERE pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

        finalResult.append(result)
        conn.close()
        return finalResult

    def getCompletedPABySecter(dateDeb,dateFin,sect):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
            #st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
        result=[]
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\';'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

        finalResult.append(result)
        conn.close()
        return finalResult

    def getUncompletedPABySecter(dateDeb,dateFin,sect):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
            #st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
        result=[]
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\';'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\';'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\';'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\';'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

        finalResult.append(result)
        conn.close()
        return finalResult

    def getAllPAByResps(dateDeb,dateFin,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' and act."P" = \''''+str(True)+'''\' and \''''+resp+'''\' && act."resp" ;'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' and act."P" = \''''+str(True)+'''\' and \''''+resp+'''\' && act."resp"  ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

            finalResult.append(result)
        conn.close()
        return finalResult

    def getCompletedPAByResps(dateDeb,dateFin,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

            finalResult.append(result)
        conn.close()
        return finalResult

    def getUncompletedPAByResps(dateDeb,dateFin,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

            finalResult.append(result)
        conn.close()
        return finalResult

    def getAllPABySecterByResps(dateDeb,dateFin,sect,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
            #st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' and act."P" = \''''+str(True)+'''\' and \''''+resp+'''\' && act."resp" ;'''
        result=[]
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' and act."P" = \''''+str(True)+'''\' and \''''+resp+'''\' && act."resp"  ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa ,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and  pa."secteurPA" = \''''+str(sect)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

        finalResult.append(result)
        conn.close()
        return finalResult

    def getCompletedPABySecterByResps(dateDeb,dateFin,sect,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
            #st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
        result=[]
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(True)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

        finalResult.append(result)
        conn.close()
        return finalResult

    def getUncompletedPABySecterByResps(dateDeb,dateFin,sect,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
            #st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' ;'''
        result=[]
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\' and \''''+resp+'''\' && act."resp" ;'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(pa."idPA") from public."PA" pa,public."Axe" axe,public."Problem" pr,public."Action" act WHERE pa."idPA"=axe."idPA" and axe."idAxe"=pr."idAxe" and pr."idProb"=act."idProb" and pa."secteurPA" = \''''+str(sect)+'''\' and act."A" = \''''+str(False)+'''\' and pa."datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\' and \''''+resp+'''\' && act."resp" ;'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

        finalResult.append(result)
        conn.close()
        return finalResult

    def getAllMyPA(imm):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        imm=str(imm)
        st='''Select "idPA","nomPA","nbPA","pagePA","datePA","piloteImm","secteurPA","participants","dateRev","nbRev","C","A" from public."PA" where "piloteImm"=\''''+imm+'''\'order By "nomPA","nbPA", "pagePA", "idPA","datePA";'''
        cursor.execute(st)
        result = cursor.fetchall()
        myPA=[]
        for res in result:
            s = PA()
            s.idPA=res[0]
            s.nomPA=res[1]
            s.nbPA=res[2]
            s.pagePA=res[3]
            s.datePA=res[4]
            s.piloteImm=res[5]
            s.secteurPA=res[6]
            s.participants=res[7]
            q=""
            for r in s.participants:
                try:
                    q+=User.FindById(r)+', '
                except:
                    q=q
            s.participants=q[:-2]
            s.dateRev=res[8]
            s.nbRev=res[9]
            s.C=res[10]
            q=""
            if s.C!=None:
                for r in s.C:
                    try:
                        q+=User.FindById(r)+', '
                    except:
                        q=q
                s.C=q[:-2]
            s.A=res[11]
            q=""
            if s.A!=None:
                for r in s.A:
                    try:
                        q+=User.FindById(r)+', '
                    except:
                        q=q
                s.A=q[:-2]
            myPA.append(s)
        conn.close()
        return myPA

    def UpdateActors(pa):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        part=str(pa.A)
        part=part.replace('[','{')
        part=part.replace(']','}')
        st="""UPDATE public."PA" SET "A" =\'"""+part+"""\'WHERE "idPA" = """+str(pa.idPA)+""";commit;"""
        cursor.execute(st)
        conn.close()

    def UpdateCheckers(pa):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        part=str(pa.C)
        part=part.replace('[','{')
        part=part.replace(']','}')
        st="""UPDATE public."PA" SET "C" =\'"""+part+"""\'WHERE "idPA" = """+str(pa.idPA)+""";commit;"""
        cursor.execute(st)
        conn.close()

    def UpdateParticipants(pa):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        part=str(pa.participants)
        part=part.replace('[','{')
        part=part.replace(']','}')
        st="""UPDATE public."PA" SET participants =\'"""+part+"""\'WHERE "idPA" = """+str(pa.idPA)+""";commit;"""
        cursor.execute(st)
        conn.close()

    def percentage(idPA):
        countP=0
        countD=0
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idPA=str(idPA)
        st='''SELECT "P","D" from public."Action" where "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA"='''+idPA+'''));'''
        cursor.execute(st)
        result = cursor.fetchall()
        conn.close()
        print(result)
        for res in result:
            if res[0]==True:
                countP+=1
            if res[1]==True:
                countD+=1
        try:
            return (countD/countP)*100
        except:
            return 0

    def UpdateSecter(idPA,new):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idPA=str(idPA)
        st='UPDATE public."PA" SET "secteurPA"=\''+new+'\' WHERE "idPA"='+idPA+';commit;'
        cursor.execute(st)
        conn.close()

    def update_rev(nbrev,idPA):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idPA=str(idPA)
        nbrev=str(nbrev)
        st='UPDATE public."PA" SET "nbRev"='+nbrev+' WHERE "idPA"='+idPA+';commit;'
        cursor.execute(st)
        conn.close()

    def Find_id(nomPA,nbPA,pagePA):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        nbPA=str(nbPA)
        pagePA=str(pagePA)
        st='''SELECT "idPA" from public."PA" where "nomPA"=\''''+nomPA+'''\' and "nbPA"='''+nbPA+''' and "pagePA"='''+pagePA+''';'''
        cursor.execute(st)
        result = cursor.fetchone()
        conn.close()
        return result[0]


    def Find_All():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='''SELECT "nomPA","nbPA","pagePA","datePA","piloteImm","secteurPA","participants","dateRev","nbRev" from public."PA"'''
        cursor.execute(str)
        result = cursor.fetchall()
        conn.close()
        all = []
        for res in result:
            s = PA()
            s.nomPA=res[0]
            s.nbPA=res[1]
            s.pagePA=res[2]
            s.datePA=res[3]
            s.piloteImm=res[4]
            s.secteurPA=res[5]
            s.participants=res[6]
            s.dateRev=res[7]
            s.nbRev=res[8]
            all.append(s)
        return all

    def Find_Last_nbPA(secName):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='''select MAX("nbPA") from public."PA" where "nomPA"=\''''+secName+'''\''''
        cursor.execute(str)
        res = cursor.fetchone()
        conn.close()
        return res
    
    def Find_Last_pagePA(nomPA,nbPA):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        nbPA=str(nbPA)
        st='''select MAX("pagePA") from public."PA" where "nomPA"=\''''+nomPA+'''\' and "nbPA"='''+nbPA+''';'''
        cursor.execute(st)
        res = cursor.fetchone()
        conn.close()
        return res[0]

    def Insert(p):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        pagePA=str(p.pagePA)
        datePA=str(p.datePA)
        imm=str(p.piloteImm)
        part=str(p.participants)
        part=part.replace('[','{')
        part=part.replace(']','}')
        C=str(p.C)
        C=C.replace('[','{')
        C=C.replace(']','}')
        A=str(p.A)
        A=A.replace('[','{')
        A=A.replace(']','}')
        daterev=str(p.dateRev)
        nbrev=str(p.nbRev)
        nbPA=str(p.nbPA)
        st='INSERT INTO public."PA"("nomPA", "nbPA", "pagePA", "datePA", "piloteImm", "secteurPA", participants, "dateRev", "nbRev","C","A") VALUES (\''+p.nomPA+'\','+nbPA+','+pagePA+',\''+datePA+'\','+imm+',\''+p.secteurPA+'\',\''+part+'\',\''+daterev+'\','+nbrev+',\''+C+'\',\''+A+'\');commit;'
        cursor.execute(st)
        conn.close()
    
    def Find_By_idPA(idPA):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='''SELECT "idPA","nomPA", "nbPA", "pagePA", "datePA", "piloteImm", "secteurPA", participants, "dateRev", "nbRev","C","A" from public."PA" where "idPA"='''+idPA+''';'''
        cursor.execute(str)
        res = cursor.fetchall()
        conn.close()
        s = PA()
        s.idPA=res[0][0]
        s.nomPA=res[0][1]
        s.nbPA=res[0][2]
        s.pagePA=res[0][3]
        s.datePA=res[0][4]
        s.piloteImm=res[0][5]
        s.secteurPA=res[0][6]
        s.participants=res[0][7]
        s.dateRev=res[0][8]
        s.nbRev=res[0][9]
        s.C=res[0][10]
        s.A=res[0][11]
        return s

    def Find_By_Secter(new):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='''SELECT "idPA" from public."PA" where "secteurPA"=\''''+new+'''\';'''
        cursor.execute(str)
        result = cursor.fetchall()
        conn.close()
        all=[]
        for res in result:
            all.append(res[0])
        return all

    def __str__(self) :
        return self.nomPA


class User():
    Immatricule = models.IntegerField()
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    pwd = models.CharField(max_length=250)

    def UpdateUserInPA_Axe_Prob_Act(lastImm,imm):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        st='''Update public."PA" Set "piloteImm"='''+str(imm)+'''  where "piloteImm"='''+str(lastImm)+''' ;commit;'''
        cursor.execute(st)
        st='''Select "idPA", participants from public."PA" where '{'''+str(lastImm)+'''}' && participants;'''
        cursor.execute(st)
        result=cursor.fetchall()
        idPAs=[]
        parts=[]
        for res in result:
            idPAs.append(res[0])
            parts.append(res[1])
        
        for idPA,part in zip(idPAs,parts):
            part.remove(int(lastImm))
            part.append(int(imm))
            part=str(part)
            part=part.replace('[','{')
            part=part.replace(']','}')
            st='''Update public."PA" Set "participants"= \''''+part+'''\' where "idPA"='''+str(idPA)+''' ;commit;'''
            cursor.execute(st)
        
        st='''Select "idAct", resp from public."Action" where '{'''+str(lastImm)+'''}' && resp;'''
        cursor.execute(st)
        result=cursor.fetchall()
        idActs=[]
        resp=[]
        for res in result:
            idActs.append(res[0])
            resp.append(res[1])
        
        for idAct,r in zip(idActs,resp):
            r.remove(int(lastImm))
            r.append(int(imm))
            r=str(r)
            r=r.replace('[','{')
            r=r.replace(']','}')
            st='''Update public."Action" Set "resp"= \''''+r+'''\' where "idAct"='''+str(idAct)+''' ;commit;'''
            cursor.execute(st)
        conn.close()

    def DeleteUser(imm):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        
        st='''Update public."PA" Set "piloteImm"= '''+'3'+''' where "piloteImm"='''+str(imm)+''' ;commit;'''
        cursor.execute(st)

        st='''Select "idPA", participants from public."PA" where '{'''+str(imm)+'''}' && participants;'''
        cursor.execute(st)
        result=cursor.fetchall()
        idPAs=[]
        parts=[]
        for res in result:
            idPAs.append(res[0])
            parts.append(res[1])
        
        for idPA,part in zip(idPAs,parts):
            part.remove(int(imm))
            part=str(part)
            part=part.replace('[','{')
            part=part.replace(']','}')
            st='''Update public."PA" Set "participants"= \''''+part+'''\' where "idPA"='''+str(idPA)+''' ;commit;'''
            cursor.execute(st)
        
        st='''Select "idAct", resp from public."Action" where '{'''+str(imm)+'''}' && resp;'''
        cursor.execute(st)
        result=cursor.fetchall()
        idActs=[]
        resp=[]
        for res in result:
            idActs.append(res[0])
            resp.append(res[1])
        
        for idAct,r in zip(idActs,resp):
            r.remove(int(imm))
            r=str(r)
            r=r.replace('[','{')
            r=r.replace(']','}')
            st='''Update public."Action" Set "resp"= \''''+r+'''\' where "idAct"='''+str(idAct)+''' ;commit;'''
            cursor.execute(st)
        
        st='''Delete from public."User" where "Immatricule"='''+str(imm)+''';commit;'''
        cursor.execute(st)
        conn.close()
        

    def createUser(user):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        st='''insert into public."User" values ('''+str(user.Immatricule)+''',\''''+user.FirstName+'''\',\''''+user.LastName+'''\',\''''+user.pwd+'''\');commit;'''
        cursor.execute(st)
        conn.close()
    
    def UpdateUser(user,lastImm):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        st='''Update public."User" Set "Immatricule"='''+str(user.Immatricule)+''',"FirstName"=\''''+user.FirstName+'''\',"LastName"=\''''+user.LastName+'''\',pwd=\''''+user.pwd+'''\' where "Immatricule"='''+str(lastImm)+''';commit;'''
        cursor.execute(st)
        conn.close()

    def Find_All():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='''SELECT "Immatricule","FirstName","LastName","pwd" from public."User" order by "Immatricule" asc'''
        cursor.execute(str)
        result = cursor.fetchall()
        conn.close()
        all = []
        for res in result:
            s = User()
            s.Immatricule=int(res[0])
            s.FirstName=res[1]
            s.LastName=res[2]
            s.pwd=res[3]
            all.append(s)
        return all

    def Find_All_id():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='''SELECT "Immatricule" from public."User"'''
        cursor.execute(str)
        result = cursor.fetchall()
        conn.close()
        all = []
        for res in result:
            all.append(res[0])
        return all

    def FindById(id):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        id=str(id)
        st='''SELECT "FirstName","LastName" from public."User" where "Immatricule"='''+id+''';'''
        cursor.execute(st)
        result = cursor.fetchall()
        conn.close()
        if result:
            return result[0][0]+' '+result[0][1]
        else:
            return False

    def FindByIdImm(id):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        id=str(id)
        st='''SELECT "Immatricule","FirstName","LastName","pwd" from public."User" where "Immatricule"='''+id+'''order by "Immatricule" asc;'''
        cursor.execute(st)
        res = cursor.fetchall()
        conn.close()
        s = User()
        s.Immatricule=int(res[0][0])
        s.FirstName=res[0][1]
        s.LastName=res[0][2]
        s.pwd=res[0][3]
        return s

    def Get_Pwd_By_Id(self,id):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        id=str(id)
        st='''SELECT "pwd" from public."User" where "Immatricule"='''+id+''';'''
        cursor.execute(st)
        result = cursor.fetchall()
        conn.close()
        return result[0][0]

    def Check_Imm(self):
        if User.FindById(self.Immatricule):
            return True
        else:
            return False

    def Check_Password(self):
        if self.pwd == self.Get_Pwd_By_Id(self.Immatricule):
            return True
        else:
            return False
    
    def serialize(self):
        return{
            'Immatricule':self.Immatricule,
            'Name':str(self.FirstName)+' '+str(self.LastName),
            'pwd':str(self.pwd)
        }

    def getUser(self):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        id=str(self.Immatricule)
        st='''SELECT "FirstName","LastName" from public."User" where "Immatricule"='''+id+''';'''
        cursor.execute(st)
        result = cursor.fetchone()
        conn.close()
        self.FirstName=result[0]
        self.LastName=result[1]
        return self

class Problem():
    idProb = models.IntegerField()
    nbProb = models.IntegerField()
    descriptionProb = models.CharField(max_length=100000)
    cr = models.IntegerField(max_length=1)
    idAxe = models.IntegerField()

    def Find_All():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='''SELECT "idProb","nbProb","descriptionProb","CR","idAxe" from public."Problem"'''
        cursor.execute(str)
        result = cursor.fetchall()
        conn.close()
        all = []
        for res in result:
            s = Problem()
            s.idProb=int(res[0])
            s.nbProb=int(res[1])
            s.descriptionProb=res[2]
            s.cr=int(res[3])
            s.idAxe=int(res[4])
            all.append(s)
        return all 

    def Find_By_idProb(idProb):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idProb=str(idProb)
        st='''SELECT "idProb","nbProb","descriptionProb","CR","idAxe" from public."Problem" where "idProb"='''+idProb+'''order by "idProb" asc;'''
        cursor.execute(st)
        res = cursor.fetchone()
        conn.close()
        s = Problem()
        s.idProb=int(res[0])
        s.nbProb=int(res[1])
        s.descriptionProb=res[2]
        s.cr=int(res[3])
        s.idAxe=int(res[4])
        return s       

    def Find_All_By_idAxe(idAxe):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idAxe=str(idAxe)
        st='''SELECT "idProb","nbProb","descriptionProb","CR","idAxe" from public."Problem" where "idAxe"='''+idAxe+'''order by "idProb" asc;'''
        cursor.execute(st)
        result = cursor.fetchall()
        conn.close()
        all = []
        for res in result:
            s = Problem()
            s.idProb=int(res[0])
            s.nbProb=int(res[1])
            s.descriptionProb=res[2]
            s.cr=int(res[3])
            s.idAxe=int(res[4])
            all.append(s)
        return all 

    def UpdateProblem(prob):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        st="""UPDATE public."Problem" SET "descriptionProb" =\'"""+prob.descriptionProb+"""\', "CR"="""+str(prob.cr)+""" WHERE "idProb" = """+str(prob.idProb)+""";commit;"""
        cursor.execute(st)
        conn.close()

    def Insert(p):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        nbProb=str(p.nbProb)
        cr=str(p.cr)
        idAxe=str(p.idAxe)
        st="""INSERT INTO public."Problem"("nbProb", "descriptionProb", "CR", "idAxe") VALUES ("""+nbProb+""",\'"""+p.descriptionProb+"""\',"""+cr+""","""+idAxe+""");commit;"""
        cursor.execute(st)
        conn.close()

    def Count_By_idAxe(idAxe):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idAxe=str(idAxe)
        st='''SELECT max("nbProb") from public."Problem" where "idAxe"='''+idAxe+''';'''
        cursor.execute(st)
        result = cursor.fetchone()
        conn.close()
        return result[0] 

    def __str__(self) :
        return self.domainProb

class Action():
    idAct = models.IntegerField()
    cause = models.CharField(max_length=100000)
    action = models.CharField(max_length=100000)
    resp = []
    datePrevue = models.DateField()
    P = models.BooleanField()
    D = models.BooleanField()
    C = models.BooleanField()
    A = models.BooleanField()
    idProb = models.IntegerField()
    nbAct = models.IntegerField()
    dateDone = models.DateField()
    dateCloture = models.DateField()

    def getAllMyActs(imm):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        imm=str(imm)
        imm='{'+imm+'}'
        st='''SELECT a."idAct",a."cause",a."action",a."resp",a."datePrevue",a."P",a."D",a."C",a."A",a."idProb",a."nbAct",pa."idPA",pa."nomPA" from public."Action" a ,public."Problem" p,public."Axe" axe,public."PA" pa where \''''+imm+'''\' && a."resp" and a."D"=False and a."P"=True and a."idProb"=p."idProb" and p."idAxe"=axe."idAxe" and axe."idPA"=pa."idPA";'''
        cursor.execute(st)
        result = cursor.fetchall()
        myActions=[]
        for res in result:
            s=[]
            s.append(int(res[0]))
            s.append(res[1])
            s.append(res[2])
            q=""
            for r in res[3]:
                q+=User.FindById(r)+', '
            s.append(q[:-2])
            s.append(res[4])
            s.append(res[5])
            s.append(res[6])
            s.append(res[7])
            s.append(res[8])
            s.append(int(res[9]))
            s.append(int(res[10]))
            s.append(int(res[11]))
            s.append(res[12])
            myActions.append(s)
        conn.close()
        return myActions

    def getAllMyCheckerActs(imm):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        imm=str(imm)
        imm='{'+imm+'}'
        st='''SELECT a."idAct",a."cause",a."action",a."resp",a."datePrevue",a."P",a."D",a."C",a."A",a."idProb",a."nbAct",pa."idPA",pa."nomPA" from public."Action" a ,public."Problem" p,public."Axe" axe,public."PA" pa
         where a."idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where \''''+imm+'''\' && "C"))) and a."D"=True and a."C"=False and a."idProb"=p."idProb" and p."idAxe"=axe."idAxe" and axe."idPA"=pa."idPA";'''
        cursor.execute(st)
        result = cursor.fetchall()
        myActions=[]
        for res in result:
            s=[]
            s.append(int(res[0]))
            s.append(res[1])
            s.append(res[2])
            q=""
            for r in res[3]:
                q+=User.FindById(r)+', '
            s.append(q[:-2])
            s.append(res[4])
            s.append(res[5])
            s.append(res[6])
            s.append(res[7])
            s.append(res[8])
            s.append(int(res[9]))
            s.append(int(res[10]))
            s.append(int(res[11]))
            s.append(res[12])
            myActions.append(s)
        conn.close()
        return myActions 

    def getAllMyActorActs(imm):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        imm=str(imm)
        imm='{'+imm+'}'
        st='''SELECT a."idAct",a."cause",a."action",a."resp",a."datePrevue",a."P",a."D",a."C",a."A",a."idProb",a."nbAct",pa."idPA",pa."nomPA" from public."Action" a ,public."Problem" p,public."Axe" axe,public."PA" pa
         where a."idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where \''''+imm+'''\' && "A"))) and a."C"=True and a."A"=False and a."idProb"=p."idProb" and p."idAxe"=axe."idAxe" and axe."idPA"=pa."idPA";'''
        cursor.execute(st)
        result = cursor.fetchall()
        myActions=[]
        for res in result:
            s=[]
            s.append(int(res[0]))
            s.append(res[1])
            s.append(res[2])
            q=""
            for r in res[3]:
                q+=User.FindById(r)+', '
            s.append(q[:-2])
            s.append(res[4])
            s.append(res[5])
            s.append(res[6])
            s.append(res[7])
            s.append(res[8])
            s.append(int(res[9]))
            s.append(int(res[10]))
            s.append(int(res[11]))
            s.append(res[12])
            myActions.append(s)
        conn.close()
        return myActions 

    def getAllPlanified(dateDeb,dateFin):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+str(True)+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])

            finalResult.append(result)
        conn.close()
        return finalResult

    def getAllDone(dateDeb,dateFin):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            finalResult.append(result)
        conn.close()
        return finalResult

    def getAllDoneAtTime(dateDeb,dateFin):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            finalResult.append(result)
        conn.close()
        return finalResult

    def getAllClustered(dateDeb,dateFin):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            finalResult.append(result)
        conn.close()
        return finalResult

    def getAllPlanifiedBySecter(dateDeb,dateFin,sect):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        result=[]
        #st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        finalResult.append(result)
        conn.close()
        return finalResult

    def getAllDoneBySecter(dateDeb,dateFin,sect):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        result=[]
        #st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        finalResult.append(result)
        conn.close()
        return finalResult

    def getAllDoneAtTimeBySecter(dateDeb,dateFin,sect):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        result=[]
        #st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        finalResult.append(result)
        conn.close()
        return finalResult

    def getAllClusteredBySecter(dateDeb,dateFin,sect):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        result=[]
        #st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        finalResult.append(result)
        conn.close()
        return finalResult

    #By Resp
    def getAllPlanifiedByResps(dateDeb,dateFin,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            finalResult.append(result)
        conn.close()
        return finalResult

    def getAllDoneByResps(dateDeb,dateFin,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            finalResult.append(result)
        conn.close()
        return finalResult

    def getAllDoneAtTimeByResps(dateDeb,dateFin,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            finalResult.append(result)
        conn.close()
        return finalResult

    def getAllClusteredByResps(dateDeb,dateFin,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        for sect in Secteur.Find_All_Secters():
            #st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
            result=[]
            if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
            finalResult.append(result)
        conn.close()
        return finalResult

    def getAllPlanifiedBySecterByResps(dateDeb,dateFin,sect,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        result=[]
        #st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "P" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        finalResult.append(result)
        conn.close()
        return finalResult

    def getAllDoneBySecterByResps(dateDeb,dateFin,sect,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        result=[]
        #st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        finalResult.append(result)
        conn.close()
        return finalResult

    def getAllDoneAtTimeBySecterByResps(dateDeb,dateFin,sect,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        result=[]
        #st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "D" = \''''+'True'+'''\' and "dateDone"<="datePrevue" and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        finalResult.append(result)
        conn.close()
        return finalResult

    def getAllClusteredBySecterByResps(dateDeb,dateFin,sect,resp):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        finalResult=[]
        dateDeb=datetime.datetime.strptime(dateDeb, '%Y-%m-%d').date()
        dateFin=datetime.datetime.strptime(dateFin, '%Y-%m-%d').date()
        result=[]
        #st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
        if datetime.datetime.strptime(str(dateDeb.year)+"-1-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-3-31", '%Y-%m-%d').date():
                if datetime.datetime.strptime(str(dateFin.year)+"-1-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date():
                    st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(dateFin)+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    result.append(None)
                    result.append(None)
                    result.append(None)
                else:
                    st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(dateDeb)+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-3-31", '%Y-%m-%d').date())+'''\')));'''
                    cursor.execute(st)
                    res = cursor.fetchone()
                    result.append(res[0])
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        else:
                result.append(None)
                if datetime.datetime.strptime(str(dateDeb.year)+"-4-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-6-30", '%Y-%m-%d').date():
                    if datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date():
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        result.append(None)
                        result.append(None)
                    else:
                        st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-4-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-6-30", '%Y-%m-%d').date())+'''\')));'''
                        cursor.execute(st)
                        res = cursor.fetchone()
                        result.append(res[0])
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-1", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                else:
                    result.append(None)
                    if datetime.datetime.strptime(str(dateDeb.year)+"-7-1", '%Y-%m-%d').date()<=dateDeb<=datetime.datetime.strptime(str(dateDeb.year)+"-9-30", '%Y-%m-%d').date():
                        if datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date():
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            result.append(None)
                        else:
                            st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-7-1", '%Y-%m-%d').date())+'''\' and \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-9-30", '%Y-%m-%d').date())+'''\')));'''
                            cursor.execute(st)
                            res = cursor.fetchone()
                            result.append(res[0])
                            if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
                    else:
                        result.append(None)
                        if datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date()<=dateFin<=datetime.datetime.strptime(str(dateFin.year)+"-12-31", '%Y-%m-%d').date():
                                st='''SELECT count(*) from public."Action" where "C" = \''''+'True'+'''\' and \''''+resp+'''\' && "resp" and "idProb" in (select "idProb" from public."Problem" where "idAxe" in (select "idAxe" from public."Axe" where "idPA" in (select "idPA" from public."PA" where "secteurPA" = \''''+str(sect)+'''\' and "datePA" between \''''+str(datetime.datetime.strptime(str(dateFin.year)+"-10-1", '%Y-%m-%d').date())+'''\' and \''''+str(dateFin)+'''\')));'''
                                cursor.execute(st)
                                res = cursor.fetchone()
                                result.append(res[0])
        finalResult.append(result)
        conn.close()
        return finalResult

    def Update_dateCloture(dateCloture,idAct):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        if dateCloture is None:
            st="""UPDATE public."Action" SET "dateCloture" =null WHERE "idAct" = """+str(idAct)+""";commit;"""
        else:
            dateCloture=str(dateCloture)
            st="""UPDATE public."Action" SET "dateCloture" =\'"""+dateCloture+"""\' WHERE "idAct" = """+str(idAct)+""";commit;"""
        cursor.execute(st)
        conn.close()

    def Update_dateDone(dateDone,idAct):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        if dateDone is None:
            st="""UPDATE public."Action" SET "dateDone" =null WHERE "idAct" = """+str(idAct)+""";commit;"""
        else:
            dateDone=str(dateDone)
            st="""UPDATE public."Action" SET "dateDone" =\'"""+dateDone+"""\' WHERE "idAct" = """+str(idAct)+""";commit;"""
        cursor.execute(st)
        conn.close()

    def UpdateAction(act):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(act.resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        datePrevue=str(act.datePrevue)
        st="""UPDATE public."Action" SET cause =\'"""+act.cause+"""\',action =\'"""+act.action+"""\',resp =\'"""+resp+"""\',"datePrevue"=\'"""+datePrevue+"""\' WHERE "idAct" = """+str(act.idAct)+""";commit;"""
        cursor.execute(st)
        conn.close()

    def Find_By_id(idAct):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idAct=str(idAct)
        st='''SELECT "idAct","cause","action","resp","datePrevue","P","D","C","A","idProb","nbAct" from public."Action" where "idAct"='''+idAct+''';'''
        cursor.execute(st)
        res = cursor.fetchone()
        conn.close()
        s = Action()
        s.idAct=int(res[0])
        s.cause=res[1]
        s.action=res[2]
        s.resp=res[3]
        q=""
        for r in s.resp:
            q+=User.FindById(r)+', '
        s.resp=q[:-2]
        s.datePrevue=res[4]
        s.P=res[5]
        s.D=res[6]
        s.C=res[7]
        s.A=res[8]
        s.idProb=int(res[9])
        s.nbAct=int(res[10])
        return s 

    def Find_By_idAct(idAct):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idAct=str(idAct)
        st='''SELECT "idAct","cause","action","resp","datePrevue","P","D","C","A","idProb","nbAct" from public."Action" where "idAct"='''+idAct+''';'''
        cursor.execute(st)
        res = cursor.fetchone()
        conn.close()
        s = Action()
        s.idAct=int(res[0])
        s.cause=res[1]
        s.action=res[2]
        s.resp=res[3]
        s.datePrevue=res[4]
        s.P=res[5]
        s.D=res[6]
        s.C=res[7]
        s.A=res[8]
        s.idProb=int(res[9])
        s.nbAct=int(res[10])
        return s 

    def Find_All():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='''SELECT "idAct","cause","action","resp","datePrevue","P","D","C","A","idProb","nbAct" from public."Action"'''
        cursor.execute(str)
        result = cursor.fetchall()
        conn.close()
        all = []
        for res in result:
            s = Action()
            s.idAct=int(res[0])
            s.cause=res[1]
            s.action=res[2]
            s.resp=int(res[3])
            s.resp=User.FindById(s.resp)
            s.datePrevue=res[4]
            s.P=res[5]
            s.D=res[6]
            s.C=res[7]
            s.A=res[8]
            s.idProb=int(res[9])
            s.nbAct=int(res[10])
            all.append(s)
        return all    

    def Find_All_By_idProb_and_userImm(idProb,userImm):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idProb=str(idProb)
        userImm=str(userImm)
        st='''SELECT "idAct","cause","action","resp","datePrevue","P","D","C","A","idProb","nbAct" from public."Action" where "idProb"='''+idProb+''' and \'{'''+userImm+'''}\' && "resp" order by "idAct" asc;'''
        cursor.execute(st)
        result = cursor.fetchall()
        conn.close()
        all = []
        for res in result:
            s = Action()
            s.idAct=int(res[0])
            s.cause=res[1]
            s.action=res[2]
            s.resp=res[3]
            q=""
            for r in s.resp:
                q+=User.FindById(r)+', '
            s.resp=q[:-2]
            s.datePrevue=res[4]
            s.P=res[5]
            s.D=res[6]
            s.C=res[7]
            s.A=res[8]
            s.idProb=int(res[9])
            s.nbAct=int(res[10])
            all.append(s)
        return all 

    def Find_All_By_idProb(idProb):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idProb=str(idProb)
        st='''SELECT "idAct","cause","action","resp","datePrevue","P","D","C","A","idProb","nbAct" from public."Action" where "idProb"='''+idProb+'''order by "idAct" asc;'''
        cursor.execute(st)
        result = cursor.fetchall()
        conn.close()
        all = []
        for res in result:
            s = Action()
            s.idAct=int(res[0])
            s.cause=res[1]
            s.action=res[2]
            s.resp=res[3]
            q=""
            for r in s.resp:
                q+=User.FindById(r)+', '
            s.resp=q[:-2]
            s.datePrevue=res[4]
            s.P=res[5]
            s.D=res[6]
            s.C=res[7]
            s.A=res[8]
            s.idProb=int(res[9])
            s.nbAct=int(res[10])
            all.append(s)
        return all 

    def Insert(p):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        resp=str(p.resp)
        resp=resp.replace('[','{')
        resp=resp.replace(']','}')
        datePrevue=str(p.datePrevue)
        P=str(p.P)
        D=str(p.D)
        C=str(p.C)
        A=str(p.A)
        idProb=str(p.idProb)
        nbAct=str(p.nbAct)
        st='INSERT INTO public."Action"(cause,action,resp,"datePrevue","P","D","C","A","idProb","nbAct") VALUES (\''+p.cause+'\',\''+p.action+'\',\''+resp+'\',\''+datePrevue+'\','+P+','+D+','+C+','+A+','+idProb+','+nbAct+');commit;'
        cursor.execute(st)
        conn.close()

    def Count_By_idProb(idProb):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idProb=str(idProb)
        st='''SELECT max("nbAct") from public."Action" where "idProb"='''+idProb+''';'''
        cursor.execute(st)
        result = cursor.fetchone()
        conn.close()
        return result[0] 

    def Update_P(idAct,P):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        P=str(P)
        idAct=str(idAct)
        st='UPDATE public."Action" SET "P"='+P+' WHERE "idAct"='+idAct+';commit;'
        cursor.execute(st)
        conn.close()

    def Update_D(idAct,D):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        D=str(D)
        idAct=str(idAct)
        st='UPDATE public."Action" SET "D"='+D+' WHERE "idAct"='+idAct+';commit;'
        cursor.execute(st)
        conn.close()  

    def Update_C(idAct,C):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        C=str(C)
        idAct=str(idAct)
        st='UPDATE public."Action" SET "C"='+C+' WHERE "idAct"='+idAct+';commit;'
        cursor.execute(st)
        conn.close()  

    def Update_A(idAct,A):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        A=str(A)
        idAct=str(idAct)
        st='UPDATE public."Action" SET "A"='+A+' WHERE "idAct"='+idAct+';commit;'
        cursor.execute(st)
        conn.close()

    def __str__(self) :
        return self.action

class Axe():
    idAxe = models.IntegerField()
    indicateur = models.CharField(max_length=1000)
    idPA = models.IntegerField()
    nbAxe = models.IntegerField()


    def Find_All():
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        str='''SELECT "idAxe","indicateur","idPA","nbAxe" from public."Axe"'''
        cursor.execute(str)
        result = cursor.fetchall()
        conn.close()
        all = []
        for res in result:
            s = Axe()
            s.idAxe=int(res[0])
            s.indicateur=res[1]
            s.idPA=int(res[2])
            s.nbAxe=int(res[3])
            all.append(s)
        return all    

    def Find_All_By_idPA(idPA):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idPA=str(idPA)
        st='''SELECT "idAxe","indicateur","idPA","nbAxe" from public."Axe" where "idPA"='''+idPA+'''order by "idAxe" asc;'''
        cursor.execute(st)
        result = cursor.fetchall()
        conn.close()
        all = []
        for res in result:
            s = Axe()
            s.idAxe=int(res[0])
            s.indicateur=res[1]
            s.idPA=int(res[2])
            s.nbAxe=int(res[3])
            all.append(s)
        return all 

    def Insert(p):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idPA=str(p.idPA)
        nbAxe=str(p.nbAxe)
        st='INSERT INTO public."Axe"(indicateur,"idPA","nbAxe") VALUES (\''+p.indicateur+'\','+idPA+','+nbAxe+');commit;'
        cursor.execute(st)
        conn.close()

    def Count_By_idPA(idPA):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idPA=str(idPA)
        st='''SELECT max("nbAxe") from public."Axe" where "idPA"='''+idPA+''';'''
        cursor.execute(st)
        result = cursor.fetchone()
        conn.close()
        return result[0] 

    def Find_By_idAxe(idAxe):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        idAxe=str(idAxe)
        st='''SELECT "idAxe","indicateur","idPA","nbAxe" from public."Axe" where "idAxe"='''+idAxe+''';'''
        cursor.execute(st)
        res = cursor.fetchone()
        conn.close()
        s = Axe()
        s.idAxe=int(res[0])
        s.indicateur=res[1]
        s.idPA=int(res[2])
        s.nbAxe=int(res[3])
        return s    

    def UpdateAxe(axe):
        conn = psycopg2.connect(database="ActionManagement", user='postgres', password='root', host='127.0.0.1', port= '5432')
        cursor = conn.cursor()
        st="""UPDATE public."Axe" SET "indicateur" =\'"""+axe.indicateur+"""\' WHERE "idAxe" = """+str(axe.idAxe)+""";commit;"""
        cursor.execute(st)
        conn.close()

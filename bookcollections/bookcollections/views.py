from django.shortcuts import render
from .models import EmpOperations
from pymongo import MongoClient


def home(request):
    dic={}
    dic['developer']='Yash Book Collections'
    dic['company']='Wellcome to BookStore'
    return render(request,"index.html",dic)

def login(request):
    page=None
    
    if request.method=="POST":
        id=request.POST.get("uid")
        ps=request.POST.get("psw")
        obj=EmpOperations()
        page=obj.checkuser(id,ps)
        
        return render(request,page)
    
def searchbook(request):
    return render(request,'Searchbook.html')

def searchbookonid(request):
    books = []  
    
    if request.method == "POST":
        fid = request.POST.get("author")
        dic = {"author": fid} 
        print(dic)
        client = MongoClient("mongodb+srv://yashbajaj:Yash#$2000@yashcluster.krjhict.mongodb.net/?retryWrites=true&w=majority&appName=YashCluster")
        db = client["yashdb"]
        coll = db["books"]
        books = list(coll.find(dic))
        client.close()
    
    return render(request, "BookSearchData.html", {'books': books})  


def newbk(request):
    return render(request,"Newbooksadd.html")
        
def addbook(request):
    msg = None
    
    if request.method == "POST":
        try:
            # Get data from POST request
            tf = request.POST.get("title")
            au = request.POST.get("author")
            ge = request.POST.get("genre")
            py = float(request.POST.get("published_year"))
            ib = float(request.POST.get("isbn"))
            pg = int(request.POST.get("pages"))
            lan = request.POST.get("language")
            pub = request.POST.get("publisher")
            
            # Validate input data
            if not all([tf, au, ge, py, ib, pg, lan, pub]):
                raise ValueError("All fields are required")
            
            # Create an instance of EmpOperations class
            obj = EmpOperations()
            
            # Call addnewemp method and get the status message
            msg = obj.addnewemp(tf, au, ge, py, ib, pg, lan, pub)
            
        except ValueError as ve:
            msg = str(ve)
        except Exception as e:
            msg = f"Error: {e}"
        
        dic = {'status': msg}
        
        return render(request, "NewBookstaus.html", dic)
    
    return render(request, "NewBookstaus.html")  # Return the form on GET request





def delbk(request):
    return render(request,"Deletebook.html")

def delete(request):
    if request.method=="POST":
        try:
           id=request.POST.get('isbn')
           dic={}
           dic["isbn"]=id
           print(dic)

           client = MongoClient("mongodb+srv://yashbajaj:Yash#$2000@yashcluster.krjhict.mongodb.net/?retryWrites=true&w=majority&appName=YashCluster")
           db = client["yashdb"]
           coll = db["books"]
           coll.delete_one(dic)
           print("delete succesfully")
           msg=("Deleted Succesfully")
        except:
         print("error in code")   
         msg=("Book Not Found")

        dic={}
        dic["status"]=msg
        return render(request,"DeleteStatus.html",dic)





def updAuthor(request):
    return render(request,"Updateauthor.html")

def chauthor(request):
    ya=None 
    if request.method=="POST":
       try:
          ti=request.POST.get("title")
          au=request.POST.get("author")
          ge=request.POST.get("genre")
          py=request.POST.get("published_year")
          ib=request.POST.get("isbn")
          pa=request.POST.get("pages")
          la=request.POST.get("language")
          pg=request.POST.get("publisher")

          dic={}
          dic['isbn']=ib
          ch={}
          ch['title']=ti
          ch['author']=au
          ch['genre']=ge
          ch['published_year']=py
          ch['pages']=pa
          ch['language']=la
          ch['publisher']=pg
          upd={'$set':ch}
          client = MongoClient("mongodb+srv://yashbajaj:Yash#$2000@yashcluster.krjhict.mongodb.net/?retryWrites=true&w=majority&appName=YashCluster")
          db = client["yashdb"]
          coll = db["books"]
          coll.update_one(dic,upd)
          print("update succesfully")
          ya=("Update Succesfully")
       except:
         print("error")
         ya=("Error In Update")

    dic={}  
    dic['status']=ya
   
    return render(request,"Upauthor.html",dic)
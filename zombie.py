import random
first = ["John",'Julius','Esther','Justin','Priscilia',"Young man","Burna","Green","Emrican","White",'Whice','Hustle',"Gopy","Marla",'Shorya',"Emtee","Nicki",'Dan','Love','Fredie',"Brenda",'Lingard',"Limpo",'Dembele','Anabelle','Kiki',"Sandra",'Casandra','Philine','Coutiho','Cavati',"Montana",'Wayne',"Jordan","Paul",'Chris',"Bond","James","Edward","Charles","Babbage","Bill","Jack","Dunlop","Slipey",'Mark','Cara',"Mercy","Berger","Hummit"]
last = ["Alexander","McCall","Marcos",'Narcos','Edding',"Torgan","David","Becam","Emerson","Lorrience","Thompson","Lucas","Abraham","Subdila","Santos","Luke","Chelsea","Manchester","Barcelona","Honda","Rica","Smith","Richard","Paulinho","Einstein","Andrew","Gomez","Mizphabet","Donald","Sellini","Charlotte","Henry","Hewlette","Robert","Ford","Anderson","Willson","Mourinho","Hezekiah","Sebastian","Diego","Malcomm","McCoaster","Greenwich","Febo","Phelionni","Silver","Douglas","PyRodri","Kendrick"]
full =[]
for i in last:
    for x in first:
        full.append(i+' '+x)
year = 0
y=["NaN","NaN","NaN","NaN","NaN"]
dep1=''
ent = 0
dep =['Biochemistry',"Physics",'Statistics','Software Programming','Cyber Security','Computer Science','Civil Engineering','Building Technology','Micro Biology','Geology','Bio Technology','Information Technology',"Computer Engineering",'Mechganical Engineering','Architecture','Mining Engineering','Survey and Geo-informatics','Data Analysis',"Machine and Deep Engineering"]
with open("schoolProject.csv","w") as file:
    for i in range(20):
        random.shuffle(full)
    for x in full:
        y=["NaN","NaN","NaN","NaN","NaN"]
        dep1=random.choice(dep)
        year = random.randint(3,5)
        ent = 2019-year
        for i in range(year):
            d = str(round(random.randint(5,11)/2.5,1))
            y[i]=d
        file.seek(0,2)
        y = ','.join(y)
        file.write("{0},{1},{2},{3},{4}\n".format(x,dep1,y,year,ent))

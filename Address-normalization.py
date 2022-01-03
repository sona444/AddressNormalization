import json
import pgeocode
nomi = pgeocode.Nominatim('in')
f = open("address.txt", "r")
pincode=[]
i=1
p=1
dictionary={}
for x in f:
    if not x.strip():
            continue
    else:
            lis = list(x.strip().split(" "))
            length = len(lis)
            last=x[length-1]
            d=-1
            if len(last)<5:
                last=lis[-2]+lis[-1]
            last=''.join(i for i in last if i.isdigit())
            if last=='':
                last=lis[d-1]
                last=''.join(i for i in last if i.isdigit())

            for g in ['.','-','Maharashtra,','DELHI','Delhi-',',Mumbai-','India']:
                last.replace(g,"")
            # if not last.strip():
            #     if lis[-2].isdigit() and lis[-2]!=',':
            #         last=lis[-2]
            #     else:
            #         last=lis[-3]
            print(last)
            # if last.isdigit():
            y=nomi.query_postal_code(last)
            i=i+1
            if y['state_name'] in lis:
                lis.remove(y['state_name'])
            if y['postal_code'] in lis:
                lis.remove(y['postal_code'])
            if y['place_name'] in lis:
                lis.remove(y['place_name'])
            if y['county_name'] in lis:
                lis.remove(y['county_name'])
            if y['community_name'] in lis:
                lis.remove(y['community_name'])
            ['Hyderabad' if x=='hydrabad' or'hydrabadh' else x for x in lis]
            ['apartments' if x=='apt' else x for x in lis]
            ['next' if x=='nxt' else x for x in lis]
            ['near' if x=='nr' else x for x in lis]
            if len(lis)<12:
                lis.remove(lis[-3])
                lis.remove(lis[-2])
                lis.remove(lis[-1])
            elif len(lis)>12:
                lis.remove(lis[-4])
                lis.remove(lis[-3])
                lis.remove(lis[-2])
                lis.remove(lis[-1])
            lent=len(lis)//2
            if 'Hyderabad' in lis:
                lis.remove('Hyderabad')
            s=""
            add1=lis[0:lent-1]
            add2=lis[lent:len(lis)-1]
            for m in ['plot','Plot','Flat','flat']:
                if m in add2 and m not in add1:
                    find=add2.index(m)
                    add1.insert(0,add2[find])
                    add2.pop(find)
                    if find < len(add2)-1:
                        add1.insert(1,add2[find+1])
                        add2.pop(find+1)
                    if find+1 < len(add2)-1:
                        add1.insert(2,add2[find+2])
                        add2.pop(find+2)
            if ',' in add2:
                f=add2.index(',')
                if f==0:
                    add2.pop(0)
                elif f==1:
                    add1.insert(-1,add2[1])
                    add2.pop(1)
            s=" ".join(add1)
            s1=" ".join(add2)
            loc=str(y['place_name']).split(',')
            diction={
                "Address_line1":s,
                "Address_line2":s1,
                "locality":loc[-1],
                "city":y['community_name'],
                "state":y['state_name'],
                "pincode":y['postal_code'],
                "geocode":str(y['latitude'])+","+str(y['longitude'])
            }
    dictionary[p]=diction
    p=p+1
json_object = json.dumps(dictionary, indent = 4)
  
with open("output.json", "w") as outfile:
    outfile.write(json_object) 
           
from django.http import HttpResponse
import datetime
import json
from django.core import serializers

import mediator_app
from mediator_app import DBUtil
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache


from mediator_app import ProfileHelper

def index(request):
    return HttpResponse("Hello, world. You're at the mediator index.")

@never_cache
@csrf_exempt
def addUser(request):
    req = request.POST
    name = req['name']
    email = req['email_id']
    address = req['address']
    password = req['password']
    contactno = req['contact_no']

    ProfileHelper.addUser(name,address,contactno,email,password)
    return HttpResponse(json.dumps("{'sells':1}"), content_type='application/json')

@never_cache
@csrf_exempt
def addVolunteer(request):
    req = request.POST
    name = req['name']
    email = req['email_id']
    address = req['address']
    area = req['area']
    password = req['password']
    contactno = req['contact_no']

    ProfileHelper.addVolunteer(name,address,area,contactno,email,password)
    return HttpResponse(json.dumps("{'sells':1}"), content_type='application/json')

@never_cache
@csrf_exempt
def getUser(request):
    req = request.POST
    email_id = req['email_id']

    query_set = mediator_app.models.User.objects.filter(email_id = email_id)

    #query = "Select * from User u where u.email_id ="  + email_id
    #db_resp_list = DBUtil.sql_select(query)

    #user = db_resp_list
    #json_ret = json.dumps(user)
    #print(json_ret)
    #return HttpResponse(json_ret, content_type='application/json')

    json_data = serializers.serialize('json', query_set)
    data = json.loads(json_data)
    l = list()
    mydata = dict()
    user = dict()

    id = data[0]['pk']
    print(id)
    for d in data:
        x = d['fields']
        l.append(x)
    temp = dict()

    mydata['User'] = l[0]
    mydata['id'] = id
    print(mydata)

    return HttpResponse(json.dumps(mydata), content_type='application/json')

@never_cache
@csrf_exempt
def getUserFromUserId(request):
    req = request.POST
    user_id = req['user_id']

    query_set = mediator_app.models.User.objects.filter(user_id = user_id)

    json_data = serializers.serialize('json', query_set)
    data = json.loads(json_data)
    l = list()
    mydata = dict()

    id = data[0]['pk']
    print(id)
    for d in data:
        x = d['fields']
        l.append(x)

    mydata['User'] = l[0]
    mydata['id'] = id
    print(mydata)

    return HttpResponse(json.dumps(mydata), content_type='application/json')

@never_cache
@csrf_exempt
def getVolunteer(request):
    req = request.POST
    email_id = req['email_id']

    query_set = mediator_app.models.Volunteer.objects.filter(email_id = email_id)

    json_data = serializers.serialize('json', query_set)
    data = json.loads(json_data)
    l = list()
    mydata = dict()

    id = data[0]['pk']
    print(id)
    for d in data:
        x = d['fields']
        l.append(x)

    mydata['Volunteer'] = l[0]
    mydata['id'] = id
    print(mydata)

    return HttpResponse(json.dumps(mydata), content_type='application/json')

@never_cache
@csrf_exempt
def addMedicine(request):
    req = request.POST
    name = req['name']
    user_id = req['user_id']
    barcode = req['barcode']
    expiry_date = req['expiry_date']
    use = req['use']
    dosage = req['dosage']
    start_date = req['start_date']
    end_date = req['end_date']

    #check if medicine is available in medicine table -> if not then add it
    query = mediator_app.models.Medicine.objects.filter(med_barcode = barcode)
    json_data = serializers.serialize('json', query)
    data = json.loads(json_data)

    print("data=")
    print(data)
    if data == []:
        ProfileHelper.addMedicine(name,barcode,use)

    query = mediator_app.models.Medicine.objects.filter(med_barcode=barcode)
    json_data = serializers.serialize('json', query)
    data = json.loads(json_data)

    print("med_id=")
    print(data[0]['pk'])
    med_id = data[0]['pk']
    print("user_id=")
    print(user_id)
    user = mediator_app.models.User.objects.filter(pk=user_id)

    #Add medicine to user's records (user medicine table)
    ProfileHelper.addUserMedicine(user_id, med_id, expiry_date, use, dosage)

    return HttpResponse(json.dumps("{'sells':1}"), content_type='application/json')

@never_cache
@csrf_exempt
def getMedicineRecords(request):
    req = request.POST
    user_id = req['user_id']

    query = mediator_app.models.UserMedicine.objects.filter(user_id=1)
    json_data =serializers.serialize('json',query)
    data = json.loads(json_data)

    print(data)

    l = list()
    mydata = dict()
    for d in data:
        x = d['fields']
        #get medicine details
        query = mediator_app.models.Medicine.objects.filter(med_id=x['medicine'])
        json_data=serializers.serialize('json',query)
        data = json.loads(json_data)
        print("##############")
        print(data[0]['fields'])
        x['med_name'] = data[0]['fields']['med_name']
        l.append(x)

    mydata = dict()
    mydata['medicine_record_list'] = l
    print(mydata)
    return HttpResponse(json.dumps(mydata), content_type='application/json')

@never_cache
@csrf_exempt
def getPickupRequests(request):
    req = request.POST
    volunteer_id = req['volunteer_id']

    query = mediator_app.models.Donation.objects.filter(volunteer_id=1)
    json_data =serializers.serialize('json',query)
    data = json.loads(json_data)

    print(data)

    l = list()
    mydata = dict()
    for d in data:
        x = d['fields']
        #get user details
        query = mediator_app.models.User.objects.filter(user_id=x['user_id'])
        json_data=serializers.serialize('json',query)
        data = json.loads(json_data)
        print("##############")
        print(data[0]['fields'])
        x['name'] = data[0]['fields']['name']
        x['address'] = data[0]['fields']['address']
        x['contact_no'] = data[0]['fields']['contact_no']
        l.append(x)

    mydata = dict()
    mydata['pickup_request_list'] = l
    print(mydata)
    return HttpResponse(json.dumps(mydata), content_type='application/json')


@never_cache
@csrf_exempt
def addPickupRequst(request):
    req = request.POST
    name = req['name']
    user_id = req['user_id']
    barcode = req['barcode']
    expiry_date = req['expiry_date']
    quantity = req['quantity']

    #check if medicine is available in medicine table -> if not then add it
    query = mediator_app.models.Medicine.objects.filter(med_barcode = barcode)
    json_data = serializers.serialize('json', query)
    data = json.loads(json_data)

    print("data=")
    print(data)
    if data == []:
        ProfileHelper.addMedicine(name,barcode,"N/A") #putting N/A for use

    query = mediator_app.models.Medicine.objects.filter(med_barcode=barcode)
    json_data = serializers.serialize('json', query)
    data = json.loads(json_data)

    print("med_id=")
    print(data[0]['pk'])
    medicine_id = data[0]['pk']
    med_id = data[0]['pk']
    print("user_id=")
    print(user_id)

    #Add donation record
    ProfileHelper.addDonation(user_id, "Request Created", medicine_id,expiry_date, quantity) # status = request created, volunteer assigned, picked up, done

    return HttpResponse(json.dumps("{'sells':1}"), content_type='application/json')



from mediator_app.models import User, Medicine, UserMedicine, Volunteer, Donation

def addUser(name,address,contactno,email,password):
    u = User(name = name,
            contact_no = contactno,
            address = address,
            email_id = email,
            password = password
             )
    u.save()

def addVolunteer(name,address,area,contactno,email,password):
    u = Volunteer(name = name,
            contact_no = contactno,
            address = address,
            area = area,
            email_id = email,
            password = password
             )
    u.save()


#update medicine table - add new medicine to medicine table
def addMedicine(name,barcode,use):
    m = Medicine(med_name = name,
                 med_barcode = barcode,
                 med_use = use)
    m.save()


#add a medicine to user's record
def addUserMedicine(user_id, med_id, expiry_date, use, dosage,start_date,end_date):
    u = User.objects.filter(user_id=user_id)
    m = Medicine.objects.filter(med_id=med_id)

    um = UserMedicine(user = u[0],
                      medicine = m[0],
                      expiry_date = expiry_date,
                      use = use,
                      dosage = dosage,
                      start_date=start_date,
                      end_date=end_date)

    um.save()

def addDonation(user_id,status,medicine_id,expiry_date, quantity):
    u = User.objects.filter(user_id=user_id)
    m = Medicine.objects.filter(med_id=medicine_id)

    d = Donation(user = u[0],
                 status = status,
                 medicine = m[0],
                 expiry_date=expiry_date,
                 quantity =quantity
                 )
    d.save()

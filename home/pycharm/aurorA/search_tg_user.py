

def phone_vlidation():
    phone=input("victims phone(+36 123 456 7891): ")
    m_phone = "+".split(phone)
    if len(m_phone) != 12 and phone[0:2] == "360":
        return False
    return True


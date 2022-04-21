def fun(s):
    try:
        user, other = s.split("@")
        web,ext = other.split(".")
        if not user or not web or not ext:
            return False
        if user!= "".join(filter(lambda x: x.isalnum() or x in ["_","-"], user)):
            return False
        if web!= "".join(filter(lambda x:x.isalnum(),web)):
            return False
        if len(ext)>3:
            return False
        return True
    except:
        return False
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

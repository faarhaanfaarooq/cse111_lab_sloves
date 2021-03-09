def replace_domain(mail, new_domain = "sheba.xyz", old_domain = "kaj.com"):
    if new_domain in mail:
        return "Unchanged: "+mail
    else:
        mail = mail.split('@')
        mail[1] = new_domain
        mail = mail[0]+"@"+mail[1]
        return "Changed: "+mail

print(replace_domain("alice@kaaj.com", "sheba.xyz", "kaaj.com"))
print(replace_domain("bob@sheba.xyz", "sheba.xyz"))
import csv, yagmail

mail = yagmail.SMTP('andrejsaule8@gmail.com')
#Opens and gets computer to read the csv file you created
    #You can make as many columns as you want and then put them as a placeholder
with open("test_test.csv") as file:
    reader = csv.reader(file)
    next(reader) #skip header row of file
    for email, name, corp in reader:
        print(f"Sending email to {name}")
        #You can create and style the body of the email with some HTML below using tags etc.
        #f infront of the quote marks will determine that it is a function
        #I added a signature below from the src= 'file_url'
        contents = [
        f"""\<p> Insert body of email here {email}</p>
                <img src="reference attachments" width="497" height="etc" class="etc" tabindex="etc">
            <html>
        """,
        #Can add attachments as you would like to
        'Add_attachments_here_if_you_like.png',
        'Add_your_brocure_or_whatever.pdf'
        ]
        #This subject variable sets the subject line of the email
        #Include the f before any strings to insert the variables from .csv read
        subject = f'{corporation} Wellness - Mindfulness Program 2019'
        #Finally we send the email!
        mail.send(f'{email}', subject, contents)

#ez_pz

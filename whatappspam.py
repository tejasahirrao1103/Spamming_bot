def whatapp():
    import pyautogui,time,webbrowser
    print("""
               __          __                                                                          
     _      __/ /_  ____ _/ /__________ _____  ____     _________  ____ _____ ___  ____ ___  ___  _____
    | | /| / / __ \/ __ `/ __/ ___/ __ `/ __ \/ __ \   / ___/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/
    | |/ |/ / / / / /_/ / /_(__  ) /_/ / /_/ / /_/ /  (__  ) /_/ / /_/ / / / / / / / / / / /  __/ /    
    |__/|__/_/ /_/\__,_/\__/____/\__,_/ .___/ .___/  /____/ .___/\__,_/_/ /_/ /_/_/ /_/ /_/\___/_/     
                                     /_/   /_/           /_/                                           
    \n""")

    print(">>>>>>>>>>>>>>>>>>>>  OPEN WHATSAPP ON WHATSAPP WEB IN DEFAULT BROWSER  <<<<<<<<<<<<<<<<<<\n")

    n=input("Enter phone number without +91 and space :- ")

    while len(n)!=10:
            n=input("Number is invalid Re-Enter number:-")

    b=input("enter massage that that you want to SPAM:- ")

    a=int(input("enter the Spam count [SPAM WILL START IN 10 SEC AFTER ENTER]:- "))

    link="http://web.whatsapp.com/send/?phone=91"+n+"&text&type=phone_number&app_absent=0"
    webbrowser.open(link)

    time.sleep(12)
    while (0<a):
        pyautogui.typewrite(b)
        pyautogui.press("enter")
        a=a-1
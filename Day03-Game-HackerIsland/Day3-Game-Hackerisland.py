import base64
def banner():
    print('''
##########################################
# Welcome to hacker island!              #
# Your mission is to exploit North Korea.#
##########################################
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"

''')


def start_game(banner):
    choice1a = base64.b64decode("cG9ydF9zY2Fu").decode('ascii')
    choice1b = base64.b64decode("b3NpbnQ=").decode('ascii')
    choice2a = base64.b64decode("MGRheQ==").decode('ascii')
    choice2b = base64.b64decode("YXV0b3B3bg==").decode('ascii')

    choice1 = input("Would you like to use \"port_scan\" or \"OSINT\" to find open ports? ").lower()
    if choice1 == choice1a: # port scan
        print("The SOC detected your traffic and has blocked your IP. Game Over")

    elif choice1 == choice1b: # osint
        print("""Nice work, using Shodan you have passively mapped the external network and found an exploitable service
running on port 445.You are ready to launch an attack.\n""")

        choice2 = input("What attack should you launch? Your new name pipe \"0day\" or Metasploit \"AutoPwn\"?")
        if choice2 == choice2a:  # oday
            print("Your slick exploit had a bug and now the blue team is laughing at your red team skillz. Try again noob.")

        elif choice2 == choice2b:  # autopwn
            print("""REVERSE SHELL! Metasploit hailmary attack saved your ass! 
You now have system level access and it's time to run Mimikatz.Dumping credz... You win!""")
        else:
            print("You shell has been terminated and IP banned. Try again.")

    else:
        print("You failed to find an exploitable service noob. Try again.")

start_game(banner())
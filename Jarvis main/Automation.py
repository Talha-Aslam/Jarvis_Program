"whatsapp jo app hai os kya liya ya libaray lagai"
# from os import startfile
import pywhatkit

# startfile('whatsapp://send?phone=+923235618150&text=Hello bander kaysy hu')
''''
ya baki program whatsapp web ka liya
'''
def WhatsappMsg(number,message):
  
     pywhatkit.sendwhatmsg_instantly(f'+92{number}'.replace(" ",""),message)

# WhatsappMsg("+923235618150","Hello bandar")
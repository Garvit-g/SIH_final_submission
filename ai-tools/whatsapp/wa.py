import pywhatkit
import datetime
cur = datetime.datetime.now()
hour = cur.hour
minute = cur.minute

def send_msg(phone, message):
   
    pywhatkit.sendwhatmsg(phone , message ,hour,minute+1)
    #pywhatkit.sendwhatmsg_to_group("F1kudL6wfAhEis2MgBalrK" , message ,hour,minute+1)
    #print("Successfully Sent!")
    
try:
    name = 'Arun Kumar'
    greeting = "Hello "+name+". Here is your Daily Update on PIB Press releases \n \n"
    message ='''1. IAS officers of 2020 batch call on the President

175 IAS officers of 2020 batch called on the President of India, Smt Droupadi Murmu at Rashtrapati Bhavan today. President said that by working with passion and pride, they can ensure that the India of 2047 will be much more prosperous, strong and happy.

https://www.pib.gov.in/PressReleasePage.aspx?PRID=1854323

2. Cabinet approves amendment to export policy for Wheat or Meslin Flour

Cabinet approves amendment to export policy for Wheat or Meslin Flour. Russia & Ukraine are the major exporters of wheat accounting for around 1/4th of the global wheat trade. The decision was taken to put a prohibition on export of wheat in May 2022.

https://www.pib.gov.in/PressReleasePage.aspx?PRID=1854352

3. Curtain raiser Commissioning of indigenous aircraft carrier

02 Sep 2022 will mark the historical milestone of realisation of Nation’s commitment towards ‘AatmaNirbharta’. Hon’ble Prime Minister would be the Chief Guest on this momentous occasion. Vikrant is the largest warship to have ever been built in India. It is also the first indigenously designed and built Aircraft Carrier.

https://www.pib.gov.in/PressReleasePage.aspx?PRID=1854457

4. Government notifies Battery Waste Management Rules, 2022

Ministry of Environment, Forest and Climate Change, Government of India published the Battery Waste Management Rules, 2022 on 24th August, 2022. The rules cover all types of batteries, viz. Electric Vehicle, automotive batteries and industrial batteries. They function based on the concept of Extended Producer Responsibility (EPR).

https://www.pib.gov.in/PressReleasePage.aspx?PRID=1854433


5. India-Mauritius 3rd Joint Committee Meeting on SME Cooperation

India-Mauritius 3rd Joint Committee Meeting on SME Cooperation held in New Delhi. Indian side was led by Shri Narayan Rane, Union Minister for Micro, Small and Medium Enterprises (MSME), Government of India. Mauritius side led by Shri Soomilduth Bholah, Union minister of Industrial Development, SMEs and Cooperatives.


https://www.pib.gov.in/PressReleasePage.aspx?PRID=1854400'''

    message = greeting+message
    #phone = "+919971390995"    
    #phone = "+919351016263"
    phone = "+919137813954"

    send_msg(phone, message)


except: 
    print("An Unexpected Error!")
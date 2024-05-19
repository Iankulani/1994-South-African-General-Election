# -*- coding: utf-8 -*-
"""

Created on Mon May  6 15:47:35 2024

@author: IAN CARTER KULANI
Phone:+265(0)988061969
E-mail:iancarterkulani@gmail.com
Purpose: The software prompts the user to enter total number of published centers,total 
number of registered  voters, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward,it determines the candidate with the majority of votes 
and displays the results on the screen.
#NOTE:For a candidate to be a majority winner of an election, the candidate total valid votes should 
be greater than majority votes, which is Fifty plus one. 

"""


print("=========================================SOUTH AFRICA 1994 PRESIDENTIAL ELECTION=========================================\n\n")



percent=100
#Get total number of published centers
Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Voters/Turnout:"))
Totalvotescast=int(input("Enter Total Votes Cast/Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes/Invalid Votes:"))
#Get Total Valid Votes
Totalvalidvotes=int(input("Enter Total Valid Votes:"))

#Get Total Valid Votes for African National Congress
Totalvalidvotesfor_African_National_Congress=int(input("Enter Total Valid Votes for African National Congress:"))
#Get Total Vald Votes for National Party
Totalvalidvotesfor_National_Party=int(input("Enter Total Valid Votes for Natinal Party:")) 
#Get Total Vald Votes for Inkatha Freedom Party  
Totalvalidvotesfor_Inkatha_Freedom_Party=int(input("Enter Total Valid Votes for Inkatha Freedom Party:"))
#Get Total Vald Votes for Freedom Front
Totalvalidvotesfor_Freedom_Front=int(input("Enter Total Valid Votes for Freedom Front:"))
#Get Total Vald Votes for Democratic Party
Totalvalidvotesfor_Democratic_Party=int(input("Enter Total Valid Votes for Democratic Party:"))
#Get Total Vald Votes for Pan African Congress
Totalvalidvotesfor_Pan_African_Congress=int(input("Enter Total Valid Votes for Pan African Congress:"))
#Get Total Vald Votes for African Christian Democratic Party
Totalvalidvotesfor_African_Christian_Democratic_Party=int(input("Enter Total Valid Votes for African Christian Democratic Party:"))
#Get Total Vald Votes for Africa Muslim Party
Totalvalidvotesfor_Africa_Muslim_Party=int(input("Enter Total Valid Votes for African Muslim Party:"))
#Get Total Vald Votes for African Moderates Congress Party
Totalvalidvotesfor_African_Moderates_Congress_Party=int(input("Enter Total Valid Votes for African Moderates Congress Party:"))
#Get Total Valid Votes for Dikwankwetla Party
Totalvalidvotesfor_Dikwankwetla_Party=int(input("Enter Total Valid Votes for Dikwankwetla Party:"))
#Get Total Vald Votes for Federal_Party
Totalvalidvotesfor_Federal_Party=int(input("Enter Total Valid Votes for Federal Party:"))
#Get Total Vald Votes for Minolity Party
Totalvalidvotesfor_Minolity_Party=int(input("Enter Total Valid Votes for Minolity Party:"))
#Get Total Vald Votes for Sport Organisation for Collective Contribution and Equal Rights
Totalvalidvotesfor_Sport_Organisation_for_Collective_Contribution_and_Equal_Rights=int(input("Enter Total Valid Votes for Sport Organisation for Collective Contribution and Equal Rights:"))
#Get Total Vald Votes for  Africa Democratic Movement
Totalvalidvotesfor_Africa_Democratic_Movement=int(input("Enter Total Valid Votes for Africa Democratic Movement:"))
#Get Total Vald Votes for Women's Rights Peace Party
Totalvalidvotesfor_Women_Rights_Peace_Party=int(input("Enter Total Valid Votes for Women's Rights Peace Party:"))  
#Get Total Valid Votes for Ximoko Progresive Party
Totalvalidvotesfor_Ximoko_Progresive_Party=int(input("Enter Total Valid Votes for Ximoko Progresive Party:"))
#Get Total Vald Votes for Keep it Straight and Simple Party
Totalvalidvotesfor_Keep_it_Straight_and_Simple_Party=int(input("Enter Total Valid Votes for Keep it Straight and Simple Party:"))
#Get Total Vald Votes for Workers List Party
Totalvalidvotesfor_Workers_List_Party=int(input("Enter Total Valid Votes for Workers List Party:"))
#Get Total Vald Votes for Luso South Africa Party 
Totalvalidvotesfor_Luso_South_Africa_Party=int(input("Enter Total Valid Votes for Luso South Africa Party:")) 


#Decision Making

if Totalvalidvotesfor_African_National_Congress>Totalvalidvotes/2+1 :
    print("Congratulations to the African National Congress For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_National_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the National Party For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_Inkatha_Freedom_Party>Totalvalidvotes/2+1: 
    print("Congratulations to theInkatha Freedom Party  For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Freedom_Front>Totalvalidvotes/2+1 :
        print("Cogratulations to the Freedom Front For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Democratic_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Democratic Party For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Pan_African_Congress>Totalvalidvotes/2+1: 
    print("Congratulations to the Pan African Congress For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_African_Christian_Democratic_Party>Totalvalidvotes/2+1 :
        print("Congratulations to the African Christian Democratic Party For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Africa_Muslim_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Africa Muslim Party you're a winner of 1994 election\n\n")
elif Totalvalidvotesfor_African_Moderates_Congress_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the African Moderates Congress Party For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Dikwankwetla_Party>Totalvalidvotes/2+1:
      print("Congratulations to the Dikwankwetla Party  For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Federal_Party>Totalvalidvotes/2+1 :
        print("Congratulations to the Federal Party  For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Minolity_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Minolity Party  For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Sport_Organisation_for_Collective_Contribution_and_Equal_Rights>Totalvalidvotes/2+1: 
    print("Congratulations to theSport Organisation for Collective Contribution_and_Equal_Rights  For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Africa_Democratic_Movement>Totalvalidvotes/2+1 :
        print("Congratulations to the Africa Democratic Movement  For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Women_Rights_Peace_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Women Rights Peace Party  For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Ximoko_Progresive_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Ximoko Progresive Party  For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Keep_it_Straight_and_Simple_Party>Totalvalidvotes/2+1 :
        print("Congratulations to the Keep it Straight and Simple Party For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Workers_List_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Democratic Party  For Winning 1994 Election\n\n")
elif Totalvalidvotesfor_Luso_South_Africa_Party>Totalvalidvotes/2+1: 
    print("Congratulations to the Luso South Africa Party For Winning 1994 Election\n\n")
else:
    print("No majority winner was found RUNOFF may be required\n")


print("__________________________________________________________ELECTION STATISTICS__________________________________________________________\n")
#calculating percentage 
#Calculating percentage for total votes cast
Percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",Percentage)
#Calculating percentage for total valid votes for all canidates
Percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",Percentage)
#Calculating percentage for null_&_void votes
Percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void votes in percentage=",Percentage)
#Calculating percentage for Total Registered voters/turnout
Percentage=round(Totalvotescast*percent/TotalRegisteredvotes, 2);
print("Total Registered voters/turnout in percentage=",Percentage)
#Calculating percentage for African National Congress
Percentage=round(Totalvalidvotesfor_African_National_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African National Congress in Percentage=",Percentage)
#Calculating percentage for National Party
Percentage=round(Totalvalidvotesfor_National_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for National Party in percentage=",Percentage)
#Calculating percentage for Inkatha Freedom Party
Percentage=round(Totalvalidvotesfor_Inkatha_Freedom_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Inkatha Freedom Party in percentage=",Percentage) 
#Calculating percentage for Freedom Front
Percentage=round(Totalvalidvotesfor_Freedom_Front*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Freedom Front in Percentage=",Percentage)
#Calculating percentage for Democratic Party
Percentage=round(Totalvalidvotesfor_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Democratic Party in percentage=",Percentage)
#Calculating percentage for Pan African Congress
Percentage=round(Totalvalidvotesfor_Pan_African_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Pan African Congress in percentage=",Percentage) 
#Calculating percentage for African Christian Democratic Party
Percentage=round(Totalvalidvotesfor_African_Christian_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African Christian Democratic Party in Percentage=",Percentage)
#Calculating percentage for Pan African Congress
Percentage=round(Totalvalidvotesfor_Pan_African_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Pan African Congress in percentage=",Percentage)
#Calculating percentage for African Christian Democratic Party 
Percentage=round(Totalvalidvotesfor_African_Christian_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African Christian Democratic Party in percentage=",Percentage) 
#Calculating percentage for Africa Muslim Party
Percentage=round(Totalvalidvotesfor_Africa_Muslim_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Africa Muslim Party in Percentage=",Percentage)
#Calculating percentage for African Moderates_Congress Party
Percentage=round(Totalvalidvotesfor_African_Moderates_Congress_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African Moderates Congress Party in percentage=",Percentage)
#Calculating percentage for Dikwankwetla Party
Percentage=round(Totalvalidvotesfor_Dikwankwetla_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Dikwankwetla Party in percentage=",Percentage)
#Calculating percentage for Federal Party
Percentage=round(Totalvalidvotesfor_Federal_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Federal Party in percentage=",Percentage) 
#Calculating percentage for Minolity Party
Percentage=round(Totalvalidvotesfor_Minolity_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Minolity Party in percentage=",Percentage) 
#Calculating percentage for Sport Organisation for Collective Contribution and Equal Rights
Percentage=round(Totalvalidvotesfor_Sport_Organisation_for_Collective_Contribution_and_Equal_Rights*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Sport Organisation for Collective Contribution and Equal Rights in Percentage=",Percentage)
#Calculating percentage for Africa Democratic Movement  
Percentage=round(Totalvalidvotesfor_Africa_Democratic_Movement*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Africa Democratic Movement in percentage=",Percentage)
#Calculating percentage for Women Rights Peace Party
Percentage=round(Totalvalidvotesfor_Women_Rights_Peace_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Women Rights Peace Party in percentage=",Percentage) 
#Calculating percentage for Africa Ximoko Progresive Party
Percentage=round(Totalvalidvotesfor_Ximoko_Progresive_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Ximoko Progresive Party in Percentage=",Percentage)
#Calculating percentage for Keep it Straight and Simple Party
Percentage=round(Totalvalidvotesfor_Keep_it_Straight_and_Simple_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Keep it Straight and Simple Party in percentage=",Percentage)
#Calculating percentage for Workers List Party
Percentage=round(Totalvalidvotesfor_Workers_List_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Workers List Party in percentage=",Percentage) 
#Calculating percentage for Luso South Africa Party
Percentage=round(Totalvalidvotesfor_Luso_South_Africa_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Luso South Africa Party in percentage=",Percentage) 


print("=========================================================================================================================\n\n\n")   

import streamlit as st
import datetime as dt
import FunctionWebApp as fw
import time
import smtplib, ssl
import yagmail
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from tempfile import NamedTemporaryFile
from fpdf import FPDF
from PIL import Image

class Formulaire:

    def __init__(self,
                 nom,
                 prénom,
                 ddn,
                 formation,
                 emploi,
                 sexe_sujet,
                 emploi_envisagé,
                 numtel,
                 Email,
                 user1,
                 mypassword,
                 mailto,
                 sujet,
                 messageRes,
                 nom_bouton_soumettre,

                 date="Data",


                 ):
        self.nom = nom
        self.prénom = prénom
        self.ddn = ddn
        self.formation = formation
        self.emploi = emploi
        self.sexe_sujet = sexe_sujet
        self.emploi_envisagé = emploi_envisagé
        self.numtel = numtel
        self.Email = Email
        self.user1 = user1
        self.mypassword = mypassword
        self.mailto = mailto
        self.sujet = sujet
        self.messageRes = messageRes
        self.date = date
        self.nom_bouton_soumettre=nom_bouton_soumettre

    def cree_en_tête(self,image,titre,sous_titre):
        """crée l'entête du site"""
        st.image(image)
        st.title(titre)
        st.subheader(sous_titre)


    def cree_formulaire(self):
        """crée un formulaire """
        with st.form(key='my_form'):
            nom = st.text_input(self.nom)
            prénom = st.text_input(self.prénom)
            ddn = st.text_input(self.ddn)
            formation = st.text_input(self.formation)
            emploi = st.text_input(self.emploi)
            sexe_sujet = st.text_input(self.sexe_sujet)
            emploi_envisagé = st.text_input(self.emploi_envisagé)
            numtel = st.text_input(self.numtel)
            Email = st.text_input(self.Email)
            if "is_ok" not in st.session_state:
                st.session_state["is_ok"] = False

            #st.write(st.session_state["is_ok"])
            #st.write("avant", st.session_state)
            submit_button1 = st.form_submit_button(label=self.nom_bouton_soumettre)
            if submit_button1:
                st.session_state["is_ok"] = not st.session_state["is_ok"]
                #st.write("apres", st.session_state)
                dateCompletDuJour = str(dt.datetime.today().isoformat())[0:16]

                message_mail = self.date + " :" + dateCompletDuJour + "\n" + self.nom + " :" + nom + "\n" + self.prénom + " :" + prénom + "\n" + \
                               self.ddn + " :" + ddn + "\n" + \
                               self.formation + " :" + formation + "\n" + self.emploi + " :" + emploi + "\n" + \
                               self.sexe_sujet + " :" + sexe_sujet + "\n" + self.emploi_envisagé + " :" + emploi_envisagé + "\n" + \
                               self.numtel + " :" + numtel + "\n" + self.Email + " :" + Email

                yag = yagmail.SMTP(user=self.user1, password=self.mypassword)
                # sending the email
                yag.send(to=self.mailto, subject=self.sujet, contents=message_mail)

                st.success(self.messageRes)



            return st.session_state["is_ok"]

class Radiographie:
    """construction du test"""
    def __init__(self,
                 range_metier,
                 nom_test1,
                 nom_test2,
                 i_débuttemp,
                 intitule,               # "Test de personnalité : "
                 msgChoixNote,           #msg "choisissez une note"
                 msgVerif,               #Bouton "Vérification"
                 msgErreur,              #"ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
                 msg1,                   #"la note"
                 msg2,                   #"se répète"
                 msg3,                   #"les notes"
                 msg4,                   #"se répètent"
                 msg5,                   #"est diponible"
                 msg6,                   # "sont disponible"
                 msg7,                   # "vous pouvez passer au"


                 ):
        self.range_metier=range_metier
        self.nom_test1=nom_test1
        self.nom_test2=nom_test2
        self.i_débuttemp=i_débuttemp
        self.intitule=intitule
        self.msgChoixNote=msgChoixNote
        self.msgVerif=msgVerif
        self.msgErreur=msgErreur
        self.msg1 = msg1
        self.msg2 = msg2
        self.msg3 = msg3
        self.msg4 = msg4
        self.msg5 = msg5
        self.msg6 = msg6
        self.msg7 = msg7


    def insert_video(self,video1):
        """insert the video"""
        with st.container():
            video_file = open(video1, 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)




    def edit_test(self):
        """edit the different tests"""
        nomkey = self.intitule+ self.nom_test1

        st.subheader(nomkey)

        with st.form(key=nomkey):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                listeA = []
                listeA.append(self.range_metier[self.i_débuttemp])
                listeA.append(self.range_metier[self.i_débuttemp + 1])
                listeA.append(self.range_metier[self.i_débuttemp + 2])

                liste1 = []
                for elem in listeA:
                    st.write(elem)
                    liste1.append(
                        st.slider(label=self.msgChoixNote, min_value=1, max_value=12, key=elem))

            with col2:
                listeB = []
                listeB.append(self.range_metier[self.i_débuttemp + 3])
                listeB.append(self.range_metier[self.i_débuttemp + 4])
                listeB.append(self.range_metier[self.i_débuttemp + 5])

                liste2 = []
                for elem in listeB:
                    st.write(elem)
                    liste2.append(
                        st.slider(label=self.msgChoixNote, min_value=1, max_value=12, key=elem))

            with col3:
                listeC = []
                listeC.append(self.range_metier[self.i_débuttemp + 6])
                listeC.append(self.range_metier[self.i_débuttemp + 7])
                listeC.append(self.range_metier[self.i_débuttemp + 8])

                liste3 = []
                for elem in listeC:
                    st.write(elem)
                    liste3.append(
                        st.slider(label=self.msgChoixNote, min_value=1, max_value=12, key=elem))

            with col4:
                listeD = []
                listeD.append(self.range_metier[self.i_débuttemp + 9])
                listeD.append(self.range_metier[self.i_débuttemp + 10])
                listeD.append(self.range_metier[self.i_débuttemp + 11])

                liste4 = []
                for elem in listeD:
                    st.write(elem)
                    liste4.append(
                        st.slider(label=self.msgChoixNote, min_value=1, max_value=12, key=elem))

            joinedlist = liste1 + liste2 + liste3 + liste4
            joinedmétier = listeA + listeB + listeC + listeD
            verif = True
            if not (fw.checkIfDuplicates_1(joinedlist)):
                verif = False

            submitted = st.form_submit_button(self.msgVerif)

            if submitted:

                if fw.checkIfDuplicates_1(joinedlist):

                    m1 =self.msgErreur
                    listduplicat = fw.getduplicat(joinedlist)
                    if len(listduplicat) == 1:
                        mess = self.msg1 + str(listduplicat) + self.msg2
                        st.error(m1 + mess)
                    else:
                        mess = self.msg3 + str(listduplicat) +self.msg4
                        st.error(m1 + mess)
                    note_total = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                    notedispo = fw.getnotedispo(joinedlist, note_total)
                    if len(notedispo) == 1:
                        mess2 = self.msg1 + str(notedispo) + self.msg5
                        st.error(mess2)
                    else:
                        mess2 = self.msg3 + str(notedispo) + self.msg6
                        st.error(mess2)

                else:
                    verif = False
                    nom_test_temp = self.msg7 + self.nom_test2
                    st.success(nom_test_temp)

        return (joinedlist, joinedmétier, verif)

class Bilan:
    """Donne les résultats sous forme graphine"""
    def __init__(self,
                liste_domaine,
                liste_intéret_generaux

                ):

        self.liste_domaine=liste_domaine
        self.liste_intéret_generaux=liste_intéret_generaux





    def domainedesintérêt(self, range_note):
        mon_dict_domaine = {self.liste_domaine[0]: (range_note[0] + range_note[23] + range_note[34]
                                              + range_note[45] + range_note[56] + range_note[67]
                                              + range_note[78] + range_note[89] + range_note[100]),
                            self.liste_domaine[1]: (range_note[1] + range_note[12] + range_note[35]
                                              + range_note[46] + range_note[57] + range_note[68]
                                              + range_note[79] + range_note[90] + range_note[101]),
                            self.liste_domaine[2]: (range_note[2] + range_note[13] + range_note[24]
                                              + range_note[47] + range_note[58] + range_note[69]
                                              + range_note[80] + range_note[91] + range_note[102]),

                            self.liste_domaine[3]: (range_note[3] + range_note[14] + range_note[25]
                                              + range_note[36] + range_note[59] + range_note[70]
                                              + range_note[81] + range_note[92] + range_note[103]),

                            self.liste_domaine[4]: (range_note[4] + range_note[15] + range_note[26]
                                              + range_note[37] + range_note[48] + range_note[71]
                                              + range_note[82] + range_note[93] + range_note[104]),

                            self.liste_domaine[5]: (range_note[5] + range_note[16] + range_note[27]
                                              + range_note[38] + range_note[49] + range_note[60]
                                              + range_note[83] + range_note[94] + range_note[105]),

                            self.liste_domaine[6]: (range_note[6] + range_note[17] + range_note[28]
                                              + range_note[39] + range_note[50] + range_note[61]
                                              + range_note[72] + range_note[95] + range_note[106]),

                            self.liste_domaine[7]: (range_note[7] + range_note[18] + range_note[29]
                                              + range_note[40] + range_note[51] + range_note[62]
                                              + range_note[73] + range_note[84] + range_note[107]),

                            self.liste_domaine[8]: (range_note[8] + range_note[19] + range_note[30]
                                              + range_note[41] + range_note[52] + range_note[63]
                                              + range_note[74] + range_note[85] + range_note[96]),

                            self.liste_domaine[9]: (range_note[9] + range_note[20] + range_note[31]
                                              + range_note[42] + range_note[53] + range_note[64]
                                              + range_note[75] + range_note[86] + range_note[97]),

                            self.liste_domaine[10]: (range_note[10] + range_note[21] + range_note[32]
                                               + range_note[43] + range_note[54] + range_note[65]
                                               + range_note[76] + range_note[87] + range_note[98]),

                            self.liste_domaine[11]: (range_note[11] + range_note[22] + range_note[33]
                                               + range_note[44] + range_note[55] + range_note[66]
                                               + range_note[77] + range_note[88] + range_note[99])}

        return mon_dict_domaine


    def get_interet_etalonne(self, range_note, sexe):
        if sexe == "M" or sexe == "m":
            d = self.domainedesintérêt(range_note)
            mon_dict_final = {self.liste_domaine[0]: Plein_air_H[d[self.liste_domaine[0]]],
                              self.liste_domaine[1]: Technique_H[d[self.liste_domaine[1]]],
                              self.liste_domaine[2]: Calcul_H[d[self.liste_domaine[2]]],
                              self.liste_domaine[3]: Scientifique_H[d[self.liste_domaine[3]]],
                              self.liste_domaine[4]: Contacts_personnels_H[d[self.liste_domaine[4]]],
                              self.liste_domaine[5]: Esthétique_H[d[self.liste_domaine[5]]],
                              self.liste_domaine[6]: Littéraire_H[d[self.liste_domaine[6]]],
                              self.liste_domaine[7]: Musical_H[d[self.liste_domaine[7]]],
                              self.liste_domaine[8]: Service_social_H[d[self.liste_domaine[8]]],
                              self.liste_domaine[9]: Travail_de_bureau_H[d[self.liste_domaine[9]]],
                              self.liste_domaine[10]: Pratique_H[d[self.liste_domaine[10]]],
                              self.liste_domaine[11]: Médical_H[d[self.liste_domaine[11]]],

                              }


        else:
            d = self.domainedesintérêt(range_note)
            mon_dict_final = {self.liste_domaine[0]: Plein_air_F[d[self.liste_domaine[0]]],
                              self.liste_domaine[1]: Technique_F[d[self.liste_domaine[1]]],
                              self.liste_domaine[2]: Calcul_F[d[self.liste_domaine[2]]],
                              self.liste_domaine[3]: Scientifique_F[d[self.liste_domaine[3]]],
                              self.liste_domaine[4]: Contacts_personnels_F[d[self.liste_domaine[4]]],
                              self.liste_domaine[5]: Esthétique_F[d[self.liste_domaine[5]]],
                              self.liste_domaine[6]: Littéraire_F[d[self.liste_domaine[6]]],
                              self.liste_domaine[7]: Musical_F[d[self.liste_domaine[7]]],
                              self.liste_domaine[8]: Service_social_F[d[self.liste_domaine[8]]],
                              self.liste_domaine[9]: Travail_de_bureau_F[d[self.liste_domaine[9]]],
                              self.liste_domaine[10]: Pratique_F[d[self.liste_domaine[10]]],
                              self.liste_domaine[11]: Médical_F[d[self.liste_domaine[11]]],

                              }

        return mon_dict_final


#========================================Fonction pour graphique "intéret généraux===================================

    def intérêt_généraux(self, range_note):

        dict_domainedesintérêt = self.domainedesintérêt(range_note)

        dict_domaine2 = {
                         self.liste_intéret_generaux[0]: (2 * dict_domainedesintérêt[self.liste_domaine[3]]
                                                          + dict_domainedesintérêt[self.liste_domaine[11]]),
                         self.liste_intéret_generaux[1]: (dict_domainedesintérêt[self.liste_domaine[7]]
                                                          +dict_domainedesintérêt[self.liste_domaine[5]]
                                                          + dict_domainedesintérêt[self.liste_domaine[6]]),
                         self.liste_intéret_generaux[2]: dict_domainedesintérêt[self.liste_domaine[8]],
                         self.liste_intéret_generaux[3]: dict_domainedesintérêt[self.liste_domaine[4]],
                         self.liste_intéret_generaux[4]: (dict_domainedesintérêt[self.liste_domaine[2]]
                                                          +dict_domainedesintérêt[self.liste_domaine[9]]),
                         self.liste_intéret_generaux[5]: (dict_domainedesintérêt[self.liste_domaine[0]]
                                                         + dict_domainedesintérêt[self.liste_domaine[10]]
                                                         + dict_domainedesintérêt[self.liste_domaine[1]])
                         }

        return dict_domaine2

    def intérêt_généraux_etalonne(self, range_note, sexe):
        if sexe == "M" or sexe == "m":
            d = self.intérêt_généraux(range_note)

            mon_interet_final = {self.liste_intéret_generaux[0]: Investigateur_H[d[self.liste_intéret_generaux[0]]],
                                 self.liste_intéret_generaux[1]: Artiste_H[d[self.liste_intéret_generaux[1]]],
                                 self.liste_intéret_generaux[2]: Social_H[d[self.liste_intéret_generaux[2]]],
                                 self.liste_intéret_generaux[3]: Entreprenant_H[d[self.liste_intéret_generaux[3]]],
                                 self.liste_intéret_generaux[4]: Conventionnel_H[d[self.liste_intéret_generaux[4]]],
                                 self.liste_intéret_generaux[5]: Réaliste_H[d[self.liste_intéret_generaux[5]]]
                                 }
        else:
            d = self.intérêt_généraux(range_note)

            mon_interet_final = {self.liste_intéret_generaux[0]: Investigateur_F[d[self.liste_intéret_generaux[0]]],
                                 self.liste_intéret_generaux[1]: Artiste_F[d[self.liste_intéret_generaux[1]]],
                                 self.liste_intéret_generaux[2]: Social_F[d[self.liste_intéret_generaux[2]]],
                                 self.liste_intéret_generaux[3]: Entreprenant_F[d[self.liste_intéret_generaux[3]]],
                                 self.liste_intéret_generaux[4]: Conventionnel_F[d[self.liste_intéret_generaux[4]]],
                                 self.liste_intéret_generaux[5]: Réaliste_F[d[self.liste_intéret_generaux[5]]]
                                 }

        return mon_interet_final



#=================================================================================================================


#"""-------------------------------------------INSTANCIATION------------------------------------------------------"""
liste_métier ="Cultivator","Inginer","Contabil","Cercetator stiintific","Director comercial","Pictor","Jurnalist","Pianist de concert","Invatator","Director administrativ","Tesator","Medic","Inginer mecanic","Statistician","Chimist","Animator radio","Desenator publicitar","Romancier","Sef de orchestra","Psiholog scolar","Secretar","Tamplar","Chirurg","Profesor de sport","Agent de schimb","Meteorolog","Vanzator","Arhitect","Autor dramatic","Compozitor de muzica","Profesor","Operator procesare texte","Coafeza/frizer","Veterinar","Topograf","Tehnician","Biolog","Agent de publicitate","Ilustrator de imagini","Istoric","Critic muzical","Asistent social","Lucrator la banca","Legator","Farmacist","Explorator","Muncitor","Expert contabil","Anchetator","Bijutier","Bibliotecar","Profesor de muzica","Educator","Arhivist","Zidar","Dentist","Antrenor de sport","Inginer electrician","Inspector de impozite","Fizician","Fotograf","Redactor periodice","Violonist","Inspector resurse umane","Agent asigurari","Ceasornicar","Optician","Horticulor","Tehnician telecomunicatii","Profesor de matematica","Botanist","Reprezentat comercial","Critic","Consilier magazin de muzica","Animator centru de distractii","Lucrator la birou","Instalator","Radiolog","Gradinar","Mecanic auto","Programator","Astronaut","Organizator licitatii","Creator de decor teatru","Chitarist","Consilier de orientare profesionala","Consilier in post fix (posta, banca)","Bijutier","Kinetoterapeut","Ghid turistic","Tehnician hi-fi/video","Ofiter de conturi","Geolog","Agent de tele-marketing","Decorator vitrine","Scenarist","Lucrator umanitar","Secretar","Brutar","Infirmier","Agricultor","Lucrator in ture","Casier la banca","Tehnician de laborator","Vanzator demonstrator","Croitor","Poet","Vanzator de instrumente muzicale"
liste_domaine = ["Aer liber","Tehnică","Calcul","Ştiinţă","Contacte personale","Estetică","Literar","Muzică","Servicii sociale","Muncă de birou","Activităţi practice","Medicină"]
liste_intéret_generaux = ["Investigativ", "Artistic", "Social", "Antreprenor", "Conventional", "Realist"]

Plein_air_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
                   23: 9, 24: 9, 25: 9, 26: 9, 27: 9,
                   28: 9, 29: 9, 30: 9, 31: 8, 32: 8, 33: 8, 34: 8, 35: 8, 36: 8, 37: 8, 38: 8, 39: 7, 40: 7, 41: 7,
                   42: 7, 43: 7, 44: 7, 45: 7, 46: 6,
                   47: 6, 48: 6, 49: 6, 50: 6, 51: 6, 52: 6, 53: 5, 54: 5, 55: 5, 56: 5, 57: 5, 58: 5, 59: 5, 60: 5,
                   61: 4, 62: 4, 63: 4, 64: 4, 65: 4,
                   66: 4, 67: 4, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 2, 77: 2, 78: 2, 79: 2,
                   80: 1, 81: 1, 82: 1, 83: 1, 84: 1,
                   85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1, 93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1,
                   99: 1, 100: 1, 101: 1, 102: 1,
                   103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1}

Plein_air_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
               23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 8, 32: 8, 33: 8, 34: 8, 35: 8, 36: 8,
               37: 8, 38: 8, 39: 8, 40: 8, 41: 8, 42: 8, 43: 7, 44: 7, 45: 7, 46: 7, 47: 7, 48: 7, 49: 7, 50: 6,
               51: 6, 52: 6, 53: 6, 54: 6, 55: 5, 56: 5, 57: 5, 58: 5, 59: 5, 60: 5, 61: 5, 62: 4, 63: 4, 64: 4,
               65: 4, 66: 4, 67: 4, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 2, 76: 2, 77: 2, 78: 2,
               79: 2, 80: 2, 81: 1, 82: 1, 83: 1, 84: 1, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
               93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
               106: 1, 107: 1, 108: 1
               }

Technique_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
               23: 9, 24: 9, 25: 8, 26: 8, 27: 8,
               28: 8, 29: 8, 30: 8, 31: 8, 32: 8, 33: 8, 34: 8, 35: 8, 36: 7, 37: 7, 38: 7, 39: 7, 40: 7, 41: 7,
               42: 7, 43: 7, 44: 7, 45: 7, 46: 6,
               47: 6, 48: 6, 49: 6, 50: 6, 51: 6, 52: 6, 53: 6, 54: 6, 55: 6, 56: 6, 57: 6, 58: 5, 59: 5, 60: 5,
               61: 5, 62: 5, 63: 5, 64: 5, 65: 5,
               66: 5, 67: 5, 68: 4, 69: 4, 70: 4, 71: 4, 72: 4, 73: 4, 74: 4, 75: 4, 76: 4, 77: 3, 78: 3, 79: 3,
               80: 3, 81: 3, 82: 3, 83: 3, 84: 3,
               85: 3, 86: 2, 87: 2, 88: 2, 89: 2, 90: 2, 91: 2, 92: 2, 93: 2, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1,
               99: 1, 100: 1, 101: 1, 102: 1,
               103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1}

Technique_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
               23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9, 36: 9,
               37: 9, 38: 9, 39: 9, 40: 9, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 9, 47: 9, 48: 9, 49: 8, 50: 8,
               51: 8, 52: 8, 53: 8, 54: 8, 55: 8, 56: 8, 57: 8, 58: 8, 59: 8, 60: 7, 61: 7, 62: 7, 63: 7, 64: 7,
               65: 7, 66: 7, 67: 7, 68: 7, 69: 6, 70: 6, 71: 6, 72: 6, 73: 6, 74: 6, 75: 6, 76: 6, 77: 6, 78: 6,
               79: 5, 80: 5, 81: 5, 82: 5, 83: 5, 84: 5, 85: 4, 86: 4, 87: 4, 88: 4, 89: 3, 90: 3, 91: 3, 92: 3,
               93: 2, 94: 2, 95: 2, 96: 2, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
               106: 1, 107: 1, 108: 1
               }

Calcul_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
            23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 8, 31: 8, 32: 8, 33: 8, 34: 8, 35: 8, 36: 8,
            37: 8, 38: 8, 39: 7, 40: 7, 41: 7, 42: 7, 43: 7, 44: 7, 45: 7, 46: 7, 47: 7, 48: 7, 49: 6, 50: 6,
            51: 6, 52: 6, 53: 6, 54: 6, 55: 6, 56: 6, 57: 6, 58: 6, 59: 5, 60: 5, 61: 5, 62: 5, 63: 5, 64: 5,
            65: 5, 66: 5, 67: 5, 68: 5, 69: 5, 70: 5, 71: 4, 72: 4, 73: 4, 74: 4, 75: 4, 76: 4, 77: 4, 78: 4,
            79: 4, 80: 4, 81: 4, 82: 4, 83: 4, 84: 3, 85: 3, 86: 3, 87: 3, 88: 3, 89: 3, 90: 2, 91: 2, 92: 2,
            93: 2, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
            106: 1, 107: 1, 108: 1
            }
Calcul_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
            23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 8, 34: 8, 35: 8, 36: 8,
            37: 8, 38: 8, 39: 8, 40: 8, 41: 8, 42: 8, 43: 8, 44: 8, 45: 8, 46: 8, 47: 8, 48: 7, 49: 7, 50: 7,
            51: 7, 52: 7, 53: 7, 54: 7, 55: 7, 56: 7, 57: 7, 58: 7, 59: 7, 60: 7, 61: 6, 62: 6, 63: 6, 64: 6,
            65: 6, 66: 6, 67: 6, 68: 6, 69: 6, 70: 6, 71: 6, 72: 5, 73: 5, 74: 5, 75: 5, 76: 5, 77: 5, 78: 5,
            79: 5, 80: 5, 81: 4, 82: 4, 83: 4, 84: 4, 85: 4, 86: 4, 87: 4, 88: 4, 89: 4, 90: 3, 91: 3, 92: 3,
            93: 3, 94: 3, 95: 3, 96: 2, 97: 2, 98: 2, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
            106: 1, 107: 1, 108: 1
            }

Scientifique_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 8,
                  22: 8, 23: 8, 24: 8, 25: 8, 26: 8, 27: 7, 28: 7, 29: 7, 30: 7, 31: 7, 32: 6, 33: 6, 34: 6,
                  35: 6, 36: 6, 37: 6, 38: 6, 39: 5, 40: 5, 41: 5, 42: 5, 43: 5, 44: 5, 45: 5, 46: 5, 47: 4,
                  48: 4, 49: 4, 50: 4, 51: 4, 52: 4, 53: 4, 54: 4, 55: 4, 56: 3, 57: 3, 58: 3, 59: 3, 60: 3,
                  61: 3, 62: 3, 63: 3, 64: 3, 65: 2, 66: 2, 67: 2, 68: 2, 69: 1, 70: 1, 71: 1, 72: 1, 73: 1,
                  74: 1, 75: 1, 76: 1, 77: 1, 78: 1, 79: 1, 80: 1, 81: 1, 82: 1, 83: 1, 84: 1, 85: 1, 86: 1,
                  87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1, 93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1,
                  100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1
                  }
Scientifique_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9,
                  22: 9, 23: 9, 24: 8, 25: 8, 26: 8, 27: 8, 28: 8, 29: 8, 30: 8, 31: 8, 32: 7, 33: 7, 34: 7,
                  35: 7, 36: 7, 37: 7, 38: 6, 39: 6, 40: 6, 41: 6, 42: 6, 43: 6, 44: 6, 45: 5, 46: 5, 47: 5,
                  48: 5, 49: 5, 50: 5, 51: 5, 52: 4, 53: 4, 54: 4, 55: 4, 56: 4, 57: 4, 58: 4, 59: 4, 60: 4,
                  61: 3, 62: 3, 63: 3, 64: 3, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 2,
                  74: 2, 75: 2, 76: 2, 77: 2, 78: 2, 79: 2, 80: 1, 81: 1, 82: 1, 83: 1, 84: 1, 85: 1, 86: 1,
                  87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1, 93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1,
                  100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1
                  }

Contacts_personnels_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9,
                         21: 9, 22: 9, 23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 8, 30: 8, 31: 8, 32: 8,
                         33: 8, 34: 8, 35: 8, 36: 7, 37: 7, 38: 7, 39: 7, 40: 7, 41: 7, 42: 7, 43: 6, 44: 6,
                         45: 6, 46: 6, 47: 6, 48: 6, 49: 6, 50: 6, 51: 6, 52: 5, 53: 5, 54: 5, 55: 5, 56: 5,
                         57: 5, 58: 5, 59: 5, 60: 5, 61: 5, 62: 5, 63: 4, 64: 4, 65: 4, 66: 4, 67: 4, 68: 4,
                         69: 4, 70: 4, 71: 4, 72: 3, 73: 3, 74: 3, 75: 3, 76: 3, 77: 3, 78: 3, 79: 3, 80: 2,
                         81: 2, 82: 2, 83: 2, 84: 2, 85: 2, 86: 2, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
                         93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1,
                         105: 1, 106: 1, 107: 1, 108: 1
                         }
Contacts_personnels_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9,
                         21: 9, 22: 9, 23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9,
                         33: 9, 34: 8, 35: 8, 36: 8, 37: 8, 38: 8, 39: 7, 40: 7, 41: 7, 42: 7, 43: 7, 44: 7,
                         45: 7, 46: 6, 47: 6, 48: 6, 49: 6, 50: 6, 51: 6, 52: 6, 53: 6, 54: 6, 55: 6, 56: 6,
                         57: 5, 58: 5, 59: 5, 60: 5, 61: 5, 62: 5, 63: 5, 64: 5, 65: 5, 66: 4, 67: 4, 68: 4,
                         69: 4, 70: 4, 71: 4, 72: 4, 73: 4, 74: 3, 75: 3, 76: 3, 77: 3, 78: 3, 79: 3, 80: 2,
                         81: 2, 82: 2, 83: 2, 84: 1, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
                         93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1,
                         105: 1, 106: 1, 107: 1, 108: 1
                         }

Esthétique_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 8, 22: 8,
                23: 8, 24: 8, 25: 8, 26: 8, 27: 7, 28: 7, 29: 7, 30: 7, 31: 7, 32: 7, 33: 7, 34: 7, 35: 7, 36: 6,
                37: 6, 38: 6, 39: 6, 40: 6, 41: 6, 42: 6, 43: 6, 44: 6, 45: 5, 46: 5, 47: 5, 48: 5, 49: 5, 50: 5,
                51: 5, 52: 5, 53: 5, 54: 5, 55: 4, 56: 4, 57: 4, 58: 4, 59: 4, 60: 4, 61: 4, 62: 3, 63: 3, 64: 3,
                65: 3, 66: 3, 67: 3, 68: 2, 69: 2, 70: 2, 71: 2, 72: 2, 73: 1, 74: 1, 75: 1, 76: 1, 77: 1, 78: 1,
                79: 1, 80: 1, 81: 1, 82: 1, 83: 1, 84: 1, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
                93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
                106: 1, 107: 1, 108: 1
                }
Esthétique_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 8, 18: 8, 19: 8, 20: 8, 21: 8, 22: 8,
                23: 7, 24: 7, 25: 7, 26: 7, 27: 7, 28: 6, 29: 6, 30: 6, 31: 6, 32: 6, 33: 6, 34: 5, 35: 5, 36: 5,
                37: 5, 38: 5, 39: 5, 40: 4, 41: 4, 42: 4, 43: 4, 44: 4, 45: 4, 46: 4, 47: 4, 48: 4, 49: 4, 50: 3,
                51: 3, 52: 3, 53: 3, 54: 3, 55: 3, 56: 3, 57: 3, 58: 3, 59: 3, 60: 2, 61: 2, 62: 2, 63: 2, 64: 2,
                65: 2, 66: 2, 67: 2, 68: 2, 69: 1, 70: 1, 71: 1, 72: 1, 73: 1, 74: 1, 75: 1, 76: 1, 77: 1, 78: 1,
                79: 1, 80: 1, 81: 1, 82: 1, 83: 1, 84: 1, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
                93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
                106: 1, 107: 1, 108: 1
                }

Littéraire_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 8, 21: 8, 22: 8,
                23: 8, 24: 8, 25: 8, 26: 7, 27: 7, 28: 7, 29: 7, 30: 7, 31: 7, 32: 7, 33: 7, 34: 6, 35: 6, 36: 6,
                37: 6, 38: 6, 39: 6, 40: 6, 41: 6, 42: 5, 43: 5, 44: 5, 45: 5, 46: 5, 47: 5, 48: 5, 49: 5, 50: 5,
                51: 5, 52: 5, 53: 4, 54: 4, 55: 4, 56: 4, 57: 4, 58: 4, 59: 4, 60: 4, 61: 4, 62: 4, 63: 4, 64: 3,
                65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 2, 74: 2, 75: 2, 76: 2, 77: 2, 78: 2,
                79: 2, 80: 2, 81: 2, 82: 2, 83: 1, 84: 1, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
                93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
                106: 1, 107: 1, 108: 1
                }
Littéraire_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 8, 17: 8, 18: 7, 19: 7, 20: 7, 21: 7, 22: 7,
                23: 7, 24: 6, 25: 6, 26: 6, 27: 6, 28: 6, 29: 6, 30: 6, 31: 5, 32: 5, 33: 5, 34: 5, 35: 5, 36: 5,
                37: 5, 38: 5, 39: 5, 40: 5, 41: 4, 42: 4, 43: 4, 44: 4, 45: 4, 46: 4, 47: 4, 48: 4, 49: 4, 50: 4,
                51: 3, 52: 3, 53: 3, 54: 3, 55: 3, 56: 3, 57: 3, 58: 3, 59: 3, 60: 3, 61: 3, 62: 3, 63: 3, 64: 3,
                65: 3, 66: 3, 67: 3, 68: 2, 69: 2, 70: 2, 71: 2, 72: 2, 73: 2, 74: 2, 75: 2, 76: 2, 77: 2, 78: 1,
                79: 1, 80: 1, 81: 1, 82: 1, 83: 1, 84: 1, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
                93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
                106: 1, 107: 1, 108: 1
                }

Musical_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
             23: 9, 24: 8, 25: 8, 26: 8, 27: 8, 28: 8, 29: 8, 30: 8, 31: 7, 32: 7, 33: 7, 34: 7, 35: 7, 36: 7,
             37: 7, 38: 7, 39: 7, 40: 6, 41: 6, 42: 6, 43: 6, 44: 6, 45: 6, 46: 6, 47: 6, 48: 6, 49: 6, 50: 5,
             51: 5, 52: 5, 53: 5, 54: 5, 55: 5, 56: 5, 57: 5, 58: 5, 59: 5, 60: 5, 61: 5, 62: 5, 63: 5, 64: 5,
             65: 4, 66: 4, 67: 4, 68: 4, 69: 4, 70: 4, 71: 4, 72: 4, 73: 4, 74: 4, 75: 4, 76: 3, 77: 3, 78: 3,
             79: 3, 80: 3, 81: 3, 82: 3, 83: 3, 84: 3, 85: 3, 86: 3, 87: 3, 88: 2, 89: 2, 90: 2, 91: 2, 92: 2,
             93: 2, 94: 2, 95: 2, 96: 2, 97: 2, 98: 2, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
             106: 1, 107: 1, 108: 1
             }
Musical_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
             23: 8, 24: 8, 25: 8, 26: 8, 27: 8, 28: 8, 29: 7, 30: 7, 31: 7, 32: 7, 33: 7, 34: 7, 35: 7, 36: 7,
             37: 6, 38: 6, 39: 6, 40: 6, 41: 6, 42: 6, 43: 6, 44: 6, 45: 6, 46: 5, 47: 5, 48: 5, 49: 5, 50: 5,
             51: 5, 52: 5, 53: 5, 54: 5, 55: 5, 56: 4, 57: 4, 58: 4, 59: 4, 60: 4, 61: 4, 62: 4, 63: 4, 64: 4,
             65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 3, 77: 2, 78: 2,
             79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
             93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
             106: 1, 107: 1, 108: 1
             }

Service_social_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9,
                    22: 9, 23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9,
                    35: 8, 36: 8, 37: 8, 38: 8, 39: 8, 40: 8, 41: 7, 42: 7, 43: 7, 44: 7, 45: 7, 46: 7, 47: 6,
                    48: 6, 49: 6, 50: 6, 51: 6, 52: 6, 53: 6, 54: 6, 55: 5, 56: 5, 57: 5, 58: 5, 59: 5, 60: 5,
                    61: 5, 62: 4, 63: 4, 64: 4, 65: 4, 66: 4, 67: 4, 68: 4, 69: 4, 70: 4, 71: 3, 72: 3, 73: 3,
                    74: 3, 75: 3, 76: 3, 77: 3, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 1, 86: 1,
                    87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1, 93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1,
                    100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1
                    }
Service_social_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9,
                    22: 8, 23: 8, 24: 8, 25: 8, 26: 8, 27: 8, 28: 8, 29: 8, 30: 8, 31: 7, 32: 7, 33: 7, 34: 7,
                    35: 7, 36: 7, 37: 7, 38: 7, 39: 6, 40: 6, 41: 6, 42: 6, 43: 6, 44: 6, 45: 6, 46: 6, 47: 6,
                    48: 5, 49: 5, 50: 5, 51: 5, 52: 5, 53: 5, 54: 5, 55: 5, 56: 5, 57: 5, 58: 4, 59: 4, 60: 4,
                    61: 4, 62: 4, 63: 4, 64: 4, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 2, 72: 2, 73: 2,
                    74: 2, 75: 2, 76: 2, 77: 2, 78: 1, 79: 1, 80: 1, 81: 1, 82: 1, 83: 1, 84: 1, 85: 1, 86: 1,
                    87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1, 93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1,
                    100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1
                    }

Travail_de_bureau_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9,
                       22: 9, 23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9,
                       35: 9, 36: 9, 37: 9, 38: 9, 39: 9, 40: 9, 41: 9, 42: 9, 43: 9, 44: 9, 45: 8, 46: 8, 47: 8,
                       48: 8, 49: 8, 50: 8, 51: 8, 52: 8, 53: 8, 54: 7, 55: 7, 56: 7, 57: 7, 58: 7, 59: 7, 60: 7,
                       61: 7, 62: 7, 63: 7, 64: 7, 65: 7, 66: 7, 67: 7, 68: 7, 69: 6, 70: 6, 71: 6, 72: 6, 73: 6,
                       74: 6, 75: 6, 76: 6, 77: 5, 78: 5, 79: 5, 80: 5, 81: 5, 82: 5, 83: 5, 84: 5, 85: 5, 86: 5,
                       87: 4, 88: 4, 89: 4, 90: 4, 91: 4, 92: 4, 93: 4, 94: 3, 95: 3, 96: 3, 97: 3, 98: 2, 99: 2,
                       100: 2, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1
                       }
Travail_de_bureau_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9,
                       22: 9, 23: 8, 24: 8, 25: 8, 26: 8, 27: 8, 28: 8, 29: 7, 30: 7, 31: 7, 32: 7, 33: 7, 34: 7,
                       35: 7, 36: 7, 37: 6, 38: 6, 39: 6, 40: 6, 41: 6, 42: 6, 43: 6, 44: 6, 45: 6, 46: 5, 47: 5,
                       48: 5, 49: 5, 50: 5, 51: 5, 52: 5, 53: 5, 54: 5, 55: 5, 56: 4, 57: 4, 58: 4, 59: 4, 60: 4,
                       61: 4, 62: 4, 63: 4, 64: 4, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3,
                       74: 3, 75: 3, 76: 3, 77: 2, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 1, 86: 1,
                       87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1, 93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1,
                       100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1
                       }

Pratique_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
              23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9, 36: 9,
              37: 9, 38: 9, 39: 9, 40: 9, 41: 9, 42: 8, 43: 8, 44: 8, 45: 8, 46: 8, 47: 8, 48: 8, 49: 8, 50: 8,
              51: 8, 52: 7, 53: 7, 54: 7, 55: 7, 56: 7, 57: 7, 58: 7, 59: 7, 60: 7, 61: 7, 62: 7, 63: 6, 64: 6,
              65: 6, 66: 6, 67: 6, 68: 6, 69: 6, 70: 5, 71: 5, 72: 5, 73: 5, 74: 5, 75: 5, 76: 5, 77: 4, 78: 4,
              79: 4, 80: 4, 81: 4, 82: 4, 83: 4, 84: 4, 85: 4, 86: 3, 87: 3, 88: 3, 89: 3, 90: 2, 91: 2, 92: 2,
              93: 2, 94: 2, 95: 2, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
              106: 1, 107: 1, 108: 1
              }
Pratique_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
              23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9, 36: 9,
              37: 9, 38: 9, 39: 9, 40: 9, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 9, 47: 9, 48: 9, 49: 9, 50: 8,
              51: 8, 52: 8, 53: 8, 54: 8, 55: 8, 56: 7, 57: 7, 58: 7, 59: 7, 60: 7, 61: 7, 62: 7, 63: 7, 64: 6,
              65: 6, 66: 6, 67: 6, 68: 6, 69: 6, 70: 6, 71: 6, 72: 6, 73: 5, 74: 5, 75: 5, 76: 5, 77: 5, 78: 5,
              79: 5, 80: 4, 81: 4, 82: 4, 83: 4, 84: 4, 85: 4, 86: 3, 87: 3, 88: 3, 89: 3, 90: 3, 91: 3, 92: 2,
              93: 2, 94: 2, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
              106: 1, 107: 1, 108: 1
              }

Médical_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
             23: 9, 24: 9, 25: 9, 26: 9, 27: 8, 28: 8, 29: 8, 30: 8, 31: 7, 32: 7, 33: 7, 34: 7, 35: 7, 36: 7,
             37: 7, 38: 7, 39: 7, 40: 7, 41: 6, 42: 6, 43: 6, 44: 6, 45: 6, 46: 6, 47: 6, 48: 5, 49: 5, 50: 5,
             51: 5, 52: 5, 53: 5, 54: 5, 55: 5, 56: 5, 57: 5, 58: 4, 59: 4, 60: 4, 61: 4, 62: 4, 63: 4, 64: 4,
             65: 4, 66: 4, 67: 4, 68: 4, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 2, 77: 2, 78: 2,
             79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 1, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
             93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
             106: 1, 107: 1, 108: 1
             }
Médical_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
             23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 8, 29: 8, 30: 8, 31: 8, 32: 8, 33: 8, 34: 8, 35: 7, 36: 7,
             37: 7, 38: 7, 39: 7, 40: 7, 41: 7, 42: 7, 43: 6, 44: 6, 45: 6, 46: 6, 47: 6, 48: 6, 49: 6, 50: 6,
             51: 6, 52: 5, 53: 5, 54: 5, 55: 5, 56: 5, 57: 5, 58: 5, 59: 5, 60: 4, 61: 4, 62: 4, 63: 4, 64: 4,
             65: 4, 66: 4, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 2, 75: 2, 76: 2, 77: 2, 78: 2,
             79: 2, 80: 2, 81: 2, 82: 2, 83: 1, 84: 1, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
             93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
             106: 1, 107: 1, 108: 1
             }
# =============================++++++++++++++++DATA INTERET GENERAUX+++++++++++++++++++++++++++++++++++++++++++++

Investigateur_H = {9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0,
                   23: 0, 24: 0, 25: 0, 26: 0, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9, 36: 9,
                   37: 9, 38: 9, 39: 9, 40: 9, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 9, 47: 9, 48: 9, 49: 9, 50: 9,
                   51: 9, 52: 9, 53: 9, 54: 9, 55: 9, 56: 9, 57: 9, 58: 9, 59: 9, 60: 9, 61: 9, 62: 9, 63: 9, 64: 9,
                   65: 9, 66: 9, 67: 9, 68: 9, 69: 9, 70: 9, 71: 9, 72: 9, 73: 9, 74: 9, 75: 9, 76: 9, 77: 9, 78: 9,
                   79: 9, 80: 9, 81: 8, 82: 8, 83: 8, 84: 8, 85: 8, 86: 8, 87: 8, 88: 8, 89: 8, 90: 8, 91: 8, 92: 8,
                   93: 8, 94: 8, 95: 7, 96: 7, 97: 7, 98: 7, 99: 7, 100: 7, 101: 7, 102: 7, 103: 7, 104: 7, 105: 7,
                   106: 7, 107: 7, 108: 7, 109: 6, 110: 6, 111: 6, 112: 6, 113: 6, 114: 6, 115: 6, 116: 6, 117: 6,
                   118: 6, 119: 6, 120: 6, 121: 6, 122: 6, 123: 6, 124: 6, 125: 6, 126: 6, 127: 5, 128: 5, 129: 5,
                   130: 5, 131: 5, 132: 5, 133: 5, 134: 5, 135: 5, 136: 5, 137: 5, 138: 5, 139: 5, 140: 5, 141: 5,
                   142: 5, 143: 5, 144: 5, 145: 5, 146: 5, 147: 5, 148: 5, 149: 5, 150: 5, 151: 4, 152: 4, 153: 4,
                   154: 4, 155: 4, 156: 4, 157: 4, 158: 4, 159: 4, 160: 4, 161: 4, 162: 4, 163: 4, 164: 4, 165: 4,
                   166: 4, 167: 4, 168: 4, 169: 4, 170: 4, 171: 3, 172: 3, 173: 3, 174: 3, 175: 3, 176: 3, 177: 3,
                   178: 3, 179: 3, 180: 3, 181: 3, 182: 3, 183: 3, 184: 3, 185: 3, 186: 3, 187: 3, 188: 3, 189: 3,
                   190: 3, 191: 3, 192: 2, 193: 2, 194: 2, 195: 2, 196: 2, 197: 2, 198: 2, 199: 2, 200: 2, 201: 2,
                   202: 2, 203: 2, 204: 2, 205: 2, 206: 2, 207: 2, 208: 2, 209: 2, 210: 2, 211: 2, 212: 2, 213: 1,
                   214: 1, 215: 1, 216: 1, 217: 1, 218: 1, 219: 1, 220: 1, 221: 1, 222: 1, 223: 1, 224: 1, 225: 1,
                   226: 1, 227: 1, 228: 1, 229: 1, 230: 1, 231: 1, 232: 1, 233: 1, 234: 1, 235: 1, 236: 1, 237: 1,
                   238: 1, 239: 1, 240: 1, 241: 1, 242: 1, 243: 1, 244: 1, 245: 1, 246: 1, 247: 1, 248: 1, 249: 1,
                   250: 1, 251: 1, 252: 1, 253: 1, 254: 1, 255: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1,
                   262: 1, 263: 1, 264: 1, 265: 1, 266: 1, 267: 1, 268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1,
                   274: 1, 275: 1, 276: 1, 277: 1, 278: 1, 279: 1, 280: 1, 281: 1, 282: 1, 283: 1, 284: 1, 285: 1,
                   286: 1, 287: 1, 288: 1, 289: 1, 290: 1, 291: 1, 292: 1, 293: 1, 294: 1, 295: 1, 296: 1, 297: 1,
                   298: 1, 299: 1, 300: 1, 301: 1, 302: 1, 303: 1, 304: 1, 305: 1, 306: 1, 307: 1, 308: 1, 309: 1,
                   310: 1, 311: 1, 312: 1, 313: 1, 314: 1, 315: 1, 316: 1, 317: 1, 318: 1, 319: 1, 320: 1, 321: 1,
                   322: 1, 323: 1, 324: 1
                   }
Investigateur_F = {9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0,
                   23: 0, 24: 0, 25: 0, 26: 0, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9, 36: 9,
                   37: 9, 38: 9, 39: 9, 40: 9, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 9, 47: 9, 48: 9, 49: 9, 50: 9,
                   51: 9, 52: 9, 53: 9, 54: 9, 55: 9, 56: 9, 57: 9, 58: 9, 59: 9, 60: 9, 61: 9, 62: 9, 63: 9, 64: 9,
                   65: 9, 66: 9, 67: 9, 68: 9, 69: 9, 70: 9, 71: 9, 72: 9, 73: 9, 74: 9, 75: 9, 76: 9, 77: 9, 78: 9,
                   79: 9, 80: 9, 81: 9, 82: 9, 83: 9, 84: 9, 85: 9, 86: 9, 87: 9, 88: 9, 89: 9, 90: 9, 91: 9, 92: 9,
                   93: 9, 94: 8, 95: 8, 96: 8, 97: 8, 98: 8, 99: 8, 100: 8, 101: 8, 102: 8, 103: 8, 104: 7, 105: 7,
                   106: 7, 107: 7, 108: 7, 109: 7, 110: 7, 111: 7, 112: 7, 113: 7, 114: 7, 115: 7, 116: 7, 117: 7,
                   118: 7, 119: 7, 120: 7, 121: 7, 122: 7, 123: 7, 124: 7, 125: 7, 126: 7, 127: 6, 128: 6, 129: 6,
                   130: 6, 131: 6, 132: 6, 133: 6, 134: 6, 135: 6, 136: 6, 137: 6, 138: 6, 139: 6, 140: 6, 141: 6,
                   142: 6, 143: 6, 144: 5, 145: 5, 146: 5, 147: 5, 148: 5, 149: 5, 150: 5, 151: 5, 152: 5, 153: 5,
                   154: 5, 155: 5, 156: 5, 157: 5, 158: 5, 159: 5, 160: 5, 161: 4, 162: 4, 163: 4, 164: 4, 165: 4,
                   166: 4, 167: 4, 168: 4, 169: 4, 170: 4, 171: 4, 172: 4, 173: 4, 174: 4, 175: 4, 176: 4, 177: 4,
                   178: 4, 179: 4, 180: 4, 181: 4, 182: 3, 183: 3, 184: 3, 185: 3, 186: 3, 187: 3, 188: 3, 189: 3,
                   190: 3, 191: 3, 192: 3, 193: 3, 194: 3, 195: 3, 196: 3, 197: 3, 198: 3, 199: 3, 200: 3, 201: 3,
                   202: 3, 203: 3, 204: 3, 205: 3, 206: 2, 207: 2, 208: 2, 209: 2, 210: 2, 211: 2, 212: 2, 213: 2,
                   214: 2, 215: 2, 216: 2, 217: 2, 218: 2, 219: 2, 220: 2, 221: 2, 222: 2, 223: 2, 224: 1, 225: 1,
                   226: 1, 227: 1, 228: 1, 229: 1, 230: 1, 231: 1, 232: 1, 233: 1, 234: 1, 235: 1, 236: 1, 237: 1,
                   238: 1, 239: 1, 240: 1, 241: 1, 242: 1, 243: 1, 244: 1, 245: 1, 246: 1, 247: 1, 248: 1, 249: 1,
                   250: 1, 251: 1, 252: 1, 253: 1, 254: 1, 255: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1,
                   262: 1, 263: 1, 264: 1, 265: 1, 266: 1, 267: 1, 268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1,
                   274: 1, 275: 1, 276: 1, 277: 1, 278: 1, 279: 1, 280: 1, 281: 1, 282: 1, 283: 1, 284: 1, 285: 1,
                   286: 1, 287: 1, 288: 1, 289: 1, 290: 1, 291: 1, 292: 1, 293: 1, 294: 1, 295: 1, 296: 1, 297: 1,
                   298: 1, 299: 1, 300: 1, 301: 1, 302: 1, 303: 1, 304: 1, 305: 1, 306: 1, 307: 1, 308: 1, 309: 1,
                   310: 1, 311: 1, 312: 1, 313: 1, 314: 1, 315: 1, 316: 1, 317: 1, 318: 1, 319: 1, 320: 1, 321: 1,
                   322: 1, 323: 1, 324: 1
                   }

Artiste_H = {9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0,
             24: 0, 25: 0, 26: 0, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9, 36: 9, 37: 9,
             38: 9, 39: 9, 40: 9, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 9, 47: 9, 48: 9, 49: 9, 50: 9, 51: 9,
             52: 9, 53: 9, 54: 9, 55: 9, 56: 9, 57: 9, 58: 9, 59: 9, 60: 9, 61: 9, 62: 9, 63: 9, 64: 9, 65: 9,
             66: 9, 67: 9, 68: 9, 69: 9, 70: 9, 71: 9, 72: 9, 73: 9, 74: 9, 75: 9, 76: 9, 77: 9, 78: 9, 79: 9,
             80: 9, 81: 8, 82: 8, 83: 8, 84: 8, 85: 8, 86: 8, 87: 8, 88: 8, 89: 8, 90: 8, 91: 8, 92: 8, 93: 8,
             94: 8, 95: 8, 96: 8, 97: 8, 98: 7, 99: 7, 100: 7, 101: 7, 102: 7, 103: 7, 104: 7, 105: 7, 106: 7,
             107: 7, 108: 7, 109: 7, 110: 7, 111: 7, 112: 7, 113: 7, 114: 6, 115: 6, 116: 6, 117: 6, 118: 6, 119: 6,
             120: 6, 121: 6, 122: 6, 123: 6, 124: 6, 125: 6, 126: 6, 127: 6, 128: 6, 129: 6, 130: 6, 131: 6, 132: 6,
             133: 6, 134: 6, 135: 6, 136: 6, 137: 5, 138: 5, 139: 5, 140: 5, 141: 5, 142: 5, 143: 5, 144: 5, 145: 5,
             146: 5, 147: 5, 148: 5, 149: 5, 150: 5, 151: 5, 152: 5, 153: 5, 154: 5, 155: 5, 156: 5, 157: 5, 158: 5,
             159: 5, 160: 5, 161: 5, 162: 5, 163: 5, 164: 5, 165: 5, 166: 5, 167: 5, 168: 5, 169: 4, 170: 4, 171: 4,
             172: 4, 173: 4, 174: 4, 175: 4, 176: 4, 177: 4, 178: 4, 179: 4, 180: 4, 181: 4, 182: 4, 183: 4, 184: 4,
             185: 4, 186: 4, 187: 4, 188: 4, 189: 4, 190: 4, 191: 4, 192: 4, 193: 4, 194: 4, 195: 4, 196: 4, 197: 4,
             198: 4, 199: 4, 200: 4, 201: 3, 202: 3, 203: 3, 204: 3, 205: 3, 206: 3, 207: 3, 208: 3, 209: 3, 210: 3,
             211: 3, 212: 3, 213: 3, 214: 3, 215: 3, 216: 3, 217: 3, 218: 3, 219: 3, 220: 3, 221: 3, 222: 2, 223: 2,
             224: 2, 225: 2, 226: 2, 227: 2, 228: 2, 229: 2, 230: 2, 231: 2, 232: 2, 233: 2, 234: 2, 235: 2, 236: 2,
             237: 2, 238: 2, 239: 2, 240: 2, 241: 2, 242: 2, 243: 2, 244: 2, 245: 2, 246: 2, 247: 2, 248: 1, 249: 1,
             250: 1, 251: 1, 252: 1, 253: 1, 254: 1, 255: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1, 262: 1,
             263: 1, 264: 1, 265: 1, 266: 1, 267: 1, 268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1, 274: 1, 275: 1,
             276: 1, 277: 1, 278: 1, 279: 1, 280: 1, 281: 1, 282: 1, 283: 1, 284: 1, 285: 1, 286: 1, 287: 1, 288: 1,
             289: 1, 290: 1, 291: 1, 292: 1, 293: 1, 294: 1, 295: 1, 296: 1, 297: 1, 298: 1, 299: 1, 300: 1, 301: 1,
             302: 1, 303: 1, 304: 1, 305: 1, 306: 1, 307: 1, 308: 1, 309: 1, 310: 1, 311: 1, 312: 1, 313: 1, 314: 1,
             315: 1, 316: 1, 317: 1, 318: 1, 319: 1, 320: 1, 321: 1, 322: 1, 323: 1, 324: 1
             }
Artiste_F = {9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0,
             24: 0, 25: 0, 26: 0, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9, 36: 9, 37: 9,
             38: 9, 39: 9, 40: 9, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 9, 47: 9, 48: 9, 49: 9, 50: 9, 51: 9,
             52: 9, 53: 9, 54: 9, 55: 9, 56: 9, 57: 9, 58: 9, 59: 9, 60: 9, 61: 9, 62: 9, 63: 9, 64: 9, 65: 9,
             66: 9, 67: 9, 68: 9, 69: 9, 70: 9, 71: 9, 72: 9, 73: 8, 74: 8, 75: 8, 76: 8, 77: 8, 78: 8, 79: 8,
             80: 7, 81: 7, 82: 7, 83: 7, 84: 7, 85: 7, 86: 7, 87: 7, 88: 7, 89: 7, 90: 7, 91: 7, 92: 7, 93: 7,
             94: 6, 95: 6, 96: 6, 97: 6, 98: 6, 99: 6, 100: 6, 101: 6, 102: 6, 103: 6, 104: 6, 105: 6, 106: 6,
             107: 6, 108: 6, 109: 6, 110: 6, 111: 6, 112: 5, 113: 5, 114: 5, 115: 5, 116: 5, 117: 5, 118: 5, 119: 5,
             120: 5, 121: 5, 122: 5, 123: 5, 124: 5, 125: 5, 126: 5, 127: 5, 128: 5, 129: 5, 130: 5, 131: 5, 132: 5,
             133: 5, 134: 5, 135: 5, 136: 4, 137: 4, 138: 4, 139: 4, 140: 4, 141: 4, 142: 4, 143: 4, 144: 4, 145: 4,
             146: 4, 147: 4, 148: 4, 149: 4, 150: 4, 151: 4, 152: 4, 153: 4, 154: 4, 155: 4, 156: 4, 157: 4, 158: 4,
             159: 4, 160: 4, 161: 3, 162: 3, 163: 3, 164: 3, 165: 3, 166: 3, 167: 3, 168: 3, 169: 3, 170: 3, 171: 3,
             172: 3, 173: 3, 174: 3, 175: 3, 176: 3, 177: 3, 178: 3, 179: 3, 180: 3, 181: 3, 182: 3, 183: 3, 184: 3,
             185: 3, 186: 2, 187: 2, 188: 2, 189: 2, 190: 2, 191: 2, 192: 2, 193: 2, 194: 2, 195: 2, 196: 2, 197: 2,
             198: 2, 199: 2, 200: 2, 201: 2, 202: 2, 203: 2, 204: 2, 205: 2, 206: 2, 207: 2, 208: 2, 209: 2, 210: 2,
             211: 1, 212: 1, 213: 1, 214: 1, 215: 1, 216: 1, 217: 1, 218: 1, 219: 1, 220: 1, 221: 1, 222: 1, 223: 1,
             224: 1, 225: 1, 226: 1, 227: 1, 228: 1, 229: 1, 230: 1, 231: 1, 232: 1, 233: 1, 234: 1, 235: 1, 236: 1,
             237: 1, 238: 1, 239: 1, 240: 1, 241: 1, 242: 1, 243: 1, 244: 1, 245: 1, 246: 1, 247: 1, 248: 1, 249: 1,
             250: 1, 251: 1, 252: 1, 253: 1, 254: 1, 255: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1, 262: 1,
             263: 1, 264: 1, 265: 1, 266: 1, 267: 1, 268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1, 274: 1, 275: 1,
             276: 1, 277: 1, 278: 1, 279: 1, 280: 1, 281: 1, 282: 1, 283: 1, 284: 1, 285: 1, 286: 1, 287: 1, 288: 1,
             289: 1, 290: 1, 291: 1, 292: 1, 293: 1, 294: 1, 295: 1, 296: 1, 297: 1, 298: 1, 299: 1, 300: 1, 301: 1,
             302: 1, 303: 1, 304: 1, 305: 1, 306: 1, 307: 1, 308: 1, 309: 1, 310: 1, 311: 1, 312: 1, 313: 1, 314: 1,
             315: 1, 316: 1, 317: 1, 318: 1, 319: 1, 320: 1, 321: 1, 322: 1, 323: 1, 324: 1
             }

Social_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9, 23: 9,
            24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 8, 36: 8, 37: 8, 38: 8,
            39: 8, 40: 8, 41: 7, 42: 7, 43: 7, 44: 7, 45: 7, 46: 7, 47: 6, 48: 6, 49: 6, 50: 6, 51: 6, 52: 6, 53: 6,
            54: 6, 55: 5, 56: 5, 57: 5, 58: 5, 59: 5, 60: 5, 61: 5, 62: 4, 63: 4, 64: 4, 65: 4, 66: 4, 67: 4, 68: 4,
            69: 4, 70: 4, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 3, 77: 3, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2,
            84: 2, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1, 93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1,
            99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1, 109: 1, 110: 1, 111: 1,
            112: 1, 113: 1, 114: 1, 115: 1, 116: 1, 117: 1, 118: 1, 119: 1, 120: 1, 121: 1, 122: 1, 123: 1, 124: 1,
            125: 1, 126: 1, 127: 1, 128: 1, 129: 1, 130: 1, 131: 1, 132: 1, 133: 1, 134: 1, 135: 1, 136: 1, 137: 1,
            138: 1, 139: 1, 140: 1, 141: 1, 142: 1, 143: 1, 144: 1, 145: 1, 146: 1, 147: 1, 148: 1, 149: 1, 150: 1,
            151: 1, 152: 1, 153: 1, 154: 1, 155: 1, 156: 1, 157: 1, 158: 1, 159: 1, 160: 1, 161: 1, 162: 1, 163: 1,
            164: 1, 165: 1, 166: 1, 167: 1, 168: 1, 169: 1, 170: 1, 171: 1, 172: 1, 173: 1, 174: 1, 175: 1, 176: 1,
            177: 1, 178: 1, 179: 1, 180: 1, 181: 1, 182: 1, 183: 1, 184: 1, 185: 1, 186: 1, 187: 1, 188: 1, 189: 1,
            190: 1, 191: 1, 192: 1, 193: 1, 194: 1, 195: 1, 196: 1, 197: 1, 198: 1, 199: 1, 200: 1, 201: 1, 202: 1,
            203: 1, 204: 1, 205: 1, 206: 1, 207: 1, 208: 1, 209: 1, 210: 1, 211: 1, 212: 1, 213: 1, 214: 1, 215: 1,
            216: 1, 217: 1, 218: 1, 219: 1, 220: 1, 221: 1, 222: 1, 223: 1, 224: 1, 225: 1, 226: 1, 227: 1, 228: 1,
            229: 1, 230: 1, 231: 1, 232: 1, 233: 1, 234: 1, 235: 1, 236: 1, 237: 1, 238: 1, 239: 1, 240: 1, 241: 1,
            242: 1, 243: 1, 244: 1, 245: 1, 246: 1, 247: 1, 248: 1, 249: 1, 250: 1, 251: 1, 252: 1, 253: 1, 254: 1,
            255: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1, 262: 1, 263: 1, 264: 1, 265: 1, 266: 1, 267: 1,
            268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1, 274: 1, 275: 1, 276: 1, 277: 1, 278: 1, 279: 1, 280: 1,
            281: 1, 282: 1, 283: 1, 284: 1, 285: 1, 286: 1, 287: 1, 288: 1, 289: 1, 290: 1, 291: 1, 292: 1, 293: 1,
            294: 1, 295: 1, 296: 1, 297: 1, 298: 1, 299: 1, 300: 1, 301: 1, 302: 1, 303: 1, 304: 1, 305: 1, 306: 1,
            307: 1, 308: 1, 309: 1, 310: 1, 311: 1, 312: 1, 313: 1, 314: 1, 315: 1, 316: 1, 317: 1, 318: 1, 319: 1,
            320: 1, 321: 1, 322: 1, 323: 1, 324: 1
            }
Social_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 8, 23: 8,
            24: 8, 25: 8, 26: 8, 27: 8, 28: 8, 29: 8, 30: 8, 31: 7, 32: 7, 33: 7, 34: 7, 35: 7, 36: 7, 37: 7, 38: 7,
            39: 6, 40: 6, 41: 6, 42: 6, 43: 6, 44: 6, 45: 6, 46: 6, 47: 6, 48: 5, 49: 5, 50: 5, 51: 5, 52: 5, 53: 5,
            54: 5, 55: 5, 56: 5, 57: 5, 58: 4, 59: 4, 60: 4, 61: 4, 62: 4, 63: 4, 64: 4, 65: 3, 66: 3, 67: 3, 68: 3,
            69: 3, 70: 3, 71: 2, 72: 2, 73: 2, 74: 2, 75: 2, 76: 2, 77: 2, 78: 1, 79: 1, 80: 1, 81: 1, 82: 1, 83: 1,
            84: 1, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1, 93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1,
            99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1, 109: 1, 110: 1, 111: 1,
            112: 1, 113: 1, 114: 1, 115: 1, 116: 1, 117: 1, 118: 1, 119: 1, 120: 1, 121: 1, 122: 1, 123: 1, 124: 1,
            125: 1, 126: 1, 127: 1, 128: 1, 129: 1, 130: 1, 131: 1, 132: 1, 133: 1, 134: 1, 135: 1, 136: 1, 137: 1,
            138: 1, 139: 1, 140: 1, 141: 1, 142: 1, 143: 1, 144: 1, 145: 1, 146: 1, 147: 1, 148: 1, 149: 1, 150: 1,
            151: 1, 152: 1, 153: 1, 154: 1, 155: 1, 156: 1, 157: 1, 158: 1, 159: 1, 160: 1, 161: 1, 162: 1, 163: 1,
            164: 1, 165: 1, 166: 1, 167: 1, 168: 1, 169: 1, 170: 1, 171: 1, 172: 1, 173: 1, 174: 1, 175: 1, 176: 1,
            177: 1, 178: 1, 179: 1, 180: 1, 181: 1, 182: 1, 183: 1, 184: 1, 185: 1, 186: 1, 187: 1, 188: 1, 189: 1,
            190: 1, 191: 1, 192: 1, 193: 1, 194: 1, 195: 1, 196: 1, 197: 1, 198: 1, 199: 1, 200: 1, 201: 1, 202: 1,
            203: 1, 204: 1, 205: 1, 206: 1, 207: 1, 208: 1, 209: 1, 210: 1, 211: 1, 212: 1, 213: 1, 214: 1, 215: 1,
            216: 1, 217: 1, 218: 1, 219: 1, 220: 1, 221: 1, 222: 1, 223: 1, 224: 1, 225: 1, 226: 1, 227: 1, 228: 1,
            229: 1, 230: 1, 231: 1, 232: 1, 233: 1, 234: 1, 235: 1, 236: 1, 237: 1, 238: 1, 239: 1, 240: 1, 241: 1,
            242: 1, 243: 1, 244: 1, 245: 1, 246: 1, 247: 1, 248: 1, 249: 1, 250: 1, 251: 1, 252: 1, 253: 1, 254: 1,
            255: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1, 262: 1, 263: 1, 264: 1, 265: 1, 266: 1, 267: 1,
            268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1, 274: 1, 275: 1, 276: 1, 277: 1, 278: 1, 279: 1, 280: 1,
            281: 1, 282: 1, 283: 1, 284: 1, 285: 1, 286: 1, 287: 1, 288: 1, 289: 1, 290: 1, 291: 1, 292: 1, 293: 1,
            294: 1, 295: 1, 296: 1, 297: 1, 298: 1, 299: 1, 300: 1, 301: 1, 302: 1, 303: 1, 304: 1, 305: 1, 306: 1,
            307: 1, 308: 1, 309: 1, 310: 1, 311: 1, 312: 1, 313: 1, 314: 1, 315: 1, 316: 1, 317: 1, 318: 1, 319: 1,
            320: 1, 321: 1, 322: 1, 323: 1, 324: 1
            }

Entreprenant_H = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
                  23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 8, 30: 8, 31: 8, 32: 8, 33: 8, 34: 8, 35: 8, 36: 7,
                  37: 7, 38: 7, 39: 7, 40: 7, 41: 7, 42: 7, 43: 6, 44: 6, 45: 6, 46: 6, 47: 6, 48: 6, 49: 6, 50: 6,
                  51: 6, 52: 5, 53: 5, 54: 5, 55: 5, 56: 5, 57: 5, 58: 5, 59: 5, 60: 5, 61: 5, 62: 5, 63: 4, 64: 4,
                  65: 4, 66: 4, 67: 4, 68: 4, 69: 4, 70: 4, 71: 4, 72: 3, 73: 3, 74: 3, 75: 3, 76: 3, 77: 3, 78: 3,
                  79: 3, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 2, 86: 2, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
                  93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
                  106: 1, 107: 1, 108: 1, 109: 1, 110: 1, 111: 1, 112: 1, 113: 1, 114: 1, 115: 1, 116: 1, 117: 1,
                  118: 1, 119: 1, 120: 1, 121: 1, 122: 1, 123: 1, 124: 1, 125: 1, 126: 1, 127: 1, 128: 1, 129: 1,
                  130: 1, 131: 1, 132: 1, 133: 1, 134: 1, 135: 1, 136: 1, 137: 1, 138: 1, 139: 1, 140: 1, 141: 1,
                  142: 1, 143: 1, 144: 1, 145: 1, 146: 1, 147: 1, 148: 1, 149: 1, 150: 1, 151: 1, 152: 1, 153: 1,
                  154: 1, 155: 1, 156: 1, 157: 1, 158: 1, 159: 1, 160: 1, 161: 1, 162: 1, 163: 1, 164: 1, 165: 1,
                  166: 1, 167: 1, 168: 1, 169: 1, 170: 1, 171: 1, 172: 1, 173: 1, 174: 1, 175: 1, 176: 1, 177: 1,
                  178: 1, 179: 1, 180: 1, 181: 1, 182: 1, 183: 1, 184: 1, 185: 1, 186: 1, 187: 1, 188: 1, 189: 1,
                  190: 1, 191: 1, 192: 1, 193: 1, 194: 1, 195: 1, 196: 1, 197: 1, 198: 1, 199: 1, 200: 1, 201: 1,
                  202: 1, 203: 1, 204: 1, 205: 1, 206: 1, 207: 1, 208: 1, 209: 1, 210: 1, 211: 1, 212: 1, 213: 1,
                  214: 1, 215: 1, 216: 1, 217: 1, 218: 1, 219: 1, 220: 1, 221: 1, 222: 1, 223: 1, 224: 1, 225: 1,
                  226: 1, 227: 1, 228: 1, 229: 1, 230: 1, 231: 1, 232: 1, 233: 1, 234: 1, 235: 1, 236: 1, 237: 1,
                  238: 1, 239: 1, 240: 1, 241: 1, 242: 1, 243: 1, 244: 1, 245: 1, 246: 1, 247: 1, 248: 1, 249: 1,
                  250: 1, 251: 1, 252: 1, 253: 1, 254: 1, 255: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1,
                  262: 1, 263: 1, 264: 1, 265: 1, 266: 1, 267: 1, 268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1,
                  274: 1, 275: 1, 276: 1, 277: 1, 278: 1, 279: 1, 280: 1, 281: 1, 282: 1, 283: 1, 284: 1, 285: 1,
                  286: 1, 287: 1, 288: 1, 289: 1, 290: 1, 291: 1, 292: 1, 293: 1, 294: 1, 295: 1, 296: 1, 297: 1,
                  298: 1, 299: 1, 300: 1, 301: 1, 302: 1, 303: 1, 304: 1, 305: 1, 306: 1, 307: 1, 308: 1, 309: 1,
                  310: 1, 311: 1, 312: 1, 313: 1, 314: 1, 315: 1, 316: 1, 317: 1, 318: 1, 319: 1, 320: 1, 321: 1,
                  322: 1, 323: 1, 324: 1
                  }
Entreprenant_F = {9: 9, 10: 9, 11: 9, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
                  23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 8, 35: 8, 36: 8,
                  37: 8, 38: 8, 39: 7, 40: 7, 41: 7, 42: 7, 43: 7, 44: 7, 45: 7, 46: 6, 47: 6, 48: 6, 49: 6, 50: 6,
                  51: 6, 52: 6, 53: 6, 54: 6, 55: 6, 56: 6, 57: 5, 58: 5, 59: 5, 60: 5, 61: 5, 62: 5, 63: 5, 64: 5,
                  65: 5, 66: 4, 67: 4, 68: 4, 69: 4, 70: 4, 71: 4, 72: 4, 73: 4, 74: 3, 75: 3, 76: 3, 77: 3, 78: 3,
                  79: 3, 80: 2, 81: 2, 82: 2, 83: 2, 84: 1, 85: 1, 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 91: 1, 92: 1,
                  93: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1, 100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1,
                  106: 1, 107: 1, 108: 1, 109: 1, 110: 1, 111: 1, 112: 1, 113: 1, 114: 1, 115: 1, 116: 1, 117: 1,
                  118: 1, 119: 1, 120: 1, 121: 1, 122: 1, 123: 1, 124: 1, 125: 1, 126: 1, 127: 1, 128: 1, 129: 1,
                  130: 1, 131: 1, 132: 1, 133: 1, 134: 1, 135: 1, 136: 1, 137: 1, 138: 1, 139: 1, 140: 1, 141: 1,
                  142: 1, 143: 1, 144: 1, 145: 1, 146: 1, 147: 1, 148: 1, 149: 1, 150: 1, 151: 1, 152: 1, 153: 1,
                  154: 1, 155: 1, 156: 1, 157: 1, 158: 1, 159: 1, 160: 1, 161: 1, 162: 1, 163: 1, 164: 1, 165: 1,
                  166: 1, 167: 1, 168: 1, 169: 1, 170: 1, 171: 1, 172: 1, 173: 1, 174: 1, 175: 1, 176: 1, 177: 1,
                  178: 1, 179: 1, 180: 1, 181: 1, 182: 1, 183: 1, 184: 1, 185: 1, 186: 1, 187: 1, 188: 1, 189: 1,
                  190: 1, 191: 1, 192: 1, 193: 1, 194: 1, 195: 1, 196: 1, 197: 1, 198: 1, 199: 1, 200: 1, 201: 1,
                  202: 1, 203: 1, 204: 1, 205: 1, 206: 1, 207: 1, 208: 1, 209: 1, 210: 1, 211: 1, 212: 1, 213: 1,
                  214: 1, 215: 1, 216: 1, 217: 1, 218: 1, 219: 1, 220: 1, 221: 1, 222: 1, 223: 1, 224: 1, 225: 1,
                  226: 1, 227: 1, 228: 1, 229: 1, 230: 1, 231: 1, 232: 1, 233: 1, 234: 1, 235: 1, 236: 1, 237: 1,
                  238: 1, 239: 1, 240: 1, 241: 1, 242: 1, 243: 1, 244: 1, 245: 1, 246: 1, 247: 1, 248: 1, 249: 1,
                  250: 1, 251: 1, 252: 1, 253: 1, 254: 1, 255: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1,
                  262: 1, 263: 1, 264: 1, 265: 1, 266: 1, 267: 1, 268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1,
                  274: 1, 275: 1, 276: 1, 277: 1, 278: 1, 279: 1, 280: 1, 281: 1, 282: 1, 283: 1, 284: 1, 285: 1,
                  286: 1, 287: 1, 288: 1, 289: 1, 290: 1, 291: 1, 292: 1, 293: 1, 294: 1, 295: 1, 296: 1, 297: 1,
                  298: 1, 299: 1, 300: 1, 301: 1, 302: 1, 303: 1, 304: 1, 305: 1, 306: 1, 307: 1, 308: 1, 309: 1,
                  310: 1, 311: 1, 312: 1, 313: 1, 314: 1, 315: 1, 316: 1, 317: 1, 318: 1, 319: 1, 320: 1, 321: 1,
                  322: 1, 323: 1, 324: 1
                  }

Conventionnel_H = {9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
                   23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9, 36: 9,
                   37: 9, 38: 9, 39: 9, 40: 9, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 9, 47: 9, 48: 9, 49: 9, 50: 9,
                   51: 9, 52: 9, 53: 9, 54: 9, 55: 9, 56: 9, 57: 9, 58: 9, 59: 9, 60: 9, 61: 9, 62: 9, 63: 9, 64: 9,
                   65: 9, 66: 9, 67: 9, 68: 9, 69: 9, 70: 9, 71: 9, 72: 9, 73: 9, 74: 9, 75: 9, 76: 9, 77: 9, 78: 9,
                   79: 9, 80: 9, 81: 9, 82: 9, 83: 9, 84: 9, 85: 9, 86: 9, 87: 9, 88: 8, 89: 8, 90: 8, 91: 8, 92: 8,
                   93: 8, 94: 8, 95: 8, 96: 8, 97: 8, 98: 8, 99: 8, 100: 8, 101: 7, 102: 7, 103: 7, 104: 7, 105: 7,
                   106: 7, 107: 7, 108: 7, 109: 7, 110: 7, 111: 7, 112: 7, 113: 7, 114: 7, 115: 7, 116: 7, 117: 7,
                   118: 7, 119: 7, 120: 6, 121: 6, 122: 6, 123: 6, 124: 6, 125: 6, 126: 6, 127: 6, 128: 6, 129: 6,
                   130: 6, 131: 6, 132: 6, 133: 6, 134: 6, 135: 6, 136: 6, 137: 6, 138: 6, 139: 5, 140: 5, 141: 5,
                   142: 5, 143: 5, 144: 5, 145: 5, 146: 5, 147: 5, 148: 5, 149: 5, 150: 5, 151: 5, 152: 5, 153: 5,
                   154: 5, 155: 5, 156: 4, 157: 4, 158: 4, 159: 4, 160: 4, 161: 4, 162: 4, 163: 4, 164: 4, 165: 4,
                   166: 4, 167: 4, 168: 4, 169: 4, 170: 3, 171: 3, 172: 3, 173: 3, 174: 3, 175: 3, 176: 3, 177: 3,
                   178: 3, 179: 3, 180: 3, 181: 3, 182: 2, 183: 2, 184: 2, 185: 2, 186: 2, 187: 2, 188: 2, 189: 2,
                   190: 1, 191: 1, 192: 1, 193: 1, 194: 1, 195: 1, 196: 1, 197: 1, 198: 1, 199: 1, 200: 1, 201: 1,
                   202: 1, 203: 1, 204: 1, 205: 1, 206: 1, 207: 1, 208: 1, 209: 1, 210: 1, 211: 1, 212: 1, 213: 1,
                   214: 1, 215: 1, 216: 1, 217: 1, 218: 1, 219: 1, 220: 1, 221: 1, 222: 1, 223: 1, 224: 1, 225: 1,
                   226: 1, 227: 1, 228: 1, 229: 1, 230: 1, 231: 1, 232: 1, 233: 1, 234: 1, 235: 1, 236: 1, 237: 1,
                   238: 1, 239: 1, 240: 1, 241: 1, 242: 1, 243: 1, 244: 1, 245: 1, 246: 1, 247: 1, 248: 1, 249: 1,
                   250: 1, 251: 1, 252: 1, 253: 1, 254: 1, 255: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1,
                   262: 1, 263: 1, 264: 1, 265: 1, 266: 1, 267: 1, 268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1,
                   274: 1, 275: 1, 276: 1, 277: 1, 278: 1, 279: 1, 280: 1, 281: 1, 282: 1, 283: 1, 284: 1, 285: 1,
                   286: 1, 287: 1, 288: 1, 289: 1, 290: 1, 291: 1, 292: 1, 293: 1, 294: 1, 295: 1, 296: 1, 297: 1,
                   298: 1, 299: 1, 300: 1, 301: 1, 302: 1, 303: 1, 304: 1, 305: 1, 306: 1, 307: 1, 308: 1, 309: 1,
                   310: 1, 311: 1, 312: 1, 313: 1, 314: 1, 315: 1, 316: 1, 317: 1, 318: 1, 319: 1, 320: 1, 321: 1,
                   322: 1, 323: 1, 324: 1
                   }
Conventionnel_F = {9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 9, 19: 9, 20: 9, 21: 9, 22: 9,
                   23: 9, 24: 9, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9, 36: 9,
                   37: 9, 38: 9, 39: 9, 40: 9, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 9, 47: 9, 48: 9, 49: 9, 50: 9,
                   51: 9, 52: 9, 53: 9, 54: 9, 55: 9, 56: 9, 57: 9, 58: 9, 59: 9, 60: 9, 61: 9, 62: 9, 63: 9, 64: 9,
                   65: 9, 66: 9, 67: 9, 68: 9, 69: 9, 70: 9, 71: 9, 72: 9, 73: 9, 74: 9, 75: 9, 76: 9, 77: 9, 78: 9,
                   79: 9, 80: 9, 81: 8, 82: 8, 83: 8, 84: 8, 85: 8, 86: 8, 87: 8, 88: 8, 89: 8, 90: 8, 91: 8, 92: 8,
                   93: 8, 94: 8, 95: 8, 96: 8, 97: 8, 98: 8, 99: 8, 100: 8, 101: 8, 102: 8, 103: 8, 104: 7, 105: 7,
                   106: 7, 107: 7, 108: 7, 109: 7, 110: 7, 111: 7, 112: 7, 113: 7, 114: 7, 115: 7, 116: 7, 117: 7,
                   118: 7, 119: 7, 120: 7, 121: 7, 122: 7, 123: 7, 124: 7, 125: 7, 126: 6, 127: 6, 128: 6, 129: 6,
                   130: 6, 131: 6, 132: 6, 133: 6, 134: 6, 135: 6, 136: 6, 137: 6, 138: 6, 139: 6, 140: 6, 141: 6,
                   142: 6, 143: 6, 144: 6, 145: 6, 146: 5, 147: 5, 148: 5, 149: 5, 150: 5, 151: 5, 152: 5, 153: 5,
                   154: 5, 155: 5, 156: 5, 157: 5, 158: 5, 159: 5, 160: 5, 161: 5, 162: 4, 163: 4, 164: 4, 165: 4,
                   166: 4, 167: 4, 168: 4, 169: 4, 170: 4, 171: 4, 172: 4, 173: 4, 174: 3, 175: 3, 176: 3, 177: 3,
                   178: 3, 179: 3, 180: 3, 181: 3, 182: 3, 183: 2, 184: 2, 185: 2, 186: 2, 187: 2, 188: 1, 189: 1,
                   190: 1, 191: 1, 192: 1, 193: 1, 194: 1, 195: 1, 196: 1, 197: 1, 198: 1, 199: 1, 200: 1, 201: 1,
                   202: 1, 203: 1, 204: 1, 205: 1, 206: 1, 207: 1, 208: 1, 209: 1, 210: 1, 211: 1, 212: 1, 213: 1,
                   214: 1, 215: 1, 216: 1, 217: 1, 218: 1, 219: 1, 220: 1, 221: 1, 222: 1, 223: 1, 224: 1, 225: 1,
                   226: 1, 227: 1, 228: 1, 229: 1, 230: 1, 231: 1, 232: 1, 233: 1, 234: 1, 235: 1, 236: 1, 237: 1,
                   238: 1, 239: 1, 240: 1, 241: 1, 242: 1, 243: 1, 244: 1, 245: 1, 246: 1, 247: 1, 248: 1, 249: 1,
                   250: 1, 251: 1, 252: 1, 253: 1, 254: 1, 255: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1,
                   262: 1, 263: 1, 264: 1, 265: 1, 266: 1, 267: 1, 268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1,
                   274: 1, 275: 1, 276: 1, 277: 1, 278: 1, 279: 1, 280: 1, 281: 1, 282: 1, 283: 1, 284: 1, 285: 1,
                   286: 1, 287: 1, 288: 1, 289: 1, 290: 1, 291: 1, 292: 1, 293: 1, 294: 1, 295: 1, 296: 1, 297: 1,
                   298: 1, 299: 1, 300: 1, 301: 1, 302: 1, 303: 1, 304: 1, 305: 1, 306: 1, 307: 1, 308: 1, 309: 1,
                   310: 1, 311: 1, 312: 1, 313: 1, 314: 1, 315: 1, 316: 1, 317: 1, 318: 1, 319: 1, 320: 1, 321: 1,
                   322: 1, 323: 1, 324: 1
                   }

Réaliste_H = {9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0,
              23: 0, 24: 0, 25: 0, 26: 0, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9, 36: 9,
              37: 9, 38: 9, 39: 9, 40: 9, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 9, 47: 9, 48: 9, 49: 9, 50: 9,
              51: 9, 52: 9, 53: 9, 54: 9, 55: 9, 56: 9, 57: 9, 58: 9, 59: 9, 60: 9, 61: 9, 62: 9, 63: 9, 64: 9,
              65: 9, 66: 9, 67: 9, 68: 9, 69: 9, 70: 9, 71: 9, 72: 9, 73: 9, 74: 9, 75: 9, 76: 9, 77: 9, 78: 9,
              79: 9, 80: 9, 81: 9, 82: 9, 83: 9, 84: 9, 85: 9, 86: 9, 87: 9, 88: 9, 89: 9, 90: 9, 91: 9, 92: 9,
              93: 9, 94: 9, 95: 9, 96: 9, 97: 9, 98: 9, 99: 9, 100: 9, 101: 9, 102: 9, 103: 9, 104: 9, 105: 9,
              106: 9, 107: 9, 108: 9, 109: 9, 110: 9, 111: 9, 112: 9, 113: 9, 114: 9, 115: 9, 116: 9, 117: 9,
              118: 9, 119: 8, 120: 8, 121: 8, 122: 8, 123: 8, 124: 8, 125: 8, 126: 8, 127: 8, 128: 8, 129: 8,
              130: 8, 131: 8, 132: 8, 133: 8, 134: 8, 135: 8, 136: 8, 137: 8, 138: 8, 139: 8, 140: 8, 141: 8,
              142: 8, 143: 8, 144: 8, 145: 8, 146: 8, 147: 8, 148: 8, 149: 8, 150: 7, 151: 7, 152: 7, 153: 7,
              154: 7, 155: 7, 156: 7, 157: 7, 158: 7, 159: 7, 160: 7, 161: 7, 162: 7, 163: 7, 164: 7, 165: 7,
              166: 7, 167: 6, 168: 6, 169: 6, 170: 6, 171: 6, 172: 6, 173: 6, 174: 6, 175: 6, 176: 6, 177: 6,
              178: 6, 179: 6, 180: 6, 181: 6, 182: 6, 183: 6, 184: 6, 185: 6, 186: 5, 187: 5, 188: 5, 189: 5,
              190: 5, 191: 5, 192: 5, 193: 5, 194: 5, 195: 5, 196: 5, 197: 5, 198: 5, 199: 5, 200: 5, 201: 4,
              202: 4, 203: 4, 204: 4, 205: 4, 206: 4, 207: 4, 208: 4, 209: 4, 210: 4, 211: 4, 212: 4, 213: 4,
              214: 4, 215: 3, 216: 3, 217: 3, 218: 3, 219: 3, 220: 3, 221: 3, 222: 3, 223: 3, 224: 3, 225: 3,
              226: 3, 227: 3, 228: 2, 229: 2, 230: 2, 231: 2, 232: 2, 233: 2, 234: 2, 235: 2, 236: 2, 237: 2,
              238: 2, 239: 2, 240: 2, 241: 2, 242: 2, 243: 2, 244: 2, 245: 2, 246: 2, 247: 2, 248: 2, 249: 2,
              250: 2, 251: 1, 252: 1, 253: 1, 254: 1, 255: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1,
              262: 1, 263: 1, 264: 1, 265: 1, 266: 1, 267: 1, 268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1,
              274: 1, 275: 1, 276: 1, 277: 1, 278: 1, 279: 1, 280: 1, 281: 1, 282: 1, 283: 1, 284: 1, 285: 1,
              286: 1, 287: 1, 288: 1, 289: 1, 290: 1, 291: 1, 292: 1, 293: 1, 294: 1, 295: 1, 296: 1, 297: 1,
              298: 1, 299: 1, 300: 1, 301: 1, 302: 1, 303: 1, 304: 1, 305: 1, 306: 1, 307: 1, 308: 1, 309: 1,
              310: 1, 311: 1, 312: 1, 313: 1, 314: 1, 315: 1, 316: 1, 317: 1, 318: 1, 319: 1, 320: 1, 321: 1,
              322: 1, 323: 1, 324: 1
              }
Réaliste_F = {9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0,
              23: 0, 24: 0, 25: 0, 26: 0, 27: 9, 28: 9, 29: 9, 30: 9, 31: 9, 32: 9, 33: 9, 34: 9, 35: 9, 36: 9,
              37: 9, 38: 9, 39: 9, 40: 9, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 9, 47: 9, 48: 9, 49: 9, 50: 9,
              51: 9, 52: 9, 53: 9, 54: 9, 55: 9, 56: 9, 57: 9, 58: 9, 59: 9, 60: 9, 61: 9, 62: 9, 63: 9, 64: 9,
              65: 9, 66: 9, 67: 9, 68: 9, 69: 9, 70: 9, 71: 9, 72: 9, 73: 9, 74: 9, 75: 9, 76: 9, 77: 9, 78: 9,
              79: 9, 80: 9, 81: 9, 82: 9, 83: 9, 84: 9, 85: 9, 86: 9, 87: 9, 88: 9, 89: 9, 90: 9, 91: 9, 92: 9,
              93: 9, 94: 9, 95: 9, 96: 9, 97: 9, 98: 9, 99: 9, 100: 9, 101: 9, 102: 9, 103: 9, 104: 9, 105: 9,
              106: 9, 107: 9, 108: 9, 109: 9, 110: 9, 111: 9, 112: 9, 113: 9, 114: 9, 115: 9, 116: 9, 117: 9,
              118: 9, 119: 9, 120: 9, 121: 9, 122: 9, 123: 9, 124: 9, 125: 9, 126: 9, 127: 9, 128: 9, 129: 9,
              130: 9, 131: 9, 132: 9, 133: 9, 134: 9, 135: 9, 136: 9, 137: 9, 138: 9, 139: 9, 140: 9, 141: 9,
              142: 9, 143: 9, 144: 9, 145: 9, 146: 9, 147: 9, 148: 9, 149: 9, 150: 9, 151: 9, 152: 9, 153: 9,
              154: 9, 155: 8, 156: 8, 157: 8, 158: 8, 159: 8, 160: 8, 161: 8, 162: 8, 163: 8, 164: 8, 165: 8,
              166: 8, 167: 8, 168: 8, 169: 8, 170: 8, 171: 8, 172: 8, 173: 8, 174: 8, 175: 8, 176: 8, 177: 8,
              178: 7, 179: 7, 180: 7, 181: 7, 182: 7, 183: 7, 184: 7, 185: 7, 186: 7, 187: 7, 188: 7, 189: 7,
              190: 7, 191: 7, 192: 7, 193: 7, 194: 7, 195: 6, 196: 6, 197: 6, 198: 6, 199: 6, 200: 6, 201: 6,
              202: 6, 203: 6, 204: 6, 205: 6, 206: 6, 207: 5, 208: 5, 209: 5, 210: 5, 211: 5, 212: 5, 213: 5,
              214: 5, 215: 5, 216: 5, 217: 5, 218: 5, 219: 5, 220: 4, 221: 4, 222: 4, 223: 4, 224: 4, 225: 4,
              226: 4, 227: 4, 228: 4, 229: 4, 230: 4, 231: 3, 232: 3, 233: 3, 234: 3, 235: 3, 236: 3, 237: 3,
              238: 3, 239: 3, 240: 3, 241: 3, 242: 2, 243: 2, 244: 2, 245: 2, 246: 2, 247: 2, 248: 2, 249: 2,
              250: 2, 251: 2, 252: 2, 253: 2, 254: 2, 255: 2, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1,
              262: 1, 263: 1, 264: 1, 265: 1, 266: 1, 267: 1, 268: 1, 269: 1, 270: 1, 271: 1, 272: 1, 273: 1,
              274: 1, 275: 1, 276: 1, 277: 1, 278: 1, 279: 1, 280: 1, 281: 1, 282: 1, 283: 1, 284: 1, 285: 1,
              286: 1, 287: 1, 288: 1, 289: 1, 290: 1, 291: 1, 292: 1, 293: 1, 294: 1, 295: 1, 296: 1, 297: 1,
              298: 1, 299: 1, 300: 1, 301: 1, 302: 1, 303: 1, 304: 1, 305: 1, 306: 1, 307: 1, 308: 1, 309: 1,
              310: 1, 311: 1, 312: 1, 313: 1, 314: 1, 315: 1, 316: 1, 317: 1, 318: 1, 319: 1, 320: 1, 321: 1,
              322: 1, 323: 1, 324: 1
              }


#===================================================================================================
#===========================================INSTANCIATION==========================================
#==================================================================================================





if __name__ == '__main__':

    # configuration of the page
    img1=Image.open("ImageMin.png")

    st.set_page_config(
        page_title="Bien Commun",
        page_icon=img1,
        layout="wide"
    )



    formulaire= Formulaire(nom='Nume',
                            prénom='Prenume',
                            ddn='Data de nastere',
                            formation='Formare',
                            emploi='Loc de munca actual',
                            sexe_sujet='Sex  (F sau M)',
                            emploi_envisagé='Loc de munca dorit',
                            numtel='Numar de telefon',
                            Email='adresa de Email',
                            user1="contactbiencommun@gmail.com",
                            mypassword="2022Succes.",
                            mailto="j.ralaizanaka@gmail.com",
                            sujet="Nou potential client",
                            messageRes="Sa trecem la actiune",
                            nom_bouton_soumettre='Trimite')

    formulaire.cree_en_tête(image="ImageBC.png",
                            titre="RADIOGRAPHIE PROFESIONALA:",
                            sous_titre="Formular de contact 🎨")

    v=formulaire.cree_formulaire()

    message1 = "Va rog sa completati si sa verificati formularul pentru a putea merge mai departe"

    init_intitule = "Test de personalitate: "
    init_msgChoixNote = "Alege o nota"
    init_msgVerif = "Verifica"
    init_msgErreur = "EROARE: FIECARE TREBUIE TREBUIE SĂ AIMNĂ O EVALUAȚIE DIFERITĂ!!!!  "
    init_msg1 = "Notă "
    init_msg2 = " se repetă"
    init_msg3 = "notele "
    init_msg4 = " se repetă"
    init_msg5 = " este disponibilă"
    init_msg6 = " sunt disponibile"
    init_msg7 = "poți sări peste "

    radiographieA = Radiographie(
        range_metier=liste_métier,
        nom_test1="TEST A",
        nom_test2="TEST B",
        i_débuttemp=0,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieB = Radiographie(
        range_metier=liste_métier,
        nom_test1="TEST B",
        nom_test2="TEST C",
        i_débuttemp=12,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"

    )

    radiographieC = Radiographie(
        range_metier=liste_métier,
        nom_test1="TEST C",
        nom_test2="TEST D",
        i_débuttemp=24,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieD = Radiographie(
        range_metier=liste_métier,
        nom_test1="TEST D",
        nom_test2="TEST E",
        i_débuttemp=36,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieE = Radiographie(
        range_metier=liste_métier,
        nom_test1="TEST E",
        nom_test2="TEST F",
        i_débuttemp=48,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieF = Radiographie(
        range_metier=liste_métier,
        nom_test1="TEST F",
        nom_test2="TEST G",
        i_débuttemp=60,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieG = Radiographie(
        range_metier=liste_métier,
        nom_test1="TEST G",
        nom_test2="TEST H",
        i_débuttemp=72,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieH = Radiographie(
        range_metier=liste_métier,
        nom_test1="TEST H",
        nom_test2="TEST I",
        i_débuttemp=84,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieI = Radiographie(
        range_metier=liste_métier,
        nom_test1="TEST I",
        nom_test2="bilan",
        i_débuttemp=96,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    # edit Video

    radiographieA.insert_video('madga_vs_roum.mp4')

    # edit formulaire A

    result = radiographieA.edit_test()
    totalnote = result[0]
    totalmetier = result[1]
    verifT = []
    verifT.append(result[2])

    # edit formulaire B

    result1 = radiographieB.edit_test()
    totalnote = totalnote + result1[0]
    totalmetier = totalmetier + result1[1]
    verifT.append(result1[2])

    # edit formulaire C

    result2 = radiographieC.edit_test()
    totalnote = totalnote + result2[0]
    totalmetier = totalmetier + result2[1]
    verifT.append(result2[2])

    # edit formulaire D

    result3 = radiographieD.edit_test()
    totalnote = totalnote + result3[0]
    totalmetier = totalmetier + result3[1]
    verifT.append(result3[2])

    # edit formulaire E

    result4 = radiographieE.edit_test()
    totalnote = totalnote + result4[0]
    totalmetier = totalmetier + result4[1]
    verifT.append(result4[2])

    # edit formulaire F

    result5 = radiographieF.edit_test()
    totalnote = totalnote + result5[0]
    totalmetier = totalmetier + result5[1]
    verifT.append(result5[2])

    # edit formulaire G

    result6 = radiographieG.edit_test()
    totalnote = totalnote + result6[0]
    totalmetier = totalmetier + result6[1]
    verifT.append(result6[2])

    # edit formulaire H

    result7 = radiographieH.edit_test()
    totalnote = totalnote + result7[0]
    totalmetier = totalmetier + result7[1]
    verifT.append(result7[2])

    # edit formulaire I

    result8 = radiographieI.edit_test()
    totalnote = totalnote + result8[0]
    totalmetier = totalmetier + result8[1]
    verifT.append(result8[2])

    # =============================================================================================
    genre = st.radio(
        "Doriți un raport în PDF?",
        ('Da', 'Nu'))

    if genre == 'Da':
        adressmail = st.text_input("Introdu adresa ta de e-mail")

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////:::

    st.markdown("""
                           Introduceți mai jos cele 3 profesii pe care le preferați între toate cele indicate sau nu pe această pagină.

                       """)

    with st.form(key='metier3'):
        col1, col2, col3 = st.columns(3)

        with col1:
            métier1 = st.text_input('Job 1')

        with col2:
            métier2 = st.text_input('Job 2')
        with col3:
            métier3 = st.text_input('Job 3')

        submitted = st.form_submit_button('Obțineți rezultatele')
        if submitted == True:

            if (verifT[0] == False and verifT[1] == False and verifT[2] == False and verifT[3] == False and \
                    verifT[4] == False and verifT[5] == False and verifT[6] == False and verifT[7] == False and verifT[
                        8] == False and v == True):
                st.success("Teste finalizate. aici sunt rezultatele")
                time.sleep(2)

                # ==========================================================================================================
                st.subheader("Interese generale")


                def plot_radar(data1, data2):
                    df = pd.DataFrame(dict(r=data1, theta=data2))
                    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
                    st.plotly_chart(fig, use_container_width=True)


                bilan = Bilan(liste_domaine, liste_intéret_generaux)

                dtemp = bilan.intérêt_généraux_etalonne(totalnote, formulaire.sexe_sujet)

                r = list(dtemp.values())

                theta = list(dtemp.keys())

                plot_radar(r, theta)

                st.subheader("Interese specifice")

                def plot_bar(domaines, val):
                    fig = go.Figure(go.Bar(
                        x=val,
                        y=domaines,
                        marker={'color': val,
                                'colorscale': 'blugrn'},
                        orientation='h'))
                    st.plotly_chart(fig, use_container_width=True)


                d1 = bilan.get_interet_etalonne(totalnote, formulaire.sexe_sujet)

                d_list = list(d1.values())

                domaines = liste_domaine
                val = d_list

                d = {'domaines': domaines, 'val': val}
                df = pd.DataFrame(data=d)
                df1 = df.sort_values(by=['val'], ascending=True)

                plot_bar(df1['domaines'], df1['val'])

                # ====================================================================================================

                st.subheader("Cele trei profesii ale tale preferate") #"Vos trois métier préférés


                def plot_met(m1, m2, m3):
                    fig1 = go.Figure(data=[go.Table(header=dict(values=['Meserii']),
                                                    cells=dict(values=[[m1, m2, m3]]))
                                           ])
                    st.plotly_chart(fig1, use_container_width=True)


                m1 = métier1
                m2 = métier2
                m3 = métier3

                plot_met(m1, m2, m3)

                # ================================================ EMAILING RAPPORT=======================================================
                if genre == "Da":
                    # bar chart
                    fig = go.Figure(go.Bar(
                        x=df1['val'],  # val,
                        y=df1['domaines'],  # domaines,
                        marker={'color': val,
                                'colorscale': 'blugrn'},
                        orientation='h'))
                    fig.update_layout(title_text="Interese specifice", title_x=0.5)

                    # radar chart
                    df = pd.DataFrame(dict(r=r, theta=theta))
                    fig2 = px.line_polar(df, r='r', theta='theta', line_close=True)
                    fig2.update_layout(title_text="Interese generale", title_x=0.5)

                    with NamedTemporaryFile("r+b", delete=False) as fd:
                        fig.write_image(fd)
                        fd.seek(0)

                    with NamedTemporaryFile("r+b", delete=False) as fd1:
                        fig2.write_image(fd1)
                        fd1.seek(0)

                    pdf = FPDF()

                    # Add a page
                    pdf.add_page()

                    # set style and size of font
                    # that you want in the pdf
                    pdf.set_font("Arial", "B", size=15)

                    # create a cell
                    pdf.cell(180, 15, txt="RAPORTUL",
                             ln=1, align='C')

                    # add another cell
                    pdf.set_font('Arial', "IU", size=14)
                    pdf.cell(180, 15, txt="Rezultatele radiografiei dumneavoastra profesionale.",#"Résultats de votre Radiographie Professionnelle.",
                             ln=2, align='C')

                    # pdf.cell(255, 15, txt="Contactez-vous à l’adresse: magda.roaita@bien-commun.fr",
                    #  ln=2, align='C')

                    pdf.image(fd1.name, x=20, y=40, w=160, h=120)

                    pdf.image(fd.name, x=30, y=150, w=144, h=108)

                    pdf.image("StickerOrange.png", x=5, y=5)

                    pdf.image("CaptureRoumain.png", x=30, y=270)

                    with NamedTemporaryFile("r+b", delete=False, suffix='.pdf') as fd3:
                        pdf.output(fd3)
                        fd3.seek(0)

                    user1 = "contactbiencommun@gmail.com"
                    mypassword = "2022Succes."

                    mailto = adressmail

                    message1 = "Vă rugăm să găsiți atașat raportul dvs"#"Veuillez trouver ci-joint votre rapport"

                    yag = yagmail.SMTP(user=user1, password=mypassword)
                    # sending the email
                    yag.send(to=adressmail, subject='Rezultatele radiografiei dumneavoastră profesionale.', contents=message1, attachments=fd3.name)

                    fd.close()
                    fd1.close()
                    fd3.close()

                    st.success("Raport trimis")#Rapport Envoyé




        else:

                if verifT[0] == True:
                    st.error("Testul A a fost făcut greșit")

                if verifT[1] == True:
                    st.error("Testul B a fost făcut greșit")

                if verifT[2] == True:
                    st.error("Testul C a fost făcut greșit")

                if verifT[3] == True:
                    st.error("Testul D a fost făcut greșit")

                if verifT[4] == True:
                    st.error("Testul E a fost făcut greșit")

                if verifT[5] == True:
                    st.error("Testul F a fost făcut greșit")

                if verifT[6] == True:
                    st.error("Testul G a fost făcut greșit")

                if verifT[7] == True:
                    st.error("Testul H a fost făcut greșit")

                if verifT[8] == True:
                    st.error("Testul I a fost făcut greșit")

                if v == False:
                    st.error("Nu ați trimis formularul")

                # =======================================================================================================

                # =======================================================================================================


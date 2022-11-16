import pytest
import json

from scrapper import Video

class TestVideo:
    
    def testTitle(self):
        video = Video("fmsoym8I-3o")
        video.set_video_infos()
        assert(video.title ==  "Pierre Niney : L\u2019interview face cach\u00e9e par HugoD\u00e9crypte") is True

    def testDescription(self):
        video = Video("fmsoym8I-3o")
        video.set_video_infos()
        assert(video.description ==  "\ud83c\udf7f L'acteur Pierre Niney est dans L\u2019interview face cach\u00e9e ! Ces prochains mois, le format revient plus fort avec des artistes, sportifs, etc.\n\ud83d\udd14 Abonnez-vous pour ne manquer aucune vid\u00e9o.\n\nInterview r\u00e9alis\u00e9e \u00e0 l\u2019occasion de la sortie du film \u00ab\u00a0Mascarade\u00a0\u00bb r\u00e9alis\u00e9 par Nicolas Bedos, le 1er novembre 2022 au cin\u00e9ma. Avec Pierre Niney, Isabelle Adjani, Fran\u00e7ois Cluzet, Marine Vacth.\n\nChaleureux remerciements au cin\u00e9ma mk2 Biblioth\u00e8que pour son accueil.\n\n\u2014\n\n00:00 Intro\n00:22 1\n03:32 2\n10:11 3\n14:09 4\n17:28 5\n20:10 6\n23:13 7\n39:22 8\n\n\u2014\n\nPr\u00e9sent\u00e9 par Hugo Travers\n\nR\u00e9alisateur : Julien Poti\u00e9\nJournalistes : Benjamin Aleberteau, Blanche Vathonne\n\nCharg\u00e9e de production d\u00e9l\u00e9gu\u00e9e : Romane Meissonnier\nAssistant de production d\u00e9l\u00e9gu\u00e9e : Cl\u00e9ment Chaulet\nCharg\u00e9e de production ex\u00e9cutive : Marie Delvall\u00e9e\n\nChef OPV : Lucas Stoll\nOPV : Pierre Amilhat, Vanon Borget\nElectricien : Alex Henry\nChef OPS : Victor Arnaud\nStagiaire image : Magali Faizeau\n\nMaquilleuse : Kim Desnoyers\nPhotographe plateau : Erwann Tanguy\n\nMonteur-\u00e9talonneur : Stan Duplan\nMixeuse : Romane Meissonnier\n\nCheffe de projets partenariats : Mathilde Rousseau\nAssistante cheffe de projets partenariats : Manon Montoriol\n\n\u2014\n\n\u00a9 HugoD\u00e9crypte / 2022") is True

    def testAuthor(self):
        video = Video("fmsoym8I-3o")
        video.set_video_infos()
        assert(video.author == "HugoD\u00e9crypte") is True  

    def testAuthor(self):
        video = Video("fmsoym8I-3o")
        video.set_video_infos()
        assert(video.author == "HugoD\u00e9crypte") is True

    def testLikes(self):
        video = Video("fmsoym8I-3o")
        video.set_video_infos()
        assert(video.likes ==  "30609") is True
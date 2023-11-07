"""
    Ecrire un QCM et afficher le score de l'utilisateur à la fin.
    Créer une structure de données qui contiendra les questions (sous forme de chaine de caractère)
    et les réponses.
    Votre programme doit parcourir cette structure pour afficher les questions et vérifier si la réponse
    est juste.
"""

question_1 = "Q1. Quel est le résultat du calcul 2*2*2 ?\n" \
            "a) 4\n"\
            "b) 5\n"\
            "c) 6\n"

question_2 = "Q1. Quel est le résultat du calcul 3*3*3 ?\n" \
            "a) 9\n"\
            "b) 27\n"\
            "c) 56\n"

question_3 = "Q1. Quel est le résultat du calcul 1*1*1 ?\n" \
            "a) 1\n"\
            "b) 4\n"\
            "c) 8\n"

questions = {
    question_1: "a",
    question_2: "b",
    question_3: "a"
}

print("Bienvenue dans le QCM.")
score = 0

for question, reponse in questions.items():
    print(question + "\n")
    reponse_utilisateur = input("Tapez votre réponse (a/b/c/d)\n")
    if reponse_utilisateur == reponse:
        score += 1
        print("Bonne réponse.")
    else:
        print("Mauvaise réponse.")

print(f"Votre score est {score}/{len(questions)}")

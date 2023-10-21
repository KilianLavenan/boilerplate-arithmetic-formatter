def max_lenght(problem):
  return max(len(problem[0]),len(problem[2]))

def somme_deux_entiers_en_chaine(chaine1, chaine2,operator):
  entier1 = int(chaine1)
  entier2 = int(chaine2)
  if operator=="+":
    somme = entier1 + entier2
  else:
    somme=entier1 - entier2
  resultat = str(somme)
  return resultat


def arithmetic_arranger(problems,solution=False):
  # Vérifie que le nombre de problèmes est inférieur à 5
  if len(problems)>5:
    return("Error: Too many problems.")
  # Vérifie que chaque problème est bien formé
  arranged_problems=""
  cut_problems=[]
  for problem in problems:
    if "  " in problem:
      return("Error: Numbers must only contain digits.")
    cut_list=problem.split()
    operator=cut_list[1]
    if operator!="+" and operator!="-":
      return("Error: Operator must be '+' or '-'.")
    if max(len(cut_list[0]),len(cut_list[2]))>4:
      return("Error: Numbers cannot be more than four digits.")
    if not (cut_list[0].isdigit() and cut_list[2].isdigit()):
      return("Error: Numbers must only contain digits.")
    cut_problems.append(cut_list)
  ligne1=""
  ligne2=""
  ligne3=""
  ligne4=""
  for problem in cut_problems:
    res=somme_deux_entiers_en_chaine(problem[0],problem[2],problem[1])
    n=max_lenght(problem)
    ligne1+=" "*(n-len(problem[0])+2)+problem[0]
    ligne2+=problem[1]+" "*(n-len(problem[2])+1)+problem[2]
    ligne3+="-"*(n+2)
    if solution==True:
      ligne4+=" "*(n-len(res)+2)+res
    if not problem==cut_problems[-1]:
      ligne1+=" "*4
      ligne2+=" "*4
      ligne3+=" "*4
      ligne4+=" "*4
  if solution==True:
    arranged_problems+=ligne1+"\n"+ligne2+"\n"+ligne3+"\n"+ligne4
  else:
    arranged_problems+=ligne1+"\n"+ligne2+"\n"+ligne3
  print("résultat:\n"+arranged_problems)
  return arranged_problems

  
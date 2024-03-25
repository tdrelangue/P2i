from icecream import ic


def create_delivery_planning(
        quarantaine=2, suremballage=1, DLC=30, contractDate=15,
        MondayLivr=True, TuesdayLivr=True, WednesdayLivr=True, ThursdayLivr=True,
        FridayLivr=True, SaturdayLivr=True, SundayLivr=False,
        MondayProd=True, TuesdayProd=True, WednesdayProd=True, ThursdayProd=True,
        FridayProd=True, SaturdayProd=True, SundayProd=False
):
    livraison = {
        'Monday': MondayLivr,
        'Tuesday': TuesdayLivr,
        'Wednesday': WednesdayLivr,
        'Thursday': ThursdayLivr,
        'Friday': FridayLivr,
        'Saturday': SaturdayLivr,
        'Sunday': SundayLivr
    }
    production = {
        'Monday': MondayProd,
        'Tuesday': TuesdayProd,
        'Wednesday': WednesdayProd,
        'Thursday': ThursdayProd,
        'Friday': FridayProd,
        'Saturday': SaturdayProd,
        'Sunday': SundayProd
    }

    PlanningSemaine = []

    for day in range(0, len(list(livraison.values()))):
        day = 6 - day
        PlanningDuJour = []
        for i in range(0, day):
            PlanningDuJour.append(None)
        if list(production.values())[day]:
            for i in range(0, DLC):
                if not list(livraison.values())[(i+day) % 7]:
                    if DLC - i <= contractDate:
                        PlanningDuJour.append("C")
                    else:
                        PlanningDuJour.append("0")
                else:
                    if i < quarantaine + suremballage:
                        PlanningDuJour.append("0")
                    elif DLC - i <= contractDate:
                        PlanningDuJour.append("C")
                    elif len(PlanningSemaine) > 0:
                        if quarantaine + suremballage + 2 >= i:
                            if check_L_in_lists(PlanningSemaine, i+day):
                                PlanningDuJour.append("1")
                            else:
                                PlanningDuJour.append("L")
                        elif DLC - i > contractDate:
                            PlanningDuJour.append("1")
                        else:
                            PlanningDuJour.append("C")
                    else:
                        if i <= quarantaine + suremballage + 2:
                            PlanningDuJour.append("L")
                        elif DLC - i > contractDate:
                            PlanningDuJour.append("1")
                        else:
                            PlanningDuJour.append("C")
            for etat_produit in range(1, contractDate + 1):
                PlanningDuJour[-etat_produit] = 'C'
            PlanningSemaine.append(PlanningDuJour)
    PlanningSemaine = correct_last_day(PlanningSemaine[::-1])
    return PlanningSemaine


def correct_last_day(planning_to_correct):
    ajout = [None]*7
    ajout.extend(planning_to_correct[0])

    planning_to_correct.append(ajout)

    for index, value in enumerate(planning_to_correct[-1]):
        if value == 'L':
            if planning_to_correct[-2][index] == 'L':
                planning_to_correct[-2][index] = '1'

    last_useful_day = len(planning_to_correct)-1
    corrected_list = planning_to_correct[0:last_useful_day]
    return planning_to_correct[0:last_useful_day]


def print_planning(planning):
    for day in planning:
        print(day)


def check_L_in_lists(my_lists, specified_number):
    for list_to_search in my_lists:
        if check_L_in_list(list_to_search, specified_number):
            return True
    return False


def check_L_in_list(my_list, specified_number):
    if 'L' in my_list:
        index_of_L = my_list.index('L')
        return index_of_L <= specified_number
    else:
        return False


def find_worst_situation(planning):
    index_worst_week = 0
    nombre_secu_worst_prod = planning[0].count('1')

    all_equal = True
    for index, prod in enumerate(planning):
        if prod.count('1') != nombre_secu_worst_prod:
            all_equal = False

    if all_equal:
        comparer = 'L'
        nombre_secu_worst_prod = planning[0].count('L')

    else:
        comparer = '1'
    max_secu = 0
    max_prod = 0
    for index, prod in enumerate(planning):
        nombre_secu_this_prod = prod.count(comparer)
        if max_prod < prod.count('L'):
            max_prod = prod.count('L')
        if max_secu < prod.count('1'):
            max_secu = prod.count('1')
        if nombre_secu_this_prod <= nombre_secu_worst_prod:
            nombre_secu_worst_prod = nombre_secu_this_prod
            index_worst_week = index

    return nombre_secu_worst_prod, planning[index_worst_week].count('L'), max_secu, max_prod


def calculate_rupture(prod_planning):
    worst_secu_stock, associated_incompressible_prod, _, _ = find_worst_situation(prod_planning)
    rupture = []
    for i in range(0, worst_secu_stock + 1):
        rupture.append(round(i / associated_incompressible_prod*100, 1))
    b = rupture[0]
    a = rupture[1]-b

    return a, b, len(rupture)


def calculate_degagement(prod_planning):
    worst_secu_stock, associated_incompressible_prod, max_secu_stock, max_incompressible_prod = find_worst_situation(prod_planning)
    degagement = []
    for i in range(1, worst_secu_stock + 2):
        degagement.append(-round((i/(worst_secu_stock + associated_incompressible_prod)-1)*100, 1))
    b = degagement[0]
    a = round(degagement[1] - b, 2)

    return a, b, len(degagement)


if __name__ == '__main__':
    plan = create_delivery_planning()
    print_planning(plan)
    print(calculate_degagement(plan))
    print(calculate_rupture(plan))

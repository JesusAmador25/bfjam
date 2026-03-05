from bfjam import knapsack_problem

pesos = [10, 8, 3, 4, 11, 7, 13, 10, 8, 9]
beneficios = [8, 5, 7, 5, 10, 8, 11, 13, 5, 11]

def test_knapsack_problem():
    assert knapsack_problem(60, 70, pesos, beneficios) == False
    assert knapsack_problem(60,60, pesos, beneficios) == (0, 0, 1, 0, 1, 1, 1, 1, 0, 1)

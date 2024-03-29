def RK2_step(population, birth_fraction, death_proportionality_constant, other_population, DT):
    midpoint_population = population + (birth_fraction * other_population - death_proportionality_constant * population) * DT / 2
    return midpoint_population + (birth_fraction * other_population - death_proportionality_constant * midpoint_population) * DT
def RK4_step(population, birth_fraction, death_proportionality_constant, other_population, DT):
    k1 = (birth_fraction * other_population - death_proportionality_constant * population) * DT
    k2 = (birth_fraction * (other_population + k1 / 2) - death_proportionality_constant * (population + k1 / 2)) * DT
    k3 = (birth_fraction * (other_population + k2 / 2) - death_proportionality_constant * (population + k2 / 2)) * DT
    k4 = (birth_fraction * (other_population + k3) - death_proportionality_constant * (population + k3)) * DT
    return population + (k1 + 2 * k2 + 2 * k3 + k4) / 6
def PredatorPrey(DT = 0.001, simLength = 12, method='RK4'):
    numIterations = int(simLength/DT) + 1
    t = 0

    predator_population = 15
    predator_birth_fraction = 0.01
    predator_death_proportionality_constant = 1.06
    prey_population = 100
    prey_birth_fraction = 2
    prey_death_proportionality_constant = 0.02

    tLst = [t]
    predatorLst = [predator_population]
    preyLst = [prey_population]
    for i in range(1, numIterations):
        t = i * DT
        if method == 'RK2':
            predator_population = RK2_step(predator_population, predator_birth_fraction, predator_death_proportionality_constant, prey_population, DT)
            prey_population = RK2_step(prey_population, prey_birth_fraction, prey_death_proportionality_constant, predator_population, DT)
        elif method == 'RK4':
            predator_population = RK4_step(predator_population, predator_birth_fraction, predator_death_proportionality_constant, prey_population, DT)
            prey_population = RK4_step(prey_population, prey_birth_fraction, prey_death_proportionality_constant, predator_population, DT)

        tLst.append(t)
        predatorLst.append(predator_population)
        preyLst.append(prey_population)

    return tLst, predatorLst, preyLst

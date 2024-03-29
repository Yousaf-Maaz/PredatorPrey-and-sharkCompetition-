def RK2_step_shark(population, birth_fraction, death_proportionality_constant, other_population, DT):
    midpoint_population = population + (birth_fraction * other_population - death_proportionality_constant * population) * DT / 2
    return midpoint_population + (birth_fraction * other_population - death_proportionality_constant * midpoint_population) * DT
def RK4_step_shark(population, birth_fraction, death_proportionality_constant, other_population, DT):
    k1 = (birth_fraction * other_population - death_proportionality_constant * population) * DT
    k2 = (birth_fraction * (other_population + k1 / 2) - death_proportionality_constant * (population + k1 / 2)) * DT
    k3 = (birth_fraction * (other_population + k2 / 2) - death_proportionality_constant * (population + k2 / 2)) * DT
    k4 = (birth_fraction * (other_population + k3) - death_proportionality_constant * (population + k3)) * DT
    return population + (k1 + 2 * k2 + 2 * k3 + k4) / 6
def sharkCompetition(DT = 0.001, simLength = 5, method='RK4'):
    numIterations = int(simLength/DT) + 1
    t = 0

    WTS_population = 20
    BTS_population = 15

    WTS_birth_fraction = 1
    WTS_death_proportionality_constant = 0.27
    BTS_birth_fraction = 1
    BTS_death_proportionality_constant = 0.2

    tLst = [t]
    WTSLst = [WTS_population]
    BTSLst = [BTS_population]
    for i in range(1, numIterations):
        t = i * DT
        if method == 'RK2':
            WTS_population = RK2_step_shark(WTS_population, WTS_birth_fraction, WTS_death_proportionality_constant, BTS_population, DT)
            BTS_population = RK2_step_shark(BTS_population, BTS_birth_fraction, BTS_death_proportionality_constant, WTS_population, DT)
        elif method == 'RK4':
            WTS_population = RK4_step_shark(WTS_population, WTS_birth_fraction, WTS_death_proportionality_constant, BTS_population, DT)
            BTS_population = RK4_step_shark(BTS_population, BTS_birth_fraction, BTS_death_proportionality_constant, WTS_population, DT)

        tLst.append(t)
        WTSLst.append(WTS_population)
        BTSLst.append(BTS_population)

    return tLst, WTSLst, BTSLst

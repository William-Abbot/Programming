def income(extractors, spawners):
    return 80 + extractors *(30 + spawners)

def incomeSimulator(extractors, spawners, iterations):
    supply = 27
    supplyCost = 600
    minerals = 0
    spawnerSupplyCost = 4
    availableStrikelings = 30
    
    for x in range(iterations):
        maxExtractors = supply // 15
        maxSpawners = supply // 4
        bestEcoExtractorCount = 0
        bestEcoSpawnerCount = 0
        bestEcoIncome = 0
        
        for eachExtractor in range(maxExtractors+1):
            currentExtractors = eachExtractor
            currentSpawners = (supply - currentExtractors*15) // spawnerSupplyCost
            currentEco = income(extractors + currentExtractors, spawners + currentSpawners)
            
            if currentEco > bestEcoIncome:
                bestEcoExtractorCount = currentExtractors
                bestEcoSpawnerCount = currentSpawners
                bestEcoIncome = currentEco
            #print("currentEco " + str(currentEco))
            #print("currentExtractors " + str(currentExtractors))
            #print("currentSpawners " + str(currentSpawners))

        extractors += bestEcoExtractorCount
        spawners += bestEcoSpawnerCount
        supply -= bestEcoExtractorCount*15
        supply -= bestEcoSpawnerCount*spawnerSupplyCost
        supply += 45
        
        #print("bestEcoIncome " + str(bestEcoIncome))
        #print("bestEcoExtractorCount " + str(bestEcoExtractorCount))
        #print("bestEcoSpawnerCount " + str(bestEcoSpawnerCount))
        #print("\n")
    print("----------------")
    print("Total Income: "+str(income(extractors, spawners)))
    print("Total Mineral Extractors: " + str(extractors))
    print("Total Spawners: " + str(spawners))
    print("Extractor/Spawner Ratio: " + str(extractors/spawners))
    

incomeSimulator(6, 24, 20)
#Programmet lar brukeren skrive inn et genom og returnerer genene i genomet

def find_genes(genome):
    START_TRIPLET = "ATG"
    END_TRIPLETS  = ["TAG", "TAA", "TGA"]

    potential_genes = genome.split(START_TRIPLET)

    #TAG, TAA eller TGA er nødvendig for å avslutte et gen
    end_triplets_found = 0

    for i in range( len(potential_genes) ):

        for triplet in END_TRIPLETS:
            end = potential_genes[i].find(triplet)

            #str.find() returner -1 dersom substring ikke finnes i en string
            if end != -1:                                       
                end_triplets_found += 1
                potential_genes[i] = potential_genes[i][0:end]

    genes = []
    for i in range( len(potential_genes) ):

        #Tomme strings fra str.split() skal ikke tas med
        if (len(potential_genes[i]) % 3 == 0) and len(potential_genes[i]) != 0:
            genes.append(potential_genes[i])
    
    if (len(genes) == 0) or (end_triplets_found == 0):
        return "No gene is found"

    return genes

def main():
    genome_from_user = input("Enter a genome string: ")
    print(find_genes(genome_from_user))


if __name__ == "__main__":
    main()

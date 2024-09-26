def curr_population(pop) :
    s = 0 
    for i in range(len(pop)) :
        s == pop[i] 

    return s 

def change_growth(gr) :
    for i in range(len(gr)) :
        gr[i] -= 0.1 

    return gr 
def change_pop(pop,gr) :
    gr = change_growth(gr) 
    for i in range(len(pop)) :
        pop[i] += gr[i]*pop[i] 

    return pop

def pop_after_n(pop,gr,n,initial) : 
    large =  initial
    year = 0
    for i in range(1,n) :
        change_pop(pop,gr) 
        if(curr_population(pop) > large) :
            large = curr_population
            year = i 
    for i in range(len(pop)) :
        print(pop[i],end=" ") 
    return [large,n]



def main() :
    pop = [50,1450,1400,1700,1500,600,1200]
    growth_rate = [2.5,2.1,1.7,1.3,0.9,0.5,0.1]

    initial = curr_population(pop) 
    # n = int(input("enter the value for n : ") ) 
    n = 5
    print()
    largest = pop_after_n(pop,growth_rate,n,initial)[0]
    no_of_years = pop_after_n(pop,growth_rate,n,initial)[1] 

    print(largest) 
    print(no_of_years) 



main()







from Domain.people import people

class addPeople:
    def addPeople(numberRandom):
        
        match numberRandom:
            case 1:
                return people("Abner", "833.151.870-53") 

            case 2:
                return people("Breno", "642.085.580-24")

            case 3:
                return people("Camila", "110.814.050-58")
            
            case 4:
                return people("David", "148.836.230-09")

            case 5:
                return people("Evandro", "515.510.380-05")

            case 6:
                return people("Fábio", "418.791.890-62")
            
            case 7:
                return people("Gabriel", "005.748.250-02")
            
            case 8:       
                return people("Higor", "903.768.480-73")
            
            case 9:
                return people("Ingrid", "929.089.430-00")
            
            case 10:
                return people("João", "006.632.820-98")
                
            case 11:
                return people("Katia", "937.967.880-09")

            case 12:
                return people("Lucas", "052.786.420-09")
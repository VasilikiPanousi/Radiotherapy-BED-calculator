#Radiotherapy BED Calculator & Treatment Comparison tool
#
#Υπολογισμός και σύγκριση βιολογικά ενεργού δόσης για εκπαιδευτικούς σκοπούς  
#
#Σημαντικές παρατηρήσεις: 
#1.Για σύγκριση BED στον ίδιο ιστό, πρέπει να χρησιμοποιούμε την ίδια τιμή α/β.
#2.Η μεγαλύτερη τιμή BED δεν σημαίνει αυτομάτως καλύτερη ή αποτελεσματικότερη θεραπεία.
#3.Το γραμμικό-τετραγωνικό μοντέλο έχει περιορισμούς στις πολύ υψηλές δόσεις ανά συνεδρία, όπως αυτές της στερεοτακτικής ακτινοχειρουργικής.
#
#
# _______BED=nd*(1+d/(a/b))_______
#
#d=δόση ανα συνεδρία
#n=αριθμός συνεδριών
#α/β=λόγος α/β του κάθε ιστού

#1. Ρωτάμε πρώτα τον χρήστη τι θέλει να κάνει: 1. να συγκρίνει διαφορετικά σχήματα για τον λιδιο ιστό ή 2. να συγκρίνει ένα σχήμα για 2 διαφορετικούς ιστούς ή 3. να είναι όλα διαφορετικά

print("BED Calculator")
print("Choose comparison mode:")
print("1. Compare different treatment schedules for the same tissue")
#Ο χρήστης επιλέγει έναν ιστό-Εισάγει το α/β μία φορά-Εισάγει διαφορετικά θεραπευτικά σχήματα-Το πρόγραμμα συγκρίνει τα BED.
print("2. Compare the same treatment schedule across different tissues")
#Ο χρήστης εισάγει ένα θεραπευτικό σχήμα-Επιλέγει όσους ιστούς θέλει-Εισάγει διαφορετικό α/β για κάθε ιστό-Το πρόγραμμα συγκρίνει τα BED.
print("3. Full comparison (different schedules and tissues)")
#Ο χρήστης εισάγει διαφορετικά θεραπευτικά σχήματα-μπορεί να επιλέξει διαφορετικό ιστό και διαφορετικό α/β-Το πρόγραμμα υπολογίζει και ταξινομεί όλα τα BED.


mode = input("Enter your choice (1, 2 or 3): ")

while mode not in ["1", "2", "3"]:
    mode = input("Invalid choice. Please enter 1, 2 or 3: ")

#Μετά ορίζω τη συνάρτηση BED μια φορά για να την έχω για όλα τα if 

def calculate_bed(dose_per_fraction, fractions, alpha_beta):
    bed = fractions*dose_per_fraction*(1+dose_per_fraction/alpha_beta)
    return bed

#δημιουργώ μια συνάρτηση που θα ζητάει έναν έγκυρο θετικό αριθμό για να την καλώ μετά όπου χρειάζομαι
# μια για δεκαδικούς και μια για ακεραιους

def get_positive_float(message):
    while True:
        try:
            number = float(input(message))
            if number > 0:
                return number
            else:
               print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_positive_int(message):
    while True:
        try:
            number = int(input(message))
            if number > 0:
                return number
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input! Please enter an integer.")


#____________________________________________________________________________________________________________________________________________________________________________
#ΙΔΙΟΣ ΙΣΤΟΣ - ΔΙΑΦΟΡΕΤΙΚΑ ΣΧΗΜΑΤΑ 
if mode == "1":
    tissue = input("Enter tissue name: ")

    ab = get_positive_float("Enter alpha/beta ratio for this tissue: ")

    number_of_treatments = get_positive_int("How many treatment schedules do you want to compare? ")

    
    while number_of_treatments <= 0:
     number_of_treatments = int(input("How many treatment schedules do you want to compare? Please enter a number above 0: "))

    dose_per_fraction = []
    fractions = []


    for i in range(number_of_treatments):
     dose = get_positive_float(f"Enter dose per fraction for treatment {i+1} (Gy): ")
     while dose <= 0:
       dose = float(input("Enter a valid positive dose: "))

     number = get_positive_int(f"Enter number of fractions for treatment {i+1}: ")
     while number <= 0:
       number = int(input("Enter a valid positive number of fractions: "))

     dose_per_fraction.append(dose)
     fractions.append(number)

    bed_results = []

    for i, (dose, number) in enumerate(zip(dose_per_fraction, fractions), start=1):
     result = calculate_bed(dose, number, ab)
     bed_results.append(result)
     print(f"BED for Treatment {i}: {result:.2f} Gy")


    treatments = list(range(1, number_of_treatments + 1))
    combined = list(zip(treatments, bed_results))
    sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)
    
    print(f"The highest BED is in Treatment {bed_results.index(max(bed_results))+1}, with a value of {max(bed_results):.2f} Gy")

    print("Treatments sorted from highest to lowest BED:")

    for treatment, bed in sorted_combined:
     print(f"Treatment {treatment} | Tissue: {tissue} | α/β: {ab} | BED: {bed:.2f} Gy")


#________________________________________________________________________________________________________________________________________________________________________________
#ΙΔΙΟ ΣΧΗΜΑ - ΔΙΑΦΟΡΕΤΙΚΟΙ ΙΣΤΟΙ
elif mode == "2":
    dose = get_positive_float("Enter dose per fraction (Gy): ")
    while dose <= 0:
        dose = float(input("Enter a valid positive dose: "))

    number = get_positive_int("Enter number of fractions: ")
    while number <= 0:
        number = int(input("Enter a valid positive number of fractions: "))

    tissues = []
    alpha_beta = []

    number_of_tissues = get_positive_int("How many tissues do you want to compare? ")

    while number_of_tissues <= 0:
        number_of_tissues = int(input("Please enter a number above 0: "))

    for i in range(number_of_tissues):
        tissue = input(f"Enter tissue {i+1}: ")

        ab = get_positive_float(f"Enter alpha/beta ratio for {tissue}: ")
        while ab <= 0:
            ab = float(input("Enter a valid positive alpha/beta ratio: "))

        tissues.append(tissue)
        alpha_beta.append(ab)

    bed_results = []

    for tissue, ab in zip(tissues, alpha_beta):
        result = calculate_bed(dose, number, ab)
        bed_results.append(result)
        print(f"BED for {tissue}: {result:.2f} Gy")

    combined = list(zip(tissues, alpha_beta, bed_results))

    sorted_combined = sorted(combined, key=lambda x: x[2], reverse=True)

    print("Tissues sorted from highest to lowest BED:")

    for tissue, ab, bed in sorted_combined:
        print(f"Tissue: {tissue} | α/β: {ab} | BED: {bed:.2f} Gy")  


#_____________________________________________________________________________________________________________________________________________________________________________________
# ΔΙΑΦΟΡΕΤΙΚΑ ΣΧΗΜΑΤΑ - ΔΙΑΦΟΡΕΤΙΚΟΙ ΙΣΤΟΙ 
elif mode == "3":
   
   number_of_treatments = get_positive_int("How many treatments do you want to compare? ")

   while number_of_treatments <= 0:
     number_of_treatments = int(input("How many treatments do you want to compare? Please enter a number above 0: "))

   dose_per_fraction = []
   fractions = []
   alpha_beta = []
   tissues = []

 # Φτιάχνω ένα for loop ώστε η σύγκριση να επαναλαμβάνεται ανάλογα με το πόσα σχήματα έχει γράψει οτι θέλει να συγκρίνει ο χρήστης στο number_of_tretaments
  ###### με το while επιβεβαιώνω οτι εάν δεν δώσει θετικούς αριθμούς θα του πω να ξανα δώσει σωστά τις τιμές 

   for i in range(number_of_treatments):
    dose = get_positive_float(f"Enter dose per fraction for treatment {i+1} (Gy): ")
    while dose <= 0:
       dose = float(input("Enter a valid positive dose: "))

    number = get_positive_int(f"Enter number of fractions for treatment {i+1}: ")
    while number <= 0:
       number = int(input("Enter a valid positive number of fractions: "))

    ab = get_positive_float(f"Enter alpha/beta for treatment {i+1}: ")
    while ab <= 0:
      ab = float(input("Enter a valid positive alpha/beta ratio: "))

    
    tissue = input(f"Enter tissue for treatment {i+1}: ")
    
 # Εαν ο χρήστης δώσει έγκυρους αριθμούς, αποθηκέυω τις τιμές με την εντολή append που προσθέτει μια τιμή στο τέλος μιας λίστας (ΜΕΣΑ ΣΤΟ FOR LOOP!)
    
    dose_per_fraction.append(dose)
    fractions.append(number)
    alpha_beta.append(ab)
    tissues.append(tissue)
 
 # Φτιάχνω μια κενή λίστα για τα αποτελέσματα του BED

    bed_results = []

 # Φτιάχνω το for loop 1. για να υπολογίζει κάθε φορά το κάθε σχήμα μόνο του και 2. για να γράφει και ποιό σχήμα είναι κάθε φορά

    for i, (dose, number, ab) in enumerate(zip(dose_per_fraction, fractions, alpha_beta), start=1):
        result = calculate_bed(dose, number, ab)
        bed_results.append(result)
        print(f"BED for Treatment {i}: {result:.2f} Gy")

    # Creating treatment numbers
    treatments = list(range(1, number_of_treatments + 1))

    # Combining the results
    combined = list(zip(treatments, bed_results, tissues, alpha_beta))

    # Sorting from highest to lowest BED
    sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)

    # Displaying the highest BED
    print(f"The highest BED is in Treatment {bed_results.index(max(bed_results))+1}, with a value of {max(bed_results):.2f} Gy")

    # Displaying sorted results
    print("Treatments sorted from highest to lowest BED:")

    for treatment, bed, tissue, ab in sorted_combined:
        print(f"Treatment {treatment} | Tissue: {tissue} | α/β: {ab} | BED: {bed:.2f} Gy")
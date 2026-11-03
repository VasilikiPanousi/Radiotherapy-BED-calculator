def calculate_bed(dose_per_fraction, fractions, alpha_beta):

    bed = fractions * dose_per_fraction * (
        1 + dose_per_fraction / alpha_beta
    )

    return bed


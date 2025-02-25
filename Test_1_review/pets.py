from warnings import catch_warnings

RAT = "RAT"
GUINEA_PIG = "GUINEA_PIG"
TARANTULA = "TARANTULA"
species_name ={ RAT: ["Lydian", "Elvira"], GUINEA_PIG: ["Egon"], TARANTULA: ["Freddie", "Katrina"] }


def swap_key_value(species_name: dict):
    name_species = {}
    try:
        for species, names in species_name.items():
            if  not isinstance(names, list):
                raise ValueError(f"Value for {species} is not a list")

            for i in range(len(names)):
                if names[i] in name_species:
                    raise ValueError(f"Duplicate pet name: {names[i]}")
                name_species[names[i]] = species

        return name_species
    except Exception as e:
        raise ValueError(f"Error during conversion: {str(e)}")



print(swap_key_value(species_name))
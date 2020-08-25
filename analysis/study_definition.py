from cohortextractor import StudyDefinition, patients, codelist

# Define some codelists
cardiac_disease_codes = codelist(["56265001", "127337006"], system="snomedct")
covid_codes = codelist(["U071", "U072"], system="icd10")

study = StudyDefinition(
    # Configure the expectations framework
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "exponential_increase",
    },

    # Define the study population
    population=patients.registered_with_one_practice_between(
        "2019-02-01", "2020-02-01"
    ),

    # Define input variables {
    age=patients.age_as_of(
        "2020-02-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),
    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),
    cardiac_disease=patients.with_these_clinical_events(
        cardiac_disease_codes,
        returning="binary_flag",
        return_expectations={"incidence": 0.2},
    ),
    # }

    # Define output variable
    covid_on_death_certificate=patients.with_these_codes_on_death_certificate(
        covid_codes,
        match_only_underlying_cause=False,
        return_expectations={"incidence": 0.001},
    ),
)

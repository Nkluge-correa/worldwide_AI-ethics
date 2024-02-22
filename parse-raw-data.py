import pandas as pd
import argparse
import json

# Mapping of principles to shorter names
PRINCIPLES = {'Accountability/Liability': 'Accountability',
 'Beneficence/Non-Maleficence': 'Beneficence',
 'Children & Adolescents Rights': "Children's Rights",
 'Dignity/Human Rights': 'Human Rights',
 'Diversity/Inclusion/Pluralism/Accessibility': 'Diversity',
 'Freedom/Autonomy/Democratic Values/Technological Sovereignty': "Autonomy",
 'Human Formation/Education': 'Human Formation',
 'Human-Centeredness/Alignment': 'Human-Centeredness',
 'Intellectual Property': 'Intellectual Property',
 'Justice/Equity/Fairness/Non-discrimination': 'Fairness',
 'Labor Rights': 'Labor Rights',
 'Open source/Fair Competition/Cooperation': 'Cooperation',
 'Privacy': 'Privacy',
 'Reliability/Safety/Security/Trustworthiness': 'Reliability',
 'Sustainability': 'Sustainability',
 'Transparency/Explainability/Auditability': 'Transparency',
 'Truthfulness': 'Truthfulness'
 }

def process_data(input_file, output_file):

    df = pd.read_parquet("data/data_raw.parquet")

    # Replace values in the `institution_type` column
    df['institution_type'] = df['institution_type'].apply(lambda x: x.replace("Civil Society Organization (CSO)/ Non-Governmental Organizaiton (NGO)", "NGO"))

    # Replace values in the `document_regulation` column
    df['document_regulation'] = df['document_regulation'].replace(
        {
        'Government-Regulation': 'Gov. Reg.',
        'Self-Regulation/Voluntary Self-Commitment': 'Self-Reg.',
        'Recommendation': 'Recommend.'
        }
    )

    # Replace values in the `document_normative` column
    df['document_normative'] = df['document_normative'].replace(
        {
        'Legally binding horizontal regulations': 'Binding',
        'Legally non-binding guidelines': 'Non-binding',
        'Legally non-binding guidelines, Legally binding horizontal regulations': 'Binding, Non-binding'
        }
    )

    # Replace values in the `document_impact` column
    df['document_impact'] = df['document_impact'].replace(
        {
        'Long-Termism': 'Long',
        'Short-Termism': 'Short',
        'Short-Termism & Long-Termism': 'Mid'
        }
    )

    # List to store processed data
    data = []

    # Iterating over each row in the DataFrame
    for i in range(len(df)):
        
        # Dictionary to store document attributes
        document = {}

        # Extracting and formatting document attributes
        document["document_name"] = df.iloc[i].document_name.strip().replace("\u200b", "").replace("\u2019", "'")
        document["country"] = df.iloc[i].country.strip() if "," not in df.iloc[i].country else [country.strip() for country in df.iloc[i].country.split(",")]
        document["world_region"] = df.iloc[i].world_region.strip() if "," not in df.iloc[i].world_region else [region.strip() for region in df.iloc[i].world_region.split(",")]
        document["institution"] = df.iloc[i].institution.strip()
        document["institution_type"] = df.iloc[i].institution_type.strip() if "," not in df.iloc[i].institution_type else [inst.strip() for inst in df.iloc[i].institution_type.split(",")]
        document["year_of_publication"] = df.iloc[i].year_of_publication
        document['number_of_male_authors'] = df.iloc[i].number_of_male_authors
        document['number_of_female_authors'] = df.iloc[i].number_of_female_authors
        document['document_size'] = df.iloc[i].document_size
        document['document_nature'] = df.iloc[i].document_nature.strip() if "," not in df.iloc[i].document_nature else [nature.strip() for nature in df.iloc[i].document_nature.split(",")]
        document['document_regulation'] = df.iloc[i].document_regulation
        document['document_normative'] = df.iloc[i].document_normative.strip() if "," not in df.iloc[i].document_normative else [norm.strip() for norm in df.iloc[i].document_normative.split(",")]
        document['document_impact'] = df.iloc[i].document_impact
        document['abstract'] = df.iloc[i].abstract.strip().replace("\u200b", "").replace("\u2019", "'")
        document['document_url'] = df.iloc[i].document_url.strip()
        if df.iloc[i].attachments != None:
            document['attachments'] = df.iloc[i].attachments.strip() if "," not in df.iloc[i].attachments else [attachment.strip() for attachment in df.iloc[i].attachments.split(",")]
        else:
            document['attachments'] = None

        # Categorizing documents based on principles
        document['principles'] = {}
        principles_in_document = [p.strip() for p in df.iloc[i].principles.split(",")]
        for p in PRINCIPLES.keys():
            if p in principles_in_document:
                document['principles'][PRINCIPLES[p]] = True
            else:
                document['principles'][PRINCIPLES[p]] = False
            
        # Extracting principles definitions
        document['principles_definition'] = {}
        principles_definition_in_document = [definition.strip().replace("\u200b", "").replace("\u2019", "'") for definition in df.iloc[i].principles_definition.split("#")[1:]]
        for p in PRINCIPLES:
            if p in principles_in_document:
                document['principles_definition'][PRINCIPLES[p]] = principles_definition_in_document[principles_in_document.index(p)].replace(p+":", "").strip()
            else:
                document['principles_definition'][PRINCIPLES[p]] = None
        
        # Appending processed document to the data list
        data.append(document)

    # Saving data list as a JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

def main():
    # Creating argument parser
    parser = argparse.ArgumentParser(description="Process Parquet file and save data as JSON")

    # Adding arguments
    parser.add_argument("--input", help="Input Parquet file", type=str, default="data/data_raw.parquet")
    parser.add_argument("--output", help="Output JSON file", type=str, default="data/data_processed.json")

    # Parsing arguments
    args = parser.parse_args()

    # Process data and save as JSON
    process_data(args.input, args.output)

if __name__ == "__main__":
    main()

# How to run this script:
# python parse-raw-data.py --input "data/data_raw.parquet" --output "data/data_processed.json"

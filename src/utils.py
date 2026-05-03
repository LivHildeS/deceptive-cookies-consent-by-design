import warnings

import pandas as pd

from src.get_constants import get_constants
from src.paths import SURVEY_PATH, SURVEY_QUESTIONS_PATH
from src.process_data import process_survey_data, process_participant_data

CONSTANTS = get_constants()


def write_survey_questions_to_file():
    """
    Writes the original questions to file, which are the original columns names in the survey file.
    """
    df = pd.read_excel(SURVEY_PATH)
    with open(SURVEY_QUESTIONS_PATH, "w") as outfile:
        for i, question in enumerate(df.columns):
            outfile.write(f"{i}: {question} \n")


def read_survey_data():
    """
    Reads the survey data and returns as a pandas dataframe.

    Returns:
        pd.DataFrame: The dataframe with the data.
    """
    with warnings.catch_warnings():  # Ignore warning about non standard formating in excel file
        warnings.filterwarnings("ignore", message="Workbook contains no default style")
        df = pd.read_excel(SURVEY_PATH)
    df = process_survey_data(df)

    return df


def read_participant_data():
    """
    Reads the experiment results and returns it as pandas DataFrame.

    Returns:
        pd: Dataframe with the experiment results.
    """
    return process_participant_data()


def get_all_data():
    """
    Reads and merges the survey data and the participant data.

    Returns:
        pd: Dataframe with the survey data and the experiment data.
    """
    survey_df = read_survey_data()
    participant_df = read_participant_data()
    df = pd.merge(survey_df, participant_df, left_on="submission_id", right_on="survey_id")
    return df

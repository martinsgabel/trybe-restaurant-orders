# from collections import Counter
from csv import reader


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file) as file:
            content = reader(file)
            data_medler(list(content))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def data_medler(file):
    # # general_set = set(file)
    # food_set = set(item[1] for item in file)
    # day_set = set(item[2] for item in file)
    # maria_data = []
    # arnaldo_data = []
    # joao_data = []

    # for item in file:
    #     if item[0] == 'maria':
    #         maria_data.append(item[1])
    #     if item[0] == 'arnaldo':
    #         arnaldo_data.append(item[1])
    #     if item[0] == 'joao':
    #         joao_data.append(item)

    # # maria
    # fav_by_maria = Counter(maria_data).most_common()[0][0]

    # # arnaldo
    # hamb_by_arnaldo = arnaldo_data.count("hamburger")

    # # joao
    # never_asked_joao = []
    # never_went_joao = []

    # for dish in food_set:
    #     if dish not in joao_data:
    #         never_asked_joao.append(dish)

    # for day in day_set:
    #     if day not in joao_data:
    #         never_went_joao.append(day)

    # res = (
    #     f"{fav_by_maria}\n"
    #     f"{hamb_by_arnaldo}\n"
    #     f"{never_asked_joao}\n"
    #     f"{never_went_joao}"
    # )

    # write(res)
    pass


def write(data):
    with open('data/mkt_campaign.txt', "w") as file:
        file.write(data)

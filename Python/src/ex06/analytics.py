import logging
import random
import config
import tg_config
import requests

logging.basicConfig(
    filename=config.log_file,
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class Research:
    def __init__(self, path):
        self.file = path
        logging.info(f"Research instance is initialiased,    Method: {Research.__name__}.{Research.__init__.__name__}")
    def file_reader(self, has_header=True):
        with open(self.file, "r") as f:
            lines = f.readlines()
            lines_to_print = []
            if not(lines[0].count('0') != 1 or lines[0].count('1') != 1 or lines[0].count(',') == 1):
                has_header = False
            for line in (lines[has_header:]):
                if not((line == "0,1\n") or (line == "1,0\n") or (line == "1,0") or (line == "1,0")):
                    logging.error(f"Not correct line format in the file,  Method: {Research.file_reader.__name__}")
                    raise ValueError("Not right input in file, should contain: \"0,1\" or \"1,0\"")
                lines_to_print.append([ int(line[0]) , int(line[2]) ])
        logging.info(f"File processing is completed with {len(lines[has_header:])},  Method: {Research.file_reader.__name__}")
        return lines_to_print
    def send_telegram_message(self, message):
        token = tg_config.TOKEN
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        channel_id = tg_config.CHANNEL_ID
        r = requests.post(url, data={
            "chat_id": channel_id,
            "text": message
            })
        if r.status_code == 200:
            print("The message has been successfully sent!")
        else:
            print("Failed to send message:", r.text)

class Calculations:
    def __init__(self, data):
        self.contest = data
        logging.info(f"Calculations instance is initialiased,   Method: {Calculations.__name__}.{Calculations.__init__.__name__}")
    def counts(self):
        heads = 0
        tails = 0
        logging.info(f"Counting heads and tails ...,  Method: {Calculations.counts.__name__}")
        for heads_tails in self.contest:
            heads += heads_tails[0]
            tails += heads_tails[1]
        logging.info("counts() has worked successfully")
        return (heads, tails)
    @staticmethod
    def fractions(heads, tails):
        logging.info(f"Counting posibilities ..., Method: {Calculations.fractions.__name__}")
        total = heads + tails
        logging.info(f"fractions() has worked successfully: {heads} * 100  heads {tails} * 100 tails,   Method: {Calculations.fractions.__name__}")
        return heads/total * 100, tails/total * 100

class Analitics(Calculations):
    @staticmethod
    def predict_random(predictions_num):
        predictions = []
        for _ in range(predictions_num):
            head = random.randint(0,1)
            tail = 1 - head
            logging.info(f"+1 predictions has been calculated and added successfully: {head} for heads and {tail} for tails, Method: {Analitics.predict_random.__name__}")
            predictions.append([head, tail])
        return predictions
    def predict_last(self):
        logging.info(f"Adding {self.contest[-1]} ...,   Method: {Analitics.predict_last.__name__}")
        return self.contest[-1]
    @staticmethod
    def save_file(data, name_of_file, extension="txt"):
        if extension != "txt":
            logging.error(f"Not correct format - {name_of_file}.{extension},    Method: {Analitics.save_file.__name__}")
            raise ValueError("only txt format!")
        with open(f"{name_of_file}.{extension}", 'w') as f:
            f.write(data)
            logging.info(f"Data has been successfully added to the {name_of_file}.{extension}: {data[:6]}...,   Method: {Analitics.save_file.__name__}")















import config
from analytics import Research, Calculations, Analitics
import sys

def main():
    """ выполняет основной скрипт для analytics.py"""
    if len(sys.argv) == config.num_arg_accepted:
        my_ins = Research(config.src_file)
        contest = my_ins.file_reader()
        # the counts from counts()
        c_ins = Calculations(contest)
        heads, tails = c_ins.counts()
        total = heads + tails
        # the fractions from fractions()
        freq_h, freq_t = Calculations.fractions(heads, tails)
        # the list of lists from predict_random() for the 3 steps
        experiments = Analitics.predict_random(config.num_of_steps)
        # the list from predict_last()
        a_ins = Analitics(contest)
        last_h, last_t = 0, 0
        for exp in experiments:
            last_t += exp[1]
            last_h += exp[0]
        # запись в файл
        Analitics.save_file(config.template.format(total, tails, heads, freq_t, freq_h,
                                                   config.num_of_steps, last_t, last_h),
                            config.res_file)


if __name__ == "__main__":
    main()
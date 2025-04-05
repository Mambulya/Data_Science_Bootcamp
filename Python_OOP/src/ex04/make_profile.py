#!/usr/bin/env python3
import cProfile
import pstats
import financial_enhanced as srcfile


if __name__ == "__main__":
    # профилирование
    profiler = cProfile.Profile()
    profiler.enable()

    # выполняется скрипт
    ticker, field = 'MSFT', 'Total Revenue'
    page_to_parse = srcfile.get_request(ticker)
    res_row = srcfile.parse_website(page_to_parse, field)
    print(res_row)

    profiler.disable()
    file_to_prof = "res.prof"
    file_report = "pstats-cumulative.txt"
    profiler.dump_stats(file_to_prof)

    # анализ профайлинга
    p = pstats.Stats(file_to_prof)
    with open(file_report, "w") as f:
        p.sort_stats('cumulative')
        p.stream = f
        p.print_stats(5)

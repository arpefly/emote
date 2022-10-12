from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from db import sql_worker


def make_chart(chat_id: int, timestamp_start: int, timestamp_end: int) -> bool:
    x_values = []
    y_values = []

    data = sql_worker.get_marks(chat_id, timestamp_start, timestamp_end)

    if len(data) < 2:
        return False

    start_date = sql_worker.get_datetime(timestamp_start)
    end_date = sql_worker.get_datetime(timestamp_end)

    for item in data:
        x_values.append(sql_worker.get_datetime(item[0]))
        y_values.append(item[1])

    fig = plt.figure(figsize=(len(x_values)/6 if len(x_values)/6 > 5 else 5, 5))
    ax = fig.add_subplot()

    fig.suptitle(f'Журнал настроения с {start_date.split(" ")[0]} по {end_date.split(" ")[0]}')
    plt.plot(x_values, y_values)

    plt.xlim(x_values[0], x_values[len(x_values) - 1])
    plt.xticks(rotation=90)

    plt.ylim(-0.5, 10.5)
    ax.yaxis.set_major_locator(MultipleLocator(base=1))

    ax.grid()
    plt.subplots_adjust(right=0.98, bottom=0.32, left=0.07)
    plt.savefig(f'charts/{chat_id}.png', dpi=200)

    return True

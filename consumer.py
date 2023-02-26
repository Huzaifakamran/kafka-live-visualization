import matplotlib.pyplot as plt
import numpy as np
from kafka import KafkaConsumer

plt.ion()

fig, ax = plt.subplots()
x = np.arange(0, 10)
y = np.zeros(10)

line, = ax.plot(x, y)

while True:
    consumer = KafkaConsumer('topic1', bootstrap_servers='localhost:9092')
    # print(list(consumer.poll(timeout_ms=1000).values())[-1][-1].value.decode('utf-8'))
    latest_value = int(list(consumer.poll(timeout_ms=1000).values())[-1][-1].value.decode('utf-8'))

    y = np.append(y[1:], latest_value)

    line.set_ydata(y)
    ax.relim()
    ax.autoscale_view(True, True, True)
    fig.canvas.draw()
    fig.canvas.flush_events()




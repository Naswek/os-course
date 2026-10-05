import statistics as st

seq = [0.02, 0.01, 0.01, 0.01, 0.02, 0.02, 0.01, 0.01, 0.02, 0.01]
rand = [0.15, 0.13, 0.12, 0.11, 0.11, 0.12, 0.11, 0.12, 0.12]

print("seq mean:", st.mean(seq))
print("seq s:", st.stdev(seq))

print("rand mean:", st.mean(rand))
print("rand s:", st.stdev(rand))

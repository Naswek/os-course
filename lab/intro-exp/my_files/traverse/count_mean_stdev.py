import statistics as st

seq = [26.67, 26.63, 26.65, 26.44, 26.31, 26.34, 26.29, 26.45, 26.47, 26.30]
rand = [26.16, 25.81, 25.92, 25.85, 25.88, 25.85, 25.85, 25.92, 25.85, 25.82]

print("seq mean:", st.mean(seq))
print("seq s:", st.stdev(seq))

print("rand mean:", st.mean(rand))
print("rand s:", st.stdev(rand))

def sliding_window_windows_count(N, C, W):
    s, e = 1, 1
    #decleartion of window
    window_sum = W[0]
    result = [0] * N
    result[0] = 1
#here are just cases if and else 
    while s <= N:
        if e + 1 <= N and window_sum + W[e] <= C:
            e += 1
            window_sum += W[e - 1]
        else:
            window_sum -= W[s - 1]
            s += 1

        if s <= e:
            for i in range(s - 1, e):
                result[i] += 1

    return result

#Here is input if N and C and a list W 
N, C = map(int, input().split())
W = list(map(int, input().split()))

#Calculate the number of different windows each element belongs to
result = sliding_window_windows_count(N, C, W)

#print the output
for count in result:
    print(count)

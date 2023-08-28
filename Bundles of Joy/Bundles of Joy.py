'''this fucntion that takes the best bundel with lower price.
T: An integer representing the number of test cases.
test_cases: A list of test cases, where each test case is a tuple containing:
n: An integer representing the total number of different items available.
m: An integer representing the number of available bundles.
bundles: A list of tuples, where each tuple contains:
price: The price of the bundle.
num_items: The number of items in the bundle.
items: A list of integers representing the items included in the bundle.'''
def min_cost_bundles(T, test_cases):
    results = []
    for i in range(T):
        n, m, bundles = test_cases[i]
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        
        for j in range(m):
            price, num_items, items = bundles[j]
            mask = 0
            for item in items:
                mask |= (1 << (item - 1))
            
            for k in range(1 << n):
                dp[k | mask] = min(dp[k | mask], dp[k] + price)
        
        results.append(dp[(1 << n) - 1])
    
    return results

# take the input of times of tests and bundels and the deserts.
T = int(input())
test_cases = []
for _ in range(T):
    n, m = map(int, input().split())
    bundles = []
    for _ in range(m):
        price, num_items, *items = map(int, input().split())
        bundles.append((price, num_items, items))
    test_cases.append((n, m, bundles))

#calculate and output the results
results = min_cost_bundles(T, test_cases)
for result in results:
    print(result)

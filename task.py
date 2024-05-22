import heapq

def connect_cables(cables):
    if cables is None or len(cables) == 0:
        return 0
    if len(cables) == 1:
        return cables[0]
    
    print("Processing...")
    heapq.heapify(cables)
    sum_length = 0
    while len(cables) > 1:
        new_cable = heapq.heappop(cables) + heapq.heappop(cables)
        sum_length += new_cable
        print(f"New cable: {new_cable}; Total length: {sum_length}")
        heapq.heappush(cables, new_cable)
    return sum_length

def main():
    cables = None
    print(f"Final cable for {cables}: {connect_cables(cables)}\n")

    cables = []
    print(f"Final cable for {cables}: {connect_cables(cables)}\n")

    cables = [13]
    print(f"Final cable for {cables}: {connect_cables(cables)}\n")

    cables = [13, 4, 1, 1, 1, 5]
    print(f"Final cable for {cables}: {connect_cables(cables)}\n")            

if __name__ == '__main__':
    main()
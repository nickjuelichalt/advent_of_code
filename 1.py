def main():
    with open("1.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

        start = 50
        answer = 0

        for i in range(0, len(lines)):
            direction = lines[i][0]
            distance = int(lines[i][1:])
            
            for _ in range(distance):
                if direction == "L":
                    start = (start - 1) % 100
                elif direction == "R":
                    start = (start + 1) % 100
                
                if start == 0:
                    answer += 1

            
        print(answer)

if __name__ == "__main__":
    main()

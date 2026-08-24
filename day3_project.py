log_status_codes: list = [200, 404, 200, 500, 200, 503, 200]
processed_logs: int = 0
caritical_erorrs: int = 0
for code in log_status_codes:
    if code == 404:
        print(f"[warning] status {code}: ressourse not found.")
        continue
    if code == 503:
        print(f"[critical] status {code}: service unavailable!")
        break
    if code == 500:
        print(f"[Erorr] status {code}: internal server error!")
        caritical_erorrs += 1
    elif code == 200:
        print(f"[success] status {code}: request processed smoothly!")

        processed_logs += 1

attempts: int = 0
max_attempts: int = 3
system_ready: bool = False
while attempts < max_attempts and not system_ready:
    attempts += 1
    user_input: str = input(f"attempt {attempts}/{max_attempts} - type 'ready' to start system: ") .strip()
    if user_input.upper() == "READY":
        system_ready = True
        print("system successfuly and running")
else:
    print("invalid command. try again")
if not system_ready:
    print("system initialization failed after maximum attempts")
row: int = 4
col: int = 4
for r in range(1, row +1):
    for c in range(1, col + 1):
        print(f"[node R{r}:C{c}] OK", end=" | ")
        print()

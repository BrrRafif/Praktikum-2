def cek_fsm(s):
    state = 'S'
    history = ['S']
    alasan = ""
    output_lines = []

    for i, c in enumerate(s):
        if c not in ['0', '1']:
          return "Input tidak valid"

        if state == 'S':
            state = 'A' if c == '0' else 'B'

        elif state == 'A':
            if c == '0':
                state = 'C'
                alasan = "mengandung substring '00'\n"
            else:
                state = 'B'

        elif state == 'B':
            state = 'A' if c == '0' else 'B'

        elif state == 'C':
            state = 'C'

        history.append(state)

    output_lines.append("\nTRACE FSM:")
    output_lines.append(" -> ".join(history))

    if state == 'B':
        output_lines.append("DITERIMA\n")
    else:
        output_lines.append("DITOLAK")
        if alasan:
            output_lines.append(f"Alasan: {alasan}")
        elif s and s[-1] != '1':
            output_lines.append("Alasan: tidak berakhir dengan '1'\n")

    return "\n".join(output_lines)


# UI
while True:
    s = input("Masukkan string (0 dan 1): ")
    result = cek_fsm(s)

    print(result)

    if "Input tidak valid" in result:
        break

    ulang = input("Ulangi? (y/n): ")

    if ulang.lower() == 'y':
        continue
    elif ulang.lower() == 'n':
        print("Program berhenti")
        break
    else:
        print("inputan gagal")
        break
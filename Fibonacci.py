if __name__ == "_main_":
    with open('morse.in') as entrada:
        with open('morse.out','w') as saida:
            morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

            linhas = entrada.readlines()

            for linha in linhas:
                temp = linha.rstrip('\n').split(" ")  
                palavra = ""

                for t in temp:    
                    cont = 0        

                    for p in morse:
                        if (t == p):
                            palavra += chr(65 + cont)  
                            break                  
                        cont += 1
                saida.write(palavra+'\n')
                if (linha == '..-. .. --'):
                    break
            entrada.close
            saida.close